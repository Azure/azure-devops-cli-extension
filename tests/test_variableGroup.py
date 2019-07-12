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
    def test_variable_group(self):
        random_project_name = self.create_random_name(prefix='varGroupTests', length=20)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)
        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            # Create variable group
            create_variable_group_command = 'az pipelines variable-group create --name group1 \
                --variables var1=value1 var2=value2 \
                --authorized --description "Sample group description" --detect false --output json'
            var_group_output = self.cmd(create_variable_group_command).get_output_in_json()
            assert var_group_output["id"] > 0
            assert var_group_output["name"] == 'group1'
            assert var_group_output["description"] == "Sample group description"
            assert var_group_output["authorized"] == True
            assert len(var_group_output["variables"]) == 2
            assert var_group_output["variables"]["var1"]["value"] == "value1"
            assert var_group_output["variables"]["var2"]["value"] == "value2"
            group_id1 = var_group_output["id"]
            
            create_variable_group_command = 'az pipelines variable-group create --name group2 \
                --variables var1=value1 var2=value2 \
                --authorized --description "Sample group description" --detect false --output json'
            var_group_output = self.cmd(create_variable_group_command).get_output_in_json()
            assert var_group_output["id"] > 0
            assert var_group_output["name"] == 'group2'
            group_id2 = var_group_output["id"]

            # List variable groups
            list_variable_group_command = 'az pipelines variable-group list --detect false --output json'
            list_var_group_output = self.cmd(list_variable_group_command).get_output_in_json()
            assert len(list_var_group_output) == 2
            assert list_var_group_output[0]["name"] == 'group2' # since default order is desc
            assert list_var_group_output[1]["name"] == 'group1'

            # show variable group
            show_variable_group_command = 'az pipelines variable-group show --id {} --detect false --output json'.format(group_id1)
            show_var_group_output = self.cmd(show_variable_group_command).get_output_in_json()
            assert show_var_group_output["id"] == group_id1
            assert show_var_group_output["name"] == 'group1'
            assert show_var_group_output["description"] == "Sample group description"
            assert show_var_group_output["authorized"] == True
            assert len(show_var_group_output["variables"]) == 2
            assert show_var_group_output["variables"]["var1"]["value"] == "value1"
            assert show_var_group_output["variables"]["var2"]["value"] == "value2"

            # delete variable group
            delete_variable_group_command = 'az pipelines variable-group delete --id {} --detect false --output json -y'.format(group_id1)
            delete_var_group_output = self.cmd(delete_variable_group_command)
            # verify deletion
            # List variable groups
            list_variable_group_command = 'az pipelines variable-group list --detect false --output json'
            list_var_group_output = self.cmd(list_variable_group_command).get_output_in_json()
            assert len(list_var_group_output) == 1
            assert list_var_group_output[0]["name"] == 'group2'

            # update variable group
            update_variable_group_command = 'az pipelines variable-group update --name newGroup \
                --description NewDescription --authorized false --id {} --detect false --output json'.format(group_id2)
            update_var_group_output = self.cmd(update_variable_group_command).get_output_in_json()
            assert update_var_group_output["id"] == group_id2
            assert update_var_group_output["name"] == 'newGroup'
            assert update_var_group_output["description"] == "NewDescription"

            import pdb
            pdb.set_trace()
            # List variables in the group 
            list_variable_group_vars_command = 'az pipelines variable-group variable list --id {} \
                 --detect false --output json'.format(group_id2)
            list_var_group_vars_output = self.cmd(list_variable_group_vars_command).get_output_in_json()
            assert len(list_var_group_vars_output) == 2
            assert list_var_group_vars_output['var1']['value'] == 'value1'
            assert list_var_group_vars_output['var2']['value'] == 'value2'

            # Add variable to the group
            add_variable_group_vars_command = 'az pipelines variable-group variable create --id {} --name NewVar1 --value NewVal1 \
                 --detect false --output json'.format(group_id2)
            add_var_group_vars_output = self.cmd(add_variable_group_vars_command).get_output_in_json()
            assert len(add_var_group_vars_output) == 3
            assert add_var_group_vars_output['var1']['value'] == 'value1'
            assert add_var_group_vars_output['var2']['value'] == 'value2'
            assert add_var_group_vars_output['NewVar1']['value'] == 'NewVal1'
            assert add_var_group_vars_output['NewVar1']['isSecret'] == None

            # Add a secret variable to the group
            add_variable_group_vars_command = 'az pipelines variable-group variable create --id {} --name NewVar2 --value NewVal2 \
                 --secret --detect false --output json'.format(group_id2)
            add_var_group_vars_output = self.cmd(add_variable_group_vars_command).get_output_in_json()
            assert len(add_var_group_vars_output) == 4
            assert add_var_group_vars_output['var1']['value'] == 'value1'
            assert add_var_group_vars_output['var2']['value'] == 'value2'
            assert add_var_group_vars_output['NewVar1']['value'] == 'NewVal1'
            assert add_var_group_vars_output['NewVar1']['isSecret'] == None
            assert add_var_group_vars_output['NewVar2']['value'] == None
            assert add_var_group_vars_output['NewVar2']['isSecret'] == True

            # update variable in the group 
            update_variable_group_vars_command = 'az pipelines variable-group variable update --id {} --name NewVar1 \
                 --new-name NewVar1Updated --secret true --value 1234 --detect false --output json'.format(group_id2)
            update_var_group_vars_output = self.cmd(update_variable_group_vars_command).get_output_in_json()
            assert len(update_var_group_vars_output) == 4
            assert update_var_group_vars_output['var1']['value'] == 'value1'
            assert update_var_group_vars_output['var2']['value'] == 'value2'
            assert update_var_group_vars_output['NewVar1Updated']['value'] == None
            assert update_var_group_vars_output['NewVar1Updated']['isSecret'] == True
            assert update_var_group_vars_output['NewVar2']['value'] == None
            assert update_var_group_vars_output['NewVar2']['isSecret'] == True

            # delete the variable from the group
            delete_variable_group_vars_command = 'az pipelines variable-group variable delete --id {} \
                 --name var1 --detect false --output json -y'.format(group_id2)
            delete_var_group_vars_output = self.cmd(delete_variable_group_vars_command)

            # list to verify update and delete 
            list_variable_group_vars_command = 'az pipelines variable-group variable list --id {} \
                 --detect false --output json'.format(group_id2)
            list_var_group_vars_output = self.cmd(list_variable_group_vars_command).get_output_in_json()
            assert len(list_var_group_vars_output) == 3
            assert list_var_group_vars_output['var2']['value'] == 'value2'
            assert list_var_group_vars_output['NewVar1Updated']['value'] == None
            assert list_var_group_vars_output['NewVar1Updated']['isSecret'] == True
            assert list_var_group_vars_output['NewVar2']['value'] == None
            assert list_var_group_vars_output['NewVar2']['isSecret'] == True

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
