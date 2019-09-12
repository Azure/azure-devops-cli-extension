# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.services import resolve_instance_and_project, get_build_client

logger = get_logger(__name__)


def pipeline_folder_create(path, description=None, organization=None,
                           project=None, detect=None):
    """ Create a folder.
    :param path: Full path of the folder.
    :type path: str
    :param description: Description of the folder.
    :type description: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    from azext_devops.devops_sdk.v5_0.build.models import Folder
    folder = Folder()
    folder.description = description
    folder.path = path
    new_folder = client.create_folder(folder=folder, path=path, project=project)
    return new_folder


def pipeline_folder_delete(path, organization=None, project=None, detect=None):
    """ Delete a folder.
    :param path: Full path of the folder.
    :type path: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    return client.delete_folder(path=path, project=project)


def pipeline_folder_list(path=None, query_order=None, organization=None, project=None, detect=None):
    """ List all folders.
    :param path: Full path of the folder.
    :type path: str
    :param query_order: Order in which folders are returned.
    :type query_order: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    if query_order:
        if query_order.lower() == 'asc':
            query_order = 'folderAscending'
        elif query_order.lower() == 'desc':
            query_order = 'folderDescending'
    return client.get_folders(path=path, query_order=query_order, project=project)


def pipeline_folder_update(path, new_path=None, new_description=None,
                           organization=None, project=None, detect=None):
    """ Update a folder name or description.
    :param path: Full path of the folder.
    :type path: str
    :param new_path: New full path of the folder.
    :type new_path: str
    :param new_description: New description of the folder.
    :type new_description: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    """
    if not new_path and not new_description:
        raise CLIError('Either --new-path or --new-description should be specified.')
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    folders = client.get_folders(path=path, project=project, query_order='folderAscending')
    folder_to_update = None
    # find matching folder if present
    for folder in folders:
        if folder.path.strip('\\') == path.strip('\\'):
            folder_to_update = folder
            break
    if not folder_to_update:
        raise CLIError('Cannot find folder with path {}. Update operation failed.'.format(path))
    if new_description:
        folder_to_update.description = new_description
    if new_path:
        folder_to_update.path = new_path
    return client.update_folder(path=path, folder=folder_to_update, project=project)
