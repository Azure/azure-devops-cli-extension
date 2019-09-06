# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'https://dev.azure.com/gsaralprivate'

class TestInvoke(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_invoke_command_basic(self):
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION)

        projects_classic = self.cmd('az devops project list -o json --detect false').get_output_in_json()
        projects = self.cmd('az devops invoke --area core --resource projects -o json --detect false').get_output_in_json()['value']
        assert len(projects) == len(projects_classic)
