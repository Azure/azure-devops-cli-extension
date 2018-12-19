# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_admin_help():
    helps['devops admin'] = """
    type: group
    short-summary: Manage administration operations.
    long-summary:
    """

    helps['devops admin banner'] = """
    type: group
    short-summary: Manage organization banner.
    long-summary:
    """