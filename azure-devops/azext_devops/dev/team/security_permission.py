# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pdb
from knack.util import CLIError
from knack.log import get_logger
from azext_devops.devops_sdk.exceptions import AzureDevOpsClientRequestError
from azext_devops.devops_sdk.v5_0.security.models import (AccessControlEntry)
from azext_devops.dev.common.services import (get_security_client,
                                              get_graph_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import (get_identity_descriptor_from_subject_descriptor,
                                                resolve_identity_as_identity_descriptor)
from azext_devops.dev.common.uuid import is_uuid

logger = get_logger(__name__)


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


def list_permissions(namespace_id, subject, token=None, include_extended_info=True, recurse=False, organization=None, detect=None):
    """ List permissions
    :param token: Security token.
    :type token: str
    :param subject: User or Group ID for which permission details are required.
    :type subject: str
    """
    #pdb.set_trace()
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph descriptor
        subject = get_identity_descriptor_from_subject_descriptor(organization,subject)
    response = client.query_access_control_lists(security_namespace_id=namespace_id, 
                                                token=token, descriptors=subject, 
                                                include_extended_info=include_extended_info, recurse=recurse )
    return response

def reset_all_permissions(namespace_id, subject, token, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph descriptor
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    response = client.remove_access_control_entries(security_namespace_id=namespace_id,
                                                   token=token, descriptors=subject)
    return response


def resolve_permissions(namespace_id, allow_bit=None, deny_bit=None, organization=None, detect=None):
    """ Resolve permissions
    """
    if allow_bit is None and deny_bit is None:
        raise CLIError('Either --allow-bit or --deny-bit parameter should be provided.')
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    permissions_types = client.query_security_namespaces(security_namespace_id=namespace_id)
    permission_response = []
    for item in permissions_types[0].actions:
        if deny_bit and item.bit & deny_bit:
            permission = {}
            permission['displayName'] = item.display_name
            permission['name'] = item.name
            permission['effectivePermission'] = 'Deny'
            permission_response.append(permission)
        elif allow_bit and item.bit & allow_bit:
            permission = {}
            permission['displayName'] = item.display_name
            permission['name'] = item.name
            permission['effectivePermission'] = 'Allow'
            permission_response.append(permission)
    return permission_response



def reset_permissions(namespace_id, permissions, subject, token, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph descriptor
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    response = client.remove_permission(security_namespace_id=namespace_id, permissions=permissions,
                                        descriptor=subject, token=token)
    return response


def add_permissions(namespace_id, subject, token, merge=True, allow_bit=None, deny_bit=None, organization=None, detect=None):
    """
    :param merge: Merge the existing permissions or replace them.
    :type auto_complete: bool
    """
    pdb.set_trace()
    if allow_bit is None and deny_bit is None:
        raise CLIError('Either --allow-bit or --deny-bit parameter should be provided.')
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph descriptor
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    container_object = {}
    aces_list = []
    ace_object = AccessControlEntry(descriptor=subject, allow=allow_bit, deny=deny_bit)
    aces_list.append(ace_object)
    container_object['token'] = token
    if merge:
        container_object['merge'] = True
    else:
       container_object['merge'] = False
    container_object['accessControlEntries'] = aces_list
    try:
        response = client.set_access_control_entries(security_namespace_id=namespace_id, container=container_object)
        return response
    except Exception as ex:
        logger.debug(ex, exc_info=True)
        message = ex.args[0]
        if 'it is reserved by the system' not in message:
            raise CLIError(ex)


def get_storage_key_from_graph_descriptor(descriptor, organization):
    client = get_graph_client(organization)
    storage_key = client.get_storage_key(subject_descriptor=descriptor)
    return storage_key

