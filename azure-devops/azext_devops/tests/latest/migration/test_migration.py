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
                                                  get_cutover_review,
                                                  approve_cutover,
                                                  delete_migration,
                                                  pause_migration,
                                                  resume_migration,
                                                  submit_pipeline_rewiring,
                                                  update_pipeline_rewiring,
                                                  retry_pipeline_rewiring,
                                                  acknowledge_pipeline_rewiring,
                                                  delete_pipeline_rewiring)


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
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
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
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('--target-repository must be specified', str(ctx.exception))

    def test_create_migration_fails_with_invalid_target_repository_url(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='ghe.example.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('https://host/org/repo', str(ctx.exception))

    def test_create_migration_fails_with_non_https_target_repository(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='http://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('https://host/org/repo', str(ctx.exception))

    def test_create_migration_fails_when_target_repository_path_is_not_org_repo(self):
        with self.assertRaises(CLIError) as ctx:
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName',
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
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

    def test_create_migration_with_service_endpoint_skips_device_flow(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration._get_device_flow_config') as mock_flow, \
             patch('azext_devops.dev.migration.migration._run_device_flow') as mock_run_flow:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG
            # Even with the env token set in setUp, presence of service-endpoint-id
            # must short-circuit token resolution entirely.
            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                organization=self._TEST_ORG,
                detect=False
            )

            mock_flow.assert_not_called()
            mock_run_flow.assert_not_called()
            self.assertEqual(mock_send.call_count, 1)
            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['serviceEndpointId'], '1df3c9b3-666c-4033-82de-059e7759ddfe')
            self.assertNotIn('gitHubUserToken', payload)

    def test_create_migration_with_service_endpoint_and_token_rejected(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                create_migration(
                    repository_id='00000000-0000-0000-0000-000000000000',
                    target_repository='https://example.ghe.com/OrgName/RepoName',
                    target_owner_user_id='TestOwner',
                    service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                    github_token='param-token',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('Specify either --service-endpoint-id or --github-token', str(ctx.exception))
            mock_send.assert_not_called()

    def test_create_migration_with_service_endpoint_ignores_env_token(self):
        # ELM_GITHUB_TOKEN is set in setUp; the service endpoint path must not
        # pick it up and must not include gitHubUserToken in the payload.
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration._get_device_flow_config') as mock_flow:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                validate_only=True,
                organization=self._TEST_ORG,
                detect=False
            )

            mock_flow.assert_not_called()
            payload = mock_send.call_args[0][3]
            self.assertNotIn('gitHubUserToken', payload)
            self.assertEqual(payload['serviceEndpointId'], '1df3c9b3-666c-4033-82de-059e7759ddfe')
            self.assertTrue(payload['validateOnly'])

    def test_create_migration_service_endpoint_with_whitespace_github_token_not_rejected(self):
        # A whitespace-only --github-token normalizes to None and must not
        # trigger the mutual-exclusion error when --service-endpoint-id is set.
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration._get_device_flow_config') as mock_flow:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                github_token='   ',
                organization=self._TEST_ORG,
                detect=False
            )

            mock_flow.assert_not_called()
            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['serviceEndpointId'], '1df3c9b3-666c-4033-82de-059e7759ddfe')
            self.assertNotIn('gitHubUserToken', payload)

    def test_create_migration_service_endpoint_conflict_returns_clear_message(self):
        # Ensure the 409/TF400898 friendly message still surfaces on the
        # service-endpoint code path (no GitHub token preflight to swallow it).
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.side_effect = CLIError('Request failed with status 409. TF400898: An Internal Error Occurred.')

            with self.assertRaises(CLIError) as ctx:
                create_migration(
                    repository_id='912d0fd3-9c17-4b35-b67b-91848ce4d6bb',
                    target_repository='https://example.ghe.com/OrgName/RepoName',
                    service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('An active migration already exists for repository 912d0fd3-9c17-4b35-b67b-91848ce4d6bb',
                          str(ctx.exception))

    def test_create_migration_service_endpoint_with_all_optional_fields(self):
        # Service endpoint path must coexist with every other optional field
        # (agent pool, cutover date, skip validation, target owner).
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration._get_device_flow_config') as mock_flow:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                service_endpoint_id='1df3c9b3-666c-4033-82de-059e7759ddfe',
                agent_pool='TestPool',
                cutover_date='2026-06-01T00:00:00Z',
                skip_validation='AgentPoolExists',
                organization=self._TEST_ORG,
                detect=False
            )

            mock_flow.assert_not_called()
            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['serviceEndpointId'], '1df3c9b3-666c-4033-82de-059e7759ddfe')
            self.assertEqual(payload['targetOwnerUserId'], 'TestOwner')
            self.assertEqual(payload['agentPoolName'], 'TestPool')
            self.assertEqual(payload['scheduledCutoverDate'], '2026-06-01T00:00:00Z')
            self.assertEqual(payload['skipValidation'], 4)
            self.assertNotIn('gitHubUserToken', payload)

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
             patch('azext_devops.dev.migration.migration.time.monotonic') as mock_monotonic, \
             patch('azext_devops.dev.migration.migration._copy_to_clipboard') as mock_copy:
            mock_sleep.return_value = None
            mock_monotonic.side_effect = [0, 0, 1]
            mock_copy.return_value = False
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

    def test_run_device_flow_copies_user_code_to_clipboard_when_available(self):
        with patch('azext_devops.dev.migration.migration._post_form') as mock_post, \
             patch('azext_devops.dev.migration.migration.time.sleep') as mock_sleep, \
             patch('azext_devops.dev.migration.migration.time.monotonic') as mock_monotonic, \
             patch('azext_devops.dev.migration.migration._copy_to_clipboard') as mock_copy, \
             patch('azext_devops.dev.migration.migration.print') as mock_print:
            mock_sleep.return_value = None
            mock_monotonic.side_effect = [0, 0]
            mock_copy.return_value = True
            mock_post.side_effect = [
                {
                    'device_code': 'devcode',
                    'user_code': 'ABCD-1234',
                    'verification_uri': 'https://example.ghe.com/login/device',
                    'interval': 1,
                    'expires_in': 900,
                },
                {'access_token': 'token-from-device-flow'},
            ]

            token = migration_module._run_device_flow('client-id', 'https://example.ghe.com')

            self.assertEqual(token, 'token-from-device-flow')
            mock_copy.assert_called_once_with('ABCD-1234')
            mock_print.assert_any_call('Code copied to clipboard.')

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
                target_owner_user_id='TestOwner',
                validate_only=True,
                cutover_date='2030-12-31T11:59:00Z',
                agent_pool='TestPool',
                skip_validation=2147483647,
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['scheduledCutoverDate'], '2030-12-31T11:59:00Z')
            self.assertEqual(payload['agentPoolName'], 'TestPool')
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
                skip_validation='AgentPoolExists,,MaxFileSize',
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
                target_owner_user_id='TestOwner',
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
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
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
                target_owner_user_id='TestOwner',
                agent_pool='  TestPool  ',
                skip_validation=42,
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['agentPoolName'], 'TestPool')
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
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
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
                target_owner_user_id='TestOwner',
                validate_only=True,
                agent_pool='TestPool',
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
                target_owner_user_id='TestOwner',
                agent_pool='TestPool',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['agentPoolName'], 'TestPool')

    def test_create_migration_service_endpoint_id_included_in_payload(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._resolve_github_user_token') as mock_token, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG
            mock_token.return_value = 'ghp_test_token'

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                service_endpoint_id='12345678-1234-1234-1234-123456789012',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['serviceEndpointId'], '12345678-1234-1234-1234-123456789012')
            # When a service connection is supplied, the server uses it for GitHub auth;
            # the CLI must not resolve or send a GitHub token.
            self.assertNotIn('gitHubUserToken', payload)

    def test_create_migration_service_endpoint_id_skips_github_token_resolution(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._resolve_github_user_token') as mock_token, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG
            mock_token.return_value = 'ghp_test_token'

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                service_endpoint_id='12345678-1234-1234-1234-123456789012',
                organization=self._TEST_ORG,
                detect=False
            )

            mock_token.assert_not_called()

    def test_create_migration_service_endpoint_id_omitted_when_not_provided(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._resolve_github_user_token') as mock_token, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG
            mock_token.return_value = 'ghp_test_token'

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertNotIn('serviceEndpointId', payload)

    def test_create_migration_empty_service_endpoint_id_omitted(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._resolve_github_user_token') as mock_token, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG
            mock_token.return_value = 'ghp_test_token'

            create_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                target_repository='https://example.ghe.com/OrgName/RepoName',
                target_owner_user_id='TestOwner',
                service_endpoint_id='   ',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertNotIn('serviceEndpointId', payload)

    def test_cancel_cutover_sends_min_value_sentinel(self):
        # The ELM service silently ignores `null` for scheduledCutoverDate and only
        # treats DateTimeOffset.MinValue ("0001-01-01T00:00:00+00:00") as the clear
        # sentinel. Sending null leaves the field set on the server.
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.get_migration') as mock_get:
            mock_get.return_value = {'stage': 'readyForCutover', 'status': 'active'}
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            cancel_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['scheduledCutoverDate'], '0001-01-01T00:00:00+00:00')

    def test_cancel_cutover_returns_success_message_when_empty_response(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.get_migration') as mock_get:
            mock_get.return_value = {'stage': 'readyForCutover', 'status': 'active'}
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            result = cancel_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            self.assertIn('message', result)
            self.assertIn('cancelled', result['message'].lower())

    def test_cancel_cutover_blocked_when_stage_is_cutover(self):
        # Service-side Bug 2394803: clearing scheduledCutoverDate after the worker
        # has entered the Cutover stage leaves the migration in a state that
        # requires server-side recovery. The CLI must block this case until the
        # service-side guard ships.
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.get_migration') as mock_get:
            mock_get.return_value = {'stage': 'cutover', 'status': 'active'}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                cancel_cutover(
                    repository_id='00000000-0000-0000-0000-000000000000',
                    organization=self._TEST_ORG,
                    detect=False
                )

            self.assertIn('Cutover stage', str(ctx.exception))
            # Must not have called PUT against the migration record.
            mock_send.assert_not_called()

    def test_get_cutover_review_calls_get(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {'totalUnprocessedCount': 3}
            mock_resolve.return_value = self._TEST_ORG

            get_cutover_review(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'GET')
            self.assertIn('/_apis/elm/migrations/00000000-0000-0000-0000-000000000000/cutoverReview', args[2])

    def test_approve_cutover_sends_cutover_failure_accepted_count(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {'stage': 'ReadyForCutover'}
            mock_resolve.return_value = self._TEST_ORG

            approve_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                accept_failures=3,
                organization=self._TEST_ORG,
                detect=False
            )

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'PUT')
            self.assertEqual(args[3]['cutoverFailureAcceptedCount'], 3)

    def test_approve_cutover_requires_accept_failures(self):
        with self.assertRaises(CLIError) as ctx:
            approve_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('--accept-failures must be specified', str(ctx.exception))

    def test_approve_cutover_rejects_negative_accept_failures(self):
        with self.assertRaises(CLIError) as ctx:
            approve_cutover(
                repository_id='00000000-0000-0000-0000-000000000000',
                accept_failures=-1,
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('non-negative integer', str(ctx.exception))

    def test_pause_returns_success_message_when_empty_response(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            result = pause_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            self.assertIn('message', result)
            self.assertIn('paused', result['message'].lower())

    def test_pause_returns_migration_data_when_service_responds(self):
        migration_response = {'repositoryId': '00000000-0000-0000-0000-000000000000', 'status': 'suspended'}
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = migration_response
            mock_resolve.return_value = self._TEST_ORG

            result = pause_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            self.assertEqual(result, migration_response)

    def test_pause_returns_migration_data_when_service_responds_paused(self):
        migration_response = {'repositoryId': '00000000-0000-0000-0000-000000000000', 'status': 'paused'}
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = migration_response
            mock_resolve.return_value = self._TEST_ORG

            result = pause_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            self.assertEqual(result, migration_response)

    def test_list_migrations_warns_when_empty(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.logger') as mock_logger:
            mock_send.return_value = {'value': []}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(organization=self._TEST_ORG, detect=False)

            mock_logger.warning.assert_called_once()
            warning_msg = mock_logger.warning.call_args[0][0]
            self.assertIn('No migrations found', warning_msg)

    def test_list_migrations_hints_include_inactive_when_not_passed(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.logger') as mock_logger:
            mock_send.return_value = {'value': []}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(include_inactive=False, organization=self._TEST_ORG, detect=False)

            warning_call = str(mock_logger.warning.call_args)
            self.assertIn('include-inactive', warning_call)

    def test_list_migrations_no_hint_when_include_inactive_passed(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send, \
             patch('azext_devops.dev.migration.migration.logger') as mock_logger:
            mock_send.return_value = {'value': []}
            mock_resolve.return_value = self._TEST_ORG

            list_migrations(include_inactive=True, organization=self._TEST_ORG, detect=False)

            warning_call = str(mock_logger.warning.call_args)
            self.assertNotIn('include-inactive', warning_call)

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

    def test_resume_fails_when_review_for_cutover(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'active', 'stage': 'ReviewForCutover'}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('cutover review', str(ctx.exception))
            self.assertIn('cutover approve', str(ctx.exception))

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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

    def test_resume_sets_validate_only_when_status_paused(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'status': 'paused'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             validate_only=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertTrue(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

    def test_resume_sets_migration_when_status_paused(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {'status': 'paused'}
            mock_resolve.return_value = self._TEST_ORG

            resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                             migration=True,
                             organization=self._TEST_ORG, detect=False)

            payload = mock_send.call_args[0][3]
            self.assertFalse(payload['validateOnly'])
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

    def test_resume_migration_promotes_validate_only_completed(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_get.return_value = {
                'status': 'completed',
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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])

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
            self.assertEqual(payload['statusRequested'], migration_module._MIGRATION_STATUS_VALUES['active'])
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
            self.assertIn('00000000-0000-0000-0000-000000000000', str(ctx.exception))

    def test_resume_completed_without_migration_flag_errors(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'completed', 'validateOnly': True}
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
            self.assertIn('00000000-0000-0000-0000-000000000000', str(ctx.exception))

    def test_resume_completed_full_migration_errors(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'completed', 'validateOnly': False}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('abandon', str(ctx.exception))

    def test_resume_completed_status_takes_precedence_over_active_status_requested(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {
                'status': 'completed',
                'statusRequested': 'active',
                'validateOnly': True,
            }
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('--migration', str(ctx.exception))

    def test_resume_completed_status_requested_without_status_is_terminal(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'statusRequested': 'completed', 'validateOnly': False}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('abandon', str(ctx.exception))

    def test_resume_completed_case_variants_are_treated_as_terminal(self):
        with patch('azext_devops.dev.migration.migration.get_migration') as mock_get, \
             patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve:
            mock_get.return_value = {'status': 'Com_PleTed', 'validateOnly': False}
            mock_resolve.return_value = self._TEST_ORG

            with self.assertRaises(CLIError) as ctx:
                resume_migration(repository_id='00000000-0000-0000-0000-000000000000',
                                 organization=self._TEST_ORG, detect=False)
            self.assertIn('abandon', str(ctx.exception))

    def test_abandon_returns_success_message(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            result = delete_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'DELETE')
            self.assertIn('/_apis/elm/migrations/', args[2])
            self.assertNotIn('removeReadOnly=true', args[2])
            self.assertIsInstance(result, dict)
            self.assertIn('message', result)
            self.assertIn('abandoned successfully', result['message'])

    def test_abandon_remove_read_only_included_when_requested(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_send.return_value = {}
            mock_resolve.return_value = self._TEST_ORG

            delete_migration(
                repository_id='00000000-0000-0000-0000-000000000000',
                remove_read_only=True,
                organization=self._TEST_ORG,
                detect=False
            )

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'DELETE')
            self.assertIn('removeReadOnly=true', args[2])

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

    def test_submit_pipeline_rewiring_accepts_space_separated_ids(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = []

            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42', '43', '44'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['pipelineIds'], [42, 43, 44])
            self.assertEqual(payload['serviceConnectionId'], '11111111-1111-1111-1111-111111111111')

    def test_submit_pipeline_rewiring_accepts_comma_separated_ids(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = []

            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42,43,44'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['pipelineIds'], [42, 43, 44])

    def test_submit_pipeline_rewiring_rejects_invalid_pipeline_id(self):
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42', 'abc'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('--pipeline-ids', str(ctx.exception))

    def test_submit_pipeline_rewiring_rejects_invalid_service_connection_guid(self):
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42'],
                service_connection_id='not-a-guid',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('--service-connection-id must be a valid GUID', str(ctx.exception))

    def test_submit_pipeline_rewiring_rejects_invalid_repository_mapping(self):
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                repository_mapping=['not-a-guid=myorg/repo'],
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('repository-mapping source repo ID', str(ctx.exception))

    def test_submit_pipeline_rewiring_rejects_repository_mapping_with_extra_slash(self):
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                repository_mapping=['aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa=myorg/repo/extra'],
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('format <owner>/<repo>', str(ctx.exception))

    def test_submit_pipeline_rewiring_parses_repository_mapping(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = []

            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                repository_mapping=['aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa=myorg/shared-templates'],
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['repositoryMappings'][0]['sourceRepositoryId'],
                             'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa')
            self.assertEqual(payload['repositoryMappings'][0]['targetRepository'],
                             'myorg/shared-templates')

    def test_update_pipeline_rewiring_rejects_no_flags(self):
        with self.assertRaises(CLIError) as ctx:
            update_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('At least one update flag must be provided', str(ctx.exception))

    def test_update_pipeline_rewiring_payload_contains_provided_fields_only(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = []

            update_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                add_ids=['50', '51'],
                remove_ids=['42'],
                service_connection_id='22222222-2222-2222-2222-222222222222',
                organization=self._TEST_ORG,
                detect=False
            )

            payload = mock_send.call_args[0][3]
            self.assertEqual(payload['addPipelineIds'], [50, 51])
            self.assertEqual(payload['removePipelineIds'], [42])
            self.assertEqual(payload['serviceConnectionId'], '22222222-2222-2222-2222-222222222222')
            self.assertNotIn('retryFailedPipelineIds', payload)
            self.assertNotIn('acknowledgePipelineIds', payload)

    def test_retry_pipeline_rewiring_calls_update_with_retry_ids(self):
        with patch('azext_devops.dev.migration.migration.update_pipeline_rewiring') as mock_update:
            mock_update.return_value = []

            retry_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42', '43'],
                organization=self._TEST_ORG,
                detect=False
            )

            kwargs = mock_update.call_args[1]
            self.assertEqual(kwargs['retry_ids'], [42, 43])

    def test_acknowledge_pipeline_rewiring_calls_update_with_ack_ids(self):
        with patch('azext_devops.dev.migration.migration.update_pipeline_rewiring') as mock_update:
            mock_update.return_value = []

            acknowledge_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['44', '45'],
                organization=self._TEST_ORG,
                detect=False
            )

            kwargs = mock_update.call_args[1]
            self.assertEqual(kwargs['acknowledge_ids'], [44, 45])

    def test_submit_pipeline_rewiring_rejects_more_than_200_ids(self):
        too_many_ids = [str(i) for i in range(1, 202)]
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=too_many_ids,
                service_connection_id='11111111-1111-1111-1111-111111111111',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('maximum of 200', str(ctx.exception))

    def test_submit_pipeline_rewiring_rejects_empty_comma_value(self):
        with self.assertRaises(CLIError) as ctx:
            submit_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                pipeline_ids=['42,,43'],
                service_connection_id='11111111-1111-1111-1111-111111111111',
                organization=self._TEST_ORG,
                detect=False
            )
        self.assertIn('contains an empty value', str(ctx.exception))

    def test_delete_pipeline_rewiring_calls_delete_with_migration_id_query(self):
        with patch('azext_devops.dev.migration.migration.resolve_instance') as mock_resolve, \
             patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
             patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_resolve.return_value = self._TEST_ORG
            mock_send.return_value = {}

            delete_pipeline_rewiring(
                repository_id='00000000-0000-0000-0000-000000000000',
                migration_id=7,
                organization=self._TEST_ORG,
                detect=False
            )

            args = mock_send.call_args[0]
            self.assertEqual(args[1], 'DELETE')
            self.assertIn('migrationId=7', args[2])

    def test_send_request_404_returns_server_message(self):
        class MockResponse(object):
            status_code = 404
            headers = {'Content-Type': 'application/json'}

            @staticmethod
            def json():
                return {'message': 'Migration not found'}

        class MockClient(object):
            @staticmethod
            def send(request, headers, content):
                del request, headers, content
                return MockResponse()

        with self.assertRaises(CLIError) as ctx:
            migration_module._send_request(MockClient(), 'GET', 'https://example.test')
        self.assertIn('status 404', str(ctx.exception))
        self.assertIn('Migration not found', str(ctx.exception))

    def test_send_request_includes_correlation_id_for_server_errors(self):
        class MockResponse(object):
            status_code = 500
            headers = {'Content-Type': 'application/json', 'X-VSS-E2EID': 'abc-123'}

            @staticmethod
            def json():
                return {'message': 'Internal server error'}

        class MockClient(object):
            @staticmethod
            def send(request, headers, content):
                del request, headers, content
                return MockResponse()

        with self.assertRaises(CLIError) as ctx:
            migration_module._send_request(MockClient(), 'GET', 'https://example.test')
        self.assertIn('abc-123', str(ctx.exception))


    def test_send_request_404_raises_resource_not_found_error(self):
        from azure.cli.core.azclierror import ResourceNotFoundError

        class MockResponse(object):
            status_code = 404
            headers = {'Content-Type': 'application/json'}

            @staticmethod
            def json():
                return {'message': 'Migration not found'}

        class MockClient(object):
            @staticmethod
            def send(request, headers, content):
                del request, headers, content
                return MockResponse()

        with self.assertRaises(ResourceNotFoundError) as ctx:
            migration_module._send_request(MockClient(), 'GET', 'https://example.test')
        self.assertIn('status 404', str(ctx.exception))

    def test_send_request_403_raises_forbidden_error(self):
        from azure.cli.core.azclierror import ForbiddenError

        class MockResponse(object):
            status_code = 403
            headers = {'Content-Type': 'application/json'}

            @staticmethod
            def json():
                return {'message': 'Access denied'}

        class MockClient(object):
            @staticmethod
            def send(request, headers, content):
                del request, headers, content
                return MockResponse()

        with self.assertRaises(ForbiddenError) as ctx:
            migration_module._send_request(MockClient(), 'GET', 'https://example.test')
        self.assertIn('status 403', str(ctx.exception))
        self.assertIn('Access denied', str(ctx.exception))

    def test_list_pipeline_rewiring_appends_hint_on_failed_migration(self):
        with patch('azext_devops.dev.migration.migration._resolve_org_for_auth') as mock_org, \
                patch('azext_devops.dev.migration.migration._resolve_repository_id') as mock_repo, \
                patch('azext_devops.dev.migration.migration._get_service_client') as mock_client, \
                patch('azext_devops.dev.migration.migration._send_request') as mock_send:
            mock_org.return_value = 'https://dev.azure.com/contoso'
            mock_repo.return_value = '11111111-1111-1111-1111-111111111111'
            mock_client.return_value = object()
            mock_send.side_effect = CLIError(
                'Request failed with status 400. Pipeline information is not available '
                'for failed migrations.')

            with self.assertRaises(CLIError) as ctx:
                migration_module.list_pipeline_rewiring(
                    repository_id='11111111-1111-1111-1111-111111111111',
                    organization='https://dev.azure.com/contoso')
            self.assertIn('pipelines delete', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()
