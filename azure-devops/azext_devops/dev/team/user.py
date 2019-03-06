# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pdb
from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.member_entitlement_management.v4_1.models.models import (UserEntitlement,
                                                                                          AccessLevel,
                                                                                          Extension,
                                                                                          GroupEntitlement,
                                                                                          GraphUser,
                                                                                          JsonPatchOperation)
from azext_devops.dev.common.services import (get_member_entitlement_management_client,
                                              resolve_instance)
from azext_devops.dev.common.identities import resolve_identity_as_id


def get_user_entitlements(top=None, skip=None, organization=None, detect=None):
    """List users for the organization.
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
    :param id: The Email id or UUID of the user.
    :type id: str
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
    :param id: The Email id or UUID of the user.
    :type id: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    if '@' in user:
        user = resolve_identity_as_id(user, organization)
    client = get_member_entitlement_management_client(organization)
    delete_user_entitlement_details = client.delete_user_entitlement(user_id=user)
    return delete_user_entitlement_details
