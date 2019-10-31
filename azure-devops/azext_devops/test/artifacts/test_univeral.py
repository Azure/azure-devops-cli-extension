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

from azext_devops.dev.artifacts.universal import (publish_package,
                                                 download_package)
from azext_devops.dev.common.artifacttool import ArtifactToolInvoker
from azext_devops.dev.common.const import ARTIFACTTOOL_PAT_ENVKEY
from azext_devops.dev.common.services import clear_connection_cache



class TestUniversalPackages(unittest.TestCase):

    _CONST_ORGANIZATION_SCOPE = 'organization'
    _CONST_PROJECT_SCOPE = 'project'
    _TEST_DEVOPS_ORGANIZATION = 'https://someorg.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'my-test-project'
    _TEST_PAT_TOKEN = 'somepattoken'
    _TEST_FEED_NAME = 'my-test-feed'
    _TEST_PACKAGE_NAME = 'my-test-package'
    _TEST_PACKAGE_VERSION = '0.0.1-preview'
    _TEST_PACKAGE_DESCRIPTION = 'test description'
    _TEST_PATH = '.'
    _TEST_FILTER = '*'

    def setUp(self):

        self.run_artifacttool = patch('azext_devops.dev.common.artifacttool.ArtifactToolInvoker.run_artifacttool')

        #start the patchers
        self.mock_run_artifacttool = self.run_artifacttool.start()
        
        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        patch.stopall()


    def test_publish_package(self):
        response = publish_package(feed = self._TEST_FEED_NAME,
            name = self._TEST_PACKAGE_NAME,
            version = self._TEST_PACKAGE_VERSION,
            description = self._TEST_PACKAGE_DESCRIPTION,
            path = self._TEST_PATH,
            organization = self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'universal', 'publish',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                 '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                 '--feed', self._TEST_FEED_NAME,
                 '--package-name', self._TEST_PACKAGE_NAME,
                 '--package-version', self._TEST_PACKAGE_VERSION,
                 '--path', self._TEST_PATH,
                 '--description', self._TEST_PACKAGE_DESCRIPTION
            ],
            'Publishing')

    def test_publish_package_with_project(self):
        response = publish_package(feed = self._TEST_FEED_NAME,
            name = self._TEST_PACKAGE_NAME,
            version = self._TEST_PACKAGE_VERSION,
            description = self._TEST_PACKAGE_DESCRIPTION,
            path = self._TEST_PATH,
            organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            scope = self._CONST_PROJECT_SCOPE)

        # assert
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'universal', 'publish',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                 '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                 '--feed', self._TEST_FEED_NAME,
                 '--package-name', self._TEST_PACKAGE_NAME,
                 '--package-version', self._TEST_PACKAGE_VERSION,
                 '--path', self._TEST_PATH,
                 '--project', self._TEST_DEVOPS_PROJECT,
                 '--description', self._TEST_PACKAGE_DESCRIPTION,
            ],
            'Publishing')
        
    def test_download_package(self):
        response = download_package(feed = self._TEST_FEED_NAME,
            name = self._TEST_PACKAGE_NAME,
            version = self._TEST_PACKAGE_VERSION,
            path = self._TEST_PATH,
            file_filter= self._TEST_FILTER,
            organization = self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'universal', 'download',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                    '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                    '--feed', self._TEST_FEED_NAME,
                    '--package-name', self._TEST_PACKAGE_NAME,
                    '--package-version', self._TEST_PACKAGE_VERSION,
                    '--path', self._TEST_PATH,
                    '--filter', self._TEST_FILTER,
            ],
            'Downloading')

    def test_download_package_with_project(self):
        response = download_package(feed = self._TEST_FEED_NAME,
            name = self._TEST_PACKAGE_NAME,
            version = self._TEST_PACKAGE_VERSION,
            path = self._TEST_PATH,
            file_filter= self._TEST_FILTER,
            organization = self._TEST_DEVOPS_ORGANIZATION,
            project = self._TEST_DEVOPS_PROJECT,
            scope = self._CONST_PROJECT_SCOPE)

        # assert
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'universal', 'download',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                    '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                    '--feed', self._TEST_FEED_NAME,
                    '--package-name', self._TEST_PACKAGE_NAME,
                    '--package-version', self._TEST_PACKAGE_VERSION,
                    '--path', self._TEST_PATH,
                    '--project', self._TEST_DEVOPS_PROJECT,
                    '--filter', self._TEST_FILTER,
            ],
            'Downloading')
                