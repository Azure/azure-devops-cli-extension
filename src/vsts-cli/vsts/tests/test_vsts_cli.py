# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from ..cli.vsts_cli import VstsCLI


class TestVstsCliMethods(unittest.TestCase):

    def test_vsts_cli(self):
        vsts_cli = VstsCLI()
        vsts_cli.show_version()
        vsts_cli.invoke(args=[])


if __name__ == '__main__':
    unittest.main()
