# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pdb
from azext_devops.dev.common.services import (get_security_client,
                                              get_graph_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import get_identity_descriptor_from_subject_descriptor
from azext_devops.dev.common.uuid import is_uuid

def list_namespaces(local_only=False, organization=None, detect=None):
    """ List all available namespaces for an organization.
    :param local_only: If true, retrieve only local security namespaces.
    :type local_only: bool
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    response = client.query_security_namespaces(local_only=local_only)
    return response


def show_namespace(namespace_id, organization=None, detect=None):
    """ Show details of a permissions avaialble in each namespace.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    response = client.query_security_namespaces(security_namespace_id=namespace_id)
    return response


def list_permissions(namespace_id, subject=None, token=None, include_extended_info=True, recurse=False, organization=None, detect=None):
    """ List permissions
    :param token: Security token.
    :type token: str
    :param subject: User or Group ID for which permission details are required.
    :type subject: str
    """
    #pdb.set_trace()
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if subject is not None and not is_uuid(subject) and '.' in subject:
        # try to solve graph descriptor
        subject = get_identity_descriptor_from_subject_descriptor(organization,subject)
    response = client.query_access_control_lists(security_namespace_id=namespace_id, 
                                                token=token, descriptors=subject, 
                                                include_extended_info=include_extended_info, recurse=recurse )
    return response


def resolve_permissions(namespace_id, allow_bit, deny_bit, organization=None, detect=None):
    """ Resolve permissions
    :param josn_response: Response json
    :type josn_response: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    permissions_types = client.query_security_namespaces(security_namespace_id=namespace_id)
    permission_response = []
    for item in permissions_types[0].actions:
        if item.bit & deny_bit:
            permission = {}
            permission['displayName'] = item.display_name
            permission['name'] = item.name
            permission['effectivePermission'] = 'Deny'
            permission_response.append(permission)
        elif item.bit & allow_bit:
            permission = {}
            permission['displayName'] = item.display_name
            permission['name'] = item.name
            permission['effectivePermission'] = 'Allow'
            permission_response.append(permission)
    return permission_response


def get_storage_key_from_graph_descriptor(descriptor, organization):
    client = get_graph_client(organization)
    storage_key = client.get_storage_key(subject_descriptor=descriptor)
    return storage_key

