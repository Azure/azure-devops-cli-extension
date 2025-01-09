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

from knack.prompting import NoTTYException

from azext_devops.devops_sdk.v5_0.git.models import GitPullRequest, GitRepository, TeamProjectReference
from azext_devops.devops_sdk.v5_0.git.models import GitImportRequest

from azext_devops.dev.repos.import_request import create_import_request
                                            
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.tests.utils.helper import get_client_mock_helper


class TestImportRepositoryMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorg.visualstudio.com'
    _TEST_PAT_TOKEN = 'some bad token'

    def setUp(self):
        self.authentication_setup()
        self.create_import_request_patcher = patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.create_import_request')
        self.get_import_request_patcher = patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_import_request')

        #start the patchers
        self.mock_create_import_request = self.create_import_request_patcher.start()
        self.mock_get_import_request = self.get_import_request_patcher.start()

        # Setup mocks for clients
        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)
        self.mock_get_client = self.get_client.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        patch.stopall()


    def test_create_import_request_basic(self):
        fake_server_response = GitImportRequest()
        fake_server_response.status = 'completed'
        self.mock_get_import_request.return_value = fake_server_response

        response = create_import_request(git_source_url = 'random_repo_name',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        repository = 'sample repository')

        #assert
        self.mock_create_import_request.assert_called_once()

    def test_auth_error_message(self):
        try:
            response = create_import_request(git_source_url = 'random_repo_name',
            organization = self._TEST_DEVOPS_ORGANIZATION,
            requires_authorization=True,
            project = 'sample project',
            repository = 'sample repository')
            self.fail('exception was expected')
        except NoTTYException as ex:
            self.assertEqual(str(ex), 'Please specify target git password / PAT in AZURE_DEVOPS_EXT_GIT_SOURCE_PASSWORD_OR_PAT environment variable in non-interactive mode.')


if __name__ == '__main__':
    unittest.main()