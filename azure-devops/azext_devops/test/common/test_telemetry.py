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


class TestTelemetryMethods(unittest.TestCase):
    
    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
   
    def test_send_telemetry_should_send_if_enabled(self):
        with patch('azext_devops.dev.common.telemetry._is_telemetry_enabled') as mock_telemetry_enabled:  
            mock_telemetry_enabled.return_value = True
            with patch('azext_devops.dev.common.telemetry._try_send_tracking_ci_event_async') as mock_telemetry_send:
                try_send_telemetry_data(self._TEST_DEVOPS_ORGANIZATION)
                #assert
                mock_telemetry_send.assert_called_once_with(self._TEST_DEVOPS_ORGANIZATION)


    def test_send_telemetry_should_not_send_if_disabled(self):
        with patch('azext_devops.dev.common.telemetry._is_telemetry_enabled') as mock_telemetry_enabled:  
            mock_telemetry_enabled.return_value = False
            with patch('azext_devops.dev.common.telemetry._try_send_tracking_ci_event_async') as mock_telemetry_send:
                try_send_telemetry_data(self._TEST_DEVOPS_ORGANIZATION)
                #assert
                mock_telemetry_send.assert_not_called()


    def test_set_tracking_data_should_set_data_correctly_with_command(self):
        set_tracking_data(['devops', 'project', 'list'])
        assert vsts_tracking_data.area == 'AzureDevopsCli'
        assert vsts_tracking_data.feature == 'devops'
        assert vsts_tracking_data.properties['Command'] == 'project list'


    def test_set_tracking_data_should_set_data_correctly_with_none(self):
        set_tracking_data(None)
        assert vsts_tracking_data.area == 'AzureDevopsCli'
        assert vsts_tracking_data.feature == 'Command'
        assert vsts_tracking_data.properties == {} 
