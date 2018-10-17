# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_dev.dev.common.configure import (print_current_configuration)


class TestConfigureMethods(unittest.TestCase):

    def test_print_current_configuration(self):
        # simple validation that we don't get an exception
        print_current_configuration()


if __name__ == '__main__':
    unittest.main()