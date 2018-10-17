# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_dev.dev.common.uuid import is_uuid


class TestUuidMethods(unittest.TestCase):

    def test_is_uuid(self):
        # upper
        self.assertEqual(is_uuid('C9B24FCD-B879-4E79-A3A2-17C3710BEE00'), True)
        # mixed case
        self.assertEqual(is_uuid('c9B24FCD-B879-4E79-A3A2-17C3710BEE00'), True)
        # no dashes
        self.assertEqual(is_uuid('c9B24FCDB8794E79A3A217C3710BEE00'), False)
        # empty string
        self.assertEqual(is_uuid(''), False)
        # invalid digit
        self.assertEqual(is_uuid('C9G24FCD-B879-4E79-A3A2-17C3710BEE00'), False)
        # one less digit
        self.assertEqual(is_uuid('C9G24FCD-B879-4E79-A3A2-17C3710BEE0'), False)
        # one more digit
        self.assertEqual(is_uuid('C9G24FCD-B879-4E79-A3A2-17C3710BEE0'), False)


if __name__ == '__main__':
    unittest.main()