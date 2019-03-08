# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new
import tempfile
import os
from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt_pass, prompt, verify_is_a_tty, NoTTYException
from azext_devops.dev.common.services import (get_pipeline_client,
                                              get_new_pipeline_client,
                                              get_git_client,
                                              get_service_endpoint_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_quote, uri_parse
from azext_devops.dev.common.uuid import is_uuid
from azext_devops.dev.common.git import get_remote_url, get_current_branch_name, resolve_git_ref_heads
from azext_devops.dev.common.arguments import should_detect
from azext_devops.dev.common.prompting import (prompt_user_friendly_choice_list,
                                               verify_is_a_tty_or_raise_error)
from azext_devops.dev.common.const import AZ_DEVOPS_GITHUB_PAT_ENVKEY
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.build.v5_1.models import Build
from azext_devops.vstsCompressed.build.v5_1.models import BuildDefinition
from azext_devops.vstsCompressed.build.v5_1.models import BuildRepository
from azext_devops.vstsCompressed.build.v5_1.models import AgentPoolQueue
from azext_devops.vstsCompressed.build.v5_1.models import DefinitionReference
from azext_devops.vstsCompressed.service_endpoint.v5_1.models import ServiceEndpoint
from azext_devops.vstsCompressed.service_endpoint.v5_1.models import EndpointAuthorization
from .github_file_checkin import checkin_file_to_github
from .build_definition import get_definition_id_from_name

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class YmlOptions:
    def __init__(self, name, id, content, description='Custom yml', params=None, path=None):  # pylint: disable=redefined-builtin
        self.name = name
        self.id = id
        self.description = description
        self.content = content
        self.path = path
        self.params = params


def pipeline_create(name, description=None, repository_name=None, repository_url=None, branch=None, yml_path=None,
                    repository_type=None, service_connection=None, yml_props=None,
                    organization=None, project=None, detect=None, queue_id=None):
    """Create a pipeline
    :param name: Name of the new pipeline
    :type name: str
    :param description: Description for the new pipeline
    :type description: str
    :param repository_url: Repository clone url for which the pipeline will be configured.
    :type repository_url: str
    :param repository_name: Name of the repository for a Azure Devops repository or owner/reponame
    in case of GitHub Repo.
    --repository-type argument is required with this. Ignored if --repository-url is supplied
    :type repository_name: str
    :param branch: Branch name for which the pipeline will be configured.
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo (if yml is already present in the repo).
    :type yml_path: str
    :param repository_type: Type of repository. Auto detected for GitHub and Azure Repos.
    :type repository_type: str
    :param yml_props: Any additional required yml template params. Provided in the format of key=value pairs.
    e.g. --yml-props repoName=contoso/webapp
    :type yml_props: str
    :param service_connection: Id of the Service Endpoint created for the repository.
    Use command az devops service-endpoint -h for creating/listing service_connections.
    :type service_connection: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    """
    url = None
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect, organization=organization, project=project, repo=repository_name)
        if not url and not repository_url and not repository:
            repository_url = _get_repository_url_from_local_repo(detect=detect)
        if not branch and should_detect(detect):
            branch = get_current_branch_name()
        if not repository_type:
            if url:
                repository_type = try_get_repository_type(url)
            elif repository_url:
                repository_type = try_get_repository_type(repository_url)
            elif repository:
                repository_type = 'tfsgit'
            if not repository_type:
                raise CLIError("--repository-url or --repository-type must be specified.")
        else:
            repository_type = repository_type.lower()

        if not url:
            if not repository_url or not branch:
                if (not repository and not repository_name) or not repository_type or not branch:
                    raise CLIError("Either --repository-url and --branch OR "\
                                "--repository-name, --repository-type and --branch must be specified.")

        # Parse repository information according to repository type
        repo_name = None
        repo_id = None
        if repository_type.lower() == "github":
            if url:
                repository_url, repo_id, branch, yml_path = _parse_github_repo_info(url)
                repo_name = repo_id
            elif repository_url:
                repo_id = _get_repo_id_from_repo_url(repository_url)
                repo_name = repo_id
            else:
                repo_name = repository_name
                repo_id = repository_name
                repository_url = 'https://github.com/' + repo_name
        if repository_type.lower() == 'tfsgit':
            repo_name = repository_name
            repo_id = _get_repository_id_from_name(organization, project, repository)

        if not service_connection and repository_type != 'tfsgit':
            service_connection = get_github_service_endpoint(organization, project)

        new_pipeline_client = get_new_pipeline_client(organization=organization)
        # No yml path => find or recommend yml scenario
        if not yml_path:
            yml_path = _create_and_get_yml_path(new_pipeline_client, repository_type, repo_id, repo_name, branch,
                                                yml_props, service_connection, project, organization)
        # Create build definition
        definition = _create_pipeline_build_object(name, description, repo_id, repo_name, repository_url, branch,
                                                   service_connection, repository_type, yml_path, queue_id)
        client = get_pipeline_client(organization)
        created_definition = client.create_definition(definition=definition, project=project)
        logger.warning('Successfully create a pipeline with Name: %s, Id: %s.',
                       created_definition.name, created_definition.id)
        return client.queue_build(build=Build(definition=created_definition), project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_list(name=None, top=None, organization=None, project=None, repository=None,
                  repository_type=None, detect=None):
    """List pipelines.
    :param name: Limit results to pipelines with this name or starting with this name. Examples: "FabCI" or "Fab*"
    :type name: bool
    :param top: Maximum number of pipelines to list.
    :type top: int
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param repository: Limit results to pipelines associated with this repository.
    :type repository: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    :param repository_type: Limit results to pipelines associated with this repository type.
    It is mandatory to pass 'repository' argument along with this argument.
    :type repository_type: str
    :rtype: [BuildDefinitionReference]
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        client = get_pipeline_client(organization)
        query_order = 'DefinitionNameAscending'
        if repository is not None:
            if repository_type is None:
                repository_type = 'TfsGit'
            if repository_type.lower() == 'tfsgit':
                repository = _resolve_repository_as_id(repository, organization, project)
            if repository is None:
                raise ValueError("Could not find a repository with name '{}', in project '{}'."
                                 .format(repository, project))
        definition_references = client.get_definitions(project=project, name=name, repository_id=repository,
                                                       repository_type=repository_type, top=top,
                                                       query_order=query_order)
        return definition_references
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_show(id=None, name=None, open=False, organization=None, project=None,  # pylint: disable=redefined-builtin
                  detect=None):
    """Get the details of a pipeline.
    :param id: ID of the pipeline.
    :type id: int
    :param name: Name of the pipeline. Ignored if --id is supplied.
    :type name: str
    :param open: Open the pipeline summary page in your web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: BuildDefinitionReference
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        client = get_pipeline_client(organization)
        if id is None:
            if name is not None:
                id = get_definition_id_from_name(name, client, project)
            else:
                raise CLIError("Either the --id argument or the --name argument must be supplied for this command.")
        build_definition = client.get_definition(definition_id=id, project=project)
        if open:
            _open_pipeline(build_definition, organization)
        return build_definition
    except VstsServiceError as ex:
        raise CLIError(ex)


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
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect, organization=organization, project=project, repo=repository_name)
        pipeline_client = get_pipeline_client(organization=organization)
        if id is None:
            if name is not None:
                id = get_definition_id_from_name(name, pipeline_client, project)
            else:
                raise CLIError("Either the --id argument or the --name argument must be supplied for this command.")
        if not repository_type:
            if repository_url:
                repository_type = try_get_repository_type(repository_url)
            elif repository:
                repository_type = 'tfsgit'
        else:
            repository_type = repository_type.lower()
        repo_name = None
        repo_id = None
        if repository_name and not repository_type:
            raise CLIError("--repository-type must be specified.")
        elif repository_type:
            if repository_type.lower() == "github":
                if repository_url:
                    repo_id = _get_repo_id_from_repo_url(repository_url)
                    repo_name = repo_id
                else:
                    repo_name = repository_name
            if repository_type.lower() == 'tfsgit':
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
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_run(id=None, branch=None, commit_id=None, name=None, open=False,  # pylint: disable=redefined-builtin
                 organization=None, project=None, detect=None):
    """Request (run) a pipeline.
    :param id: ID of the pipeline to queue. Required if --name is not supplied.
    :type id: int
    :param name: Name of the pipeline to queue. Ignored if --id is supplied.
    :type name: str
    :param branch: Name of the branch on which the pipeline run is to be queued.
    :type branch: str
    :param commit_id: Commit-id on which the pipeline run is to be queued.
    :type commit_id: str
    :param open: Open the pipeline results page in your web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: :class:`<Build> <build.v5_1.models.Build>`
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        if id is None and name is None:
            raise ValueError('Either the --id argument or the --name argument ' +
                             'must be supplied for this command.')
        client = get_pipeline_client(organization)
        if id is None:
            id = get_definition_id_from_name(name, client, project)
        definition_reference = DefinitionReference(id=id)
        build = Build(definition=definition_reference, source_branch=branch, source_version=commit_id)
        queued_build = client.queue_build(build=build, project=project)
        if open:
            _open_pipeline(queued_build, organization)
        return queued_build
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_delete(id, organization=None, project=None, detect=None): # pylint: disable=redefined-builtin
    """Delete a pipeline.
    :param id: ID of the pipeline.
    :type id: int
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        client = get_pipeline_client(organization)
        build = client.delete_definition(definition_id=id, project=project)
        return build
    except VstsServiceError as ex:
        raise CLIError(ex)


def _open_pipeline_run(run, organization):
    """Open the build results page in your web browser.
    :param :class:`<Build> <build.v5_1.models.Build>` build:
    :param str organization:
    """
    # https://dev.azure.com/OrgName/ProjectName/_build/results?buildId=1234
    project = run.project.name
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_build/results?buildid='\
        + uri_quote(str(run.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)


def _open_pipeline(definition, organization):
    """Opens the build definition in the default browser.
    :param :class:`<BuildDefinitionReference> <build.v5_1.models.BuildDefinitionReference>` definition:
    :param str organization:
    """
    # https://dev.azure.com/OrgName/ProjectName/_build/index?definitionId=1234
    project = definition.project.name
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_build?definitionId='\
        + uri_quote(str(definition.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)


def _resolve_repository_as_id(repository, organization, project):
    if is_uuid(repository):
        return repository
    else:
        git_client = get_git_client(organization)
        repositories = git_client.get_repositories(project=project, include_links=False, include_all_urls=False)
        for found_repository in repositories:
            if found_repository.name.lower() == repository.lower():
                return found_repository.id
    return None


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


def _parse_github_repo_info(github_file_url):
    _REPOSITORY_PARSE_ERROR = 'Repository could not be parsed to a yml file in a GitHub repository.'
    parsed_url = uri_parse(github_file_url)
    logger.debug('Parsing GitHub url: %s', parsed_url)
    if parsed_url.scheme == 'https' and parsed_url.netloc == 'github.com':
        # Parse path to find Id and file path
        logger.debug('Parsing path in the url to find repo, branch and yml path')
        stripped_path = parsed_url.path.strip('/')
        if stripped_path.count('/') > 2:
            owner, repository_name, path = stripped_path.split('/', 2)
        else:
            raise CLIError(_REPOSITORY_PARSE_ERROR)
        repo_id = '{owner}/{repo_name}'.format(owner=owner, repo_name=repository_name)
        repo_url = 'https://github.com/{id}.git'.format(id=repo_id)
        path = path.strip('/')
        if path.count('/') > 1:
            blob, branch_name, file_path = path.split('/', 2)
            file_path = './{}'.format(file_path)
        else:
            raise CLIError(_REPOSITORY_PARSE_ERROR)
        if blob != 'blob':
            raise CLIError(_REPOSITORY_PARSE_ERROR)
        return repo_url, repo_id, branch_name, file_path
    else:
        raise CLIError(_REPOSITORY_PARSE_ERROR)


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


def _create_repo_properties_object(service_endpoint, branch):
    return {
        "connectedServiceId": service_endpoint,
        "defaultBranch": branch
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
            if connection.type == endpoint_type.lower():
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
    existing_service_endpoints = _get_service_endpoints(organization, project)
    service_endpoints_choice_list = ['Create new GitHub service connection']
    github_service_endpoints = []
    choice = 0
    for endpoint in existing_service_endpoints:
        if 'github.com' in endpoint.url:
            service_endpoints_choice_list.append('Name: {}, Url: {}'.format(endpoint.name, endpoint.url))
            github_service_endpoints.append(endpoint)
    if github_service_endpoints:
        choice = prompt_user_friendly_choice_list("Create or choose existing service connection? ",
                                                  service_endpoints_choice_list)
    if choice == 0:
        logger.debug("Creating a new service endpoint.")
        github_pat = get_github_pat_token()
        try:
            verify_is_a_tty()
            se_name = prompt('Enter a service endpoint name to create? ')
        except NoTTYException:
            se_name = 'AzureDevopsCliCreatePipelineFlow'
            logger.warning("Creating a new service endpoint with name %s", se_name)
        service_endpoint_authorization = EndpointAuthorization(parameters={'accessToken':github_pat},
                                                               scheme='PersonalAccessToken')
        service_endpoint_to_create = ServiceEndpoint(authorization=service_endpoint_authorization,
                                                     name=se_name, type='github',
                                                     url='https://github.com/')
        return se_client.create_service_endpoint(service_endpoint_to_create, project).id
    return existing_service_endpoints[choice-1].id


def get_github_pat_token():
    github_pat = os.getenv(AZ_DEVOPS_GITHUB_PAT_ENVKEY, None)
    if github_pat:
        logger.warning('Using GitHub PAT token found in environment variable (%s).', AZ_DEVOPS_GITHUB_PAT_ENVKEY)
        return github_pat

    verify_is_a_tty_or_raise_error('GitHub PAT token is required for this command. '\
        'Either set the environment variable ({env_var}) or run the command interactively.'.format(
            env_var=AZ_DEVOPS_GITHUB_PAT_ENVKEY))
    return prompt_pass(msg='Enter your GitHub PAT token: ')


def try_get_repository_type(url):
    if 'https://github.com' in url:
        return 'github'
    if 'https://dev.azure.com' or '.visualstudio.com' in url:
        return 'tfsgit'
    return None


def _create_and_get_yml_path(pipeline_client, repository_type, repo_id, repo_name, branch, yml_props,
                             service_endpoint, project, organization):
    logger.debug('No yml file was given. Trying to find the yml file in the repo.')
    default_yml_exists = False
    yml_names = []
    yml_options = []
    configurations = pipeline_client.get_configurations(
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

    recommendations = pipeline_client.get_recommended_templates(
        project=project, repository_type=repository_type,
        repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
    logger.debug('List of recommended templates..')
    for recommendation in recommendations:
        logger.debug(recommendation.name)
        yml_names.append(recommendation.name)
        yml_options.append(YmlOptions(name=recommendation.name, content=recommendation.content,
                                      id=recommendation.id, description=recommendation.description,
                                      params=recommendation.parameters))
    temp_filename = None
    yml_selection_index = 0
    proceed_selection = 1
    while proceed_selection == 1:
        yml_selection_index = prompt_user_friendly_choice_list("Choose a yml template to create a pipeline:",
                                                               yml_names)
        if yml_options[yml_selection_index].params:
            yml_options[yml_selection_index].content = _handle_yml_props(
                params_required=yml_options[yml_selection_index].params,
                yml_props=yml_props,
                template_id=yml_options[yml_selection_index].id,
                pipeline_client=pipeline_client,
                repo_name=repo_name,
                organization=organization,
                project=project)
        temp_dir = tempfile.mkdtemp(prefix='AzurePipelines_')
        temp_filename = os.path.join(temp_dir, 'azure-pipelines.yml')
        f = open(temp_filename, mode='w')
        f.write(yml_options[yml_selection_index].content)
        f.close()
        # open the file
        _open_file(temp_filename)
        proceed_selection = prompt_user_friendly_choice_list(
            'We have opened the pipeline yaml file for you to review/edit. '\
            'Please edit, save and close the file in the editor before proceeding. '\
            'Do you want to proceed creating a pipeline?',
            ['Proceed with this yml', 'Revisit recommendations'])
    # Read updated data from the file
    f = open(temp_filename, mode='r')
    content = f.read()
    f.close()
    import shutil
    shutil.rmtree(temp_dir)

    checkin_path = 'azure-pipelines.yml'
    if default_yml_exists and not yml_options[yml_selection_index].path:  # We need yml path from user
        logger.warning('A yml file azure-pipelines.yml already exists in the repository root.')
        verify_is_a_tty_or_raise_error('Yml file path is required to checkin the pipeline yml '\
            'to the repository. Checkin the yml file to the repository and create a pipeline from that yml '\
            'or run this command interactively.')
        checkin_path = prompt(msg='Enter a yml file path to checkin the new pipeline yml in the repository? ',
                              help_string='e.g. /azure-pipeline.yml to add in the root folder.')
    if default_yml_exists and checkin_path.strip('/') == 'azure-pipelines.yml':
        logger.warning('File update is not handled. We will create the pipeline with the yaml selected. '
                       'Checkin the created yml in the repository and then run the pipeline created by this command.')
    else:
        if repository_type == 'github':
            checkin_file_to_github(checkin_path, content, service_endpoint, repo_name, branch,
                                   organization, project)
        elif repository_type == 'tfsgit':
            _checkin_file_to_azure_repo(checkin_path, content, repo_name, branch, organization, project)
        else:
            logger.warning('File checkin is not handled for this repository type. '\
                        'Checkin the created yml in the repository and then run the pipeline created by this command.')
    return checkin_path


def _open_file(filepath):
    import subprocess
    import platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def _checkin_file_to_azure_repo(path_to_commit, content, repo_name, branch,
                                organization, project, message="Set up CI with Azure Pipelines"):
    git_client = get_git_client(organization=organization)
    from azext_devops.vstsCompressed.git.v4_0.models import GitPush, GitRefUpdate
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


def _handle_yml_props(params_required, yml_props, template_id, pipeline_client, repo_name, organization, project):
    logger.warning('The template requires a few inputs. '
                   'These can be provided as --yml-props in the command arguments or be input interactively.')
    params_to_render = {}
    for param in params_required:
        # hack this is fixed in 149
        if param.name == 'serviceEndpointId':
            param.name = 'azureServiceConnectionId'
        logger.debug('looking for param %s in props', param.name)
        prop_found = False
        if yml_props:
            for prop in yml_props:
                parts = prop.split('=', 1)
                if len(parts) == 1:
                    raise CLIError('Usage error: --yml_props prop_key1=prop_value1 prop_key2=prop_value2 ')
                if parts[0] == param.name:
                    prop_found = True
                    params_to_render[parts[0]] = parts[1]
        elif _is_intelligent_handling_enabled_for_prop_name_type(prop_type=param.type, prop_name=param.name):
            logger.debug('This property is handled intelligently (Name: %s) (Type: %s)', param.name, param.type)
            if param.name == 'repositoryName':
                logger.warning('Auto filling param %s: %s', param.name, repo_name)
                params_to_render[param.name] = repo_name
                prop_found = True
            else:
                fetched_value = fetch_yaml_prop_intelligently(param.name, param.type, organization, project)
                if fetched_value is not None:
                    logger.warning('Auto filling param %s: %s', param.name, fetched_value)
                    params_to_render[param.name] = fetched_value
                    prop_found = True
        if not prop_found:
            input_value = _prompt_for_prop_input(param.name, param.type)
            params_to_render[param.name] = input_value
            prop_found = True
        if not prop_found:
            raise CLIError('Missing required property for this template. '\
                            'Property Name: {propname} of type: {proptype} needs to be provided '\
                            'in --yml-props.'.format(propname=param.name, proptype=param.type))
    rendered_template = pipeline_client.render_template(template_id=template_id,
                                                        template_parameters={'tokens':params_to_render})
    return rendered_template.content


def fetch_yaml_prop_intelligently(prop_name, prop_type, organization, project):
    if prop_type.lower() == 'connectedservice:azurerm':
        return get_azure_rm_service_connection(organization, project)
    return None


def get_azure_rm_service_connection(organization, project):
    azurerm_connections = _get_service_endpoints(organization=organization, project=project, endpoint_type='azurerm')
    if azurerm_connections:
        service_endpoints_choice_list = ['Create new AzureRM Service connection']
        choice = 0
        for endpoint in azurerm_connections:
            service_endpoints_choice_list.append('Name: {}'.format(endpoint.name))
        if service_endpoints_choice_list:
            choice = prompt_user_friendly_choice_list("Create or choose existing service connection? ",
                                                      service_endpoints_choice_list)
        if choice == 0:
            logger.debug("Creating a new service connection.")
            logger.warning("Creating azure service connection is not handled. Please create and supply the value.")
        else:
            return azurerm_connections[choice-1].id
    else:
        return None


SMART_HANDLING_FOR_PROP_TYPES = [ 'connectedservice:azurerm' ]
SMART_HANDLING_FOR_PROP_NAMES = [ 'repositoryname' ]

def _is_intelligent_handling_enabled_for_prop_name_type(prop_name, prop_type):
    if prop_name.lower() in SMART_HANDLING_FOR_PROP_NAMES:
        return True
    if prop_type.lower() in SMART_HANDLING_FOR_PROP_TYPES:
        return True
    return False


def _prompt_for_prop_input(prop_name, prop_type):
    verify_is_a_tty_or_raise_error('The template requires a few inputs. These can be provided as --yml-props '\
                                   'in the command arguments or be input interatively.')
    return prompt(msg='Please enter a value for {prop_name}: '.format(prop_name=prop_name),
                  help_string='Value of type {prop_type} is required.'.format(prop_type=prop_type))


def _create_pipeline_build_object(name, description, repo_id, repo_name, repository_url, branch,
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
        definition.repository.properties = _create_repo_properties_object(service_endpoint, branch)
    definition.repository.type = repository_type
    # Set build process
    definition.process = _create_process_object(yml_path)
    # set agent queue
    definition.queue = AgentPoolQueue()
    definition.queue.id = 163  # todo atbagga This should not be hardcoded
    if queue_id:
        definition.queue.id = queue_id  # todo atbagga This should not be hardcoded
    return definition


def _get_repository_id_from_name(organization, project, repository):
    git_client = get_git_client(organization)
    repository = git_client.get_repository(project=project, repository_id=repository)
    return repository.id
