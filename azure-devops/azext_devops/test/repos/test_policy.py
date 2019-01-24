# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.repos.policy import nameOfArray


class TestUuidMethods(unittest.TestCase):

    def test_name_of_array(self):
        first_name = 'a'
        middle_name = 'b'
        last_name = 'c'
        nameOfArrayResult = nameOfArray([first_name,middle_name,last_name])
        self.assertEqual(nameOfArrayResult, ['first_name','middle_name','last_name'])


if __name__ == '__main__':
    unittest.main()