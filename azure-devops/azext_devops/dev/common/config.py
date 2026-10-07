# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from knack.config import CLIConfig, get_config_parser
from .const import (AZ_DEVOPS_CONFIG_DIR_ENVKEY,
                    AZ_DEVOPS_DEFAULT_CONFIG_DIR,
                    CLI_ENV_VARIABLE_PREFIX,
                    CONFIG_FILE_NAME)


_UNSET = object()


def _ensure_private_config_dir(config_dir):
    os.makedirs(config_dir, mode=0o700, exist_ok=True)
    if os.name != 'nt':
        os.chmod(config_dir, 0o700)


def _get_config_dir():
    configured_dir = os.getenv(AZ_DEVOPS_CONFIG_DIR_ENVKEY, None)
    azure_devops_config_dir = configured_dir or AZ_DEVOPS_DEFAULT_CONFIG_DIR
    _ensure_private_config_dir(azure_devops_config_dir)
    return azure_devops_config_dir


AZ_DEVOPS_GLOBAL_CONFIG_DIR = _get_config_dir()
AZ_DEVOPS_GLOBAL_CONFIG_PATH = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, CONFIG_FILE_NAME)


class AzDevopsConfig(CLIConfig):
    def __init__(self, config_dir=AZ_DEVOPS_GLOBAL_CONFIG_DIR, config_env_var_prefix=CLI_ENV_VARIABLE_PREFIX):
        super(AzDevopsConfig, self).__init__(config_dir=config_dir, config_env_var_prefix=config_env_var_prefix)
        self.config_parser = get_config_parser()


azdevops_config = AzDevopsConfig()
azdevops_config.config_parser.read(AZ_DEVOPS_GLOBAL_CONFIG_PATH)


def set_global_config_value(section, option, value):
    azdevops_config.set_value(section, option, _normalize_config_value(value))
    azdevops_config.config_parser.read(AZ_DEVOPS_GLOBAL_CONFIG_PATH)


def _normalize_config_value(value):
    if value:
        value = '' if value in ["''", '""'] else value
    return value
