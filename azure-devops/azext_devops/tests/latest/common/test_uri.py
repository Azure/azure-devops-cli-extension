# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azext_devops.dev.common.uri import (canonicalize_azure_devops_organization_url,
                                         parse_azure_devops_git_remote,
                                         uri_parse_instance_from_git_uri)


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

    def test_parse_azure_devops_git_remote_canonicalizes_https_userinfo(self):
        result = parse_azure_devops_git_remote(
            "https://mockorg@dev.azure.com/mockorg/mockproject/_git/mockrepo")
        self.assertEqual(
            result.repository_url,
            "https://dev.azure.com/mockorg/mockproject/_git/mockrepo")

    def test_parse_azure_devops_git_remote_rejects_ambiguous_authority(self):
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://attacker.example\\@dev.azure.com/org/project/_git/repo"))
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://attacker.example%5c@dev.azure.com/org/project/_git/repo"))
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://user:password@dev.azure.com/org/project/_git/repo"))
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://user@attacker.example@dev.azure.com/org/project/_git/repo"))

    def test_parse_azure_devops_git_remote_rejects_spoofed_hosts(self):
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://dev.azure.com.evil.example/org/project/_git/repo"))
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://notvisualstudio.com/project/_git/repo"))

    def test_canonicalize_azure_devops_organization_url(self):
        self.assertEqual(
            canonicalize_azure_devops_organization_url("https://dev.azure.com/MyOrg/"),
            "https://dev.azure.com/MyOrg")
        self.assertEqual(
            canonicalize_azure_devops_organization_url("https://myorg.visualstudio.com/"),
            "https://myorg.visualstudio.com/")
        self.assertIsNone(canonicalize_azure_devops_organization_url(
            "https://dev.azure.com.evil.example/MyOrg"))

    def test_canonicalize_azure_devops_service_organization_url(self):
        service_names = ('artifacts', 'feeds', 'pkgs', 'vssps', 'extmgmt', 'auditservice')
        for service_name in service_names:
            service_url = "https://{service}.dev.azure.com/MyOrg/".format(service=service_name)
            with self.subTest(service_name=service_name):
                self.assertEqual(
                    canonicalize_azure_devops_organization_url(service_url),
                    service_url.rstrip('/'))
        self.assertIsNone(canonicalize_azure_devops_organization_url(
            "https://evil.artifacts.dev.azure.com/MyOrg"))
        self.assertIsNone(canonicalize_azure_devops_organization_url(
            "https://artifacts.dev.azure.com/MyOrg/Unexpected"))

    def test_service_organization_url_is_not_a_git_remote(self):
        self.assertIsNone(parse_azure_devops_git_remote(
            "https://artifacts.dev.azure.com/MyOrg/Project/_git/Repository"))


if __name__ == '__main__':
    unittest.main()