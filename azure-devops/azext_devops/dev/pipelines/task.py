
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.vstsCompressed.exceptions import VstsServiceError
from knack.util import CLIError
from azext_devops.dev.common.services import (get_task_agent_client,
                                              resolve_instance)
from azext_devops.dev.common.uuid import is_uuid


def task_list(organization=None, task_id=None, detect=None):
    """List tasks.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param str task_id: The UUID of the task.
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: [TaskDefinition]
    """
    try:
        if task_id is not None and not is_uuid(task_id):
            raise ValueError("The --id argument must be a UUID.")
        organization = resolve_instance(detect=detect, organization=organization)
        client = get_task_agent_client(organization)
        definition_references = client.get_task_definitions(task_id=task_id)
        return definition_references
    except VstsServiceError as ex:
        raise CLIError(ex)


def task_show(id, version, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show task.
    :param str id: The UUID of the task.
    :param str version: The version of the task.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: TaskDefinition
    """
    try:
        if not is_uuid(id):
            raise ValueError("The --id argument must be a UUID.")
        organization = resolve_instance(detect=detect, organization=organization)
        client = get_task_agent_client(organization)
        definition_references = client.get_task_definition(task_id=id,
                                                           version_string=version)
        return definition_references
    except VstsServiceError as ex:
        raise CLIError(ex)
