# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from knack.util import CLIError
try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azext_devops.dev.repos.policy import *
from azext_devops.vstsCompressed.policy.v4_0.models.models import PolicyConfiguration, PolicyTypeRef
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.vstsCompressed.policy.v4_0.policy_client import PolicyClient


class TestUuidMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorg.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'sample project'
    _TEST_PAT_TOKEN = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'
    _TEST_REPOSITORY_ID = 'b4da517c-0398-42dc-b2a8-0d3f240757f9'

    def setUp(self):
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_policies_patcher = patch('azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient.get_policy_configurations')
        self.get_policy_patcher = patch('azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient.get_policy_configuration')
        self.delete_policy_patcher = patch('azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient.delete_policy_configuration')
        self.create_policy_patcher = patch('azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient.create_policy_configuration')
        self.update_policy_patcher = patch('azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient.update_policy_configuration')

        self.mock_get_client = self.get_client.start()
        self.mock_get_policies = self.get_policies_patcher.start()
        self.mock_get_policy = self.get_policy_patcher.start()
        self.mock_delete_policy = self.delete_policy_patcher.start()
        self.mock_create_policy = self.create_policy_patcher.start()
        self.mock_update_policy = self.update_policy_patcher.start()

        self.mock_get_client.return_value = PolicyClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        clear_connection_cache()

    def tearDown(self):
        self.get_client.stop()
        self.get_policies_patcher.stop()
        self.get_policy_patcher.stop()
        self.delete_policy_patcher.stop()
        self.create_policy_patcher.stop()
        self.update_policy_patcher.stop()

    def test_list_policy(self):
        list_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_get_policies.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, scope=None)

    def test_list_policy_repo_scope(self):
        list_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off',
        repository_id='fake_repo_id')

        #assert
        self.mock_get_policies.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, scope='fake_repo_id')

    def test_list_policy_branch_scope(self):
        list_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off',
        repository_id='1d1dad71-f27c-4370-810d-838ec41efd41',
        branch='master')

        #assert
        self.mock_get_policies.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, scope='1d1dad71f27c4370810d838ec41efd41:refs/heads/master')

    def test_list_policy__only_branch_scope_error(self):
        try:
            list_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            detect='off',
            branch='master')
            self.fail('failure was expected')
        except CLIError as ex:
            #assert
            self.assertEqual(str(ex),
            '--repository-id is required with --branch')

    def test_get_policy(self):
        get_policy(policy_id = 121,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_get_policy.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, configuration_id=121)

    def test_delete_policy(self):
        delete_policy(policy_id = 121,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_delete_policy.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, configuration_id=121)

if __name__ == '__main__':
    unittest.main()