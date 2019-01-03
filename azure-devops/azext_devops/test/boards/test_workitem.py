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

from azext_devops.dev.boards.work_item import (delete_work_item,
                                            show_work_item)
from azext_devops.dev.common.services import clear_connection_cache



class TestWorkItemMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://azuredevopsclitest.visualstudio.com'
    _TEST_PAT_TOKEN = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'

    def setUp(self):

        self.get_WI_patcher = patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.get_work_item')
        self.create_WI_patcher = patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.create_work_item')
        self.delete_WI_patcher = patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.delete_work_item')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')
        self.open_in_browser_patcher = patch('azext_devops.dev.boards.work_item._open_work_item')
        self.validate_token_patcher = patch('azext_devops.dev.common.services.validate_token_for_instance')

        #start the patchers
        self.mock_get_WI = self.get_WI_patcher.start()
        self.mock_create_WI = self. create_WI_patcher.start()
        self.mock_delete_WI = self.delete_WI_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()
        self.mock_validate_token = self.validate_token_patcher.start()
        self.mock_open_browser = self.open_in_browser_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        self.mock_get_WI.stop()
        self.mock_create_WI.stop()
        self.mock_delete_WI.stop()
        self.mock_get_credential.stop()
        self.mock_validate_token.stop()
        self.mock_open_browser.stop()


    def test_show_work_item_correct_id(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(work_item_id=test_work_item_id, devops_organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_credential.assert_called_with(self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(self.mock_get_credential.call_count, 2)
        self.mock_get_WI.assert_called_once_with(test_work_item_id)
        assert response.id == test_work_item_id


    def test_show_work_item_correct_id_open_browser(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(work_item_id=test_work_item_id, open_browser=True, devops_organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_open_browser.assert_called_with(response,self._TEST_DEVOPS_ORGANIZATION)
        self.mock_validate_token.assert_not_called()
        self.mock_get_credential.assert_called_with(self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(self.mock_get_credential.call_count, 2)
        self.mock_get_WI.assert_called_once_with(test_work_item_id)


    def test_show_work_item_raises_exception_invalid_id(self):

        test_work_item_id = 1000

        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True
        self.mock_get_WI.side_effect = Exception(r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        with self.assertRaises(Exception) as exc:
            response = show_work_item(work_item_id=test_work_item_id, devops_organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(str(exc.exception),r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        #assert
        self.mock_get_WI.assert_called_once_with(test_work_item_id)
        self.mock_validate_token.assert_not_called()
        self.mock_get_credential.assert_called_with(self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(self.mock_get_credential.call_count, 2)


    def test_delete_work_item_correct_id(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True
        self.mock_delete_WI.return_value.id = test_work_item_id

        response = delete_work_item(work_item_id=test_work_item_id, destroy=False, devops_organization=self._TEST_DEVOPS_ORGANIZATION, detect='Off')

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_credential.assert_called_with(self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(self.mock_get_credential.call_count, 2)
        self.mock_delete_WI.assert_called_once_with(test_work_item_id, False)
        assert response.id == test_work_item_id


    def test_delete_work_item_raises_exception_invalid_id(self):

        test_work_item_id = 1000

        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True
        self.mock_delete_WI.side_effect = Exception(r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        with self.assertRaises(Exception) as exc:
            response = delete_work_item(work_item_id=test_work_item_id, devops_organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(str(exc.exception),r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        self.mock_delete_WI.assert_called_once_with(test_work_item_id,False)
        self.mock_validate_token.assert_not_called()
        self.mock_get_credential.assert_called_with(self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(self.mock_get_credential.call_count, 2)


if __name__ == '__main__':
    unittest.main()