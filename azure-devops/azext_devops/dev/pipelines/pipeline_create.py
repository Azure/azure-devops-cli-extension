# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import tempfile
import os
from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt
from azext_devops.dev.common.services import (get_new_pipeline_client,
                                              get_new_cix_client,
                                              get_git_client,
                                              get_service_endpoint_client,
                                              get_default_subscription_info,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_parse
from azext_devops.dev.common.utils import open_file, delete_dir
from azext_devops.dev.common.git import get_remote_url, get_current_branch_name, resolve_git_ref_heads
from azext_devops.dev.common.arguments import should_detect
from azext_devops.dev.common.prompting import (prompt_user_friendly_choice_list,
                                               verify_is_a_tty_or_raise_error)
from azext_devops.devops_sdk.v5_1.build.models import (Build, BuildDefinition,
                                                       BuildRepository, AgentPoolQueue)
from azext_devops.devops_sdk.v5_1.service_endpoint.models import ServiceEndpoint, EndpointAuthorization
from .build_definition import get_definition_id_from_name
from .github_api_helper import get_github_pat_token, push_files_github, get_github_repos_api_url, Files

logger = get_logger(__name__)

# pylint: disable=too-few-public-methods
class YmlOptions:
    def __init__(self, name, id, content, description='Custom yml', params=None, path=None, assets=None):  # pylint: disable=redefined-builtin
        self.name = name
        self.id = id
        self.description = description
        self.content = content
        self.path = path
        self.params = params
        self.assets = assets

_GITHUB_REPO_TYPE = 'github'
_AZURE_GIT_REPO_TYPE = 'tfsgit'

def pipeline_create(name, description=None, repository_name=None, repository_url=None, branch=None, yml_path=None,
                    repository_type=None, service_connection=None,
                    organization=None, project=None, detect=None, queue_id=None):
    """Create a pipeline
    :param name: Name of the new pipeline
    :type name: str
    :param description: Description for the new pipeline
    :type description: str
    :param repository_url: Repository clone url for which the pipeline will be configured. If omitted along with
    --repository-name and --repository-type, it will be auto-detected from the git remote url of local repository.
    :type repository_url: str
    :param repository_name: Name of the repository for a Azure Devops repository or owner/reponame
    in case of GitHub Repo. --repository-type argument is required with this.
    Ignored if --repository-url is supplied
    :type repository_name: str
    :param branch: Branch name for which the pipeline will be configured. If omitted, it will be auto-detected
    from local repository
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo (if yml is already present in the repo).
    :type yml_path: str
    :param repository_type: Type of repository. If omitted, it will be auto-detected from remote url
    of local repository. 'tfsgit' for Azure Repos, 'github' for GitHub repository.
    :type repository_type: str
    :param service_connection: Id of the Service connection created for the repository.
    Use command az devops service-endpoint -h for creating/listing service_connections.
    :type service_connection: str
    :param queue_id: Id of the queue in the available agent pools. Will be auto detected if not specified.
    :type queue_id: str
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect, organization=organization, project=project, repo=repository_name)
    if not validate_name_is_available(name, organization, project):
        raise CLIError('Pipeline with name {name} already exists.'.format(name=name))
    if not repository_url and not repository:
        repository_url = _get_repository_url_from_local_repo(detect=detect)
    if not branch and should_detect(detect):
        branch = get_current_branch_name()
    if not repository_type:
        if repository_url:
            repository_type = try_get_repository_type(repository_url)
        elif repository:
            repository_type = _AZURE_GIT_REPO_TYPE
        if not repository_type:
            raise CLIError("--repository-url or --repository-type must be specified.")
    else:
        repository_type = repository_type.lower()

    if not repository_url or not branch:
        if (not repository and not repository_name) or not repository_type or not branch:
            raise CLIError("Either --repository-url and --branch OR "\
                        "--repository-name, --repository-type and --branch must be specified.")

    # Parse repository information according to repository type
    repo_name = None
    repo_id = None
    api_url = None
    if repository_type.lower() == _GITHUB_REPO_TYPE:
        if repository_url:
            repo_id = _get_repo_id_from_repo_url(repository_url)
            repo_name = repo_id
        else:
            repo_name = repository_name
            repo_id = repository_name
            repository_url = 'https://github.com/' + repo_name
        api_url = get_github_repos_api_url(repo_id)
    if repository_type.lower() == _AZURE_GIT_REPO_TYPE:
        repo_name = repository_name
        repo_id = _get_repository_id_from_name(organization, project, repository)

    if not service_connection and repository_type != _AZURE_GIT_REPO_TYPE:
        service_connection = get_github_service_endpoint(organization, project)

    new_cix_client = get_new_cix_client(organization=organization)
    # No yml path => find or recommend yml scenario
    if not yml_path:
        yml_path = _create_and_get_yml_path(new_cix_client, repository_type, repo_id, repo_name, branch,
                                            service_connection, project, organization)
    if not queue_id:
        queue_id = _get_agent_queue_by_heuristic(organization=organization, project=project)
        if queue_id is None:
            logger.warning('Cannot find a hosted pool queue in the project. Provide a --queue-id in command params.')

    # Create build definition
    definition = _create_pipeline_build_object(name, description, repo_id, repo_name, repository_url, api_url, branch,
                                               service_connection, repository_type, yml_path, queue_id)
    client = get_new_pipeline_client(organization)
    created_definition = client.create_definition(definition=definition, project=project)
    logger.warning('Successfully created a pipeline with Name: %s, Id: %s.',
                   created_definition.name, created_definition.id)
    return client.queue_build(build=Build(definition=created_definition), project=project)


def pipeline_update(name=None, id=None, description=None, new_name=None, repository_url=None,  # pylint: disable=redefined-builtin
                    branch=None, yml_path=None, repository_type=None, service_connection=None, queue_id=None,
                    repository_name=None, organization=None, project=None, detect=None):
    """Update a pipeline
    :param name: Name of the pipeline to update.
    :type name: str
    :param id: Id of the pipeline to update.
    :type id: str
    :param new_name: New updated name of the pipeline.
    :type new_name: str
    :param description: Description to be updated for the pipeline.
    :type description: str
    :param repository_url: Repository clone url for which the pipeline will be configured.
    :type repository_url: str
    :param repository_name: Repository name for which the pipeline is to be setup.
    --repository-type should also be provided with this.
    :type repository_name: str
    :param repository_type: Type of repository.
    :type repository_type: str
    :param branch: Branch name for which the pipeline will be configured.
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo.
    :type yml_path: str
    :param queue_id: Queue id of the agent pool where the pipeline needs to run.
    :type queue_id: int
    :param service_connection: Id of the service connection for pipelines to connect to the repository.
    Use command az devops service-endpoint -h for creating/listing service-connections.
    :type service_connection: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    """
    # pylint: disable=too-many-branches
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect, organization=organization, project=project, repo=repository_name)
    pipeline_client = get_new_pipeline_client(organization=organization)
    if id is None:
        if name is not None:
            id = get_definition_id_from_name(name, pipeline_client, project)
        else:
            raise CLIError("Either the --id argument or the --name argument must be supplied for this command.")
    if not repository_type:
        if repository_url:
            repository_type = try_get_repository_type(repository_url)
        elif repository:
            repository_type = _AZURE_GIT_REPO_TYPE
    else:
        repository_type = repository_type.lower()
    repo_name = None
    repo_id = None
    if repository_name and not repository_type:
        raise CLIError("--repository-type must be specified.")
    elif repository_type:
        if repository_type.lower() == _GITHUB_REPO_TYPE:
            if repository_url:
                repo_id = _get_repo_id_from_repo_url(repository_url)
                repo_name = repo_id
            else:
                repo_name = repository_name
        if repository_type.lower() == _AZURE_GIT_REPO_TYPE:
            repo_name = repository_name
            repo_id = _get_repository_id_from_name(organization, project, repository)
    definition = pipeline_client.get_definition(definition_id=id, project=project)
    if new_name:
        definition.name = new_name
    if description:
        definition.description = description
    if repo_name:
        definition.repository.name = repo_name
    if repo_id:
        definition.repository.id = repo_id
    if repository_type:
        definition.repository.type = repository_type
    if branch:
        definition.repository.default_branch = branch
    if service_connection:
        definition.repository.connected_service_id = service_connection
    if queue_id:
        definition.queue = AgentPoolQueue()
        definition.queue.id = queue_id
    if yml_path:
        definition.process = _create_process_object(yml_path)

    return pipeline_client.update_definition(project=project, definition_id=id, definition=definition)


def validate_name_is_available(name, organization, project):
    client = get_new_pipeline_client(organization=organization)
    definition_references = client.get_definitions(project=project, name=name)
    if not definition_references:
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


def _get_repo_id_from_repo_url(repository_url):
    parsed_url = uri_parse(repository_url)
    logger.debug('Parsing GitHub url: %s', parsed_url)
    if parsed_url.scheme == 'https' and parsed_url.netloc == 'github.com':
        logger.debug('Parsing path in the url to find repo id.')
        stripped_path = parsed_url.path.strip('/')
        if stripped_path.endswith('.git'):
            stripped_path = stripped_path[:-4]
        return stripped_path
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


def _get_service_endpoints(organization, project, endpoint_type=None):
    """
    Get the list of existing service connections filtered by type if mentioned
    """
    client = get_service_endpoint_client(organization)
    all_connections = client.get_service_endpoints(project)
    if endpoint_type is None:
        return all_connections
    else:
        filtered_connection = []
        for connection in all_connections:
            if connection.type.lower() == endpoint_type.lower():
                filtered_connection.append(connection)
        return filtered_connection

def get_github_service_endpoint(organization, project):
    """
    This will try to create a GitHub service connection if there is no existing one in the project
    GitHub pat token will be asked for interactively or can be provided
    by setting the Environment variable AZ_DEVOPS_GITHUB_PAT_ENVKEY.
    Service endpoint connection name is asked as input from the user, if the environment is non interative
    name is set to default  AzureDevopsCliCreatePipelineFlow
    """
    se_client = get_service_endpoint_client(organization)
    existing_service_endpoints = _get_service_endpoints(organization, project, 'github')
    service_endpoints_choice_list = ['Create new GitHub service connection']
    github_service_endpoints = []
    choice = 0
    for endpoint in existing_service_endpoints:
        if endpoint.authorization.scheme == 'InstallationToken':
            service_endpoints_choice_list.append('Name: {} {}'.format(endpoint.name, '(Recommended)'))
        else:
            service_endpoints_choice_list.append('Name: {}'.format(endpoint.name))
        github_service_endpoints.append(endpoint)
    if github_service_endpoints:
        choice = prompt_user_friendly_choice_list(
            "Which service connection do you want to use to communicate with GitHub?",
            service_endpoints_choice_list)
    if choice == 0:
        logger.debug("Creating a new service endpoint.")
        github_pat = get_github_pat_token()
        se_name = prompt('Enter a service endpoint name to create? ')
        print('')
        service_endpoint_authorization = EndpointAuthorization(parameters={'accessToken':github_pat},
                                                               scheme='PersonalAccessToken')
        service_endpoint_to_create = ServiceEndpoint(authorization=service_endpoint_authorization,
                                                     name=se_name, type='github',
                                                     url='https://github.com/')
        return se_client.create_service_endpoint(service_endpoint_to_create, project).id
    return existing_service_endpoints[choice-1].id


def try_get_repository_type(url):
    if 'https://github.com' in url:
        return _GITHUB_REPO_TYPE
    if 'https://dev.azure.com' or '.visualstudio.com' in url:
        return _AZURE_GIT_REPO_TYPE
    return None


def _create_and_get_yml_path(cix_client, repository_type, repo_id, repo_name, branch,
                             service_endpoint, project, organization):
    logger.debug('No yml file was given. Trying to find the yml file in the repo.')
    default_yml_exists = False
    yml_names = []
    yml_options = []
    configurations = cix_client.get_configurations(
        project=project, repository_type=repository_type,
        repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
    for configuration in configurations:
        if configuration.path.strip('/') == 'azure-pipelines.yml':
            default_yml_exists = True
        logger.debug('The repo has a yml pipeline definition. Path: %s', configuration.path)
        custom_name = 'Existing yml (path={})'.format(configuration.path)
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
        logger.debug(recommendation.name)
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
                cix_client=cix_client,
                repo_name=repo_name,
                organization=organization,
                project=project)
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
            # open the file
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
        checkin_path = prompt(msg='Enter a yaml file path to checkin the new pipeline yaml in the repository? ',
                              help_string='e.g. /new_azure-pipeline.yml to add in the root folder.')
        print('')
    files.append(Files(checkin_path, content))
    print('Files to be added to your repository ({numfiles})'.format(numfiles=len(files)))
    count_file = 1
    for file in files:
        print('{index}) {file}'.format(index=count_file, file=file.path))
        count_file = count_file + 1

    if default_yml_exists and checkin_path.strip('/') == 'azure-pipelines.yml':
        # atbagga todo update file
        print('Edits on the existing yaml can be done in the code repository.')
    else:
        commit_strategy_choice_list = ['Commit directly to the {branch} branch.'.format(branch=branch),
                                       'Create a new branch for this commit and start a pull request.']
        commit_choice = prompt_user_friendly_choice_list("How do you want to commit the files to the repository?",
                                                         commit_strategy_choice_list)
        commit_direct_to_branch = True
        if commit_choice == 1:
            commit_direct_to_branch = False

        if repository_type == _GITHUB_REPO_TYPE:
            push_files_github(files, repo_name, branch, commit_direct_to_branch)
        elif repository_type == _AZURE_GIT_REPO_TYPE:
            _checkin_files_to_azure_repo(files, repo_name, branch, organization, project)
        else:
            logger.warning('File checkin is not handled for this repository type. '
                           'Checkin the created yml in the repository and then run '
                           'the pipeline created by this command.')
    return checkin_path


def _checkin_files_to_azure_repo(files, repo_name, branch, organization, project,
                                 message="Set up CI with Azure Pipelines"):
    if files:
        for file in files:
            _checkin_file_to_azure_repo(file.path, file.content, repo_name, branch, organization, project, message)
    else:
        raise CLIError("No files to checkin.")


def _checkin_file_to_azure_repo(path_to_commit, content, repo_name, branch,
                                organization, project, message="Set up CI with Azure Pipelines"):
    logger.warning('Checking in file %s in the Azure repo %s', path_to_commit, repo_name)
    message = message + ' [skip ci]'
    git_client = get_git_client(organization=organization)
    from azext_devops.devops_sdk.v5_0.git.models import GitPush, GitRefUpdate
    # Get base commit Id
    all_heads_refs = git_client.get_refs(repository_id=repo_name,
                                         project=project,
                                         filter='heads/')
    old_object_id = None
    for ref in all_heads_refs:
        if ref.name == resolve_git_ref_heads(branch):
            old_object_id = ref.object_id
    if not old_object_id:
        raise CLIError('Cannot checkin the file. Error in getting the commits info for {branch}'.format(branch=branch))

    push_object = GitPush()
    ref_update = GitRefUpdate()
    ref_update.name = resolve_git_ref_heads(branch)
    ref_update.old_object_id = old_object_id
    push_object.ref_updates = [ref_update]
    push_object.commits = _get_commits_object(path_to_commit, content, message)
    git_client.create_push(push=push_object, repository_id=repo_name, project=project)


def _get_commits_object(path_to_commit, content, message):
    return [
        {
            "comment": message,
            "changes": [
                {
                    "changeType": "add",
                    "item": {
                        "path": path_to_commit
                    },
                    "newContent": {
                        "content": content,
                        "contentType": "rawtext"
                    }
                }
            ]
        }
    ]


def _get_pipelines_trigger(repo_type):
    if repo_type.lower() == _GITHUB_REPO_TYPE:
        return [{"settingsSourceType":2, "triggerType":2},
                {"forks":{"enabled": "true", "allowSecrets": "false"},
                 "settingsSourceType":2, "triggerType": "pullRequest"}]
    return [{"settingsSourceType":2, "triggerType":2}]


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
        elif _is_intelligent_handling_enabled_for_prop_type(prop_type=param.type):
            logger.debug('This property is handled intelligently (Name: %s) (Type: %s)', param.name, param.type)
            fetched_value = fetch_yaml_prop_intelligently(param.type, organization, project, repo_name)
            if fetched_value is not None:
                logger.debug('Auto filling param %s with value %s', param.name, fetched_value)
                params_to_render[param.name] = fetched_value
                prop_found = True
        if not prop_found:
            input_value = _prompt_for_prop_input(param_name_for_user, param.type)
            params_to_render[param.name] = input_value
            prop_found = True
    rendered_template = cix_client.render_template(template_id=template_id,
                                                   template_parameters={'tokens':params_to_render})
    return rendered_template.content, rendered_template.assets


def fetch_yaml_prop_intelligently(prop_type, organization, project, repo_name):
    if prop_type.lower() == 'endpoint:azurerm':
        return get_azure_rm_service_connection(organization, project)
    if prop_type.lower() == 'connectedservice:azurerm':
        return get_azure_rm_service_connection_id(organization, project)
    if prop_type.lower() == 'environmentresource:kubernetes':
        return get_kubernetes_environment_resource(organization, project, repo_name)
    if prop_type.lower() == 'endpoint:containerregistry':
        return get_container_registry_service_connection(organization, project)
    return None


def get_azure_rm_service_connection_id(organization, project):
    azure_rm_connection = get_azure_rm_service_connection(organization, project)
    return azure_rm_connection['Id']


def get_azure_rm_service_connection(organization, project):
    logger.debug('Create a new Azure Resource Manager service connection')
    subscription_id, subscription_name, tenant_id, environment_name = get_default_subscription_info()
    cix_client = get_new_cix_client(organization=organization)
    azure_rm_connection_create_obj = get_azure_rm_connection_create_object(
        subscription_id, subscription_name, environment_name, tenant_id)
    azure_rm_connection = cix_client.create_resources(creation_parameters=azure_rm_connection_create_obj,
                                                      project=project)
    azure_rm_connection_obj = azure_rm_connection.resources['azureRmConnection']
    poll_connection_ready(organization, project, azure_rm_connection_obj['Id'])
    return azure_rm_connection_obj


def get_kubernetes_environment_resource(organization, project, repo_name):
    logger.debug("Creating a new k8s environment resource.")
    import subprocess
    import json
    subscription_id, subscription_name, tenant_id, environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for fetching AKS clusters.", subscription_name)
    aks_list = subprocess.check_output('az aks list -o json', shell=True)
    aks_list = json.loads(aks_list)
    if aks_list:
        cluster_choice = 0
        cluster_choice_list = []
        for aks_clusters in aks_list:
            cluster_choice_list.append(aks_clusters['name'])
        cluster_choice = prompt_user_friendly_choice_list(
            "Which kubernetes cluster do you want to target for this pipeline?", cluster_choice_list)
        selected_cluster = aks_list[cluster_choice]
        create_namespace, namespace = get_kubernetes_namespace(organization, project, selected_cluster,
                                                               subscription_id, subscription_name, tenant_id,
                                                               environment_name)
        kubernetes_connection_obj = get_kubernetes_connection_create_object(
            subscription_id, subscription_name, selected_cluster['id'], selected_cluster['name'],
            selected_cluster['fqdn'], tenant_id, namespace, create_namespace, environment_name)
        cix_client = get_new_cix_client(organization=organization)
        kubernetes_connection = cix_client.create_resources(creation_parameters=kubernetes_connection_obj,
                                                            project=project)
        k8s_connection_obj = kubernetes_connection.resources['k8sConnection']
        poll_connection_ready(organization, project, k8s_connection_obj['Id'])
        kubernetes_env_obj = get_kubernetes_resource_create_object(
            k8s_connection_obj['Name'],
            selected_cluster['name'],
            repo_name,
            k8s_connection_obj['Id'],
            namespace)
        kubernetes_environment_resource = cix_client.create_resources(creation_parameters=kubernetes_env_obj,
                                                                      project=project)
        return kubernetes_environment_resource.resources['k8sResource']
    else:
        raise CLIError('There are no AKS clusters under your subscription. '
                       'Create the clusters or switch to another subscription, verify with '
                       'command \'az aks list\' and try again.')
    return None


def get_kubernetes_namespace(organization, project, cluster, subscription_id, subscription_name,
                             tenant_id, azure_env):
    choice_list = []
    existing_namespace_list = []
    choice_list.append("Create new")
    se_request_obj = get_se_kubernetes_namespace_request_obj(subscription_id, subscription_name, cluster['id'],
                                                             cluster['name'], cluster['fqdn'], azure_env, tenant_id)
    se_client = get_service_endpoint_client(organization=organization)
    se_result = se_client.execute_service_endpoint_request(service_endpoint_request=se_request_obj, project=project,
                                                           endpoint_id=cluster['name'])
    if se_result.result:
        import json
        for namespace in se_result.result:
            ns_json_obj = json.loads(namespace)
            existing_namespace_list.append(ns_json_obj['Value'])
            choice_list.append(ns_json_obj['Value'])
    choice = prompt_user_friendly_choice_list("Which kubernetes namespace do you want to target?",
                                              choice_list)
    if choice == 0:
        create_namespace = True
        namespace = prompt("Enter a name for new namespace to create: ")
        print('')
    else:
        create_namespace = False
        namespace = existing_namespace_list[choice-1]
    return create_namespace, namespace


def get_se_kubernetes_namespace_request_obj(subscription_id, subscription_name, cluster_id, cluster_name, fqdn,
                                            azure_env, tenant_id):
    return {
        "dataSourceDetails": {
            "dataSourceName": "KubernetesNamespaces",
            "headers": [
            ],
            "resourceUrl": "",
            "parameters": {
                "clusterName": cluster_name
            }
        },
        "resultTransformationDetails": {
            "resultTemplate": "{ \"Value\" : \"{{metadata.name}}\", \"DisplayValue\" : \"{{metadata.name}}\" }"
        },
        "serviceEndpointDetails": {
            "authorization": {
                "parameters": {
                    "azureEnvironment": azure_env,
                    "azureTenantId": tenant_id
                },
                "scheme": "Kubernetes"
            },
            "data": {
                "authorizationType": "AzureSubscription",
                "azureSubscriptionId": subscription_id,
                "azureSubscriptionName": subscription_name,
                "clusterId": cluster_id
            },
            "type": "Kubernetes",
            "url": "https://" + fqdn
            }
        }


def get_container_registry_service_connection(organization, project):
    import subprocess
    import json
    subscription_id, subscription_name, tenant_id, _environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for fetching Azure Container Registries.",
                   subscription_name)
    acr_list = subprocess.check_output('az acr list -o json', shell=True)
    acr_list = json.loads(acr_list)
    if acr_list:
        registry_choice = 0
        registry_choice_list = []
        for acr_clusters in acr_list:
            registry_choice_list.append(acr_clusters['name'])
        registry_choice = prompt_user_friendly_choice_list(
            "Which Azure Container Registry do you want to use for this pipeline", registry_choice_list)
        selected_registry = acr_list[registry_choice]
        cix_client = get_new_cix_client(organization=organization)
        acr_connection_obj = get_container_registry_connection_create_object(
            subscription_id,
            subscription_name,
            tenant_id,
            selected_registry['id'],
            selected_registry['name'],
            selected_registry['loginServer'])
        acr_container_resource = cix_client.create_resources(creation_parameters=acr_connection_obj, project=project)
        poll_connection_ready(organization, project,
                              acr_container_resource.resources['containerRegistryConnection']['Id'])
        return acr_container_resource.resources['containerRegistryConnection']
    else:
        raise CLIError('There is no Azure container registry under your subscription. '
                       'Create an ACR or switch to another subscription, '
                       'verify with command \'az acr list\' and try again.')
    return None


def poll_connection_ready(organization, project, connection_id):
    import colorama
    import humanfriendly
    import time
    colorama.init()
    with humanfriendly.Spinner(label="Checking resource readiness") as spinner:
        se_client = get_service_endpoint_client(organization)
        while True:
            spinner.step()
            time.sleep(0.5)
            service_endpoint = se_client.get_service_endpoint_details(project, connection_id)
            if service_endpoint.is_ready:
                break


def _is_intelligent_handling_enabled_for_prop_type(prop_type):
    SMART_HANDLING_FOR_PROP_TYPES = ['connectedservice:azurerm',
                                     'endpoint:azurerm',
                                     'environmentresource:kubernetes',
                                     'endpoint:containerregistry']
    if prop_type.lower() in SMART_HANDLING_FOR_PROP_TYPES:
        return True
    return False


def _prompt_for_prop_input(prop_name, prop_type):
    verify_is_a_tty_or_raise_error('The template requires a few inputs. These can be provided as --yml-props '\
                                   'in the command arguments or be input interatively.')
    val = prompt(msg='Please enter a value for {prop_name}: '.format(prop_name=prop_name),
                 help_string='Value of type {prop_type} is required.'.format(prop_type=prop_type))
    print('')
    return val


def _create_pipeline_build_object(name, description, repo_id, repo_name, repository_url, api_url, branch,
                                  service_endpoint, repository_type, yml_path, queue_id):
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
        logger.warning('Auto detecting agent pool. Queue: %s, Pool: %s', choosen_queue.name, choosen_queue.pool.name)
        return choosen_queue.id
    return None


def get_kubernetes_resource_create_object(resource_name, cluster_name, repo_name,
                                          kubernetes_service_connection_id, namespace):
    return {
        "k8sResource": {
            "resourcetocreate": {
                "name": resource_name,
                "namespace": namespace,
                "clusterName": cluster_name,
                "serviceEndpointId": kubernetes_service_connection_id
            },
            "type": "environmentResource:kubernetes"
        },
        "environment": {
            "resourcetocreate": {
                "name": repo_name,
                "description": "CI/CD setup from this repo: '{reponame}'".format(reponame=repo_name)
            },
            "type": "environment"
        }
    }

def get_kubernetes_connection_create_object(subscription_id, subscription_name, cluster_id, cluster_name, fqdn,
                                            tenant_id, namespace, create_namespace, azure_env):
    return {
        "k8sConnection": {
            "resourcetocreate": {
                "data": {
                    "authorizationType": "AzureSubscription",
                    "azureSubscriptionId": subscription_id,
                    "azureSubscriptionName": subscription_name,
                    "clusterId": cluster_id,
                    "namespace": namespace,
                    "operation.createNamespace": create_namespace
                },
                "name": cluster_name + "-" + namespace,
                "type": "kubernetes",
                "url": "https://" + fqdn,
                "authorization": {
                    "scheme": "Kubernetes",
                    "parameters": {
                        "azureEnvironment": azure_env,
                        "azureTenantId": tenant_id
                    }
                }
            },
            "type": "endpoint:kubernetes"
        }
    }

def get_container_registry_connection_create_object(subscription_id, subscription_name, tenant_id, registry_id,
                                                    registry_name, login_server):
    return {
        "containerRegistryConnection": {
            "resourcetocreate": {
                "data": {
                    "registrytype": "ACR",
                    "registryId": registry_id,
                    "subscriptionId": subscription_id,
                    "subscriptionName": subscription_name
                },
                "name": registry_name,
                "type": "dockerregistry",
                "url": "https://" + login_server,
                "authorization": {
                    "scheme": "serviceprincipal",
                    "parameters": {
                        "tenantId": tenant_id,
                        "servicePrincipalId": "<placeholder>",
                        "scope": registry_id,
                        "loginServer": login_server
                    }
                }
            },
            "type": "endpoint:containerRegistry"
        }
    }


def get_azure_rm_connection_create_object(subscription_id, subscription_name, azure_env, tenant_id):
    return {
        "azureRmConnection": {
            "resourcetocreate": {
                "data": {
                    "subscriptionId": subscription_id,
                    "subscriptionName": subscription_name,
                    "environment": azure_env,
                    "scopeLevel": "Subscription",
                    "creationMode": "Automatic",
                    "azureSpnRoleAssignmentId": "",
                    "azureSpnPermissions": "",
                    "spnObjectId": "",
                    "appObjectId": ""
                },
                "name": "{sub_name} ({sub_id})".format(sub_name=subscription_name, sub_id=subscription_id),
                "type": "azurerm",
                "url": "https://management.azure.com/",
                "authorization": {
                    "scheme": "ServicePrincipal",
                    "parameters": {
                        "tenantid": tenant_id,
                        "serviceprincipalid": "",
                        "authenticationType": "spnKey",
                        "serviceprincipalkey": ""
                    }
                }
            },
            "type": "endpoint:azureRm"
        }
    }
