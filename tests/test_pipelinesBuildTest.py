# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/devops-cli-test-org'

class PipelinesTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_build_listQueueShow(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION + ' project=buildtests')

        build_definition_name = 'BuildTests Definition1'

        #QueueBuild
        queue_build_command = 'az pipelines build queue --definition-name "' + build_definition_name + '" --detect false --output json'
        queue_build_output = self.cmd(queue_build_command).get_output_in_json()
        assert len(queue_build_output) > 0
        queued_build_id = queue_build_output["id"]
        assert queued_build_id > 0
        
        #Show Build 
        show_build_command = 'az pipelines build show --id ' + str(queued_build_id) + ' --detect false --output json'
        show_build_output = self.cmd(show_build_command).get_output_in_json()
        assert len(show_build_output) > 0
        assert show_build_output["definition"]["name"] == build_definition_name
        assert show_build_output["id"] == queued_build_id

        #Extract definition Id to test filtering in list command
        definition_id_filter = show_build_output["definition"]["id"]
        
        #List Builds 
        list_build_command_without_filters = 'az pipelines build list --detect false --output json'
        list_build_output_without_filters = self.cmd(list_build_command_without_filters).get_output_in_json()
        assert len(list_build_output_without_filters) > 0
        
        list_build_command_with_filters = 'az pipelines build list --definition-ids ' + str(definition_id_filter) + ' --detect false --output json'
        list_build_output_with_filters = self.cmd(list_build_command_with_filters).get_output_in_json()
        assert len(list_build_output_with_filters) > 0
        #all builds belong to same build definition
        for build in list_build_output_with_filters:
            assert build["definition"]["id"] == definition_id_filter

        assert len(list_build_output_without_filters) > len(list_build_output_with_filters)