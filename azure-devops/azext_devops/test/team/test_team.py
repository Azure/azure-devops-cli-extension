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
from azext_devops.dev.team.team import (create_team)

from azext_devops.dev.common.services import clear_connection_cache
from vsts.core.v4_0.core_client import CoreClient
    
class TestTeamMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
    _TEST_PROJECT_NAME = 'sample_project'

    def setUp(self):
        self.get_client = patch('vsts.vss_connection.VssConnection.get_client')
        self.create_team_patcher = patch('vsts.core.v4_0.core_client.CoreClient.create_team')

        #start the patcher
        self.mock_get_client = self.get_client.start()
        self.mock_create_team = self.create_team_patcher.start()

        #set return values
        self.mock_get_client.return_value = CoreClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        self.mock_get_client.stop()
        self.mock_create_team.stop()

    def test_create_team(self):
        response = create_team('sample name', 'sample description', self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')
        
        #assert
        self.mock_create_team.assert_called_once()


if __name__ == '__main__':
    unittest.main()