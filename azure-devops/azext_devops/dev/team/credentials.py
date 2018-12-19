# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys

from knack.log import get_logger
from knack.prompting import NoTTYException, prompt_pass
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from azext_devops.dev.common._credentials import clear_credential, set_credential
from azext_devops.dev.common.services import _get_vss_connection, get_base_url

logger = get_logger(__name__)

def credential_set(devops_organization=None):
    """Set the credential (PAT) to use for a particular account
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    """
    token = _get_pat_token()
    if devops_organization is not None:
        devops_organization = get_base_url(devops_organization)
        logger.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', token)
        connection = _get_vss_connection(devops_organization, credentials)
        location_client = connection.get_client('vsts.location.v4_1.location_client.LocationClient')
        try:
            location_client.get_connection_data()
        except Exception as ex2:
            logger.debug(ex2, exc_info=True)
            raise CLIError("Failed to authenticate using the supplied token.")
    set_credential(devops_organization=devops_organization, token=token)


def credential_clear(devops_organization=None):
    """Clear the credential for a particular account
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    """
    if devops_organization is not None:
        devops_organization = get_base_url(devops_organization)
    clear_credential(devops_organization)
    print('The credential was successfully cleared.')


def _get_pat_token():
    try:
        token = prompt_pass('Token: ', confirm=False, help_string="The token (PAT) to authenticate with.")
    except NoTTYException:
        logger.info("Getting PAT token in non-interactive mode.")
        token = sys.stdin.readline().rstrip()
    return token

