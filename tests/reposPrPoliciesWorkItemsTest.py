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
from datetime import datetime
from .utilities.helper import ( get_random_name , DEVOPS_CLI_TEST_ORGANIZATION , DEVOPS_CLI_TEST_PAT_TOKEN )

class AzReposPrPolicyTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_pull_request_policies_workitems(self):

        with patch('azext_devops.dev.team.credentials._get_pat_token') as mock_pat_token:  
            mock_pat_token.return_value = DEVOPS_CLI_TEST_PAT_TOKEN
            self.cmd('az devops login')
            self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        
        #List PR
        pr_list = self.cmd('az repos pr list --project PullRequestLiveTest --repository PullRequestLiveTest --detect off --output json', checks=[
            self.check("[0].createdBy.displayName", "Gaurav Saral"),
            self.check("[0].description", 'Updated README.md'),
            self.check("[1].description", 'Updated EXAMPLE'),
        ]).get_output_in_json()
        assert len(pr_list) > 0

        pr_id_to_query = pr_list[0]["pullRequestId"]
        
        #PR Policies list command
        list_pr_policies_command = 'az repos pr policies list --id ' + str(pr_id_to_query) + ' --detect off --output json'
        list_pr_policies_output = self.cmd(list_pr_policies_command).get_output_in_json()
        assert len(list_pr_policies_output) > 0

        #PR policies queue evaluation command
        policy_evaluation_id = list_pr_policies_output[0]["evaluationId"]
        queue_pr_policy_command = ('az repos pr policies queue --id ' + str(pr_id_to_query) + ' -e ' + policy_evaluation_id + 
        ' --detect off --output json')
        queue_pr_policy_output = self.cmd(queue_pr_policy_command).get_output_in_json()
        assert len(queue_pr_policy_output) > 0
        assert queue_pr_policy_output["evaluationId"] == policy_evaluation_id
        assert queue_pr_policy_output["status"] == 'queued'

        #PR work-items add command
        work_item_ids_to_add = '20 21'
        work_item_id_to_remove = '20'
        add_wit_pr_command = ('az repos pr work-items add --id ' + str(pr_id_to_query) + ' --work-items ' + work_item_ids_to_add + 
            ' --detect off --output json')
        add_wit_pr_output = self.cmd(add_wit_pr_command).get_output_in_json()
        assert len(add_wit_pr_output) > 1

        #PR work-items list command
        list_wit_pr_command = 'az repos pr work-items list --id ' + str(pr_id_to_query) + ' --detect off --output json'
        list_wit_pr_output = self.cmd(list_wit_pr_command).get_output_in_json()
        assert len(list_wit_pr_output) > 1

        #PR work-items remove command
        remove_wit_pr_command = ('az repos pr work-items remove --id ' + str(pr_id_to_query) + ' --work-items ' + work_item_id_to_remove + 
            ' --detect off --output json')
        self.cmd(remove_wit_pr_command)
        #verify removed
        list_wit_pr_output = self.cmd(list_wit_pr_command, checks=[
            self.check("[0].id", "21")
        ]).get_output_in_json()
        assert len(list_wit_pr_output) == 1
        
