# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import base64
from .item_content import ItemContent
from vsts.git.v4_0.models.change import Change
from vsts.git.v4_0.models.git_item import GitItem
from vsts.git.v4_0.models.git_change import GitChange
from vsts.git.v4_0.models.git_commit_ref import GitCommitRef
from vsts.git.v4_0.models.git_push import GitPush
from vsts.git.v4_0.models.git_push_ref import GitPushRef
from vsts.git.v4_0.models.git_ref_update import GitRefUpdate
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.git import resolve_git_ref_heads
from vsts.cli.common.services import (get_git_client,
                                      resolve_instance,
                                      resolve_instance_project_and_repo)


def show_push(push_id, include_commits=False, include_ref_updates=False, repository=None, project=None, team_instance=None, detect=None):
    """Get the details of a push.
    :param int push_id: ID of the push to retrieve.
    :param bool include_commits: Include commits of the push.
    :param bool include_ref_updates: Include updates of the push.
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        return client.get_push(push_id=push_id,
                               include_commits=include_commits,
                               include_ref_updates=include_ref_updates,
                               repository_id=repository,
                               project=project)
    except Exception as ex:
        handle_command_exception(ex)


def create_push_add(target_branch, object_id, comment, path, filename, binary=False, repository=None, project=None, team_instance=None, detect=None):
    """Create a push to add a file.
    :param str target_branch: Name of the target branch.
    :param str object_id: ID of the object the commit is based on.
    :param str comment: Comment of the commit.
    :param str path: Absolute path (in the repository) of the file.
    :param str filename: Name of the file to import as data.
    :param bool binary: Treat input file as binary (default False).
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)

        push = _create_file_push(change_type='add',
                                 target_branch=target_branch,
                                 object_id=object_id,
                                 comment=comment,
                                 path=path,
                                 filename=filename,
                                 binary=binary)
        return client.create_push(push=push, repository_id=repository, project=project)
    except Exception as ex:
        handle_command_exception(ex)


def create_push_update(target_branch, object_id, comment, path, filename, binary=False, repository=None, project=None, team_instance=None, detect=None):
    """Create a push to update a file.
    :param str target_branch: Name of the target branch.
    :param str object_id: ID of the object the commit is based on.
    :param str comment: Comment of the commit.
    :param str path: Absolute path (in the repository) of the file.
    :param str filename: Name of the file to import as data.
    :param bool binary: Treat input file as binary (default False).
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)

        push = _create_file_push(change_type='edit',
                                 target_branch=target_branch,
                                 object_id=object_id,
                                 comment=comment,
                                 path=path,
                                 filename=filename,
                                 binary=binary)
        return client.create_push(push=push, repository_id=repository, project=project)
    except Exception as ex:
        handle_command_exception(ex)


def _create_file_push(change_type, target_branch, object_id, comment, path, filename, binary):
    with open(filename, 'r') as input:
        data = input.read()

    ref_update = GitRefUpdate(name=resolve_git_ref_heads(target_branch),
                              old_object_id=object_id)
    content = ItemContent(content=base64.b64encode(data) if binary else data,
                          contentType='base64encoded' if binary else 'rawText')
    change = Change(change_type=change_type,
                    item=GitItem(path=path),
                    new_content=content)
    commit = GitCommitRef(comment=comment, changes=[ change ])
    return GitPush(ref_updates=[ ref_update ], commits=[ commit ])


def create_push_delete(target_branch, object_id, comment, path, repository=None, project=None, team_instance=None, detect=None):
    """Create a push to delete a file.
    :param str target_branch: Name of the target branch.
    :param str object_id: ID of the object the commit is based on.
    :param str comment: Comment of the commit.
    :param str path: Absolute path (in the repository) of the file.
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)

        ref_update = GitRefUpdate(name=resolve_git_ref_heads(target_branch),
                                  old_object_id=object_id)
        change = Change(change_type='delete',
                        item=GitItem(path=path))
        commit = GitCommitRef(comment=comment, changes=[ change ])
        push = GitPush(ref_updates=[ ref_update ], commits=[ commit ])
        return client.create_push(push=push, repository_id=repository, project=project)
    except Exception as ex:
        handle_command_exception(ex)


def create_push_rename(target_branch, object_id, comment, old_path, new_path, repository=None, project=None, team_instance=None, detect=None):
    """Create a push to rename a file.
    :param str target_branch: Name of the target branch.
    :param str object_id: ID of the object the commit is based on.
    :param str comment: Comment of the commit.
    :param str old_path: Absolute source path (in the repository) of the file to rename.
    :param str new_path: Absolute destination path (in the repository) of the file to rename.
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)

        ref_update = GitRefUpdate(name=resolve_git_ref_heads(target_branch),
                                  old_object_id=object_id)
        change = Change(change_type='rename',
                        source_server_item=old_path,
                        item=GitItem(path=new_path))
        commit = GitCommitRef(comment=comment, changes=[ change ])
        push = GitPush(ref_updates=[ ref_update ], commits=[ commit ])
        return client.create_push(push=push, repository_id=repository, project=project)
    except Exception as ex:
        handle_command_exception(ex)
