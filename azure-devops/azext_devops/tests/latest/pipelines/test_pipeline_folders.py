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

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.dev.pipelines.pipeline_folders import (pipeline_folder_create,
                                                         pipeline_folder_delete,
                                                         pipeline_folder_list,
                                                         pipeline_folder_update)
from azext_devops.devops_sdk.v5_0.build.build_client import BuildClient
from azext_devops.devops_sdk.v5_0.build.models import Folder


class TestPipelinesFoldersMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'MyProject'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()

        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client')
        #start the patchers
        self.mock_get_client = self.get_client_patcher.start()
        # Set return values which will be same across tests
        self.mock_get_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)
        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_folder_create(self):
        with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.create_folder') as mock_create_folder:
            # Creating folder
            new_folder = pipeline_folder_create(path='test', description='test description',
                           project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            folder = Folder()
            folder.description = 'test description'
            folder.path = 'test'
            # assert
            mock_create_folder.assert_called_once_with(
                folder=folder, path='test', project=self._TEST_DEVOPS_PROJECT)

    def test_folder_delete(self):
        with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.delete_folder') as mock_delete_folder:
            # deleting folder
            pipeline_folder_delete(
                path='test', project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_delete_folder.assert_called_once_with(
                path='test', project=self._TEST_DEVOPS_PROJECT)
    
    def test_folder_list(self):
        with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.get_folders') as mock_list_folders:
            # listing folders
            folders = pipeline_folder_list(
                path='test', query_order='asc', project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_list_folders.assert_called_once_with(
                path='test', query_order='folderAscending', project=self._TEST_DEVOPS_PROJECT)

    def test_folder_update(self):
        with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.update_folder') as mock_update_folders:
            with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.get_folders') as mock_list_folders:
                folder = Folder()
                folder.description ='hello world'
                folder.path = 'test'
                mock_list_folders.return_value = [folder]

                update_folder = Folder()
                update_folder.description ='hello world updated'
                update_folder.path = 'test123'

                updated_folder = pipeline_folder_update(
                    path='test', new_path='test123', new_description='hello world updated',
                    project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)

                # assert
                mock_list_folders.assert_called_once_with(
                    path='test', project=self._TEST_DEVOPS_PROJECT, query_order='folderAscending')
                mock_update_folders.assert_called_once_with(
                    folder=mock_list_folders.return_value[0], path='test', project=self._TEST_DEVOPS_PROJECT)
                self.assertEqual(mock_list_folders.return_value[0].path, 'test123')
                self.assertEqual(mock_list_folders.return_value[0].description, 'hello world updated')
                
    
    def test_folder_update_with_invalid_input(self):
        with self.assertRaises(Exception) as exc:
            response = pipeline_folder_update(
                    path='test', project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
        self.assertEqual(str(exc.exception),r'Either --new-path or --new-description should be specified.')                
