# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import time
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class DevopsTeamTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_devops_team_createUpdateShowListDeleteListMember(self):
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=DevopsTeamTests')
    
        team_name = self.create_random_name(prefix='team_name', length=15)
        team_name2 = self.create_random_name(prefix='team_name2', length=15)
        updated_team_name = self.create_random_name(prefix='updated_', length=15)
        team_description = 'Sample description'
        updated_team_description = 'Sample updated description'
    
        try:
            # create a team
            create_team_command = ('az devops team create --name "' + team_name + '" --description "' + team_description + '" --output json --detect off')
            create_team_output = self.cmd(create_team_command).get_output_in_json()
            created_team_id = create_team_output['id']
            assert len(create_team_output) > 0
            assert create_team_output["name"] == team_name
            assert create_team_output["description"] == team_description

            # create one more team
            create_team_command = ('az devops team create --name "' + team_name2 + '" --description "' + team_description + '" --output json --detect off')
            create_team_output2 = self.cmd(create_team_command).get_output_in_json()
            created_team_id2 = create_team_output2['id'] 
            assert len(create_team_output2) > 0
            assert create_team_output2["name"] == team_name2
            assert create_team_output2["description"] == team_description

            #list team command
            list_teams_command = 'az devops team list --output json --detect off'
            list_teams_output = self.cmd(list_teams_command).get_output_in_json()
            assert len(list_teams_output) == 3  # one default project team and 2 teams created by test
            list_team_ids = []
            for team in list_teams_output:
                list_team_ids.append(team['id'])
            assert created_team_id in list_team_ids
            assert created_team_id2 in list_team_ids

            #show team command
            show_team_command = 'az devops team show --team "' + created_team_id + '" --output json --detect off'
            show_team_output = self.cmd(show_team_command).get_output_in_json()
            assert len(show_team_output) > 0
            assert show_team_output["name"] == team_name
            assert show_team_output["description"] == team_description
            assert show_team_output["id"] == created_team_id

            #update team  
            update_team_command = ('az devops team update --team "' + team_name + '" --name "' + updated_team_name + 
                '" --description "' + updated_team_description + '" --output json --detect off')
            update_team_output = self.cmd(update_team_command).get_output_in_json()
            assert len(update_team_output) > 0
            assert update_team_output["name"] == updated_team_name
            assert update_team_output["description"] == updated_team_description
            assert update_team_output["id"] == created_team_id

            # Testing 'list-member' command for default team in this project
            list_team_members_command = 'az devops team list-member --team "' + "DevopsTeamTests Team" + '" --output json --detect off'
            list_team_members_output = self.cmd(list_team_members_command).get_output_in_json()
            assert len(list_team_members_output) == 3

        finally:
            # TestCleanup - delete team
            delete_team_command = 'az devops team delete --id "' + created_team_id + '" --output json --detect off --yes'
            self.cmd(delete_team_command)

            # delete second team 
            delete_team_command = 'az devops team delete --id "' + created_team_id2 + '" --output json --detect off --yes'
            self.cmd(delete_team_command)

            list_teams_command = 'az devops team list --output json --detect off'
            list_teams_output_after_delete = self.cmd(list_teams_command).get_output_in_json()
            for team in list_teams_output_after_delete:
                if (team["id"] == created_team_id or team["id"] == created_team_id2):
                    assert 0

