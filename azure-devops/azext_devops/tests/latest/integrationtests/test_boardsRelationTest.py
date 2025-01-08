# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'
class BoardsRelationsTest(DevopsScenarioTest):
    def validate_relation_count_on_work_item(self, work_item_set, relation_count_set):
        index = 0
        for work_item in work_item_set:
            show_work_item_command = "az boards work-item show --id {0} --detect false --output json --expand relations".format(work_item['id'])
            work_item = self.cmd(show_work_item_command).get_output_in_json()
            if work_item['relations'] == None:
                assert relation_count_set[index] == 0
            else:
                assert len(work_item['relations']) == relation_count_set[index]

            index = index + 1

    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_boards_releations_create_remove(self):
        random_project_name = self.create_random_name(prefix='WIRel', length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            # lets create 4 work items
            wi_name = "Task_{}"
            wi_set = []
            for number in range(5):
                create_wi_command = 'az boards work-item create --project '+ random_project_name +' --title ' \
                                    + wi_name.format(number) +  ' --type Task  --detect false --output json'
                created_wit = self.cmd(create_wi_command).get_output_in_json()
                wi_set.append(created_wit)

            #add Task 1,2,3 as child of 0  (multiple add)
            create_relation_command = 'az boards work-item relation add --id {} --detect false --output json'.format(wi_set[0]['id']) \
                + ' --relation-type child --target-id {},{},{}'.format(wi_set[1]['id'], wi_set[2]['id'], wi_set[3]['id'])
            create_relation_output = self.cmd(create_relation_command).get_output_in_json()
            assert len(create_relation_output['relations']) == 3
            self.validate_relation_count_on_work_item(wi_set, [3, 1, 1, 1, 0])

            #remove 1,2 as child of 0  (multiple remove)
            remove_relation_command = 'az boards work-item relation remove --id {} -y --detect false --output json'.format(wi_set[0]['id']) \
                + ' --relation-type child --target-id {},{}'.format(wi_set[1]['id'], wi_set[2]['id'])
            remove_relation_output = self.cmd(remove_relation_command).get_output_in_json()
            assert len(remove_relation_output['relations']) == 1
            self.validate_relation_count_on_work_item(wi_set, [1, 0, 0, 1, 0])

            #add 4 as child of 0 (single add)
            create_relation_command = 'az boards work-item relation add --id {} --detect false --output json'.format(wi_set[0]['id']) \
                + ' --relation-type child --target-id {}'.format(wi_set[4]['id'])
            create_relation_output = self.cmd(create_relation_command).get_output_in_json()
            assert len(create_relation_output['relations']) == 2
            self.validate_relation_count_on_work_item(wi_set, [2, 0, 0, 1, 1])

            #remove 3 as child of 0 (single remove)
            remove_relation_command = 'az boards work-item relation remove -y --id {} --detect false --output json'.format(wi_set[0]['id']) \
                + ' --relation-type child --target-id {}'.format(wi_set[3]['id'])
            remove_relation_output = self.cmd(remove_relation_command).get_output_in_json()
            assert len(remove_relation_output['relations']) == 1
            self.validate_relation_count_on_work_item(wi_set, [1, 0, 0, 0, 1])

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
