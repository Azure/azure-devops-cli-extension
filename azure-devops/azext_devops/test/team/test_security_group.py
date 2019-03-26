# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pdb
import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azext_devops.vstsCompressed.graph.v4_1.graph_client import (GraphClient)
# from azext_devops.dev.team.security_group import (list_groups,
#                                                   get_group,
#                                                   delete_group,
#                                                   update_group,
#                                                   add_membership,
#                                                   remove_membership,
#                                                   list_memberships)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
    
class TestSecurityGroupMethods(AuthenticatedTests):
    pass
    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_NAME = 'sample_project'
    _OFF = 'Off'
    _GROUP_MGMT_CLIENT_LOCATION = 'azext_devops.vstsCompressed.graph.v4_1.graph_client.GraphClient.'
    _GROUP_ID = 'adda517c-0398-42dc-b2a8-0d3f240757f9'

    def setUp(self):
        self.authentication_setUp()
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_patch_op_patcher = patch('azext_devops.dev.team.security_group._create_patch_operation')
        self.list_groups_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'list_groups')
        self.get_group_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'get_group')
        self.get_descriptor_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'get_descriptor')
        
        self.mock_get_client = self.get_client.start()
        self.mock_list_groups = self.list_groups_patcher.start()
        self.mock_get_group = self.get_group_patcher.start()
        self.mock_get_descriptor= self.get_descriptor_patcher.start()
        
        #set return values
        self.mock_get_client.return_value = GraphClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_groups(self):
        response = list_groups(organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_groups.assert_called_once()

    def test_show_group(self):
        response = get_group(id=self._GROUP_ID, organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_get_group.assert_called_once()
        self.mock_get_descriptor.assert_called_once()
    
    def test_delete_group(self):
        response = delete_group(id=self._GROUP_ID, organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_get_group.assert_called_once()
        self.mock_get_descriptor.assert_called_once()