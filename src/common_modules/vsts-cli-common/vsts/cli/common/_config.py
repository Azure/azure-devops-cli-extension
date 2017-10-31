# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import stat
from six.moves import configparser

from knack.config import CLIConfig, get_config_parser
from vsts._file_cache import get_cache_dir

GLOBAL_CONFIG_DIR = get_cache_dir()
CONFIG_FILE_NAME = 'config'
GLOBAL_CONFIG_PATH = os.path.join(GLOBAL_CONFIG_DIR, CONFIG_FILE_NAME)
ENV_VAR_PREFIX = 'VSTS_'
DEFAULTS_SECTION = 'defaults'

_UNSET = object()
_ENV_VAR_FORMAT = ENV_VAR_PREFIX + '{section}_{option}'


class VstsConfig(CLIConfig):
    def __init__(self):
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
    config.set(section, option, value)
    set_global_config(config)
