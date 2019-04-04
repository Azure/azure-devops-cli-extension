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
                                              get_core_client,
                                              resolve_instance)
from azext_devops.dev.common.uuid import is_uuid
from .security_group_helper import (GraphGroupVstsCreationContext,
                                    GraphGroupMailAddressCreationContext,
                                    GraphGroupOriginIdCreationContext)


def list_groups(project=None, continuation_token=None, subject_types=None, organization=None, detect=None):
    """ List all groups.
    :param str project: List groups for a particular project.
    :param str continuation_token : If there are more results than can't be returned in a single page,\
     the result set will containt a continuation token for retrieval of the next set of results.
    :param [str] subject_types: A comma separated list of user subject subtypes to reduce the retrieved results.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    scope_descriptor = None
    if project is not None and not is_uuid(project):
        project = _get_project_id(organization,project)
        scope_descriptor = get_descriptor_from_storage_key(project, client)
    if subject_types is not None:
        subject_types = subject_types.split(',')
    group_list_response = client.list_groups(scope_descriptor=scope_descriptor,
                                             continuation_token=continuation_token, subject_types=subject_types)
    if group_list_response.continuation_token is not None:
        print('Showing only 500 groups.' +
              ' To list next set of groups use this token as --continuation-token argument and run the command again. TOKEN:',
              group_list_response.continuation_token)
    return group_list_response.graph_groups


def create_group(name=None, description=None, origin_id=None, groups, email_id=None, project=None, organization=None, detect=None):
    """Create a new Azure DevOps group or materialize an existing AAD group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    scope_descriptor = None
    if project is not None and not is_uuid(project):
        if name is None:
            raise CLIError('--project argument is only valid for VSTS groups.')
        project = _get_project_id(organization,project)
        scope_descriptor = get_descriptor_from_storage_key(project, client)
    if name is not None and origin_id is None and emaild_id is None:
        group_creation_context = GraphGroupVstsCreationContext(display_name=name, description=description)
    elif origin_id is not None and email_id is None:
        group_creation_context = GraphGroupOriginIdCreationContext(origin_id=origin_id)
    elif email_id is not None:
        group_creation_context =GraphGroupMailAddressCreationContext(mail_address=email_id)
    else:
        raise CLIError('Provide exactly one value out of name, origin_id and email_id')
    group_details = client.create_group(creation_context=group_creation_context, scope_descriptor=scope_descriptor)
    return group_details


def get_group(id, organization=None, detect=None):
    """Show group details.
    :param str id: Descriptor of the group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    group_details = client.get_group(group_descriptor=id)
    return group_details


def update_group(id, name=None, description=None, organization=None, detect=None):
    """Update name AND/OR description for a Azure DevOps group.
    :param str id: Descriptor of the group.
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
    update_group_details = client.update_group(group_descriptor=id, patch_document=patch_document)
    return update_group_details


def delete_group(id, organization=None, detect=None):
    """Delete an Azure DevOps group.
    :param str id: ID of the group.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    delete_group_details = client.delete_group(group_descriptor=id)
    return delete_group_details


def list_memberships(id, relationship='members', organization=None, detect=None):
    """List memberships.
    :param str id: Group descriptor whose membership details are required.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if '@' in id:
        id = resolve_identity_as_id(id, organization)
    direction = 'down'
    if relationship == 'memberof':
        direction = 'up'
    membership_list = client.list_memberships(subject_descriptor=id, direction=direction)
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
    if not is_uuid(member_id):
        member_id = resolve_identity_as_id(member_id, organization)
    subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    membership_details = client.add_membership(subject_descriptor=subject_descriptor,
                                               container_descriptor=group_id)
    return membership_details
    

def remove_membership(member_id, group_id, organization=None, detect=None):
    """Remove membership.
    :param str member_id: Id of User or group to be removed.
    :param str group_id: Id of the group from which member needs to be removed.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if not is_uuid(member_id):
        member_id = resolve_identity_as_id(member_id, organization)
    subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    try:
        client.check_membership_existence(subject_descriptor=subject_descriptor,
                                          container_descriptor=group_id)
        membership_details = client.remove_membership(subject_descriptor=subject_descriptor,
                                                      container_descriptor=group_id)
    except:
        raise CLIError("Membership doesn't exists.")
    return membership_details


def get_descriptor_from_storage_key(storage_key, client):
    descriptor = client.get_descriptor(storage_key)
    return descriptor

def get_storage_key_from_descriptor(descriptor, client):
    storage_key= client.get_storage_key(subject_descriptor=descriptor)
    return storage_key

def _create_patch_operation(op, path, value):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation

def _get_project_id(organization, project):
    core_client = get_core_client(organization)
    project = core_client.get_project(project_id=project)
    return project.id
