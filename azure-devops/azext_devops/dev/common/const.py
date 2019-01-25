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

COMMENT_REQUIREMENTS_POLICY = 'CommentRequirementsPolicy'
COMMENT_REQUIREMENTS_POLICY_ID = 'c6a1889d-b943-4856-b76f-9e46bb6b0df2'

MERGE_STRATEGY_POLICY = 'MergeStrategyPolicy'
MERGE_STRATEGY_POLICY_ID = 'fa4e907d-c16b-4a4c-9dfa-4916e5d171ab'

FILE_SIZE_POLICY = 'FileSizePolicy'
FILE_SIZE_POLICY_ID = '2e26e725-8201-4edd-8bf5-978563c34a80'

WORKITEM_LINKING_POLICY = 'WorkItemLinkingPolicy'
WORKITEM_LINKING_POLICY_ID = '40e92b44-2fe1-4dd6-b3d8-74a9c21d0c6e'

STATUS_POLICY = 'StatusPolicy'
STATUS_POLICY_ID = 'cbdc66da-9728-4af8-aada-9a5a32e4a226'

REPO_POLICY_TYPE = [APPROVER_COUNT_POLICY, BUILD_POLICY, COMMENT_REQUIREMENTS_POLICY, MERGE_STRATEGY_POLICY,
                    FILE_SIZE_POLICY, WORKITEM_LINKING_POLICY, STATUS_POLICY]
