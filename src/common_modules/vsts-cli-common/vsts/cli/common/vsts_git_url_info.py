# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from msrest.serialization import Model

from .file_cache import get_cli_cache
from .uri import uri_parse

logger = get_logger(__name__)

class AzdosGitUrlInfo(object):
    """ AzdosGitUrlInfo.
    """
    def __init__(self, remote_url):
        from msrest import Serializer, Deserializer
        from msrest.exceptions import DeserializationError, SerializationError
        self.project = None
        self.repo = None
        self.uri = None
        if remote_url is not None:
            logger.debug("Remote url: %s", remote_url)
            models = {'_RemoteInfo': self._RemoteInfo}

            remote_url = remote_url.lower()
            remote_info = None
            if _git_remote_info_cache[remote_url]:
                deserializer = Deserializer(models)
                try:
                    remote_info = deserializer.deserialize_data(_git_remote_info_cache[remote_url], '_RemoteInfo')
                except DeserializationError as ex:
                    logger.debug(ex, exc_info=True)
                if remote_info is not None:
                    self.project = remote_info.project
                    self.repo = remote_info.repository
                    self.uri = remote_info.server_url
            if remote_info is None:
                azdos_info = self.get_azdos_info(remote_url)
                if azdos_info is not None:
                    self.project = azdos_info.repository.project.id
                    self.repo = azdos_info.repository.id
                    apis_path_segment = '/_apis/'
                    apis_path_segment_pos = azdos_info.repository.url.find(apis_path_segment)
                    if apis_path_segment_pos >= 0:
                        self.uri = azdos_info.repository.url[:apis_path_segment_pos]
                    else:
                        self.uri = azdos_info.server_url
                    serializer = Serializer(models)
                    try:
                        _git_remote_info_cache[remote_url] = \
                            serializer.serialize_data(self._RemoteInfo(self.project, self.repo, self.uri),
                                                      '_RemoteInfo')
                    except SerializationError as ex:
                        logger.debug(ex, exc_info=True)

    @staticmethod
    def get_azdos_info(remote_url):
        from azdos.git.v4_0.git_client import GitClient
        from .services import _get_credentials
        components = uri_parse(remote_url.lower())
        if components.scheme == 'ssh':
            # Convert to https url.
            netloc = AzdosGitUrlInfo.convert_ssh_netloc_to_https_netloc(components.netloc)
            if netloc is None:
                return None
            uri = 'https://' + netloc + '/' + components.path
            ssh_path_segment = '_ssh/'
            ssh_path_segment_pos = uri.find(ssh_path_segment)
            if ssh_path_segment_pos >= 0:
                uri = uri[:ssh_path_segment_pos] + '_git/' + uri[ssh_path_segment_pos + len(ssh_path_segment):]
        else:
            uri = remote_url
        credentials = _get_credentials(uri)
        return GitClient.get_azdos_info_by_remote_url(uri, credentials=credentials)

    @staticmethod
    def convert_ssh_netloc_to_https_netloc(netloc):
        if netloc is None:
            return None
        if netloc.find('@') < 0:
            # on premise url
            logger.warning('TFS SSH URLs are not supported for repo auto-detection yet. See the following issue for ' +
                            'latest updates: https://github.com/Microsoft/azdos-cli/issues/142')
            return None
        else:
            # hosted url
            import re
            regex = re.compile('([^@]+)@[^\.]+(\.[^:]+)')
            match = regex.match(netloc)
            if match is not None:
                return match.group(1) + match.group(2)
            return None

    @staticmethod
    def is_azdos_url_candidate(url):
        if url is None:
            return False
        components = uri_parse(url.lower())
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
            super(AzdosGitUrlInfo._RemoteInfo, self).__init__()
            self.project = project
            self.repository = repository
            self.server_url = server_url


_git_remote_info_cache = get_cli_cache('remotes', 0)
