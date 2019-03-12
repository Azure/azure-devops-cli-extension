# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.common.format import trim_for_display, date_time_to_only_date


class TestFormatMethods(unittest.TestCase):

    def test_trim_for_display(self):
        input = 'Gallery extensions for Portal Extension'
        output = trim_for_display(input, 20)
        self.assertEqual(output, 'Gallery extensions f...')

        input = 'Aex platform'
        output = trim_for_display(input, 20)
        self.assertEqual(output, input)

        input = ''
        output = trim_for_display(input, 20)
        self.assertEqual(output, input)

        input = None
        output = trim_for_display(input, 20)
        self.assertEqual(output, input)

    def test_date_time_to_only_date(self):
        input = '2019-02-24T02:45:41.277000+00:00'
        output = date_time_to_only_date(input)
        self.assertEqual(output, '2019-02-24')

        input = 'Aex platform'
        output = date_time_to_only_date(input)
        self.assertEqual(output, input)


if __name__ == '__main__':
    unittest.main()