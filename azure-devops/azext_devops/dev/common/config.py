# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from knack.config import CLIConfig, get_config_parser
from knack.util import ensure_dir
from .const import (AZ_DEVOPS_CONFIG_DIR_ENVKEY,
                    AZ_DEVOPS_DEFAULT_CONFIG_DIR,
                    CLI_ENV_VARIABLE_PREFIX,
                    CONFIG_FILE_NAME,
                    DEFAULTS_SECTION,
                    DEVOPS_PREVIEW_DEFAULT)


_UNSET = object()


def _get_config_dir():
    azure_devops_config_dir = os.getenv(AZ_DEVOPS_CONFIG_DIR_ENVKEY, None) or AZ_DEVOPS_DEFAULT_CONFIG_DIR
    # Create a directory if it doesn't exist
    ensure_dir(azure_devops_config_dir)
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


def get_preview_value():
    if azdevops_config.has_option(DEFAULTS_SECTION, DEVOPS_PREVIEW_DEFAULT):
        preview = azdevops_config.get(DEFAULTS_SECTION, DEVOPS_PREVIEW_DEFAULT)
        return bool(preview)

    return False


def _normalize_config_value(value):
    if value:
        value = '' if value in ["''", '""'] else value
    return value
