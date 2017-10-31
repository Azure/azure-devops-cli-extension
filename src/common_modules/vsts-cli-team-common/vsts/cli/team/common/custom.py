# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging


from msrest.authentication import BasicAuthentication
from vsts.cli.common._credentials import clear_credential, set_credential
from vsts.cli.common.configure import handle_configure
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.vsts import _get_vss_connection, get_base_url


def credential_set(token, team_instance=None):
    """Set the credential (PAT) to use for a particular account
    :param token:
    :type token: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    """
    try:
        credentials = BasicAuthentication('', token)
        if team_instance is not None:
            team_instance = get_base_url(team_instance)
            logging.info("Creating connection with personal access token.")
            connection = _get_vss_connection(team_instance, credentials)
            location_client = connection.get_client('vsts.location.v4_0.location_client.LocationClient')
            try:
                location_client.get_connection_data()
            except Exception as ex2:
                logging.exception(ex2)
                raise ValueError("Failed to authenticate using the supplied token.")
        set_credential(team_instance=team_instance, token=token)
    except Exception as ex:
        handle_command_exception(ex)


def credential_clear(team_instance=None):
    """Clear the credential for a particular account
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    """
    try:
        if team_instance is not None:
            team_instance = get_base_url(team_instance)
        clear_credential(team_instance)
        print('The credential was successfully cleared.')
    except Exception as ex:
        handle_command_exception(ex)


def configure(defaults=None):
    """Configure the VSTS CLI or view your configuration.
    :param defaults: Space separated 'name=value' pairs for common arguments defaults,
        e.g. '--defaults output=table arg=value' Use '' to clear the defaults, e.g. --defaults output=''.
    :type defaults: str
    """
    handle_configure(defaults=defaults)


def feedback():
    """Displays information on how to provide feedback to the VSTS CLI team.
    """
    print('Thank you for taking the time to share your feedback. Please submit your feedback on the following web ' +
          'page: https://aka.ms/vsts-cli-feedback')
