# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.core.v4_0.models.web_api_team import WebApiTeam
from azext_devops.dev.common.services import (get_core_client,
                                              resolve_instance_and_project)

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
        return core_client.create_team(team_to_create, project)
    except VstsServiceError as ex:
        raise CLIError(ex)
