# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

from azext_devops.devops_sdk.v5_0.work.models import (TeamContext,
                                                      TeamSettingsIteration)
from azext_devops.dev.common.services import (resolve_instance_and_project,
                                              get_work_client)


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


def get_team_iteration(id, team, organization=None, project=None, detect=None):
    """ Get iteration details for a team.
    :param id: ID of the iteration.
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


def delete_team_iteration(id, team, organization=None, project=None, detect=None):
    """ Remove iteration from a team.
    :param id: ID of the iteration.
    :type: str
    :param team: Name or ID of the team.
    :type: str
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_work_client(organization)
    team_context = TeamContext(project=project, team=team)
    team_iteration = client.delete_team_iteration(team_context=team_context, id=id)
    return team_iteration


def post_team_iteration(id, team, organization=None, project=None, detect=None):
    """Add iteration to a team.
    :param id: ID of the iteration.
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
