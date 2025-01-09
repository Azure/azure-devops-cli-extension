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

from azext_devops.dev.team.credentials import credential_set, credential_clear

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests

class TestLoginLogoutMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_TOKEN = "RandomToken"
    
    def setUp(self):
        self.authentication_setup()
        self.set_credential_patcher = patch('azext_devops.dev.team.credentials.set_credential')
        self.mock_set_credential = self.set_credential_patcher.start()

        self.clear_credential_patcher = patch('azext_devops.dev.team.credentials.clear_credential')
        self.mock_clear_credential = self.clear_credential_patcher.start()

        self.get_pat_token_patcher = patch('azext_devops.dev.team.credentials._get_pat_token')
        self.mock_get_token = self.get_pat_token_patcher.start()
        
        self.get_verify_token_patcher = patch('azext_devops.dev.team.credentials._verify_token')
        self.mock_verify_token = self.get_verify_token_patcher.start()

        self.get_update_default_config_patcher = patch('azext_devops.dev.team.credentials._check_and_set_default_organization')
        self.mock_update_config = self.get_update_default_config_patcher.start()

        self.get_clear_default_config_patcher = patch('azext_devops.dev.team.credentials._check_and_clear_default_organization')
        self.mock_clear_config = self.get_clear_default_config_patcher.start()

        self.mock_get_token.return_value = self._TEST_TOKEN
        
        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()
        
    def test_login_with_org(self):
        credential_set(organization=self._TEST_DEVOPS_ORGANIZATION)
                
        #assert
        self.mock_get_token.assert_called_once()
        self.mock_verify_token.assert_called_once()
        self.mock_set_credential.assert_called_once_with(organization=self._TEST_DEVOPS_ORGANIZATION, token=self._TEST_TOKEN)
        self.mock_update_config.assert_called_once()

    def test_login_without_org(self):
        credential_set()
                
        #assert
        self.mock_get_token.assert_called_once()
        self.mock_verify_token.assert_not_called()
        self.mock_set_credential.assert_called_once_with(organization=None, token=self._TEST_TOKEN)
        self.mock_update_config.assert_called_once()

    def test_logout_with_org(self):
        credential_clear(organization=self._TEST_DEVOPS_ORGANIZATION)
        # assert
        self.mock_clear_credential.assert_called_once_with(self._TEST_DEVOPS_ORGANIZATION)
        self.mock_clear_config.assert_called_once()

    def test_logout_without_org(self):
        credential_clear()
        # assert
        self.mock_clear_credential.assert_called_once_with(None)
        self.mock_clear_config.assert_called_once()

if __name__ == '__main__':
    unittest.main()