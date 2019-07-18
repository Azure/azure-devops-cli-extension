
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt_pass
from azext_devops.dev.common.services import get_build_client, resolve_instance_and_project
from azext_devops.dev.pipelines.build_definition import get_definition_id_from_name
from azext_devops.dev.common.const import AZ_DEVOPS_PIPELINES_VARIABLES_KEY_PREFIX
from azext_devops.dev.common.prompting import verify_is_a_tty_or_raise_error

logger = get_logger(__name__)


def pipeline_variable_add(name, pipeline_id=None, pipeline_name=None, value=None, allow_override=None, secret=None,
                          organization=None, project=None, detect=None):
    """(Preview) Add a variable to a pipeline
    :param pipeline_id: Id of the pipeline.
    :type pipeline_id: int
    :param pipeline_name: Name of the pipeline. Ignored if --pipeline-id parameter is supplied.
    :type pipeline_name: str
    :param allow_override: Indicates whether the value can be set at queue time.
    :type allow_override: bool
    :param secret: Indicates whether the variable's value is a secret.
    :type secret: bool
    :param name: Name of the variable.
    :type name: str
    :param value: Value of the variable. For secret variables, if --value parameter is not given,
    it will be picked from environment variable prefixed with AZURE_DEVOPS_EXT_PIPELINE_VAR_ or
    user will be prompted to enter it via standard input.
    e.g. A variable named `MySecret` can be input using environment variable
    AZURE_DEVOPS_EXT_PIPELINE_VAR_MySecret
    :type value: str
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if pipeline_id is None and pipeline_name is None:
        raise ValueError('Either the --pipeline-id or --pipeline-name argument ' +
                         'must be supplied for this command.')
    pipeline_client = get_build_client(organization)
    if pipeline_id is None:
        pipeline_id = get_definition_id_from_name(pipeline_name, pipeline_client, project)
    # get pipeline definition
    pipeline_definition = pipeline_client.get_definition(definition_id=pipeline_id, project=project)
    # Check if the variable already exists
    if pipeline_definition.variables:
        for key in pipeline_definition.variables.keys():
            if key.lower() == name.lower():
                raise CLIError(
                    'Variable \'{}\' already exists. '
                    'Use `az pipelines variable update` command to update the key/value.'.format(key))
    else:
        pipeline_definition.variables = {}
    # Add the variable to the definition
    from azext_devops.devops_sdk.v5_0.build.models import BuildDefinitionVariable
    if not value:
        if secret:
            value = _get_value_from_env_or_stdin(var_name=name)
        else:
            raise CLIError('--value is required as parameter for non secret variable.')

    pipeline_definition.variables[name] = BuildDefinitionVariable(allow_override=allow_override, is_secret=secret,
                                                                  value=value)
    updated_variables = pipeline_client.update_definition(
        project=project, definition_id=pipeline_id, definition=pipeline_definition).variables
    var_name, var_value = _case_insensitive_get(input_dict=updated_variables, search_key=name)
    return { var_name:var_value }



def pipeline_variable_update(name, pipeline_id=None, pipeline_name=None, new_name=None, value=None,
                             allow_override=None, secret=None, prompt_value=None, organization=None,
                             project=None, detect=None):
    """(Preview) Update a variable in a pipeline
    :param pipeline_id: Id of the pipeline.
    :type pipeline_id: int
    :param pipeline_name: Name of the pipeline. Ignored if --pipeline-id parameter is supplied.
    :type pipeline_name: str
    :param allow_override: Indicates whether the value can be set at queue time.
    :type allow_override: bool
    :param secret: Indicates whether the variable's value is a secret.
    :type secret: bool
    :param name: Name of the variable.
    :type name: str
    :param new_name: New name of the variable.
    :type new_name: str
    :param value: New value of the variable. For secret variables, use --prompt-value parameter,
    to be prompted to enter it via standard input. For non-interactive consoles it can be picked from
    environment variable prefixed with AZURE_DEVOPS_EXT_PIPELINE_VAR_ e.g. A variable nameed `MySecret`
    can be input using environment variable AZURE_DEVOPS_EXT_PIPELINE_VAR_MySecret
    :type value: str
    :param secret: If the value of the variable is a secret.
    :type secret: str
    :param prompt_value: Set it to True to update the value of a secret variable using
    environment variable or prompt via standard input.
    :type prompt_value: str
    """
    if not new_name and not value and secret is None and allow_override is None and not prompt_value:
        raise CLIError('Atleast one of --new-name, --value, --is-secret, --prompt-value or --allow-override '
                       'must be specified for update.')
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if pipeline_id is None and pipeline_name is None:
        raise ValueError('Either the --pipeline-id or --pipeline-name argument ' +
                         'must be supplied for this command.')
    pipeline_client = get_build_client(organization)
    if pipeline_id is None:
        pipeline_id = get_definition_id_from_name(pipeline_name, pipeline_client, project)
    # get pipeline definition
    pipeline_definition = pipeline_client.get_definition(definition_id=pipeline_id, project=project)
    old_key = None
    old_value = None
    new_key = None
    # Check if the variable already exists
    old_key, old_value = _case_insensitive_get(input_dict=pipeline_definition.variables, search_key=name)
    new_key = new_name if new_name else old_key
    if old_key:
        secret = old_value.is_secret if secret is None else secret
        allow_override = old_value.allow_override if allow_override is None else allow_override
        if not value and secret and prompt_value:
            value = _get_value_from_env_or_stdin(var_name=new_key)
        from azext_devops.devops_sdk.v5_0.build.models import BuildDefinitionVariable
        if old_key != new_key:
            existing_key, _ = _case_insensitive_get(input_dict=pipeline_definition.variables, search_key=new_key)
            if existing_key:
                raise CLIError('Variable \'{}\' already exists.'.format(existing_key))
            pipeline_definition.variables.pop(old_key)
        pipeline_definition.variables[new_key] = BuildDefinitionVariable(
            is_secret=secret,
            value=old_value.value if value is None else value,
            allow_override=allow_override)
        updated_variables = pipeline_client.update_definition(
            project=project, definition_id=pipeline_id, definition=pipeline_definition).variables
        var_name, var_value = _case_insensitive_get(input_dict=updated_variables, search_key=new_key)
        return { var_name:var_value }
    raise CLIError('Variable \'{}\' does not exist.'.format(name))


def pipeline_variable_list(pipeline_id=None, pipeline_name=None, organization=None, project=None, detect=None):
    """(Preview) List the variables in a pipeline
    :param pipeline_id: Id of the pipeline.
    :type pipeline_id: int
    :param pipeline_name: Name of the pipeline. Ignored if --pipeline-id parameter is supplied.
    :type pipeline_name: str
     """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if pipeline_id is None and pipeline_name is None:
        raise ValueError('Either the --pipeline-id or --pipeline-name argument ' +
                         'must be supplied for this command.')
    pipeline_client = get_build_client(organization)
    if pipeline_id is None:
        pipeline_id = get_definition_id_from_name(pipeline_name, pipeline_client, project)
    # get pipeline definition
    pipeline_definition = pipeline_client.get_definition(definition_id=pipeline_id, project=project)
    return pipeline_definition.variables


def pipeline_variable_delete(name, pipeline_id=None, pipeline_name=None, organization=None, project=None, detect=None):
    """(Preview) Delete a variable from pipeline
    :param pipeline_id: Id of the pipeline.
    :type pipeline_id: int
    :param pipeline_name: Name of the pipeline.
    :type pipeline_name: str
    :param name: Name of the variable to delete.
    :type name: str
     """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if pipeline_id is None and pipeline_name is None:
        raise ValueError('Either the --pipeline-id or --pipeline-name argument ' +
                         'must be supplied for this command.')
    pipeline_client = get_build_client(organization)
    if pipeline_id is None:
        pipeline_id = get_definition_id_from_name(name, pipeline_client, project)
    # get pipeline definition
    pipeline_definition = pipeline_client.get_definition(definition_id=pipeline_id, project=project)

    key_to_delete = None
    # Check if the variable already exists
    key = None
    if pipeline_definition.variables:
        for key in pipeline_definition.variables.keys():
            if key.lower() == name.lower():
                key_to_delete = key
                break
    if not key_to_delete:
        raise CLIError('Variable \'{}\' does not exist. '.format(name))
    _ = pipeline_definition.variables.pop(key)
    _ = pipeline_client.update_definition(project=project, definition_id=pipeline_id, definition=pipeline_definition)
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
    if input_dict:
        for key in input_dict.keys():
            if key.lower() == search_key:
                return key, input_dict[key]
    return None, None
