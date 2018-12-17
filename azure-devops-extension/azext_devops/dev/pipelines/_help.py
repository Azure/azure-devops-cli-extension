# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_pipelines_help():
    helps['pipelines'] = """
    type: group
    short-summary: Manage Azure DevOps Pipelines.
    long-summary:
    """

    helps['pipelines definition'] = """
    type: group
    short-summary: Manage build pipelines definitions.
    long-summary:
    """

    helps['pipelines release'] = """
    type: group
    short-summary: Commands to work with and manage releases.
    long-summary:
    """

    helps['pipelines release definition'] = """
    type: group
    short-summary: Manage release definitions.
    long-summary:
    """
