# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import json

from azext_devops.dev.boards._format import (transform_work_item_tags)
from azext_devops.test.utils.authentication import AuthenticatedTests


class TestTableTransforms(unittest.TestCase):

    def test_transform_work_item_tags_correct_values(self):
        expected_id = 176
        expected_tags = "mytag"
        test_input = {}
        test_input['id'] = expected_id
        test_input['fields'] = {}
        test_input['fields']['System.Id'] = expected_id
        test_input['fields']['System.Tags'] = expected_tags
        actual = transform_work_item_tags(test_input)
        self.assertEquals(expected_id, actual['ID'])
        self.assertEquals(expected_tags, actual['Tags'])

    def test_transform_work_item_tags_correct_column_order(self):
        test_input = {}
        test_input['id'] = 1
        test_input['fields'] = {}
        test_input['fields']['System.Id'] = 1
        test_input['fields']['System.Tags'] = "tag"
        actual = transform_work_item_tags(test_input)
        self.assertEquals(2, len(actual))
        self.assertEquals('ID', list(actual.items())[0][0])
        self.assertEquals('Tags', list(actual.items())[1][0])

if __name__ == '__main__':
    unittest.main()