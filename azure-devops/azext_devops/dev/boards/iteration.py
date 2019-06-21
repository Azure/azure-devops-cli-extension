# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.devops_sdk.exceptions import AzureDevOpsServiceError
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import WorkItemClassificationNode
from azext_devops.devops_sdk.v5_0.work.models import (TeamContext,
                                                      TeamSettingsIteration,
                                                      TeamSettingsPatch)
from azext_devops.dev.common.arguments import convert_date_only_string_to_iso8601
from azext_devops.dev.common.services import (resolve_instance_and_project,
                                              get_work_item_tracking_client,
                                              get_work_client)
from azext_devops.dev.common.uuid import EMPTY_UUID
from .boards_helper import resolve_classification_node_path, handle_common_boards_errors

logger = get_logger(__name__)

_STRUCTURE_GROUP_ITERATION = 'iterations'


def get_project_iterations(depth=1, path=None, organization=None, project=None, detect=None):
    """List iterations for a project.
    :param depth: Depth of child nodes to be fetched. Example: --depth 3.
    :type depth: int
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    if path:
        path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_ITERATION)
    list_of_iterations = client.get_classification_node(project=project,
                                                        structure_group=_STRUCTURE_GROUP_ITERATION,
                                                        depth=depth, path=path)
    return list_of_iterations


def update_project_iteration(path, child_id=None, name=None, start_date=None,
                             finish_date=None, organization=None, project=None, detect=None):
    """Update project iteration.
    :param name: New name of the iteration.
    :type: str
    :param child_id: Move an existing iteration and add as child node for this iteration.
    :type: int
    """
    if start_date is None and finish_date is None and name is None and child_id is None:
        raise CLIError('At least one of --start-date , --finish-date , --child-id or --name arguments is required.')
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_ITERATION)
    if child_id:
        move_classification_node_object = WorkItemClassificationNode()
        move_classification_node_object.id = child_id
        update_iteration = client.create_or_update_classification_node(project=project,
                                                                       posted_node=move_classification_node_object,
                                                                       structure_group=_STRUCTURE_GROUP_ITERATION,
                                                                       path=path)
    classification_node_object = client.get_classification_node(project=project,
                                                                structure_group=_STRUCTURE_GROUP_ITERATION,
                                                                path=path)
    if classification_node_object.attributes is None and \
       ((start_date and not finish_date) or (not start_date and finish_date)):
        raise CLIError('You must specify both start and finish dates or neither date')
    if classification_node_object.attributes is None:
        attributes_obj = {}
        classification_node_object.attributes = attributes_obj
    if start_date:
        start_date = convert_date_only_string_to_iso8601(value=start_date, argument='start_date')
        classification_node_object.attributes['startDate'] = start_date
    if finish_date:
        finish_date = convert_date_only_string_to_iso8601(value=finish_date, argument='finish_date')
        classification_node_object.attributes['finishDate'] = finish_date
    if name is not None:
        classification_node_object.name = name
    update_iteration = client.update_classification_node(project=project,
                                                         posted_node=classification_node_object,
                                                         structure_group=_STRUCTURE_GROUP_ITERATION,
                                                         path=path)
    return update_iteration


def delete_project_iteration(path, organization=None, project=None, detect=None):
    """Delete iteration.
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_work_item_tracking_client(organization)
    path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_ITERATION)
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
    if path:
        path = resolve_classification_node_path(client, path, project, _STRUCTURE_GROUP_ITERATION)
    classification_node_object = WorkItemClassificationNode()
    if ((start_date and not finish_date) or (not start_date and finish_date)):
        raise CLIError('You must specify both start and finish dates or neither date')
    if classification_node_object.attributes is None:
        attributes_obj = {}
        classification_node_object.attributes = attributes_obj
        if start_date:
            start_date = convert_date_only_string_to_iso8601(value=start_date, argument='start_date')
            classification_node_object.attributes['startDate'] = start_date
        if finish_date:
            finish_date = convert_date_only_string_to_iso8601(value=finish_date, argument='finish_date')
            classification_node_object.attributes['finishDate'] = finish_date
    if name is not None:
        classification_node_object.name = name
    response = client.create_or_update_classification_node(project=project,
                                                           posted_node=classification_node_object,
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


def delete_team_iteration(id, team, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Remove iteration from a team.
    :param id: Identifier of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    try:
        team_iteration = client.delete_team_iteration(team_context=team_context, id=id)
        return team_iteration
    except AzureDevOpsServiceError as ex:
        handle_common_boards_errors(ex)


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
    try:
        team_iteration = client.post_team_iteration(iteration=team_setting_iteration, team_context=team_context)
        return team_iteration
    except AzureDevOpsServiceError as ex:
        _handle_empty_backlog_iteration_id(ex=ex, client=client, team_context=team_context)


def list_iteration_work_items(id, team, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """List work-items for an iteration.
    :param id: Identifier of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    work_items = client.get_iteration_work_items(iteration_id=id, team_context=team_context)
    wit_client = get_work_item_tracking_client(organization)
    relation_types = wit_client.get_relation_types()
    work_items = _fill_friendly_name_for_relations_in_iteration_work_items(relation_types_from_service=relation_types,
                                                                           iteration_work_items=work_items)
    return work_items


def set_default_iteration(team, id=None, default_iteration_macro=None, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Set default iteration for a team.
    :param id: Identifier of the iteration which needs to be set as default.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    :param default_iteration_macro: Default iteration macro. Example: @CurrentIteration.
    :type: str
    """
    if default_iteration_macro is None and id is None:
        raise CLIError('Either --id or --default-iteration-macro is required.')
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    patch_object = TeamSettingsPatch()
    if id:
        patch_object.default_iteration = id
    if default_iteration_macro:
        patch_object.default_iteration_macro = default_iteration_macro
    team_iteration_setting = client.update_team_settings(team_settings_patch=patch_object, team_context=team_context)
    return team_iteration_setting


def set_backlog_iteration(team, id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Set backlog iteration for a team.
    :param id: Identifier of the iteration which needs to be set as backlog iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    patch_object = TeamSettingsPatch()
    patch_object.backlog_iteration = id
    team_iteration_setting = client.update_team_settings(team_settings_patch=patch_object, team_context=team_context)
    return team_iteration_setting


def show_default_iteration(team, organization=None, project=None, detect=None):
    """Show default iteration for a team.
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_iteration_setting = client.get_team_settings(team_context=team_context)
    return team_iteration_setting


def show_backlog_iteration(team, organization=None, project=None, detect=None):
    """Show backlog iteration for a team.
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_iteration_setting = client.get_team_settings(team_context=team_context)
    return team_iteration_setting


def _fill_friendly_name_for_relations_in_iteration_work_items(relation_types_from_service, iteration_work_items):
    if not iteration_work_items.work_item_relations:
        return iteration_work_items
    for relation in iteration_work_items.work_item_relations:
        for relation_type_from_service in relation_types_from_service:
            if relation_type_from_service.reference_name == relation.rel:
                relation.rel = relation_type_from_service.name
    return iteration_work_items


def _handle_empty_backlog_iteration_id(ex, client, team_context):
    logger.debug(ex, exc_info=True)
    exception_message_str = r'The guid specified for parameter rootIterationId must not be Guid.Empty.'
    if exception_message_str in ex.message:
        # Check if backlog iteration ID is empty
        backlog_setting = client.get_team_settings(team_context=team_context)
        if backlog_setting.backlog_iteration.id == EMPTY_UUID:
            raise CLIError('No backlog iteration has been selected for your team. '
                           'Before you can select iterations for your team to participate in, '
                           'you must first specify a backlog iteration.'
                           '\nYou can set backlog iteration by running following command: '
                           'az boards iteration team set-backlog-iteration --team <TeamID> --id <BacklogIterationID>')
    handle_common_boards_errors(ex)
