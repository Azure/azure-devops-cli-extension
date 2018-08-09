# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack.log import get_logger
from knack.prompting import NoTTYException, prompt_pass
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from vsts.cli.common._credentials import clear_credential, set_credential
from vsts.cli.common.services import _get_vss_connection, get_base_url
from vsts.cli.common.version import disable_command_version_checking, DISABLE_VERSION_CHECK_SETTING

logger = get_logger(__name__)

def credential_set(token=None, team_instance=None):
    """Set the credential (PAT) to use for a particular account
    :param token: PAT token for the VSTS account or your TFS project collection.  If not supplied, you will be prompted
                  for your token.
    :type token: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    """
    disable_command_version_checking()
    if token is None:
        try:
            token = prompt_pass('Token: ', confirm=False, help_string="The token (PAT) to authenticate with.")
        except NoTTYException:
            raise CLIError('The token argument needs to be set when run in a non-interactive mode.')

    if team_instance is not None:
        team_instance = get_base_url(team_instance)
        logger.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', token)
        connection = _get_vss_connection(team_instance, credentials)
        location_client = connection.get_client('vsts.location.v4_1.location_client.LocationClient')
        try:
            location_client.get_connection_data()
        except Exception as ex2:
            logger.debug(ex2, exc_info=True)
            raise ValueError("Failed to authenticate using the supplied token.")
    set_credential(team_instance=team_instance, token=token)


def credential_clear(team_instance=None):
    """Clear the credential for a particular account
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    """
    disable_command_version_checking()
    if team_instance is not None:
        team_instance = get_base_url(team_instance)
    clear_credential(team_instance)
    print('The credential was successfully cleared.')

