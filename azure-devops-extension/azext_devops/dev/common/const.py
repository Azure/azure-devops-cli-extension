# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os 

from azure.cli.core._environment import get_config_dir

# Config directory
AZ_GLOBAL_CONFIG_DIR = get_config_dir()
AZ_DEVOPS_CONFIG_DIR_NAME = 'azuredevops' 
AZ_DEVOPS_CONFIG_DIR = os.path.join(AZ_GLOBAL_CONFIG_DIR, AZ_DEVOPS_CONFIG_DIR_NAME)


# Environment Variables
CLI_ENV_VARIABLE_PREFIX = 'AZURE_DEVOPS_CLI_'
AZ_DEVOPS_CONFIG_DIR_ENVKEY =  CLI_ENV_VARIABLE_PREFIX + 'CONFIG_DIR'
