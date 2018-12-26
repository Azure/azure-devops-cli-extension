# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_artifacts_help():
    helps['artifacts'] = """
        type: group
        short-summary: Manage Azure Artifacts.
        long-summary:
    """

    helps['artifacts universal'] = """
        type: group
        short-summary: (PREVIEW) Manage Universal Packages
        long-summary:
    """
