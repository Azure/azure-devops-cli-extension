# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import webbrowser

from knack.util import CLIError
from vsts.git.v4_0.models.git_repository_create_options import GitRepositoryCreateOptions
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_git_client,
                                      resolve_instance_and_project)
from vsts.cli.common.uri import uri_quote


def create_repo(name, team_instance=None, project=None, detect=None, open_browser=False):
    """Create a Git repository in a team project.
    :param name: Name for the new repository.
    :type name: int
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :param open_browser: Open the repository page in your web browser.
    :type open_browser: bool
    :rtype: :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        team_instance, project = resolve_instance_and_project(detect=detect,
                                                              team_instance=team_instance,
                                                              project=project)
        git_client = get_git_client(team_instance)
        create_options = GitRepositoryCreateOptions()
        create_options.name = name
        repository = git_client.create_repository(git_repository_to_create=create_options,
                                                  project=project)
        if open_browser:
            _open_repository(repository, team_instance)
        return repository
    except Exception as ex:
        handle_command_exception(ex)


def list_repos(team_instance=None, project=None, detect=None):
    """List Git repositories of a team project.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: list of :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        team_instance, project = resolve_instance_and_project(detect=detect,
                                                              team_instance=team_instance,
                                                              project=project)
        git_client = get_git_client(team_instance)
        repository = git_client.get_repositories(project=project)
        return repository
    except Exception as ex:
        handle_command_exception(ex)


def show_repo(repo_id=None, name=None, team_instance=None, project=None, detect=None, open_browser=False):
    """Get the details of a Git repository.
    :param repo_id: ID of the repository. Required if --name is not specified.
    :type repo_id: int
    :param name: Name of the repository. Ignored if --id is specified.
    :type name: int
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :param open_browser: Open the repository page in your web browser.
    :type open_browser: bool
    :rtype: :class:`<GitRepository> <git.v4_0.models.GitRepository>`
    """
    try:
        if repo_id is None and name is None:
            raise CLIError('Either the --name argument or the --id argument needs to be specified.')
        if repo_id is not None:
            identifier = repo_id
        else:
            identifier = name
        team_instance, project = resolve_instance_and_project(detect=detect,
                                                              team_instance=team_instance,
                                                              project=project)
        git_client = get_git_client(team_instance)
        repository = git_client.get_repository(project=project, repository_id=identifier)
        if open_browser:
            _open_repository(repository, team_instance)
        return repository
    except Exception as ex:
        handle_command_exception(ex)


def _open_repository(repository, team_instance):
    """Opens the pull request in the default browser.
    :param repository: The repository to open.
    :type repository: str
    """
    url = team_instance.rstrip('/') + '/' + uri_quote(repository.project.name)\
        + '/_git/' + uri_quote(repository.name)
    logging.debug('Opening web page: %s', url)
    webbrowser.open_new(url=url)
