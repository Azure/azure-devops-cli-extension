# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from __future__ import print_function

import os

from .config import GLOBAL_CONFIG_PATH, CLI_ENV_VARIABLE_PREFIX, set_global_config
from six.moves import configparser
from knack.config import get_config_parser
from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt_y_n, prompt_choice_list, NoTTYException

logger = get_logger(__name__)

answers = {}


def print_current_configuration(file_config=None):
    if file_config is None:
        file_config = get_config_parser()
        file_config.read([GLOBAL_CONFIG_PATH])
    for section in file_config.sections():
        print()
        print('[{}]'.format(section))
        for option in file_config.options(section):
            print('{} = {}'.format(option, file_config.get(section, option)))
    env_vars = [ev for ev in os.environ if ev.startswith(CLI_ENV_VARIABLE_PREFIX)]
    if env_vars:
        print(MSG_HEADING_ENV_VARS)
        print('\n'.join(['{} = {}'.format(ev, os.environ[ev]) for ev in env_vars]))


def _handle_global_configuration():
    # print location of global configuration
    print(MSG_GLOBAL_SETTINGS_LOCATION.format(GLOBAL_CONFIG_PATH))
    # set up the config parsers
    file_config = get_config_parser()
    config_exists = file_config.read([GLOBAL_CONFIG_PATH])
    global_config = get_config_parser()
    global_config.read(GLOBAL_CONFIG_PATH)
    should_modify_global_config = False
    if config_exists:
        # print current config and prompt to allow global config modification
        print(MSG_HEADING_CURRENT_CONFIG_INFO)
        print_current_configuration(file_config)
        should_modify_global_config = prompt_y_n(MSG_PROMPT_MANAGE_GLOBAL, default='n')
        answers['modify_global_prompt'] = should_modify_global_config
    if not config_exists or should_modify_global_config:
        # no config exists yet so configure global config or user wants to modify global config
        output_index = prompt_choice_list(MSG_PROMPT_GLOBAL_OUTPUT, OUTPUT_LIST,
                                          default=get_default_from_config(global_config,
                                                                          'core', 'output',
                                                                          OUTPUT_LIST))
        answers['output_type_prompt'] = output_index
        answers['output_type_options'] = str(OUTPUT_LIST)
        try:
            from azext_dev.dev.repos.git_alias import setup_git_aliases, are_git_aliases_setup
            if not are_git_aliases_setup():
                setup_aliases = prompt_y_n(MSG_PROMPT_GIT_ALIAS, default='y')
                if setup_aliases:
                    answers['git_aliases'] = True
                    setup_git_aliases()
                else:
                    answers['git_aliases'] = False
            else:
                answers['git_aliases'] = True
        except (ModuleNotFoundError, CLIError):
            logger.debug('Skipping git alias configuration, because module was not found.')
        enable_file_logging = prompt_y_n(MSG_PROMPT_FILE_LOGGING, default='n')
        allow_telemetry = prompt_y_n(MSG_PROMPT_TELEMETRY, default='y')
        answers['telemetry_prompt'] = allow_telemetry
        # save the global config
        try:
            global_config.add_section('core')
        except configparser.DuplicateSectionError:
            pass
        try:
            global_config.add_section('logging')
        except configparser.DuplicateSectionError:
            pass
        global_config.set('core', 'output', OUTPUT_LIST[output_index]['name'])
        global_config.set('core', 'collect_telemetry', 'yes' if allow_telemetry else 'no')
        global_config.set('logging', 'enable_log_file', 'yes' if enable_file_logging else 'no')
        set_global_config(global_config)


def interactive_configure():
    try:
        print(MSG_INTRO)
        _handle_global_configuration()
        if 'git_aliases' in answers and answers['git_aliases']:
            message = MSG_CLOSING.format(MSG_CLOSING_GIT_COMMAND)
        else:
            message = MSG_CLOSING.format('')
        print(message)
    except NoTTYException:
        raise CLIError('This command is interactive and no tty available.')
    except (EOFError, KeyboardInterrupt):
        print()


def get_default_from_config(config, section, option, choice_list, fallback=1):
    try:
        config_val = config.get(section, option)
        return [i for i, x in enumerate(choice_list)
                if 'name' in x and x['name'] == config_val][0] + 1
    except (IndexError, configparser.NoSectionError, configparser.NoOptionError):
        return fallback


OUTPUT_LIST = [
    {'name': 'json', 'desc': 'JSON formatted output that most closely matches API responses'},
    {'name': 'jsonc',
     'desc': 'Colored JSON formatted output that most closely matches API responses'},
    {'name': 'table', 'desc': 'Human-readable output format'},
    {'name': 'tsv', 'desc': 'Tab and Newline delimited, great for GREP, AWK, etc.'}
]

MSG_INTRO = '\nWelcome to the Azure Dev CLI! This command will guide you through setting some default values.\n'
MSG_CLOSING = '\nYou\'re all set! Here are some commands to try:\n' \
              ' $ az dev login\n' \
              ' $ az dev code pr list\n{}' \
              ' $ az dev feedback\n'

MSG_CLOSING_GIT_COMMAND = ' $ git pr list\n'

MSG_GLOBAL_SETTINGS_LOCATION = 'Your settings can be found at {}'

MSG_HEADING_CURRENT_CONFIG_INFO = 'Your current configuration is as follows:'
MSG_HEADING_ENV_VARS = '\nEnvironment variables:'

MSG_PROMPT_MANAGE_GLOBAL = '\nDo you wish to change your settings?'
MSG_PROMPT_GLOBAL_OUTPUT = '\nWhat default output format would you like?'
MSG_PROMPT_TELEMETRY = '\nMicrosoft would like to collect anonymous VSTS CLI usage data to ' \
                       'improve our CLI.  Participation is voluntary and when you choose to ' \
                       'participate, your device automatically sends information to Microsoft ' \
                       'about how you use the VSTS CLI.  The data is anonymous and does not ' \
                       'include commandline argument values.  To update your choice, run "vsts ' \
                       'configure" again.\nSelect y to enable data collection.'
MSG_PROMPT_GIT_ALIAS = '\nConfigure aliases for Git (to enable commands like "git pr list")?'
MSG_PROMPT_CLEAR_GIT_ALIAS = '\nGit aliases are configured, would you like to clear them?'
MSG_PROMPT_FILE_LOGGING = '\nWould you like to enable logging to file?'
