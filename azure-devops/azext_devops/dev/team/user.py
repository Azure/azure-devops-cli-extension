# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.vstsCompressed.member_entitlement_management.v4_1.models.models import (AccessLevel,
                                                                                          GraphUser,
                                                                                          JsonPatchOperation)
from azext_devops.dev.common.services import (get_member_entitlement_management_client,
                                              resolve_instance)
from azext_devops.dev.common.arguments import resolve_true_false
from azext_devops.dev.common.identities import resolve_identity_as_id


def get_user_entitlements(top=100, skip=None, organization=None, detect=None):
    """List users for an organization [except for AAD users].
    :param int top: Maximum number of the users to return. Max value is 10000.
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


def update_user_entitlement(user, license_type, organization=None, detect=None):
    """Update license type for a user.
    :param user: The Email id or UUID of the user.
    :type user: str
    :param license_type: License type for the user.
    :type license_type: str
    :rtype: UserEntitlementsPatchResponse
    """
    patch_document = []
    value = {}
    value['accountLicenseType'] = license_type
    patch_document.append(_create_patch_operation('replace', '/accessLevel', value))
    organization = resolve_instance(detect=detect, organization=organization)
    if '@' in user:
        user = resolve_identity_as_id(user, organization)
    client = get_member_entitlement_management_client(organization)
    try:
        user_entitlement_update = client.update_user_entitlement(document=patch_document, user_id=user)
        return user_entitlement_update.user_entitlement
    except Exception:
        raise CLIError('Invalid license type.')


def add_user_entitlement(user, license_type, send_email_invite='true', organization=None, detect=None):
    """Add user.
    :param user: The Email id of the user.
    :type user: str
    :param license_type: License type for the user.
    :type license_type: str
    :rtype: UserEntitlementsPatchResponse
    """
    do_not_send_invite = False
    do_not_send_invite = not resolve_true_false(send_email_invite)
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_access_level = AccessLevel()
    user_access_level.account_license_type = license_type
    graph_user = GraphUser()
    graph_user.subject_kind = 'user'
    graph_user.principal_name = user
    value = {}
    value['accessLevel'] = user_access_level
    value['extensions'] = []
    value['projectEntitlements'] = []
    value['user'] = graph_user
    patch_document = []
    patch_document.append(_create_patch_operation('add', '', value))
    try:
        user_entitlement_details = client.update_user_entitlements(document=patch_document,
                                                                   do_not_send_invite_for_new_users=do_not_send_invite)
        user_entitlement_details.results[0].result                                    
    except Exception:
        raise CLIError('Invalid license type.')


def _create_patch_operation(op, path, value):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation
