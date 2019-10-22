# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model
from knack.log import get_logger

from .file_cache import get_cli_cache
from .uri import uri_parse

logger = get_logger(__name__)


class VstsGitUrlInfo():
    """ VstsGitUrlInfo.
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
                        logger.debug(ex, exc_info=True)

    @staticmethod
    def get_vsts_info(remote_url):
        from azext_devops.devops_sdk.v5_0.git.git_client import GitClient
        from .services import _get_credentials
        components = uri_parse(remote_url.lower())
        if components.scheme == 'ssh':
            # Convert to https url.
            netloc = VstsGitUrlInfo.convert_ssh_netloc_to_https_netloc(components.netloc)
            if netloc is None:
                return None
            # New ssh urls do not have _ssh so path is like org/project/repo
            # We need to convert it into project/_git/repo/ or org/project/_git/repo for dev.azure.com urls
            path = components.path
            ssh_path_segment = '_ssh/'
            ssh_path_segment_pos = components.path.find(ssh_path_segment)
            if ssh_path_segment_pos < 0:  # new ssh url
                path_vals = components.path.strip('/').split('/')
                if path_vals and len(path_vals) == 3:
                    if 'visualstudio.com' in netloc:
                        path = '{proj}/{git}/{repo}'.format(proj=path_vals[1], git='_git', repo=path_vals[2])
                    elif 'dev.azure.com' in netloc:
                        path = '{org}/{proj}/{git}/{repo}'.format(
                            org=path_vals[0], proj=path_vals[1], git='_git', repo=path_vals[2])
                else:
                    logger.debug("Unsupported url format encountered in git repo url discovery.")
                uri = 'https://' + netloc + '/' + path
            else:  # old ssh urls
                uri = 'https://' + netloc + '/' + path.strip('/')
                ssh_path_segment_pos = uri.find(ssh_path_segment)
                if ssh_path_segment_pos >= 0:
                    uri = uri[:ssh_path_segment_pos] + '_git/' + uri[ssh_path_segment_pos + len(ssh_path_segment):]
        else:
            uri = remote_url
        credentials = _get_credentials(uri)
        try:
            return GitClient.get_vsts_info_by_remote_url(uri, credentials=credentials)
        except Exception as ex:
            exceptionTypeName = type(ex).__name__
            if exceptionTypeName == 'AzureDevOpsAuthenticationError':
                logger.warning('Auto-detect from git url failed because of insufficient permissions.')
                return
            import sys
            from six import reraise
            reraise(*sys.exc_info())

    @staticmethod
    def convert_ssh_netloc_to_https_netloc(netloc):
        if netloc is None:
            return None
        if netloc.find('@') < 0:
            # on premise url
            logger.warning('DevOps SSH URLs are not supported for repo auto-detection yet. See the following issue for \
                           latest updates: https://github.com/Microsoft/azure-devops-cli-extension/issues/142')
            return None
        # hosted url
        import re
        regex = re.compile(r'([^@]+)@[^\.]+(\.[^:]+)')
        match = regex.match(netloc)
        if match is not None:
            # Handle new and old url formats
            if match.group(1) == 'git' and match.group(2) == '.dev.azure.com':
                return match.group(2).strip('.')
            return match.group(1) + match.group(2)
        return None

    @staticmethod
    def is_vsts_url_candidate(url):
        if url is None:
            return False
        components = uri_parse(url.lower())
        if components.netloc == 'github.com':
            return False
        if components.path is not None \
            and (components.path.find('/_git/') >= 0 or components.path.find('/_ssh/') >= 0 or
                 components.scheme == 'ssh'):
            return True

        return False

    class _RemoteInfo(Model):

        _attribute_map = {
            'project': {'key': 'project', 'type': 'str'},
            'repository': {'key': 'repository', 'type': 'str'},
            'server_url': {'key': 'serverUrl', 'type': 'str'}
        }

        def __init__(self, project=None, repository=None, server_url=None):
            super(VstsGitUrlInfo._RemoteInfo, self).__init__()  # pylint: disable=protected-access
            self.project = project
            self.repository = repository
            self.server_url = server_url


_git_remote_info_cache = get_cli_cache('remotes', 0)
