# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model


class PermissionDetails(Model):
    """PermissionDetails.

    :param bit: Permission bit
    :type bit: int
    :param display_ame: Display string for permission
    :type display_ame: str
    :param effective_permission: Effective permission value, Allow, Deny, Not set.
    :type effective_permission:str
    :param name: Name of permission as found in namespace details.
    :type name:str
    """

    _attribute_map = {
        'bit': {'key': 'bit', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'effective_permission': {'key': 'effectivePermission', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, bit=None, display_name=None, effective_permission=None, name=None):
        super(PermissionDetails, self).__init__()
        self.bit = bit
        self.display_name = display_name
        self.effective_permission = effective_permission
        self.name = name
