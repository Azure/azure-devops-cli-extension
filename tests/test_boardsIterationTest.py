# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import unittest
from knack.util import CLIError

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/v-anvashist0376'

class BoardsIterationsTest(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_boards_iterations(self):
        random_project_name = 'Iteration' + self.create_random_name(prefix='Proj_', length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        try:
            # PROJECT LEVEL ITERATIONS
            #create project
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]
            list_project_iteration_cmd = 'az boards iteration project list --project ' + random_project_name + ' --output json --detect false'
            list_project_iteration = self.cmd(list_project_iteration_cmd).get_output_in_json()
            initial_iterations_number =  len(list_project_iteration['children'])

            #create team
            team_name = self.create_random_name(prefix='teamName1_', length=15)
            create_team_cmd = 'az devops team create --name ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            create_team = self.cmd(create_team_cmd).get_output_in_json()
            assert create_team['name'] == team_name

            list_project_iteration_cmd = 'az boards iteration project list --depth 0 --project ' + random_project_name + ' --output json --detect false'
            list_project_iteration = self.cmd(list_project_iteration_cmd).get_output_in_json()
            project_root_node_name =  list_project_iteration['name']
            project_root_node_identifier =  list_project_iteration['identifier']

            #create project root level iteration
            root_iteration_name = team_name + self.create_random_name(prefix='_Root_Itr_', length=15)
            create_project_iteration_cmd = 'az boards iteration project create --name '+ root_iteration_name + ' --project ' + random_project_name + ' --output json --detect false'
            create_project_iteration = self.cmd(create_project_iteration_cmd).get_output_in_json()
            
            root_project_iteration_path = create_project_iteration['path']
            root_project_iteration_id = create_project_iteration['id']
            root_project_iteration_identifier = create_project_iteration['identifier']
            #list project iterations
            list_project_iteration_cmd = 'az boards iteration project list --project ' + random_project_name + ' --output json --detect false'
            list_project_iteration = self.cmd(list_project_iteration_cmd).get_output_in_json()
            assert len(list_project_iteration['children']) == initial_iterations_number + 1

            #create 2 project child level iterations
            child_iteration_name1 = self.create_random_name(prefix='Child_Itr_', length=15)
            create_project_iteration_child_cmd = 'az boards iteration project create --name ' + child_iteration_name1 + ' --path "'+ root_project_iteration_path + '" --project ' + random_project_name + ' --output json --detect false'
            create_project_iteration_child = self.cmd(create_project_iteration_child_cmd).get_output_in_json()
            child_iteration1_path = create_project_iteration_child['path']
            child_iteration1_id = create_project_iteration_child['id']
            child_iteration1_identifier = create_project_iteration_child['identifier']
            
            child_iteration_name2 = self.create_random_name(prefix='Child_Itr_', length=15)
            create_project_iteration_child_cmd = 'az boards iteration project create --name ' + child_iteration_name2 + ' --start-date "2019-06-17" --finish-date "2019-06-28"' + ' --path "'+ root_project_iteration_path + '" --project ' + random_project_name + ' --output json --detect false'
            create_project_iteration_child = self.cmd(create_project_iteration_child_cmd).get_output_in_json()
            child_iteration2_path = create_project_iteration_child['path']
            child_iteration2_identifier = create_project_iteration_child['identifier']
            child_iteration2_id = create_project_iteration_child['id']

            list_project_iteration_cmd = 'az boards iteration project list --depth 2 --project ' + random_project_name + ' --output json --detect false'
            list_project_iteration = self.cmd(list_project_iteration_cmd).get_output_in_json()
            root_list_project_iteration = list_project_iteration['children']
            assert len(root_list_project_iteration) == (initial_iterations_number + 1)
            for entry in root_list_project_iteration:
                if entry['name'] == root_iteration_name and entry['hasChildren'] and entry['children']:
                    child_name_list = [entry['children'][0]['name'], entry['children'][1]['name']]
                    assert child_iteration_name1 in child_name_list
                    assert child_iteration_name2 in child_name_list

            # show project iteration
            show_project_iteration_cmd = 'az boards iteration project show --id ' + str(child_iteration1_id) + ' --project ' + random_project_name + ' --output json --detect false'
            show_project_iteration = self.cmd(show_project_iteration_cmd).get_output_in_json()
            assert show_project_iteration[0]['path'] == child_iteration1_path
            assert show_project_iteration[0]['id'] == child_iteration1_id
            
            # update project iteration
            update_project_iteration_name_cmd = 'az boards iteration project update --path "' + child_iteration1_path + '" --child-id ' + str(child_iteration2_id) + ' --project ' + random_project_name + ' --output json --detect false'
            print(update_project_iteration_name_cmd)
            update_project_iteration = self.cmd(update_project_iteration_name_cmd).get_output_in_json()
            assert update_project_iteration['path'] == child_iteration1_path 
            assert update_project_iteration['id'] == child_iteration1_id

            # TEAM LEVEL ITERATIONS
            list_team_iteration_cmd = 'az boards iteration team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            list_team_iteration = self.cmd(list_team_iteration_cmd).get_output_in_json()
            assert len(list_team_iteration) == 0
        
            # Adding a new iteration to team before configuring backlog iteration should throw error.
            with self.assertRaises(Exception) as exc:
                team_iteration_add_cmd = 'az boards iteration team add --id ' + root_project_iteration_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
                team_iteration_add = self.cmd(team_iteration_add_cmd).get_output_in_json()
            self.assertIn('No backlog iteration has been selected for your team. Before you can select iterations for your team to participate in, you must first specify a backlog iteration.', str(exc.exception))


            # set back log iteration and then add both child iterations to team
            backlog_team_iteration_set_cmd = 'az boards iteration team set-backlog-iteration --id ' + project_root_node_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            backlog_team_iteration_set = self.cmd(backlog_team_iteration_set_cmd).get_output_in_json()
            assert backlog_team_iteration_set['backlogIteration']['id'] == project_root_node_identifier
            assert backlog_team_iteration_set['backlogIteration']['name'] == project_root_node_name ## '\\'+random_project_name+'\\'+'Iteration'

            backlog_team_iteration_show_cmd = 'az boards iteration team show-backlog-iteration --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            backlog_team_iteration_show = self.cmd(backlog_team_iteration_show_cmd).get_output_in_json()
            assert backlog_team_iteration_set['backlogIteration']['id'] == project_root_node_identifier
            assert backlog_team_iteration_set['backlogIteration']['name'] == project_root_node_name

            team_iteration_add_cmd = 'az boards iteration team add --id ' + child_iteration1_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            team_iteration_add = self.cmd(team_iteration_add_cmd).get_output_in_json()
            assert team_iteration_add['id'] == child_iteration1_identifier
            assert team_iteration_add['name'] == child_iteration_name1

            team_iteration_add_cmd = 'az boards iteration team add --id ' + child_iteration2_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            team_iteration_add = self.cmd(team_iteration_add_cmd).get_output_in_json()
            assert team_iteration_add['id'] == child_iteration2_identifier
            assert team_iteration_add['name'] == child_iteration_name2
        
            # set and get default team iteration
            default_team_iteration_set_cmd = 'az boards iteration team set-default-iteration --id ' + root_project_iteration_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            default_team_iteration_set = self.cmd(default_team_iteration_set_cmd).get_output_in_json()
            assert default_team_iteration_set['defaultIteration']['id'] == root_project_iteration_identifier
            assert default_team_iteration_set['defaultIteration']['name'] == root_iteration_name

            self.sleep_in_live_run(30)

            default_team_iteration_show_cmd = 'az boards iteration team show-default-iteration --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            default_team_iteration_show = self.cmd(default_team_iteration_show_cmd).get_output_in_json()
            assert default_team_iteration_show['defaultIteration']['id'] == root_project_iteration_identifier
            assert default_team_iteration_show['defaultIteration']['name'] == root_iteration_name

            list_team_iteration_cmd = 'az boards iteration team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            list_team_iteration = self.cmd(list_team_iteration_cmd).get_output_in_json()
            assert len(list_team_iteration) == 2

            team_iteration_remove_cmd = 'az boards iteration team remove --id ' + child_iteration1_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            team_iteration_remove = self.cmd(team_iteration_remove_cmd)

            list_team_iteration_cmd = 'az boards iteration team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            list_team_iteration = self.cmd(list_team_iteration_cmd).get_output_in_json()
            assert len(list_team_iteration) == 1

            team_iteration_remove_cmd = 'az boards iteration team remove --id ' + child_iteration2_identifier + ' --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            team_iteration_remove = self.cmd(team_iteration_remove_cmd)

            list_team_iteration_cmd = 'az boards iteration team list --team ' + team_name + ' --project ' + random_project_name + ' --output json --detect false'
            list_team_iteration = self.cmd(list_team_iteration_cmd).get_output_in_json()
            assert len(list_team_iteration) == 0

            delete_project_iteration_cmd = 'az boards iteration project delete --path "'+ root_project_iteration_path + '" --project ' + random_project_name + ' --output json --detect false -y'
            delete_project_iteration = self.cmd(delete_project_iteration_cmd)
            list_project_iteration = self.cmd(list_project_iteration_cmd).get_output_in_json()
            assert len(list_project_iteration['children']) == initial_iterations_number   

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
