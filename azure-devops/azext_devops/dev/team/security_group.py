# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.devops_sdk.exceptions import AzureDevOpsClientRequestError
from azext_devops.devops_sdk.v5_0.graph.models import (JsonPatchOperation,
                                                       GraphSubjectLookup,
                                                       GraphSubjectLookupKey)
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_graph_client,
                                              get_project_id_from_name,
                                              resolve_instance_and_project,
                                              resolve_instance)
from .security_group_helper import (GraphGroupVstsCreationContext,
                                    GraphGroupMailAddressCreationContext,
                                    GraphGroupOriginIdCreationContext)

logger = get_logger(__name__)


def list_groups(scope='project', project=None, continuation_token=None, subject_types=None, organization=None, detect=None):
    """ List all the groups in a project or organization
    :param scope: List groups at project or organization level.
    :type scope: str
    :param continuation_token : If there are more results that can't be returned in a single page, the result set
                                will contain a continuation token for retrieval of the next set of results.
    :type continuation_token: str
    :param subject_types: A comma separated list of user subject subtypes to reduce the retrieved results.
                          This could be the initial part of descriptor [before the dot] e.g. vssgp,aad
    :type subject_types: [str]
    :rtype: :class:`<PagedGraphGroups> <azure.devops.v5_0.graph.models.PagedGraphGroups>`
    """
    if scope == 'project':
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
    else:                                                             
        organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    scope_descriptor = None
    if project is not None:
        project_id = get_project_id_from_name(organization, project)
        scope_descriptor = get_descriptor_from_storage_key(project_id, client)
    if subject_types is not None:
        subject_types = subject_types.split(',')
    group_list_response = client.list_groups(scope_descriptor=scope_descriptor,
                                             continuation_token=continuation_token, subject_types=subject_types)
    return group_list_response


def create_group(name=None, description=None, origin_id=None, email_id=None,
                 groups=None, scope='project', project=None, organization=None, detect=None):
    """
    :param name: Name of Azure DevOps group.
    :type name: str
    :param description: Description of Azure DevOps group.
    :type description: str
    :param origin_id: Create new group using the OriginID as a reference to an existing group
                      from an external AD or AAD backed provider. Required if name or email-id is missing.
    :type origin_id: str
    :param email_id: Create new group using the mail address as a reference to an existing group
                     from an external AD or AAD backed provider. Required if name or origin-id is missing.
    :type email_id: str
    :param groups: A comma separated list of descriptors referencing groups you want the newly created
                   group to join.
    :type groups: [str]
    :param scope: Create group at project or organization level.
    :type scope: str
    :rtype: :class:`<GraphGroup> <azure.devops.v5_0.graph.models.GraphGroup>`
    """
    if scope == 'project':
        organization, project = resolve_instance_and_project(detect=detect,
                                                             organization=organization,
                                                             project=project)
    else:                                                             
        organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    if name is not None and origin_id is None and email_id is None:
        group_creation_context = GraphGroupVstsCreationContext(display_name=name, description=description)
    elif origin_id is not None and email_id is None and name is None:
        group_creation_context = GraphGroupOriginIdCreationContext(origin_id=origin_id)
    elif email_id is not None and name is None and origin_id is None:
        group_creation_context = GraphGroupMailAddressCreationContext(mail_address=email_id)
    else:
        raise CLIError('Provide exactly one argument out of name, origin-id or email-id.')
    scope_descriptor = None
    if project is not None:
        project_id = get_project_id_from_name(organization, project)
        scope_descriptor = get_descriptor_from_storage_key(project_id, client)
    if groups is not None:
        groups = groups.split(',')
    group_details = client.create_group(creation_context=group_creation_context,
                                        scope_descriptor=scope_descriptor, group_descriptors=groups)
    return group_details


def get_group(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show group details.
    :param id: Descriptor of the group.
    :type id: str
    :rtype: :class:`<GraphGroup> <azure.devops.v5_0.graph.models.GraphGroup>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    group_details = client.get_group(group_descriptor=id)
    return group_details


def update_group(id, name=None, description=None, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Update name AND/OR description for an Azure DevOps group.
    :param id: Descriptor of the group.
    :type id: str
    :param name: New name for Azure DevOps group.
    :type name: str
    :param description: New description for Azure DevOps group.
    :type description: str
    :rtype: :class:`<GraphGroup> <azure.devops.v5_0.graph.models.GraphGroup>`
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


def delete_group(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete an Azure DevOps group.
    :param id: Descriptor of the group.
    :type id: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    delete_group_details = client.delete_group(group_descriptor=id)
    return delete_group_details


def list_memberships(id, relationship='members', organization=None, detect=None):  # pylint: disable=redefined-builtin
    """List memberships for a group or user.
    :param id: Group descriptor or User Email whose membership details are required.
    :type id: str
    :rtype: [GraphMembership]
    """
    organization = resolve_instance(detect=detect, organization=organization)
    subject_descriptor = id
    client = get_graph_client(organization)
    if '@' in id or '.' not in id:
        id = resolve_identity_as_id(id, organization)
        subject_descriptor = get_descriptor_from_storage_key(id, client)
    direction = 'down'
    if relationship == 'memberof':
        direction = 'up'
    membership_list = client.list_memberships(subject_descriptor=subject_descriptor, direction=direction)
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
    :param member_id: Descriptor of the group or Email Id of the user to be added.
    :type member_id: str
    :param group_id: Descriptor of the group to which member needs to be added.
    :type group_id: str
    :rtype: :class:`<GraphMembership> <azure.devops.v5_0.graph.models.GraphMembership>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    subject_descriptor = member_id
    if '@' in member_id or '.' not in member_id:
        member_id = resolve_identity_as_id(member_id, organization)
        subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    membership_details = client.add_membership(subject_descriptor=subject_descriptor,
                                               container_descriptor=group_id)
    lookup_keys = []
    container = GraphSubjectLookupKey(membership_details.container_descriptor)
    subject = GraphSubjectLookupKey(membership_details.member_descriptor)
    lookup_keys.append(container)
    lookup_keys.append(subject)
    subject_lookup = GraphSubjectLookup(lookup_keys=lookup_keys)
    membership_details = client.lookup_subjects(subject_lookup=subject_lookup)
    return membership_details


def remove_membership(member_id, group_id, organization=None, detect=None):
    """Remove membership.
    :param member_id: Descriptor of the group or Email Id of the user to be removed.
    :type member_id: str
    :param group_id: Descriptor of the group from which member needs to be removed.
    :type group_id: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_graph_client(organization)
    subject_descriptor = member_id
    if '@' in member_id or '.' not in member_id:
        member_id = resolve_identity_as_id(member_id, organization)
        subject_descriptor = get_descriptor_from_storage_key(member_id, client)
    try:
        client.check_membership_existence(subject_descriptor=subject_descriptor,
                                          container_descriptor=group_id)
        membership_details = client.remove_membership(subject_descriptor=subject_descriptor,
                                                      container_descriptor=group_id)
    except AzureDevOpsClientRequestError as ex:
        logger.debug(ex, exc_info=True)
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
