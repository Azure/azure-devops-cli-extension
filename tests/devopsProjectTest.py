# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

class DevopsProjectTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_devops_projects_ListShow(self):
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')

        # Create Project test cannot run in recording since create is a long running operation and
        # it just returns that operation succeeded so there is one GET project call made with name of project.
        known_project_name_in_organization = 'ProjectListShowTest'
        list_project_command = 'az dev project list --output json --detect off'
        list_project_output = self.cmd(list_project_command).get_output_in_json()
        #Verify known test projects in the list
        for project in list_project_output:
            if (project["name"] == known_project_name_in_organization):
                known_projects_id = project["id"]
        assert len(list_project_output) > 1
        assert len(known_projects_id) > 1

        show_project_command = 'az dev project show --id ' + known_projects_id + ' --output json --detect off'
        show_project_output = self.cmd(show_project_command).get_output_in_json()
        assert show_project_output["id"] == known_projects_id
        assert show_project_output["name"] == known_project_name_in_organization