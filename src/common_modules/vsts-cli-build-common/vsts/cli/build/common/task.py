
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_task_agent_client,
                                      resolve_instance)
from vsts.cli.common.uuid import is_uuid


def task_list(team_instance=None, task_id=None, detect=None):
    """List tasks.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param str task_id: The UUID of the task.
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: [TaskDefinition]
    """
    try:
        if task_id is not None and not is_uuid(task_id):
            raise ValueError("The --id argument must be a UUID.")
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_task_agent_client(team_instance)
        definition_references = client.get_task_definitions(task_id=task_id)
        return definition_references
    except Exception as ex:
        handle_command_exception(ex)


def task_show(task_id, version, team_instance=None, detect=None):
    """Show task.
    :param str task_id: The UUID of the task.
    :param str version: The version of the task.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: TaskDefinition
    """
    try:
        if not is_uuid(task_id):
            raise ValueError("The --id argument must be a UUID.")
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_task_agent_client(team_instance)
        definition_references = client.get_task_definition(task_id=task_id,
                                                           version_string=version)
        return definition_references
    except Exception as ex:
        handle_command_exception(ex)

