# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_pipelines_help():
    helps['dev build'] = """
    type: group
    short-summary: Commands to work with and manage builds.
    long-summary:
    """

    helps['dev build definition'] = """
    type: group
    short-summary: Manage build definitions.
    long-summary:
    """
