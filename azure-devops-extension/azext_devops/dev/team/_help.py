# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_team_help():
    helps['devops'] = """
    type: group
    short-summary: Manage Azure DevOps organization level operations.
    long-summary: |
        Other Related Groups 
        az pipelines: Manage Azure DevOps Pipelines 
        az boards: Manage Azure DevOps Boards
        az repos: Manage Azure DevOps Repos
        az artifacts: Manage Azure DevOps Artifacts
        """

    helps['devops project'] = """
    type: group
    short-summary: Manage team projects.
    """

    helps['devops service-endpoint'] = """
    type: group
    short-summary: Manage service endpoints/service connections
    long-summary: https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints
    """