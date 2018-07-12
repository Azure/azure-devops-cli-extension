# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from ..common.configure import configure


class TestConfigureMethods(unittest.TestCase):

    def test_configure(self):
        # ist config, and simply validate that we don't get any exceptions
        configure(list_config=True)


if __name__ == '__main__':
    unittest.main()
