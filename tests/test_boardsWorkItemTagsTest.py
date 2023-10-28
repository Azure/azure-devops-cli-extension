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

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'https://dev.azure.com/thomasmoerkerken'

class BoardsWorkItemTagsTests(DevopsScenarioTest):

    @disable_telemetry
    @set_authentication
    @AllowLargeResponse(size_kb=3072)
    def test_boards_work_item_tags_add_list_remove_tag(self):
        wi_name = 'samplebug'
        wi_test_project_name = 'WorkItemAddListRemoveTagTests'
        wi_id = 0
        wi_tag1 = "my tag"
        wi_tag2 = "tag2"
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        try:
            create_wi_command = (f'az boards work-item create --project {wi_test_project_name} --title {wi_name} '
                                ' --type Bug  --detect false --output json')
            wi_create = self.cmd(create_wi_command, checks=[
                self.check('fields."System.AreaPath"', wi_test_project_name),
                self.check('fields."System.WorkItemType"', 'Bug'),
                self.check('fields."System.Title"', wi_name)
            ]).get_output_in_json()

            wi_id = wi_create['id']

            show_wi_command = (f'az boards work-item tag add --tag "{wi_tag1}" --id {str(wi_id)} '
                               f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --detect false --output json')
            self.cmd(show_wi_command, checks=[
                self.check('fields."System.Tags"', wi_tag1)
            ]).get_output_in_json()

            show_wi_command = (f'az boards work-item tag add --tag "{wi_tag2}" --id {str(wi_id)} '
                               f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --detect false --output json')
            self.cmd(show_wi_command, checks=[
                self.check('fields."System.Tags"', wi_tag1 + '; ' + wi_tag2)
            ]).get_output_in_json()

            list_wi_command = (f'az boards work-item tag list --id {str(wi_id)} '
                               f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --detect false --output json')
            self.cmd(list_wi_command, checks=[
                self.check("id", wi_id),
                self.check('fields."System.Tags"', f'{wi_tag1}; {wi_tag2}')
            ]).get_output_in_json()

            remove_wi_command = (f'az boards work-item tag remove --tag "{wi_tag1}" --id {str(wi_id)} '
                                 f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --detect false --output json')
            self.cmd(remove_wi_command, checks=[
                self.check("id", wi_id),
                self.check('fields."System.Tags"', wi_tag2)
            ]).get_output_in_json()

            remove_wi_command = (f'az boards work-item tag remove --tag "{wi_tag2}" --id {str(wi_id)} '
                                 f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --detect false --output json')
            self.cmd(remove_wi_command, checks=[
                self.check("id", wi_id),
                self.check('fields."System.Tags"', None)
            ]).get_output_in_json()

        finally:
            #delete the work item created for test
            delete_wi_command = (f'az boards work-item delete --id {str(wi_id)} '
                                 f'--org {DEVOPS_CLI_TEST_ORGANIZATION} --project {wi_test_project_name} '
                                '--yes --detect false --output json')
            self.cmd(delete_wi_command , checks=[
                self.check('id', wi_id)
            ]).get_output_in_json()

            # verify if the work item is deleted or not
            with self.assertRaises(CLIError) as wi_except:
                self.cmd(show_wi_command).get_output_in_json()
            self.assertEqual(str(wi_except.exception), (f'TF401232: Work item {str(wi_id)} does not exist, '
                                                        'or you do not have permissions to read it.'))
