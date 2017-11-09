# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import datetime
import logging
import os
import threading

from collections import OrderedDict
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from msrest.serialization import Model
from vsts.customer_intelligence.v4_0.models.customer_intelligence_event import CustomerIntelligenceEvent
from vsts.vss_connection import VssConnection
from .arguments import should_detect
from .config import vsts_config
from ._credentials import get_credential
from .file_cache import get_cli_cache
from .git import get_remote_url
from .version import VERSION


def get_vss_connection(team_instance):
    if team_instance not in _vss_connection:
        credentials = _get_credentials(team_instance)
        try:
            _vss_connection[team_instance] = _get_vss_connection(team_instance, credentials)
            collect_telemetry = None
            if vsts_config.has_option('core', 'collect_telemetry'):
                collect_telemetry = vsts_config.get('core', 'collect_telemetry')
            if collect_telemetry is None or collect_telemetry != 'no':
                logging.debug('Telemetry enabled.')
                _try_send_tracking_ci_event_async(team_instance)
            else:
                logging.debug('Telemetry disabled.')
            # _vss_connection[team_instance].authenticate()
        except Exception as ex:
            logging.exception(str(ex))
            raise CLIError(ex)
    return _vss_connection[team_instance]


def _get_credentials(team_instance):
    if _PAT_ENV_VARIABLE_NAME in os.environ:
        pat = os.environ[_PAT_ENV_VARIABLE_NAME]
    else:
        pat = get_credential(team_instance)
    if pat is not None:
        logging.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', pat)
        return credentials
    else:
        # todo: need to add back az login fallback here.
        raise_authentication_error('Before you can run VSTS commands, you need to sign in or setup credentials.')


def _get_vss_connection(team_instance, credentials):
    return VssConnection(get_base_url(team_instance), creds=credentials, user_agent='vstscli/{}'.format(VERSION))


def get_first_vss_instance_uri():
    for key in _vss_connection:
        return key


def get_build_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.build.v4_0.build_client.BuildClient')


def get_ci_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.customer_intelligence.v4_0.customer_intelligence_client.CustomerIntelligenceClient')


def get_core_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.core.v4_0.core_client.CoreClient')


def get_git_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.git.v4_0.git_client.GitClient')


def get_identity_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.identity.v4_0.identity_client.IdentityClient')


def get_location_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.location.v4_0.location_client.LocationClient')


def get_operations_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.operations.v4_0.operations_client.OperationsClient')


def get_policy_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.policy.v4_0.policy_client.PolicyClient')


def get_work_item_tracking_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient')


def get_base_url(team_instance):
    if team_instance is not None:
        return team_instance
    else:
        _raise_team_team_instance_arg_error()


def _raise_team_team_instance_arg_error():
    raise CLIError('--instance must be specified. The value should be the URI of your VSTS account, ' +
                   'for example: https://<account>.visualstudio.com or your TFS proiject collection. ' +
                   'You can set a default value by running: vsts configure --defaults ' +
                   'instance=https://<account>.visualstudio.com. For auto detection to ' +
                   'work (--detect on), you must be in a local Git directory that has a "remote" referencing a VSTS ' +
                   'or TFS repository.')


def _raise_team_project_arg_error():
    raise CLIError('--project must be specified. The value should be the ID or name of a VSTS project.')


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
    logging.info("Detect: Url discovery took " + str(duration))
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
        logging.exception(ex)


def _try_send_tracking_ci_event_async(team_instance=None):
    if vsts_tracking_data is not None and vsts_tracking_data.area is not None:
        try:
            thread = threading.Thread(target=_send_tracking_ci_event, args=[team_instance])
            thread.start()
        except Exception as ex:
            # we should always continue if we fail to set tracking data
            logging.exception(str(ex))


def _send_tracking_ci_event(team_instance=None, ci_client=None):
    if ci_client is None:
        ci_client = get_ci_client(team_instance=team_instance)
    try:
        ci_client.publish_events([vsts_tracking_data])
        return True
    except Exception as ex:
        logging.exception(ex)
        return False


def get_connection_data(team_instance):
    team_instance = team_instance.lower()
    if team_instance in _connection_data:
        return _connection_data[team_instance]
    else:
        location_client = get_location_client(team_instance)
        _connection_data[team_instance] = location_client.get_connection_data()
        return _connection_data[team_instance]


def raise_authentication_error(message):
    raise CLIError(str(message) + "  Please see https://aka.ms/vsts-cli-auth for more information.")


class VstsGitUrlInfo:
    """ VstsGitUrlInfo.
    """
    def __init__(self, remote_url):
        from msrest import Serializer, Deserializer
        from msrest.exceptions import DeserializationError, SerializationError
        self.project = None
        self.repo = None
        self.uri = None
        if remote_url is not None:
            logging.debug("Remote url: %s", remote_url)
            models = {'_RemoteInfo': self._RemoteInfo}

            remote_url = remote_url.lower()
            remote_info = None
            if _git_remote_info_cache[remote_url]:
                deserializer = Deserializer(models)
                try:
                    remote_info = deserializer.deserialize_data(_git_remote_info_cache[remote_url], '_RemoteInfo')
                except DeserializationError as ex:
                    logging.exception(str(ex))
                if remote_info is not None:
                    self.project = remote_info.project
                    self.repo = remote_info.repository
                    self.uri = remote_info.server_url
            if remote_info is None:
                vsts_info = self.get_vsts_info(remote_url)
                if vsts_info is not None:
                    self.project = vsts_info.repository.project.id
                    self.repo = vsts_info.repository.id
                    apis_path_segment = '/_apis/'
                    apis_path_segment_pos = vsts_info.repository.url.find(apis_path_segment)
                    if apis_path_segment_pos >= 0:
                        self.uri = vsts_info.repository.url[:apis_path_segment_pos]
                    else:
                        self.uri = vsts_info.server_url
                    serializer = Serializer(models)
                    try:
                        _git_remote_info_cache[remote_url] = \
                            serializer.serialize_data(self._RemoteInfo(self.project, self.repo, self.uri),
                                                      '_RemoteInfo')
                    except SerializationError as ex:
                        logging.exception(str(ex))

    @staticmethod
    def get_vsts_info(remote_url):
        from vsts.git.v4_0.git_client import GitClient
        components = urlparse(remote_url.lower())
        if components.scheme == 'ssh':
            # Convert to https url.
            netloc = VstsGitUrlInfo.convert_ssh_netloc_to_https_netloc(components.netloc)
            uri = 'https://' + netloc + '/' + components.path
            ssh_path_segment = '_ssh/'
            ssh_path_segment_pos = uri.find(ssh_path_segment)
            if ssh_path_segment_pos >= 0:
                uri = uri[:ssh_path_segment_pos] + '_git/' + uri[ssh_path_segment_pos + len(ssh_path_segment):]
        else:
            uri = remote_url
        credentials = _get_credentials(uri)
        return GitClient.get_vsts_info_by_remote_url(uri, credentials=credentials)

    @staticmethod
    def convert_ssh_netloc_to_https_netloc(netloc):
        if netloc is None:
            return None
        import re
        regex = re.compile('([^@]+)@[^\.]+(\.[^:]+)')
        match = regex.match(netloc)
        if match is not None:
            return match.group(1) + match.group(2)
        return None

    @staticmethod
    def is_vsts_url_candidate(url):
        if url is None:
            return False
        components = urlparse(url.lower())
        if components.netloc == 'github.com':
            return False
        elif components.path is not None \
                and (components.path.find('/_git/') >= 0 or components.path.find('/_ssh/') >= 0):
            return True
        else:
            return False

    class _RemoteInfo(Model):

        _attribute_map = {
            'project': {'key': 'project', 'type': 'str'},
            'repository': {'key': 'repository', 'type': 'str'},
            'server_url': {'key': 'serverUrl', 'type': 'str'}
        }

        def __init__(self, project=None, repository=None, server_url=None):
            super(VstsGitUrlInfo._RemoteInfo, self).__init__()
            self.project = project
            self.repository = repository
            self.server_url = server_url


_DEFAULTS_SECTION = 'defaults'
_TEAM_INSTANCE_DEFAULT = 'instance'
_TEAM_PROJECT_DEFAULT = 'project'
_PAT_ENV_VARIABLE_NAME = 'VSTS_CLI_PAT'
_AUTH_TOKEN_ENV_VARIABLE_NAME = 'VSTS_CLI_AUTH_TOKEN'

_connection_data = {}
_git_hashes_cache = get_cli_cache('valid_hashes', 3600 * 6)
_git_remote_info_cache = get_cli_cache('remotes', 0)
_vss_connection = OrderedDict()
vsts_tracking_data = CustomerIntelligenceEvent()
