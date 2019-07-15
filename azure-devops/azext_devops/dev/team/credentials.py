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
from azext_devops.dev.common.services import _get_connection, get_base_url

logger = get_logger(__name__)


def credential_set(organization=None):
    """Set the credential (PAT) to use for a particular organization.
    Refer https://aka.ms/azure-devops-cli-auth for more information on providing PAT as input.
    """
    token = _get_pat_token()
    if organization is not None:
        organization = get_base_url(organization)
        logger.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', token)
        connection = _get_connection(organization, credentials)
        vstsDir = 'azext_devops.devops_sdk.'
        location_client = connection.get_client(vstsDir + 'v5_0.location.location_client.LocationClient')
        try:
            connection_data = location_client.get_connection_data()
        except Exception as ex2:
            logger.debug(ex2, exc_info=True)
            raise CLIError("Failed to authenticate using the supplied token.")
        # An organization with public project enabled will not throw any exception for invalid token.
        # Hence, handle anonymous user case here.
        if connection_data.authenticated_user.id == _ANONYMOUS_USER_ID:
            raise CLIError("Failed to authenticate using the supplied token.")
    set_credential(organization=organization, token=token)
    _check_and_set_default_organization(organization)


def credential_clear(organization=None):
    """Clear the credential for all or a particular organization
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/.
    If no organization is specified, all organizations will be logged out.
    :type organization: str
    """
    if organization is not None:
        organization = get_base_url(organization)
    clear_credential(organization)
    if organization is not None:
        print('The credential was successfully cleared.')
    else:
        print('Logged out of all Azure DevOps organizations.')
    _check_and_clear_default_organization(organization)


def _get_pat_token():
    try:
        token = prompt_pass('Token: ', confirm=False, help_string="The token (PAT) to authenticate with.")
    except NoTTYException:
        logger.info("Getting PAT token in non-interactive mode.")
        token = sys.stdin.readline().rstrip()
    return token


# Sets organization if the default is not set
def _check_and_set_default_organization(organization):
    if organization is not None:
        from azext_devops.dev.common.config import azdevops_config
        from azext_devops.dev.common.const import DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT
        from .configure import configure
        current_org_default = None
        if azdevops_config.has_option(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT):
            current_org_default = azdevops_config.get(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT)
        if current_org_default is None or current_org_default == '':
            configure(defaults=['organization={}'.format(organization)])
            logger.debug("Setting this organization as default. No default was set earlier.")
        else:
            logger.debug("Another organization is already set as default.")


# Clears organization if the default is set to same
def _check_and_clear_default_organization(organization):
    if organization is not None:
        from azext_devops.dev.common.config import azdevops_config
        from azext_devops.dev.common.const import DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT
        from .configure import configure
        current_org_default = None
        if azdevops_config.has_option(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT):
            current_org_default = azdevops_config.get(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT)
        if current_org_default == organization:
            configure(defaults=["organization=''"])
            logger.debug("Resetting default organization.")
        else:
            logger.debug("Default org not reset. Different organization is set as default.")


_ANONYMOUS_USER_ID = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
