# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import pytest

from knack.util import CLIError
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'

class BoardsWorkItemTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_workItemCreateShowUpdateDelete(self):
        wi_name = 'sampleTask'
        wi_test_project_name = 'WorkItemCreateShowUpdateDeleteTests'
        wi_id =0
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        try:
            create_wi_command = 'az boards work-item create --project '+ wi_test_project_name +' --title ' + wi_name \
                                + ' --type Task  --detect false --output json'
            wi_create = self.cmd(create_wi_command, checks=[
                self.check('fields."System.AreaPath"', wi_test_project_name),
                self.check('fields."System.WorkItemType"', 'Task'),
                self.check('fields."System.Title"', wi_name)
            ]).get_output_in_json()

            wi_id = wi_create['id']

            show_wi_command ='az boards work-item show --org ' + DEVOPS_CLI_TEST_ORGANIZATION + ' --id '+ str(wi_id) + ' --detect false --output json'
            self.cmd(show_wi_command, checks=[
                self.check("id", wi_id)
            ]).get_output_in_json()

            update_wi_command = 'az boards work-item update --org ' + DEVOPS_CLI_TEST_ORGANIZATION + ' --id '+ str(wi_id)+' --state Done --detect false --output json'
            self.cmd(update_wi_command, checks=[
                self.check("id", wi_id),
                self.check('fields."System.AreaPath"', wi_test_project_name),
                self.check('fields."System.State"','Done')
            ]).get_output_in_json()

        finally:
            #delete the work item created for test
            delete_wi_command = ('az boards work-item delete --org {org_name} --id {wit_id} --project {project_name} '
                '--yes --detect false --output json'.format(org_name=DEVOPS_CLI_TEST_ORGANIZATION, wit_id=str(wi_id),
                project_name=wi_test_project_name))
            delete_wi_response = self.cmd(delete_wi_command , checks=[
                self.check('id', wi_id)
            ]).get_output_in_json()

            # verify if the work item is deleted or not
            with self.assertRaises(CLIError) as wi_except:
                wi_show = self.cmd(show_wi_command).get_output_in_json()
            self.assertEqual(str(wi_except.exception), 'TF401232: Work item ' + str(wi_id) + ' does not exist, or you do not have permissions to read it.')


