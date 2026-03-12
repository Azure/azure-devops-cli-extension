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
                                                  set_validate_only,
                                                  migrate_migration)


class TestMigrationCommands(unittest.TestCase):

    _TEST_ORG = 'https://codedev.ms/elmo1'

    def test_list_migrations_calls_get(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(organization=self._TEST_ORG, detect=False)

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertIn('/_apis/elm/migrations', args[2])

    def test_create_migration_payload_defaults_validate_only_true(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://microsoft.ghe.com/1ES/Gardener',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])

    def test_create_migration_payload_includes_optional_fields(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://microsoft.ghe.com/1ES/Gardener',
                target_owner_user_id='GeoffCoxMSFT',
                validate_only=False,
                scheduled_cutover_date='2030-12-31T11:59:00Z',
                agent_pool_name='MigrationPool',
                skip_validation='ActivePullRequestCount,PullRequestDeltaSize',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertFalse(payload['validateOnly'])
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
                target_repository='https://microsoft.ghe.com/1ES/Gardener',
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
                target_repository='https://microsoft.ghe.com/1ES/Gardener',
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
                target_repository='https://microsoft.ghe.com/1ES/Gardener',
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

    def test_set_validate_only_requires_on_or_off(self):
        with self.assertRaises(CLIError):
            set_validate_only(repository_id='00000000-0000-0000-0000-000000000000',
                              organization=self._TEST_ORG, detect=False)

    def test_migrate_sets_active(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            migrate_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertFalse(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], 'active')


if __name__ == '__main__':
    unittest.main()
