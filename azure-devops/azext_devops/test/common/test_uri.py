# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.common.uri import (uri_parse_instance_from_git_uri)


class TestUriMethods(unittest.TestCase):

    def test_uri_parse_instance_from_git_uri(self):
        # simple validation that we don't get an exception
        uri = "https://mseng@dev.azure.com/mseng/azuredevops/_git/azuredevops"
        result = uri_parse_instance_from_git_uri(uri)
        self.assertEqual(result, "https://dev.azure.com/mseng")

        uri = "https://mseng.visualstudio.com/AzureDevOps/_git/AzureDevOps"
        result = uri_parse_instance_from_git_uri(uri)
        self.assertEqual(result, "https://mseng.visualstudio.com/")

        uri = "https://mseng.visualstudio.com/"
        result = uri_parse_instance_from_git_uri(uri)
        self.assertEqual(result, "https://mseng.visualstudio.com/")


if __name__ == '__main__':
    unittest.main()