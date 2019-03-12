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

from azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client import MemberEntitlementManagementClient
from azext_devops.dev.team.user import (get_user_entitlements,
                                        get_user_entitlement)

from azext_devops.dev.common.services import clear_connection_cache

    
class TestUserMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_NAME = 'sample_project'
    _TEST_TEAM_NAME = 'sample_team'
    _TEST_TEAM_DESCRIPTION = 'sample_team_description'
    _TOP_VALUE = 10
    _SKIP_VALUE = 2
    _OFF = 'Off'
    _USER_MGMT_CLIENT_LOCATION = 'azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client.MemberEntitlementManagementClient.'

    def setUp(self):
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')
        self.list_user_patcher = patch(self._USER_MGMT_CLIENT_LOCATION + 'get_user_entitlements')
        
        self.mock_get_client = self.get_client.start()
        self.mock_get_users = self.list_user_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()
        
        #set return values
        self.mock_get_client.return_value = MemberEntitlementManagementClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_user(self):
        get_user_entitlements(self._TEST_DEVOPS_ORGANIZATION, 'off')
                
        #assert
        self.mock_get_users.assert_called_once()
