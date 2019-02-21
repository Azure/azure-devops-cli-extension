# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.dev.common.services import (get_build_client, get_git_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_quote
from azext_devops.dev.common.uuid import is_uuid

logger = get_logger(__name__)


def build_definition_list(name=None, top=None, organization=None, project=None, repository=None,
                          repository_type=None, detect=None):
    """List build definitions.
    :param name: Limit results to definitions with this name or starting with this name. Examples: "FabCI" or "Fab*"
    :type name: bool
    :param top: Maximum number of definitions to list.
    :type top: int
    :param repository: Limit results to definitions associated with this repository.
    :type repository: str
    :param repository_type: Limit results to definitions associated with this repository type.
    It is mandatory to pass 'repository' argument along with this argument.
    :type repository_type: str
    :rtype: [BuildDefinitionReference]
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect, organization=organization, project=project, repo=repository)
    client = get_build_client(organization)
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


def build_definition_show(id=None, name=None, open=False, organization=None, project=None,  # pylint: disable=redefined-builtin
                          detect=None):
    """Get the details of a build definition.
    :param id: ID of the definition.
    :type id: int
    :param name: Name of the definition. Ignored if --id is supplied.
    :type name: str
    :param open: Open the definition summary page in your web browser.
    :type open: bool
    :rtype: BuildDefinitionReference
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    if id is None:
        if name is not None:
            id = get_definition_id_from_name(name, client, project)
        else:
            raise ValueError("Either the --id argument or the --name argument must be supplied for this command.")
    build_definition = client.get_definition(definition_id=id, project=project)
    if open:
        _open_definition(build_definition, organization)
    return build_definition


def _open_definition(definition, organization):
    """Opens the build definition in the default browser.
    :param :class:`<BuildDefinitionReference> <build.v4_0.models.BuildDefinitionReference>` definition:
    :param str organization:
    """
    # https://dev.azure.com/OrgName/ProjectName/_build/index?definitionId=1234
    project = definition.project.name
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_build/index?definitionId='\
        + uri_quote(str(definition.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)


def get_definition_id_from_name(name, client, project):
    definition_references = client.get_definitions(project=project, name=name)
    if len(definition_references) == 1:
        return definition_references[0].id
    elif len(definition_references) > 1:
        if is_uuid(project):
            project = definition_references[0].project.name
        message = 'Multiple definitions were found matching name "{name}" in project "{project}".  Try '\
                  + 'supplying the definition ID.'
        raise ValueError(message.format(name=name, project=project))
    else:
        raise ValueError('There were no build definitions matching name "{name}" in project "{project}".'
                         .format(name=name, project=project))


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
