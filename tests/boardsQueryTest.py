# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

class AzureDevTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_queryShow(self):
        wi_test_project_name = 'WorkItemCreateShowUpdateDeleteTests'
        wi_account_instance='https://AzureDevOpsCliTest.visualstudio.com'
        wi_account_pat = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'

        self.cmd('az devops configure --defaults organization=' + wi_account_instance)
        self.cmd('az devops login --token ' + wi_account_pat)

        show_query_command_with_id = 'az boards query --org https://AzureDevOpsCliTest.visualstudio.com --detect off -p ' + wi_test_project_name + ' --id 51a3e288-2372-4af7-b722-79806154084b --output json'
        query_result = self.cmd(show_query_command_with_id).get_output_in_json()
        assert len(query_result) > 0

        wiql_string = "select [System.Id], [System.WorkItemType], [System.Title], [System.AssignedTo], [System.State], [System.Tags] from WorkItems where [System.TeamProject] = 'WorkItemCreateShowUpdateDeleteTests' and [System.WorkItemType] = 'Bug' and [System.State] = 'Active'"
        show_query_command_with_wiql = 'az boards query --org https://AzureDevOpsCliTest.visualstudio.com -p WorkItemCreateShowUpdateDeleteTests --wiql "' + wiql_string +'" --output json'
        query_result = self.cmd(show_query_command_with_wiql).get_output_in_json()
        assert len(query_result) > 0