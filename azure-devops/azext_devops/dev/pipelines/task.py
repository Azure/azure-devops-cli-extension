
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_task_agent_client,
                                              resolve_instance)
from azext_devops.dev.common.uuid import is_uuid


def task_list(organization=None, task_id=None, detect=None):
    """List tasks.
    :param str task_id: The UUID of the task.
    :type detect: str
    :rtype: [TaskDefinition]
    """
    if task_id is not None and not is_uuid(task_id):
        raise ValueError("The --id argument must be a UUID.")
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_task_agent_client(organization)
    definition_references = client.get_task_definitions(task_id=task_id)
    return definition_references


def task_show(id, version, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show task.
    :param str id: The UUID of the task.
    :param str version: The version of the task.
    :rtype: TaskDefinition
    """
    if not is_uuid(id):
        raise ValueError("The --id argument must be a UUID.")
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_task_agent_client(organization)
    definition_references = client.get_task_definition(task_id=id,
                                                       version_string=version)
    return definition_references
