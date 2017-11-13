# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import logging


from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from vsts.cli.common._credentials import clear_credential, set_credential
from vsts.cli.common.config import (set_global_config_value,
                                    CORE_SECTION,
                                    DEFAULTS_SECTION,
                                    LOGGING_SECTION)
from vsts.cli.common.configure import interactive_configure, print_current_configuration
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import _get_vss_connection, get_base_url
from vsts.cli.common.version import DISABLE_VERSION_CHECK_SETTING


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


def configure(defaults=None, collect_telemetry=None, enable_log_file=None, use_git_aliases=None,
              default_output=None, disable_version_check=None, list_config=False):
    """Configure the VSTS CLI or view your configuration.
    :param defaults: Space separated 'name=value' pairs for common arguments defaults,
        e.g. '--defaults output=table arg=value' Use '' to clear the defaults, e.g. --defaults output=''.
    :type defaults: str
    :param collect_telemetry: Microsoft would like to collect anonymous VSTS CLI usage data to
        improve our CLI.  Participation is voluntary and when you choose to
        participate, your device automatically sends information to Microsoft
        about how you use the VSTS CLI.  The data is anonymous and does not
        include commandline argument values.  Set to 'yes' to enable telemetry collection
        or 'no' to disable it.
    :type collect_telemetry: str
    :param enable_log_file: Set to 'yes' to enable logging to file, or 'no' to disable.
    :type enable_log_file: str
    :param use_git_aliases: Set to 'yes' to configure Git aliases global git config file (to enable commands like "git pr list").
        Set to 'no' to remove any aliases set by the tool.
    :type use_git_aliases: str
    :param default_output: Specifies the default output format for commands.
    :type default_output: str
    :param disable_version_check: Set to 'yes' to disable checking for updated versions of the CLI.
    :type disable_version_check: str
    :param list_config: Lists the contents of the config file.
    :type list_config: bool
    """
    if defaults is None and collect_telemetry is None and enable_log_file is None\
            and use_git_aliases is None and default_output is None\
            and disable_version_check is None and list_config is False:
        interactive_configure()
        return
    if defaults:
        for default in defaults:
            parts = default.split('=', 1)
            if len(parts) == 1:
                raise CLIError('usage error: --defaults STRING=STRING STRING=STRING ...')
            set_global_config_value(DEFAULTS_SECTION, parts[0], parts[1])
    if collect_telemetry is not None:
        set_global_config_value(CORE_SECTION, 'collect_telemetry', collect_telemetry)
    if enable_log_file is not None:
        set_global_config_value(LOGGING_SECTION, 'enable_log_file', enable_log_file)
    if default_output is not None:
        set_global_config_value(CORE_SECTION, 'output', default_output)
    if disable_version_check:
        set_global_config_value(CORE_SECTION, DISABLE_VERSION_CHECK_SETTING, disable_version_check)
    if use_git_aliases is not None:
        from vsts.cli.code.common.git_alias import setup_git_aliases, clear_git_aliases
        if use_git_aliases == 'yes':
            setup_git_aliases()
        elif use_git_aliases == 'no':
            clear_git_aliases()
    if list_config:
        print_current_configuration()


def feedback():
    """Displays information on how to provide feedback to the VSTS CLI team.
    """
    print('Thank you for taking the time to share your feedback. Please submit your feedback on the following web ' +
          'page: https://aka.ms/vsts-cli-feedback')
