# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_pipelines_help():
    helps['pipelines'] = """
    type: group
    short-summary: Manage Azure Pipelines.
    long-summary:
    """

    helps['pipelines build'] = """
    type: group
    short-summary: Manage Azure Pipelines build.
    long-summary:
    """

    helps['pipelines build tag'] = """
    type: group
    short-summary: Manage build tags.
    long-summary:
    """

    helps['pipelines build definition'] = """
    type: group
    short-summary: Manage build pipelines definitions.
    long-summary:
    """

    helps['pipelines build task'] = """
    type: group
    short-summary: Manage build pipelines task.
    long-summary:
    """

    helps['pipelines release'] = """
    type: group
    short-summary: Manage releases.
    long-summary:
    """

    helps['pipelines release definition'] = """
    type: group
    short-summary: Manage release definitions.
    long-summary:
    """

    helps['pipelines runs'] = """
    type: group
    short-summary: Manage pipeline runs.
    long-summary:
    """

    helps['pipelines runs artifact'] = """
    type: group
    short-summary: Download, upload and list run artifacts.
    long-summary:
    """
