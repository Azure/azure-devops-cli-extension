# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

from azext_devops.dev.team.invoke import apiVersionToFloat


class TestApiVersionToFloat(unittest.TestCase):

    def test_plain_version(self):
        self.assertEqual(apiVersionToFloat('7.1'), 7.1)

    def test_preview_version_without_subversion(self):
        self.assertEqual(apiVersionToFloat('7.1-preview'), 7.1)

    def test_preview_version_with_subversion(self):
        # e.g. "7.1-preview.1" - the sub-version suffix used to break float() conversion
        self.assertEqual(apiVersionToFloat('7.1-preview.1'), 7.1)

    def test_preview_version_with_multi_digit_subversion(self):
        self.assertEqual(apiVersionToFloat('5.0-preview.10'), 5.0)
