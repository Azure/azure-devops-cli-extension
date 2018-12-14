# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# pylint: disable=line-too-long

def load_artifacts_help():
    helps['artifacts'] = """
        type: group
        short-summary: Manage Azure DevOps Artifacts.
        long-summary:
    """

    helps['artifacts universal'] = """
        type: group
        short-summary: (PREVIEW) Manage Universal Packages
        long-summary:
    """