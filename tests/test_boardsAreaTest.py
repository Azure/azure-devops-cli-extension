# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import time
import unittest
from knack.util import CLIError

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/ishitamehta'

class BoardsAreaTest(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_boards_areas(self):
        random_project_name = self.create_random_name(prefix='Area1', length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)
        
        try:
            # PROJECT LEVEL AREAS
            #create project
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            list_project_area_cmd = 'az boards area project list --project ' + random_project_name + ' --output json --detect false'
            list_project_area = self.cmd(list_project_area_cmd).get_output_in_json()
            assert list_project_area['children'] == None

            #create team
            team_name = self.create_random_name(prefix='teamArea_', length=15)
            create_team_cmd = 'az devops team create --name ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            create_team = self.cmd(create_team_cmd).get_output_in_json()
            assert create_team['name'] == team_name

            list_project_area_cmd = 'az boards area project list --depth 0 --project ' + random_project_name + ' --output json --detect false'
            list_project_area = self.cmd(list_project_area_cmd).get_output_in_json()
            project_root_node_name =  list_project_area['name']
            project_root_node_identifier =  list_project_area['identifier']

            #create project root level areas
            root_area_name = team_name + self.create_random_name(prefix='_Root_Area_', length=15)
            create_project_area_cmd = 'az boards area project create --name '+ root_area_name + ' --project ' + random_project_name + ' --output json --detect false'
            create_project_area = self.cmd(create_project_area_cmd).get_output_in_json()
            
            root_project_area_path = create_project_area['path']
            root_project_area_id = create_project_area['id']
            root_project_area_identifier = create_project_area['identifier']
            #list project areas
            list_project_area_cmd = 'az boards area project list --project ' + random_project_name + ' --output json --detect false'
            list_project_area = self.cmd(list_project_area_cmd).get_output_in_json()
            assert len(list_project_area['children']) == 1

            #create 2 project child level areas
            child_area_name1 = self.create_random_name(prefix='ChildArea', length=15)
            create_project_area_child_cmd = 'az boards area project create --name ' + child_area_name1 + ' --path "'+ root_project_area_path + '" --project ' + random_project_name + ' --output json --detect false'
            create_project_area_child = self.cmd(create_project_area_child_cmd).get_output_in_json()
            child_area1_path = create_project_area_child['path']
            child_area1_id = create_project_area_child['id']
            child_area1_identifier = create_project_area_child['identifier']
            
            child_area_name2 = self.create_random_name(prefix='ChildArea', length=15)
            create_project_area_child_cmd = 'az boards area project create --name ' + child_area_name2 + ' --path "'+ root_project_area_path + '" --project ' + random_project_name + ' --output json --detect false'
            create_project_area_child = self.cmd(create_project_area_child_cmd).get_output_in_json()
            child_area2_path = create_project_area_child['path']
            child_area2_identifier = create_project_area_child['identifier']
            child_area2_id = create_project_area_child['id']

            list_project_area_cmd = 'az boards area project list --depth 2 --project ' + random_project_name + ' --output json --detect false'
            list_project_area = self.cmd(list_project_area_cmd).get_output_in_json()
            root_list_project_area = list_project_area['children']
            assert len(root_list_project_area) == 1
            for entry in root_list_project_area:
                if entry['name'] == root_area_name and entry['hasChildren'] and entry['children']:
                    child_name_list = [entry['children'][0]['name'], entry['children'][1]['name']]
                    assert child_area_name1 in child_name_list
                    assert child_area_name2 in child_name_list

            # show project area
            show_project_area_cmd = 'az boards area project show --id ' + str(child_area1_id) + ' --project ' + random_project_name + ' --output json --detect false'
            show_project_area = self.cmd(show_project_area_cmd).get_output_in_json()
            assert show_project_area[0]['path'] == child_area1_path
            assert show_project_area[0]['id'] == child_area1_id

            # update area
            update_project_area_name_cmd = 'az boards area project update --path "' + child_area1_path + '" --child-id ' + str(child_area2_id) + ' --project ' + random_project_name + ' --output json --detect false'
            update_project_area = self.cmd(update_project_area_name_cmd).get_output_in_json()
            assert update_project_area['path'] == child_area1_path + "\\" +child_area_name2
            assert update_project_area['id'] == child_area2_id
            child_area2_path = update_project_area['path']

            # TEAM LEVEL AREAS
            list_team_area_cmd = 'az boards area team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            print(list_team_area_cmd)
            list_team_area = self.cmd(list_team_area_cmd).get_output_in_json()
            assert len(list_team_area['values']) == 0

            # Adding a new area to team before configuring default area should throw error.
            with self.assertRaises(Exception) as exc:
                if "Area\\" in root_project_area_path:
                    updated_root_project_area_path = root_project_area_path.replace("Area\\", '')
                    print(updated_root_project_area_path)
                    team_area_add_cmd = 'az boards area team add --path "' + updated_root_project_area_path + '" --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
                    team_area_add = self.cmd(team_area_add_cmd).get_output_in_json()
            self.assertIn('DefaultValue\nPlease see https://aka.ms/azure-devops-cli-troubleshooting for more information on troubleshooting common errors.' , str(exc.exception))
            
            list_team_area_cmd = 'az boards area team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            print(list_team_area_cmd)
            list_team_area = self.cmd(list_team_area_cmd).get_output_in_json()
            assert len(list_team_area['values']) == 0

            child_area1_path = child_area1_path.replace("Area\\", '')
            child_area1_path = child_area1_path[1:]
            team_area_add_cmd = 'az boards area team add --path "' + child_area1_path + '" --team ' + team_name + ' --project ' + random_project_name + ' --set-as-default --output json --detect false'
            team_area_add = self.cmd(team_area_add_cmd).get_output_in_json()
            assert len(team_area_add['values']) == 1
            assert team_area_add['defaultValue'] == child_area1_path

            child_area2_path = child_area2_path.replace("Area\\", '')
            child_area2_path = child_area2_path[1:]
            team_area_add_cmd = 'az boards area team add --path "' + child_area2_path + '" --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            team_area_add = self.cmd(team_area_add_cmd).get_output_in_json()
            assert len(team_area_add['values']) == 2
        
            team_area_update_cmd = 'az boards area team update --path "' + child_area2_path + '" --team ' + team_name + '  --include-sub-areas true --set-as-default --project ' + random_project_name + ' --output json --detect false'
            team_area_update = self.cmd(team_area_update_cmd).get_output_in_json()
            assert team_area_update['defaultValue'] == child_area2_path
            assert len(team_area_update['values']) == 2
            updated_list = team_area_update['values']
            for entry in updated_list:
                if entry['value'] == child_area2_path:
                    assert entry['includeChildren'] == True

            list_team_area_cmd = 'az boards area team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            print(list_team_area_cmd)
            list_team_area = self.cmd(list_team_area_cmd).get_output_in_json()
            assert len(list_team_area['values']) == 2
    
            with self.assertRaises(Exception) as exc:
                team_area_remove_cmd = 'az boards area team remove --path "' + child_area2_path + '" --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
                print(team_area_remove_cmd)
                team_area_remove = self.cmd(team_area_remove_cmd)
            self.assertIn('You are trying to remove the default area for this team. Please change the default area node and then try this command again.', str(exc.exception))

            team_area_remove_cmd = 'az boards area team remove --path "' + child_area1_path + '" --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            print(team_area_remove_cmd)
            team_area_remove = self.cmd(team_area_remove_cmd)

            list_team_area_cmd = 'az boards area team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            print(list_team_area_cmd)
            list_team_area = self.cmd(list_team_area_cmd).get_output_in_json()
            assert len(list_team_area['values']) == 1

            delete_project_area_cmd = 'az boards area project delete --path "'+ root_project_area_path + '" --project ' + random_project_name + ' --output json --detect false -y'
            delete_project_area = self.cmd(delete_project_area_cmd)
            list_project_area = self.cmd(list_project_area_cmd).get_output_in_json()
            assert list_project_area['children'] == None

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)