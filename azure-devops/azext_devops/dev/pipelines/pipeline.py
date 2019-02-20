# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new
import webbrowser
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


class YmlOptions:
    def __init__(self, name, id, content, description='Custom yml', params=None, path=None):
        self.name = name
        self.id = id
        self.description = description
        self.content = content
        self.path = path
        self.params = params


def pipeline_create(name, description=None, url=None, repository_url=None, branch=None, yml_path=None,
                    repository_type=None, service_endpoint=None, yml_props=None,
                    organization=None, project=None, detect=None):
    """Create a pipeline
    :param name: Name of the new pipeline
    :type name: str
    :param description: Description for the new pipeline
    :type description: str
    :param url: Url of the yml file for which the pipeline will be configured
    :type url: str
    :param repository_url: Repository clone url for which the pipeline will be configured.
    Ignored if --url is specified.
    :type repository_url: str
    :param branch: Branch name for which the pipeline will be configured. Ignored if --url is specified.
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo (if yml is already present in the repo).
    Ignored if --url is specified.
    :type yml_path: str
    :param repository_type: Type of repository. Auto detected for Github and Azure Repos.
    :type repository_type: str
    :param yml_props: Any additional required yml template params. Provided in the format of key=value pairs.
    e.g. --yml-props repoName=contoso/webapp
    :type yml_props: str
    :param service_endpoint: Id of the Service Endpoint created for the repository.
    Use command az devops service-endpoint -h for creating/listing service-endpoints.
    :type service_endpoint: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        # Todo: Detect repository url from git clone url here if url or repository-url is not specified.
        if not url and (not repository_url or not branch):
            raise CLIError("Either --url or --repository-url, --branch must be specified.")
        if not repository_type:
            if url:
                repository_type = try_get_repository_type(url)
            else:
                repository_type = try_get_repository_type(repository_url)
            if not repository_type:
                raise CLIError("--repository-type must be specified.")
        # Parse repository information according to repository type
        repo_name = None
        if repository_type.lower() == "github":
            if url:
                repository_url, repo_id, branch, yml_path = _parse_github_repo_info(url)
            else:
                repo_id = _get_repo_id_from_repo_url(repository_url)
            repo_name = repo_id
        if repository_type.lower() == 'tfsgit':
            # todo atbagga handle tfsgit repo url parsing
            raise CLIError('Work in Progress')

        if not service_endpoint:
            service_endpoint = get_github_service_endpoint(organization, project)

        new_pipeline_client = get_new_pipeline_client(organization=organization)
        default_yml_exists = False
        # No yml path == find or recommend yml scenario
        if not yml_path:
            logger.debug('No yml file was given. Trying to find the yml file in the repo.')
            yml_names = []
            yml_options = []
            configurations = new_pipeline_client.get_configurations(
                project=project, repository_type=repository_type,
                repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
            for configuration in configurations:
                if configuration.path == 'azure-pipelines.yml':
                    default_yml_exists = True
                logger.debug('The repo has a yml pipeline definition. Path: %s', configuration.path)
                custom_name = 'Existing yml (path={})'.format(configuration.path)
                yml_names.append(custom_name)
                yml_options.append(YmlOptions(name=custom_name, content=configuration.content, id='customid',
                                              path=configuration.path))
            recommendations = new_pipeline_client.get_recommended_templates(
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
                _fp, temp_filename = tempfile.mkstemp(text=True)
                f = open(temp_filename, mode='w')
                f.write(yml_options[yml_selection_index].content)
                f.close()
                # open the file
                webbrowser.open(temp_filename)
                proceed_selection = prompt_user_friendly_choice_list(
                    'Do you want to proceed creating a pipeline?',
                    ['Proceed with this yml', 'Revisit recommendations'])
            # Read updated data from the file
            f = open(temp_filename, mode='r')
            content = f.read()
            f.close()
            # todo atbagga fix this
            # import os
            # os.remove(temp_filename)
            if yml_options[yml_selection_index].params:
                params_to_render = {}
                for param in yml_options[yml_selection_index].params:
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
                    if not prop_found:
                        raise CLIError('Missing required property for this template.'\
                                        'Property Name: {propname} of type: {proptype} needs to be provided'\
                                        'in --yml-props.'.format(propname=param.name, proptype=param.type))
                new_pipeline_client.render_template(template_id=yml_options[yml_selection_index].id,
                                                    template_parameters=params_to_render)
            else:
                logger.debug("Existing template edited or No required params for this template.")

            checkin_path = 'azure-pipelines.yml'
            if default_yml_exists and not yml_options[yml_selection_index].path:  # We need yml path from user
                logger.warning('A yml file azure-pipelines.yml already exists in the repository root.')
                verify_is_a_tty_or_raise_error('Yml file path is required to checkin the pipeline yml'\
                    'to the repository. Checkin the yml file to the repository and create a pipeline from that yml'\
                    'or run this command interactively.')
                checkin_path = prompt(msg='Enter a yml file path to checkin the new yml pipeline in the repository? ',
                                      help_string='e.g. /azure-pipeline.yml to add in the root folder.')

            checkin_file_to_github(checkin_path, content, service_endpoint, repo_name, branch,
                                   organization, project)
            yml_path = checkin_path

        # Create build definition
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

        client = get_pipeline_client(organization)
        return client.create_definition(definition=definition, project=project)
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
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect, organization=organization, project=project, repo=repository)
        client = get_pipeline_client(organization)
        query_order = 'DefinitionNameAscending'
        repository_type = None
        if repository is not None:
            if repository_type is None:
                repository_type = 'TfsGit'
            if repository_type.lower() == 'tfsgit':
                resolved_repository = _resolve_repository_as_id(repository, organization, project)
            else:
                resolved_repository = repository
            if resolved_repository is None:
                raise ValueError("Could not find a repository with name '{}', in project '{}'."
                                 .format(repository, project))
        else: 
            resolved_repository = None
        definition_references = client.get_definitions(project=project, name=name, repository_id=resolved_repository,
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
                raise ValueError("Either the --id argument or the --name argument must be supplied for this command.")
        build_definition = client.get_definition(definition_id=id, project=project)
        if open:
            _open_pipeline(build_definition, organization)
        return build_definition
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_update(name, description=None, url=None, repository_url=None, branch=None, yml_path=None,
                    repository_type=None, service_endpoint=None, yml_props=None,
                    organization=None, project=None, detect=None):
    """Update a pipeline
    :param name: Name of the pipeline to update
    :type name: str
    :param id: Id of the pipeline to update
    :type id: str
    :param description: New description for the pipeline
    :type description: str
    :param repository_url: Repository clone url for which the pipeline will be configured.
    :type repository_url: str
    :param branch: Branch name for which the pipeline will be configured.
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo (if yml is already present in the repo).
    :type yml_path: str
    :param service_endpoint: Id of the service endpoint for pipelines to connect to the repository.
    Use command az devops service-endpoint -h for creating/listing service-endpoints.
    :type service_endpoint: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    """
    pass


def pipeline_run(id=None, name=None, open=False,  # pylint: disable=redefined-builtin
                 organization=None, project=None, detect=None):
    """Request (run) a pipeline.
    :param id: ID of the pipeline to queue. Required if --name is not supplied.
    :type id: int
    :param name: Name of the pipeline to queue. Ignored if --id is supplied.
    :type name: str
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
        build = Build(definition=definition_reference)
        queued_build = client.queue_build(build=build, project=project)
        if open:
            _open_pipeline(queued_build, organization)
        return queued_build
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_delete(id, organization=None, project=None, detect=None): # pylint: disable=redefined-builtin
    """Delete a pipeline.
    :param pipeline_id: ID of the pipeline.
    :type pipeline_id: int
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

def _parse_github_repo_info(github_file_url):
    _REPOSITORY_PARSE_ERROR = 'Repository could not be parsed to a yml file in a Github repository.'
    parsed_url = uri_parse(github_file_url)
    logger.debug('Parsing github url: %s', parsed_url)
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
    logger.debug('Parsing github url: %s', parsed_url)
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


def _get_service_endpoints(organization, project):
    """
    get the list of existing service endpoint connections
    """
    client = get_service_endpoint_client(organization)
    return client.get_service_endpoints(project)


def get_github_service_endpoint(organization, project):
    """
    This will try to create a github service connection if there is no existing one in the project
    Github pat token will be asked for interactively or can be provided
    by setting the Environment variable AZ_DEVOPS_GITHUB_PAT_ENVKEY.
    Service endpoint connection name is asked as input from the user, if the environment is non interative
    name is set to default  AzureDevopsCliCreatePipelineFlow
    """
    se_client = get_service_endpoint_client(organization)
    existing_service_endpoints = _get_service_endpoints(organization, project)
    service_endpoints_choice_list = ['Create new Github service connection']
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
    else:
        return existing_service_endpoints[choice-1].id


def get_github_pat_token():
    github_pat = os.getenv(AZ_DEVOPS_GITHUB_PAT_ENVKEY, None)
    if github_pat:
        logger.warning('Using Github PAT token found in environment variable (%s).', AZ_DEVOPS_GITHUB_PAT_ENVKEY)
        return github_pat

    verify_is_a_tty_or_raise_error('Github PAT token is required for this command.'\
        'Either set the environment variable ({env_var}) or run the command interactively.'.format(
            env_var=AZ_DEVOPS_GITHUB_PAT_ENVKEY))
    return prompt_pass(msg='Enter your Github PAT token: ')


def try_get_repository_type(url):
    if 'https://github.com' in url:
        return 'github'
    if 'https://dev.azure.com' or '.visualstudio.com' in url:
        return 'tfsgit'
