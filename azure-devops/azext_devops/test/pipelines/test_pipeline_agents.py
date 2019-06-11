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

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests


class TestPipelinesRunsArtifactsMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'MyProject'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client')

        #start the patchers
        self.mock_get_artifacts = self.get_artifacts_patcher.start()

        # Set return values which will be same across tests
        self.mock_get_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_runs_artifacts_list(self):
        # set return values
        response = run_artifact_list(run_id=12345, organization=self._TEST_DEVOPS_ORGANIZATION, 
            project=self._TEST_DEVOPS_PROJECT, detect=None)
        #assert
        self.mock_get_artifacts.assert_called_once_with(build_id=12345, project=self._TEST_DEVOPS_PROJECT)
