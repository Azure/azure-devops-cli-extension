# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from azdos.cli.common.version import disable_command_version_checking, DISABLE_VERSION_CHECK_SETTING


def feedback():
    """Displays information on how to provide feedback to the VSTS CLI team.
    """
    print('Thank you for taking the time to share your feedback. Please submit your feedback on the following web ' +
          'page: https://aka.ms/azdos-cli-feedback')
    disable_command_version_checking()
