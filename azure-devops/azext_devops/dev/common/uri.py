# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

try:
    from urllib.parse import urlparse, quote
except ImportError:
    from urllib import quote
    from urlparse import urlparse

import re
from collections import namedtuple


AzureDevOpsGitRemote = namedtuple(
    'AzureDevOpsGitRemote',
    ['repository_url', 'organization_url', 'host'])

_UNSAFE_URL_CHARACTERS = re.compile(r'[\x00-\x20\x7f\\]')
_SAFE_USERINFO = re.compile(r'^[A-Za-z0-9._-]+$')
_SAFE_HOST_LABEL = re.compile(r'^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$')


def uri_parse(url):
    # Special handling for NEW ssh urls which do not start with ssh://
    if not url.startswith('ssh:') and ("vs-ssh.visualstudio.com" in url or "ssh.dev.azure.com" in url):
        # e.g. org@vs-ssh.visualstudio.com:v3/org/project/repo
        # e.g. git@ssh.dev.azure.com:v3/org/Project/Repo
        # append ssh at start to set correct scheme
        return urlparse("ssh://{original_uri}".format(original_uri=url))
    return urlparse(url)


def uri_quote(query_data):
    return quote(query_data)


def parse_azure_devops_git_remote(remote_url):
    # Reject characters that URL parsers and HTTP transports may interpret differently.
    if not remote_url or _UNSAFE_URL_CHARACTERS.search(remote_url):
        return None

    lowered_url = remote_url.lower()
    if lowered_url.startswith('https://'):
        return _parse_azure_devops_https_git_remote(remote_url)
    if lowered_url.startswith('ssh://') or '@' in remote_url:
        return _parse_azure_devops_ssh_git_remote(remote_url)
    return None


def canonicalize_azure_devops_organization_url(url):  # pylint: disable=too-many-return-statements
    if not url or _UNSAFE_URL_CHARACTERS.search(url):
        return None

    git_remote = parse_azure_devops_git_remote(url)
    if git_remote is not None:
        return git_remote.organization_url

    # Explicit --organization values use a narrower grammar than general service URLs.
    parsed_url = _parse_safe_https_url(url, allow_userinfo=False)
    if parsed_url is None:
        return None

    host, path_segments = parsed_url
    if host == 'dev.azure.com' or _is_dev_azure_service_host(host):
        if len(path_segments) != 1:
            return None
        return 'https://{host}/{organization}'.format(host=host, organization=path_segments[0])

    if _is_visualstudio_host(host) and not path_segments:
        return 'https://{host}/'.format(host=host)
    return None


def organization_url_from_azure_devops_url(url):
    if not url or _UNSAFE_URL_CHARACTERS.search(url):
        return None

    parsed_url = _parse_safe_https_url(url, allow_userinfo=False)
    if parsed_url is None:
        return None

    host, path_segments = parsed_url
    # API and discovery URLs may contain paths after the organization segment.
    if host == 'dev.azure.com' or _is_dev_azure_service_host(host):
        if not path_segments:
            return None
        return 'https://{host}/{organization}'.format(host=host, organization=path_segments[0])

    if _is_visualstudio_host(host):
        return 'https://{host}/'.format(host=host)
    return None


def is_azure_devops_host(host):
    if not host:
        return False
    host = host.lower()
    return host in ('dev.azure.com', 'ssh.dev.azure.com') or _is_dev_azure_service_host(host) or \
        _is_visualstudio_host(host) or host == 'vs-ssh.visualstudio.com'


# Only works for hosted scenario
def uri_parse_instance_from_git_uri(uri):
    git_remote = parse_azure_devops_git_remote(uri)
    if git_remote is not None:
        return git_remote.organization_url
    organization_url = canonicalize_azure_devops_organization_url(uri)
    if organization_url is not None:
        return organization_url
    return uri


def is_valid_url(url):
    parsed_url = uri_parse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    return True


def _parse_azure_devops_https_git_remote(remote_url):  # pylint: disable=too-many-return-statements
    parsed_url = _parse_safe_https_url(remote_url, allow_userinfo=True)
    if parsed_url is None:
        return None

    host, path_segments, userinfo = parsed_url
    if host == 'dev.azure.com':
        # Modern clone URL: /{organization}/{project}/_git/{repository}.
        if len(path_segments) != 4 or path_segments[2].lower() != '_git':
            return None
        organization = path_segments[0]
        if userinfo is not None and userinfo.lower() != organization.lower():
            return None
        organization_url = 'https://dev.azure.com/{organization}'.format(organization=organization)
    elif _is_visualstudio_host(host):
        # Legacy URLs can include collection path segments before project/_git/repository.
        if len(path_segments) < 3 or path_segments[-2].lower() != '_git':
            return None
        if userinfo is not None:
            return None
        organization_url = 'https://{host}/'.format(host=host)
    else:
        return None

    repository_url = 'https://{host}/{path}'.format(
        host=host, path='/'.join(path_segments))
    return AzureDevOpsGitRemote(repository_url, organization_url, host)


def _parse_azure_devops_ssh_git_remote(remote_url):  # pylint: disable=too-many-return-statements
    parsed_url = None
    lowered_url = remote_url.lower()
    if lowered_url.startswith('ssh://'):
        parsed = urlparse(remote_url)
        if parsed.scheme.lower() != 'ssh' or parsed.password or not parsed.username or \
                parsed.query or parsed.fragment:
            return None
        try:
            port = parsed.port
        except ValueError:
            return None
        if port not in (None, 22):
            return None
        parsed_url = (parsed.username, parsed.hostname, parsed.path.strip('/').split('/'))
    else:
        # Match SCP-style SSH remotes such as git@ssh.dev.azure.com:v3/org/project/repo.
        match = re.match(r'^([^@/:]+)@([^@/:]+):(.+)$', remote_url)
        if match is None:
            return None
        # Split the match into SSH username, hostname, and repository path segments.
        parsed_url = (match.group(1), match.group(2), match.group(3).strip('/').split('/'))

    userinfo, host, path_segments = parsed_url
    if not host or not _SAFE_USERINFO.match(userinfo) or any(not segment for segment in path_segments):
        return None

    host = host.lower()
    if path_segments[0].lower() == 'v3':
        # Current SSH form: v3/{organization}/{project}/{repository}.
        if len(path_segments) != 4:
            return None
        organization, project, repository = path_segments[1:]
    elif len(path_segments) == 3 and path_segments[1].lower() == '_ssh':
        # Legacy visualstudio.com URI form: {project}/_ssh/{repository}.
        project, repository = path_segments[0], path_segments[2]
        organization = userinfo
    elif len(path_segments) == 4 and path_segments[2].lower() == '_ssh':
        # Legacy dev.azure.com URI form: {organization}/{project}/_ssh/{repository}.
        organization, project, repository = path_segments[0], path_segments[1], path_segments[3]
    else:
        return None

    if host == 'ssh.dev.azure.com':
        # Convert the modern SSH endpoint to the equivalent canonical HTTPS URL.
        if userinfo.lower() != 'git':
            return None
        https_host = 'dev.azure.com'
        organization_url = 'https://dev.azure.com/{organization}'.format(organization=organization)
        repository_path = '{organization}/{project}/_git/{repository}'.format(
            organization=organization, project=project, repository=repository)
    elif host == 'vs-ssh.visualstudio.com':
        # The SSH username identifies the organization on the legacy endpoint.
        if userinfo.lower() != organization.lower() or not _is_safe_host_label(organization):
            return None
        https_host = '{organization}.visualstudio.com'.format(organization=organization.lower())
        organization_url = 'https://{host}/'.format(host=https_host)
        repository_path = '{project}/_git/{repository}'.format(project=project, repository=repository)
    else:
        return None

    repository_url = 'https://{host}/{path}'.format(host=https_host, path=repository_path)
    return AzureDevOpsGitRemote(repository_url, organization_url, https_host)


def _parse_safe_https_url(url, allow_userinfo):  # pylint: disable=too-many-return-statements
    if _UNSAFE_URL_CHARACTERS.search(url):
        return None

    match = re.match(r'^https://([^/?#]*)(/[^?#]*)?/?$', url, re.IGNORECASE)
    if match is None:
        return None

    authority = match.group(1)
    # Percent-encoding in the authority can produce different hosts across URL parsers.
    if not authority or '%' in authority:
        return None

    userinfo = None
    if '@' in authority:
        if not allow_userinfo or authority.count('@') != 1:
            return None
        userinfo, authority = authority.split('@', 1)
        if not userinfo or ':' in userinfo or not _SAFE_USERINFO.match(userinfo):
            return None

    if ':' in authority:
        # Azure DevOps hosted endpoints support only HTTPS on the default port.
        host, port = authority.rsplit(':', 1)
        if port != '443':
            return None
    else:
        host = authority

    host = host.lower()
    if not is_azure_devops_host(host):
        return None

    path = match.group(2) or ''
    if '//' in path:
        return None
    path_segments = [segment for segment in path.strip('/').split('/') if segment]
    if allow_userinfo:
        return host, path_segments, userinfo
    return host, path_segments


def _is_visualstudio_host(host):
    suffix = '.visualstudio.com'
    if not host.endswith(suffix):
        return False
    organization = host[:-len(suffix)]
    return organization != 'vs-ssh' and _is_safe_host_label(organization)


def _is_dev_azure_service_host(host):
    # Azure DevOps APIs can require a service-specific organization endpoint.
    # Limit this to one Microsoft-controlled DNS label directly under dev.azure.com.
    suffix = '.dev.azure.com'
    if not host.endswith(suffix):
        return False
    service = host[:-len(suffix)]
    return service != 'ssh' and _is_safe_host_label(service)


def _is_safe_host_label(label):
    return bool(_SAFE_HOST_LABEL.match(label))
