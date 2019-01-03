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
from azext_devops.dev.repos.ref import (list_refs, create_ref, delete_ref, update_ref)
from azext_devops.test.utilities.helper import DEVOPS_CLI_TEST_ORGANIZATION


class TestRefMethods(unittest.TestCase):

    def setUp(self):
        self.list_refs_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_refs')
        self.update_ref_patcher = patch('vsts.git.v4_0.git_client.GitClient.update_refs')

        # start the patchers
        self.mock_list_refs = self.list_refs_patcher.start()
        self.mock_update_ref = self.update_ref_patcher.start()

        # clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        self.mock_list_refs.stop()
        self.mock_update_ref.stop()

    def test_list_refs(self):
        response = list_refs(devops_organization=DEVOPS_CLI_TEST_ORGANIZATION,
                             project='sample project',
                             detect='off')
        # assert
        self.mock_list_refs.assert_called_once()

    def test_create_ref(self):
        response = create_ref(name='sample_ref',
                              object_id='1234567890',
                              devops_organization=DEVOPS_CLI_TEST_ORGANIZATION,
                              project='sample project',
                              detect='off')
        # assert
        self.mock_update_ref.assert_called_once()

    def test_update_ref(self):
        response = update_ref(name='sample_ref',
                              old_object_id='1234567890',
                              new_object_id='0987654321',
                              devops_organization=DEVOPS_CLI_TEST_ORGANIZATION,
                              project='sample project',
                              detect='off')
        # assert
        self.mock_update_ref.assert_called_once()

    def test_delete_ref(self):
        response = delete_ref(name='sample_ref',
                              object_id='1234567890',
                              devops_organization=DEVOPS_CLI_TEST_ORGANIZATION,
                              project='sample project',
                              detect='off')
        # assert
        self.mock_update_ref.assert_called_once()

if __name__ == '__main__':
    unittest.main()
