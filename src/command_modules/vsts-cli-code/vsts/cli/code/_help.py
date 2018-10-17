# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_repos_help():
    helps['dev code'] = """
    type: group
    short-summary: Commands to work with and manage code repositories.
    long-summary:
    """

    helps['dev code pr'] = """
    type: group
    short-summary: Manage pull requests.
    long-summary:
    """

    helps['dev code pr policies'] = """
    type: group
    short-summary: Manage pull request policy.
    long-summary:
    """

    helps['dev code pr reviewers'] = """
    type: group
    short-summary: Manage pull request reviewers.
    long-summary:
    """

    helps['dev code pr work-items'] = """
    type: group
    short-summary: Manage work items associated with pull requests.
    long-summary:
    """

    helps['dev code repo'] = """
    type: group
    short-summary: Manage repositories.
    long-summary:
    """