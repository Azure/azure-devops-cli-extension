# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'https://dev.azure.com/devops-cli-test-org'

class PipelinesBuildTagTests(DevopsScenarioTest):    
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_build_tag_listAddDelete(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION + ' project=buildtests')

        build_definition_name = 'BuildTests Definition1'

        #QueueBuild to get a build ID
        queue_build_command = 'az pipelines build queue --definition-name "' + build_definition_name + '" --detect false --output json'
        queue_build_output = self.cmd(queue_build_command).get_output_in_json()
        queued_build_id = queue_build_output["id"]

        try:
            #Add build tag to queued build
            add_build_tag_command = 'az pipelines build tag add --build-id ' + str(queued_build_id) + ' --tags TestTag0 --detect false --output json'
            add_build_tag_output = self.cmd(add_build_tag_command).get_output_in_json()
            assert len(add_build_tag_output) == 1
            assert add_build_tag_output == ['TestTag0']

            #Add build tags to queued build
            add_build_tag_command = 'az pipelines build tag add --build-id ' + str(queued_build_id) + ' --tags "TestTag1,TestTag2" --detect false --output json'
            add_build_tag_output = self.cmd(add_build_tag_command).get_output_in_json()
            assert len(add_build_tag_output) == 3
            assert add_build_tag_output == ['TestTag0', 'TestTag1', "TestTag2"]

            #List build tags added to queued build
            list_build_tag_command = 'az pipelines build tag list --build-id ' + str(queued_build_id) + ' --detect false --output json'
            list_build_tag_output = self.cmd(list_build_tag_command).get_output_in_json()
            assert len(list_build_tag_output) == 3
            assert list_build_tag_output == ['TestTag0', 'TestTag1', "TestTag2"]

            #Delete build tag from queued build
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag2 --detect false --output json'
            delete_build_tag_output = self.cmd(delete_build_tag_command).get_output_in_json()
            assert len(delete_build_tag_output) == 2
            assert delete_build_tag_output == ['TestTag0', 'TestTag1']
        finally:
            #Delete tags added for test
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag1 --detect false --output json'
            self.cmd(delete_build_tag_command)
            delete_build_tag_command = 'az pipelines build tag delete --build-id ' + str(queued_build_id) + ' --tag TestTag0 --detect false --output json'
            self.cmd(delete_build_tag_command)

            #Verify deletion
            list_build_tag_command = 'az pipelines build tag list --build-id ' + str(queued_build_id) + ' --detect false --output json'
            add_build_tag_output = self.cmd(list_build_tag_command).get_output_in_json()
            if (len(add_build_tag_output) == 0):
                assert 1