# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import threading
from knack.log import get_logger

from azext_devops.devops_sdk.v5_0.customer_intelligence.models import CustomerIntelligenceEvent

logger = get_logger(__name__)

vsts_tracking_data = CustomerIntelligenceEvent()


def init_telemetry():
    global vsts_tracking_data  # pylint: disable=global-statement
    if vsts_tracking_data is None:
        vsts_tracking_data = CustomerIntelligenceEvent()
    if vsts_tracking_data.properties is None:
        vsts_tracking_data.properties = {}


def try_send_telemetry_data(organization):
    try:
        if _is_telemetry_enabled():
            logger.debug('Azure devops telemetry enabled.')
            _try_send_tracking_ci_event_async(organization)
        else:
            logger.debug('Azure devops telemetry disabled.')
    except BaseException as ex:  # pylint: disable=broad-except
        logger.debug(ex, exc_info=True)
        logger.debug('Azure devops telemetry sending failed.')


def set_tracking_data(**kwargs):
    init_telemetry()
    try:
        vsts_tracking_data.area = 'AzureDevopsCli'
        vsts_tracking_data.properties = {}
        command_line_args = vars(kwargs.get('args', None))
        command_line_split = command_line_args['command'].split()
        vsts_tracking_data.feature = command_line_split[0]
        if len(command_line_split) > 1:
            vsts_tracking_data.properties['Command'] = ' '.join(command_line_split[1:])

        args = []
        for key, value in command_line_args.items():
            if value and isinstance(value, str) and not key.startswith('_') and key != 'command':
                args.append(key)

        vsts_tracking_data.properties['Args'] = ' '.join(args)
        vsts_tracking_data.properties['ShellType'] = _get_shell_type()
        import sys
        vsts_tracking_data.properties['IsInteractive'] = str(sys.stdin.isatty())
        vsts_tracking_data.properties['OutputType'] = command_line_args['_output_format']

    except BaseException as ex:  # pylint: disable=broad-except
        logger.debug(ex, exc_info=True)


def _is_telemetry_enabled():
    from azure.cli.core.telemetry import is_telemetry_enabled
    return is_telemetry_enabled()


def _try_send_tracking_ci_event_async(organization=None):
    if (vsts_tracking_data is not None and vsts_tracking_data.area is not None and
            vsts_tracking_data.feature is not None):
        logger.debug("Logging telemetry to azure devops server.")
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[organization])
            thread.start()
        except BaseException as ex:  # pylint: disable=broad-except
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
    except BaseException as ex:  # pylint: disable=broad-except
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
