# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function


def feedback():
    """Displays information on how to provide feedback to the Azure DevOps CLI team.
    """
    url = 'https://aka.ms/azure-devops-cli-feedback'
    print('Thank you for taking the time to share your feedback. Please submit your feedback on the following web ' +
          'page: {url}'.format(url=url))
