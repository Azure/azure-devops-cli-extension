# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_security_client,
                                              resolve_instance)


def list_namespaces(organization=None, detect=None):
    """ List all available namespaces for an organization.
    """
    #local only param
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    response = client.query_security_namespaces(None)
    return response


def show_namespace(namespace_id, organization=None, detect=None):
    """ Show details of a permissions avaialble in each namespace.
    :param security_namespace_id: Namespace ID.
    :type id: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    response = client.query_security_namespaces(security_namespace_id=namespace_id)
    return response
