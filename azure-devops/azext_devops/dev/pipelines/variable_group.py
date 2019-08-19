# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.services import get_task_agent_client, resolve_instance_and_project
from azext_devops.dev.pipelines.pipeline_variables import _case_insensitive_get, _get_value_from_env_or_stdin

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class VariableGroupAuthorized():
    _attribute_map = {
        'variable_group_parameters': {'key': 'variable_group_parameters', 'type': 'VariableGroupParameters'},
        'authorized': {'key': 'authorized', 'type': 'bool'}
    }

    def __init__(self, variable_group_parameters, authorized):
        self.authorized = authorized if authorized is not None else False
        self.id = variable_group_parameters.id
        self.description = variable_group_parameters.description
        self.name = variable_group_parameters.name
        self.provider_data = variable_group_parameters.provider_data
        self.type = variable_group_parameters.type
        self.variables = variable_group_parameters.variables


def variable_group_create(name, variables, description=None, authorize=None,
                          organization=None, project=None, detect=None):
    """Create a variable group
    :param name: Name of the variable group.
    :type name: str
    :param description: Description of the variable group.
    :type description: str
    :param authorize: Whether the variable group should be accessible by all pipelines.
    :type authorize: boolean
    :param variables: Variables in format key=value space separated pairs. Secret variables should be managed using
    `az pipelines variable-group variable` commands.
    :type type: [str]
    """
    group_type = 'Vsts'
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
    var_group = client.add_variable_group(group=var_group, project=project)
    if authorize is not None:
        from .pipeline_utils import set_authorize_resource
        set_authorize_resource(
            authorized=authorize, res_id=var_group.id, name=var_group.name, res_type='variablegroup',
            organization=organization, project=project)
    return VariableGroupAuthorized(var_group, authorize)


def variable_group_show(group_id, organization=None, project=None, detect=None):
    """Show variable group details.
    :param group_id: ID of the variable group.
    :type group_id: int
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    from .pipeline_utils import get_authorize_resource
    authorized = get_authorize_resource(
        res_id=var_group.id, res_type='variablegroup', organization=organization, project=project)
    return VariableGroupAuthorized(var_group, authorized)


def variable_group_list(group_name=None, action_filter=None, top=None, continuation_token=None, query_order='Desc',
                        organization=None, project=None, detect=None):
    """List variable groups
    :param group_name: Name of the variable group. Wildcards are accepted. e.g. var_group*
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
    _QUERY_ORDER_ASCENDING = 'idAscending'
    _QUERY_ORDER_DESCENDING = 'idDescending'
    query_order = _QUERY_ORDER_DESCENDING if query_order.lower() == 'desc' else _QUERY_ORDER_ASCENDING
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
    delete_response = client.delete_variable_group(project=project, group_id=group_id)
    print("Deleted variable group successfully.")
    return delete_response


def variable_group_update(group_id, name=None, description=None, authorize=None,
                          organization=None, project=None, detect=None):
    """Update a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: New name of the variable group.
    :type name: str
    :param authorize: Whether the variable group should be accessible by all pipelines.
    :type authorize: boolean
    :param description: New description of the variable group.
    :type description: str
    """
    if not name and not description and authorize is None:
        raise CLIError("Either --name, --description or --authorize must be specified for update.")
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    update = False
    if name:
        var_group.name = name
        update = True
    if description:
        var_group.description = description
        update = True
    if update:
        var_group = client.update_variable_group(group=var_group, project=project, group_id=group_id)
    if authorize is not None:
        from .pipeline_utils import set_authorize_resource
        set_authorize_resource(
            authorized=authorize, res_id=var_group.id, name=var_group.name, res_type='variablegroup',
            organization=organization, project=project)
    else:
        from .pipeline_utils import get_authorize_resource
        authorize = get_authorize_resource(res_id=var_group.id, res_type='variablegroup',
                                           organization=organization, project=project)
    return VariableGroupAuthorized(var_group, authorize)


def variable_group_variable_add(group_id, name, value=None, secret=None,
                                organization=None, project=None, detect=None):
    """Add a variable to a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: Name of the variable.
    :type name: str
    :param value: Value of the variable. For secret variables, if --value parameter is not given,
    it will be picked from environment variable prefixed with AZURE_DEVOPS_EXT_PIPELINE_VAR_ or
    user will be prompted to enter it via standard input.
    e.g. PersonalAccessToken can be input using environment variable AZURE_DEVOPS_EXT_PIPELINE_VAR_PersonalAccessToken
    :type value: str
    :param secret: If the value of the variable is a secret.
    :type secret: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    # Check if the variable already exists
    for key in var_group.variables.keys():
        if key.lower() == name.lower():
            raise CLIError(
                'Variable \'{}\' already exists. '
                'Use `az pipelines variable-group variable update` command to update the key/value.'.format(key))
    # Add the variable to the variable group.
    from azext_devops.devops_sdk.v5_0.task_agent.models import VariableValue
    if not value:
        if secret:
            value = _get_value_from_env_or_stdin(var_name=name)
        else:
            raise CLIError('--value is required as parameter for non secret variable.')

    var_group.variables[name] = VariableValue(is_secret=secret, value=value)
    updated_variables = client.update_variable_group(group=var_group, project=project, group_id=group_id).variables
    var_name, var_value = _case_insensitive_get(input_dict=updated_variables, search_key=name)
    return {var_name: var_value}


def variable_group_variable_update(group_id, name, new_name=None, value=None, secret=None, prompt_value=False,
                                   organization=None, project=None, detect=None):
    """Update a variable in a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: Name of the variable.
    :type name: str
    :param new_name: New name of the variable.
    :type new_name: str
    :param value: New value of the variable. For secret variables, if --value parameter is not given,
    it will be picked from environment variable prefixed with AZURE_DEVOPS_EXT_PIPELINE_VAR_ or
    user will be prompted to enter it via standard input.
    e.g. PersonalAccessToken can be input using environment variable AZURE_DEVOPS_EXT_PIPELINE_VAR_PersonalAccessToken
    :type value: str
    :param secret: If the value of the variable is a secret.
    :type secret: str
    :param prompt_value: Set it to True to update the value of a secret variable using
    environment variable or prompt via standard input.
    :type prompt_value: str
    """
    if not new_name and not value and secret is None and not prompt_value:
        raise CLIError('Atleast one of --new-name, --value or --is-secret, --prompt-value '
                       'must be specified for update.')
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    old_key = None
    old_value = None
    new_key = None
    # Check if the variable already exists
    old_key, old_value = _case_insensitive_get(input_dict=var_group.variables, search_key=name)
    new_key = new_name if new_name else old_key
    if old_key:
        secret = old_value.is_secret if secret is None else secret
        if not value and secret and prompt_value:
            value = _get_value_from_env_or_stdin(var_name=new_key)
        from azext_devops.devops_sdk.v5_0.task_agent.models import VariableValue
        if old_key != new_key:
            existing_key, _ = _case_insensitive_get(input_dict=var_group.variables, search_key=new_key)
            if existing_key:
                raise CLIError('Variable \'{}\' already exists.'.format(existing_key))
            var_group.variables.pop(old_key)
        var_group.variables[new_key] = VariableValue(
            is_secret=secret,
            value=old_value.value if value is None else value)
        updated_variables = client.update_variable_group(
            group=var_group, project=project, group_id=group_id).variables
        var_name, var_value = _case_insensitive_get(input_dict=updated_variables, search_key=new_key)
        return {var_name: var_value}
    raise CLIError('Variable \'{}\' does not exist. '.format(name))


def variable_group_variable_list(group_id, organization=None, project=None, detect=None):
    """List the variables in a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    return var_group.variables


def variable_group_variable_delete(group_id, name, organization=None, project=None, detect=None):
    """Delete a variable from variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: Name of the variable.
    :type name: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    if not var_group:
        raise CLIError('Variable group with Id {} could not be found.'.format(group_id))
    key_to_delete = None
    # Check if the variable already exists
    key = None
    for key in var_group.variables.keys():
        if key.lower() == name.lower():
            key_to_delete = key
            break
    if not key_to_delete:
        raise CLIError('Variable \'{}\' does not exist. '.format(name))
    _ = var_group.variables.pop(key)
    _ = client.update_variable_group(group=var_group, project=project, group_id=group_id).variables
    print('Deleted variable \'{}\' successfully.'.format(key_to_delete))
