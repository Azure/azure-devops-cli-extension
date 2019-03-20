﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client


class FeedTokenClient(Client):
    """FeedToken
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(FeedTokenClient, self).__init__(base_url, creds)
        self._serialize = Serializer()
        self._deserialize = Deserializer()

    resource_area_identifier = 'cdeb6c7d-6b25-4d6f-b664-c2e3ede202e8'

    def get_personal_access_token(self, feed_name=None, token_type=None):
        """GetPersonalAccessToken.
        [Preview API] Get a time-limited session token representing the current user, with permissions scoped to the read/write of Artifacts.
        :param str feed_name:
        :param str token_type: Type of token to retrieve (e.g. 'SelfDescribing', 'Compact').
        :rtype: object
        """
        route_values = {}
        if feed_name is not None:
            route_values['feedName'] = self._serialize.url('feed_name', feed_name, 'str')
        query_parameters = {}
        if token_type is not None:
            query_parameters['tokenType'] = self._serialize.query('token_type', token_type, 'str')
        response = self._send(http_method='GET',
                              location_id='dfdb7ad7-3d8e-4907-911e-19b4a8330550',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

