# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model

class ClientToolRelease(Model):
    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'rid': {'key': 'rid', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, name=None, rid=None, version=None, uri=None):
        super(ClientToolRelease, self).__init__()
        self.name = name
        self.rid = rid
        self.version = version
        self.uri = uri
        