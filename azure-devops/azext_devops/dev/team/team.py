# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from vsts.core.v4_0.models.web_api_team import WebApiTeam
from azext_devops.dev.common.services import (get_core_client,
                                              resolve_instance_and_project)
from vsts.exceptions import VstsServiceError

def create_team(name, description=None, devops_organization=None, project=None, detect=None):
    """Create a team.
    :param name: Name of the new team.
    :type name: str
    :param description: Description of the new team
    :type description: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WebApiTeam> <core.v4_0.models.WebApiTeam>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        team_to_create = WebApiTeam(name=name, description=description)
        return core_client.create_team(team=team_to_create, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

def delete_team(team_id, devops_organization=None, project=None, detect=None):
    """Deletes a team.
    :param team_id: The name or id of the team to delete.
    :type team_id: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        return core_client.delete_team(team_id=team_id, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

def get_team(team_id, devops_organization=None, project=None, detect=None):
    """Gets a team.
    :param team_id: The name or id of the team to show.
    :type team_id: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        return core_client.get_team(team_id=team_id, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

    
def list_teams(top=None, skip=None, devops_organization=None, project=None, detect=None):
    """List teams.
    :param top: Maximum number of teams to return.
    :type top: int
    :param skip: Number of teams to skip.
    :type skip: int
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        return core_client.get_teams(top=top, skip=skip, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def list_team_members(team_id, top=None, skip=None, devops_organization=None, project=None, detect=None):
    """List members of a particular team.
    :param team_id: The name or id of the team to show members of.
    :type team_id: str
    :param top: Maximum number of members to return.
    :type top: int
    :param skip: Number of members to skip.
    :type skip: int
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        return core_client.get_team_members(team_id=team_id, top=top, skip=skip, project_id=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


def update_team(team_id, name=None, description=None, devops_organization=None, project=None, detect=None):
    """Update a team's name and/or description.
    :param team_id: The name or id of the team to be updated.
    :type team_id: str
    :param name: New name of the team.
    :type name: str
    :param description: New description of the team
    :type description: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    """
    if name is None and description is None:
        raise CLIError('Either name or description should be provided.')
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        core_client = get_core_client(devops_organization)
        updated_team_data = WebApiTeam(name=name, description=description)
        return core_client.update_team(team_data=updated_team_data, project_id=project, team_id=team_id)
    except VstsServiceError as ex:
        raise CLIError(ex)