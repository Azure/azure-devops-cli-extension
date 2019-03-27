# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.git.models import GitRefUpdate
from azext_devops.devops_sdk.exceptions import AzureDevOpsServiceError
from azext_devops.dev.common.git import resolve_git_refs
from azext_devops.dev.common.services import (get_git_client,
                                              resolve_instance_project_and_repo)

logger = get_logger(__name__)


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
    except AzureDevOpsServiceError as ex:
        raise CLIError(ex)


def create_ref(name, object_id, repository=None, organization=None, project=None, detect=None):
    """Create a reference.
    :param str name: Name of the reference to create (example: heads/my_branch or tags/my_tag).
    :param str object_id: Id of the object to create the reference from.
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
        # by default, the create method does not support setting the is_locked value
        # to True.
        ref_update = GitRefUpdate(is_locked=False,
                                  name=resolve_git_refs(name),
                                  new_object_id=object_id,
                                  old_object_id='0000000000000000000000000000000000000000')
        return client.update_refs(ref_updates=[ref_update],
                                  repository_id=repository,
                                  project=project)[0]
    except AzureDevOpsServiceError as ex:
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
    except AzureDevOpsServiceError as ex:
        raise CLIError(ex)


def lock_ref(name, repository=None, organization=None, project=None, detect=None):
    """Lock a reference.
    :param str name: Name of the reference to update (example: heads/my_branch).
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    return _update_ref(name, True, repository, organization, project, detect)


def unlock_ref(name, repository=None, organization=None, project=None, detect=None):
    """Unlock a reference.
    :param str name: Name of the reference to update (example: heads/my_branch).
    :param str repository: Name or ID of the repository.
    :param str organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :param str project: Name or ID of the project.
    :param str detect: Automatically detect organization and project. Default is "on".
    """
    return _update_ref(name, False, repository, organization, project, detect)


def _update_ref(name, locked, repository, organization, project, detect):
    try:
        organization, project, repository = resolve_instance_project_and_repo(
            detect=detect,
            organization=organization,
            project=project,
            repo=repository)
        client = get_git_client(organization)
        ref_update = GitRefUpdate(is_locked=locked)
        return client.update_ref(new_ref_info=ref_update,
                                 repository_id=repository,
                                 filter=name,
                                 project=project)
    except AzureDevOpsServiceError as ex:
        raise CLIError(ex)
