# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from azext_devops.dev.team.credentials import credential_set
from .utilities.helper import ( get_random_name , DEVOPS_CLI_TEST_ORGANIZATION , DEVOPS_CLI_TEST_PAT_TOKEN, disable_telemetry )

class ReposRepoTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_repos_createListShowDelete(self):
        random_name = get_random_name(8)

        with patch('azext_devops.dev.team.credentials._get_pat_token') as mock_pat_token:  
            mock_pat_token.return_value = DEVOPS_CLI_TEST_PAT_TOKEN
            self.cmd('az devops login')
            self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        try:
            create_repo_command = 'az repos create --name ' + random_name +' --project RepoCreateListShowDeleteTests --output json --detect off'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            created_repo_id = repo_create_output["id"]
            assert len(created_repo_id) > 0

            list_repo_command = 'az repos list --project RepoCreateListShowDeleteTests --output json  --detect off'
            verified_repo_list = False
            list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_before_delete:
                if(repos["id"] == created_repo_id):
                    verified_repo_list = True
            assert verified_repo_list == True

            show_repo_command = 'az repos show --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests --output json --detect off'
            show_repo_output = self.cmd(show_repo_command).get_output_in_json()
            assert show_repo_output["id"] == created_repo_id
            
        finally:
            delete_repo_command = 'az repos delete --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests -y --output json --detect off'
            self.cmd(delete_repo_command)
            
            #Verify Deletion
            list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
            for repos in list_repo_output_after_delete:
                if(repos["id"] == created_repo_id):
                    assert 0
                    