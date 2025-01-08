# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'


class BoardsQueryTests(DevopsScenarioTest): 
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_queryShow(self):
        wi_test_project_name = 'WorkItemCreateShowUpdateDeleteTests'
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        show_query_command_with_id = 'az boards query --org '+ DEVOPS_CLI_TEST_ORGANIZATION +' --detect false -p ' + wi_test_project_name + ' --id 253d8eb4-0bd1-4c92-adc9-d305c8b99b92 --output json'
        query_result = self.cmd(show_query_command_with_id).get_output_in_json()
        assert len(query_result) > 0

        wiql_string = "select [System.Id], [System.WorkItemType], [System.Title], [System.AssignedTo], [System.State], [System.Tags] from WorkItems where [System.TeamProject] = 'WorkItemCreateShowUpdateDeleteTests' and [System.WorkItemType] = 'Task'"
        show_query_command_with_wiql = 'az boards query --org ' + DEVOPS_CLI_TEST_ORGANIZATION +' -p WorkItemCreateShowUpdateDeleteTests --wiql "' + wiql_string +'" --output json'
        query_result = self.cmd(show_query_command_with_wiql).get_output_in_json()
        assert len(query_result) > 0