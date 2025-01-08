# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from datetime import datetime
from .utilities.helper import (
    DevopsScenarioTest, get_random_name, disable_telemetry, set_authentication, get_test_org_from_env_variable)

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'

class AzReposPrPolicyTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_pull_request_policies_workitems(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION) 
         
        #List PR
        pr_list = self.cmd('az repos pr list --project PullRequestLiveTest --repository PullRequestLiveTest --detect false --output json', checks=[
            self.check("[0].description", "Updated README.md"),
            self.check("[1].description", "Updated README.md"),
        ]).get_output_in_json()
        assert len(pr_list) > 0

        pr_id_to_query = pr_list[1]["pullRequestId"] 

        #PR Policies list command
        list_pr_policies_command = 'az repos pr policy list --id ' + str(pr_id_to_query) + ' --detect false --output json'
        list_pr_policies_output = self.cmd(list_pr_policies_command).get_output_in_json()
        assert len(list_pr_policies_output) > 0

        #PR policies queue evaluation command
        policy_evaluation_id = list_pr_policies_output[0]["evaluationId"]
        queue_pr_policy_command = ('az repos pr policy queue --id ' + str(pr_id_to_query) + ' -e ' + policy_evaluation_id + 
        ' --detect false --output json')
        queue_pr_policy_output = self.cmd(queue_pr_policy_command).get_output_in_json()
        assert len(queue_pr_policy_output) > 0
        assert queue_pr_policy_output["evaluationId"] == policy_evaluation_id
        assert queue_pr_policy_output["status"] == 'queued'

        #PR work-item add command
        work_item_ids_to_add = '129 130'
        work_item_id_to_remove = '130'

        add_wit_pr_command = ('az repos pr work-item add --id ' + str(pr_id_to_query) + ' --work-items ' + work_item_ids_to_add + 
            ' --detect false --output json')
        add_wit_pr_output = self.cmd(add_wit_pr_command).get_output_in_json()
        assert len(add_wit_pr_output) > 1

        #PR work-item list command
        list_wit_pr_command = 'az repos pr work-item list --id ' + str(pr_id_to_query) + ' --detect false --output json'
        list_wit_pr_output = self.cmd(list_wit_pr_command).get_output_in_json()
        assert len(list_wit_pr_output) > 1

        #PR work-item remove command
        remove_wit_pr_command = ('az repos pr work-item remove --id ' + str(pr_id_to_query) + ' --work-items ' + work_item_id_to_remove + 
            ' --detect false --output json')
        self.cmd(remove_wit_pr_command)
        #verify removed
        list_wit_pr_output = self.cmd(list_wit_pr_command, checks=[
            self.check("[0].id", "129")
        ]).get_output_in_json()
        assert len(list_wit_pr_output) == 1
        
