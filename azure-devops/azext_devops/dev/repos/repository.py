# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import webbrowser

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.devops_sdk.v5_0.git.models import GitRepositoryCreateOptions
from azext_devops.dev.common.services import (get_git_client,
                                              resolve_instance_and_project,
                                              resolve_instance_project_and_repo)
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.uri import uri_quote


logger = get_logger(__name__)


def create_repo(name, organization=None, project=None, detect=None, open=None):  # pylint: disable=redefined-builtin
    """Create a Git repository in a team project.
    :param name: Name for the new repository.
    :type name: str
    :param open: Open the repository page in your web browser.
    :type open: bool
    :rtype: :class:`<GitRepository> <v5_0.git.models.GitRepository>`
    """
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


def delete_repo(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a Git repository in a team project.
    :param id: ID of the repository.
    :type id: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    git_client = get_git_client(organization)
    delete_response = git_client.delete_repository(project=project, repository_id=id)
    print('Deleted repository {}'.format(id))
    return delete_response


def list_repos(organization=None, project=None, detect=None):
    """List Git repositories of a team project.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    git_client = get_git_client(organization)
    repository = git_client.get_repositories(project=project)
    return repository


def update_repo(repository, default_branch=None, name=None, organization=None, project=None, detect=None):
    """Update the Git repository.
    :param repository: Name or ID of the repository.
    :type repository: str
    :param name: New name for the repository.
    :type name: str
    :param default_branch: Default branch to be set for the repository. Example: 'refs/heads/live' or 'live'.
    :type default_branch: str
    """
    if not default_branch and not name:
        raise CLIError("Either --default-branch or --name (for rename) must be provided to update repository.")
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect,
        organization=organization,
        project=project,
        project_required=True,
        repo=repository)
    git_client = get_git_client(organization)
    # Get the repo to be updated
    repository = git_client.get_repository(project=project, repository_id=repository)
    if default_branch:
        default_branch = resolve_git_ref_heads(default_branch)
        repository.default_branch = default_branch
    if name:
        repository.name = name
    repository = git_client.update_repository(
        project=project, repository_id=repository.id, new_repository_info=repository)
    return repository


def show_repo(repository, organization=None, project=None, detect=None, open=None):  # pylint: disable=redefined-builtin
    """Get the details of a Git repository.
    :param repository: Name or ID of the repository.
    :type repository: str
    :param open: Open the repository page in your web browser.
    :type open: bool
    :rtype: :class:`<GitRepository> <v5_0.git.models.GitRepository>`
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect,
        organization=organization,
        project=project,
        project_required=True,
        repo=repository)
    git_client = get_git_client(organization)
    repository = git_client.get_repository(project=project, repository_id=repository)
    if open:
        _open_repository(repository, organization)
    return repository


def _open_repository(repository, organization):
    """Opens the pull request in the default browser.
    :param repository: The repository to open.
    :type repository: str
    """
    url = organization.rstrip('/') + '/' + uri_quote(repository.project.name)\
        + '/_git/' + uri_quote(repository.name)
    logger.debug('Opening web page: %s', url)
    webbrowser.open_new(url=url)
