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


class ProfileClient(Client):
    """Profile
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(ProfileClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8ccfef3d-2b87-4e99-8ccb-66e343d2daa8'

    def get_profile(self, id, details=None, with_attributes=None, partition=None, core_attributes=None, force_refresh=None):
        """GetProfile.
        [Preview API] Gets a user profile.
        :param str id: The ID of the target user profile within the same organization, or 'me' to get the profile of the current authenticated user.
        :param bool details: Return public profile information such as display name, email address, country, etc. If false, the withAttributes parameter is ignored.
        :param bool with_attributes: If true, gets the attributes (named key-value pairs of arbitrary data) associated with the profile. The partition parameter must also have a value.
        :param str partition: The partition (named group) of attributes to return.
        :param str core_attributes: A comma-delimited list of core profile attributes to return. Valid values are Email, Avatar, DisplayName, and ContactWithOffers.
        :param bool force_refresh: Not used in this version of the API.
        :rtype: :class:`<Profile> <azure.devops.v5_1.profile.models.Profile>`
        """
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if details is not None:
            query_parameters['details'] = self._serialize.query('details', details, 'bool')
        if with_attributes is not None:
            query_parameters['withAttributes'] = self._serialize.query('with_attributes', with_attributes, 'bool')
        if partition is not None:
            query_parameters['partition'] = self._serialize.query('partition', partition, 'str')
        if core_attributes is not None:
            query_parameters['coreAttributes'] = self._serialize.query('core_attributes', core_attributes, 'str')
        if force_refresh is not None:
            query_parameters['forceRefresh'] = self._serialize.query('force_refresh', force_refresh, 'bool')
        response = self._send(http_method='GET',
                              location_id='f83735dc-483f-4238-a291-d45f6080a9af',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Profile', response)

