# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class BoardsClient(Client):
    """Boards
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(BoardsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '11635d5f-a4f9-43ea-a48b-d56be43fee0f'

