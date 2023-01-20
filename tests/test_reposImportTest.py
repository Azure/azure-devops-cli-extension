# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable, get_random_name

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/devops-cli-test-org'

class ReposImportTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_repos_import_create(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        #Generate random repo name
        random_repo_name = get_random_name(8) 
        
        try:
            #Create a repo with random name
            print(DEVOPS_CLI_TEST_ORGANIZATION)
            create_repo_command = 'az repos create --detect false --name ' + random_repo_name +' --project TestSupportProject --output json'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            created_repo_id = repo_create_output["id"]
            assert len(created_repo_id) > 0
            
            #Import repo
            import_repo_command = 'az repos import create --git-source-url https://dev.azure.com/devops-cli-test-org/TestSupportProject/_git/snakes-and-ladders --repository ' + created_repo_id + ' --project TestSupportProject --detect false --output json'
            import_repo_output = self.cmd(import_repo_command).get_output_in_json()
            import_repo_status = import_repo_output["status"]
            assert import_repo_status == 'completed'
            list_repo_command = 'az repos list --project TestSupportProject --output json --detect false'
            verified_repo_list = False
            list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_before_delete:
                if(repos["id"] == created_repo_id):
                    verified_repo_list = True
            assert verified_repo_list == True
            

        finally:
            #TestCleanup - Delete the temporary repo we created for the test
            list_repo_command = 'az repos list --project TestSupportProject --output json --detect false'
            delete_repo_command = 'az repos delete --detect false --id ' + created_repo_id + ' --project TestSupportProject -y --output json'
            self.cmd(delete_repo_command)
            
            #Verify Deletion
            list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_after_delete:
                if(repos["id"] == created_repo_id):
                    assert 0