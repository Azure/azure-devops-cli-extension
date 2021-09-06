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


class PermissionTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_devops_security_permission_tests(self):
        random_project_name = self.create_random_name(prefix='Permission_',length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            #Permanently delete work items permission
            permission_bit = 32768
            #add user
            user_add_response = self.cmd('az devops user add -o json --detect false --email-id ' + _TEST_EMAIL_ID + ' --license-type stakeholder').get_output_in_json()
            user_id = user_add_response['id']
            assert user_add_response['user']['mailAddress'] == _TEST_EMAIL_ID

            #list namespace
            list_namespace = self.cmd('az devops security permission namespace list -o json --detect false').get_output_in_json()

            #Further tests are on Project namespace : 52d39943-cb85-4d7f-8fa8-c6baac873819
            project_namespace_id = '52d39943-cb85-4d7f-8fa8-c6baac873819'
            #show namespace
            show_namespace = self.cmd('az devops security permission namespace show --id '+ project_namespace_id +' -o json --detect false').get_output_in_json()
            assert show_namespace[0]['namespaceId'] == project_namespace_id

            # permission list tokens
            list_permission = self.cmd('az devops security permission list --id '+ project_namespace_id + ' --subject ' + _TEST_EMAIL_ID +' -o json --detect false').get_output_in_json()
            acl_entries = list_permission[0]['acesDictionary'].keys()
            email_id_found = False
            for entry in acl_entries:
                if _TEST_EMAIL_ID in entry:
                    email_id_found = True
                    ace_key = entry
            assert email_id_found == True

            project_token = "$PROJECT:vstfs:///Classification/TeamProject/"+created_project_id

            show_permission = self.cmd('az devops security permission show --id '+ project_namespace_id + ' --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert show_permission[0]['token'] == project_token
            assert show_permission[0]['includeExtendedInfo'] == True
            original_resolved_permissions = show_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert original_resolved_permissions is not None
            for entry in original_resolved_permissions:
                if entry['bit'] ==  permission_bit:
                    curr_allow_value = entry['effectivePermission']
            assert curr_allow_value != 'Allow'

            update_permission = self.cmd('az devops security permission update --id '+ project_namespace_id + ' --allow-bit 65536 --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert update_permission[0]['token'] == project_token
            resolved_permissions = update_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert resolved_permissions is not None
            for entry in resolved_permissions:
                if entry['bit'] ==  permission_bit: 
                    new_allow_value = entry['effectivePermission']
                    assert new_allow_value == 'Allow'
           
            update_permission = self.cmd('az devops security permission update --id '+ project_namespace_id + ' --deny-bit 65536 --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert update_permission[0]['token'] == project_token
            resolved_permissions = update_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert resolved_permissions is not None
            for entry in resolved_permissions:
                if entry['bit'] ==  permission_bit: 
                    new_allow_value = entry['effectivePermission']
                    assert new_allow_value == 'Deny'

            reset_permission = self.cmd('az devops security permission reset --id '+ project_namespace_id + ' --permission-bit 65536 --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert reset_permission[0]['token'] == project_token
            resolved_permissions = reset_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert resolved_permissions is not None
            for entry in resolved_permissions:
                if entry['bit'] ==  permission_bit: 
                    new_allow_value = entry['effectivePermission']
                    assert new_allow_value == curr_allow_value
            
            update_permission = self.cmd('az devops security permission update --id '+ project_namespace_id + ' --deny-bit 65536 --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert update_permission[0]['token'] == project_token
            resolved_permissions = update_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert resolved_permissions is not None
            for entry in resolved_permissions:
                if entry['bit'] ==  32768: 
                    new_allow_value = entry['effectivePermission']
                    assert new_allow_value == 'Deny'
            assert resolved_permissions != original_resolved_permissions

            reset_all_permission = self.cmd('az devops security permission reset-all --id '+ project_namespace_id + ' --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -y -o json --detect false').get_output_in_json()
            assert reset_all_permission == True

            show_permission = self.cmd('az devops security permission show --id '+ project_namespace_id + ' --subject ' + _TEST_EMAIL_ID + ' --token "' + project_token +'" -o json --detect false').get_output_in_json()
            assert show_permission[0]['token'] == project_token
            assert show_permission[0]['includeExtendedInfo'] == True
            resolved_permissions = show_permission[0]['acesDictionary'][ace_key]['resolvedPermissions']
            assert resolved_permissions is not None
            for entry in resolved_permissions:
                if entry['bit'] ==  32768:
                    new_allow_value = entry['effectivePermission']
            assert curr_allow_value == new_allow_value
            assert resolved_permissions == original_resolved_permissions
            
        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)