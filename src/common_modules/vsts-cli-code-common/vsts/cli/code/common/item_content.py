# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model

class ItemContent(Model):

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'contentType': {'key': 'contentType', 'type': 'str'}
    }

    def __init__(self, content=None, contentType=None):
        super(ItemContent, self).__init__()
        self.content = content
        self.contentType = contentType
