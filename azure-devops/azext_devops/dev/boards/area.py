# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import WorkItemClassificationNode
from azext_devops.devops_sdk.v5_0.work.models import (TeamContext,
                                                      TeamFieldValuesPatch,
                                                      TeamFieldValue)
from azext_devops.dev.common.services import (resolve_instance_and_project,
                                              get_work_item_tracking_client,
                                              get_work_client)
from .boards_helper import resolve_classification_node_path
_STRUCTURE_GROUP_AREA = 'areas'


def get_project_areas(depth=1, path=None, organization=None, project=None, detect=None):
    """List areas for a project.
    :param depth: Depth of child nodes to be fetched. Example: --depth 3
    :type depth: int
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    if path:
        path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_AREA)
    list_of_areas = client.get_classification_node(project=project,
                                                   structure_group=_STRUCTURE_GROUP_AREA,
                                                   depth=depth, path=path)    
    return list_of_areas


def delete_project_area(path, organization=None, project=None, detect=None):
    """Delete area.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_AREA)
    response = client.delete_classification_node(project=project,
                                                 structure_group=_STRUCTURE_GROUP_AREA,
                                                 path=path)
    return response


def create_project_area(name, path=None, organization=None, project=None, detect=None):
    """Create area.
    :param name: Name of the area.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    if path:
        path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_AREA)
    classification_node_object = WorkItemClassificationNode()
    classification_node_object.name = name
    response = client.create_or_update_classification_node(project=project,
                                                           posted_node=classification_node_object,
                                                           structure_group=_STRUCTURE_GROUP_AREA,
                                                           path=path)
    return response


def get_project_area(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
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


def update_project_area(path, name=None, child_id=None, organization=None, project=None, detect=None):
    """Update area.
    :param name: New name of the area.
    :type: str
    :param child_id: Move an existing area and add as child node for this area.
    :type: int
    """
    if name is None and child_id is None:
        raise CLIError('Either --name or --child-id should be provided.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_AREA)
    if child_id:
        move_classification_node_object = WorkItemClassificationNode()
        move_classification_node_object.id = child_id
        response = client.create_or_update_classification_node(project=project,
                                                               posted_node=move_classification_node_object,
                                                               structure_group=_STRUCTURE_GROUP_AREA,
                                                               path=path)
    classification_node_object = client.get_classification_node(project=project,
                                                                structure_group=_STRUCTURE_GROUP_AREA,
                                                                path=path)
    if name is not None:
        classification_node_object.name = name
        response = client.update_classification_node(project=project,
                                                     posted_node=classification_node_object,
                                                     structure_group=_STRUCTURE_GROUP_AREA,
                                                     path=path)
    return response


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


def add_team_area(path, team, set_as_default=False, include_sub_areas=None,
                  organization=None, project=None, detect=None):
    """Add area to a team.
    :param set_as_default: Set this area path as default area for this team. Default: False
    :type set_as_default: bool
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    get_response = client.get_team_field_values(team_context=team_context)
    patch_doc = TeamFieldValuesPatch()
    patch_doc.values = get_response.values
    if include_sub_areas is None:
        include_sub_areas = False
    team_field_value = TeamFieldValue(include_children=include_sub_areas, value=path)
    if set_as_default:
        patch_doc.default_value = path
    else:
        patch_doc.default_value = get_response.default_value
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
    if get_response.default_value == path:
        raise CLIError('You are trying to remove the default area for this team. '
                       'Please change the default area node and then try this command again.')
    area_found = False
    for entry in get_response.values:
        if path == entry.value[:]:
            area_found = True
            get_response.values.remove(entry)
    if not area_found:
        raise CLIError('Path is not added to team area list.')
    patch_doc = TeamFieldValuesPatch()
    patch_doc.values = get_response.values
    patch_doc.default_value = get_response.default_value
    update_response = client.update_team_field_values(patch=patch_doc, team_context=team_context)
    return update_response


def update_team_area(path, team, include_sub_areas=None, set_as_default=False,
                     organization=None, project=None, detect=None):
    """Update team area.
    :param set_as_default: Set as default team area path. Default: False
    :type set_as_default: bool
    """
    if include_sub_areas is None and set_as_default is False:
        raise CLIError('Either --set-as-default or --include-sub-areas parameter should be provided.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    get_response = client.get_team_field_values(team_context=team_context)
    patch_doc = TeamFieldValuesPatch()
    area_found = False
    for entry in get_response.values:
        if path == entry.value[:]:
            area_found = True
            if include_sub_areas is not None:
                entry.include_children = include_sub_areas
            if set_as_default is True:
                patch_doc.default_value = path
            else:
                patch_doc.default_value = get_response.default_value
    if not area_found:
        raise CLIError('Path is not added to team area list.')
    patch_doc.values = get_response.values
    update_response = client.update_team_field_values(patch=patch_doc, team_context=team_context)
    return update_response
