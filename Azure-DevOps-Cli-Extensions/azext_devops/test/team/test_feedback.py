# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.team.feedback import feedback


class TestFeedbackMethods(unittest.TestCase):

    def test_feedback(self):
        # simply validate that we don;t get any exceptions
        feedback()


if __name__ == '__main__':
    unittest.main()