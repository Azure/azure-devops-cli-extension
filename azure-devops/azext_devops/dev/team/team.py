# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.vstsCompressed.core.v4_0.models.models import WebApiTeam
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.dev.common.services import (get_core_client,
                                              resolve_instance_and_project)


def create_team(name, description=None, organization=None, project=None, detect=None):
    """Create a team.
    :param name: Name of the new team.
    :type name: str
    :param description: Description of the new team.
    :type description: str
    :rtype: :class:`<WebApiTeam> <core.v4_0.models.WebApiTeam>`
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        team_to_create = WebApiTeam(name=name, description=description)
        return core_client.create_team(team=team_to_create, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_team(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a team.
    :param id: The id (UUID) of the team to delete.
    :type id: str
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        return core_client.delete_team(team_id=id, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def get_team(team, organization=None, project=None, detect=None):
    """Show team details.
    :param team: The name or id of the team to show.
    :type team: str
    :rtype: :class:`<WebApiTeam> <core.v4_0.models.WebApiTeam>`
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        return core_client.get_team(team_id=team, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def get_teams(top=None, skip=None, organization=None, project=None, detect=None):
    """List all teams in a project.
    :param top: Maximum number of teams to return.
    :type top: int
    :param skip: Number of teams to skip.
    :type skip: int
    :rtype: [WebApiTeam]
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        return core_client.get_teams(top=top, skip=skip, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def get_team_members(team, top=None, skip=None, organization=None, project=None, detect=None):
    """List members of a team.
    :param team: The name or id of the team to show members of.
    :type team: str
    :param top: Maximum number of members to return.
    :type top: int
    :param skip: Number of members to skip.
    :type skip: int
    :rtype: [IdentityRef]
    """
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        return core_client.get_team_members(team_id=team, top=top, skip=skip, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def update_team(team, name=None, description=None, organization=None, project=None, detect=None):
    """Update a team's name and/or description.
    :param team: The name or id of the team to be updated.
    :type team: str
    :param name: New name of the team.
    :type name: str
    :param description: New description of the team.
    :type description: str
    :rtype: :class:`<WebApiTeam> <core.v4_0.models.WebApiTeam>`
    """
    if name is None and description is None:
        raise CLIError('Either name or description argument must be provided.')
    try:
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
        core_client = get_core_client(organization)
        updated_team_data = WebApiTeam(name=name, description=description)
        return core_client.update_team(team_data=updated_team_data, project_id=project, team_id=team)
    except VstsServiceError as ex:
        raise CLIError(ex)
