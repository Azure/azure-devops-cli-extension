# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_team_help():
    helps['dev'] = """
    type: group
    short-summary: Commands to work with Azure DevOps Organization level operations.
    long-summary:
    """

    helps['dev project'] = """
    type: group
    short-summary: Commands to work with and manage team projects.
    long-summary:
    """
