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
from azext_devops.dev.common.const import DEFAULTS_SECTION
from azext_devops.dev.team.configure import print_current_configuration, configure
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.dev.common.services import clear_connection_cache

class TestConfigureMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'

    def setUp(self):
        self.authentication_setup()
        self.set_config_patcher = patch('azext_devops.dev.team.configure.set_global_config_value')
        self.mock_set_config = self.set_config_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_print_current_configuration(self):
        # simple validation that we don't get an exception
        print_current_configuration()
    
    def test_setting_invalid_org_url_throws_error(self):
        with self.assertRaises(Exception) as exc:
            configure(defaults=['organization=abc'])
        self.assertEqual(str(exc.exception),r'Organization should be a valid Azure DevOps or Azure DevOps Server repository url. See command help for details.')
        self.mock_set_config.assert_not_called()

    def test_setting_valid_org_url_should_work(self):
        configure(defaults=['organization={}'.format(self._TEST_DEVOPS_ORGANIZATION)])
        self.mock_set_config.assert_called_once_with(section=DEFAULTS_SECTION, option='organization', value=self._TEST_DEVOPS_ORGANIZATION)

    def test_setting_org_to_blank_should_succeed(self):
        configure(defaults=["organization="])
        self.mock_set_config.assert_called_once_with(section=DEFAULTS_SECTION, option='organization', value='')

    def test_setting_invalid_Default_key_should_fail(self):
        with self.assertRaises(Exception) as exc:
            configure(defaults=["abcd=abcd"])
        self.assertEqual(str(exc.exception), r"usage error: invalid default value setup. Supported values are ['organization', 'project'].")
        self.mock_set_config.assert_not_called()

if __name__ == '__main__':
    unittest.main()