# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class PipelinesFolderTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_pipeline_folders(self):
        random_project_name = self.create_random_name(prefix='pipelinesFolderTest', length=25)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)
        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            # create a pipeline
            FOLDER_NAME = '\\TestFolder'
            FOLDER_DESCRIPTION = 'Test folder'
            folder_create_command = 'az pipelines folder create --path {} --description "{}" \
                --detect false --output json'.format(FOLDER_NAME, FOLDER_DESCRIPTION)
            folder_create_output = self.cmd(folder_create_command).get_output_in_json()
            assert folder_create_output['path'] == FOLDER_NAME
            assert folder_create_output['description'] == FOLDER_DESCRIPTION

            UPDATED_FOLDER_DESCRIPTION = 'New test folder'
            UPDATED_FOLDER_PATH = '\\Testing' + FOLDER_NAME
            folder_update_command = 'az pipelines folder update --path {} --new-path "{}" --new-description "{}" \
                --detect false --output json'.format(FOLDER_NAME, UPDATED_FOLDER_PATH, UPDATED_FOLDER_DESCRIPTION)
            folder_update_output = self.cmd(folder_update_command).get_output_in_json()
            assert folder_update_output['path'] == UPDATED_FOLDER_PATH
            assert folder_update_output['description'] == UPDATED_FOLDER_DESCRIPTION

            folder_list_command = 'az pipelines folder list --detect false --output json --query-order asc'
            folder_list_output = self.cmd(folder_list_command).get_output_in_json()
            assert len(folder_list_output) == 3  # root folder + testing/test123 nested folders
            assert folder_list_output[0]['path'] == '\\'  # root folder
            assert folder_list_output[0]['description'] == None
            assert folder_list_output[1]['path'] == '\\Testing'
            assert folder_list_output[1]['description'] == None
            assert folder_list_output[2]['path'] == UPDATED_FOLDER_PATH
            assert folder_list_output[2]['description'] == UPDATED_FOLDER_DESCRIPTION

            folder_delete_command = 'az pipelines folder delete --path "{}" --detect false --output json -y'.format(UPDATED_FOLDER_PATH)
            folder_delete_output = self.cmd(folder_delete_command)
            # verify deletion
            folder_list_output = self.cmd(folder_list_command).get_output_in_json()
            assert len(folder_list_output) == 2
            assert folder_list_output[0]['path'] == '\\'  # root folder
            assert folder_list_output[0]['description'] == None
            assert folder_list_output[1]['path'] == '\\Testing'
            assert folder_list_output[1]['description'] == None

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
