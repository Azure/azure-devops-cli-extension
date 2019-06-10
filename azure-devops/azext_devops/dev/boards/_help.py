# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_boards_help():
    helps['boards'] = """
    type: group
    short-summary: Manage Azure Boards.
    long-summary:
    """

    helps['boards work-item'] = """
    type: group
    short-summary: Manage work items.
    long-summary:
    """

    helps['boards query'] = """
    type: command
    short-summary: Manage queries.
    long-summary:
    """

    helps['boards iteration'] = """
    type: group
    short-summary: Manage iterations.
    long-summary:
    """

    helps['boards iteration team'] = """
    type: group
    short-summary: Manage iterations for a team.
    long-summary:
    """

    helps['boards iteration project'] = """
    type: group
    short-summary: Manage iterations for a project.
    long-summary:
    """

    helps['boards iteration project update'] = """
    type: command
    long-summary: Move iteration or update iteration details like name AND/OR start-date and finish-date.
    """

    helps['boards area'] = """
    type: group
    short-summary: Manage area paths.
    long-summary:
    """

    helps['boards area project'] = """
    type: group
    short-summary: Manage areas for a project.
    long-summary:
    """

    helps['boards area project update'] = """
    type: command
    long-summary: Move area or update area name.
    """

    helps['boards area team'] = """
    type: group
    short-summary: Manage areas for a team.
    long-summary:
    """

    helps['boards area team update'] = """
    type: command
    long-summary:Update any area to include/exclude sub areas OR Set already added area as default.
    """

    helps['boards work-item relation'] = """
    type: group
    short-summary: Manage work item relations.
    long-summary:
    """
