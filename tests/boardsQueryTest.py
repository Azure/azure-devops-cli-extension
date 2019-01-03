# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import ( DEVOPS_CLI_TEST_ORGANIZATION , DEVOPS_CLI_TEST_PAT_TOKEN, disable_telemetry, PAT_ENV_VARIABLE_NAME )

class BoardsQueryTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_queryShow(self):
        wi_test_project_name = 'WorkItemCreateShowUpdateDeleteTests'

        os.environ[PAT_ENV_VARIABLE_NAME] = DEVOPS_CLI_TEST_PAT_TOKEN
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        show_query_command_with_id = 'az boards query --org '+ DEVOPS_CLI_TEST_ORGANIZATION +' --detect off -p ' + wi_test_project_name + ' --id 51a3e288-2372-4af7-b722-79806154084b --output json'
        query_result = self.cmd(show_query_command_with_id).get_output_in_json()
        assert len(query_result) > 0

        wiql_string = "select [System.Id], [System.WorkItemType], [System.Title], [System.AssignedTo], [System.State], [System.Tags] from WorkItems where [System.TeamProject] = 'WorkItemCreateShowUpdateDeleteTests' and [System.WorkItemType] = 'Bug' and [System.State] = 'Active'"
        show_query_command_with_wiql = 'az boards query --org ' + DEVOPS_CLI_TEST_ORGANIZATION +' -p WorkItemCreateShowUpdateDeleteTests --wiql "' + wiql_string +'" --output json'
        query_result = self.cmd(show_query_command_with_wiql).get_output_in_json()
        assert len(query_result) > 0