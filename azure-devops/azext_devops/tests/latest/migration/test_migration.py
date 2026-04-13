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
            self.assertNotIn('includeInactiveMigrations', args[2])

    def test_list_migrations_include_inactive(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(include_inactive=True, organization=self._TEST_ORG, detect=False)

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertIn('includeInactiveMigrations=true', args[2])

    def test_create_migration_payload_defaults_validate_only_false(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertFalse(payload['validateOnly'])

    def test_create_migration_fails_without_target_repository(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('--target-repository must be specified', str(ctx.exception))

    def test_create_migration_fails_with_invalid_target_repository_url(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='ghe.example.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('must be a valid URL', str(ctx.exception))

    def test_create_migration_without_agent_pool(self):
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
            self.assertNotIn('agentPoolName', payload)

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
                validate_only=True,
                cutover_date='2030-12-31T11:59:00Z',
                agent_pool='MigrationPool',
                skip_validation=2147483647,
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['scheduledCutoverDate'], '2030-12-31T11:59:00Z')
            self.assertEqual(payload['agentPoolName'], 'MigrationPool')
            self.assertEqual(payload['skipValidation'], 2147483647)

    def test_create_migration_skip_validation_accepts_integer_string(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                skip_validation='2147483647',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['skipValidation'], 2147483647)

    def test_create_migration_skip_validation_accepts_policy_names(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                skip_validation='PullRequestDeltaSize, AgentPoolExists',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['skipValidation'], 6)

    def test_create_migration_skip_validation_accepts_all_name(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                skip_validation='All',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['skipValidation'], 2147483647)

    def test_create_migration_skip_validation_rejects_invalid_policy_name(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                skip_validation='BogusPolicy',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('unsupported policy name', str(ctx.exception))

    def test_create_migration_skip_validation_rejects_empty_policy_name(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                skip_validation='AgentPoolExists,,MaxRepoSize',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('contains an empty policy name', str(ctx.exception))

    def test_create_migration_empty_agent_pool_omitted(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='  ',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertNotIn('agentPoolName', payload)

    def test_create_migration_omits_none_skip_validation(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                skip_validation=None,
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertNotIn('skipValidation', payload)

    def test_create_migration_trims_agent_pool(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='  MigrationPool  ',
                skip_validation=42,
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['agentPoolName'], 'MigrationPool')
            self.assertEqual(payload['skipValidation'], 42)

    def test_create_migration_passes_target_repository_to_api(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['targetRepository'], 'https://example.com/OrgName/RepoName')

    def test_create_migration_validate_only_flag_sends_true(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                validate_only=True,
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])

    def test_create_migration_agent_pool_always_in_payload(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['agentPoolName'], 'MigrationPool')

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
                             validate_only=True, migration=True,
                             organization=self._TEST_ORG, detect=False)

    def test_resume_fails_when_active(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'active', 'stage': 'synchronization'}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('az devops migrations pause', str(ctx.exception))

    def test_resume_fails_when_active_via_statusRequested(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'statusRequested': 'Active', 'stage': 'validation'}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('statusRequested: Active', str(ctx.exception))

    def test_resume_sets_validate_only(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'status': 'suspended'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             validate_only=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], 'active')

    def test_resume_sets_migration(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'status': 'suspended'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             migration=True,
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
            mock_get.return_value = {'status': 'failed'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertNotIn('validateOnly', payload)
            self.assertEqual(payload['statusRequested'], 'active')

    def test_resume_migration_promotes_validate_only_succeeded(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {
                'status': 'succeeded',
                'validateOnly': True,
            }
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             migration=True,
                             organization=self._TEST_ORG, detect=False)

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'PUT')
            payload = args[3]
            self.assertFalse(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], 'active')

    def test_resume_migration_promote_uses_only_state_transition_fields(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {
                'status': 'succeeded',
                'validateOnly': True,
                'targetRepository': 'https://ghe.example.com/org/repo',
                'targetOwnerUserId': 'testuser',
                'agentPoolName': 'MyPool',
                'scheduledCutoverDate': '2030-06-01T00:00:00Z',
                'skipValidation': 2147483647,
            }
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             migration=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['validateOnly'], False)
            self.assertEqual(payload['statusRequested'], 'active')
            self.assertEqual(set(payload.keys()), {'validateOnly', 'statusRequested'})
            self.assertNotIn('agentPoolName', payload)
            self.assertNotIn('scheduledCutoverDate', payload)
            self.assertNotIn('targetRepository', payload)
            self.assertNotIn('targetOwnerUserId', payload)
            self.assertNotIn('skipValidation', payload)

    def test_resume_succeeded_without_migration_flag_errors(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'succeeded', 'validateOnly': True}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('--migration', str(ctx.exception))

    def test_resume_succeeded_full_migration_errors(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'succeeded', 'validateOnly': False}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('abandon', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()
