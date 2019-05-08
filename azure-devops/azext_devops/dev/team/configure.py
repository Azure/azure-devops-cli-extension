# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import os

from knack.config import get_config_parser
from knack.log import get_logger
from knack.util import CLIError

from azext_devops.dev.common.config import (set_global_config_value, AZ_DEVOPS_GLOBAL_CONFIG_PATH)
from azext_devops.dev.common.const import (CLI_ENV_VARIABLE_PREFIX, DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT,
                                           DEVOPS_TEAM_PROJECT_DEFAULT, DEVOPS_PREVIEW_DEFAULT)

logger = get_logger(__name__)


CONFIG_VALID_DEFAULT_KEYS_LIST = [DEVOPS_ORGANIZATION_DEFAULT, DEVOPS_TEAM_PROJECT_DEFAULT]


def configure(defaults=None, use_git_aliases=None, list_config=False, enable_preview_commands=None):
    """Configure the Azure DevOps CLI or view your configuration.
    :param defaults: Space separated 'name=value' pairs for common arguments defaults,
        e.g. '--defaults project=my-project-name organization=https://dev.azure.com/organizationName
        arg=value' Use '' to clear the defaults, e.g. --defaults project=''.
    :type defaults: str
    :param use_git_aliases: Set to 'yes' to configure Git aliases global git config file
        (to enable commands like "git pr list").
        Set to 'no' to remove any aliases set by the tool.
    :type use_git_aliases: str
    :param list_config: Lists the contents of the config file.
    :type list_config: bool
    :param enable_preview_commands: Set to 'yes' to use preview commands
        Set to 'no' to not use any preview commands
    :type enable_preview_commands: str
    """
    if defaults is None and use_git_aliases is None and list_config is False and enable_preview_commands is None:
        raise CLIError('usage error: atleast one of the options must be specified.'
                       'For list of supported options see help using -h flag.')
    if defaults:
        for default in defaults:
            parts = default.split('=', 1)
            if len(parts) == 1:
                raise CLIError('usage error: --defaults STRING=STRING STRING=STRING ...')
            if parts[0] not in CONFIG_VALID_DEFAULT_KEYS_LIST:
                raise CLIError('usage error: invalid default value setup. Supported values are {}.'
                               .format(CONFIG_VALID_DEFAULT_KEYS_LIST))
            set_global_config_value(DEFAULTS_SECTION, parts[0], parts[1])
    if enable_preview_commands is not None:
        set_global_config_value(DEFAULTS_SECTION, DEVOPS_PREVIEW_DEFAULT, enable_preview_commands)
    if use_git_aliases is not None:
        from azext_devops.dev.repos.git_alias import setup_git_aliases, clear_git_aliases
        if use_git_aliases == 'yes':
            setup_git_aliases()
        elif use_git_aliases == 'no':
            clear_git_aliases()
    if list_config:
        print_current_configuration()


def print_current_configuration(file_config=None):
    from azext_devops.dev.repos.git_alias import are_git_aliases_setup
    if file_config is None:
        file_config = get_config_parser()
        file_config.read([AZ_DEVOPS_GLOBAL_CONFIG_PATH])
    for section in file_config.sections():
        print()
        print('[{}]'.format(section))
        for option in file_config.options(section):
            print('{} = {}'.format(option, file_config.get(section, option)))
    # Print if git alias is setup or not
    is_git_alias_setup = MSG_NO
    if are_git_aliases_setup():
        is_git_alias_setup = MSG_YES
    print('{} = {}'.format(MSG_GIT_ALIAS_SETUP, is_git_alias_setup))
    env_vars = [ev for ev in os.environ if ev.startswith(CLI_ENV_VARIABLE_PREFIX)]
    if env_vars:
        print(MSG_HEADING_ENV_VARS)
        print('\n'.join(['{}'.format(ev) for ev in env_vars]))


MSG_INTRO = '\nWelcome to the Azure DevOps CLI! This command will guide you through setting some default values.\n'
MSG_CLOSING = '\nYou\'re all set! Here are some commands to try:\n' \
              ' $ az devops login\n' \
              ' $ az repos pr list\n{}' \
              ' $ az devops feedback\n'

MSG_CLOSING_GIT_COMMAND = ' $ git pr list\n'
MSG_GIT_ALIAS_SETUP = '\nUse git alias'

MSG_GLOBAL_SETTINGS_LOCATION = 'Your settings can be found at {}'

MSG_HEADING_CURRENT_CONFIG_INFO = 'Your current configuration is as follows:'
MSG_HEADING_ENV_VARS = '\nEnvironment variables:'

MSG_PROMPT_MANAGE_GLOBAL = '\nDo you wish to change your settings?'
MSG_PROMPT_GIT_ALIAS = '\nConfigure aliases for Git (to enable commands like "git pr list")?'
MSG_PROMPT_CLEAR_GIT_ALIAS = '\nGit aliases are configured, would you like to clear them?'

MSG_YES = 'Yes'
MSG_NO = 'No'
