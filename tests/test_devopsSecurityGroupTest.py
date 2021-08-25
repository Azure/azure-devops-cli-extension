# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from knack.util import CLIError
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'https://dev.azure.com/devops-cli-test-org'
_TEST_EMAIL_ID = 'new_user_test@outlook.com'
_GROUP_DESCRIPTION = 'some description'


class GroupTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_devops_group_and_member_tests(self):
        random_project_name = self.create_random_name(prefix='GroupTests_',length=15)
        project_group_name = 'project security ' + self.create_random_name(prefix='GroupName_',length=15)
        org_group_name = 'org security ' + self.create_random_name(prefix='GroupName_',length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]
            
            list_project_groups = self.cmd('az devops security group list -o json --detect false').get_output_in_json()
            assert list_project_groups.get('graphGroups') is not None
            list_response = list_project_groups['graphGroups']
            project_group_list_length = len(list_response)
            for entry in list_response:
                if entry['displayName'] == 'Project Valid Users':
                    valid_users_group_descriptor = entry['descriptor']
            
            #add user
            user_add_response = self.cmd('az devops user add -o json --detect false --email-id ' + _TEST_EMAIL_ID + ' --license-type stakeholder').get_output_in_json()
            user_id = user_add_response['id']
            assert user_add_response['user']['mailAddress'] == _TEST_EMAIL_ID

            list_valid_users_members = self.cmd('az devops security group membership list --id '+ valid_users_group_descriptor +' -o json --detect false').get_output_in_json()
            len_valid_users_members = len(list_valid_users_members)
            assert len_valid_users_members == 5

            create_project_group = self.cmd('az devops security group create --name "'+ project_group_name +'" --description "'+ _GROUP_DESCRIPTION +'" -o json --detect false').get_output_in_json()
            assert create_project_group['displayName'] == project_group_name
            project_group_descriptor = create_project_group['descriptor']

            self.sleep_in_live_run(60)

            show_project_group = self.cmd('az devops security group show --id "'+ project_group_descriptor +'" -o json --detect false').get_output_in_json()
            assert show_project_group['displayName'] == project_group_name
            assert project_group_descriptor == show_project_group['descriptor']

            group_found = False
            list_project_groups = self.cmd('az devops security group list -o json --detect false').get_output_in_json()
            assert list_project_groups.get('graphGroups') is not None
            list_response = list_project_groups['graphGroups']
            for entry in list_response:
                if entry['displayName'] == project_group_name:
                    group_found = True
            assert group_found is True

            #create 2nd group
            project_group_name2 = 'project security ' + self.create_random_name(prefix='GroupName_',length=15)
            create_project_group = self.cmd('az devops security group create --name "'+ project_group_name2 +'" --groups "'+ list_response[0]['descriptor'] +'" -o json --detect false').get_output_in_json()
            assert create_project_group['displayName'] == project_group_name2
            project_group_descriptor2 = create_project_group['descriptor']

            self.sleep_in_live_run(60)
            #create 3rd group and add it to multiple existing groups
            project_group_name3 = 'project security ' + self.create_random_name(prefix='GroupName_',length=15)
            create_project_group = self.cmd('az devops security group create --name "'+ project_group_name3 +'" --groups "'+ list_response[0]['descriptor'] + ',' + project_group_descriptor2 +'" -o json --detect false').get_output_in_json()
            assert create_project_group['displayName'] == project_group_name3
            project_group_descriptor3 = create_project_group['descriptor']

            self.sleep_in_live_run(60)
            # validate list membership
            list_valid_users_members = self.cmd('az devops security group membership list --id '+ valid_users_group_descriptor +' -o json --detect false').get_output_in_json()
            new_valid_users_members_len = len(list_valid_users_members)
            assert new_valid_users_members_len == len_valid_users_members + 3

            # member relationship
            list_group_name3_members = self.cmd('az devops security group membership list --id '+ project_group_descriptor3 +' -o json --detect false').get_output_in_json()
            assert len(list_group_name3_members) == 0

            self.sleep_in_live_run(60) # Test is still flaky without this sleep only two memberships are reflected in time for the call.
            # member of 
            list_group_name3_memberof = self.cmd('az devops security group membership list --id '+ project_group_descriptor3 +' --relationship memberof -o json --detect false').get_output_in_json()
            assert len(list_group_name3_memberof) == 3

            # add membership
            add_membership = self.cmd('az devops security group membership add --group-id '+ project_group_descriptor +' --member-id '+ project_group_descriptor3 +' -o json --detect false').get_output_in_json()
            
            # add user
            add_membership = self.cmd('az devops security group membership add --group-id '+ project_group_descriptor +' --member-id '+ _TEST_EMAIL_ID  +' -o json --detect false').get_output_in_json()

            self.sleep_in_live_run(60)
            list_group_name3_memberof = self.cmd('az devops security group membership list --id '+ project_group_descriptor3 +' --relationship memberof -o json --detect false').get_output_in_json()
            assert len(list_group_name3_memberof) == 4

            list_project_group_name_members = self.cmd('az devops security group membership list --id '+ project_group_descriptor +' -o json --detect false').get_output_in_json()
            assert len(list_project_group_name_members) == 2

            # remove membership
            remove_membership = self.cmd('az devops security group membership remove --group-id '+ project_group_descriptor +' --member-id '+ project_group_descriptor3 +' -y -o json --detect false')
            
            self.sleep_in_live_run(60)
            list_group_name3_memberof = self.cmd('az devops security group membership list --id '+ project_group_descriptor3 +' --relationship memberof -o json --detect false').get_output_in_json()
            assert len(list_group_name3_memberof) == 3

            #update
            project_group_name4 = 'project security ' + self.create_random_name(prefix='GroupName_',length=15)
            update_project_group = self.cmd('az devops security group update --name "'+ project_group_name4 +'" --id "'+ project_group_descriptor3 + '" -o json --detect false').get_output_in_json()
            assert update_project_group['displayName'] == project_group_name4
            assert project_group_descriptor3 == update_project_group['descriptor']

            #delete
            self.sleep_in_live_run(60)
            delete_project_group = self.cmd('az devops security group delete --id "'+ project_group_descriptor3 +'" -y -o json --detect false')

            self.sleep_in_live_run(60)
            # validate list
            list_valid_users_members = list_project_groups = self.cmd('az devops security group membership list --id '+ valid_users_group_descriptor +' -o json --detect false').get_output_in_json()
            new_valid_users_members_len = len(list_valid_users_members)
            assert new_valid_users_members_len == len_valid_users_members + 2

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
