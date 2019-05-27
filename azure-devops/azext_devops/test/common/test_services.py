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

from azext_devops.dev.common.telemetry import (set_tracking_data, 
    try_send_telemetry_data, vsts_tracking_data)

from azext_devops.dev.common.services import (get_connection,
                                              clear_connection_cache,
                                              resolve_instance_project_and_repo)


class TestServicesMethods(unittest.TestCase):    
    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
    _TEST_DEVOPS_ORGANIZATION2 = 'https://dev.azure.com/MyOrganization'

    def setUp(self):
        clear_connection_cache()
   
    def test_get_connection_cache_works(self):
        with patch('azext_devops.dev.common.services._get_credentials') as mock_get_credentials:  
            with patch('azext_devops.dev.common.telemetry.try_send_telemetry_data') as mock_telemetry_send:
                get_connection(self._TEST_DEVOPS_ORGANIZATION)
                get_connection(self._TEST_DEVOPS_ORGANIZATION.lower())
                #assert
                mock_telemetry_send.assert_called_once_with(self._TEST_DEVOPS_ORGANIZATION.lower())
                mock_get_credentials.assert_called_once()

    def test_get_connection_cache_works_mulitple_organization(self):
        with patch('azext_devops.dev.common.services._get_credentials') as mock_get_credentials:  
            with patch('azext_devops.dev.common.telemetry.try_send_telemetry_data') as mock_telemetry_send:
                get_connection(self._TEST_DEVOPS_ORGANIZATION)
                get_connection(self._TEST_DEVOPS_ORGANIZATION2)
                #assert
                self.assertEqual(2, mock_get_credentials.call_count)
                self.assertEqual(2, mock_telemetry_send.call_count)

    def test_resolve_instance_project_and_repo(self):
        try:
            resolve_instance_project_and_repo(detect='false',
                                              organization='',
                                              project='',
                                              project_required=False,
                                              repo=None,
                                              repo_required=True)
            self.fail('we should have received an error')
        except CLIError as ex:
            self.assertEqual(str(ex), '--repository must be specified')


if __name__ == '__main__':
    unittest.main()