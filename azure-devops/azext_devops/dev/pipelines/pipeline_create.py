# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import tempfile
import os
from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt
from azext_devops.dev.common.services import (get_new_pipeline_client, get_new_cix_client, get_git_client,
                                              resolve_instance_and_project, resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_parse
from azext_devops.dev.common.utils import open_file, delete_dir
from azext_devops.dev.common.git import get_remote_url, get_current_branch_name
from azext_devops.dev.common.arguments import should_detect
from azext_devops.dev.common.prompting import (prompt_user_friendly_choice_list,
                                               verify_is_a_tty_or_raise_error,
                                               prompt_not_empty)
from azext_devops.dev.pipelines.pipeline_create_helpers.github_api_helper import (
    push_files_github, get_github_repos_api_url, Files)
from azext_devops.dev.pipelines.pipeline_create_helpers.pipelines_resource_provider import (
    get_azure_rm_service_connection, get_azure_rm_service_connection_id, get_github_service_endpoint,
    get_kubernetes_environment_resource, get_container_registry_service_connection, get_webapp_from_list_selection)
from azext_devops.dev.pipelines.pipeline_create_helpers.azure_repos_helper import push_files_to_azure_repo
from azext_devops.devops_sdk.v5_1.build.models import Build, BuildDefinition, BuildRepository, AgentPoolQueue
from .build_definition import fix_path_for_api

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class YmlOptions:
    def __init__(self, name, id, content, description='Custom yaml', params=None, path=None, assets=None):  # pylint: disable=redefined-builtin
        self.name = name
        self.id = id
        self.description = description
        self.content = content
        self.path = path
        self.params = params
        self.assets = assets


_GITHUB_REPO_TYPE = 'github'
_AZURE_GIT_REPO_TYPE = 'TfsGit'
_GITHUBENTERPRISE_REPO_TYPE = 'githubenterprise'


# pylint: disable=too-many-statements
def pipeline_create(name, description=None, repository=None, branch=None, yml_path=None, repository_type=None,
                    service_connection=None, organization=None, project=None, detect=None, queue_id=None,
                    skip_first_run=None, folder_path=None):
    """Create a new Azure Pipeline (YAML based)
    :param name: Name of the new pipeline
    :type name: str
    :param description: Description for the new pipeline
    :type description: str
    :param repository: Repository for which the pipeline needs to be configured.
    Can be clone url of the git repository or name of the repository for a Azure Repos
    or Owner/RepoName in case of GitHub repository.
    If omitted it will be auto-detected from the remote url of local git repository.
    If name is mentioned instead of url, --repository-type argument is also required.
    :type repository: str
    :param branch: Branch name for which the pipeline will be configured. If omitted, it will be auto-detected
    from local repository
    :type branch: str
    :param yml_path: Path of the pipelines yaml file in the repo (if yaml is already present in the repo).
    :type yml_path: str
    :param repository_type: Type of repository. If omitted, it will be auto-detected from remote url
    of local repository. 'tfsgit' for Azure Repos, 'github' for GitHub repository.
    :type repository_type: str
    :param service_connection: Id of the Service connection created for the repository for GitHub repository.
    Use command az devops service-endpoint -h for creating/listing service_connections. Not required for Azure Repos.
    :type service_connection: str
    :param queue_id: Id of the queue in the available agent pools. Will be auto detected if not specified.
    :type queue_id: str
    :param skip_first_run: Specify this flag to prevent the first run being triggered by the command.
    Command will return a pipeline if run is skipped else it will output a pipeline run.
    :type skip_first_run: bool
    :param folder_path: Path of the folder where the pipeline needs to be created. Default is root folder.
    e.g. "user1/test_pipelines"
    :type folder_path: str
    """
    repository_name = None
    if repository:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
    else:
        organization, project, repository_name = resolve_instance_project_and_repo(
            detect=detect, organization=organization, project=project)
    # resolve repository if local repo for azure repo
    if repository_name:
        repository = repository_name
        repository_type = _AZURE_GIT_REPO_TYPE
    # resolve repository from local repo for github repo
    if not repository:
        repository = _get_repository_url_from_local_repo(detect=detect)
    if not repository:
        raise CLIError('The following arguments are required: --repository.')
    if not repository_type:
        repository_type = try_get_repository_type(repository)
    if not repository_type:
        raise CLIError('The following arguments are required: --repository-type. '
                       'Check command help for valid values.')
    if not branch and should_detect(detect):
        branch = get_current_branch_name()
    if not branch:
        raise CLIError('The following arguments are required: --branch.')
    # repository, repository-type, branch should be set by now
    if not repository_name and is_valid_url(repository):
        repository_name = _get_repo_name_from_repo_url(repository, repository_type)

    if not repository_name and repository_type.lower() == _GITHUBENTERPRISE_REPO_TYPE:
        repository_name = _get_repo_name_from_repo_url(repository, repository_type)
    else:
        repository_name = repository

    # Validate name availability so user does not face name conflicts after going through the whole process
    if not validate_name_is_available(name, folder_path, organization, project):
        raise CLIError('Pipeline with name {name} already exists.'.format(name=name))

    # Parse repository information according to repository type
    repo_id = None
    api_url = None
    repository_url = None
    if repository_type.lower() == _GITHUB_REPO_TYPE:
        repo_id = repository_name
        repository_url = 'https://github.com/' + repository_name
        api_url = get_github_repos_api_url(repository_name)
    if repository_type.lower() == _GITHUBENTERPRISE_REPO_TYPE:
        repo_id = repository_name
        repository_url = repository
        ghe_url = uri_parse(repository_url)
        api_url = ghe_url.scheme + '://' + ghe_url.netloc + '/api/v3/repos/' + repository_name

    if repository_type.lower() == _AZURE_GIT_REPO_TYPE.lower():
        repo_id = _get_repository_id_from_name(organization, project, repository_name)

    if not service_connection and repository_type.lower() != _AZURE_GIT_REPO_TYPE.lower():
        service_connection = get_github_service_endpoint(organization, project)

    new_cix_client = get_new_cix_client(organization=organization)
    # No yml path => find or recommend yml scenario
    queue_branch = branch
    if not yml_path:
        if repository_type.lower() == _GITHUBENTERPRISE_REPO_TYPE:
            raise CLIError('The following arguments are required for GitHub Enterprise: --yaml-path.')
        yml_path, queue_branch = _create_and_get_yml_path(new_cix_client, repository_type, repo_id,
                                                          repository_name, branch, service_connection, project,
                                                          organization)
    if not queue_id:
        queue_id = _get_agent_queue_by_heuristic(organization=organization, project=project)
        if queue_id is None:
            logger.warning('Cannot find a hosted pool queue in the project. Provide a --queue-id in command params.')

    # Create build definition
    definition = _create_pipeline_build_object(name, description, repo_id, repository_name, repository_url, api_url,
                                               branch, service_connection, repository_type, yml_path, queue_id,
                                               folder_path)
    client = get_new_pipeline_client(organization)
    created_definition = client.create_definition(definition=definition, project=project)
    logger.warning('Successfully created a pipeline with Name: %s, Id: %s.',
                   created_definition.name, created_definition.id)
    if skip_first_run:
        return created_definition
    return client.queue_build(build=Build(definition=created_definition, source_branch=queue_branch),
                              project=project)


def pipeline_update(id, description=None, new_name=None,  # pylint: disable=redefined-builtin
                    branch=None, yml_path=None, queue_id=None, organization=None, project=None, detect=None,
                    new_folder_path=None):
    """Update a pipeline
    :param id: Id of the pipeline to update.
    :type id: str
    :param new_name: New updated name of the pipeline.
    :type new_name: str
    :param description: New description for the pipeline.
    :type description: str
    :param branch: Branch name for which the pipeline will be configured.
    :type branch: str
    :param yml_path: Path of the pipelines yaml file in the repo.
    :type yml_path: str
    :param queue_id: Queue id of the agent pool where the pipeline needs to run.
    :type queue_id: int
    :param new_folder_path: New full path of the folder to move the pipeline to.
    e.g. "user1/production_pipelines"
    :type new_folder_path: str
    """
    # pylint: disable=too-many-branches
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    pipeline_client = get_new_pipeline_client(organization=organization)
    definition = pipeline_client.get_definition(definition_id=id, project=project)
    if new_name:
        definition.name = new_name
    if description:
        definition.description = description
    if branch:
        definition.repository.default_branch = branch
    if queue_id:
        definition.queue = AgentPoolQueue()
        definition.queue.id = queue_id
    if yml_path:
        definition.process = _create_process_object(yml_path)
    if new_folder_path:
        definition.path = new_folder_path
    return pipeline_client.update_definition(project=project, definition_id=id, definition=definition)


def validate_name_is_available(name, path, organization, project):
    client = get_new_pipeline_client(organization=organization)
    path = fix_path_for_api(path)
    definition_references = client.get_definitions(project=project, name=name, path=path)
    if len(definition_references.value) == 0:
        return True
    return False


def _get_repository_url_from_local_repo(detect):
    if should_detect(detect):
        return get_remote_url(is_github_url_candidate)
    return None


def is_github_url_candidate(url):
    if url is None:
        return False
    components = uri_parse(url.lower())
    if components.netloc == 'github.com':
        return True
    return False


def is_valid_url(url):
    if ('github.com' in url or 'visualstudio.com' in url or 'dev.azure.com' in url):
        return True
    return False


def _get_repo_name_from_repo_url(repository_url, repo_type):
    """
    Should be called with a valid github or azure repo url
    returns owner/reponame for github repos, repo_name for azure repo type
    """
    if repo_type.lower() == _GITHUB_REPO_TYPE:
        parsed_url = uri_parse(repository_url)
        logger.debug('Parsing GitHub url: %s', parsed_url)
        if parsed_url.scheme == 'https' and parsed_url.netloc == 'github.com':
            logger.debug('Parsing path in the url to find repo id.')
            stripped_path = parsed_url.path.strip('/')
            if stripped_path.endswith('.git'):
                stripped_path = stripped_path[:-4]
            return stripped_path
    if repo_type.lower() == _AZURE_GIT_REPO_TYPE:
        parsed_list = repository_url.split('/')
        index = 0
        for item in parsed_list:
            if ('visualstudio.com' in item or 'dev.azure.com' in item) and len(parsed_list) > index + 4:
                return parsed_list[index + 4]
            index = index + 1
    if repo_type.lower() == _GITHUBENTERPRISE_REPO_TYPE:
        parsed_url = uri_parse(repository_url)
        logger.debug('Parsing GitHubEnterprise url: %s', parsed_url)
        stripped_path = parsed_url.path.strip('/')
        if stripped_path.endswith('.git'):
            stripped_path = stripped_path[:-4]
        parts = stripped_path.split('/')
        return parts[-2] + '/' + parts[-1]

    raise CLIError('Could not parse repository url.')


def _create_repo_properties_object(service_endpoint, branch, api_url):
    return {
        "connectedServiceId": service_endpoint,
        "defaultBranch": branch,
        "apiUrl": api_url
    }


def _create_process_object(yaml_path):
    return {
        "yamlFilename": yaml_path,
        "type": 2
    }


def try_get_repository_type(url):
    if 'https://github.com' in url:
        return _GITHUB_REPO_TYPE
    if 'dev.azure.com' in url or '.visualstudio.com' in url:
        return _AZURE_GIT_REPO_TYPE
    return None


def _create_and_get_yml_path(cix_client, repository_type, repo_id, repo_name, branch,  # pylint: disable=too-many-locals, too-many-statements
                             service_endpoint, project, organization):
    logger.debug('No yaml file was given. Trying to find the yaml file in the repo.')
    queue_branch = branch
    default_yml_exists = False
    yml_names = []
    yml_options = []
    configurations = cix_client.get_configurations(
        project=project, repository_type=repository_type,
        repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
    for configuration in configurations:
        if configuration.path.strip('/') == 'azure-pipelines.yml':
            default_yml_exists = True
        logger.debug('The repo has a yaml pipeline definition. Path: %s', configuration.path)
        custom_name = 'Existing yaml (path={})'.format(configuration.path)
        yml_names.append(custom_name)
        yml_options.append(YmlOptions(name=custom_name, content=configuration.content, id='customid',
                                      path=configuration.path))

    recommendations = cix_client.get_template_recommendations(
        project=project, repository_type=repository_type,
        repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
    logger.debug('List of recommended templates..')
    # sort recommendations
    from operator import attrgetter
    recommendations = sorted(recommendations, key=attrgetter('recommended_weight'), reverse=True)
    for recommendation in recommendations:
        yml_names.append(recommendation.name)
        yml_options.append(YmlOptions(name=recommendation.name, content=recommendation.content,
                                      id=recommendation.id, description=recommendation.description,
                                      params=recommendation.parameters, assets=recommendation.assets))
    temp_filename = None
    files = []
    yml_selection_index = 0
    proceed_selection = 1
    while proceed_selection == 1:
        proceed_selection = 0
        # Clear files since user can change the template now
        del files[:]
        yml_selection_index = prompt_user_friendly_choice_list("Which template do you want to use for this pipeline?",
                                                               yml_names)
        if yml_options[yml_selection_index].params:
            yml_options[yml_selection_index].content, yml_options[yml_selection_index].assets = _handle_yml_props(
                params_required=yml_options[yml_selection_index].params,
                template_id=yml_options[yml_selection_index].id,
                cix_client=cix_client, repo_name=repo_name, organization=organization, project=project)
        temp_dir = tempfile.mkdtemp(prefix='AzurePipelines_')
        temp_filename = os.path.join(temp_dir, 'azure-pipelines.yml')
        f = open(temp_filename, mode='w')
        f.write(yml_options[yml_selection_index].content)
        f.close()
        assets = yml_options[yml_selection_index].assets
        if assets:
            for asset in assets:
                files.append(Files(asset.destination_path, asset.content))
        view_choice = prompt_user_friendly_choice_list(
            'Do you want to view/edit the template yaml before proceeding?',
            ['Continue with generated yaml', 'View or edit the yaml'])
        if view_choice == 1:
            open_file(temp_filename)
            proceed_selection = prompt_user_friendly_choice_list(
                'Do you want to proceed creating a pipeline?',
                ['Proceed with this yaml', 'Choose another template'])
    # Read updated data from the file
    f = open(temp_filename, mode='r')
    content = f.read()
    f.close()
    delete_dir(temp_dir)
    checkin_path = 'azure-pipelines.yml'
    if default_yml_exists and not yml_options[yml_selection_index].path:  # We need yml path from user
        logger.warning('A yaml file azure-pipelines.yml already exists in the repository root.')
        checkin_path = prompt_not_empty(
            msg='Enter a yaml file path to checkin the new pipeline yaml in the repository? ',
            help_string='e.g. /new_azure-pipeline.yml to add in the root folder.')
        print('')
    files.append(Files(checkin_path, content))
    print('Files to be added to your repository ({numfiles})'.format(numfiles=len(files)))
    count_file = 1
    for file in files:
        print('{index}) {file}'.format(index=count_file, file=file.path))
        count_file = count_file + 1
    print('')
    if default_yml_exists and checkin_path.strip('/') == 'azure-pipelines.yml':
        print('Edits on the existing yaml can be done in the code repository.')
    else:
        queue_branch = push_files_to_repository(organization, project, repo_name, branch, files, repository_type)
    return checkin_path, queue_branch


def push_files_to_repository(organization, project, repo_name, branch, files, repository_type):
    commit_strategy_choice_list = ['Commit directly to the {branch} branch.'.format(branch=branch),
                                   'Create a new branch for this commit and start a pull request.']
    commit_choice = prompt_user_friendly_choice_list("How do you want to commit the files to the repository?",
                                                     commit_strategy_choice_list)
    commit_direct_to_branch = commit_choice == 0
    if repository_type == _GITHUB_REPO_TYPE:
        return push_files_github(files, repo_name, branch, commit_direct_to_branch)
    if repository_type.lower() == _AZURE_GIT_REPO_TYPE.lower():
        return push_files_to_azure_repo(files, repo_name, branch, commit_direct_to_branch, organization, project)
    raise CLIError('File push failed: Repository type not supported.')


def _get_pipelines_trigger(repo_type):
    if repo_type.lower() == _GITHUB_REPO_TYPE or repo_type.lower() == _GITHUBENTERPRISE_REPO_TYPE:
        return [{"settingsSourceType": 2, "triggerType": 2},
                {"forks": {"enabled": "true", "allowSecrets": "false"},
                 "settingsSourceType": 2, "triggerType": "pullRequest"}]
    return [{"settingsSourceType": 2, "triggerType": 2}]


def _handle_yml_props(params_required, template_id, cix_client, repo_name, organization, project):
    logger.warning('The template requires a few inputs. We will help you fill them out')
    params_to_render = {}
    for param in params_required:
        param_name_for_user = param.name
        # override with more user friendly name if available
        if param.display_name:
            param_name_for_user = param.display_name
        logger.debug('Looking for param %s in props', param.name)
        prop_found = False
        if param.default_value:
            prop_found = True
            user_input_val = prompt(msg='Enter a value for {param_name} [Press Enter for default: {param_default}]:'
                                    .format(param_name=param_name_for_user, param_default=param.default_value))
            print('')
            if user_input_val:
                params_to_render[param.name] = user_input_val
            else:
                params_to_render[param.name] = param.default_value
        elif _is_intelligent_handling_enabled_for_prop_type(prop_name=param.name, prop_type=param.type):
            logger.debug('This property is handled intelligently (Name: %s) (Type: %s)', param.name, param.type)
            fetched_value = fetch_yaml_prop_intelligently(param.name, param.type, organization, project, repo_name)
            if fetched_value is not None:
                logger.debug('Auto filling param %s with value %s', param.name, fetched_value)
                params_to_render[param.name] = fetched_value
                prop_found = True
        if not prop_found:
            input_value = _prompt_for_prop_input(param_name_for_user, param.type)
            params_to_render[param.name] = input_value
            prop_found = True
    rendered_template = cix_client.render_template(template_id=template_id,
                                                   template_parameters={'tokens': params_to_render})
    return rendered_template.content, rendered_template.assets


def fetch_yaml_prop_intelligently(prop_name, prop_type, organization, project, repo_name):
    if prop_type.lower() == 'endpoint:azurerm':
        return get_azure_rm_service_connection(organization, project)
    if prop_type.lower() == 'connectedservice:azurerm':
        return get_azure_rm_service_connection_id(organization, project)
    if prop_type.lower() == 'environmentresource:kubernetes':
        return get_kubernetes_environment_resource(organization, project, repo_name)
    if prop_type.lower() == 'endpoint:containerregistry':
        return get_container_registry_service_connection(organization, project)
    if prop_name.lower() == 'webappname':
        return get_webapp_from_list_selection()
    return None


def _is_intelligent_handling_enabled_for_prop_type(prop_name, prop_type):
    SMART_HANDLING_FOR_PROP_TYPES = ['connectedservice:azurerm',
                                     'endpoint:azurerm',
                                     'environmentresource:kubernetes',
                                     'endpoint:containerregistry']
    SMART_HANDLING_FOR_PROP_NAMES = ['webappname']
    if prop_type.lower() in SMART_HANDLING_FOR_PROP_TYPES:
        return True
    if prop_name.lower() in SMART_HANDLING_FOR_PROP_NAMES:
        return True
    return False


def _prompt_for_prop_input(prop_name, prop_type):
    verify_is_a_tty_or_raise_error('The template requires a few inputs. These cannot be provided as in command '
                                   'arguments. It can only be input interatively.')
    val = prompt(msg='Please enter a value for {prop_name}: '.format(prop_name=prop_name),
                 help_string='Value of type {prop_type} is required.'.format(prop_type=prop_type))
    print('')
    return val


def _create_pipeline_build_object(name, description, repo_id, repo_name, repository_url, api_url, branch,
                                  service_endpoint, repository_type, yml_path, queue_id, path):
    definition = BuildDefinition()
    definition.name = name
    if description:
        definition.description = description
    # Set build repo
    definition.repository = BuildRepository()
    if repo_id:
        definition.repository.id = repo_id
    if repo_name:
        definition.repository.name = repo_name
    if repository_url:
        definition.repository.url = repository_url
    if branch:
        definition.repository.default_branch = branch
    if service_endpoint:
        definition.repository.properties = _create_repo_properties_object(service_endpoint, branch, api_url)
    if path:
        definition.path = path
    # Hack to avoid the case sensitive GitHub type for service hooks.
    if repository_type.lower() == _GITHUB_REPO_TYPE:
        definition.repository.type = 'GitHub'
    else:
        definition.repository.type = repository_type
    # Set build process
    definition.process = _create_process_object(yml_path)
    # set agent queue
    definition.queue = AgentPoolQueue()
    definition.triggers = _get_pipelines_trigger(repository_type)
    if queue_id:
        definition.queue.id = queue_id
    return definition


def _get_repository_id_from_name(organization, project, repository):
    git_client = get_git_client(organization)
    repository = git_client.get_repository(project=project, repository_id=repository)
    return repository.id


def _get_agent_queue_by_heuristic(organization, project):
    """
    Tries to detect a queue in the agent pool in a project
    Returns id of Hosted Ubuntu 16.04, first hosted pool queue, first queue in that order
    None if no queues are returned
    """
    from azext_devops.dev.common.services import get_new_task_agent_client
    choosen_queue = None
    agent_client = get_new_task_agent_client(organization=organization)
    queues = agent_client.get_agent_queues(project=project)
    if queues:
        choosen_queue = queues[0]
        found_first_hosted_pool_queue = False
        for queue in queues:
            if queue.name == 'Hosted Ubuntu 1604':
                choosen_queue = queue
                break
            if not found_first_hosted_pool_queue and queue.pool.is_hosted:
                choosen_queue = queue
                found_first_hosted_pool_queue = True
        logger.debug('Auto detecting agent pool. Queue: %s, Pool: %s', choosen_queue.name, choosen_queue.pool.name)
        return choosen_queue.id
    return None
