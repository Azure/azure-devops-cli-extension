# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import sys
import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azure.cli import __main__ as cli_main

class Test_ThreeStateFlagTests(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = TEST_DEVOPS_ORG_URL
    _TEST_PAT_TOKEN = 'somepat'

    def setUp(self):
        self.list_banner_patcher = patch('azext_devops.dev.admin.banner.banner_list')

        #start the patchers
        self.mock_list_banner = self.list_banner_patcher.start()


    def tearDown(self):
        patch.stopall()


    def test_pure_switch(self):
        try:
            sys.exit(cli_main(["devops","admin","banner","list"]))
        except:
            print("something wrong in az cli")

        self.mock_list_banner.assert_called_once_with(organization=None, detect=None)