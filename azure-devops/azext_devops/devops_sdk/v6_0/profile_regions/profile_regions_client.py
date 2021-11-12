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


class ProfileRegionsClient(Client):
    """ProfileRegions
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(ProfileRegionsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8ccfef3d-2b87-4e99-8ccb-66e343d2daa8'

    def get_geo_region(self, ip):
        """GetGeoRegion.
        [Preview API] Lookup up country/region based on provided IPv4, null if using the remote IPv4 address.
        :param str ip:
        :rtype: :class:`<GeoRegion> <azure.devops.v6_0.profile_regions.models.GeoRegion>`
        """
        query_parameters = {}
        if ip is not None:
            query_parameters['ip'] = self._serialize.query('ip', ip, 'str')
        response = self._send(http_method='GET',
                              location_id='35b3ff1d-ab4c-4d1c-98bb-f6ea21d86bd9',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('GeoRegion', response)

    def get_regions(self):
        """GetRegions.
        [Preview API]
        :rtype: :class:`<ProfileRegions> <azure.devops.v6_0.profile_regions.models.ProfileRegions>`
        """
        response = self._send(http_method='GET',
                              location_id='b129ca90-999d-47bb-ab37-0dcf784ee633',
                              version='6.0-preview.1')
        return self._deserialize('ProfileRegions', response)

