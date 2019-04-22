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


def list_permissions(namespace_id, subject, token=None, include_extended_info=True,
                     recurse=False, organization=None, detect=None):
    """ List permissions
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
    response = client.query_access_control_lists(security_namespace_id=namespace_id,
                                                 token=token, descriptors=subject,
                                                 include_extended_info=include_extended_info, recurse=recurse)
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
    """ Assign Allow or Deny permission to this user/group.
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


def resolve_permissions_json(namespace_id, json_path, organization=None, detect=None):
    """ Resolve permissions with json
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_security_client(organization)
    permissions_types = client.query_security_namespaces(security_namespace_id=namespace_id)
    with open(json_path) as file:
        response_json = json.load(file)
        inherited_allow = 0
        inherited_deny = 0
        effective_allow = 0
        effective_deny = 0
        if len(response_json) > 1 or len(response_json[0]['acesDictionary']) > 1:
            raise CLIError('The Json response can only have one entry in acesDictionary.')
        acl = list(response_json[0]['acesDictionary'].values())[0]
        print(acl)
        allow_bit = acl['allow']
        deny_bit = acl['deny']
        if acl['extendedInfo']['effectiveAllow'] is not None:
            effective_allow = acl['extendedInfo']['effectiveAllow']
        if acl['extendedInfo']['effectiveDeny'] is not None:
            effective_deny = acl['extendedInfo']['effectiveDeny']
        if response_json[0]['includeExtendedInfo'] is True:
            inherited_allow = allow_bit ^ effective_allow
            inherited_deny = deny_bit ^ effective_deny
        permission_response = []
        for item in permissions_types[0].actions:
            permission = {}
            permission['displayName'] = item.display_name
            permission['name'] = item.name
            if effective_deny and item.bit & effective_deny:
                permission['effectivePermission'] = 'Deny'
                if inherited_deny & item.bit:
                    permission['effectivePermission'] = 'Deny(Inherited)'
            elif effective_allow and item.bit & effective_allow:
                permission['effectivePermission'] = 'Allow'
                if inherited_allow & item.bit:
                    permission['effectivePermission'] = 'Allow(Inherited)'
            else:
                permission['effectivePermission'] = 'Not set'
            permission_response.append(permission)
        return permission_response
