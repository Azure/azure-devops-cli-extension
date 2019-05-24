# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import json
import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azext_devops.devops_sdk.v5_0.security.security_client import (SecurityClient)
from azext_devops.devops_sdk.v5_0.security.models import (AccessControlList,
                                                          AccessControlEntry,
                                                          AceExtendedInformation,
                                                          ActionDefinition,
                                                          SecurityNamespaceDescription)
from azext_devops.dev.team.security_permission import (list_namespaces,
                                                  show_namespace,
                                                  list_tokens,
                                                  show_permissions,
                                                  reset_all_permissions,
                                                  reset_permissions,
                                                  update_permissions,
                                                  _resolve_bits)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.test.utils.helper import get_client_mock_helper

class TestSecurityPermissionsMethods(AuthenticatedTests):
    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_DESCRIPTOR = 'scp.someRandomDescriptorForProject'
    _OFF = 'Off'
    _SECURITY_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.security.security_client.SecurityClient.'
    _TEST_GROUP_DESCRIPTOR = 'vssgp.someRandomDescriptorForGroup'
    _TEST_GROUP_NAME = 'New test security group'
    _TEST_SECURITY_TOKEN = 'some_security_token'
    _TEST_USER_DESCRIPTOR = 'aad.someRandomDescriptorForUser'
    _TEST_IDENTITY_DESCRIPTOR = 'Microsoft.Identity.aaaaaaaa'
    _TEST_SECURITY_NAMESPACE_ID = 'bf7bfa03-b2b7-47db-xxxx-fa2e002xxxx'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        
        self.list_namespaces_patcher = patch(self._SECURITY_CLIENT_LOCATION + 'query_security_namespaces')
        self.list_acl_patcher = patch(self._SECURITY_CLIENT_LOCATION + 'query_access_control_lists')
        self.set_ace_patcher = patch(self._SECURITY_CLIENT_LOCATION + 'set_access_control_entries')
        self.get_identity_descriptor_patcher = patch('azext_devops.dev.team.security_permission._resolve_subject_as_identity_descriptor')
        self.resolve_bits_patcher = patch('azext_devops.dev.team.security_permission._resolve_bits')
        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client')

        self.mock_get_client = self.get_client.start()
        self.mock_get_identity_descriptor = self.get_identity_descriptor_patcher.start()
        self.mock_list_namespaces = self.list_namespaces_patcher.start()
        self.mock_list_acl = self.list_acl_patcher.start()
        self.mock_resolve_bits = self.resolve_bits_patcher.start()
        self.mock_set_ace = self.set_ace_patcher.start()
        #set return values
        self.mock_get_client.return_value = SecurityClient(base_url=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_identity_descriptor.return_value = self._TEST_IDENTITY_DESCRIPTOR
        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_namespaces(self):
        response = list_namespaces(False,organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_namespaces.assert_called_once()
        list_namespaces_param = self.mock_list_namespaces.call_args_list[0][1]
        self.assertEqual(False, list_namespaces_param['local_only'])
    
    def test_show_namespace(self):
        response = show_namespace(namespace_id=self._TEST_SECURITY_NAMESPACE_ID,organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_namespaces.assert_called_once()
        show_namespace_param = self.mock_list_namespaces.call_args_list[0][1]
        self.assertEqual(self._TEST_SECURITY_NAMESPACE_ID, show_namespace_param['security_namespace_id'])
    
    def test_list_tokens(self):
        response = list_tokens(namespace_id=self._TEST_SECURITY_NAMESPACE_ID,
                                subject = self._TEST_GROUP_DESCRIPTOR, 
                                recurse=False,organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_acl.assert_called_once()
        list_tokens_param = self.mock_list_acl.call_args_list[0][1]
        self.assertEqual(self._TEST_SECURITY_NAMESPACE_ID, list_tokens_param['security_namespace_id'])
        self.assertEqual(False, list_tokens_param['recurse'])
        self.assertEqual(True, list_tokens_param['include_extended_info'])
        self.assertEqual(self._TEST_IDENTITY_DESCRIPTOR, list_tokens_param['descriptors'])
        
    def test_show_permissions(self):
        self.mock_resolve_bits.return_value = self._get_resolve_bits_response()
        response = show_permissions(namespace_id=self._TEST_SECURITY_NAMESPACE_ID,
                                    subject = self._TEST_GROUP_DESCRIPTOR, 
                                    token= self._TEST_SECURITY_TOKEN,
                                    organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_acl.assert_called_once()
        show_permissions_param = self.mock_list_acl.call_args_list[0][1]
        self.assertEqual(self._TEST_SECURITY_NAMESPACE_ID, show_permissions_param['security_namespace_id'])
        self.assertEqual(False, show_permissions_param['recurse'])
        self.assertEqual(True, show_permissions_param['include_extended_info'])
        self.assertEqual(self._TEST_IDENTITY_DESCRIPTOR, show_permissions_param['descriptors'])

    def test_update_permissions(self):
        self.mock_resolve_bits.return_value = self._get_resolve_bits_response()
        response = update_permissions(namespace_id=self._TEST_SECURITY_NAMESPACE_ID,
                                    allow_bit = 1,
                                    subject = self._TEST_GROUP_DESCRIPTOR, 
                                    token= self._TEST_SECURITY_TOKEN,
                                    organization=self._TEST_DEVOPS_ORGANIZATION,detect=self._OFF)
        #assert
        self.mock_list_acl.assert_called_once()
        show_permissions_param = self.mock_list_acl.call_args_list[0][1]
        update_permissions_param = self.mock_set_ace.call_args_list[0][1]
        self.assertEqual(self._TEST_SECURITY_NAMESPACE_ID, show_permissions_param['security_namespace_id'])
        self.assertEqual(False, show_permissions_param['recurse'])
        self.assertEqual(True, show_permissions_param['include_extended_info'])
        self.assertEqual(self._TEST_IDENTITY_DESCRIPTOR, show_permissions_param['descriptors'])

    def _get_resolve_bits_response(self,changed_bits=0):
        # api response
         
        namespace_details = self._form_namespace_details_response()
        acl_response = self._form_permission_api_response()
        resolved_bits = _resolve_bits(acl_response, namespace_details,changed_bits=changed_bits)
        return resolved_bits
    
    def _form_namespace_details_response(self):
        #namespace list reponse
        namespace_details = []
        namespace_details_entry = SecurityNamespaceDescription()
        dummy_actions = []
        # GENERIC_READ
        readAction = ActionDefinition()
        readAction.bit = 1
        readAction.displayName = 'View Resource'
        readAction.name = 'GENERIC_READ'
        readAction.namespace_id = self._TEST_SECURITY_NAMESPACE_ID
        dummy_actions.append(readAction)
        # GENERIC_WRITE
        writeAction = ActionDefinition()
        writeAction.bit = 2
        writeAction.displayName = 'Create Resource'
        writeAction.name = 'GENERIC_WRITE'
        writeAction.namespace_id = self._TEST_SECURITY_NAMESPACE_ID
        dummy_actions.append(writeAction)
        # GENERIC_WRITE
        updateAction = ActionDefinition()
        updateAction.bit = 4
        updateAction.displayName = 'Update Resource'
        updateAction.name = 'GENERIC_UPDATE'
        updateAction.namespace_id = self._TEST_SECURITY_NAMESPACE_ID
        dummy_actions.append(updateAction)
        namespace_details_entry.actions = dummy_actions
        namespace_details.append(namespace_details_entry)
        return namespace_details

    def _form_permission_api_response(self,allow_bit=0, deny_bit=0, effective_allow=0, effective_deny=0):
        acl_response = []
        acl_entry = AccessControlList()
        ace_dictionary = {}
        ace_entry = AccessControlEntry()
        ace_entry.allow = allow_bit
        ace_entry.deny = deny_bit
        ace_entry.descriptor = self._TEST_IDENTITY_DESCRIPTOR
        extended_info = AceExtendedInformation()
        extended_info.effective_allow = effective_allow
        extended_info.effective_deny = effective_deny
        ace_entry.extended_info = extended_info
        ace_dictionary[self._TEST_IDENTITY_DESCRIPTOR] = ace_entry
        acl_entry.aces_dictionary = ace_dictionary
        acl_entry.include_extended_info = True
        acl_entry.inherit_permissions = False
        acl_entry.token = self._TEST_SECURITY_TOKEN
        acl_response.append(acl_entry)
        return acl_response

