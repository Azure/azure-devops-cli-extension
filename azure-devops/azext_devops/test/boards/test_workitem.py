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
from azext_devops.test.utils.helper import get_client_mock_helper, TEST_DEVOPS_ORG_URL
from azext_devops.test.utils.authentication import AuthenticatedTests


class TestWorkItemMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = TEST_DEVOPS_ORG_URL
    _TEST_PAT_TOKEN = 'somepat'
    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.get_work_item')
        self.create_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.create_work_item')
        self.delete_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.delete_work_item')
        self.open_in_browser_patcher = patch('azext_devops.dev.boards.work_item._open_work_item')

        # patch get client so no network call is made
        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)
        self.get_client_patcher.start()

        #start the patchers
        self.mock_get_WI = self.get_WI_patcher.start()
        self.mock_create_WI = self. create_WI_patcher.start()
        self.mock_delete_WI = self.delete_WI_patcher.start()
        self.mock_open_browser = self.open_in_browser_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        patch.stopall()


    def test_show_work_item_correct_id(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(id=test_work_item_id, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id,as_of=None, expand='all', fields=None)
        assert response.id == test_work_item_id


    def test_show_work_item_correct_id_fields(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(id=test_work_item_id, fields='System.Id,System.AreaPath', organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id, as_of=None, fields=['System.Id','System.AreaPath'] ,expand='all')
        assert response.id == test_work_item_id

    def test_show_work_item_correct_id_expand(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(id=test_work_item_id, expand='relations', organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id,as_of=None, fields=None, expand='relations')
        assert response.id == test_work_item_id

    def test_show_work_item_correct_id_as_of(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id
        as_of_date = '2019-01-01'
        response = show_work_item(id=test_work_item_id, as_of=as_of_date, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
        iso_date = convert_date_string_to_iso8601(as_of_date)
        self.mock_get_WI.assert_called_once_with(test_work_item_id,as_of=iso_date, expand='all', fields=None)
        assert response.id == test_work_item_id

    def test_show_work_item_correct_id_open_browser(self):

        test_work_item_id = 1

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id

        response = show_work_item(id=test_work_item_id, open=True, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_open_browser.assert_called_with(response,self._TEST_DEVOPS_ORGANIZATION)
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id, as_of=None, expand='all', fields=None)


    def test_show_work_item_raises_exception_invalid_id(self):

        test_work_item_id = 1000

        self.mock_get_WI.side_effect = Exception(r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        with self.assertRaises(Exception) as exc:
            response = show_work_item(id=test_work_item_id, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(str(exc.exception),r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        #assert
        self.mock_get_WI.assert_called_once_with(test_work_item_id, as_of=None, expand='all', fields=None)
        self.mock_validate_token.assert_not_called()


    def test_delete_work_item_correct_id(self):

        test_work_item_id = 1

        # set return values
        self.mock_delete_WI.return_value.id = test_work_item_id

        response = delete_work_item(id=test_work_item_id, destroy=False, project='testproject', organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_delete_WI.assert_called_once_with(id=test_work_item_id, project='testproject', destroy=False)
        assert response.id == test_work_item_id


    def test_delete_work_item_raises_exception_invalid_id(self):

        test_work_item_id = 1000

        self.mock_delete_WI.side_effect = Exception(r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        with self.assertRaises(Exception) as exc:
            response = delete_work_item(id=test_work_item_id, project='test', organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(str(exc.exception),r'TF401232: Work item 1000 does not exist, or you do not have permissions to read it.')

        self.mock_delete_WI.assert_called_once_with(id=test_work_item_id, project='test', destroy=False)
        self.mock_validate_token.assert_not_called()


if __name__ == '__main__':
    unittest.main()