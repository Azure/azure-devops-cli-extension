# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from vsts.exceptions import VstsServiceError
from azext_devops.dev.common.services import (get_wiki_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)


def create_wiki(name, wiki_type='projectWiki', mapped_path='./', version=None,
                organization=None, project=None, repository=None, detect=None):
    """Create a wiki.
    :param name: Name of the new wiki.
    :type name: str
    :param wiki_type: Type of the new wiki.
    :type wiki_type: str
    :param version: Version of the new wiki.
    :type version: str
    :param mapped_path: Mapped path of the new wiki.
    :type mapped_path: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param Repository: Name or ID of the repository.
    :type Repository: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                              organization=organization,
                                                                              project=project,
                                                                              repo=repository)
        wiki_client = get_wiki_client(organization)
        from vsts.wiki.v5_1.models import WikiCreateParametersV2
        wiki_params = WikiCreateParametersV2()
        wiki_params.name = name
        wiki_params.type = wiki_type
        wiki_params.project_id = project
        wiki_params.repository_id = repository
        if mapped_path:
            wiki_params.mapped_path = mapped_path
        if version:
            from vsts.wiki.v5_1.models import GitVersionDescriptor
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
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project,
                                                             project_required=False)
        wiki_client = get_wiki_client(organization)
        return wiki_client.get_all_wikis(project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def show_wiki(wiki, organization=None, project=None, detect=None):
    """Show details of a wiki.
    :param wiki: Name or Id of the new wiki.
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
