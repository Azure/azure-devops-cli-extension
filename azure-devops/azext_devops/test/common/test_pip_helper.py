# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.common.pip_helper import install_keyring

class TestPipHelperMethods(unittest.TestCase):

    def test_run_pip_is_present_in_cli_core(self):
        try:
            from azure.cli.core.extension.operations import _run_pip
        except ImportError:
            self.fail('dependency on cli core is broken, pip helper will need fix')

    def test_keyring_install_working(self):
        install_keyring()
        # uninstall keyring
        pip_args = ['uninstall', 'keyring', '-y']
        from azure.cli.core.extension.operations import _run_pip
        pip_status_code = _run_pip(pip_args)  # pylint: disable=protected-access
        if pip_status_code > 0:
            self.fail('keyring uninstall failed')

        try:
            import keyring
            self.fail('importing keyring should have failed')
        except ImportError:
            print('expected')

        # install keyring and make sure we can import that
        install_keyring()
        import keyring

if __name__ == '__main__':
    unittest.main()