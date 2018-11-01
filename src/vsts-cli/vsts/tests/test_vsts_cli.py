# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from ..cli.azdos_cli import AzdosCLI


class TestAzdosCliMethods(unittest.TestCase):

    def test_azdos_cli(self):
        azdos_cli = AzdosCLI()
        azdos_cli.show_version()
        azdos_cli.invoke(args=[])


if __name__ == '__main__':
    unittest.main()
