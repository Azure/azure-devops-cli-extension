# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

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


def get_user_entitlements(top=None, skip=None, filter=None, select=None, organization=None, detect=None):
    """List users for the organization.
    :param int top: Maximum number of the users to return. Max value is 10000. Default value is 100
    :param str filter: Comma (",") separated list of properties and their values to filter on.
                        Currently, the API only supports filtering by ExtensionId.
                        An example parameter would be filter=extensionId eq search.
    :param select: Comma (",") separated list of properties to select in the result entitlements.
                    Names of the properties are - 'Projects, 'Extensions' and 'Grouprules'
    :param int skip: Offset: Number of records to skip.
    :rtype: [UserEntitlement]
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_member_entitlement_management_client(organization)
    user_entitlements = client.get_user_entitlements(top=top, skip=skip)
    return user_entitlements
