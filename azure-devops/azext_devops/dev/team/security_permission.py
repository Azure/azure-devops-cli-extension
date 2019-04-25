# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import json
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
from .security_permission_helper import PermissionDetails
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
    """ Show details of permissions avaialble in each namespace.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    response = _get_permission_types(namespace_id, organization)
    return response

def list_tokens(namespace_id, subject, include_extended_info=True,
                     recurse=False, organization=None, detect=None):
    """ List tokens for given user/group and namespace.
    :param include_extended_info: Populate the extended information properties for the access control entries
                                  contained in the returned lists.
    :type include_extended_info: bool
    :param recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.
    :type recurse: bool
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph subject descriptor for groups
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    response = client.query_access_control_lists(security_namespace_id=namespace_id, descriptors=subject,
                                                 include_extended_info=include_extended_info, recurse=recurse)
    return response


def show_permissions(namespace_id, subject, token, include_extended_info=True,
                     recurse=False, organization=None, detect=None):
    """ Show permissions for given token, namespace and user/group.
    :param include_extended_info: Populate the extended information properties for the access control entries
                                  contained in the returned lists.
    :type include_extended_info: bool
    :param recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.
    :type recurse: bool
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph subject descriptor for groups
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    raw_response = client.query_access_control_lists(security_namespace_id=namespace_id,
                                                 token=token, descriptors=subject,
                                                 include_extended_info=include_extended_info, recurse=recurse)
    permissions_types = client.query_security_namespaces(security_namespace_id=namespace_id)
    resolved_permissions_response = None
    resolved_permissions_response = _resolve_bits(raw_response, permissions_types)
    import pdb
    pdb.set_trace()
    for acl in raw_response:
        for ace in acl.aces_dictionary:
            ace_value = acl.aces_dictionary[ace].serialize()
            ace_value['resolvedPermissions'] = resolved_permissions_response

    response = _update_json(raw_response, resolved_permissions_response)
    return response

def reset_all_permissions(namespace_id, subject, token, organization=None, detect=None):
    """ Clear all permissions of this token for a user or group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph subject descriptor for groups
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    response = client.remove_access_control_entries(security_namespace_id=namespace_id,
                                                    token=token, descriptors=subject)
    return response


def reset_permissions(namespace_id, permissions, subject, token, organization=None, detect=None):
    """ Reset permission for given permission bits
    :param permissions: Permission bits which needs to be reset for given user/group and token.
    :type permissions:str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph subject descriptor for groups
        subject = get_identity_descriptor_from_subject_descriptor(organization, subject)
    response = client.remove_permission(security_namespace_id=namespace_id, permissions=permissions,
                                        descriptor=subject, token=token)
    return response


def add_permissions(namespace_id, subject, token, merge=True, allow_bit=None, deny_bit=None,
                    organization=None, detect=None):
    """ Assign allow or deny permission to this user/group.
    """
    if allow_bit is None and deny_bit is None:
        raise CLIError('Either --allow-bit or --deny-bit parameter should be provided.')
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(subject, organization)
    elif not is_uuid(subject) and '.' in subject:
        # try to solve graph subject descriptor for groups
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


def _resolve_bits(response, permissions_types):
    
    inherited_allow = 0
    inherited_deny = 0
    effective_allow = 0
    effective_deny = 0
    if len(response) > 1 or len(response[0].aces_dictionary) > 1:
        raise CLIError('Multiple entries found in acesDictionary. Please filter the response by token.')
    acl = response[0]
    ace = list(acl.aces_dictionary.values())[0]
    allow_bit = ace.allow
    deny_bit = ace.deny
    if acl.include_extended_info is True:
        if ace.extended_info.effective_allow is not None:
            effective_allow = ace.extended_info.effective_allow
        if ace.extended_info.effective_deny is not None:
            effective_deny = ace.extended_info.effective_deny       
    if acl.include_extended_info is True:
        inherited_allow = allow_bit ^ effective_allow
        inherited_deny = deny_bit ^ effective_deny

    permission_response = []
    for item in permissions_types[0].actions:
        permission_value_string = None
        if effective_deny and item.bit & effective_deny:
            permission_value_string = 'Deny'
            if inherited_deny & item.bit:
                permission_value_string = 'Deny (inherited)'
        elif effective_allow and item.bit & effective_allow:
            permission_value_string = 'Allow'
            if inherited_allow & item.bit:
                permission_value_string = 'Allow (inherited)'
        else:
            permission_value_string = 'Not set'

        perm_obj = PermissionDetails()
        perm_obj.bit = item.bit
        perm_obj.name = item.name
        perm_obj.display_name = item.display_name
        perm_obj.effective_permission = permission_value_string
        permission_response.append(perm_obj) 
    return permission_response


def _update_json(original_response, permissions_response):
    response = []
    for acl in original_response:
        acl_value = acl.serialize()
        for ace in acl_value['acesDictionary']:
            acl_value['acesDictionary'][ace]['resolvedPermissions'] = permissions_response
        response.append(acl_value)
    return response


def _get_permission_types(namespace_id, organization):
    client = get_security_client(organization)
    response = client.query_security_namespaces(security_namespace_id=namespace_id)
    return response
