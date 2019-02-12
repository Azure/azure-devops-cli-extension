# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import datetime
import os
import threading

from collections import OrderedDict
from knack.log import get_logger
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from azure.devops.v4_0.customer_intelligence.models import CustomerIntelligenceEvent
from azure.devops.connection import Connection
from .arguments import should_detect
from .config import vsts_config
from ._credentials import get_credential
from .git import get_remote_url
from .version import VERSION
from .vsts_git_url_info import VstsGitUrlInfo

logger = get_logger(__name__)


def get_vss_connection(team_instance):
    if team_instance not in _vss_connection:
        credentials = _get_credentials(team_instance)
        try:
            _vss_connection[team_instance] = _get_vss_connection(team_instance, credentials)
            collect_telemetry = None
            if vsts_config.has_option('core', 'collect_telemetry'):
                collect_telemetry = vsts_config.get('core', 'collect_telemetry')
            if collect_telemetry is None or collect_telemetry != 'no':
                logger.debug('Telemetry enabled.')
                _try_send_tracking_ci_event_async(team_instance)
            else:
                logger.debug('Telemetry disabled.')
        except Exception as ex:
            logger.debug(ex, exc_info=True)
            raise CLIError(ex)
    return _vss_connection[team_instance]


def _get_credentials(team_instance):
    if _PAT_ENV_VARIABLE_NAME in os.environ:
        pat = os.environ[_PAT_ENV_VARIABLE_NAME]
    else:
        pat = get_credential(team_instance)
    if pat is not None:
        logger.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', pat)
        return credentials
    else:
        # todo: need to add back az login fallback here.
        raise_authentication_error('Before you can run VSTS commands, you need to run the login command to setup credentials.')


def _get_vss_connection(team_instance, credentials):
    return Connection(get_base_url(team_instance), creds=credentials, user_agent='vstscli/{}'.format(VERSION))


def get_first_vss_instance_uri():
    for key in _vss_connection:
        return key


def get_build_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.build.build_client.BuildClient')


def get_ci_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client(
        'azure.devops.v4_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient')


def get_core_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.core.core_client.CoreClient')


def get_git_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.git.git_client.GitClient')


def get_identity_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.identity.identity_client.IdentityClient')


def get_location_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.location.location_client.LocationClient')


def get_member_entitlement_management_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_1.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient')


def get_operations_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.operations.operations_client.OperationsClient')


def get_policy_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.policy.policy_client.PolicyClient')


def get_settings_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_1.settings.settings_client.SettingsClient')


def get_task_agent_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.task_agent.task_agent_client.TaskAgentClient')


def get_work_item_tracking_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('azure.devops.v4_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')


def get_base_url(team_instance):
    if team_instance is not None:
        return team_instance
    else:
        _raise_team_team_instance_arg_error()


def _raise_team_team_instance_arg_error():
    raise CLIError('--instance must be specified. The value should be the URI of your VSTS account, ' +
                   'for example: https://<account>.visualstudio.com or your TFS project collection. ' +
                   'You can set a default value by running: vsts configure --defaults ' +
                   'instance=https://<account>.visualstudio.com. For auto detection to ' +
                   'work (--detect on), you must be in a local Git directory that has a "remote" referencing a VSTS ' +
                   'or TFS repository.')


def _raise_team_project_arg_error():
    raise CLIError('--project must be specified. The value should be the ID or name of a team project. ' +
                   'You can set a default value by running: vsts configure --defaults project=<ProjectName>.')


def resolve_instance_project_and_repo(detect, team_instance, project=None, project_required=True, repo=None):
    if team_instance is None:
        if should_detect(detect):
            git_info = get_vsts_info_from_current_remote_url()
            team_instance = git_info.uri
            if project is None:
                project = git_info.project
                if repo is None:
                    repo = git_info.repo
        if team_instance is None:
            team_instance = _resolve_instance_from_config(team_instance)
        if project is None:
            project = _resolve_project_from_config(project, project_required)
    if project_required and project is None:
        _raise_team_project_arg_error()
    return team_instance, project, repo


def resolve_instance_and_project(detect, team_instance, project=None, project_required=True):
    team_instance, project, _ = resolve_instance_project_and_repo(detect=detect,
                                                                  team_instance=team_instance,
                                                                  project=project,
                                                                  project_required=project_required)
    return team_instance, project


def resolve_instance(detect, team_instance):
    team_instance, _ = resolve_instance_and_project(detect=detect,
                                                    team_instance=team_instance,
                                                    project_required=False)
    return team_instance


def _resolve_instance_from_config(team_instance):
    from .config import vsts_config
    if team_instance is None:
        if vsts_config.has_option(_DEFAULTS_SECTION, _TEAM_INSTANCE_DEFAULT):
            team_instance = vsts_config.get(_DEFAULTS_SECTION, _TEAM_INSTANCE_DEFAULT)
        if team_instance is None or team_instance == '':
            _raise_team_team_instance_arg_error()
    return team_instance


def _resolve_project_from_config(project, project_required=True):
    from .config import vsts_config
    if project is None:
        if vsts_config.has_option(_DEFAULTS_SECTION, _TEAM_PROJECT_DEFAULT):
            project = vsts_config.get(_DEFAULTS_SECTION, _TEAM_PROJECT_DEFAULT)
        if project_required and (project is None or project == ''):
            _raise_team_project_arg_error()
    return project


def get_vsts_info_from_current_remote_url():
    start = datetime.datetime.now()
    info = VstsGitUrlInfo(get_remote_url(VstsGitUrlInfo.is_vsts_url_candidate))
    end = datetime.datetime.now()
    duration = end - start
    logger.info("Detect: Url discovery took " + str(duration))
    return info


def set_tracking_data(argv):
    try:
        vsts_tracking_data.area = 'CLI'
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


def _try_send_tracking_ci_event_async(team_instance=None):
    if vsts_tracking_data is not None and vsts_tracking_data.area is not None:
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[team_instance])
            thread.start()
        except Exception as ex:
            # we should always continue if we fail to set tracking data
            logger.debug(ex, exc_info=True)


def _send_tracking_ci_event(team_instance=None, ci_client=None):
    if ci_client is None:
        ci_client = get_ci_client(team_instance=team_instance)
    try:
        ci_client.publish_events([vsts_tracking_data])
        return True
    except Exception as ex:
        logger.debug(ex, exc_info=True)
        return False


def get_connection_data(team_instance):
    team_instance = team_instance.lower()
    if team_instance in _connection_data:
        return _connection_data[team_instance]
    else:
        location_client = get_location_client(team_instance)
        _connection_data[team_instance] = location_client.get_connection_data()
        return _connection_data[team_instance]


def get_authentication_error(message):
    return CLIError(str(message) + "  Please see https://aka.ms/vsts-cli-auth for more information.")


def raise_authentication_error(message):
    raise get_authentication_error(message)


_DEFAULTS_SECTION = 'defaults'
_TEAM_INSTANCE_DEFAULT = 'instance'
_TEAM_PROJECT_DEFAULT = 'project'
_PAT_ENV_VARIABLE_NAME = 'VSTS_CLI_PAT'
_AUTH_TOKEN_ENV_VARIABLE_NAME = 'VSTS_CLI_AUTH_TOKEN'

_connection_data = {}
_vss_connection = OrderedDict()
vsts_tracking_data = CustomerIntelligenceEvent()
