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

from knack.util import CLIError

from azext_devops.dev.migration.migration import (list_migrations,
                                                  create_migration,
                                                  cancel_cutover,
                                                  resume_migration)


class TestMigrationCommands(unittest.TestCase):

    _TEST_ORG = 'https://elm.contoso.com/elmo1'

    def test_list_migrations_calls_get(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(organization=self._TEST_ORG, detect=False)

            mock_resolve.assert_called_once_with(detect=False, organization=self._TEST_ORG)
            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertTrue(args[2].startswith(self._TEST_ORG.rstrip('/')))
            self.assertIn('/_apis/elm/migrations', args[2])

    def test_create_migration_payload_defaults_validate_only_true(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])

    def test_create_migration_rejects_validate_only_false(self):
        with self.assertRaises(CLIError):
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                validate_only=False,
                organization=self._TEST_ORG,
                detect=False
            )

    def test_create_migration_payload_includes_optional_fields(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                scheduled_cutover_date='2030-12-31T11:59:00Z',
                agent_pool_name='MigrationPool',
                skip_validation='ActivePullRequestCount,PullRequestDeltaSize',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['scheduledCutoverDate'], '2030-12-31T11:59:00Z')
            self.assertEqual(payload['agentPoolName'], 'MigrationPool')
            self.assertEqual(payload['skipValidation'], 'ActivePullRequestCount,PullRequestDeltaSize')

    def test_create_migration_omits_empty_optional_fields(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool_name='  ',
                skip_validation='   ',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertNotIn('agentPoolName', payload)
            self.assertNotIn('skipValidation', payload)

    def test_create_migration_trims_optional_fields(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool_name='  MigrationPool  ',
                skip_validation=' ActivePullRequestCount, PullRequestDeltaSize ',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['agentPoolName'], 'MigrationPool')
            self.assertEqual(payload['skipValidation'], 'ActivePullRequestCount, PullRequestDeltaSize')

    def test_create_migration_rejects_invalid_target_repository(self):
        with self.assertRaises(CLIError):
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='microsoft/gcox-test-1',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

    def test_create_migration_accepts_ghe_url(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

    def test_create_migration_accepts_github_url(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://github.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

    def test_create_migration_rejects_non_ghe_host(self):
        with self.assertRaises(CLIError):
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

    def test_cancel_cutover_sets_null(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            cancel_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertIsNone(payload['scheduledCutoverDate'])

    def test_resume_rejects_both_flags(self):
        with self.assertRaises(CLIError):
            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             validate_only=True, migrate=True,
                             organization=self._TEST_ORG, detect=False)

    def test_resume_fails_when_active(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'state': 'active', 'stage': 'synchronizing'}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError):
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)

    def test_resume_sets_validate_only(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'state': 'succeeded'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             validate_only=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], 'active')

    def test_resume_sets_migrate(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'state': 'suspended'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             migrate=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertFalse(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], 'active')

    def test_resume_without_flags_preserves_mode(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'state': 'failed'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertNotIn('validateOnly', payload)
            self.assertEqual(payload['statusRequested'], 'active')


if __name__ == '__main__':
    unittest.main()
