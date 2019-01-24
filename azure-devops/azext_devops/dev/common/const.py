# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.core._environment import get_config_dir

# Config directory
AZ_CLI_GLOBAL_CONFIG_DIR = get_config_dir()
_AZ_DEVOPS_CONFIG_DIR_NAME = 'azuredevops'
AZ_DEVOPS_DEFAULT_CONFIG_DIR = os.path.join(AZ_CLI_GLOBAL_CONFIG_DIR, _AZ_DEVOPS_CONFIG_DIR_NAME)


# Environment Variables
CLI_ENV_VARIABLE_PREFIX = 'AZURE_DEVOPS_EXT_'
AZ_DEVOPS_CONFIG_DIR_ENVKEY = CLI_ENV_VARIABLE_PREFIX + 'CONFIG_DIR'

# Config file constants
CONFIG_FILE_NAME = 'config'
DEFAULTS_SECTION = 'defaults'
DEVOPS_ORGANIZATION_DEFAULT = 'organization'
DEVOPS_TEAM_PROJECT_DEFAULT = 'project'
PAT_ENV_VARIABLE_NAME = CLI_ENV_VARIABLE_PREFIX + 'PAT'
AUTH_TOKEN_ENV_VARIABLE_NAME = CLI_ENV_VARIABLE_PREFIX + 'AUTH_TOKEN'

# policy constants

APPROVER_COUNT_POLICY = 'ApproverCountPolicy'
APPROVER_COUNT_POLICY_ID = 'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd'

BUILD_POLICY = 'Buildpolicy'
BUILD_POLICY_ID = '0609b952-1397-4640-95ec-e00a01b2c241'

REPO_POLICY_TYPE = [APPROVER_COUNT_POLICY, BUILD_POLICY]
