# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from azext_devops.dev.common.services import get_task_agent_client, resolve_instance_and_project

logger = get_logger(__name__)


def variable_group_create(name, description=None, group_type=None, variables=None,
                          organization=None, project=None, detect=None):
    """Create a variable group
    :param name: Name of the variable group.
    :type name: str
    :param description: Description of the variable group.
    :type description: str
    :param group_type: Type of the variable group.
    :type group_type: str
    :param variables: Variables in format key=value. Secret variables should be managed using
    `az pipelines variable` commands.
    :type type: [str]
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    from azext_devops.devops_sdk.v5_0.task_agent.models import VariableGroupParameters, VariableValue
    variables_dict = {}
    if variables:
        for variable in variables:
            key, value = variable.split('=', 1)
            variables_dict[key] = VariableValue(is_secret=False, value=value)

    var_group = VariableGroupParameters(name=name, description=description, type=group_type, variables=variables_dict)
    return client.add_variable_group(group=var_group, project=project)


def variable_group_show(group_id, organization=None, project=None, detect=None):
    """Show variable group details
    :param group: ID of the variable group.
    :type group: int
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    return client.get_variable_group(group_id=group_id, project=project)


def variable_group_list(group_name=None, action_filter=None, top=None, continuation_token=None, query_order='Desc',
                        organization=None, project=None, detect=None):
    """List variable groups
    :param group_name: Name of the variable group.
    :type group_name: str
    :param action_filter: Action filter for the variable group.
    It specifies the action which can be performed on the variable groups.
    :type action_filter: str
    :param top: Number of variable groups to get.
    :type top: str
    :param continuation_token: Gets the variable groups after the continuation token provided.
    :type continuation_token: str
    :param query_order: Gets the results in the defined order.
    :type query_order: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    return client.get_variable_groups(project=project, group_name=group_name, action_filter=action_filter, top=top,
                                      continuation_token=continuation_token, query_order=query_order)


def variable_group_delete(group_id, organization=None, project=None, detect=None):
    """Delete a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    return client.delete_variable_group(project=project, group_id=group_id)


def variable_group_update(group_id, name=None, description=None, variables=None,
                          organization=None, project=None, detect=None):
    """Update a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: Name of the variable group.
    :type name: str
    :param description: Description of the variable group.
    :type description: str
    :param group_type: Type of the variable group.
    :type group_type: str
    :param variables: Variables in format key=value. Variables will be appended/updated to the existing variables.
    Secret variables should be managed using `az pipelines variable` commands.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    from azext_devops.devops_sdk.v5_0.task_agent.models import VariableGroupParameters, VariableValue
    variables_dict = {}
    if variables:
        for variable in variables:
            key, value = variable.split('=', 1)
            variables_dict[key] = VariableValue(is_secret=False, value=value)
    var_group = VariableGroupParameters(name=name, description=description, variables=variables_dict)
    return client.update_variable_group(group=var_group, project=project, group_id=group_id)


def variable_group_variable_add(group=None, organization=None, project=None, detect=None):
    """Add a variable to a variable group
    """
    pass


def variable_group_variable_list(group=None, organization=None, project=None, detect=None):
    """List the variables in a variable group
    """
    pass


def variable_group_variable_delete(group=None, organization=None, project=None, detect=None):
    """Delete a variable from variable group
    """
    pass
    