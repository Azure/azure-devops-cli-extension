# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.git.v4_0.models.git_ref_update import GitRefUpdate
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.git import resolve_git_refs
from vsts.cli.common.services import (get_git_client,
                                      resolve_instance,
                                      resolve_instance_project_and_repo)

def list_refs(filter=None, repository=None, team_instance=None, project=None, detect=None):
    """List the references.
    :param str filter: Filter to apply to the refs.
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance,project=project,repo=repository)
        client = get_git_client(team_instance)
        return client.get_refs(repository_id=repository,
                               project=project,
                               filter=filter)
    except Exception as ex:
        handle_command_exception(ex)


def create_ref(name, object_id, locked=False, repository=None, team_instance=None, project=None, detect=None):
    """Create a reference.
    :param str name: Name of the reference to create (example: heads/my_branch).
    :param str object_id: id of the object to create the reference from.
    :param bool locked: If the reference is locked (default False)
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        ref_update = GitRefUpdate(is_locked=locked,
                                  name=resolve_git_refs(name),
                                  new_object_id=object_id,
                                  old_object_id='0000000000000000000000000000000000000000')
        return client.update_refs([ ref_update ], repository, project)[0]
    except Exception as ex:
        handle_command_exception(ex)


def delete_ref(name, object_id, repository=None, team_instance=None, project=None, detect=None):
    """Delete a reference.
    :param str name: Name of the reference to create (example: heads/my_branch).
    :param str object_id: id of the reference to delete.
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        ref_update = GitRefUpdate(name=resolve_git_refs(name),
                                  new_object_id='0000000000000000000000000000000000000000',
                                  old_object_id=object_id)
        return client.update_refs([ ref_update ], repository, project)[0]
    except Exception as ex:
        handle_command_exception(ex)


def update_ref(name, old_object_id, new_object_id, repository=None, team_instance=None, project=None, detect=None):
    """Update a reference.
    :param str name: Name of the reference to create (example: heads/my_branch).
    :param str old_object_id: id of the old reference.
    :param str new_object_id: id of the new reference.
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        ref_update = GitRefUpdate(name=resolve_git_refs(name),
                                  new_object_id=new_object_id,
                                  old_object_id=old_object_id)
        return client.update_refs([ ref_update ], repository, project)[0]
    except Exception as ex:
        handle_command_exception(ex)
