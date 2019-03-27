# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import threading
from knack.log import get_logger

from azext_devops.vstsCompressed.customer_intelligence.v4_0.models.models import CustomerIntelligenceEvent

logger = get_logger(__name__)


def try_send_telemetry_data(organization):
    try:
        if _is_telemetry_enabled():
            logger.debug('Azure devops telemetry enabled.')
            _try_send_tracking_ci_event_async(organization)
        else:
            logger.debug('Azure devops telemetry disabled.')
    except BaseException as ex:
        logger.debug(ex, exc_info=True)
        logger.debug('Azure devops telemetry sending failed.')


def set_tracking_data(**kwargs):
    try:
        vsts_tracking_data.area = 'AzureDevopsCli'
        vsts_tracking_data.properties = {}
        command_line_args = vars(kwargs.get('args', None))
        command_line_split = command_line_args['command'].split()
        vsts_tracking_data.feature = command_line_split[0]
        if len(command_line_split) > 1:
            vsts_tracking_data.properties['Command'] = ''.join(command_line_split[1:])

        args = []
        for key, value in command_line_args.items():
            if value and type(value) == 'str' and not key.startswith('_') and key != 'command':
                args.append(key)

        vsts_tracking_data.properties['Args'] = ''.join(args)
        vsts_tracking_data.properties['ShellType'] = _get_shell_type()
        import sys
        vsts_tracking_data.properties['IsInteractive'] = sys.stdin.isatty()
        vsts_tracking_data.properties['OutputType'] = command_line_args['_output_format']

    except BaseException as ex:
        logger.debug(ex, exc_info=True)


def _is_telemetry_enabled():
    from azure.cli.core import get_default_cli
    collect_telemetry = None
    # Read the telemetry flag from az cli config file not the az devops extension config file
    az_cli_ctx = get_default_cli()
    az_config = az_cli_ctx.config
    if az_config.has_option('core', 'collect_telemetry'):
        collect_telemetry = az_config.get('core', 'collect_telemetry')
    return bool(collect_telemetry is None or collect_telemetry != 'no')


def _try_send_tracking_ci_event_async(organization=None):
    if (vsts_tracking_data is not None and vsts_tracking_data.area is not None and
            vsts_tracking_data.feature is not None):
        logger.debug("Logging telemetry to azure devops server.")
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[organization])
            thread.start()
        except BaseException as ex:
            # we should always continue if we fail to set tracking data
            logger.debug(ex, exc_info=True)
    else:
        logger.debug("Skipping telemetry to azure devops server.")


def _send_tracking_ci_event(organization=None, ci_client=None):
    from .services import get_ci_client
    if ci_client is None:
        ci_client = get_ci_client(organization=organization)
    try:
        ci_client.publish_events([vsts_tracking_data])
        return True
    except BaseException as ex:
        logger.debug(ex, exc_info=True)
        return False


# azure cli uses this to get shell type from os environment
def _get_shell_type():
    import os
    if 'ZSH_VERSION' in os.environ:
        return 'zsh'
    if 'BASH_VERSION' in os.environ:
        return 'bash'
    if 'KSH_VERSION' in os.environ or 'FCEDIT' in os.environ:
        return 'ksh'
    if 'WINDIR' in os.environ:
        return 'cmd'
    return _remove_cmd_chars(_remove_symbols(os.environ.get('SHELL')))


def _remove_cmd_chars(s):
    if isinstance(s, str):
        return s.replace("'", '_').replace('"', '_').replace('\r\n', ' ').replace('\n', ' ')
    return s


def _remove_symbols(s):
    if isinstance(s, str):
        for c in '$%^&|':
            s = s.replace(c, '_')
    return s


vsts_tracking_data = CustomerIntelligenceEvent()
