# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_boards_help():
    helps['boards'] = """
    type: group
    short-summary: Commands to work with and manage work items.
    long-summary:
    """

    helps['boards item'] = """
    type: group
    short-summary: Manage work items.
    long-summary:
    """