# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new
from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.services import (get_build_client,
                                              get_git_client,
                                              resolve_instance_and_project,
                                              get_new_pipeline_client_v60)
from azext_devops.dev.common.uri import uri_quote
from azext_devops.dev.common.uuid import is_uuid
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.devops_sdk.v5_0.build.models import Build, DefinitionReference
from azext_devops.devops_sdk.v6_0.pipelines.models import (RunPipelineParameters,
                                                           RunResourcesParameters,
                                                           RepositoryResourceParameters)
from .build_definition import get_definition_id_from_name, fix_path_for_api
from .pipeline_run import _open_pipeline_run, _open_pipeline_run6_0

logger = get_logger(__name__)


def pipeline_list(name=None, top=None, organization=None, project=None, repository=None, query_order=None,
                  folder_path=None, repository_type=None, detect=None):
    """ List pipelines.
    :param name: Limit results to pipelines with this name or starting with this name. Examples: "FabCI" or "Fab*"
    :type name: str
    :param top: Maximum number of pipelines to list.
    :type top: int
    :param query_order: Order of the results.
    :type query_order: str
    :param repository: Limit results to pipelines associated with this repository.
    :type repository: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    :param folder_path: If specified, filters to definitions under this folder.
    :type folder_path: str
    :param repository_type: Limit results to pipelines associated with this repository type.
    It is mandatory to pass 'repository' argument along with this argument.
    :type repository_type: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    query_order = _resolve_query_order(query_order)
    if repository is not None:
        if repository_type is None:
            repository_type = 'TfsGit'
        if repository_type.lower() == 'tfsgit':
            repository = _resolve_repository_as_id(repository, organization, project)
        if repository is None:
            raise ValueError("Could not find a repository with name '{}', in project '{}'."
                             .format(repository, project))
    folder_path = fix_path_for_api(folder_path)
    definition_references = client.get_definitions(project=project, name=name, repository_id=repository,
                                                   repository_type=repository_type, top=top, path=folder_path,
                                                   query_order=query_order)
    return definition_references


def _resolve_query_order(query_order):
    if query_order:
        query_order_vals = ['definitionNameAscending', 'definitionNameDescending', 'lastModifiedAscending',
                            'lastModifiedDescending', 'none']
        for val in query_order_vals:
            if query_order.lower() in val.lower():
                return val
        logger.warning("Cannot resolve --query-order, continuing with 'none'")
    return 'none'


def pipeline_show(id=None, name=None, open=False, organization=None, project=None,  # pylint: disable=redefined-builtin
                  folder_path=None, detect=None):
    """ Get the details of a pipeline.
    :param id: ID of the pipeline.
    :type id: int
    :param name: Name of the pipeline. Ignored if --id is supplied.
    :type name: str
    :param folder_path: Folder path of pipeline. Default is root level folder.
    :type folder_path: str
    :param open: Open the pipeline summary page in your web browser.
    :type open: bool
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    if id is None:
        if name is not None:
            id = get_definition_id_from_name(name, client, project, path=folder_path)
        else:
            raise CLIError("Either the --id argument or the --name argument must be supplied for this command.")
    build_definition = client.get_definition(definition_id=id, project=project)
    if open:
        _open_pipeline(build_definition, organization)
    return build_definition


def set_param_variable(variables, as_dict=False, argument='variables'):
    param_variables = None
    if variables is not None and variables:
        param_variables = {}
        for variable in variables:
            separator_pos = variable.find('=')
            if separator_pos >= 0:
                if as_dict:
                    param_variables[variable[:separator_pos]] = {"value": variable[separator_pos + 1:]}
                else:
                    param_variables[variable[:separator_pos]] = variable[separator_pos + 1:]
            else:
                raise ValueError(
                    f'The --{argument} argument should consist of space separated "name=value" pairs.')
    return param_variables


def pipeline_run(id=None, branch=None, commit_id=None, name=None, open=False, variables=None,  # pylint: disable=redefined-builtin
                 folder_path=None, organization=None, project=None, detect=None, parameters=None):
    """ Queue (run) a pipeline.
    :param id: ID of the pipeline to queue. Required if --name is not supplied.
    :type id: int
    :param name: Name of the pipeline to queue. Ignored if --id is supplied.
    :type name: str
    :param branch: Name of the branch on which the pipeline run is to be queued. Example: refs/heads/master or master
    or refs/pull/1/merge or refs/tags/tag
    :type branch: str
    :param folder_path: Folder path of pipeline. Default is root level folder.
    :type folder_path: str
    :param variables: Space separated "name=value" pairs for the variables you would like to set.
    :type variables: [str]
    :param parameters: Space separated "name=value" pairs for the parameters you would like to set.
    :type parameters: [str]
    :param commit_id: Commit-id on which the pipeline run is to be queued.
    :type commit_id: str
    :param open: Open the pipeline results page in your web browser.
    :type open: bool
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if id is None and name is None:
        raise ValueError('Either the --id argument or the --name argument ' +
                         'must be supplied for this command.')
    client = get_build_client(organization)

    if id is None:
        id = get_definition_id_from_name(name, client, project, folder_path)

    if parameters:
        logger.debug('Using "pipelines client v6_0" to include parameters in run')
        client = get_new_pipeline_client_v60(organization)

        repositories = {"self": RepositoryResourceParameters(ref_name=branch, version=commit_id)}
        resources = RunResourcesParameters(repositories=repositories)
        template_parameters = set_param_variable(parameters, argument='parameters')

        param_variables = set_param_variable(variables, as_dict=True)
        run_parameters = RunPipelineParameters(
            resources=resources, variables=param_variables, template_parameters=template_parameters)

        queued_pipeline = client.run_pipeline(run_parameters=run_parameters, project=project, pipeline_id=id)
        if open:
            _open_pipeline_run6_0(queued_pipeline, project, organization)
        return queued_pipeline

    definition_reference = DefinitionReference(id=id)
    branch = resolve_git_ref_heads(branch)
    build = Build(definition=definition_reference, source_branch=branch, source_version=commit_id)

    param_variables = set_param_variable(variables)
    build.parameters = param_variables

    queued_build = client.queue_build(build=build, project=project)

    if open:
        _open_pipeline_run(queued_build, organization)
    return queued_build


def pipeline_delete(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """ Delete a pipeline.
    :param id: ID of the pipeline.
    :type id: int
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    build = client.delete_definition(definition_id=id, project=project)
    print('Pipeline {id} was deleted successfully.'.format(id=id))
    return build


def _open_pipeline(definition, organization):
    """Opens the build definition in the default browser.
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
    git_client = get_git_client(organization)
    repositories = git_client.get_repositories(project=project, include_links=False, include_all_urls=False)
    for found_repository in repositories:
        if found_repository.name.lower() == repository.lower():
            return found_repository.id
    return None
