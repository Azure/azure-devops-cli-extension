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
                                                    update_service_endpoint)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.test.utils.helper import get_client_mock_helper


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

if __name__ == '__main__':
    unittest.main()