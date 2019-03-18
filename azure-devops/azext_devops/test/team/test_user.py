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

from azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client import (MemberEntitlementManagementClient)
from azext_devops.dev.team.user import (get_user_entitlements,
                                        get_user_entitlement,
                                        add_user_entitlement,
                                        delete_user_entitlement,
                                        update_user_entitlement)

from azext_devops.dev.common.services import clear_connection_cache

    
class TestUserMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_NAME = 'sample_project'
    _TOP_VALUE = 10
    _SKIP_VALUE = 2
    _OFF = 'Off'
    _TEST_USER_ID = 'adda517c-0398-42dc-b2a8-0d3f240757f9'
    _USER_MGMT_CLIENT_LOCATION = 'azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client.MemberEntitlementManagementClient.'

    def setUp(self):
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')
        self.get_patch_op_patcher = patch('azext_devops.dev.team.user._create_patch_operation')
        self.list_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'get_user_entitlements')
        self.get_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'get_user_entitlement')
        self.add_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'update_user_entitlements')
        self.remove_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'delete_user_entitlement')
        self.update_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'update_user_entitlement')
        
        self.mock_get_client = self.get_client.start()
        self.mock_get_users = self.list_user_patcher.start()
        self.mock_add_user = self.add_user_patcher.start()
        self.mock_get_user = self.get_user_patcher.start()
        self.mock_remove_user = self.remove_user_patcher.start()
        self.mock_update_user = self.update_user_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()
        
        #set return values
        self.mock_get_client.return_value = MemberEntitlementManagementClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_user(self):
        get_user_entitlements(top=self._TOP_VALUE, skip=self._SKIP_VALUE, 
                              organization=self._TEST_DEVOPS_ORGANIZATION, detect=self._OFF)            
        #assert
        self.mock_get_users.assert_called_once()
        list_user_param = self.mock_get_users.call_args_list[0][1]
        self.assertEqual(10,list_user_param['top'])
        self.assertEqual(2, list_user_param['skip'])

    def test_show_user(self):
        get_user_entitlement(user=self._TEST_USER_ID, organization=self._TEST_DEVOPS_ORGANIZATION, detect=self._OFF)
        #assert
        self.mock_get_user.assert_called_once_with(user_id = 'adda517c-0398-42dc-b2a8-0d3f240757f9')

    def test_add_user(self):
        add_user_entitlement(user='someuser@xyz.com', license_type='stakeholder', 
                             organization=self._TEST_DEVOPS_ORGANIZATION, detect=self._OFF)
        #assert
        self.mock_add_user.assert_called_once()
        add_user_param = self.mock_add_user.call_args_list[0][1]
        add_user_param_document = add_user_param['document'][0].value
        self.assertEqual(False, add_user_param['do_not_send_invite_for_new_users'])
        self.assertEqual('stakeholder', add_user_param_document['accessLevel'].account_license_type)
        self.assertEqual('user', add_user_param_document['user'].subject_kind)
        self.assertEqual('someuser@xyz.com', add_user_param_document['user'].principal_name)
    
    def test_remove_user(self):
        delete_user_entitlement(user=self._TEST_USER_ID, organization= self._TEST_DEVOPS_ORGANIZATION, detect=self._OFF)
        #assert
        self.mock_remove_user.assert_called_once()

    def test_update_user(self):
        update_user_entitlement(user=self._TEST_USER_ID, license_type='express', 
                                organization=self._TEST_DEVOPS_ORGANIZATION, detect=self._OFF)
        #assert
        self.mock_update_user.assert_called_once()
        update_user_param = self.mock_update_user.call_args_list[0][1]
        update_user_param_document = update_user_param['document'][0].value
        print(update_user_param_document)
        self.assertEqual('express', update_user_param_document['accountLicenseType'])
        self.assertEqual('adda517c-0398-42dc-b2a8-0d3f240757f9', update_user_param['user_id'])
    