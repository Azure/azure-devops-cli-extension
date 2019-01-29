# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

try:
    from urllib.parse import urlparse, quote
except ImportError:
    from urllib import quote
    from urlparse import urlparse


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


# Only works for hosted scenario
def uri_parse_instance_from_git_uri(uri):
    if "/_git" in uri:
        parsed_uri = urlparse(uri)
        # old Uri format
        if "visualstudio.com" in uri:
            return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        # new Uri format
        if "dev.azure.com" in uri:
            org_name = parsed_uri.path.strip("/").split("/")[0]
            return parsed_uri.scheme + "://" + parsed_uri.hostname + "/" + org_name

    return uri
