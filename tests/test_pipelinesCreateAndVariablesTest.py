# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class PipelinesTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_pipeline_create_and_variables_test(self):
        random_project_name = self.create_random_name(prefix='pipelinesTest', length=20)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)
        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            list_repo_command = 'az repos list --project {} --output json --detect false'.format(created_project_id)
            created_repo_id = None
            created_repo_name = None
            list_repo_output = self.cmd(list_repo_command).get_output_in_json()
            assert len(list_repo_output) > 0
            created_repo_id = list_repo_output[0]["id"]
            created_repo_name = list_repo_output[0]["name"]
            
            # Import repo with yaml file
            import_repo_command = 'az repos import create --git-source-url https://dev.azure.com/AzureDevOpsCliTest/ImportRepoTest/_git/snakes-and-ladders --repository ' + created_repo_id + ' --detect false --output json'
            import_repo_output = self.cmd(import_repo_command).get_output_in_json()
            import_repo_status = import_repo_output["status"]
            assert import_repo_status == 'completed'

            # create a pipeline
            PIPELINE_NAME = 'ContosoBuild'
            PIPELINE_DESCRIPTION = 'Pipeline for contoso project'
            pipeline_create_command = 'az pipelines create --name {} --description "{}" --repository {} \
                --repository-type tfsgit --branch master --yml-path azure-pipelines.yml --detect false \
                --output json'.format(PIPELINE_NAME, PIPELINE_DESCRIPTION, created_repo_name)
            pipeline_create_output = self.cmd(pipeline_create_command).get_output_in_json()
            created_pipeline_id = pipeline_create_output['definition']['id']
            created_pipeline_name = pipeline_create_output['definition']['name']
            assert created_pipeline_name == PIPELINE_NAME

            # Pipeline run and run list

            # Create variable 
            create_variable_command = 'az pipelines variable create --pipeline-id {} --name var1 \
                --value value1 --secret --allow-override --detect false --output json'.format(created_pipeline_id)
            var_create_output = self.cmd(create_variable_command).get_output_in_json()
            assert var_create_output['var1']['value'] == None
            assert var_create_output['var1']['allowOverride'] == True
            assert var_create_output['var1']['isSecret'] == True
            
            create_variable_command = 'az pipelines variable create --pipeline-id {} --name var2 \
                --value value2 --detect false --output json'.format(created_pipeline_id)
            var_create_output = self.cmd(create_variable_command).get_output_in_json()
            assert var_create_output['var2']['value'] == 'value2'
            assert var_create_output['var2']['allowOverride'] == None
            assert var_create_output['var2']['isSecret'] == None
            assert var_create_output.get('var1') == None
            
            # List variables 
            list_variable_command = 'az pipelines variable list --pipeline-id {} --detect false --output json'.format(created_pipeline_id)
            list_var_output = self.cmd(list_variable_command).get_output_in_json()
            assert len(list_var_output) == 2
            assert list_var_output['var1']['value'] == None
            assert list_var_output['var1']['allowOverride'] == True
            assert list_var_output['var1']['isSecret'] == True
            assert list_var_output['var2']['value'] == 'value2'
            assert list_var_output['var2']['allowOverride'] == None
            assert list_var_output['var2']['isSecret'] == None

            # delete variable 
            delete_variable_command = 'az pipelines variable delete --pipeline-id {} --name var2 --detect false \
                --output json -y'.format(created_pipeline_id)
            delete_var_output = self.cmd(delete_variable_command)
            # verify deletion List variable 
            list_variable_command = 'az pipelines variable list --pipeline-id {} --detect false --output json'.format(created_pipeline_id)
            list_var_output = self.cmd(list_variable_command).get_output_in_json()
            assert len(list_var_output) == 1
            assert list_var_output['var1']['value'] == None
            assert list_var_output['var1']['allowOverride'] == True
            assert list_var_output['var1']['isSecret'] == True

            # update variable 
            update_variable_command = 'az pipelines variable update --name var1  --new-name var1Updated --secret false --value 123\
                --allow-override false --pipeline-id {} --detect false --output json'.format(created_pipeline_id)
            update_var_output = self.cmd(update_variable_command).get_output_in_json()
            assert update_var_output['var1Updated']['value'] == '123'
            assert update_var_output['var1Updated']['allowOverride'] == None
            assert update_var_output['var1Updated']['isSecret'] == None

            pipelines_list_command = 'az pipelines list --detect false --output json'
            pipelines_list_output = self.cmd(pipelines_list_command).get_output_in_json()
            len(pipelines_list_output) == 1
            assert pipelines_list_output[0]['name'] == PIPELINE_NAME

            # Delete pipeline 
            pipeline_delete_command = 'az pipelines delete --id {} --detect false \
                --output json -y'.format(created_pipeline_id)
            self.cmd(pipeline_delete_command)
            # verify delete - list pipelines

            pipelines_list_command = 'az pipelines list --detect false --output json'
            pipelines_list_output = self.cmd(pipelines_list_command).get_output_in_json()
            len(pipelines_list_output) == 0


            created_pipeline_id = pipeline_create_output['definition']['id']
        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
