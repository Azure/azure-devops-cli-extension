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

from knack.util import CLIError
from azext_devops.dev.team.project import create_project
from azext_devops.dev.team.team import (create_team,
                                        delete_team,
                                        get_team,
                                        list_teams,
                                        list_team_members)

from azext_devops.dev.common.services import clear_connection_cache
from vsts.core.v4_0.core_client import CoreClient
    
class TestTeamMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://dev.azure.com/AzureDevOpsCliTest'
    _TEST_PROJECT_NAME = 'sample_project'
    _TEST_TEAM_NAME = 'sample_team'
    _TEST_TEAM_DESCRIPTION = 'sample_team_description'

    def setUp(self):
        self.get_client = patch('vsts.vss_connection.VssConnection.get_client')
        self.create_team_patcher = patch('vsts.core.v4_0.core_client.CoreClient.create_team')
        self.delete_team_patcher = patch('vsts.core.v4_0.core_client.CoreClient.delete_team')
        self.get_team_patcher = patch('vsts.core.v4_0.core_client.CoreClient.get_team')
        self.list_teams_patcher = patch('vsts.core.v4_0.core_client.CoreClient.get_teams')
        self.list_members_patcher = patch('vsts.core.v4_0.core_client.CoreClient.get_team_members')

        #start the patcher
        self.mock_get_client = self.get_client.start()
        self.mock_create_team = self.create_team_patcher.start()
        self.mock_delete_team = self.delete_team_patcher.start()
        self.mock_get_team = self.get_team_patcher.start()
        self.mock_list_teams = self.list_teams_patcher.start()
        self.mock_list_members = self.list_members_patcher.start()

        #set return values
        self.mock_get_client.return_value = CoreClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_create_team(self):
        create_team(self._TEST_TEAM_NAME, self._TEST_TEAM_DESCRIPTION, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')
        
        #assert
        self.mock_create_team.assert_called_once()
        create_team_param = self.mock_create_team.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_team_param['project_id'], str(create_team_param))
        self.assertEqual(self._TEST_TEAM_NAME, create_team_param['team'].name, str(create_team_param))
        self.assertEqual(self._TEST_TEAM_DESCRIPTION, create_team_param['team'].description, str(create_team_param))

    def test_delete_team(self):
        delete_team(self._TEST_TEAM_NAME, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')

        #assert
        self.mock_delete_team.assert_called_once()
        delete_team_param = self.mock_delete_team.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, delete_team_param['project_id'], str(delete_team_param))
        self.assertEqual(self._TEST_TEAM_NAME, delete_team_param['team_id'], str(delete_team_param))

    def test_get_team(self):
        get_team(self._TEST_TEAM_NAME, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')
        
        #assert
        self.mock_get_team.assert_called_once()
        get_team_param = self.mock_get_team.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, get_team_param['project_id'], str(get_team_param))
        self.assertEqual(self._TEST_TEAM_NAME, get_team_param['team_id'], str(get_team_param))
    
    def test_list_teams(self):

        top_value = 10
        skip_value = 2
        list_teams(top_value, skip_value, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')

        #assert
        self.mock_list_teams.assert_called_once()
        list_teams_param = self.mock_list_teams.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, list_teams_param['project_id'], str(list_teams_param))
        self.assertEqual(10, list_teams_param['top'], str(list_teams_param))
        self.assertEqual(2, list_teams_param['skip'], str(list_teams_param))

    def test_list_members(self):

        top_value = 10
        skip_value = 2
        list_team_members(self._TEST_TEAM_NAME, top_value, skip_value, self._TEST_DEVOPS_ORGANIZATION, self._TEST_PROJECT_NAME, 'Off')

        #assert
        self.mock_list_members.assert_called_once()
        list_team_members_param = self.mock_list_members.call_args_list[0][1]
        self.assertEqual(self._TEST_TEAM_NAME, list_team_members_param['team_id'], str(list_team_members_param))
        self.assertEqual(self._TEST_PROJECT_NAME, list_team_members_param['project_id'], str(list_team_members_param))
        self.assertEqual(10, list_team_members_param['top'], str(list_team_members_param))
        self.assertEqual(2, list_team_members_param['skip'], str(list_team_members_param))


if __name__ == '__main__':
    unittest.main()