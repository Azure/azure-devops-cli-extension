# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import os
from urllib.error import HTTPError

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from knack.util import CLIError
import azext_devops.dev.migration.migration as migration_module

from azext_devops.dev.migration.migration import (list_migrations,
                                                  create_migration,
                                                  cancel_cutover,
                                                  resume_migration)


class TestMigrationCommands(unittest.TestCase):

    _TEST_ORG = 'https://elm.contoso.com/elmo1'

    def setUp(self):
        self._original_env_token = os.environ.get('ELM_GITHUB_TOKEN')
        os.environ['ELM_GITHUB_TOKEN'] = 'env-token-for-tests'

    def tearDown(self):
        if self._original_env_token is None:
            os.environ.pop('ELM_GITHUB_TOKEN', None)
        else:
            os.environ['ELM_GITHUB_TOKEN'] = self._original_env_token

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

    def test_list_migrations_with_project_filter(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(project='MyProject', organization=self._TEST_ORG, detect=False)

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertIn('project=MyProject', args[2])

    def test_list_migrations_with_project_filter_url_encoded(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(project='My Project', organization=self._TEST_ORG, detect=False)

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertIn('project=My+Project', args[2])

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
            self.assertEqual(payload['gitHubUserToken'], 'env-token-for-tests')

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
        self.assertIn('https://host/org/repo', str(ctx.exception))

    def test_create_migration_fails_with_non_https_target_repository(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='http://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('https://host/org/repo', str(ctx.exception))

    def test_create_migration_fails_when_target_repository_path_is_not_org_repo(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName',
                target_owner_user_id='GeoffCoxMSFT',
                agent_pool='MigrationPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('https://host/org/repo', str(ctx.exception))

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

    def test_create_migration_uses_parameter_token_over_environment(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                github_token='param-token',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['gitHubUserToken'], 'param-token')

    def test_create_migration_uses_device_flow_when_no_token_provided(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration._run_device_flow') as mock_run_device_flow:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.side_effect = [
                {'clientId': 'client-id-123', 'enterpriseUrl': 'https://example.ghe.com'},
                {}
            ]
            mock_run_device_flow.return_value = 'device-flow-token'
            os.environ.pop('ELM_GITHUB_TOKEN', None)

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='GeoffCoxMSFT',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['gitHubUserToken'], 'device-flow-token')
            mock_run_device_flow.assert_called_once_with('client-id-123', 'https://example.ghe.com')

    def test_create_migration_conflict_returns_clear_message(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.side_effect = CLIError('Request failed with status 409. TF400898: An Internal Error Occurred.')

            with self.assertRaises(CLIError) as ctx:
                create_migration(
                    repository_id='912d0fd3-9c17-4b35-b67b-91848ce4d6bb',
                    target_repository='https://example.ghe.com/OrgName/RepoName',
                    github_token='token',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('An active migration already exists for repository 912d0fd3-9c17-4b35-b67b-91848ce4d6bb',
                          str(ctx.exception))

    def test_create_migration_non_conflict_error_passes_through(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.side_effect = CLIError('Request failed with status 400. Bad request')

            with self.assertRaises(CLIError) as ctx:
                create_migration(
                    repository_id='00000000-0000-0000-0000-000000000000',
                    target_repository='https://example.ghe.com/OrgName/RepoName',
                    github_token='token',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('status 400', str(ctx.exception))

    def test_create_migration_no_token_and_missing_device_flow_config_fields_fails(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = {'clientId': 'client-id-only'}
            os.environ.pop('ELM_GITHUB_TOKEN', None)

            with self.assertRaises(CLIError) as ctx:
                create_migration(
                    repository_id='00000000-0000-0000-0000-000000000000',
                    target_repository='https://example.ghe.com/OrgName/RepoName',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('missing clientId or enterpriseUrl', str(ctx.exception))

    def test_build_device_flow_config_url_encodes_target_repository(self):
        url = migration_module._build_device_flow_config_url(
            self._TEST_ORG,
            'https://example.ghe.com/org name/repo name'
        )

        self.assertIn('/_apis/migrations/deviceFlowConfig?', url)
        self.assertIn('targetRepository=https%3A%2F%2Fexample.ghe.com%2Forg+name%2Frepo+name', url)
        self.assertIn('api-version=7.2-preview', url)

    def test_get_device_flow_config_falls_back_to_legacy_path_on_404(self):
        with patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.side_effect = [
                CLIError("Request failed with status 404. The controller for path '/_apis/migrations/deviceFlowConfig' was not found."),
                {'clientId': 'abc', 'enterpriseUrl': 'https://example.ghe.com'}
            ]

            result = migration_module._get_device_flow_config(
                client=object(),
                organization=self._TEST_ORG,
                target_repository='https://example.ghe.com/org/repo'
            )

            self.assertEqual(result['clientId'], 'abc')
            self.assertEqual(mock_send.call_count, 2)

    def test_get_device_flow_config_both_paths_404_shows_pat_guidance(self):
        with patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.side_effect = [
                CLIError("Request failed with status 404. The controller for path '/_apis/migrations/deviceFlowConfig' was not found."),
                CLIError("Request failed with status 404. The controller for path '/_apis/elm/migrations/deviceFlowConfig' was not found."),
            ]

            with self.assertRaises(CLIError) as ctx:
                migration_module._get_device_flow_config(
                    client=object(),
                    organization=self._TEST_ORG,
                    target_repository='https://example.ghe.com/org/repo'
                )

            self.assertIn('Provide --github-token or set ELM_GITHUB_TOKEN', str(ctx.exception))

    def test_run_device_flow_handles_access_denied(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post, \
             patch('azext_devops.dev.migration.migration.time.sleep') as mock_sleep, \
             patch('azext_devops.dev.migration.migration.time.monotonic') as mock_monotonic:
            mock_sleep.return_value = None
            mock_monotonic.side_effect = [0, 0]
            mock_post.side_effect = [
                {
                    'device_code': 'devcode',
                    'user_code': 'ABCD-1234',
                    'verification_uri': 'https://example.ghe.com/login/device',
                    'interval': 1,
                    'expires_in': 900,
                },
                {'error': 'access_denied'},
            ]

            with self.assertRaises(CLIError) as ctx:
                migration_module._run_device_flow('client-id', 'https://example.ghe.com')

            self.assertIn('Authorization denied', str(ctx.exception))

    def test_run_device_flow_handles_expired_token(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post, \
             patch('azext_devops.dev.migration.migration.time.sleep') as mock_sleep, \
             patch('azext_devops.dev.migration.migration.time.monotonic') as mock_monotonic:
            mock_sleep.return_value = None
            mock_monotonic.side_effect = [0, 0]
            mock_post.side_effect = [
                {
                    'device_code': 'devcode',
                    'user_code': 'ABCD-1234',
                    'verification_uri': 'https://example.ghe.com/login/device',
                    'interval': 1,
                    'expires_in': 900,
                },
                {'error': 'expired_token'},
            ]

            with self.assertRaises(CLIError) as ctx:
                migration_module._run_device_flow('client-id', 'https://example.ghe.com')

            self.assertIn('Device code expired', str(ctx.exception))

    def test_run_device_flow_retries_authorization_pending_and_returns_token(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post, \
             patch('azext_devops.dev.migration.migration.time.sleep') as mock_sleep, \
             patch('azext_devops.dev.migration.migration.time.monotonic') as mock_monotonic:
            mock_sleep.return_value = None
            mock_monotonic.side_effect = [0, 0, 1]
            mock_post.side_effect = [
                {
                    'device_code': 'devcode',
                    'user_code': 'ABCD-1234',
                    'verification_uri': 'https://example.ghe.com/login/device',
                    'interval': 1,
                    'expires_in': 900,
                },
                {'error': 'authorization_pending'},
                {'access_token': 'token-from-device-flow'},
            ]

            token = migration_module._run_device_flow('client-id', 'https://example.ghe.com')
            self.assertEqual(token, 'token-from-device-flow')

    def test_run_device_flow_fails_for_invalid_interval(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post:
            mock_post.return_value = {
                'device_code': 'devcode',
                'user_code': 'ABCD-1234',
                'verification_uri': 'https://example.ghe.com/login/device',
                'interval': 'abc',
                'expires_in': 900,
            }

            with self.assertRaises(CLIError) as ctx:
                migration_module._run_device_flow('client-id', 'https://example.ghe.com')

            self.assertIn('Invalid device-flow response: interval must be a positive integer.', str(ctx.exception))

    def test_run_device_flow_fails_for_invalid_expires_in(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post:
            mock_post.return_value = {
                'device_code': 'devcode',
                'user_code': 'ABCD-1234',
                'verification_uri': 'https://example.ghe.com/login/device',
                'interval': 5,
                'expires_in': 0,
            }

            with self.assertRaises(CLIError) as ctx:
                migration_module._run_device_flow('client-id', 'https://example.ghe.com')

            self.assertIn('Invalid device-flow response: expires_in must be a positive integer.', str(ctx.exception))

    def test_post_form_401_returns_generic_guidance(self):
        with patch('azext_devops.dev.migration.migration.urlopen') as mock_urlopen:
            mock_urlopen.side_effect = HTTPError(
                url='https://example.ghe.com/login/device/code',
                code=401,
                msg='Unauthorized',
                hdrs=None,
                fp=None
            )

            with self.assertRaises(CLIError) as ctx:
                migration_module._post_form('https://example.ghe.com/login/device/code', {
                    'client_id': 'client-id'
                })

            self.assertIn('GitHub device flow is unavailable for this organization.', str(ctx.exception))

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

    def test_send_request_uses_precheck_issue_detail_from_response_body(self):
        class MockResponse(object):
            status_code = 400
            headers = {'Content-Type': 'application/json'}

            @staticmethod
            def json():
                return {
                    'validationIssues': [
                        {
                            'PreCheckIssueType': 'TargetRepositoryDoesNotExist',
                            'Message': 'Target repository could not be found.'
                        }
                    ],
                    'message': 'Generic server message'
                }

        class MockClient(object):
            @staticmethod
            def send(request, headers, content):
                del request, headers, content
                return MockResponse()

        with self.assertRaises(CLIError) as ctx:
            migration_module._send_request(MockClient(), 'POST', 'https://example.test')

        text = str(ctx.exception)
        self.assertIn('status 400', text)
        self.assertIn('Pre-check issues:', text)
        self.assertIn('TargetRepositoryDoesNotExist', text)
        self.assertIn('Target repository could not be found.', text)


if __name__ == '__main__':
    unittest.main()
