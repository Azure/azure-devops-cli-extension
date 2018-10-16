# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

try:
    from urllib.parse import urlparse, quote
except ImportError:
    from urlparse import urlparse
    from urllib import quote


def uri_parse(url):
    return urlparse(url)


def uri_quote(query_data):
    return quote(query_data)

def uri_parse_instance_from_git_uri(uri):
    if("/_git" in uri):
        parsed_uri = urlparse(uri)
        #old Uri format
        if("visualstudio.com" in uri):
            return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        #new Uri format
        if("dev.azure.com" in uri):
            org_name = parsed_uri.path.strip("/").split("/")[0]
            return parsed_uri.scheme + "://" + parsed_uri.hostname + "/" + org_name

    return uri