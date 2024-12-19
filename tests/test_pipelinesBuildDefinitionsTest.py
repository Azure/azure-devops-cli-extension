# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class PipelinesBuildDefinitionTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_build_definition_listShow(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION + ' project=buildtests')

        build_definition_name = 'BuildTests Definition1'

        #list build definition
        list_build_definition_command = 'az pipelines build definition list --detect false --output json'
        list_build_definition_output = self.cmd(list_build_definition_command).get_output_in_json()
        assert len(list_build_definition_output) > 0
        for build_definition in list_build_definition_output:
            if(build_definition["name"] == build_definition_name):
                build_definition_id = build_definition["id"]
            assert build_definition["id"] > 0


        #show build definition
        show_build_definition_command = 'az pipelines build definition show --id ' + str(build_definition_id) + ' --detect false --output json'
        show_build_definition_output = self.cmd(show_build_definition_command).get_output_in_json()
        assert len(show_build_definition_output) > 0
        assert show_build_definition_output["name"] == build_definition_name
   