# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import urllib
import webbrowser

from knack.util import CLIError
from vsts.git.v4_0.models.git_repository_create_options import GitRepositoryCreateOptions
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.vsts import (get_base_url,
                                  get_git_client,
                                  resolve_instance_and_project)


def create_repo(name, team_instance=None, project=None, detect=None, open_browser=False):
    """Creates a new repository on the server
    :param name: The name of the new repository.
    :type name: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :param open_browser: Open the repository in the default web browser.
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
    """List all the repositories in the specified team project.
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
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
    """Shows information about a repository.
    :param repo_id: The UUID of the Repository to show.  Required if --name is not specified.
    :type repo_id: int
    :param name: The name of the repository to show.  Ignored if --id is specified.
    :type name: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :param open_browser: Open the repository in the default web browser.
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
    url = team_instance.rstrip('/') + '/' + urllib.parse.quote(repository.project.name)\
        + '/_git/' + urllib.parse.quote(repository.name)
    logging.debug('Opening web page: %s', url)
    webbrowser.open_new(url=url)
