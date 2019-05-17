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

        

        # test_work_item_id = 1

        # # set return values
        # self.mock_get_WI.return_value.id = test_work_item_id

        # response = show_work_item(id=test_work_item_id, organization=self._TEST_DEVOPS_ORGANIZATION)

        # # assert
        # self.mock_validate_token.assert_not_called()
        # self.mock_get_WI.assert_called_once_with(test_work_item_id, expand='All')
        # assert response.id == test_work_item_id