# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch, ANY
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch, ANY

from knack.util import CLIError
from azext_devops.dev.boards.work_item_tags import (add_work_item_tags,
                                                    list_work_item_tags,
                                                    remove_work_item_tags,
                                                    _remove_tag_from_tagstring)
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.helper import get_client_mock_helper, TEST_DEVOPS_ORG_URL
from azext_devops.test.utils.authentication import AuthenticatedTests


class TestWorkItemTagMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = TEST_DEVOPS_ORG_URL
    _TEST_PAT_TOKEN = 'somepat'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.get_work_item')
        self.create_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.create_work_item')
        self.update_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.update_work_item')
        self.delete_WI_patcher = patch('azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.delete_work_item')
        self.open_in_browser_patcher = patch('azext_devops.dev.boards.work_item._open_work_item')

        # patch get client so no network call is made
        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)
        self.get_client_patcher.start()

        #start the patchers
        self.mock_get_WI = self.get_WI_patcher.start()
        self.mock_create_WI = self.create_WI_patcher.start()
        self.mock_update_WI = self.update_WI_patcher.start()
        self.mock_delete_WI = self.delete_WI_patcher.start()
        self.mock_open_browser = self.open_in_browser_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        patch.stopall()


    def test_add_work_item_tag_correct_id(self):

        test_work_item_id = 1
        test_work_item_new_tag = "newtag"

        # set return values
        self.mock_update_WI.return_value.id = test_work_item_id
        self.mock_update_WI.return_value.fields = { "System.Tags": test_work_item_new_tag }

        response = add_work_item_tags(id=test_work_item_id, tag=test_work_item_new_tag, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_update_WI.assert_called_once_with(document=ANY, id=test_work_item_id)
        args, kwargs = self.mock_update_WI.call_args
        self.assertEqual(response.id, test_work_item_id)
        #assert expected patch document
        actual_patch_document = kwargs.get('document')[0]
        self.assertEqual("add", actual_patch_document.op)
        self.assertEqual("/fields/System.Tags", actual_patch_document.path)
        self.assertEqual(test_work_item_new_tag, actual_patch_document.value)


    def test_add_work_item_tag_none_id(self):

        test_work_item_id = None
        test_work_item_new_tag = "newtag"

        with self.assertRaises(CLIError) as exc:
            add_work_item_tags(id=test_work_item_id, tag=test_work_item_new_tag, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn('--id must be provided', str(exc.exception))


    def test_add_work_item_tag_none_tag(self):

        test_work_item_id = 1
        test_work_item_new_tag = None

        with self.assertRaises(CLIError) as exc:
            add_work_item_tags(id=test_work_item_id, tag=test_work_item_new_tag, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn('--tag must be provided', str(exc.exception))


    def test_list_work_item_tag_correct_id(self):

        test_work_item_id = 1
        
        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id
        self.mock_get_WI.return_value.fields = { "System.Tags": "mytag" }
        response = list_work_item_tags(id=test_work_item_id, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id, as_of=None, fields=['System.Id','System.Tags'], expand=None)
        self.assertEqual(response.id, test_work_item_id)
        self.assertEqual(response.fields['System.Tags'], "mytag")


    def test_list_work_item_tag_none_id(self):

        test_work_item_id = None

        with self.assertRaises(CLIError) as exc:
            list_work_item_tags(id=test_work_item_id, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn('--id must be provided', str(exc.exception))


    def test_remove_work_item_tag(self):

        test_work_item_id = 1
        test_work_item_tag_to_remove = "mytag"
        expected_system_tags_value = ""
        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id
        self.mock_get_WI.return_value.fields = { "System.Tags": test_work_item_tag_to_remove }
        self.mock_update_WI.return_value.id = test_work_item_id
        self.mock_update_WI.return_value.fields = { "System.Id": test_work_item_id }

        response = remove_work_item_tags(id=test_work_item_id, tag=test_work_item_tag_to_remove, organization=self._TEST_DEVOPS_ORGANIZATION)

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_get_WI.assert_called_once_with(test_work_item_id, as_of=None, fields=['System.Id','System.Tags'], expand=None)
        self.mock_update_WI.assert_called_once_with(document=ANY, id=test_work_item_id)
        args, kwargs = self.mock_update_WI.call_args
        self.assertEqual(response.id, test_work_item_id)
        self.assertEqual('System.Tags' in response.fields, False)
        #assert expected patch document
        actual_patch_document = kwargs.get('document')[0]
        self.assertEqual("replace", actual_patch_document.op)
        self.assertEqual("/fields/System.Tags", actual_patch_document.path)
        self.assertEqual(expected_system_tags_value, actual_patch_document.value)


    def test_remove_work_item_nonexistent_tag_from_workitem_with_tags(self):

        test_work_item_id = 1
        test_work_item_tag_to_remove = "mytag"

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id
        self.mock_get_WI.return_value.fields = { "System.Tags": "other_tag" }
        self.mock_update_WI.return_value.id = test_work_item_id
        self.mock_update_WI.return_value.fields = { "System.Tags": "other_tag" }

        with self.assertRaises(CLIError) as exc:
            remove_work_item_tags(id=test_work_item_id, tag=test_work_item_tag_to_remove, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn(f'Work item tag {test_work_item_tag_to_remove} was not found on work item with id {test_work_item_id}.', str(exc.exception))


    def test_remove_work_item_tag_when_no_tags_exist(self):

        test_work_item_id = 1
        test_work_item_tag_to_remove = "mytag"

        # set return values
        self.mock_get_WI.return_value.id = test_work_item_id
        self.mock_get_WI.return_value.fields = { "System.Id": test_work_item_id }
        self.mock_update_WI.return_value.id = test_work_item_id
        self.mock_update_WI.return_value.fields = { "System.Id": test_work_item_id }

        with self.assertRaises(CLIError) as exc:
            remove_work_item_tags(id=test_work_item_id, tag=test_work_item_tag_to_remove, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn(f'Work item with id {test_work_item_id} has no tags.', str(exc.exception))


    def test_remove_work_item_tag_none_id(self):

        test_work_item_id = None
        test_work_item_new_tag = "newtag"

        with self.assertRaises(CLIError) as exc:
            remove_work_item_tags(id=test_work_item_id, tag=test_work_item_new_tag, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn('--id must be provided', str(exc.exception))


    def test_remove_work_item_tag_none_tag(self):

        test_work_item_id = 1
        test_work_item_new_tag = None

        with self.assertRaises(CLIError) as exc:
            remove_work_item_tags(id=test_work_item_id, tag=test_work_item_new_tag, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertIn('--tag must be provided', str(exc.exception))


    def test_remove_first_tag_from_tagstring(self):
        current_tags = "tag1; tag2; tag3"
        tag_to_remove = "tag1"
        expected_result = "tag2; tag3"

        actual = _remove_tag_from_tagstring(current_tags, tag_to_remove)

        self.assertEqual(expected_result, actual)


    def test_remove_last_tag_from_tagstring(self):
        current_tags = "tag1; tag2; tag3"
        tag_to_remove = "tag3"
        expected_result = "tag1; tag2"

        actual = _remove_tag_from_tagstring(current_tags, tag_to_remove)

        self.assertEqual(expected_result, actual)


    def test_remove_only_tag_from_tagstring(self):
        current_tags = "tag1"
        tag_to_remove = "tag1"
        expected_result = ""

        actual = _remove_tag_from_tagstring(current_tags, tag_to_remove)

        self.assertEqual(expected_result, actual)


    def test_remove_tag_from_tagstring(self):
        current_tags = "tag1; tag2; tag3"
        tag_to_remove = "tag2"
        expected_result = "tag1; tag3"

        actual = _remove_tag_from_tagstring(current_tags, tag_to_remove)

        self.assertEqual(expected_result, actual)


if __name__ == '__main__':
    unittest.main()
