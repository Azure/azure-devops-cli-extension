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

from azext_devops.vstsCompressed.extension_management.v4_1.extension_management_client import ExtensionManagementClient
from azext_devops.dev.team.extension import  (list_extensions,
                                              get_extension,
                                              install_extension,
                                              uninstall_extension,
                                              enable_extension,
                                              disable_extension)

from azext_devops.dev.common.services import clear_connection_cache

class MockInstalledExtension(object):
    def __init__(self, flags):
        self.flags = flags
    
class TestExtensionMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _EXT_MGMT_CLIENT_LOCATION = 'azext_devops.vstsCompressed.extension_management.v4_1.extension_management_client.ExtensionManagementClient.'

    def setUp(self):
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_installed_extensions_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'get_installed_extensions')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')

        #start the patcher
        self.mock_get_client = self.get_client.start()
        self.mock_get_installed_extensions = self.get_installed_extensions_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()

        #set return values
        self.mock_get_client.return_value = ExtensionManagementClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        self.mock_get_client.stop()
        self.mock_get_installed_extensions.stop()
        self.mock_get_credential.stop()

    def test_list_extensions(self):
        list_extensions('false','false',self._TEST_DEVOPS_ORGANIZATION, 'off')
                
        #assert
        self.mock_get_installed_extensions.assert_called_once_with(include_disabled_extensions=False)

    def test_list_extensions_include_disabled_extension(self):
        list_extensions('false','true',self._TEST_DEVOPS_ORGANIZATION, 'off')
                
        #assert
        self.mock_get_installed_extensions.assert_called_once_with(include_disabled_extensions=True)

    def test_list_extension_include_builtin_extension(self):
        extensions = []
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('installed'))

        self.mock_get_installed_extensions.return_value = extensions

        result = list_extensions('true','true',self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.assertEqual(len(result), 3)

    def test_list_extension_include_builtin_extension(self):
        extensions = []
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('installed'))

        self.mock_get_installed_extensions.return_value = extensions

        result = list_extensions('false','true',self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()