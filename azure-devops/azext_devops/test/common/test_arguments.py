# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.common.arguments import (should_detect)


class TestArgumentsMethods(unittest.TestCase):

    def test_should_detect(self):
        # tests default behaviour for detect
        self.assertEqual(should_detect(None), True)


if __name__ == '__main__':
    unittest.main()