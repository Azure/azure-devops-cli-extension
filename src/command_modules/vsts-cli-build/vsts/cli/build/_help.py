# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

helps['build'] = """
    type: group
    short-summary: Manage build definitions.
    long-summary:
"""

helps['build queue'] = """
    type: command
    short-summary: Queue a new build.
    long-summary: Queue a new build with an ID.
"""
