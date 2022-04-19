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


class TestUser(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_devops_user_command_addUpdateListShowRemove(self):
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION)
        try:
            user_id = None
            # check user list before adding the user
            list_response = self.cmd('az devops user list -o json --detect false').get_output_in_json()
            assert list_response.get('members') is not None
            user_list_response = list_response['members']
            assert len(user_list_response) > 0
            user_id_found = False
            for item in user_list_response :
                if item['user']['mailAddress'] == _TEST_EMAIL_ID:
                    user_id_found = True
            # Remove the user if already present in the organization.
            if user_id_found == True:
                user_remove_response = self.cmd('az devops user remove --user ' + _TEST_EMAIL_ID + ' -o json --detect false -y')

            #add user
            user_add_response = self.cmd('az devops user add -o json --detect false --email-id ' + _TEST_EMAIL_ID + ' --license-type stakeholder').get_output_in_json()
            user_id = user_add_response['id']
            assert user_add_response['user']['mailAddress'] == _TEST_EMAIL_ID

            # check if user is present in list response
            list_response = self.cmd('az devops user list -o json --detect false').get_output_in_json()
            assert list_response.get('members') is not None
            user_list_response = list_response['members']
            assert len(user_list_response) > 1
            user_id_found = False
            for item in user_list_response :
                if item['user']['mailAddress'] == _TEST_EMAIL_ID:
                    user_id_found = True
            assert user_id_found == True

            # show user details
            user_show_response = self.cmd('az devops user show -o json --detect false --user ' + _TEST_EMAIL_ID).get_output_in_json()
            assert user_show_response['id'] == user_id
            assert user_show_response['user']['mailAddress'] == _TEST_EMAIL_ID

            # update user 
            # can't verify this for organizations created by microsoft account, since access level type is always earlyAdopter
            user_update_response = self.cmd('az devops user update -o json --detect false --user ' + _TEST_EMAIL_ID + ' --license-type express').get_output_in_json()
            assert user_update_response['user']['mailAddress'] == _TEST_EMAIL_ID

     
        finally:
            if user_id is not None:
                user_remove_response = self.cmd('az devops user remove --user ' + _TEST_EMAIL_ID + ' -o json --detect false -y')
                
                # check user list
                list_response = self.cmd('az devops user list -o json --detect false').get_output_in_json()
                assert list_response.get('members') is not None
                user_list_response = list_response['members']
                assert len(user_list_response) > 0
                user_id_found = False
                for item in user_list_response :
                    if item['user']['mailAddress'] == _TEST_EMAIL_ID:
                        user_id_found = True
                assert user_id_found == False
