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

from azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client import (WorkItemTrackingClient)

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.test.utils.helper import get_client_mock_helper
from azext_devops.dev.boards.iteration import (get_project_iterations,
                                               get_project_iteration,
                                               delete_project_iteration,
                                               create_project_iteration,
                                               update_project_iteration,
                                               get_team_iterations,
                                               get_team_iteration,
                                               post_team_iteration,
                                               delete_team_iteration)

class TestBoardsIterationMethods(AuthenticatedTests):
    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_NAME = 'sample_project'
    _WORK_ITEM_TRACKING_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.'
    _WORK_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work.work_client.WorkClient.'
    _STRUCTURE_GROUP = 'iterations'
    _ROOT_ITERATION_PATH = _TEST_PROJECT_NAME + '\root_iteration'
    _ROOT_ITERATION_NAME = 'root_iteration'
    _CHILD_ITERATION_NAME = 'child_iteration'
    _NEW_ITERATION_NAME = 'root_iteration_renamed'
    _ITERATION_ID = 1
    _TEAM = 'sample_team'
    _ITERATION_IDENTIFIER = 'some-guid'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_classification_nodes_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'get_classification_nodes')
        self.get_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'get_classification_node')
        self.delete_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'delete_classification_node')
        self.create_update_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'create_or_update_classification_node')
        self.update_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'update_classification_node')
        self.get_team_iterations_patcher = patch(self._WORK_CLIENT_LOCATION + 'get_team_iterations')
        self.get_team_iteration_patcher = patch(self._WORK_CLIENT_LOCATION + 'get_team_iteration')
        self.delete_team_iteration_patcher = patch(self._WORK_CLIENT_LOCATION + 'delete_team_iteration')
        self.post_team_iteration_patcher = patch(self._WORK_CLIENT_LOCATION + 'post_team_iteration')

        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)

        self.mock_get_client = self.get_client.start()
        self.mock_get_classification_node = self.get_classification_node_patcher.start()
        self.mock_get_classification_nodes = self.get_classification_nodes_patcher.start()
        self.mock_delete_classification_node = self.delete_classification_node_patcher.start()
        self.mock_create_update_classification_node = self.create_update_classification_node_patcher.start()
        self.mock_update_classification_node = self.update_classification_node_patcher.start()
        self.mock_get_team_iterations = self.get_team_iterations_patcher.start()
        self.mock_get_team_iteration = self.get_team_iteration_patcher.start()
        self.mock_delete_team_iteration = self.delete_team_iteration_patcher.start()
        self.mock_post_team_iteration = self.post_team_iteration_patcher.start()
        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_project_iteration(self):
        response = get_project_iterations(depth=1,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_node.assert_called_once()
        list_project_iterations_param = self.mock_get_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, list_project_iterations_param['project'], str(list_project_iterations_param))
        self.assertEqual(self._STRUCTURE_GROUP, list_project_iterations_param['structure_group'], str(list_project_iterations_param))
        self.assertEqual(1, list_project_iterations_param['depth'], str(list_project_iterations_param))

    def test_list_project_iteration_with_depth_and_path(self):
        response = get_project_iterations(depth=3,path=self._ROOT_ITERATION_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_node.assert_called_once()
        list_project_iterations_param = self.mock_get_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, list_project_iterations_param['project'], str(list_project_iterations_param))
        self.assertEqual(self._STRUCTURE_GROUP, list_project_iterations_param['structure_group'], str(list_project_iterations_param))
        self.assertEqual(3, list_project_iterations_param['depth'], str(list_project_iterations_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, list_project_iterations_param['path'], str(list_project_iterations_param))

    def test_show_project_iteration(self):
        iteratin_ids_list = []
        iteratin_ids_list.append(1)
        response = get_project_iteration(id=self._ITERATION_ID,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_nodes.assert_called_once()
        show_project_iteration_param = self.mock_get_classification_nodes.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, show_project_iteration_param['project'], str(show_project_iteration_param))
        self.assertEqual(iteratin_ids_list, show_project_iteration_param['ids'], str(show_project_iteration_param))

    def test_delete_project_iteration(self):
        response = delete_project_iteration(path=self._ROOT_ITERATION_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_delete_classification_node.assert_called_once()
        delete_project_iteration_param = self.mock_delete_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, delete_project_iteration_param['project'], str(delete_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, delete_project_iteration_param['structure_group'], str(delete_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, delete_project_iteration_param['path'], str(delete_project_iteration_param))

    def test_create_project_iteration(self):
        response = create_project_iteration(name=self._ROOT_ITERATION_NAME,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        create_project_iteration_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_iteration_param['project'], str(create_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_iteration_param['structure_group'], str(create_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_NAME, create_project_iteration_param['posted_node'].name, str(create_project_iteration_param))
        #self.assertEqual(self._ROOT_ITERATION_PATH, create_project_iteration_param['path'], str(delete_project_iteration_param))

    def test_create_project_iteration_with_path(self):
        response = create_project_iteration(name=self._CHILD_ITERATION_NAME,path=self._ROOT_ITERATION_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        create_project_iteration_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_iteration_param['project'], str(create_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_iteration_param['structure_group'], str(create_project_iteration_param))
        self.assertEqual(self._CHILD_ITERATION_NAME, create_project_iteration_param['posted_node'].name, str(create_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, create_project_iteration_param['path'], str(create_project_iteration_param))

    def test_update_project_iteration(self):
        response = update_project_iteration(path=self._ROOT_ITERATION_PATH, name=self._NEW_ITERATION_NAME,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        #self.mock_create_update_classification_node.assert_called_once()
        self.mock_get_classification_node.assert_called_once()
        self.mock_update_classification_node.assert_called_once()
        update_project_iteration_param = self.mock_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, update_project_iteration_param['project'], str(update_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, update_project_iteration_param['structure_group'], str(update_project_iteration_param))
        self.assertEqual(self._NEW_ITERATION_NAME, update_project_iteration_param['posted_node'].name, str(update_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, update_project_iteration_param['path'], str(update_project_iteration_param))

    def test_move_project_iteration(self):
        child_iteration_id = '2'
        response = update_project_iteration(path=self._ROOT_ITERATION_PATH, name=self._NEW_ITERATION_NAME, child_id=child_iteration_id,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        self.mock_get_classification_node.assert_called_once()
        
        self.mock_update_classification_node.assert_called_once()
        update_project_iteration_param = self.mock_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, update_project_iteration_param['project'], str(update_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, update_project_iteration_param['structure_group'], str(update_project_iteration_param))
        self.assertEqual(self._NEW_ITERATION_NAME, update_project_iteration_param['posted_node'].name, str(update_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, update_project_iteration_param['path'], str(update_project_iteration_param))

        create_project_iteration_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_iteration_param['project'], str(create_project_iteration_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_iteration_param['structure_group'], str(create_project_iteration_param))
        self.assertEqual(child_iteration_id, create_project_iteration_param['posted_node'].id, str(create_project_iteration_param))
        self.assertEqual(self._ROOT_ITERATION_PATH, create_project_iteration_param['path'], str(create_project_iteration_param))

    def test_get_team_iterations(self):
        response = get_team_iterations(team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_iterations.assert_called_once()
        list_team_iterations_param = self.mock_get_team_iterations.call_args_list[0][1]
        self.assertEqual(self._TEAM, list_team_iterations_param['team_context'].team, str(list_team_iterations_param))
        self.assertEqual(self._TEST_PROJECT_NAME, list_team_iterations_param['team_context'].project, str(list_team_iterations_param))

    def test_get_team_iteration(self):
        response = get_team_iteration(id=self._ITERATION_IDENTIFIER,team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_iteration.assert_called_once()
        show_team_iteration_param = self.mock_get_team_iteration.call_args_list[0][1]
        self.assertEqual(self._TEAM, show_team_iteration_param['team_context'].team, str(show_team_iteration_param))
        self.assertEqual(self._TEST_PROJECT_NAME, show_team_iteration_param['team_context'].project, str(show_team_iteration_param))
        self.assertEqual(self._ITERATION_IDENTIFIER, show_team_iteration_param['id'], str(show_team_iteration_param))

    def test_remove_team_iteration(self):
        response = delete_team_iteration(id=self._ITERATION_IDENTIFIER,team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_delete_team_iteration.assert_called_once()
        remove_team_iteration_param = self.mock_delete_team_iteration.call_args_list[0][1]
        self.assertEqual(self._TEAM, remove_team_iteration_param['team_context'].team, str(remove_team_iteration_param))
        self.assertEqual(self._TEST_PROJECT_NAME, remove_team_iteration_param['team_context'].project, str(remove_team_iteration_param))
        self.assertEqual(self._ITERATION_IDENTIFIER, remove_team_iteration_param['id'], str(remove_team_iteration_param))

    def test_add_team_iteration(self):
        response = post_team_iteration(id=self._ITERATION_IDENTIFIER,team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_post_team_iteration.assert_called_once()
        create_team_iteration_param = self.mock_post_team_iteration.call_args_list[0][1]
        self.assertEqual(self._TEAM, create_team_iteration_param['team_context'].team, str(create_team_iteration_param))
        self.assertEqual(self._TEST_PROJECT_NAME, create_team_iteration_param['team_context'].project, str(create_team_iteration_param))
        self.assertEqual(self._ITERATION_IDENTIFIER, create_team_iteration_param['iteration'].id, str(create_team_iteration_param))
