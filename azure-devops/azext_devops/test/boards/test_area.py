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

from azext_devops.devops_sdk.v5_0.work.models import (TeamFieldValue,
                                                      TeamFieldValuesPatch)
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.test.utils.helper import get_client_mock_helper
from azext_devops.dev.boards.area import (get_project_areas,
                                          get_project_area,
                                          delete_project_area,
                                          create_project_area,
                                          update_project_area,
                                          get_team_areas,
                                          add_team_area,
                                          remove_team_area,
                                          update_team_area)

class TestBoardsAreaMethods(AuthenticatedTests):
    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_PROJECT_NAME = 'sample_project'
    _WORK_ITEM_TRACKING_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.'
    _WORK_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work.work_client.WorkClient.'
    _STRUCTURE_GROUP = 'areas'
    _ROOT_AREA_NAME = 'root_area'
    _ROOT_AREA_PATH = _TEST_PROJECT_NAME + '\\' + _ROOT_AREA_NAME 
    _CHILD_AREA_NAME = 'child_area'
    _CHILD_AREA_PATH = _ROOT_AREA_PATH + '\\' + _CHILD_AREA_NAME 
    _NEW_AREA_NAME = 'root_area_renamed'
    _TEAM = 'sample_team'
    _AREA_ID = 1
    _AREA_IDENTIFIER = 'some-guid'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_classification_nodes_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'get_classification_nodes')
        self.get_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'get_classification_node')
        self.delete_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'delete_classification_node')
        self.create_update_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'create_or_update_classification_node')
        self.update_classification_node_patcher = patch(self._WORK_ITEM_TRACKING_CLIENT_LOCATION + 'update_classification_node')
        self.get_team_field_values_patcher = patch(self._WORK_CLIENT_LOCATION + 'get_team_field_values')
        self.update_team_field_values_patcher = patch(self._WORK_CLIENT_LOCATION + 'update_team_field_values')

        self.get_client = patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper)

        self.mock_get_client = self.get_client.start()
        self.mock_get_classification_node = self.get_classification_node_patcher.start()
        self.mock_get_classification_nodes = self.get_classification_nodes_patcher.start()
        self.mock_delete_classification_node = self.delete_classification_node_patcher.start()
        self.mock_create_update_classification_node = self.create_update_classification_node_patcher.start()
        self.mock_update_classification_node = self.update_classification_node_patcher.start()
        self.mock_get_team_field_values = self.get_team_field_values_patcher.start()
        self.mock_update_team_field_values = self.update_team_field_values_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_list_project_areas(self):
        response = get_project_areas(depth=1,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_node.assert_called_once()
        list_project_areas_param = self.mock_get_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, list_project_areas_param['project'], str(list_project_areas_param))
        self.assertEqual(self._STRUCTURE_GROUP, list_project_areas_param['structure_group'], str(list_project_areas_param))
        self.assertEqual(1, list_project_areas_param['depth'], str(list_project_areas_param))

    def test_list_project_area_with_depth_and_path(self):
        response = get_project_areas(depth=3,path=self._ROOT_AREA_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_node.assert_called_once()
        list_project_areas_param = self.mock_get_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, list_project_areas_param['project'], str(list_project_areas_param))
        self.assertEqual(self._STRUCTURE_GROUP, list_project_areas_param['structure_group'], str(list_project_areas_param))
        self.assertEqual(3, list_project_areas_param['depth'], str(list_project_areas_param))
        self.assertEqual(self._ROOT_AREA_PATH, list_project_areas_param['path'], str(list_project_areas_param))
    
    def test_show_project_area(self):
        area_ids_list = []
        area_ids_list.append(1)
        response = get_project_area(id=self._AREA_ID,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_nodes.assert_called_once()
        show_project_area_param = self.mock_get_classification_nodes.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, show_project_area_param['project'], str(show_project_area_param))
        self.assertEqual(area_ids_list, show_project_area_param['ids'], str(show_project_area_param))

    def test_delete_project_area(self):
        response = delete_project_area(path=self._ROOT_AREA_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_delete_classification_node.assert_called_once()
        delete_project_area_param = self.mock_delete_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, delete_project_area_param['project'], str(delete_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, delete_project_area_param['structure_group'], str(delete_project_area_param))
        self.assertEqual(self._ROOT_AREA_PATH, delete_project_area_param['path'], str(delete_project_area_param))


    def test_create_project_area(self):
        response = create_project_area(name=self._ROOT_AREA_NAME,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        create_project_area_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_area_param['project'], str(create_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_area_param['structure_group'], str(create_project_area_param))
        self.assertEqual(self._ROOT_AREA_NAME, create_project_area_param['posted_node'].name, str(create_project_area_param))

    def test_create_project_area_with_path(self):
        response = create_project_area(name=self._CHILD_AREA_NAME,path=self._ROOT_AREA_PATH,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        create_project_area_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_area_param['project'], str(create_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_area_param['structure_group'], str(create_project_area_param))
        self.assertEqual(self._CHILD_AREA_NAME, create_project_area_param['posted_node'].name, str(create_project_area_param))
        self.assertEqual(self._ROOT_AREA_PATH, create_project_area_param['path'], str(create_project_area_param))

    def test_update_project_area(self):
        response = update_project_area(path=self._ROOT_AREA_PATH, name=self._NEW_AREA_NAME,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_get_classification_node.assert_called_once()
        self.mock_update_classification_node.assert_called_once()
        update_project_area_param = self.mock_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, update_project_area_param['project'], str(update_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, update_project_area_param['structure_group'], str(update_project_area_param))
        self.assertEqual(self._NEW_AREA_NAME, update_project_area_param['posted_node'].name, str(update_project_area_param))
        self.assertEqual(self._ROOT_AREA_PATH, update_project_area_param['path'], str(update_project_area_param))

    def test_move_project_area(self):
        child_area_id = '2'
        response = update_project_area(path=self._ROOT_AREA_PATH, name=self._NEW_AREA_NAME, child_id=child_area_id,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        #assert
        self.mock_create_update_classification_node.assert_called_once()
        self.mock_get_classification_node.assert_called_once()
        
        self.mock_update_classification_node.assert_called_once()
        update_project_area_param = self.mock_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, update_project_area_param['project'], str(update_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, update_project_area_param['structure_group'], str(update_project_area_param))
        self.assertEqual(self._NEW_AREA_NAME, update_project_area_param['posted_node'].name, str(update_project_area_param))
        self.assertEqual(self._ROOT_AREA_PATH, update_project_area_param['path'], str(update_project_area_param))

        create_project_area_param = self.mock_create_update_classification_node.call_args_list[0][1]
        self.assertEqual(self._TEST_PROJECT_NAME, create_project_area_param['project'], str(create_project_area_param))
        self.assertEqual(self._STRUCTURE_GROUP, create_project_area_param['structure_group'], str(create_project_area_param))
        self.assertEqual(child_area_id, create_project_area_param['posted_node'].id, str(create_project_area_param))
        self.assertEqual(self._ROOT_AREA_PATH, create_project_area_param['path'], str(create_project_area_param))

    def test_get_team_areas(self):
        response = get_team_areas(team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_field_values.assert_called_once()
        list_team_areas_param = self.mock_get_team_field_values.call_args_list[0][1]
        self.assertEqual(self._TEAM, list_team_areas_param['team_context'].team, str(list_team_areas_param))
        self.assertEqual(self._TEST_PROJECT_NAME, list_team_areas_param['team_context'].project, str(list_team_areas_param))

    def test_update_team_area(self):
        self.mock_get_team_field_values.return_value = self._prepare_team_field_values_patch_object(path=self._CHILD_AREA_PATH, include_children=False, is_default=False)
        self.mock_update_team_field_values.return_value = self._prepare_team_field_values_patch_object(path=self._CHILD_AREA_PATH, include_children=True, is_default=True)
        response = update_team_area(path=self._CHILD_AREA_PATH, set_as_default=True, include_sub_areas=True, team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_field_values.assert_called_once()
        update_team_area_param = self.mock_update_team_field_values.call_args_list[0][1]
        self.assertEqual(self._TEAM, update_team_area_param['team_context'].team, str(update_team_area_param))
        self.assertEqual(self._TEST_PROJECT_NAME, update_team_area_param['team_context'].project, str(update_team_area_param))
        area_path_include_children= False
        area_path_found = False
        area_path_is_default = False
        for entry in response.values:
            if self._CHILD_AREA_PATH ==  entry.value:
                area_path_found = True
                area_path_include_children = ( entry.include_children is True )
        if response.default_value == self._CHILD_AREA_PATH:
            area_path_is_default = True
        self.assertEqual(area_path_found, True)
        self.assertEqual(area_path_is_default, True)
        self.assertEqual(area_path_include_children, True)

    def test_remove_team_area(self):
        self.mock_get_team_field_values.return_value = self._prepare_team_field_values_patch_object(path=self._CHILD_AREA_PATH, include_children=False, is_default=False)
        response = remove_team_area(path=self._CHILD_AREA_PATH,team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_field_values.assert_called_once()
        self.mock_update_team_field_values.assert_called_once()
        remove_team_area_param = self.mock_update_team_field_values.call_args_list[0][1]
        self.assertEqual(self._TEAM, remove_team_area_param['team_context'].team, str(remove_team_area_param))
        self.assertEqual(self._TEST_PROJECT_NAME, remove_team_area_param['team_context'].project, str(remove_team_area_param))
        updated_team_field_values = remove_team_area_param['patch'].values
        for entry in updated_team_field_values:
            self.assertNotEqual(self._CHILD_AREA_PATH, entry.value , str(remove_team_area_param))

    def test_add_team_area(self):
        self.mock_update_team_field_values.return_value = self._prepare_team_field_values_patch_object(path=self._CHILD_AREA_PATH, include_children=True, is_default=False)
        response = add_team_area(path=self._CHILD_AREA_PATH,team=self._TEAM,project=self._TEST_PROJECT_NAME,organization=self._TEST_DEVOPS_ORGANIZATION)
        self.mock_get_team_field_values.assert_called_once()
        self.mock_update_team_field_values.assert_called_once()
        add_team_area_param = self.mock_update_team_field_values.call_args_list[0][1]
        self.assertEqual(self._TEAM, add_team_area_param['team_context'].team, str(add_team_area_param))
        self.assertEqual(self._TEST_PROJECT_NAME, add_team_area_param['team_context'].project, str(add_team_area_param))
        area_path_found = False
        for entry in response.values:
            if self._CHILD_AREA_PATH ==  entry.value:
                area_path_found = True
        self.assertEqual(area_path_found, True)


    def _prepare_team_field_values_patch_object(self, path, include_children=False, is_default=True):
        patch_obj = TeamFieldValuesPatch()
        patch_obj.values = []
        # add root node
        team_field_value = TeamFieldValue(include_children=False, value=self._ROOT_AREA_PATH)
        patch_obj.values.append(team_field_value)
        patch_obj.default_value = self._ROOT_AREA_PATH
        # add child node
        team_field_value = TeamFieldValue(include_children=include_children, value=path)
        if is_default:
            patch_obj.default_value = path
        patch_obj.values.append(team_field_value)
        team_field_value = TeamFieldValue(include_children=False, value=self._ROOT_AREA_PATH)
        patch_obj.values.append(team_field_value)
        return patch_obj
