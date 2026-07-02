# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch
from azext_devops.dev.common.vsts_git_url_info import VstsGitUrlInfo, _is_azure_devops_host


class Test_VstsGitUrlInfo_Methods(unittest.TestCase):

    def test_get_vsts_info_old_url_format_with_new_ssh_format(self):
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                VstsGitUrlInfo.get_vsts_info('organization@vs-ssh.visualstudio.com:v3/organization/project/repository')
                # Asserts            
                mock_get_vsts_info.assert_called_once()
                mock_get_creds.assert_called_once()
                get_vsts_info_url_param = mock_get_vsts_info.call_args_list[0][0]
                self.assertEqual(
                    'https://organization.visualstudio.com/project/_git/repository'.lower(), get_vsts_info_url_param[0])
                    

    def test_get_vsts_info_old_url_format_with_https(self):
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                VstsGitUrlInfo.get_vsts_info('https://organization.visualstudio.com/project/_git/repository')
                # Asserts            
                mock_get_vsts_info.assert_called_once()
                mock_get_creds.assert_called_once()
                get_vsts_info_url_param = mock_get_vsts_info.call_args_list[0][0]
                self.assertEqual(
                    'https://organization.visualstudio.com/project/_git/repository'.lower(), get_vsts_info_url_param[0])
                    

    def test_get_vsts_info_old_url_format_with_old_ssh_format(self):
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                VstsGitUrlInfo.get_vsts_info('ssh://organization@vs-ssh.visualstudio.com:22/project/_ssh/repository')
                # Asserts            
                mock_get_vsts_info.assert_called_once()
                mock_get_creds.assert_called_once()
                get_vsts_info_url_param = mock_get_vsts_info.call_args_list[0][0]
                self.assertEqual(
                    'https://organization.visualstudio.com/project/_git/repository'.lower(), get_vsts_info_url_param[0])


    def test_get_vsts_inf_new_url_format_with_ssh(self):
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                VstsGitUrlInfo.get_vsts_info('git@ssh.dev.azure.com:v3/organization/project/repository')
                # Asserts            
                mock_get_vsts_info.assert_called_once()
                mock_get_creds.assert_called_once()
                get_vsts_info_url_param = mock_get_vsts_info.call_args_list[0][0]
                self.assertEqual(
                    'https://dev.azure.com/organization/project/_git/repository'.lower(), get_vsts_info_url_param[0])

    def test_get_vsts_inf_new_url_format_with_https(self):
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                VstsGitUrlInfo.get_vsts_info('https://organization@dev.azure.com/organization/project/_git/repository')
                # Asserts            
                mock_get_vsts_info.assert_called_once()
                mock_get_creds.assert_called_once()
                get_vsts_info_url_param = mock_get_vsts_info.call_args_list[0][0]
                self.assertEqual(
                    'https://organization@dev.azure.com/organization/project/_git/repository'.lower(), get_vsts_info_url_param[0])

    def test_get_vsts_info_rejects_arbitrary_host_with_git_path(self):
        """Credentials must never be sent to non-Azure DevOps hosts."""
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                result = VstsGitUrlInfo.get_vsts_info('https://evil.com/org/project/_git/repo')
                self.assertIsNone(result)
                mock_get_creds.assert_not_called()
                mock_get_vsts_info.assert_not_called()

    def test_get_vsts_info_rejects_attacker_ssh_url(self):
        """SSH URLs to non-Azure DevOps hosts must not trigger credential retrieval."""
        with patch('azext_devops.devops_sdk.v5_0.git.git_client.GitClient.get_vsts_info_by_remote_url') as mock_get_vsts_info:
            with patch('azext_devops.dev.common.services._get_credentials') as mock_get_creds:
                result = VstsGitUrlInfo.get_vsts_info('https://attacker.io/fake/_git/repo')
                self.assertIsNone(result)
                mock_get_creds.assert_not_called()
                mock_get_vsts_info.assert_not_called()


class Test_IsVstsUrlCandidate(unittest.TestCase):

    def test_rejects_none(self):
        self.assertFalse(VstsGitUrlInfo.is_vsts_url_candidate(None))

    def test_rejects_github(self):
        self.assertFalse(VstsGitUrlInfo.is_vsts_url_candidate('https://github.com/org/repo'))

    def test_rejects_arbitrary_host_with_git_path(self):
        self.assertFalse(VstsGitUrlInfo.is_vsts_url_candidate('https://evil.com/org/project/_git/repo'))

    def test_rejects_arbitrary_host_with_ssh_path(self):
        self.assertFalse(VstsGitUrlInfo.is_vsts_url_candidate('https://attacker.io/project/_ssh/repo'))

    def test_accepts_dev_azure_com(self):
        self.assertTrue(VstsGitUrlInfo.is_vsts_url_candidate(
            'https://dev.azure.com/org/project/_git/repo'))

    def test_accepts_visualstudio_com(self):
        self.assertTrue(VstsGitUrlInfo.is_vsts_url_candidate(
            'https://myorg.visualstudio.com/project/_git/repo'))

    def test_accepts_ssh_dev_azure_com(self):
        self.assertTrue(VstsGitUrlInfo.is_vsts_url_candidate(
            'git@ssh.dev.azure.com:v3/org/project/repo'))

    def test_accepts_vs_ssh_visualstudio_com(self):
        self.assertTrue(VstsGitUrlInfo.is_vsts_url_candidate(
            'org@vs-ssh.visualstudio.com:v3/org/project/repo'))


class Test_IsAzureDevOpsHost(unittest.TestCase):

    def test_dev_azure_com(self):
        self.assertTrue(_is_azure_devops_host('dev.azure.com'))

    def test_ssh_dev_azure_com(self):
        self.assertTrue(_is_azure_devops_host('ssh.dev.azure.com'))

    def test_visualstudio_com(self):
        self.assertTrue(_is_azure_devops_host('myorg.visualstudio.com'))

    def test_vs_ssh_visualstudio_com(self):
        self.assertTrue(_is_azure_devops_host('vs-ssh.visualstudio.com'))

    def test_user_at_dev_azure_com(self):
        self.assertTrue(_is_azure_devops_host('org@dev.azure.com'))

    def test_git_at_ssh_dev_azure_com(self):
        self.assertTrue(_is_azure_devops_host('git@ssh.dev.azure.com'))

    def test_rejects_github(self):
        self.assertFalse(_is_azure_devops_host('github.com'))

    def test_rejects_arbitrary_host(self):
        self.assertFalse(_is_azure_devops_host('evil.com'))

    def test_rejects_none(self):
        self.assertFalse(_is_azure_devops_host(None))

    def test_rejects_subdomain_spoof(self):
        self.assertFalse(_is_azure_devops_host('dev.azure.com.evil.com'))

    def test_rejects_visualstudio_com_spoof(self):
        self.assertFalse(_is_azure_devops_host('notvisualstudio.com'))
