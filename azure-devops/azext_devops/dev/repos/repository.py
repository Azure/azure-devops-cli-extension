# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import webbrowser

from knack.util import CLIError
from knack.log import get_logger
from vsts.exceptions import VstsServiceError
from vsts.git.v4_0.models.git_repository_create_options import GitRepositoryCreateOptions
from azext_devops.dev.common.services import (get_git_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.uri import uri_quote


logger = get_logger(__name__)


def create_repo(name, organization=None, project=None, detect=None, open=False):  # pylint: disable=redefined-builtin
    """Create a Git repository in a team project.
    :param name: Name for the new repository.
    :type name: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :param open: Open the repository page in your web browser.
    :type open: bool
    :rtype: :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        git_client = get_git_client(organization)
        create_options = GitRepositoryCreateOptions()
        create_options.name = name
        repository = git_client.create_repository(git_repository_to_create=create_options,
                                                  project=project)
        if open:
            _open_repository(repository, organization)
        return repository
    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_repo(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a Git repository in a team project.
    :param id: ID of the repository.
    :type id: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        git_client = get_git_client(organization)
        delete_response = git_client.delete_repository(project=project, repository_id=id)
        print('Deleted repository {}'.format(id))
        return delete_response
    except VstsServiceError as ex:
        raise CLIError(ex)


def list_repos(organization=None, project=None, detect=None):
    """List Git repositories of a team project.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: list of :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        git_client = get_git_client(organization)
        repository = git_client.get_repositories(project=project)
        return repository
    except VstsServiceError as ex:
        raise CLIError(ex)


def show_repo(repo, organization=None, project=None, detect=None, open=False):  # pylint: disable=redefined-builtin
    """Get the details of a Git repository.
    :param repo: ID or name of the repository.
    :type repo: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization, project and repository. Default is "on".
    :type detect: str
    :param open: Open the repository page in your web browser.
    :type open: bool
    :rtype: :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        organization, project, repo = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            project_required=True,
            repo=repo)
        git_client = get_git_client(organization)
        repository = git_client.get_repository(project=project, repository_id=repo)
        if open:
            _open_repository(repository, organization)
        return repository
    except VstsServiceError as ex:
        raise CLIError(ex)


def _open_repository(repository, organization):
    """Opens the pull request in the default browser.
    :param repository: The repository to open.
    :type repository: str
    """
    url = organization.rstrip('/') + '/' + uri_quote(repository.project.name)\
        + '/_git/' + uri_quote(repository.name)
    logger.debug('Opening web page: %s', url)
    webbrowser.open_new(url=url)
