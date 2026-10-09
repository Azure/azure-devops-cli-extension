# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model
from knack.log import get_logger

from .file_cache import get_cli_cache
from .uri import (is_azure_devops_host,
                  organization_url_from_azure_devops_url,
                  parse_azure_devops_git_remote)

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

            parsed_remote = parse_azure_devops_git_remote(remote_url)
            if parsed_remote is None:
                return
            remote_url = parsed_remote.repository_url
            remote_info = None
            if _git_remote_info_cache[remote_url]:
                deserializer = Deserializer(models)
                try:
                    remote_info = deserializer.deserialize_data(_git_remote_info_cache[remote_url], '_RemoteInfo')
                except DeserializationError as ex:
                    logger.debug(ex, exc_info=True)
                if remote_info is not None:
                    organization_url = organization_url_from_azure_devops_url(remote_info.server_url)
                    if organization_url is not None:
                        self.project = remote_info.project
                        self.repo = remote_info.repository
                        self.uri = organization_url
                    else:
                        remote_info = None
            if remote_info is None:
                vsts_info = self.get_vsts_info(remote_url)
                if vsts_info is not None:
                    apis_path_segment = '/_apis/'
                    apis_path_segment_pos = vsts_info.repository.url.find(apis_path_segment)
                    if apis_path_segment_pos >= 0:
                        organization_url = organization_url_from_azure_devops_url(
                            vsts_info.repository.url[:apis_path_segment_pos])
                    else:
                        organization_url = organization_url_from_azure_devops_url(vsts_info.server_url)
                    if organization_url is None:
                        logger.warning('Auto-detect returned an invalid Azure DevOps organization URL.')
                        return
                    self.project = vsts_info.repository.project.id
                    self.repo = vsts_info.repository.id
                    self.uri = organization_url
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
        parsed_remote = parse_azure_devops_git_remote(remote_url)
        if parsed_remote is None:
            logger.warning('Skipping auto-detect: remote URL host is not a known Azure DevOps host.')
            return None
        uri = parsed_remote.repository_url
        credentials = _get_credentials(parsed_remote.organization_url)
        try:
            return GitClient.get_vsts_info_by_remote_url(uri, credentials=credentials)
        except Exception as ex:  # pylint: disable=broad-except
            exceptionTypeName = type(ex).__name__
            if exceptionTypeName == 'AzureDevOpsAuthenticationError':
                logger.warning('Auto-detect from git remote url failed because of insufficient permissions.')
                return None
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
        return parse_azure_devops_git_remote(url) is not None

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


def _is_azure_devops_host(netloc):
    """Return True only for known Azure DevOps hosted service hostnames."""
    if netloc is None or '@' in netloc or '\\' in netloc:
        return False
    host = netloc.rsplit(':', 1)[0].lower()
    return is_azure_devops_host(host)


_git_remote_info_cache = get_cli_cache('remotes', 0)
