# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_repos_help():
    helps['repos'] = """
    type: group
    short-summary: Manage Azure Repos.
    long-summary:
    """

    helps['repos pr'] = """
    type: group
    short-summary: Manage pull requests.
    long-summary:
    """

    helps['repos pr policies'] = """
    type: group
    short-summary: Manage pull request policy.
    long-summary:
    """

    helps['repos pr reviewers'] = """
    type: group
    short-summary: Manage pull request reviewers.
    long-summary:
    """

    helps['repos pr work-items'] = """
    type: group
    short-summary: Manage work items associated with pull requests.
    long-summary:
    """

    helps['repos import'] = """
    type: group
    short-summary: Manage Git repositories import
    long-summary:
    """
