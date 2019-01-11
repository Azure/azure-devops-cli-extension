# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

class TestPipHelperMethods(unittest.TestCase):

    def test_run_pip_is_present_in_cli_core(self):
        try:
            from azure.cli.core.extension.operations import _run_pip
        except ImportError:
            self.fail('dependency on cli core is broken, pip helper will need fix')


if __name__ == '__main__':
    unittest.main()