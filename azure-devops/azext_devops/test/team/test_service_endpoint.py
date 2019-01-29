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
                                                    create_service_endpoint)
from azext_devops.dev.team.const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                                        SERVICE_ENDPOINT_TYPE_GITHUB,
                                        SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                                        SERVICE_ENDPOINT_TYPE_AZURE_RM)

from azext_devops.dev.common.services import clear_connection_cache
    
class TestServiceEndpointMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
    _TEST_PROJECT_NAME = 'sample_project'

    def setUp(self):
        self.get_SEs_patcher = patch('vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient.get_service_endpoints')
        self.get_SE_details_patcher = patch('vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient.get_service_endpoint_details')
        self.create_SE_patcher = patch('vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient.create_service_endpoint')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')

        self.mock_get_SEs = self.get_SEs_patcher.start()
        self.mock_get_SE_detail = self.get_SE_details_patcher.start()
        self.mock_create_SE = self.create_SE_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        self.get_SEs_patcher.stop()
        self.get_SE_details_patcher.stop()
        self.create_SE_patcher.stop()
        self.get_credential_patcher.stop()

    def test_list_service_endpoint(self):
        response = list_service_endpoints(self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)
        
        #assert
        self.mock_get_SEs.assert_called_once_with(self._TEST_PROJECT_NAME)

    def test_get_service_endpoint(self):
        randomId = 'abcdfe34343'
        response = show_service_endpoint(randomId, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME)

        #assert
        self.mock_get_SE_detail.assert_called_once_with(self._TEST_PROJECT_NAME, randomId)

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
                                           organization = self._TEST_DEVOPS_ORGANIZATION,
                                           project = self._TEST_PROJECT_NAME)

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

    def test_create_service_endpoint_azure_rm(self):
        response = create_service_endpoint(service_endpoint_type = SERVICE_ENDPOINT_TYPE_AZURE_RM, 
                                           authorization_scheme = SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL, 
                                           name = '',
                                           organization = self._TEST_DEVOPS_ORGANIZATION,
                                           project = self._TEST_PROJECT_NAME)

        #assert
        # not doing extensive comparision because object creation code does not have much logic
        self.mock_create_SE.assert_called_once()

if __name__ == '__main__':
    unittest.main()