from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

import string
import random

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

class ReposRepoTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_repos_createListShowDelete(self):
        random_name = random_string(8)
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com token=vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vc77xniwr23zylla')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vc77xniwr23zylla')

        create_repo_command = 'az repos repo create --detect off --name ' + random_name +' --project RepoCreateListShowDeleteTests'
        repo_create_output = self.cmd(create_repo_command).get_output_in_json()
        created_repo_id = repo_create_output["id"]
        assert len(created_repo_id) > 0

        list_repo_command = 'az repos repo list --detect off --project RepoCreateListShowDeleteTests'
        list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
        assert len(list_repo_output_before_delete) > 1

        show_repo_command = 'az repos repo show --detect off --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests'
        show_repo_output = self.cmd(show_repo_command).get_output_in_json()
        assert show_repo_output["id"] == created_repo_id
        
        delete_repo_command = 'az repos repo delete --detect off --id ' + created_repo_id + ' --project RepoCreateListShowDeleteTests -y'
        self.cmd(delete_repo_command)
        list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
        assert len(list_repo_output_before_delete) == len(list_repo_output_after_delete) + 1