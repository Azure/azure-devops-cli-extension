# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from azext_devops.dev.common.services import get_task_agent_client, resolve_instance_and_project

logger = get_logger(__name__)


def variable_group_create(name, description=None, group_type=None, variables=None, organization=None, project=None, detect=None):
    """Create a variable group
    :param name: Name of the variable group.
    :type name: str
    :param description: Description of the variable group.
    :type description: str
    :param type: Type of the variable group.
    :type type: str
    :param variables: Variables in format key=value.
    :type type: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    from azext_devops.devops_sdk.v5_0.task_agent.models import VariableGroupParameters, VariableValue
    import pdb
    pdb.set_trace()
    variables_dict = {}
    if variables:
        for variable in variables:
            key, value = variable.split('=', 1)
            variables_dict[key] = VariableValue(is_secret=False, value=value)

    var_group = VariableGroupParameters(name=name, description=description, type=group_type, variables=variables_dict)
    return client.add_variable_group(group=var_group, project=project)
