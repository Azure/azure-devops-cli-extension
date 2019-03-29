# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import pdb
from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.graph.models import (JsonPatchOperation,
                                                       GraphSubjectLookup,
                                                       GraphSubjectLookupKey)
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_graph_client,
                                              resolve_instance)

from .security_group_helper import GraphGroupVstsCreationContext


def list_groups(project_id=None, continuation_token=None, subject_types=None, organization=None, detect=None):
    """ List all groups.
    :param str project_id: List groups for a particular project.
    :param [str] subject_types: A comma separated list of user subject subtypes to reduce the retrieved results.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    scope_descriptor = None
    if project_id is not None:
        scope_descriptor = get_descriptor_from_storage_key(project_id, client)
    if subject_types is not None:
        subject_types = subject_types.split(',')
    group_list_response = client.list_groups(scope_descriptor=scope_descriptor,
                                             continuation_token=continuation_token, subject_types=subject_types)
    if group_list_response.continuation_token is not None:
        print('Showing only 500 groups.' +
              ' To list next set of groups use this continuation token and run the command again. TOKEN:',
              group_list_response.continuation_token)
    return group_list_response.graph_groups


def create_group(name, description=None, project_id=None, organization=None, detect=None):
    """Create a group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    scope_descriptor = None
    if project_id is not None:
        scope_descriptor = get_descriptor_from_storage_key(project_id, client)
    group_creation_context = GraphGroupVstsCreationContext(display_name=name, description=description)
    group_details = client.create_group(creation_context=group_creation_context, scope_descriptor=scope_descriptor)
    return group_details


def get_group(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show group details.
    :param str id: The UUID of the group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    group_descriptor = get_descriptor_from_storage_key(id, client)
    group_details = client.get_group(group_descriptor=group_descriptor)
    return group_details


def update_group(id, name=None, description=None, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Update name AND/OR description for a group.
    :param str id: The UUID of the group.
    """
    if name is None and description is None:
        raise CLIError('Either name or description argument must be provided.')
    patch_document = []
    if name is not None:
        patch_document.append(_create_patch_operation('replace', '/displayName', name))
    if description is not None:
        patch_document.append(_create_patch_operation('replace', '/description', description))
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    group_descriptor = get_descriptor_from_storage_key(id, client)
    update_group_details = client.update_group(group_descriptor=group_descriptor, patch_document=patch_document)
    return update_group_details


def delete_group(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete group.
    :param str id: The UUID of the group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    group_descriptor = get_descriptor_from_storage_key(id, client)
    delete_group_details = client.delete_group(group_descriptor=group_descriptor)
    return delete_group_details


def list_memberships(id, relationship='members', organization=None, detect=None):  # pylint: disable=redefined-builtin
    """List memberships.
    :param str id: Group UUID whose membership details are required.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if '@' in id:
        id = resolve_identity_as_id(id, organization)
    subject_descriptor = get_descriptor_from_storage_key(id, client)
    direction = 'down'
    if relationship == 'memberof':
        direction = 'up'
    membership_list = client.list_memberships(subject_descriptor, direction=direction)
    lookup_keys = []
    for members in membership_list:
        if relationship == 'memberof':
            key = GraphSubjectLookupKey(members.container_descriptor)
        else:
            key = GraphSubjectLookupKey(members.member_descriptor)
        lookup_keys.append(key)
    subject_lookup = GraphSubjectLookup(lookup_keys=lookup_keys)
    members_details = client.lookup_subjects(subject_lookup=subject_lookup)
    return members_details


def add_membership(member_id, group_id, organization=None, detect=None):
    """Add membership.
    :param str member_id: Id of User or group to be added.
    :param str group_id: Id of the group to which member needs to be added.
    """
    pdb.set_trace()
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if '@' in member_id:
        member_id = resolve_identity_as_id(member_id, organization)
    subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    container_descriptor = get_descriptor_from_storage_key(group_id, client)
    membership_details = client.add_membership(subject_descriptor=subject_descriptor,
                                               container_descriptor=container_descriptor)
    lookup_keys = []
    lookup_keys.append(GraphSubjectLookupKey(membership_details.member_descriptor))
    lookup_keys.append(GraphSubjectLookupKey(membership_details.container_descriptor))
    subject_lookup = GraphSubjectLookup(lookup_keys=lookup_keys)
    members_lookup_details = client.lookup_subjects(subject_lookup=subject_lookup)
    return members_lookup_details


def remove_membership(member_id, group_id, organization=None, detect=None):
    """Remove membership.
    :param str member_id: Id of User or group to be removed.
    :param str group_id: Id of the group from which member needs to be removed.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if '@' in member_id:
        member_id = resolve_identity_as_id(member_id, organization)
    subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    container_descriptor = get_descriptor_from_storage_key(group_id, client)
    try:
        client.check_membership_existence(subject_descriptor=subject_descriptor,
                                          container_descriptor=container_descriptor)
        membership_details = client.remove_membership(subject_descriptor=subject_descriptor,
                                                      container_descriptor=container_descriptor)
    except:
        raise CLIError("Membership doesn't exists.")
    return membership_details


def get_descriptor_from_storage_key(storage_key, client):
    descriptor = client.get_descriptor(storage_key)
    return descriptor


def _create_patch_operation(op, path, value):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation
