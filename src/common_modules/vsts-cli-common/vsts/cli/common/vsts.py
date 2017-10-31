# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import datetime
import logging
import threading

from collections import OrderedDict
from urllib.parse import urlparse
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from msrest.serialization import Model
from vsts._file_cache import get_cache
from vsts.customer_intelligence.v4_0.models.customer_intelligence_event import CustomerIntelligenceEvent
from vsts.vss_connection import VssConnection
from ._credentials import get_credential
from .git import get_git_credentials, get_remote_url, GIT_CREDENTIALS_PASSWORD_KEY, GIT_CREDENTIALS_USERNAME_KEY
from .version import VERSION


def get_vss_connection(team_instance):
    team_instance = resolve_team_instance_uri(team_instance)
    if team_instance not in _vss_connection:
        pat = get_credential(team_instance)
        if pat is not None:
            logging.info("Creating connection with personal access token.")
            credentials = BasicAuthentication('', pat)
        else:
            # todo: need to add back az login fallback here.
            raise_authentication_error('Before you can run VSTS commands, you need to sign in or setup credentials.')
        try:
            _vss_connection[team_instance] = _get_vss_connection(team_instance, credentials)
            _try_send_tracking_ci_event_async(team_instance)
            _vss_connection[team_instance].authenticate()
        except Exception as ex:
            logging.exception(str(ex))
            raise CLIError(ex)
    return _vss_connection[team_instance]


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


def get_git_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.git.v4_0.git_client.GitClient')


def get_identity_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.identity.v4_0.identity_client.IdentityClient')


def get_location_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.location.v4_0.location_client.LocationClient')


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
    raise CLIError('--team-instance must be specified. The value should be the URI of your Team Services account, ' +
                   'for example: https://<account>.visualstudio.com. You can set a default value by running: az ' +
                   'configure --defaults team-instance=https://<account>.visualstudio.com. For auto detection to ' +
                   'work (--detect on), you must be in a local Git directory that has a "remote" referencing a Team ' +
                   'Services hosted repository.')


def _raise_team_project_arg_error():
    raise CLIError('--team-project must be specified. The value should be the ID or name of a Team Services project. ' +
                   'For auto detection to work (--detect on), you must be in a local Git directory that has a ' +
                   '"remote" referencing a Team Services hosted repository.')


def resolve_team_instance_uri(team_instance):
    # from azure.cli.core._config import az_config
    if team_instance is None:
        # if az_config.has_option(_DEFAULTS_SECTION, _TEAM_INSTANCE_DEFAULT):
            # team_instance = az_config.get(_DEFAULTS_SECTION, _TEAM_INSTANCE_DEFAULT)
        if team_instance is None or team_instance == '':
            _raise_team_team_instance_arg_error()
    return team_instance


def resolve_project(project):
    # from azure.cli.core._config import az_config
    if project is None:
        # if az_config.has_option(_DEFAULTS_SECTION, _TEAM_PROJECT_DEFAULT):
            # project = az_config.get(_DEFAULTS_SECTION, _TEAM_PROJECT_DEFAULT)
        if project is None or project == '':
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
                    if arg is not None and argv:
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


def normalize_url_for_key(url):
    if url.endswith("/"):
        url = url[:-1]
    url = url.lower()
    return url


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
            models = {'_RemoteInfo': self._RemoteInfo}
            components = urlparse(remote_url)
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
                if components.scheme == 'ssh':
                    # Convert to https url.
                    netloc = VstsGitUrlInfo.convert_ssh_netloc_to_https_netloc(components.netloc)
                    uri = 'https://' + netloc
                    ssh = True
                else:
                    uri = components.scheme + '://' + components.netloc
                    ssh = False
                git_client = get_git_client(team_instance=uri)
                relative_url = components.path
                if ssh:
                    ssh_path_segment = '_ssh/'
                    ssh_path_segment_pos = relative_url.find(ssh_path_segment)
                    if ssh_path_segment_pos >= 0:
                        relative_url = relative_url[0:ssh_path_segment_pos] + '_git/'\
                                       + relative_url[(ssh_path_segment_pos + len(ssh_path_segment)):]
                vsts_info = git_client.get_vsts_info(relative_url)
                if vsts_info is not None:
                    self.project = vsts_info.repository.project.id
                    self.repo = vsts_info.repository.id
                    self.uri = vsts_info.server_url
                    serializer = Serializer(models)
                    try:
                        _git_remote_info_cache[remote_url] = \
                            serializer.serialize_data(self._RemoteInfo(self.project, self.repo, self.uri), '_RemoteInfo')
                    except SerializationError as ex:
                        logging.exception(str(ex))


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
_TEAM_INSTANCE_DEFAULT = 'team-instance'
_TEAM_PROJECT_DEFAULT = 'team-project'

_connection_data = {}
_git_hashes_cache = get_cache('valid_hashes', 3600 * 6)
_git_remote_info_cache = get_cache('remotes', 0)
_vss_connection = OrderedDict()
vsts_tracking_data = CustomerIntelligenceEvent()
