# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import webbrowser
from knack.util import CLIError
from azext_devops.dev.common.services import (get_wiki_client,
                                              get_git_client,
                                              get_project_id_from_name,
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
    :param version: [Required for codewiki type] Repository branch name to publish the code wiki from.
    :type version: str
    :param mapped_path: [Required for codewiki type] Mapped path of the new wiki
    e.g. '/' to publish from root of repository.
    :type mapped_path: str
    :param repository: [Required for codewiki type] Name or ID of the repository to publish the wiki from.
    :type repository: str
    """
    repository_id = None
    if wiki_type == 'codewiki':
        organization, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                              organization=organization,
                                                                              project=project,
                                                                              repo=repository,
                                                                              repo_required=True)
        repository_id = _get_repository_id_from_name(organization=organization,
                                                     project=project,
                                                     repository=repository)
    else:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
    wiki_client = get_wiki_client(organization)
    from azext_devops.devops_sdk.v5_0.wiki.models import WikiCreateParametersV2
    wiki_params = WikiCreateParametersV2()
    wiki_params.name = name
    wiki_params.type = wiki_type
    project_id = get_project_id_from_name(organization=organization,
                                          project=project)
    wiki_params.project_id = project_id
    wiki_params.repository_id = repository_id
    if mapped_path:
        wiki_params.mapped_path = mapped_path
    if version:
        from azext_devops.devops_sdk.v5_0.wiki.models import GitVersionDescriptor
        version_descriptor = GitVersionDescriptor()
        version_descriptor.version = version
        wiki_params.version = version_descriptor
    return wiki_client.create_wiki(wiki_create_params=wiki_params, project=project)


def delete_wiki(wiki, organization=None, project=None, detect=None):
    """Delete a wiki.
    :param wiki: Name or Id of the wiki to delete.
    :type wiki: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    wiki_client = get_wiki_client(organization)
    return wiki_client.delete_wiki(wiki_identifier=wiki, project=project)


def list_wiki(scope='project', organization=None, project=None, detect=None):
    """List all the wikis in a project or organization.
    :param scope: List the wikis at project or organization level.
    :type scope: str
    """
    if scope == 'project':
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
    else:
        organization = resolve_instance(detect=detect,
                                        organization=organization)
    wiki_client = get_wiki_client(organization)
    return wiki_client.get_all_wikis(project=project)


def show_wiki(wiki, open=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details of a wiki.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param open: Open the wiki in your web browser.
    :type open: bool
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    wiki_client = get_wiki_client(organization)
    wiki_object = wiki_client.get_wiki(wiki_identifier=wiki, project=project)
    if open:
        webbrowser.open_new(url=wiki_object.remote_url)
    return wiki_object


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
    """
    if not content and not file_path:
        raise CLIError('Either --file-path or --content must be specified.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    wiki_client = get_wiki_client(organization)
    from azext_devops.devops_sdk.v5_0.wiki.models import WikiPageCreateOrUpdateParameters
    parameters = WikiPageCreateOrUpdateParameters()
    if content:
        parameters.content = content
    if file_path:
        fp = open(file_path, mode='r')
        parameters.content = fp.read()
        fp.close()
    return wiki_client.create_or_update_page(parameters=parameters, wiki_identifier=wiki,
                                             project=project, path=path, version=None, comment=comment)


def update_page(wiki, path, version, comment=_DEFAULT_PAGE_UPDATE_MESSAGE, content=None, file_path=None,
                organization=None, project=None, detect=None):
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
    :param version: Version (ETag) of file to edit.
    :type version: str
    """
    if not content and not file_path:
        raise CLIError('Either --file-path or --content must be specified.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    wiki_client = get_wiki_client(organization)
    from azext_devops.devops_sdk.v5_0.wiki.models import WikiPageCreateOrUpdateParameters
    parameters = WikiPageCreateOrUpdateParameters()
    if content:
        parameters.content = content
    if file_path:
        fp = open(file_path, mode='r')
        parameters.content = fp.read()
        fp.close()
    return wiki_client.create_or_update_page(parameters=parameters, wiki_identifier=wiki,
                                             project=project, path=path, version=version, comment=comment)


def get_page(wiki, path, version=None, recursion_level=None, open=False,  # pylint: disable=redefined-builtin
             include_content=False, organization=None, project=None, detect=None):
    """Get the content of a page or open a page.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param version: Version (ETag) of the wiki page.
    :type version: str
    :param recursion_level: Recursion level of the wiki page.
    :type recursion_level: str
    :param include_content: Include content of the page.
    :type include_content: str
    :param open: Open the wiki page in your web browser.
    :type open: bool
    """
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


def delete_page(wiki, path, comment=_DEFAULT_PAGE_DELETE_MESSAGE, organization=None, project=None, detect=None):
    """Delete a page.
    :param wiki: Name or Id of the wiki.
    :type wiki: str
    :param path: Path of the wiki page.
    :type path: str
    :param comment: Comment in the commit message of delete operation.
    :type comment: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    wiki_client = get_wiki_client(organization)
    return wiki_client.delete_page(wiki_identifier=wiki, path=path, comment=comment, project=project)


def _get_repository_id_from_name(organization, project, repository):
    git_client = get_git_client(organization)
    repository = git_client.get_repository(project=project, repository_id=repository)
    return repository.id
