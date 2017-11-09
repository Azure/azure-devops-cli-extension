# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import stat
from six.moves import configparser

from knack.config import CLIConfig, get_config_parser


CONFIG_FILE_NAME = 'config'
ENV_VAR_PREFIX = 'VSTS_CLI_'
CORE_SECTION = 'core'
DEFAULTS_SECTION = 'defaults'
LOGGING_SECTION = 'logging'

_UNSET = object()
_ENV_VAR_FORMAT = ENV_VAR_PREFIX + '{section}_{option}'


def _get_config_dir():
    vsts_config_dir = os.getenv('VSTS_CONFIG_DIR', None) or os.path.expanduser(os.path.join('~', '.vsts', 'cli'))
    if not os.path.exists(vsts_config_dir):
        os.makedirs(vsts_config_dir)
    return vsts_config_dir


GLOBAL_CONFIG_DIR = _get_config_dir()
GLOBAL_CONFIG_PATH = os.path.join(GLOBAL_CONFIG_DIR, CONFIG_FILE_NAME)


class VstsConfig(CLIConfig):
    def __init__(self, config_dir=GLOBAL_CONFIG_DIR, config_env_var_prefix=ENV_VAR_PREFIX):
        CLIConfig.__init__(self, config_dir=config_dir, config_env_var_prefix=config_env_var_prefix)
        self.config_parser = get_config_parser()


vsts_config = VstsConfig()
vsts_config.config_parser.read(GLOBAL_CONFIG_PATH)


def set_global_config(config):
    if not os.path.isdir(GLOBAL_CONFIG_DIR):
        os.makedirs(GLOBAL_CONFIG_DIR)
    with open(GLOBAL_CONFIG_PATH, 'w') as configfile:
        config.write(configfile)
    os.chmod(GLOBAL_CONFIG_PATH, stat.S_IRUSR | stat.S_IWUSR)
    # reload config
    vsts_config.config_parser.read(GLOBAL_CONFIG_PATH)


def set_global_config_value(section, option, value):
    config = get_config_parser()
    config.read(GLOBAL_CONFIG_PATH)
    try:
        config.add_section(section)
    except configparser.DuplicateSectionError:
        pass
    config.set(section, option, _normalize_config_value(value))
    set_global_config(config)


def _normalize_config_value(value):
    if value:
        value = '' if value in ["''", '""'] else value
    return value
