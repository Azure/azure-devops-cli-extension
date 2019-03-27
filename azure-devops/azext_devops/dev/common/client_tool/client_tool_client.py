# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from azext_devops.devops_sdk.client import Client

from . import models


class ClientToolClient(Client):
    def __init__(self, base_url=None, creds=None):
        super(ClientToolClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '3fda18ba-dff2-42e6-8d10-c521b23b85fc'

    def get_clienttool_release(
            self,
            tool_name,
            os_name=None,
            arch=None,
            distro_name=None,
            distro_version=None,
            version=None):

        route_values = {}
        if tool_name is not None:
            route_values['toolName'] = self._serialize.url('tool_name', tool_name, 'str')
        query_parameters = {}
        if os_name is not None:
            query_parameters['osName'] = self._serialize.query('os_name', os_name, 'str')
        if arch is not None:
            query_parameters['arch'] = self._serialize.query('arch', arch, 'str')
        if distro_name is not None:
            query_parameters['distroName'] = self._serialize.query('distro_name', distro_name, 'str')
        if distro_version is not None:
            query_parameters['distroVersion'] = self._serialize.query('distro_version', distro_version, 'str')
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='187ec90d-dd1e-4ec6-8c57-937d979261e5',
                              version='5.0-preview',
                              route_values=route_values,
                              query_parameters=query_parameters)

        return self._deserialize('ClientToolRelease', response)
