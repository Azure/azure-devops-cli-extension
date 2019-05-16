# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.devops_sdk.v5_0.security.models import (AccessControlEntry)
from azext_devops.dev.common.services import (get_security_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import (get_identity_descriptor_from_subject_descriptor,
                                                resolve_identity_as_identity_descriptor)
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
    """ Show details of permissions available in each namespace.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    response = _get_permission_types(client, namespace_id)
    return response

def list_tokens(namespace_id, subject, token=None,
                recurse=False, organization=None, detect=None):
    """ List tokens for given user/group and namespace.
    :param recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.
    :type recurse: bool
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    subject = _resolve_subject_as_identity_descriptor(subject, organization)
    response = _query_permissions(client, namespace_id, subject, token, recurse)
    return response


def show_permissions(namespace_id, subject, token, organization=None, detect=None):
    """ Show permissions for given token, namespace and user/group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    subject = _resolve_subject_as_identity_descriptor(subject, organization)
    list_response = _query_permissions(client, namespace_id, subject, token, False)
    permissions_types = _get_permission_types(client, namespace_id)
    resolved_permissions_response = _resolve_bits(list_response, permissions_types)
    response = _update_json(list_response, resolved_permissions_response)
    return response

def reset_all_permissions(namespace_id, subject, token, organization=None, detect=None):
    """ Clear all permissions of this token for a user/group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    subject = _resolve_subject_as_identity_descriptor(subject, organization)
    response = client.remove_access_control_entries(security_namespace_id=namespace_id,
                                                    token=token, descriptors=subject)
    return response


def reset_permissions(namespace_id, permission_bit, subject, token, organization=None, detect=None):
    """ Reset permission for given permission bit(s)
    :param permission_bit: Permission bit or addition of permission bits which needs to be reset
                           for given user/group and token.
    :type permission_bit:int
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    subject = _resolve_subject_as_identity_descriptor(subject, organization)
    client.remove_permission(security_namespace_id=namespace_id, permissions=permission_bit,
                             descriptor=subject, token=token)
    # get the effective permission list for this namespace , token
    list_response = _query_permissions(client, namespace_id, subject, token, False)
    permissions_types = _get_permission_types(client, namespace_id)
    resolved_permissions_response = _resolve_bits(list_response, permissions_types, permission_bit)
    response = _update_json(list_response, resolved_permissions_response)
    return response


def update_permissions(namespace_id, subject, token, merge=True, allow_bit=0, deny_bit=0,
                       organization=None, detect=None):
    """ Assign allow or deny permission to given user/group.
    """
    if allow_bit == 0 and deny_bit == 0:
        raise CLIError('Either --allow-bit or --deny-bit parameter should be provided.')
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    subject = _resolve_subject_as_identity_descriptor(subject, organization)
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
    client.set_access_control_entries(security_namespace_id=namespace_id, container=container_object)
    allow_bit = allow_bit & (~deny_bit)
    changed_bits = allow_bit + deny_bit
    list_response = _query_permissions(client, namespace_id, subject, token, False)
    permissions_types = _get_permission_types(client, namespace_id)
    resolved_permissions_response = _resolve_bits(list_response, permissions_types, changed_bits)
    response = _update_json(list_response, resolved_permissions_response)
    return response


def _resolve_bits(response, permissions_types, changed_bits=0):
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
    # If changed_bits is zero, display all permissions
    if changed_bits == 0:
        total_permission_types = len(permissions_types[0].actions)
        last_permission_bit_value = permissions_types[0].actions[total_permission_types-1].bit
        changed_bits = 2*last_permission_bit_value - 1

    permission_response = []
    for item in permissions_types[0].actions:
        if changed_bits & item.bit:
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

            permission_obj = PermissionDetails()
            permission_obj.bit = item.bit
            permission_obj.name = item.name
            permission_obj.display_name = item.display_name
            permission_obj.effective_permission = permission_value_string
            permission_response.append(permission_obj)
    return permission_response


def _update_json(original_response, permissions_response):
    response = []
    for acl in original_response:
        acl_value = acl.serialize()
        for ace in acl_value['acesDictionary']:
            acl_value['acesDictionary'][ace]['resolvedPermissions'] = permissions_response
        response.append(acl_value)
    return response


def _get_permission_types(client, namespace_id):
    response = client.query_security_namespaces(security_namespace_id=namespace_id)
    return response


def _query_permissions(client, namespace_id, subject, token, recurse):
    list_response = client.query_access_control_lists(security_namespace_id=namespace_id,
                                                      token=token, descriptors=subject,
                                                      include_extended_info=True, recurse=recurse)
    return list_response


def _resolve_subject_as_identity_descriptor(subject,organization):
    if '@' in subject:
        subject = resolve_identity_as_identity_descriptor(identity_filter=subject, organization=organization)
    elif '.' in subject:
        # try to solve graph subject descriptor for groups
        subject = get_identity_descriptor_from_subject_descriptor(subject_descriptor=subject, organization=organization)
    return subject
    