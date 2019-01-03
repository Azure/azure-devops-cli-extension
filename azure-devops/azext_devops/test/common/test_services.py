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

from azext_devops.dev.common.telemetry import (set_tracking_data, 
    try_send_telemetry_data, vsts_tracking_data)

from azext_devops.dev.common.services import get_vss_connection

class TestServicesMethods(unittest.TestCase):
    
    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
   
    def test_get_vss_connection_cache_works(self):
        with patch('azext_devops.dev.common.services._get_credentials') as mock_get_credentials:  
            with patch('azext_devops.dev.common.telemetry.try_send_telemetry_data') as mock_telemetry_send:
                get_vss_connection(self._TEST_DEVOPS_ORGANIZATION)
                get_vss_connection(self._TEST_DEVOPS_ORGANIZATION.lower())
                #assert
                mock_telemetry_send.assert_called_once_with(self._TEST_DEVOPS_ORGANIZATION.lower())
                mock_get_credentials.assert_called_once()

