# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

from .utilities.helper import get_random_name

class ReposRepoTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_repos_createListShowDelete(self):
        random_name = get_random_name(8)
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com token=vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')

        create_repo_command = 'az repos repo create --name ' + random_name +' --project RepoCreateListShowDeleteTests --output json --detect off'
        repo_create_output = self.cmd(create_repo_command).get_output_in_json()
        created_repo_id = repo_create_output["id"]
        assert len(created_repo_id) > 0

        list_repo_command = 'az repos repo list --project RepoCreateListShowDeleteTests --output json  --detect off'
        list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
        assert len(list_repo_output_before_delete) > 1

        show_repo_command = 'az repos repo show --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests --output json --detect off'
        show_repo_output = self.cmd(show_repo_command).get_output_in_json()
        assert show_repo_output["id"] == created_repo_id
        
        delete_repo_command = 'az repos repo delete --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests -y --output json --detect off'
        self.cmd(delete_repo_command)
        list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
        assert len(list_repo_output_before_delete) == len(list_repo_output_after_delete) + 1