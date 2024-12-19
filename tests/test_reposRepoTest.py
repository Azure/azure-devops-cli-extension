# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import (
    DevopsScenarioTest, get_random_name, disable_telemetry, set_authentication, get_test_org_from_env_variable)

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'

class ReposRepoTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_repos_createListShowDelete(self):
        random_name = get_random_name(8)
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        
        created_repo_id = None
        try:
            create_repo_command = 'az repos create --name ' + random_name +' --project RepoCreateListShowDeleteTests --output json --detect false'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            created_repo_id = repo_create_output["id"]
            created_repo_name = repo_create_output["name"]
            assert len(created_repo_id) > 0

            list_repo_command = 'az repos list --project RepoCreateListShowDeleteTests --output json  --detect false'
            verified_repo_list = False
            list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_before_delete:
                if(repos["id"] == created_repo_id):
                    verified_repo_list = True
            assert verified_repo_list == True

            show_repo_command = 'az repos show -r ' + created_repo_id + ' --project RepoCreateListShowDeleteTests --output json --detect false'
            show_repo_output = self.cmd(show_repo_command).get_output_in_json()
            assert show_repo_output["id"] == created_repo_id
            
            updated_repo_name = created_repo_name + 'Updated'
            update_repo_command = 'az repos update -r ' + created_repo_id + ' -p RepoCreateListShowDeleteTests --name ' + updated_repo_name  + ' -o json --detect false'
            update_repo_output = self.cmd(update_repo_command).get_output_in_json()
            assert update_repo_output["id"] == created_repo_id
            assert update_repo_output["name"] == updated_repo_name

        finally:
            delete_repo_command = 'az repos delete --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests -y --output json --detect false'
            self.cmd(delete_repo_command)
            
            #Verify Deletion
            list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_after_delete:
                if(repos["id"] == created_repo_id):
                    assert 0
                    