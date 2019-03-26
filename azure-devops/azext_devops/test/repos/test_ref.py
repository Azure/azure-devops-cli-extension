# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch, ANY
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch, ANY

from azext_devops.vstsCompressed.git.v4_0.git_client import GitClient
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.dev.repos.ref import (list_refs, create_ref, delete_ref, lock_ref, unlock_ref)
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.test.utils.helper import get_client_mock_helper, TEST_DEVOPS_ORG_URL


class TestRefMethods(AuthenticatedTests):

    def setUp(self):
        self.authentication_setUp()

        self.get_refs_patcher = patch('azext_devops.vstsCompressed.git.v4_0.git_client.GitClient.get_refs')
        self.update_ref_patcher = patch('azext_devops.vstsCompressed.git.v4_0.git_client.GitClient.update_ref')
        self.update_refs_patcher = patch('azext_devops.vstsCompressed.git.v4_0.git_client.GitClient.update_refs')

        self.mock_get_refs = self.get_refs_patcher.start()
        self.mock_update_ref = self.update_ref_patcher.start()
        self.mock_update_refs = self.update_refs_patcher.start()

        # Setup mocks for clients
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client', new=get_client_mock_helper)
        self.mock_get_client = self.get_client.start()

        # clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_refs(self):
        self.authenticate()

        response = list_refs(organization=TEST_DEVOPS_ORG_URL,
                             project='sample_project',
                             detect='off')
        # assert
        self.mock_get_refs.assert_called_once_with(filter=None,
                                                   project='sample_project',
                                                   repository_id=None)

    def test_create_ref(self):
        self.authenticate()

        response = create_ref(name='sample_ref',
                              object_id='1234567890',
                              organization=TEST_DEVOPS_ORG_URL,
                              project='sample_project',
                              detect='off')
        # assert
        self.mock_update_refs.assert_called_once_with(project='sample_project',
                                                      ref_updates=ANY,
                                                      repository_id=None)

    def test_lock_ref(self):
        self.authenticate()

        response = lock_ref(name='sample_ref',
                            organization=TEST_DEVOPS_ORG_URL,
                            project='sample_project',
                            detect='off')
        # assert
        self.mock_update_ref.assert_called_once_with(project='sample_project',
                                                     new_ref_info=ANY,
                                                     filter='sample_ref',
                                                     repository_id=None)

    def test_unlock_ref(self):
        self.authenticate()

        response = unlock_ref(name='sample_ref',
                              organization=TEST_DEVOPS_ORG_URL,
                              project='sample_project',
                              detect='off')
        # assert
        self.mock_update_ref.assert_called_once_with(project='sample_project',
                                                     new_ref_info=ANY,
                                                     filter='sample_ref',
                                                     repository_id=None)

    def test_delete_ref(self):
        self.authenticate()

        response = delete_ref(name='sample_ref',
                              object_id='1234567890',
                              organization=TEST_DEVOPS_ORG_URL,
                              project='sample_project',
                              detect='off')
        # assert
        self.mock_update_refs.assert_called_once_with(project='sample_project',
                                                      ref_updates=ANY,
                                                      repository_id=None)


if __name__ == '__main__':
    unittest.main()
