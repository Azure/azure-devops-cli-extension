# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_boards_help():
    helps['boards'] = """
    type: group
    short-summary: Manage Azure Boards.
    long-summary: This command group is a part of the azure-devops extension.
    """

    helps['boards work-item'] = """
    type: group
    short-summary: Manage work items.
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
    long-summary: Update any area to include/exclude sub areas OR Set already added area as default.
    """

    helps['boards area team add'] = """
    type: command
    long-summary: Every team needs to have a default area configured which can't be empty.
                  Hence, you need to pass --set-as-default while adding first area to your team.
                  You can later configure any other area which already added to team as default
                  by using `az boards area team update -h` command.
    examples:
          - name: Add area to a team.
            text: |
                az boards area team add --team 'ContosoTeam' --path '\\ContosoProject\\MyProjectAreaName'
    """

    helps['boards work-item relation'] = """
    type: group
    short-summary: Manage work item relations.
    long-summary:
    """

    helps['boards work-item tag'] = """
    type: group
    short-summary: Manage work item tags.
    long-summary:
    """
