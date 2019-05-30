# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import WorkItemClassificationNode
from azext_devops.devops_sdk.v5_0.work.models import (TeamContext,
                                                      TeamFieldValuesPatch,
                                                      TeamFieldValue,)
from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
from azext_devops.dev.common.services import (resolve_instance_and_project,
                                              get_work_item_tracking_client,
                                              get_work_client)


def get_project_areas(depth=1, path=None, organization=None, project=None, detect=None):
    """List areas for a project.
    :param depth: Depth of children to fetch.
    :type depth: int
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    list_of_areas = client.get_classification_node(project=project,
                                                        structure_group='areas',
                                                        depth=depth, path=path)
    return list_of_areas
    

def delete_project_area(path, organization=None, project=None, detect=None):
    """Delete area for a project.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    response = client.delete_classification_node(project=project,
                                                 structure_group='areas',
                                                 path=path)
    return response


def create_project_area(name, path=None, organization=None, project=None, detect=None):
    """Create area path.
    :param name: Name of the area.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    classification_node_object = WorkItemClassificationNode()    
    classification_node_object.name = name
    response = client.create_or_update_classification_node(project=project,
                                                          posted_node = classification_node_object,
                                                          structure_group='areas',
                                                          path=path)
    return response


def get_project_area(id, organization=None, project=None, detect=None):
    """Show area details for a project.
    :param id: Area ID.
    :type id: int
    """
    ids = [int(id)]
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    response = client.get_classification_nodes(project=project,
                                               ids=ids)
    return response


def update_project_area(path=None, name=None, new_path_id=None, organization=None, project=None, detect=None):
    """Update Area.
    :param name: New name of the area.
    :type: str
    :param new_path_id: ID of the New path for this area.
    :type: int
    """
    if name is None and new_path_id is None:
        raise CLIError('Either --name or new-path should be provided.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    classification_node_object = client.get_classification_node(project=project,
                                                                structure_group='areas',
                                                                path=path)
    if name is not None:
        classification_node_object.name = name
    update_area = client.update_classification_node(project=project,
                                                    posted_node = classification_node_object,
                                                    structure_group='areas',
                                                    path=path)
    if new_path_id:
        move_classification_node_object = WorkItemClassificationNode()
        move_classification_node_object.id = new_path_id
        move_area = client.create_or_update_classification_node(project=project,
                                                          posted_node = move_classification_node_object,
                                                          structure_group='areas',
                                                          path=path)
    return move_area

def get_team_areas(team, organization=None, project=None, detect=None):
    """List areas for a team.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    list_of_areas = client.get_team_field_values(team_context=team_context)
    return list_of_areas


def add_team_area(path, team, include_sub_areas=None, organization=None, project=None, detect=None):
    """Add area to a team.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    get_response = client.get_team_field_values(team_context=team_context)
    patch_doc = TeamFieldValuesPatch()
    patch_doc.default_value = get_response.default_value
    patch_doc.values = get_response.values
    if include_sub_areas is None:
        include_sub_areas = False
    team_field_value = TeamFieldValue(include_children=include_sub_areas, value=path)
    patch_doc.values.append(team_field_value)
    update_response = client.update_team_field_values(patch=patch_doc, team_context=team_context)
    return update_response


def remove_team_area(path, team, organization=None, project=None, detect=None):
    """Remove area from a team.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    get_response = client.get_team_field_values(team_context=team_context)
    for entry in get_response.values:
        if path == entry.value[:]:
            get_response.values.remove(entry)
    patch_doc = TeamFieldValuesPatch()
    patch_doc.default_value = get_response.default_value
    patch_doc.values = get_response.values
    update_response = client.update_team_field_values(patch=patch_doc, team_context=team_context)
    return update_response


def configure_team_area(default_area, team, include_sub_areas=None, organization=None, project=None, detect=None):
    """Configure default area for a team.
    :param default_area:default_area: Default area path value
    :type default_area: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    get_response = client.get_team_field_values(team_context=team_context)
    get_response.default_value = default_area
    update_response = client.update_team_field_values(patch=get_response, team_context=team_context)
    return update_response