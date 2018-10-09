# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

import string 
import random
from datetime import datetime
from .utilities.helper import get_random_name

class AzureDevTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_pull_request_createUpdateVoteListAbandonReactivateComplete(self):
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com token=vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        #Generate random repo name
        random_repo_name = get_random_name(8) 
        
        try:
            #Create a repo with random name
            create_repo_command = 'az repos repo create --detect off --name ' + random_repo_name +' --project PullRequestLiveTest --output json'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            created_repo_id = repo_create_output["id"]
            assert len(created_repo_id) > 0
            
            #Import repo for testing
            import_repo_command = 'az repos import create --git-source-url https://dev.azure.com/AzureDevOpsCliTest/ImportRepoTest/_git/snakes-and-ladders --repository ' + created_repo_id + ' --project PullRequestLiveTest --detect Off --output json'
            import_repo_output = self.cmd(import_repo_command).get_output_in_json()
            import_repo_status = import_repo_output["status"]
            assert import_repo_status == 'completed'
            
            #Create a PR in imported repo
            pr_title = 'Fixing a bug in cli engine'
            create_pr_command = 'az repos pr create -p PullRequestLiveTest -r ' + created_repo_id + ' -s testbranch -t master --title "' + pr_title + '" -d "Sample PR description" --detect Off --output json'
            create_pr_output = self.cmd(create_pr_command).get_output_in_json()
            create_pr_id = create_pr_output["pullRequestId"]
            create_pr_datetime = datetime.strptime(create_pr_output["creationDate"], "%Y-%m-%dT%H:%M:%S.%f%z")
            assert create_pr_id > 0
            create_pr_id = str(create_pr_id)
            
            #Update PR to change description 
            updated_description = 'This should be the pr description'
            update_pr_command = 'az repos pr update --id ' + create_pr_id + ' -d "' + updated_description + '" --detect off --output json'
            update_pr_output = self.cmd(update_pr_command).get_output_in_json()
            update_pr_description = update_pr_output["description"]
            assert update_pr_description == updated_description
            
            #Vote on PR 
            vote_pr_command = 'az repos pr set-vote --id ' + create_pr_id + ' --vote approve --detect Off --output json'
            vote_pr_output = self.cmd(vote_pr_command).get_output_in_json()
            vote_pr_status = vote_pr_output["vote"]
            #From API documentation 10 - approved 5 - approved with suggestions 0 - no vote -5 - waiting for author -10 - rejected
            assert vote_pr_status == 10
            
            #List PR
            pr_list = self.cmd('az repos pr list --project PullRequestLiveTest --repository PullRequestLiveTest --detect Off --output json', checks=[
                self.check("[0].createdBy.displayName", "Gaurav Saral"),
                self.check("[0].description", 'Updated README.md'),
                self.check("[1].description", 'Updated EXAMPLE'),
            ]).get_output_in_json()
            assert len(pr_list) > 0
            
            #Show PR 
            show_pr_command = 'az repos pr show --id ' + create_pr_id + ' --detect Off --output json'
            show_pr_output = self.cmd(show_pr_command).get_output_in_json()
            show_pr_title = show_pr_output["title"]
            show_pr_description = show_pr_output["description"]
            assert show_pr_title == pr_title
            assert show_pr_description == update_pr_description
            
            #Abandon PR
            abandon_pr_command = 'az repos pr abandon --id ' + create_pr_id + ' --detect Off --output json'
            abandon_pr_output = self.cmd(abandon_pr_command).get_output_in_json()
            abandon_pr_status = abandon_pr_output["status"]
            assert abandon_pr_status == 'abandoned'
            
            #Reactivate PR 
            reactivate_pr_command = 'az repos pr reactivate --id ' + create_pr_id + ' --detect Off --output json'
            reactivate_pr_output = self.cmd(reactivate_pr_command).get_output_in_json()
            reactivate_pr_status = reactivate_pr_output["status"]
            assert reactivate_pr_status == 'active'
            
            #Complete PR 
            complete_pr_command = 'az repos pr complete --id ' + create_pr_id + ' --detect Off --output json'
            complete_pr_output = self.cmd(complete_pr_command).get_output_in_json()
            complete_pr_queued_time = datetime.strptime(complete_pr_output["completionQueueTime"], "%Y-%m-%dT%H:%M:%S.%f%z")
            complete_pr_completion_options = complete_pr_output["completionOptions"]
            assert len(complete_pr_completion_options) > 0
            assert create_pr_datetime < complete_pr_queued_time
        
        finally:
            #TestCleanup - Delete the temporary repo we created for the test
            list_repo_command = 'az repos repo list --project PullRequestLiveTest --output json --detect off'
            list_repo_output_before_delete = self.cmd(list_repo_command).get_output_in_json()
            delete_repo_command = 'az repos repo delete --detect off --id ' + created_repo_id + ' --project PullRequestLiveTest -y --output json'
            self.cmd(delete_repo_command)
            
            #Verify Deletion
            list_repo_output_after_delete = self.cmd(list_repo_command).get_output_in_json()
            assert len(list_repo_output_before_delete) == len(list_repo_output_after_delete) + 1
