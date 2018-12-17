# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import threading
from knack.log import get_logger
from vsts.customer_intelligence.v4_0.models.customer_intelligence_event import CustomerIntelligenceEvent

logger = get_logger(__name__)


def try_send_telemetry_data(devops_organization):
    from azure.cli.core import get_default_cli
    try:
        if(_is_telemetry_enabled()):
            logger.debug('Azure devops telemetry enabled.')
            _try_send_tracking_ci_event_async(devops_organization)
        else:
            logger.debug('Azure devops telemetry disabled.')
    except:
        logger.debug('Azure devops telemetry failed or not allowed.')


def set_tracking_data(argv):
    try:
        vsts_tracking_data.area = 'AzureDevopsCli'
        vsts_tracking_data.properties = {}
        if argv is not None and argv:
            vsts_tracking_data.feature = argv[0]
            if len(argv) > 1:
                command = []
                args = []
                command_populated = False
                for arg in argv[1:]:
                    if arg is not None and argv and len(arg) > 0:
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
        else:
            vsts_tracking_data.feature = 'Command'
    except Exception as ex:
        logger.debug(ex, exc_info=True)


def _is_telemetry_enabled():
    collect_telemetry = None
    # Read the telemetry flag from az cli config file not the az devops extension config file
    az_cli_ctx = get_default_cli()
    az_config = az_cli_ctx.config
    if az_config.has_option('core', 'collect_telemetry'):
        collect_telemetry = az_config.get('core', 'collect_telemetry')
    if collect_telemetry is None or collect_telemetry != 'no':
        return True
    else:
        return False


def _try_send_tracking_ci_event_async(devops_organization=None):
    if vsts_tracking_data is not None and vsts_tracking_data.area is not None:
        logger.debug("Logging telemetry to azure devops server.")
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[devops_organization])
            thread.start()
        except Exception as ex:
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
    except Exception as ex:
        logger.debug(ex, exc_info=True)
        return False


vsts_tracking_data = CustomerIntelligenceEvent()
