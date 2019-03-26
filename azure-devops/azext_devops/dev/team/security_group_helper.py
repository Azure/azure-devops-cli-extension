# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azext_devops.vstsCompressed.graph.v4_1.models.models import (GraphGroupCreationContext)

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
        super(GraphGroupCreationContext, self).__init__()
        self.display_name = display_name
        self.description = description
