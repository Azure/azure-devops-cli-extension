# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import ( DEVOPS_CLI_TEST_ORGANIZATION , DEVOPS_CLI_TEST_PAT_TOKEN, disable_telemetry, PAT_ENV_VARIABLE_NAME )

class PipelinesBuildDefinitionTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_build_definition_listShow(self):

        os.environ[PAT_ENV_VARIABLE_NAME] = DEVOPS_CLI_TEST_PAT_TOKEN
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        build_definition_name = 'BuildTests Definition1'

        #list build definition
        list_build_definition_command = 'az pipelines build definition list --detect off --output json'
        list_build_definition_output = self.cmd(list_build_definition_command).get_output_in_json()
        assert len(list_build_definition_output) > 0
        for build_definition in list_build_definition_output:
            if(build_definition["name"] == build_definition_name):
                build_definition_id = build_definition["id"]
            assert build_definition["id"] > 0


        #show build definition
        show_build_definition_command = 'az pipelines build definition show --definition-id ' + str(build_definition_id) + ' --detect off --output json'
        show_build_definition_output = self.cmd(show_build_definition_command).get_output_in_json()
        assert len(show_build_definition_output) > 0
        assert show_build_definition_output["name"] == build_definition_name
   