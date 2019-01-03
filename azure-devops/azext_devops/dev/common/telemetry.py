# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import threading
from vsts.customer_intelligence.v4_0.models.customer_intelligence_event import CustomerIntelligenceEvent
from knack.log import get_logger

logger = get_logger(__name__)


def try_send_telemetry_data(devops_organization):
    try:
        if _is_telemetry_enabled():
            logger.debug('Azure devops telemetry enabled.')
            _try_send_tracking_ci_event_async(devops_organization)
        else:
            logger.debug('Azure devops telemetry disabled.')
    except BaseException as ex:
        logger.debug(ex, exc_info=True)
        logger.debug('Azure devops telemetry sending failed.')


def set_tracking_data(argv):
    try:
        vsts_tracking_data.area = 'AzureDevopsCli'
        vsts_tracking_data.properties = {}
        if argv:
            vsts_tracking_data.feature = argv[0]
        else:
            vsts_tracking_data.feature = None
        if len(argv) > 1:
            command = []
            args = []
            command_populated = False
            for arg in argv[1:]:
                if arg and argv:
                    if not command_populated and arg[0] != '-':
                        command.append(arg)
                    elif arg[0] == '-':
                        args.append(arg.lstrip('-'))
                        command_populated = True
            if command:
                vsts_tracking_data.properties['Command'] = ' '.join(command)
            else:
                vsts_tracking_data.properties['Command'] = ''
            vsts_tracking_data.properties['Args'] = args
            vsts_tracking_data.properties['ShellType'] = _get_shell_type()

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


def _try_send_tracking_ci_event_async(devops_organization=None):
    if (vsts_tracking_data is not None and vsts_tracking_data.area is not None and
            vsts_tracking_data.feature is not None):
        logger.debug("Logging telemetry to azure devops server.")
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[devops_organization])
            thread.start()
        except BaseException as ex:
            # we should always continue if we fail to set tracking data
            logger.debug(ex, exc_info=True)
    else:
        logger.debug("Skipping telemetry to azure devops server.")


def _send_tracking_ci_event(devops_organization=None, ci_client=None):
    from .services import get_ci_client
    if ci_client is None:
        ci_client = get_ci_client(devops_organization=devops_organization)
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
