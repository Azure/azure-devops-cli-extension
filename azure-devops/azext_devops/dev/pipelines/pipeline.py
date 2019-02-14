# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from vsts.exceptions import VstsServiceError
from vsts.build.v5_1.models.build import Build
from vsts.build.v5_1.models.build_definition import BuildDefinition
from vsts.build.v5_1.models.build_repository import BuildRepository
from vsts.build.v5_1.models.agent_pool_queue import AgentPoolQueue
from vsts.build.v5_1.models.definition_reference import DefinitionReference
from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_pipeline_client,
                                              get_new_pipeline_client,
                                              get_git_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_quote, uri_parse
from azext_devops.dev.common.uuid import is_uuid
from azext_devops.dev.common.prompting import prompt_user_friendly_choice_list
from .build_definition import get_definition_id_from_name

logger = get_logger(__name__)


class YmlOptions:
    def __init__(self, name, content, description='Custom yml', params=None):
        self.name = name
        self.description = description
        self.content = content
        self.params = params


def pipeline_create(name, repository_type, repository_url=None, branch=None, yml_path=None,
                    service_endpoint=None, description=None, url=None,
                    organization=None, project=None, detect=None):
    """Create a pipeline
    :param name: Name of the new pipeline
    :type name: str
    :param description: Description for the new pipeline
    :type description: str
    :param url: Url of the yml file for which the pipeline will be configured
    :type url: str
    :param repository_url: Repository clone url for which the pipeline will be configured
    :type repository_url: str
    :param branch: Branch name for which the pipeline will be configured
    :type branch: str
    :param yml_path: Path of the pipelines yml file in the repo (if yml is already present in the repo)
    :type yml_path: str
    :param repository_type: Type of repository
    :type repository_type: str
    :param service_endpoint: Service endpoint id created for the repository.
    :type service_endpoint: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    """
    import pdb 
    pdb.set_trace()
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        if not repository_type:
            raise CLIError("--repository-type must be specified.")
        if not url and (not repository_url or not branch):
            raise CLIError("Either --url or --repository-url, --branch must be specified.")
        # Parse repository information according to repository type
        repo_name = None
        if repository_type.lower() == "github":
            if url:
                repository_url, repo_id, branch, yml_path = _parse_github_repo_info(url)
            else:
                repo_id = _get_repo_id_from_repo_url(repository_url)
        repo_name = repo_id

        # No yml path == find or recommend yml scenario
        if not yml_path:
            logger.debug('No yml file was given. Trying to find the yml file in the repo.')
        new_pipeline_client = get_new_pipeline_client(organization=organization)
        yml_names = []
        yml_options = []

        # from vsts.cix.v5_1.models.configuration_file import ConfigurationFile
        configurations = new_pipeline_client.get_configurations(
            project=project, repository_type=repository_type,
            repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
        for configuration in configurations:
            logger.debug('The repo has a yml pipeline definition. Path: %s', configuration.path)
            custom_name = 'Existing yml (path={})'.format(configuration.path)
            yml_names.append(custom_name)
            yml_options.append(YmlOptions(custom_name, configuration.content))
        recommendations = new_pipeline_client.get_recommended_templates(
            project=project, repository_type=repository_type,
            repository_id=repo_id, branch=branch, service_connection_id=service_endpoint)
        logger.debug('List of recommended templates..')
        for recommendation in recommendations:
            logger.debug(recommendation.name)
            yml_names.append(recommendation.name)
            yml_options.append(YmlOptions(recommendation.name, recommendation.content,
                                          recommendation.description, recommendation.parameters))
        import webbrowser
        import tempfile
        filename = None
        proceed_selection = 1
        while proceed_selection == 1:
            selection_id = prompt_user_friendly_choice_list("Choose a yml template to create a pipeline:", yml_names)
            print("TODO: Ask for parameter or auto fill if possible.")
            _fp, filename = tempfile.mkstemp(text=True)
            f = open(filename, mode='w')
            f.write(yml_options[selection_id].content)
            f.close()
            # open the file
            webbrowser.open(filename)
            proceed_selection = prompt_user_friendly_choice_list(
                'Do you want to proceed creating a pipeline?',
                ['Use the created yml', 'Revisit recommendations', 'Exit'])
        # read data from file
        f = open(filename, mode='r')
        print(f.read())
        f.close()
        # import os
        # this is failing to remove ... os.remove(filename)
        print("TODO: Github Auth and checkin the template.")
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
        definition.repository.type = repository_type
        if service_endpoint:
            definition.repository.properties = _get_repo_properties_object(service_endpoint, branch)
        # Set build process
        definition.process = _create_process_object(yml_path)
        # set agent queue
        definition.queue = AgentPoolQueue()
        definition.queue.id = 163  # This should not be hardcoded

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


def pipeline_update():
    """Update a pipeline
    """
    pass


def pipeline_run(id=None, name=None, open=False, # pylint: disable=redefined-builtin
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
            pipeline_id = get_definition_id_from_name(name, client, project)
        definition_reference = DefinitionReference(id=pipeline_id)
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


def pipeline_tag(id=None, organization=None, project=None, detect=None):
    """Tag a pipeline.
    """
    pass


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
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_build/results?definitionId='\
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

def _parse_github_repo_info(github_repository):
    parsed_url = uri_parse(github_repository)
    logger.debug('Parsing github url: %s', parsed_url)
    if parsed_url.scheme == 'https' and parsed_url.netloc == 'github.com':
        # Parse path to find Id and yaml path
        logger.debug('Parsing path in the url to find repo branch and yml path')
        stripped_path = parsed_url.path.strip('/')
        if stripped_path.count('/') > 2:
            owner, repository_name, path = stripped_path.split('/', 2)
        else:
            raise CLIError('Repository could not be parsed to a yml file in a Github repository.')

        repo_id = '{owner}/{repo_name}'.format(owner=owner, repo_name=repository_name)
        repo_url = 'https://github.com/{id}.git'.format(id=repo_id)
        stripped_path = parsed_url.path.strip('/')

        path = path.strip('/')
        if path.count('/') > 1:
            blob, branch_name, yml_path = path.split('/', 2)
            yml_path = './{}'.format(yml_path)
        else:
            raise CLIError('Repository could not be parsed to a yml file in a Github repository.')

        if blob != 'blob':
            raise CLIError('Repository could not be parsed to a yml file in a Github repository.')

        return repo_url, repo_id, branch_name, yml_path
    else:
        raise CLIError('Repository could not be parsed to a yml file in a Github repository.')


def _get_repo_id_from_repo_url(repository_url):
    parsed_url = uri_parse(repository_url)
    logger.debug('Parsing github url: %s', parsed_url)
    if parsed_url.scheme == 'https' and parsed_url.netloc == 'github.com':
        logger.debug('Parsing path in the url to find repo id.')
        stripped_path = parsed_url.path.strip('')
        if stripped_path.endswith('.git'):
            stripped_path = stripped_path[:-4]
        return stripped_path.strip('/')
    raise CLIError('Could not parse repository url.')


def _get_repo_properties_object(service_endpoint, branch):
    return {
        "connectedServiceId": service_endpoint,
        "defaultBranch": branch
    }


def _create_process_object(yaml_path):
    return {
        "yamlFilename": yaml_path,
        "type": 2
    }
