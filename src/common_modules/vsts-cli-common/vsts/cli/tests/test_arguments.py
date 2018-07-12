# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from ..common.arguments import (resolve_on_off_switch,
                                should_detect)


class TestArgumentsMethods(unittest.TestCase):

    def test_resolve_on_off_switch(self):
        self.assertEqual(resolve_on_off_switch("on"), True)
        self.assertEqual(resolve_on_off_switch("off"), False)

        with self.assertRaises(ValueError):
            resolve_on_off_switch(None)
        with self.assertRaises(ValueError):
            resolve_on_off_switch('')
        with self.assertRaises(ValueError):
            resolve_on_off_switch('foo')
        with self.assertRaises(ValueError):
            resolve_on_off_switch('ON')
        with self.assertRaises(ValueError):
            resolve_on_off_switch('OOF')

    def test_should_detect(self):
        # tests default behaviour for detect
        self.assertEqual(should_detect(None), True)


if __name__ == '__main__':
    unittest.main()
