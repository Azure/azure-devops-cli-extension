# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import unittest
from azext_devops.dev.common.arguments import should_detect, convert_date_string_to_iso8601


class TestArgumentsMethods(unittest.TestCase):

    def test_should_detect(self):
        # tests default behaviour for detect
        self.assertEqual(should_detect(None), True)


class TestConvertDateStringToIso8601(unittest.TestCase):

    def _assert_valid(self, input_value, expected_substring=None):
        result = convert_date_string_to_iso8601(input_value)
        self.assertIsInstance(result, str, 'Expected string, got {}'.format(type(result)))
        # Must be JSON-serializable as a string field
        json.dumps({'date': result})
        if expected_substring:
            self.assertIn(expected_substring, result)
        return result

    # --- timezone-aware inputs (the original bug) ---

    def test_utc_z_suffix(self):
        result = self._assert_valid('2026-03-24T20:55:00Z', '2026-03-24T20:55:00')
        self.assertIn('+00:00', result)

    def test_utc_explicit_offset(self):
        result = self._assert_valid('2026-03-24T20:55:00+00:00', '2026-03-24T20:55:00')
        self.assertIn('+00:00', result)

    def test_negative_offset(self):
        result = self._assert_valid('2026-03-24T20:55:00-07:00')
        self.assertIn('-07:00', result)

    def test_positive_offset(self):
        result = self._assert_valid('2026-03-24T20:55:00+05:30')
        self.assertIn('+05:30', result)

    def test_milliseconds_with_z(self):
        result = self._assert_valid('2026-03-24T20:55:00.000Z')
        self.assertIn('+00:00', result)

    # --- timezone-naive inputs (should get local tz applied) ---

    def test_naive_datetime(self):
        self._assert_valid('2026-03-24T20:55:00')

    def test_date_only(self):
        result = self._assert_valid('2026-03-24')
        self.assertIn('2026-03-24T00:00:00', result)

    def test_human_readable_date(self):
        result = self._assert_valid('March 24, 2026')
        self.assertIn('2026-03-24', result)

    def test_slash_date(self):
        result = self._assert_valid('03/24/2026')
        self.assertIn('2026-03-24', result)

    # --- invalid inputs ---

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            convert_date_string_to_iso8601('')

    def test_whitespace_raises(self):
        with self.assertRaises(ValueError):
            convert_date_string_to_iso8601('   ')

    def test_garbage_string_raises(self):
        with self.assertRaises(ValueError):
            convert_date_string_to_iso8601('not-a-date')

    def test_null_string_raises(self):
        with self.assertRaises(ValueError):
            convert_date_string_to_iso8601('null')

    def test_none_raises(self):
        with self.assertRaises((ValueError, TypeError)):
            convert_date_string_to_iso8601(None)

    # --- argument name in error message ---

    def test_error_includes_argument_name(self):
        with self.assertRaises(ValueError) as ctx:
            convert_date_string_to_iso8601('bad', argument='scheduled-cutover-date')
        self.assertIn('scheduled-cutover-date', str(ctx.exception))

    def test_error_without_argument_name(self):
        with self.assertRaises(ValueError) as ctx:
            convert_date_string_to_iso8601('bad')
        self.assertIn('bad', str(ctx.exception))

    # --- JSON payload round-trip (simulates what _send_request does) ---

    def test_json_payload_roundtrip(self):
        result = convert_date_string_to_iso8601('2026-03-24T20:55:00Z')
        payload = {'scheduledCutoverDate': result}
        serialized = json.dumps(payload)
        deserialized = json.loads(serialized)
        self.assertEqual(deserialized['scheduledCutoverDate'], result)


if __name__ == '__main__':
    unittest.main()