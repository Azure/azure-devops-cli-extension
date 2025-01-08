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

from azext_devops.dev.pipelines.build import (build_show)
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.devops_sdk.v5_0.build.build_client import BuildClient


class TestPipelinesBuildMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PAT_TOKEN = 'Some_PAT_Token'
    
    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client')
        self.get_build_patcher = patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.get_build')
        self.open_in_browser_patcher = patch('azext_devops.dev.pipelines.build._open_build')

        #start the patchers
        self.mock_get_build= self.get_build_patcher.start()
        self.mock_get_client = self.get_client.start()
        self.mock_open_browser = self.open_in_browser_patcher.start()

        # Set return values which will be same across tests
        self.mock_get_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_show_build(self):
        # set return values
        response = build_show(id=12345, open=False, organization=self._TEST_DEVOPS_ORGANIZATION, 
            project='testproject', detect=None)
        #assert
        self.mock_get_build.assert_called_once_with(build_id=12345, project='testproject')
        self.mock_open_browser.assert_not_called()

    def test_show_build_with_open_browser(self):
        # set return values
        self.mock_get_build.return_value = "dummy_build"
        response = build_show(id=12345, open=True, organization=self._TEST_DEVOPS_ORGANIZATION, 
            project='testproject', detect=None)
        #assert
        self.mock_get_build.assert_called_once_with(build_id=12345, project='testproject')
        self.mock_open_browser.assert_called_once_with("dummy_build", self._TEST_DEVOPS_ORGANIZATION)

    def test_show_build_with_detected_project_org(self):
        _DUMMY_INSTANCE = 'dummy_instance'
        _DUMMY_PROJECT = 'dummy_project'
        _DUMMY_BUILD = 'dummy_build'
        _DUMMY_REPO = 'dummy_repo'
        with patch('azext_devops.dev.common.services.resolve_instance_project_and_repo') as mock_resolve_instance_project_repo:
            mock_resolve_instance_project_repo.return_value = _DUMMY_INSTANCE, _DUMMY_PROJECT, _DUMMY_REPO

            # set return values
            self.mock_get_build.return_value = _DUMMY_BUILD

            response = build_show(id=12345)

            #assert
            mock_resolve_instance_project_repo.assert_called_once()
            self.mock_get_build.assert_called_once_with(build_id=12345, project=_DUMMY_PROJECT)
            self.mock_open_browser.assert_not_called()


if __name__ == '__main__':
    unittest.main()