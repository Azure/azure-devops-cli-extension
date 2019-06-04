# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class DevopsProjectTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_devops_projects_CreateListShowDelete(self):
        
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        
        random_project_name = self.create_random_name(prefix='projectTest', length=15)
        try:
            project_description = 'This is a sample project description'
            source_control_type = 'git'
            project_visibility = 'public'
            create_project_command = ('az devops project create --name ' + random_project_name + ' -d "' + project_description + 
            '" --source-control ' + source_control_type + ' --visibility ' + project_visibility + ' --output json --detect false')
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]
            assert len(created_project_id) > 0
            assert project_description == project_create_output["description"]
            assert project_visibility == project_create_output["visibility"].lower()
            assert source_control_type == project_create_output["capabilities"]["versioncontrol"]["sourceControlType"].lower()
            
            list_project_command = 'az devops project list --output json --detect false'
            list_project_output = self.cmd(list_project_command).get_output_in_json()
            verified_project_list = False
            assert len(list_project_output) > 1
            for project in list_project_output:
                if (project["id"] == created_project_id):
                    verified_project_list = True
            assert verified_project_list == True
            
            show_project_command = 'az devops project show --project ' + created_project_id + ' --output json --detect false'
            show_project_output = self.cmd(show_project_command).get_output_in_json()
            assert show_project_output["id"] == created_project_id
            assert show_project_output["name"] == random_project_name

        finally:
            #Delete the project create for the test
            delete_project_command = 'az devops project delete --id ' + created_project_id + ' -y --output json --detect false'
            self.cmd(delete_project_command)
            
            #Verify Deletion
            list_project_command = 'az devops project list --output json --detect false'
            list_project_output_after_delete = self.cmd(list_project_command).get_output_in_json()
            for project in list_project_output_after_delete:
                if (project["id"] == created_project_id):
                    assert 0
            
