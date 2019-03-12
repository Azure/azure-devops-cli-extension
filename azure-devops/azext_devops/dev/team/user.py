# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.member_entitlement_management.v4_1.models.models import (UserEntitlement, ProjectRef, Group,
                                                                                          ProjectEntitlement,
                                                                                          AccessLevel,
                                                                                          Extension,
                                                                                          GroupEntitlement,
                                                                                          GraphUser,
                                                                                          JsonPatchOperation)
from azext_devops.dev.common.services import (get_member_entitlement_management_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import resolve_identity_as_id


def get_user_entitlements(top=None, skip=None, organization=None, detect=None):
    """List users for an organization.
    :param int top: Maximum number of the users to return. Max value is 10000. Default value is 100
    :param int skip: Offset: Number of records to skip.
    :rtype: [UserEntitlement]
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_entitlements = client.get_user_entitlements(top=top, skip=skip)
    return user_entitlements


def get_user_entitlement(user, organization=None, detect=None):
    """Show user details.
    :param user: The Email id or UUID of the user.
    :type user: str
    :rtype: UserEntitlement
    """
    organization = resolve_instance(detect=detect, organization=organization)
    if '@' in user:
        user = resolve_identity_as_id(user, organization)
    client = get_member_entitlement_management_client(organization)
    user_entitlement_details = client.get_user_entitlement(user_id=user)
    return user_entitlement_details


def delete_user_entitlement(user, organization=None, detect=None):
    """Remove user from an organization.
    :param user: The Email id or UUID of the user.
    :type user: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    if '@' in user:
        user = resolve_identity_as_id(user, organization)
    client = get_member_entitlement_management_client(organization)
    delete_user_entitlement_details = client.delete_user_entitlement(user_id=user)
    return delete_user_entitlement_details


def update_user_entitlement(user, access_level, organization=None, detect=None):
    """Update access level for a user.
    :param user: The Email id or UUID of the user.
    :type user: str
    :param access_level: Access level for the user. 
    :type access_level: str
    :rtype: UserEntitlementsPatchResponse
    """
    patch_document = []
    value = {}
    value['account_license_type'] = access_level
    patch_document.append(_create_patch_operation('replace','accessLevel',value))
    organization = resolve_instance(detect=detect, organization=organization)
    if '@' in user:
        user = resolve_identity_as_id(user, organization)
    client = get_member_entitlement_management_client(organization)
    user_entitlement_update = client.update_user_entitlement(document=patch_document,user_id=user)
    return user_entitlement_update.user_entitlement


def add_user_entitlement(user, access_level, organization=None, detect=None):
    """Add user.
    :param user: The Email id of the user.
    :type user: str
    :param access_level: Access level for the user. 
    :type access_level: str
    :rtype: UserEntitlementsPatchResponse
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_access_level = AccessLevel()
    user_access_level.account_license_type = access_level
    graph_user = GraphUser()
    graph_user.subject_kind = 'user'
    graph_user.principal_name = user
    user_entitlement = UserEntitlement()
    user_entitlement.access_level = user_access_level
    user_entitlement.user = graph_user
    user_entitlement_details = client.add_user_entitlement(user_entitlement)
    return user_entitlement_details.user_entitlement


def _create_patch_operation(op, field, value):
    path = '/{field}'.format(field=field)
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation