# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack.util import CLIError
from azext_dev.dev.common.config import (set_global_config_value,
                                    CORE_SECTION,
                                    DEFAULTS_SECTION,
                                    LOGGING_SECTION)
from azext_dev.dev.common.configure import interactive_configure, print_current_configuration
from azext_dev.dev.common.version import disable_command_version_checking, DISABLE_VERSION_CHECK_SETTING


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
    disable_command_version_checking()
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
        from azext_dev.dev.repos.git_alias import setup_git_aliases, clear_git_aliases
        if use_git_aliases == 'yes':
            setup_git_aliases()
        elif use_git_aliases == 'no':
            clear_git_aliases()
    if list_config:
        print_current_configuration()
