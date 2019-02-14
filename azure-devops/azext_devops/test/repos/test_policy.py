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
            minimum_approver_count=2,
            organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            detect='off')
            self.fail('create should have thrown CLIError')
        except CLIError as ex:
            #assert
            self.assertEqual(str(ex),
            '--minimum-approver-count, --creator-vote-counts, --allow-downvotes, --reset-on-source-push are required for ApproverCountPolicy')

    def test_create_policy_policy_type_and_configuration_missing(self):
        try:
            create_policy(organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            detect='off')
            self.fail('create should have thrown CLIError')
        except CLIError as ex:
            #assert
            self.assertEqual(str(ex),
            'Either --policy-configuration or --policy-type must be passed')

    def test_create_policy_scope(self):
        create_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
        policy_type='ApproverCountPolicy',
        minimum_approver_count=2, creator_vote_counts= True, allow_downvotes= False, reset_on_source_push= True,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        self.mock_create_policy.assert_called_once()
        create_policy_object = self.mock_create_policy.call_args_list[0][1]
        self.assertEqual(self._TEST_DEVOPS_PROJECT, create_policy_object['project'], str(create_policy_object))
        scope = create_policy_object['configuration'].settings['scope'][0]  # 0 because we set only only scope from CLI
        self.assertEqual(scope['repositoryId'], self._TEST_REPOSITORY_ID)
        self.assertEqual(scope['refName'], 'master')
        self.assertEqual(scope['matchKind'], 'exact')

    def test_create_policy_scope_repo_only(self):
        create_policy(repository_id=self._TEST_REPOSITORY_ID,
        policy_type='FileSizePolicy',
        maximum_git_blob_size_in_bytes=2, use_uncompressed_size= True,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        self.mock_create_policy.assert_called_once()
        create_policy_object = self.mock_create_policy.call_args_list[0][1]
        self.assertEqual(self._TEST_DEVOPS_PROJECT, create_policy_object['project'], str(create_policy_object))
        scope = create_policy_object['configuration'].settings['scope'][0]  # 0 because we set only only scope from CLI
        self.assertEqual(scope['repositoryId'], self._TEST_REPOSITORY_ID)
        self.assertEqual('refName' in scope, False)
        self.assertEqual('matchKind' in scope, False)

    def test_create_policy_scope_repo_only_error(self):
        try:
            create_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
            policy_type='FileSizePolicy',
            maximum_git_blob_size_in_bytes=2, use_uncompressed_size= True,
            organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            detect='off')
            self.fail('create should have thrown CLIError')
        except CLIError as ex:
            self.assertEqual(str(ex),
            'You can only use repository for this policy type not branch')

    def test_create_policy_setting_creation(self):
        create_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
        policy_type='ApproverCountPolicy',
        minimum_approver_count=2, creator_vote_counts= True, allow_downvotes= False, reset_on_source_push= True,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        self.mock_create_policy.assert_called_once()
        create_policy_object = self.mock_create_policy.call_args_list[0][1]
        self.assertEqual(self._TEST_DEVOPS_PROJECT, create_policy_object['project'], str(create_policy_object))
        settings = create_policy_object['configuration'].settings  # 0 because we set only only scope from CLI
        self.assertEqual(settings['minimumApproverCount'], 2)
        self.assertEqual(settings['creatorVoteCounts'], True)
        self.assertEqual(settings['allowDownvotes'], False)
        self.assertEqual(settings['resetOnSourcePush'], True)

    def test_create_policy_id_assignment(self):
        create_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
        policy_type='ApproverCountPolicy',
        minimum_approver_count=2, creator_vote_counts= True, allow_downvotes= False, reset_on_source_push= True,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        self.mock_create_policy.assert_called_once()
        create_policy_object = self.mock_create_policy.call_args_list[0][1]
        self.assertEqual(self._TEST_DEVOPS_PROJECT, create_policy_object['project'], str(create_policy_object))
        policy_type_id = create_policy_object['configuration'].type['id']  # 0 because we set only only scope from CLI
        self.assertEqual(policy_type_id, 'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd')

    def test_update_policy(self):
        update_policy(repository_id=self._TEST_REPOSITORY_ID, branch='master',
        policy_id = 121,
        policy_type='ApproverCountPolicy',
        minimum_approver_count=2, creator_vote_counts= True, allow_downvotes= False, reset_on_source_push= True,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = self._TEST_DEVOPS_PROJECT,
        detect='off')

        self.mock_update_policy.assert_called_once()
        update_policy_object = self.mock_update_policy.call_args_list[0][1]
        self.assertEqual(update_policy_object['configuration_id'], 121)        

if __name__ == '__main__':
    unittest.main()