# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.member_entitlement_management.models import (AccessLevel,
                                                                               GraphUser,
                                                                               JsonPatchOperation)
from azext_devops.dev.common.services import (get_member_entitlement_management_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import resolve_identity_as_id


def get_user_entitlements(top=100, skip=None, organization=None, detect=None):
    """List users in an organization [except for users which are added via AAD groups].
    :param int top: Maximum number of users to return. Max value is 10000.
    :param int skip: Offset: Number of records to skip.
    :rtype: [UserEntitlement]
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_entitlements = client.get_user_entitlements(top=top, skip=skip)
    return user_entitlements


def get_user_entitlement(user, organization=None, detect=None):
    """Show user details.
    :param user: Email ID or ID of the user.
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
    :param user: Email ID or ID of the user.
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
    :param user: Email ID or ID of the user.
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
    user_entitlement_update = client.update_user_entitlement(document=patch_document, user_id=user)
    if user_entitlement_update.is_success is False and \
            user_entitlement_update.operation_results[0].errors[0] is not None:
        raise CLIError(user_entitlement_update.operation_results[0].errors[0]['value'])
    return user_entitlement_update.user_entitlement


def add_user_entitlement(email_id, license_type, send_email_invite=None, organization=None, detect=None):
    """Add user.
    :param email_id: Email ID of the user.
    :type email_id: str
    :param license_type: License type for the user.
    :type license_type: str
    :rtype: UserEntitlementsPatchResponse
    """
    if send_email_invite is None:
        send_email_invite = True
    do_not_send_invite = not send_email_invite
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_access_level = AccessLevel()
    user_access_level.account_license_type = license_type
    graph_user = GraphUser()
    graph_user.subject_kind = 'user'
    graph_user.principal_name = email_id
    value = {}
    value['accessLevel'] = user_access_level
    value['extensions'] = []
    value['projectEntitlements'] = []
    value['user'] = graph_user
    patch_document = []
    patch_document.append(_create_patch_operation('add', '', value))
    user_entitlement = client.update_user_entitlements(document=patch_document,
                                                       do_not_send_invite_for_new_users=do_not_send_invite)
    if user_entitlement.have_results_succeeded is False and user_entitlement.results[0].errors[0] is not None:
        raise CLIError(user_entitlement.results[0].errors[0]['value'])
    return user_entitlement.results[0].result


def _create_patch_operation(op, path, value):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation
