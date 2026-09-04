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
from knack.prompting import NoTTYException
from azext_devops.dev.team.service_endpoint import (list_service_endpoints,
                                                    show_service_endpoint,
                                                    create_service_endpoint,
                                                    create_github_service_endpoint,
                                                    create_azurerm_service_endpoint,
                                                    delete_service_endpoint,
                                                    update_service_endpoint,
                                                    migrate_external_federated_credential)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.tests.utils.helper import get_client_mock_helper


class TestServiceEndpointMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/someorg'
    _TEST_PROJECT_NAME = 'sample_project'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)
        self.get_SEs_patcher = patch('azext_devops.devops_sdk.v5_0.service_endpoint.service_endpoint_client.ServiceEndpointClient.get_service_endpoints')
        self.get_SE_details_patcher = patch('azext_devops.devops_sdk.v5_0.service_endpoint.service_endpoint_client.ServiceEndpointClient.get_service_endpoint_details')
        self.create_SE_patcher = patch('azext_devops.devops_sdk.v5_0.service_endpoint.service_endpoint_client.ServiceEndpointClient.create_service_endpoint')
        self.delete_SE_patcher = patch('azext_devops.devops_sdk.v5_0.service_endpoint.service_endpoint_client.ServiceEndpointClient.delete_service_endpoint')
        self.set_authorize_endpoint = patch('azext_devops.dev.pipelines.pipeline_utils.set_authorize_resource')
        self.get_authorize_endpoint = patch('azext_devops.dev.pipelines.pipeline_utils.get_authorize_resource')

        self.mock_get_client = self.get_client.start()
        self.mock_get_SEs = self.get_SEs_patcher.start()
        self.mock_get_SE_detail = self.get_SE_details_patcher.start()
        self.mock_create_SE = self.create_SE_patcher.start()
        self.mock_delete_SE = self.delete_SE_patcher.start()
        self.mock_set_authorize = self.set_authorize_endpoint.start()
        self.mock_get_authorize = self.get_authorize_endpoint.start()

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_service_endpoint(self):
        response = list_service_endpoints(self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)
        
        #assert
        self.mock_get_SEs.assert_called_once_with(self._TEST_PROJECT_NAME)

    def test_get_service_endpoint(self):
        randomId = 'abcdfe34343'
        response = show_service_endpoint(randomId, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)

        #assert
        self.mock_get_SE_detail.assert_called_once_with(self._TEST_PROJECT_NAME, randomId)

    def test_delete_service_endpoint(self):
        randomId = 'abcdfe34343'
        delete_service_endpoint(randomId, 'false', self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)

        #assert 
        self.mock_delete_SE.assert_called_once_with(self._TEST_PROJECT_NAME, randomId, 'false')

    def test_update_service_endpoint(self):
        randomId = 'abcdfe34343'
        update_service_endpoint(id=randomId, enable_for_all=True, organization=self._TEST_DEVOPS_ORGANIZATION,
                                project=self._TEST_PROJECT_NAME)

        #assert 
        self.mock_get_SE_detail.assert_called_once_with(self._TEST_PROJECT_NAME, randomId)
        self.mock_set_authorize.assert_called_once()
        self.mock_get_authorize.assert_called_once()


    def test_update_without_params_service_endpoint(self):
        randomId = 'abcdfe34343'
        try:
            update_service_endpoint(id=randomId, enable_for_all=None, organization=self._TEST_DEVOPS_ORGANIZATION,
                                    project=self._TEST_PROJECT_NAME)
        except CLIError as ex:
            self.assertEqual(str(ex), 'Atleast one property to be updated must be specified.')
            self.mock_get_SE_detail.assert_not_called()
            self.mock_set_authorize.assert_not_called()
            self.mock_get_authorize.assert_not_called()

    def test_create_service_endpoint_github(self):
        import os
        os.environ['AZURE_DEVOPS_EXT_GITHUB_PAT'] = 'fakeToken'
        response = create_github_service_endpoint(name = '', github_url='',
                                                  organization = self._TEST_DEVOPS_ORGANIZATION, 
                                                  project = self._TEST_PROJECT_NAME)
        del os.environ['AZURE_DEVOPS_EXT_GITHUB_PAT']

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

    def test_create_service_endpoint_azure_rm(self):
        import os
        os.environ['AZURE_DEVOPS_EXT_AZURE_RM_SERVICE_PRINCIPAL_KEY'] = 'fakeKey'
        response = create_azurerm_service_endpoint(name = '',
                                                   azure_rm_tenant_id='',
                                                   azure_rm_service_principal_id='', 
                                                   azure_rm_subscription_id='',
                                                   azure_rm_subscription_name='',
                                                   organization = self._TEST_DEVOPS_ORGANIZATION,
                                                   project = self._TEST_PROJECT_NAME)
        del os.environ['AZURE_DEVOPS_EXT_AZURE_RM_SERVICE_PRINCIPAL_KEY']

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

    def test_create_service_endpoint_ttyi_exception_github(self):
        try:
            response = create_github_service_endpoint(name = '', github_url='',
                                                      organization = self._TEST_DEVOPS_ORGANIZATION,
                                                      project = self._TEST_PROJECT_NAME)
            self.fail('exception was expected')
        except NoTTYException as ex:
            self.assertEqual(str(ex), 'Please pass GitHub access token in AZURE_DEVOPS_EXT_GITHUB_PAT environment variable in non-interactive mode.')

    def test_create_service_endpoint_ttyi_exception_azure_se(self):
        try:
            response = create_azurerm_service_endpoint(name = '',
                                                       azure_rm_tenant_id='',
                                                       azure_rm_service_principal_id='', 
                                                       azure_rm_subscription_id='',
                                                       azure_rm_subscription_name='',
                                                       organization = self._TEST_DEVOPS_ORGANIZATION,
                                                       project = self._TEST_PROJECT_NAME)
            self.fail('exception was expected')
        except NoTTYException as ex:
            self.assertEqual(str(ex), 'Please specify azure service principal key in AZURE_DEVOPS_EXT_AZURE_RM_SERVICE_PRINCIPAL_KEY environment variable in non-interactive mode or use --azure-rm-service-principal-certificate-path.')


class TestMigrateExternalFederatedCredential(unittest.TestCase):

    _TEST_AZDO_SUBJECT = 'sc://myorg/myproject/myconnection'
    _TEST_BEARER_TOKEN = 'fake-entra-token'
    _TEST_SUBSCRIPTIONS = [{'tenantId': 'tenant-123', 'isDefault': True}]

    def _make_profile_mock(self, mock_profile_cls):
        mock_profile = mock_profile_cls.return_value
        mock_profile.load_cached_subscriptions.return_value = self._TEST_SUBSCRIPTIONS
        return mock_profile

    def _make_response_mock(self, ok=True, json_data=None, status_code=200, text=''):
        from unittest.mock import MagicMock
        mock_resp = MagicMock()
        mock_resp.ok = ok
        mock_resp.status_code = status_code
        mock_resp.text = text
        mock_resp.json.return_value = json_data or {'status': 'success'}
        return mock_resp

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value=_TEST_BEARER_TOKEN)
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    @patch('azext_devops.dev.team.service_endpoint.requests.post')
    def test_convert_derives_org_from_subject(self, mock_post, mock_profile_cls, mock_get_token):
        self._make_profile_mock(mock_profile_cls)
        mock_post.return_value = self._make_response_mock()

        result = migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        mock_post.assert_called_once()
        url = mock_post.call_args[0][0]
        self.assertIn('https://dev.azure.com/myorg', url)
        self.assertIn('externalfederatedcredentialmigration', url)
        self.assertEqual(result, {'status': 'success'})

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value=_TEST_BEARER_TOKEN)
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    @patch('azext_devops.dev.team.service_endpoint.requests.post')
    def test_convert_uses_explicit_origin(self, mock_post, mock_profile_cls, mock_get_token):
        self._make_profile_mock(mock_profile_cls)
        mock_post.return_value = self._make_response_mock()
        explicit_origin = 'https://dev.azure.com/otherorg'

        migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT, origin=explicit_origin)

        url = mock_post.call_args[0][0]
        self.assertIn('otherorg', url)

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value=_TEST_BEARER_TOKEN)
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    @patch('azext_devops.dev.team.service_endpoint.requests.post')
    def test_convert_sends_bearer_token(self, mock_post, mock_profile_cls, mock_get_token):
        self._make_profile_mock(mock_profile_cls)
        mock_post.return_value = self._make_response_mock()

        migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        headers = mock_post.call_args[1]['headers']
        self.assertEqual(headers['Authorization'], 'Bearer {0}'.format(self._TEST_BEARER_TOKEN))
        self.assertEqual(headers['Content-Type'], 'application/json')

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value=_TEST_BEARER_TOKEN)
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    @patch('azext_devops.dev.team.service_endpoint.requests.post')
    def test_convert_sends_subject_in_body(self, mock_post, mock_profile_cls, mock_get_token):
        import json
        self._make_profile_mock(mock_profile_cls)
        mock_post.return_value = self._make_response_mock()

        migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        body = json.loads(mock_post.call_args[1]['data'])
        self.assertEqual(body['serviceConnectionInput'], self._TEST_AZDO_SUBJECT)

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value=_TEST_BEARER_TOKEN)
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    @patch('azext_devops.dev.team.service_endpoint.requests.post')
    def test_convert_raises_on_http_error(self, mock_post, mock_profile_cls, mock_get_token):
        self._make_profile_mock(mock_profile_cls)
        mock_post.return_value = self._make_response_mock(ok=False, status_code=400, text='Bad Request')

        with self.assertRaises(CLIError) as ctx:
            migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        self.assertIn('400', str(ctx.exception))
        self.assertIn('Bad Request', str(ctx.exception))

    def test_convert_raises_on_invalid_subject_format(self):
        with self.assertRaises(CLIError) as ctx:
            migrate_external_federated_credential(azdo_subject='not-a-valid-subject')

        self.assertIn('--azdo-subject', str(ctx.exception))

    @patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login', return_value='')
    @patch('azext_devops.dev.team.service_endpoint.Profile')
    def test_convert_raises_when_no_entra_token(self, mock_profile_cls, mock_get_token):
        self._make_profile_mock(mock_profile_cls)

        with self.assertRaises(CLIError) as ctx:
            migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        self.assertIn('az login', str(ctx.exception))

    @patch('azext_devops.dev.team.service_endpoint.Profile')
    def test_convert_raises_when_no_subscriptions(self, mock_profile_cls):
        mock_profile = mock_profile_cls.return_value
        mock_profile.load_cached_subscriptions.return_value = []

        with self.assertRaises(CLIError) as ctx:
            migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        self.assertIn('az login', str(ctx.exception))

    @patch('azext_devops.dev.team.service_endpoint.Profile')
    def test_convert_handles_missing_cached_subscriptions(self, mock_profile_cls):
        mock_profile = mock_profile_cls.return_value
        mock_profile.get_current_account_user.side_effect = RuntimeError('no cached account')
        mock_profile.load_cached_subscriptions.return_value = None

        with self.assertRaises(CLIError) as ctx:
            migrate_external_federated_credential(azdo_subject=self._TEST_AZDO_SUBJECT)

        self.assertIn('az login', str(ctx.exception))

if __name__ == '__main__':
    unittest.main()