# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from vsts.git.v4_0.models.git_ref_update import GitRefUpdate
from vsts.exceptions import VstsServiceError
from azext_devops.dev.common.git import resolve_git_refs
from azext_devops.dev.common.services import (get_git_client,
                                              resolve_instance_project_and_repo)


# pylint: disable=redefined-builtin
def list_refs(filter=None, repository=None, organization=None, project=None, detect=None):
    """List the references.
    :param str filter: A filter to apply to the refs (starts with). Example: head or heads/ for the branches.
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            repo=repository)
        client = get_git_client(organization)
        return client.get_refs(repository_id=repository,
                               project=project,
                               filter=filter)
    except VstsServiceError as ex:
        raise CLIError(ex)


def create_ref(name, object_id, locked=False, repository=None, organization=None, project=None, detect=None):
    """Create a reference.
    :param str name: Name of the reference to create (example: heads/my_branch or tags/my_tag).
    :param str object_id: Id of the object to create the reference from.
    :param bool locked: If the reference is locked (default False)
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            repo=repository)
        client = get_git_client(organization)
        ref_update = GitRefUpdate(is_locked=locked,
                                  name=resolve_git_refs(name),
                                  new_object_id=object_id,
                                  old_object_id='0000000000000000000000000000000000000000')
        return client.update_refs(ref_updates=[ref_update],
                                  repository_id=repository,
                                  project=project)[0]
    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_ref(name, object_id, repository=None, organization=None, project=None, detect=None):
    """Delete a reference.
    :param str name: Name of the reference to delete (example: heads/my_branch).
    :param str object_id: Id of the reference to delete.
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            repo=repository)
        client = get_git_client(organization)
        ref_update = GitRefUpdate(name=resolve_git_refs(name),
                                  new_object_id='0000000000000000000000000000000000000000',
                                  old_object_id=object_id)
        return client.update_refs(ref_updates=[ref_update],
                                  repository_id=repository,
                                  project=project)[0]
    except VstsServiceError as ex:
        raise CLIError(ex)


def update_ref(name, old_object_id, new_object_id, repository=None, organization=None,
               project=None, detect=None):
    """Update a reference.
    :param str name: Name of the reference to update (example: heads/my_branch).
    :param str old_object_id: Id of the old reference.
    :param str new_object_id: Id of the new reference.
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            repo=repository)
        client = get_git_client(organization)
        ref_update = GitRefUpdate(name=resolve_git_refs(name),
                                  new_object_id=new_object_id,
                                  old_object_id=old_object_id)
        return client.update_refs(ref_updates=[ref_update],
                                  repository_id=repository,
                                  project=project)[0]
    except VstsServiceError as ex:
        raise CLIError(ex)
