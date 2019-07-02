
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt_pass
from azext_devops.dev.common.services import get_build_client, resolve_instance_and_project
from azext_devops.dev.pipelines.build_definition import get_definition_id_from_name
from azext_devops.dev.common.prompting import verify_is_a_tty_or_raise_error
from azext_devops.devops_sdk.v5_0.build.models import Build, DefinitionReference

logger = get_logger(__name__)

def pipeline_variable_add(pipeline_id, pipeline_name, name, value=None, allow_override=None,  is_secret=None,
                                organization=None, project=None, detect=None):
    """(Preview) Add a variable to a pipeline
    :param pipeline_id: Id of the pipeline.
    :type pipeline_id: int
    :param pipeline_name: Name of the pipeline.
    :type pipeline_name: str
    :param allow_override: Indicates whether the value can be set at queue time.
    :type allow_override: bool
    :param is_secret: Indicates whether the variable's value is a secret.
    :type is_secret: bool
    :param name: Name of the variable.
    :type name: str
    :param value: Value of the variable. For secret variables, if --value parameter is not given,
    it will be picked from environment variable prefixed with AZURE_DEVOPS_EXT_PIPELINE_VAR_ or
    user will be prompted to enter it via standard input.
    e.g. A variable nameed `MySecret` can be input using environment variable
    AZURE_DEVOPS_EXT_PIPELINE_VAR_MySecret
    :type value: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if pipeline_id is None and pipeline_name is None:
        raise ValueError('Either the --pipeline-id argument or the --pipeline-name argument ' +
                         'must be supplied for this command.')
    client = get_build_client(organization)
    if id is None:
        id = get_definition_id_from_name(name, client, project)
    # get pipeline definition
    pipeline_definition = client.get_definition(definition_id=id, project=project)
    # Check if the variable already exists
    for key in pipeline_definition.variables.keys():
        if key.lower() == name.lower():
            raise CLIError(
                'Variable \'{}\' already exists. '
                'Use `az pipelines variable update` command to update the key/value.'.format(key))
    # Add the variable to the definition
    from azext_devops.devops_sdk.v5_0.build.models import BuildDefinitionVariable
    if not value:
        if is_secret:
            value = _get_value_from_env_or_stdin(var_name=name)
        else:
            raise CLIError('--value is required as parameter for non secret variable.')

    var_group.variables[name] = VariableValue(is_secret=is_secret, value=value)
    return client.update_variable_group(group=var_group, project=project, group_id=group_id).variables


def variable_group_variable_update(group_id, name, new_name=None, value=None, is_secret=None, prompt_value=False,
                                   organization=None, project=None, detect=None):
    """Update a variable in a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    :param name: Name of the variable.
    :type name: str
    :param name: New name of the variable.
    :type name: str
    :param value: New value of the variable.
    :type value: str
    :param is_secret: If the value of the variable is a secret.
    :type is_secret: str
    :param prompt_value: Set it to True to update the value of a secret variable using
    environment variable or prompt via standard input.
    :type prompt_value: str
    """
    if not new_name and not value and is_secret is None and not prompt_value:
        raise CLIError('Atleast one of --new-name, --value or --is-secret, --prompt-value '
                       'must be specified for update.')
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
    old_key = None
    old_value = None
    new_key = None
    # Check if the variable already exists
    old_key, old_value = _case_insensitive_get(input_dict=var_group.variables, search_key=name)
    new_key = new_name if new_name else old_key
    if old_key:
        is_secret = old_value.is_secret if is_secret is None else is_secret
        if not value and is_secret and prompt_value:
            value = _get_value_from_env_or_stdin(var_name=new_key)
        from azext_devops.devops_sdk.v5_0.task_agent.models import VariableValue
        if old_key != new_key:
            existing_key, _ = _case_insensitive_get(input_dict=var_group.variables, search_key=new_key)
            if existing_key:
                raise CLIError('Variable \'{}\' already exists.'.format(existing_key))
            var_group.variables.pop(old_key)
        var_group.variables[new_key] = VariableValue(
            is_secret=is_secret,
            value=old_value.value if value is None else value)
        print(old_value.value if value is None else value)
        return client.update_variable_group(group=var_group, project=project, group_id=group_id).variables
    raise CLIError(
        'Variable \'{}\' does not exist. '
        'Use `az pipelines variable-group variable update` command to update the key/value.'.format(name))


def variable_group_variable_list(group_id, organization=None, project=None, detect=None):
    """List the variables in a variable group
    :param group_id: Id of the variable group.
    :type group_id: int
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_task_agent_client(organization)
    var_group = client.get_variable_group(group_id=group_id, project=project)
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


def _get_value_from_env_or_stdin(var_name):
    env_var_name = AZ_DEVOPS_PIPELINES_VARIABLES_KEY_PREFIX + var_name
    logger.debug('Checking for variable %s in environment variable %s', var_name, env_var_name)
    import os
    value = os.getenv(env_var_name, None)
    logger.debug('Value of Variable %s in environment variable is found %s', var_name, value is not None)
    if not value:
        verify_is_a_tty_or_raise_error(
            'For non-interactive consoles set environment variable {}, or pipe the value of variable into the command.'
            .format(env_var_name))
        value = prompt_pass(msg=var_name + ': ')
    return value


def _case_insensitive_get(input_dict, search_key):
    search_key = search_key.lower()
    for key in input_dict.keys():
        if key.lower() == search_key:
            return key, input_dict[key]
    return None, None
