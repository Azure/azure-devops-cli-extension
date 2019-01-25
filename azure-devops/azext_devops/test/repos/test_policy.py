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
from azext_devops.dev.common.services import clear_connection_cache


class TestUuidMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://AzureDevOpsCliTest.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'sample project'
    _TEST_PAT_TOKEN = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'
    _TEST_REPOSITORY_ID = 'b4da517c-0398-42dc-b2a8-0d3f240757f9'

    def setUp(self):
        self.get_policies_patcher = patch('vsts.policy.v4_0.policy_client.PolicyClient.get_policy_configurations')
        self.get_policy_patcher = patch('vsts.policy.v4_0.policy_client.PolicyClient.get_policy_configuration')
        self.delete_policy = patch('vsts.policy.v4_0.policy_client.PolicyClient.delete_policy_configuration')

        self.mock_get_policies = self.get_policies_patcher.start()
        self.mock_get_policy = self.get_policy_patcher.start()
        self.mock_delete_policy = self.delete_policy.start()

        clear_connection_cache()

    def tearDown(self):
        self.mock_get_policies.stop()
        self.mock_get_policy.stop()
        self.mock_delete_policy.stop()

    def test_name_of_array(self):
        first_name = 'a'
        middle_name = 'b'
        last_name = 'c'
        desired_result = ['first_name','middle_name','last_name']
        nameOfArrayResult = nameOfArray([first_name,middle_name,last_name])
        self.assertEqual(nameOfArrayResult, desired_result)
        #the misplace here is intentional
        nameOfArrayResult = nameOfArray([ first_name ,    middle_name ,     last_name])
        self.assertEqual(nameOfArrayResult, desired_result)

    def test_list_policy(self):
        list_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_get_policies.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT)

    def test_get_policy(self):
        get_policy(id = 121,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_get_policy.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, configuration_id=121)

    def test_delete_policy(self):
        delete_policy(id = 121,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        #assert
        self.mock_delete_policy.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, configuration_id=121)

    def test_create_policy_argument_missing_message(self):
        try:
            create_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
            policy_type='ApproverCountPolicy',
            minimumApproverCount=2)
            self.fail('create should have thrown CLIError')
        except CLIError as ex:
            self.assertEqual(str(ex), '--minimumApproverCount --creatorVoteCounts --allowDownvotes --resetOnSourcePush are required for ApproverCountPolicy')

if __name__ == '__main__':
    unittest.main()