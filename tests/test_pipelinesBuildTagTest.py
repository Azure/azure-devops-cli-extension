# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DEVOPS_CLI_TEST_ORGANIZATION, disable_telemetry, set_authentication

class PipelinesBuildTagTests(ScenarioTest):    
    @disable_telemetry
    @set_authentication
    def test_build_tag_listAddDelete(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION + ' project=buildtests')

        build_definition_name = 'BuildTests Definition1'

        #QueueBuild to get a build ID
        queue_build_command = 'az pipelines build queue --definition-name "' + build_definition_name + '" --detect off --output json'
        queue_build_output = self.cmd(queue_build_command).get_output_in_json()
        queued_build_id = queue_build_output["id"]

        try:
            #Add build tag to queued build
            add_build_tag_command = 'az pipelines build tag add --build-id ' + str(queued_build_id) + ' --tags TestTag0 --detect off --output json'
            add_build_tag_output = self.cmd(add_build_tag_command).get_output_in_json()
            assert len(add_build_tag_output) == 1
            assert add_build_tag_output == ['TestTag0']

            #Add build tags to queued build
            add_build_tag_command = 'az pipelines build tag add --build-id ' + str(queued_build_id) + ' --tags TestTag1,TestTag2 --detect off --output json'
            add_build_tag_output = self.cmd(add_build_tag_command).get_output_in_json()
            assert len(add_build_tag_output) == 3
            assert add_build_tag_output == ['TestTag0', 'TestTag1', "TestTag2"]

            #List build tags added to queued build
            show_build_tag_command = 'az pipelines build tag show --build-id ' + str(queued_build_id) + ' --detect off --output json'
            show_build_tag_output = self.cmd(show_build_tag_command).get_output_in_json()
            assert len(show_build_tag_output) == 3
            assert show_build_tag_output == ['TestTag0', 'TestTag1', "TestTag2"]

            #Delete build tag from queued build
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag2 --detect off --output json'
            delete_build_tag_output = self.cmd(delete_build_tag_command).get_output_in_json()
            assert len(delete_build_tag_output) == 3
            assert delete_build_tag_output == ['TestTag0', 'TestTag1']
        finally:
            #Delete tags added for test
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag1 --detect off --output json'
            self.cmd(delete_build_tag_command)
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag0 --detect off --output json'
            self.cmd(delete_build_tag_command)

            #Verify deletion
            show_build_tag_command = 'az pipelines build tag show --build-id ' + str(queued_build_id) + ' --detect off --output json'
            show_build_tag_output = self.cmd(show_build_tag_command).get_output_in_json()
            if (len(show_build_tag_output) == 0):
                assert 0