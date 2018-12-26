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
