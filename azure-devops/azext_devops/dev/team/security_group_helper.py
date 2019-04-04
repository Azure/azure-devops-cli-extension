# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azext_devops.devops_sdk.v5_0.graph.models import (GraphGroupCreationContext)


class GraphGroupVstsCreationContext(GraphGroupCreationContext):
    """GraphGroupVstsCreationContext.

    :param displayName: Name of the group.
    :type displayName: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, display_name, description=None):
        super(GraphGroupVstsCreationContext, self).__init__()
        self.display_name = display_name
        self.description = description


class GraphGroupMailAddressCreationContext(GraphGroupCreationContext):
    """GraphGroupMailAddressCreationContext.

    :param mailAddress: This should be the mail address or the group in the source AD or AAD provider.
    :type mailAddress: str
    """

    _attribute_map = {
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
    }

    def __init__(self, mail_address):
        super(GraphGroupMailAddressCreationContext, self).__init__()
        self.mail_address = mail_address


class GraphGroupOriginIdCreationContext(GraphGroupCreationContext):
    """GraphGroupOriginIdCreationContext.

    :param originId: This should be the object id or sid of the group from the source AD or AAD provider.
    :type originId: str
    """

    _attribute_map = {
        'origin_id': {'key': 'originId', 'type': 'str'},
    }

    def __init__(self, origin_id):
        super(GraphGroupOriginIdCreationContext, self).__init__()
        self.origin_id = origin_id
