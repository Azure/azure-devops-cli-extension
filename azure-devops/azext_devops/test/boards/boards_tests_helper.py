# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.devops_sdk.v5_0.work_item_tracking.models import WorkItemClassificationNode

PATH_SEPARATOR = '\\'
TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
TEST_PROJECT_NAME = 'sample_project'
WORK_ITEM_TRACKING_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient.'
WORK_CLIENT_LOCATION = 'azext_devops.devops_sdk.v5_0.work.work_client.WorkClient.'
TEST_TEAM_NAME = 'sample_team'

def get_root_nodes_response():
    root_nodes_list = []
    classification_node1 = WorkItemClassificationNode()
    classification_node1.structure_type = 'area'
    classification_node1.name = TEST_PROJECT_NAME
    classification_node1.additional_properties['path'] = PATH_SEPARATOR + TEST_PROJECT_NAME + PATH_SEPARATOR + 'Area'
    root_nodes_list.append(classification_node1)
    classification_node2 = WorkItemClassificationNode()
    classification_node2.structure_type = 'iteration'
    classification_node2.name = TEST_PROJECT_NAME
    classification_node2.additional_properties['path'] = PATH_SEPARATOR + TEST_PROJECT_NAME + PATH_SEPARATOR + 'Iteration'
    root_nodes_list.append(classification_node2)
    return root_nodes_list