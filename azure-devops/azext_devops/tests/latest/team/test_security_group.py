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

from azext_devops.devops_sdk.v5_0.graph.graph_client import (GraphClient)
from azext_devops.dev.team.security_group import (list_groups,
                                                  get_group,
                                                  create_group,
                                                  delete_group,
                                                  update_group,
                                                  add_membership,
                                                  remove_membership,
                                                  list_memberships)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.tests.utils.helper import get_client_mock_helper

class TestSecurityGroupMethods(AuthenticatedTests):
    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_DESCRIPTOR = 'scp.someRandomDescriptorForProject'
    _GROUP_MGMT_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.graph.graph_client.GraphClient.'
    _TEST_GROUP_DESCRIPTOR = 'vssgp.someRandomDescriptorForGroup'
    _TEST_GROUP_NAME = 'New test security group'
    _TEST_GROUP_DESCRIPTION = 'Some test description'
    _TEST_USER_DESCRIPTOR = 'aad.someRandomDescriptorForUser'
    
    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_patch_op_patcher = patch('azext_devops.dev.team.security_group._create_patch_operation')
        self.list_groups_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'list_groups')
        self.get_group_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'get_group')
        self.create_group_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'create_group')
        self.get_descriptor_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'get_descriptor')
        self.delete_group_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'delete_group')
        self.update_group_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'update_group')
        self.list_memberships_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'list_memberships')
        self.lookup_subjects_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'lookup_subjects')
        self.get_project_patcher = patch('azext_devops.devops_sdk.v5_0.core.core_client.CoreClient.get_project')
        self.add_membership_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'add_membership')
        self.remove_membership_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'remove_membership')
        self.check_membership_patcher = patch(self._GROUP_MGMT_CLIENT_LOCATION + 'check_membership_existence')

        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)

        self.mock_get_client = self.get_client.start()
        self.mock_list_groups = self.list_groups_patcher.start()
        self.mock_get_group = self.get_group_patcher.start()
        self.mock_get_descriptor= self.get_descriptor_patcher.start()
        self.mock_create_group = self.create_group_patcher.start()
        self.mock_delete_group = self.delete_group_patcher.start()
        self.mock_update_group = self.update_group_patcher.start()
        self.mock_list_memberships = self.list_memberships_patcher.start()
        self.mock_add_membership = self.add_membership_patcher.start()
        self.mock_remove_membership = self.remove_membership_patcher.start()
        self.mock_lookup_subjects = self.lookup_subjects_patcher.start()
        self.mock_get_project = self.get_project_patcher.start()
        self.mock_check_membership = self.check_membership_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_groups_with_org_filter(self):
        response = list_groups(scope='organization', organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_list_groups.assert_called_once()

    def test_list_groups(self):
        self.mock_get_descriptor.return_value = self._TEST_PROJECT_DESCRIPTOR
        response = list_groups(project=self._TEST_PROJECT_DESCRIPTOR,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_list_groups.assert_called_once()
        list_groups_param = self.mock_list_groups.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_DESCRIPTOR, list_groups_param['scope_descriptor'], str(list_groups_param))

    def test_show_group(self):
        response = get_group(id=self._TEST_GROUP_DESCRIPTOR, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_group.assert_called_once()
        get_group_param = self.mock_get_group.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_DESCRIPTOR, get_group_param['group_descriptor'], str(get_group_param))


    def test_delete_group(self):
        response = delete_group(id=self._TEST_GROUP_DESCRIPTOR, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_delete_group.assert_called_once()

    def test_update_group(self):
        response = update_group(id=self._TEST_GROUP_DESCRIPTOR, description='Updated description for the test group', organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_update_group.assert_called_once()

    def test_create_group_in_org(self):
        response = create_group(scope='organization', name=self._TEST_GROUP_NAME, description= self._TEST_GROUP_DESCRIPTION, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_group.assert_called_once()
        create_group_param = self.mock_create_group.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_NAME, create_group_param['creation_context'].display_name, str(create_group_param))
        self.assertEqual(self._TEST_GROUP_DESCRIPTION, create_group_param['creation_context'].description, str(create_group_param))

    def test_create_group(self):
        self.mock_get_descriptor.return_value = self._TEST_PROJECT_DESCRIPTOR
        response = create_group(name=self._TEST_GROUP_NAME, description= self._TEST_GROUP_DESCRIPTION, project=self._TEST_PROJECT_DESCRIPTOR, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_group.assert_called_once()
        create_group_param = self.mock_create_group.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_NAME, create_group_param['creation_context'].display_name, str(create_group_param))
        self.assertEqual(self._TEST_GROUP_DESCRIPTION, create_group_param['creation_context'].description, str(create_group_param))
        self.assertEqual(self._TEST_PROJECT_DESCRIPTOR, create_group_param['scope_descriptor'], str(create_group_param))

    def test_list_memberships(self):
        response = list_memberships(id=self._TEST_GROUP_DESCRIPTOR,  organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_list_memberships.assert_called_once()
        self.mock_lookup_subjects.assert_called_once()
        list_memberships_param = self.mock_list_memberships.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_DESCRIPTOR, list_memberships_param['subject_descriptor'], str(list_memberships_param))
        self.assertEqual('down', list_memberships_param['direction'], str(list_memberships_param))

    def test_list_memberships_member_of(self):
        response = list_memberships(id=self._TEST_GROUP_DESCRIPTOR, relationship='memberof', organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_list_memberships.assert_called_once()
        self.mock_lookup_subjects.assert_called_once()
        list_memberships_param = self.mock_list_memberships.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_DESCRIPTOR, list_memberships_param['subject_descriptor'], str(list_memberships_param))
        self.assertEqual('up', list_memberships_param['direction'], str(list_memberships_param))

    def test_add_membership(self):
        response = add_membership(group_id=self._TEST_GROUP_DESCRIPTOR, member_id=self._TEST_USER_DESCRIPTOR, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_add_membership.assert_called_once()
        self.mock_lookup_subjects.assert_called_once()
        add_membership_param = self.mock_add_membership.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_DESCRIPTOR, add_membership_param['container_descriptor'], str(add_membership_param))
        self.assertEqual(self._TEST_USER_DESCRIPTOR, add_membership_param['subject_descriptor'], str(add_membership_param))

    
    def test_remove_membership(self):
        response = remove_membership(group_id=self._TEST_GROUP_DESCRIPTOR, member_id=self._TEST_USER_DESCRIPTOR, organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_remove_membership.assert_called_once()
        remove_membership_param = self.mock_remove_membership.call_args_list[0][1]
        self.assertEqual(self._TEST_GROUP_DESCRIPTOR, remove_membership_param['container_descriptor'], str(remove_membership_param))
        self.assertEqual(self._TEST_USER_DESCRIPTOR, remove_membership_param['subject_descriptor'], str(remove_membership_param))
