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
    def __init__(self, flags, install_state=None):
        self.flags = flags
        self.install_state = install_state
    
class TestExtensionMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _EXT_MGMT_CLIENT_LOCATION = 'azext_devops.vstsCompressed.extension_management.v4_1.extension_management_client.ExtensionManagementClient.'

    def setUp(self):
        self.get_client = patch('azext_devops.vstsCompressed.vss_connection.VssConnection.get_client')
        self.get_installed_extensions_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'get_installed_extensions')
        self.get_installed_extension_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'get_installed_extension_by_name')
        self.install_extension_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'install_extension_by_name')
        self.uninstall_extension_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'uninstall_extension_by_name')
        self.update_installed_extension_patcher = patch(self._EXT_MGMT_CLIENT_LOCATION + 'update_installed_extension')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')

        #start the patcher
        self.mock_get_client = self.get_client.start()
        self.mock_get_installed_extensions = self.get_installed_extensions_patcher.start()
        self.mock_get_installed_extension = self.get_installed_extension_patcher.start()
        self.mock_install_extension = self.install_extension_patcher.start()
        self.mock_uninstall_extension = self.uninstall_extension_patcher.start()
        self.mock_update_installed_extension = self.update_installed_extension_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()

        #set return values
        self.mock_get_client.return_value = ExtensionManagementClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        self.get_client.stop()
        self.get_installed_extensions_patcher.stop()
        self.get_installed_extension_patcher.stop()
        self.install_extension_patcher.stop()
        self.uninstall_extension_patcher.stop()
        self.update_installed_extension_patcher.stop()
        self.get_credential_patcher.stop()
        

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

    def test_list_extension_not_include_builtin_extension(self):
        extensions = []
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('builtIn, installed'))
        extensions.append(MockInstalledExtension('installed'))

        self.mock_get_installed_extensions.return_value = extensions

        result = list_extensions('false','true',self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.assertEqual(len(result), 1)

    def test_get_extension(self):
        get_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_get_installed_extension.assert_called_once_with(publisher_name='ms', extension_name='code-search')

    def test_install_extension(self):
        install_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_install_extension.assert_called_once_with(publisher_name='ms', extension_name='code-search')
        
    def test_uninstall_extension(self):
        uninstall_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_uninstall_extension.assert_called_once_with(publisher_name='ms', extension_name='code-search')

    def test_enable_extension(self):
        extension = MockInstalledExtension('builtIn', MockInstalledExtension('disabled , buildIn , multiVersion'))
        self.mock_get_installed_extension.return_value = extension

        enable_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_update_installed_extension.assert_called_once()
        udpate_extension_object = self.mock_update_installed_extension.call_args_list[0][0]
        install_state_flags = udpate_extension_object[0].install_state.flags
        self.assertEqual('buildIn, multiVersion', install_state_flags)

    def test_enable_extension_disabled_not_first(self):
        extension = MockInstalledExtension('builtIn', MockInstalledExtension('buildIn , multiVersion , disabled'))
        self.mock_get_installed_extension.return_value = extension

        enable_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_update_installed_extension.assert_called_once()
        udpate_extension_object = self.mock_update_installed_extension.call_args_list[0][0]
        install_state_flags = udpate_extension_object[0].install_state.flags
        self.assertEqual('buildIn, multiVersion', install_state_flags)


    def test_disable_extension(self):
        extension = MockInstalledExtension('builtIn', MockInstalledExtension('buildIn, multiVersion'))
        self.mock_get_installed_extension.return_value = extension

        disable_extension('ms', 'code-search', self._TEST_DEVOPS_ORGANIZATION, 'off')

        self.mock_update_installed_extension.assert_called_once()
        udpate_extension_object = self.mock_update_installed_extension.call_args_list[0][0]
        install_state_flags = udpate_extension_object[0].install_state.flags
        self.assertEqual('buildIn, multiVersion, disabled', install_state_flags)

if __name__ == '__main__':
    unittest.main()