# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import webbrowser

from knack.util import CLIError
from vsts.exceptions import VstsServiceError
from azext_devops.dev.common.services import (get_wiki_client,
                                              get_core_client,
                                              get_git_client,
                                              resolve_instance,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)


_DEFAULT_PAGE_ADD_MESSAGE = 'Added a new page using Azure DevOps CLI'
_DEFAULT_PAGE_UPDATE_MESSAGE = 'Updated the page using Azure DevOps CLI'
_DEFAULT_PAGE_DELETE_MESSAGE = 'Deleted the page using Azure DevOps CLI'

def create_wiki(name, wiki_type='projectwiki', mapped_path=None, version=None,
                organization=None, project=None, repository=None, detect=None):
    """Create a wiki.
    :param name: Name of the new wiki.
    :type name: str
    :param wiki_type: Type of wiki to create.
    :type wiki_type: str
    :param version: Version of the new wiki. Not required for project wiki. Repository branch name for code wiki.
    :type version: str
    :param mapped_path: Mapped path of the new wiki e.g. '/' to publish from root of repository.
    Not required for project wiki.
    :type mapped_path: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param repository: Name or ID of the repository.
    :type repository: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                              organization=organization,
                                                                              project=project,
                                                                              repo=repository)
        wiki_client = get_wiki_client(organization)
        from vsts.wiki.v4_1.models import WikiCreateParametersV2
        wiki_params = WikiCreateParametersV2()
        wiki_params.name = name
        wiki_params.type = wiki_type
        project_id = _get_project_id_from_name(organization=organization,
                                               project=project)
        wiki_params.project_id = project_id
        repository_id = _get_repository_id_from_name(organization=organization,
                                                     project=project,
                                                     repository=repository)
        wiki_params.repository_id = repository_id
        if mapped_path:
            wiki_params.mapped_path = mapped_path
        if version:
            from vsts.wiki.v4_1.models import GitVersionDescriptor
            version_descriptor = GitVersionDescriptor()
            version_descriptor.version = version
            wiki_params.version = version_descriptor
        return wiki_client.create_wiki(wiki_create_params=wiki_params, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_wiki(wiki, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a wiki.
    :param wiki: Name or Id of the wiki to delete.
    :type wiki: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        return wiki_client.delete_wiki(wiki_identifier=wiki, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def list_wiki(organization=None, project=None, detect=None):
    """List all the wikis in a project or organization.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization = resolve_instance(detect=detect,
                                        organization=organization)
        wiki_client = get_wiki_client(organization)
        return wiki_client.get_all_wikis(project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def show_wiki(wiki, organization=None, project=None, detect=None):
    """Show details of a wiki.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        return wiki_client.get_wiki(wiki_identifier=wiki, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def add_page(wiki, path, comment=_DEFAULT_PAGE_ADD_MESSAGE, content=None, file_path=None,
             organization=None, project=None, detect=None):
    """Add a new page.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param content: Content of the wiki page. Ignored if --file-path is specified.
    :type content: str
    :param file_path: Path of the file input if content is specified in the file.
    :type file_path: str
    :param comment: Comment in the commit message of file add operation.
    :type comment: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        if not content and not file_path:
            raise CLIError('Either --file-path or --content must be specified.')
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        from vsts.wiki.v4_1.models import WikiPageCreateOrUpdateParameters
        parameters = WikiPageCreateOrUpdateParameters()
        if content:
            parameters.content = content
        if file_path:
            fp = open(file_path, mode='r')
            parameters.content = fp.read()
            fp.close()
        return wiki_client.create_or_update_page(parameters=parameters, wiki_identifier=wiki,
                                                 project=project, path=path, version=None, comment=comment)
    except VstsServiceError as ex:
        raise CLIError(ex)



def update_page(wiki, path, comment=_DEFAULT_PAGE_UPDATE_MESSAGE, content=None, file_path=None,
                page_version=None, organization=None, project=None, detect=None):
    """Edit a page.
     :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param content: Content of the wiki page. Ignored if --file-path is specified.
    :type content: str
    :param file_path: Path of the file input if content is specified in the file.
    :type file_path: str
    :param comment: Comment in the commit message of file edit operation.
    :type comment: str
    :param page_version: Version of file to edit.
    :type page_version: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        if not content and not file_path:
            raise CLIError('Either --file-path or --content must be specified.')
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        from vsts.wiki.v4_1.models import WikiPageCreateOrUpdateParameters
        parameters = WikiPageCreateOrUpdateParameters()
        if content:
            parameters.content = content
        if file_path:
            fp = open(file_path, mode='r')
            parameters.content = fp.read()
            fp.close()
        return wiki_client.create_or_update_page(parameters=parameters, wiki_identifier=wiki,
                                                 project=project, path=path, version=page_version, comment=comment)
    except VstsServiceError as ex:
        raise CLIError(ex)


def get_page(wiki, path, version=None, recursion_level=None, open=False,
             include_content=False, organization=None, project=None, detect=None):
    """Get the content of a page or open a page.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param version: Version of the wiki page.
    :type version: str
    :param recursion_level: Recursion level of the wiki page.
    :type recursion_level: str
    :param include_content: Include content of the page. 
    :type include_content: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param open: Open the pull request in your web browser.
    :type open: bool
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        page_object = wiki_client.get_page(
            wiki_identifier=wiki, project=project, path=path,
            recursion_level=recursion_level, version_descriptor=version,
            include_content=include_content)
        if open:
            webbrowser.open_new(url=page_object.page.remote_url)
        return page_object

    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_page(wiki, path, comment=_DEFAULT_PAGE_DELETE_MESSAGE, organization=None, project=None, detect=None):
    """Delete a page.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param comment: Comment in the commit message of delete operation.
    :type comment: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        wiki_client = get_wiki_client(organization)
        return wiki_client.delete_page(wiki_identifier=wiki, path=path, comment=comment, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def _get_project_id_from_name(organization, project):
    core_client = get_core_client(organization)
    team_project = core_client.get_project(project_id=project)
    return team_project.id


def _get_repository_id_from_name(organization, project, repository):
    git_client = get_git_client(organization)
    repository = git_client.get_repository(project=project, repository_id=repository)
    return repository.id
