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
from azext_devops.dev.common.vsts_git_url_info import VstsGitUrlInfo


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
