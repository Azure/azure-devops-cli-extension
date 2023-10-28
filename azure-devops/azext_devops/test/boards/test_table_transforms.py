# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.boards._format import (transform_work_item_tags)


class TestTableTransforms(unittest.TestCase):

    _TEST_WORK_ITEM_ID = 1
    _TEST_WORK_ITEM_TAG = "mytag"
    _TEST_TABLE_INPUT = {
        'id': _TEST_WORK_ITEM_ID,
        'fields': {
            'System.Id': _TEST_WORK_ITEM_ID,
            'System.Tags': _TEST_WORK_ITEM_TAG
        }
    }

    def test_transform_work_item_tags_correct_values(self):
        actual = transform_work_item_tags(self._TEST_TABLE_INPUT)
        self.assertEquals(self._TEST_WORK_ITEM_ID, actual['ID'])
        self.assertEquals(self._TEST_WORK_ITEM_TAG, actual['Tags'])

    def test_transform_work_item_tags_correct_column_order(self):
        actual = transform_work_item_tags(self._TEST_TABLE_INPUT)
        self.assertEquals(2, len(actual))
        self.assertEquals('ID', list(actual.keys())[0])
        self.assertEquals('Tags', list(actual.keys())[1])

if __name__ == '__main__':
    unittest.main()
