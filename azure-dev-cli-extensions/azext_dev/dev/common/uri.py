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
