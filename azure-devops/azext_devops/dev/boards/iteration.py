# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import WorkItemClassificationNode
from azext_devops.devops_sdk.v5_0.work.models import (TeamContext,
                                                      TeamSettingsIteration)
from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
from azext_devops.dev.common.services import (resolve_instance_and_project,
                                              get_work_item_tracking_client,
                                              get_work_client)
_STRUCTURE_GROUP_ITERATION = 'iterations'


def get_project_iterations(depth=1, path=None, organization=None, project=None, detect=None):
    """List iterations for a project.
    :param depth: Depth of children to fetch.
    :type depth: int
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    list_of_iterations = client.get_classification_node(project=project,
                                                        structure_group=_STRUCTURE_GROUP_ITERATION,
                                                        depth=depth, path=path)
    return list_of_iterations


def update_project_iteration(path, child_id=None, name=None, start_date=None,
                             finish_date=None,  organization=None, project=None, detect=None):
    """Update iteration.
    :param name: New name of the iteration.
    :type: str
    :param child_id: Add a child node for this iteration.
    :type: int
    """
    if start_date is None and finish_date is None and name is None and child_id is None:
        raise CLIError('At least one of --start-date , --finish-date , --child-id or --name arguments is required.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    if child_id:
        move_classification_node_object = WorkItemClassificationNode()
        move_classification_node_object.id = child_id
        update_iteration = client.create_or_update_classification_node(project=project,
                                                                       posted_node = move_classification_node_object,
                                                                       structure_group=_STRUCTURE_GROUP_ITERATION,
                                                                       path=path)
    
    classification_node_object = client.get_classification_node(project=project,
                                                                structure_group=_STRUCTURE_GROUP_ITERATION,
                                                                path=path)
    if classification_node_object.attributes is None and ((start_date and not finish_date) or (not start_date and finish_date)):
        raise CLIError('You must specify both start and finish dates or neither date')
    
    if classification_node_object.attributes is None:
        attributes_obj = {}
        classification_node_object.attributes = attributes_obj
    if start_date:
        start_date = convert_date_string_to_iso8601(value=start_date, argument='start_date')
        classification_node_object.attributes['startDate'] = start_date
    if finish_date:
        finish_date = convert_date_string_to_iso8601(value=finish_date, argument='finish_date')
        classification_node_object.attributes['finishDate'] = finish_date
        
    if name is not None:
        classification_node_object.name = name
    update_iteration = client.update_classification_node(project=project,
                                                         posted_node = classification_node_object,
                                                         structure_group=_STRUCTURE_GROUP_ITERATION,
                                                         path=path)
    return update_iteration


def delete_project_iteration(path, organization=None, project=None, detect=None):
    """Delete iteration for a project.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    response = client.delete_classification_node(project=project,
                                                 structure_group=_STRUCTURE_GROUP_ITERATION,
                                                 path=path)
    return response


def get_project_iteration(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Show iteration details for a project.
    :param id: Iteration ID.
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


def create_project_iteration(name, path=None, start_date=None, finish_date=None,
                             organization=None, project=None, detect=None):
    """Create iteration.
    :param name: Name of the iteration.
    :type: str
    """
    if start_date is None and finish_date is None and name is None:
        raise CLIError('At least one of --start-date , --finish-date or --name arguments is required.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    classification_node_object = WorkItemClassificationNode()
    if  ((start_date and not finish_date) or (not start_date and finish_date)):
        raise CLIError('You must specify both start and finish dates or neither date')
    else:
        if classification_node_object.attributes is None:
            attributes_obj = {}
            classification_node_object.attributes = attributes_obj
            if start_date:
                start_date = convert_date_string_to_iso8601(value=start_date, argument='start_date')
                classification_node_object.attributes['startDate'] = start_date
            if finish_date:
                finish_date = convert_date_string_to_iso8601(value=finish_date, argument='finish_date')
                classification_node_object.attributes['finishDate'] = finish_date
        
    if name is not None:
        classification_node_object.name = name
    response = client.create_or_update_classification_node(project=project,
                                                           posted_node = classification_node_object,
                                                           structure_group=_STRUCTURE_GROUP_ITERATION,
                                                           path=path)
    return response


def get_team_iterations(team, timeframe=None, organization=None, project=None, detect=None):
    """List iterations for a team.
    :param team: The name or id of the team.
    :type team: str
    :param timeframe: A filter for which iterations are returned based on relative time.
     Only Current is supported currently.
    :type: str
    :rtype: :class:`<WebApiTeam> <v5_0.core.models.WebApiTeam>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    list_of_iterations = client.get_team_iterations(team_context=team_context, timeframe=timeframe)
    return list_of_iterations


def get_team_iteration(id, team, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """ Get iteration details for a team.
    :param id: Identifier of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_iteration = client.get_team_iteration(team_context=team_context, id=id)
    return team_iteration


def delete_team_iteration(id, team, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """ Remove iteration from a team.
    :param id: Identifier of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_iteration = client.delete_team_iteration(team_context=team_context, id=id)
    return team_iteration


def post_team_iteration(id, team, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Add iteration to a team.
    :param id: Identifier of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_setting_iteration = TeamSettingsIteration(id=id)
    team_iteration = client.post_team_iteration(iteration=team_setting_iteration, team_context=team_context)
    return team_iteration
