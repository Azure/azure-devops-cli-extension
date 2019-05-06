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
from azext_devops.dev.team.service_endpoint import (list_service_endpoints,
                                                    show_service_endpoint,
                                                    create_service_endpoint,
                                                    delete_service_endpoint)
from azext_devops.dev.team.const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                                        SERVICE_ENDPOINT_TYPE_GITHUB,
                                        SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                                        SERVICE_ENDPOINT_TYPE_AZURE_RM)

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

        self.mock_get_client = self.get_client.start()
        self.mock_get_SEs = self.get_SEs_patcher.start()
        self.mock_get_SE_detail = self.get_SE_details_patcher.start()
        self.mock_create_SE = self.create_SE_patcher.start()
        self.mock_delete_SE = self.delete_SE_patcher.start()

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
        delete_service_endpoint(randomId, false, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)

        #assert 
        self.mock_delete_SE(self._TEST_PROJECT_NAME, randomId, false)

    def test_create_service_endpoint_unsupported(self):
        try:
            create_service_endpoint(service_endpoint_type = SERVICE_ENDPOINT_TYPE_GITHUB, authorization_scheme = SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL, name = '')
            self.fail()
        except CLIError as ex:
            pass

    def test_create_service_endpoint_github(self):
        response = create_service_endpoint(service_endpoint_type = SERVICE_ENDPOINT_TYPE_GITHUB, 
                                           authorization_scheme = SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN, 
                                           name = '',
                                           github_access_token = 'fake',
                                           organization = self._TEST_DEVOPS_ORGANIZATION,
                                           project = self._TEST_PROJECT_NAME)

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

    def test_create_service_endpoint_azure_rm(self):
        response = create_service_endpoint(service_endpoint_type = SERVICE_ENDPOINT_TYPE_AZURE_RM, 
                                           authorization_scheme = SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL, 
                                           name = '',
                                           azure_rm_service_principal_key = 'fake',
                                           organization = self._TEST_DEVOPS_ORGANIZATION,
                                           project = self._TEST_PROJECT_NAME)

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

if __name__ == '__main__':
    unittest.main()