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


class LocationClient(Client):
    """Location
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(LocationClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_connection_data(self, connect_options=None, last_change_id=None, last_change_id64=None):
        """GetConnectionData.
        [Preview API] This was copied and adapted from TeamFoundationConnectionService.Connect()
        :param str connect_options:
        :param int last_change_id: Obsolete 32-bit LastChangeId
        :param long last_change_id64: Non-truncated 64-bit LastChangeId
        :rtype: :class:`<ConnectionData> <azure.devops.v5_0.location.models.ConnectionData>`
        """
        query_parameters = {}
        if connect_options is not None:
            query_parameters['connectOptions'] = self._serialize.query('connect_options', connect_options, 'str')
        if last_change_id is not None:
            query_parameters['lastChangeId'] = self._serialize.query('last_change_id', last_change_id, 'int')
        if last_change_id64 is not None:
            query_parameters['lastChangeId64'] = self._serialize.query('last_change_id64', last_change_id64, 'long')
        response = self._send(http_method='GET',
                              location_id='00d9565f-ed9c-4a06-9a50-00e7896ccab4',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('ConnectionData', response)

    def get_resource_area(self, area_id, enterprise_name=None, organization_name=None):
        """GetResourceArea.
        [Preview API]
        :param str area_id:
        :param str enterprise_name:
        :param str organization_name:
        :rtype: :class:`<ResourceAreaInfo> <azure.devops.v5_0.location.models.ResourceAreaInfo>`
        """
        route_values = {}
        if area_id is not None:
            route_values['areaId'] = self._serialize.url('area_id', area_id, 'str')
        query_parameters = {}
        if enterprise_name is not None:
            query_parameters['enterpriseName'] = self._serialize.query('enterprise_name', enterprise_name, 'str')
        if organization_name is not None:
            query_parameters['organizationName'] = self._serialize.query('organization_name', organization_name, 'str')
        response = self._send(http_method='GET',
                              location_id='e81700f7-3be2-46de-8624-2eb35882fcaa',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ResourceAreaInfo', response)

    def get_resource_area_by_host(self, area_id, host_id):
        """GetResourceAreaByHost.
        [Preview API]
        :param str area_id:
        :param str host_id:
        :rtype: :class:`<ResourceAreaInfo> <azure.devops.v5_0.location.models.ResourceAreaInfo>`
        """
        route_values = {}
        if area_id is not None:
            route_values['areaId'] = self._serialize.url('area_id', area_id, 'str')
        query_parameters = {}
        if host_id is not None:
            query_parameters['hostId'] = self._serialize.query('host_id', host_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e81700f7-3be2-46de-8624-2eb35882fcaa',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ResourceAreaInfo', response)

    def get_resource_areas(self, enterprise_name=None, organization_name=None):
        """GetResourceAreas.
        [Preview API]
        :param str enterprise_name:
        :param str organization_name:
        :rtype: [ResourceAreaInfo]
        """
        query_parameters = {}
        if enterprise_name is not None:
            query_parameters['enterpriseName'] = self._serialize.query('enterprise_name', enterprise_name, 'str')
        if organization_name is not None:
            query_parameters['organizationName'] = self._serialize.query('organization_name', organization_name, 'str')
        response = self._send(http_method='GET',
                              location_id='e81700f7-3be2-46de-8624-2eb35882fcaa',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceAreaInfo]', self._unwrap_collection(response))

    def get_resource_areas_by_host(self, host_id):
        """GetResourceAreasByHost.
        [Preview API]
        :param str host_id:
        :rtype: [ResourceAreaInfo]
        """
        query_parameters = {}
        if host_id is not None:
            query_parameters['hostId'] = self._serialize.query('host_id', host_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e81700f7-3be2-46de-8624-2eb35882fcaa',
                              version='5.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceAreaInfo]', self._unwrap_collection(response))

    def delete_service_definition(self, service_type, identifier):
        """DeleteServiceDefinition.
        [Preview API]
        :param str service_type:
        :param str identifier:
        """
        route_values = {}
        if service_type is not None:
            route_values['serviceType'] = self._serialize.url('service_type', service_type, 'str')
        if identifier is not None:
            route_values['identifier'] = self._serialize.url('identifier', identifier, 'str')
        self._send(http_method='DELETE',
                   location_id='d810a47d-f4f4-4a62-a03f-fa1860585c4c',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_service_definition(self, service_type, identifier, allow_fault_in=None, preview_fault_in=None):
        """GetServiceDefinition.
        [Preview API] Finds a given service definition.
        :param str service_type:
        :param str identifier:
        :param bool allow_fault_in: If true, we will attempt to fault in a host instance mapping if in SPS.
        :param bool preview_fault_in: If true, we will calculate and return a host instance mapping, but not persist it.
        :rtype: :class:`<ServiceDefinition> <azure.devops.v5_0.location.models.ServiceDefinition>`
        """
        route_values = {}
        if service_type is not None:
            route_values['serviceType'] = self._serialize.url('service_type', service_type, 'str')
        if identifier is not None:
            route_values['identifier'] = self._serialize.url('identifier', identifier, 'str')
        query_parameters = {}
        if allow_fault_in is not None:
            query_parameters['allowFaultIn'] = self._serialize.query('allow_fault_in', allow_fault_in, 'bool')
        if preview_fault_in is not None:
            query_parameters['previewFaultIn'] = self._serialize.query('preview_fault_in', preview_fault_in, 'bool')
        response = self._send(http_method='GET',
                              location_id='d810a47d-f4f4-4a62-a03f-fa1860585c4c',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ServiceDefinition', response)

    def get_service_definitions(self, service_type=None):
        """GetServiceDefinitions.
        [Preview API]
        :param str service_type:
        :rtype: [ServiceDefinition]
        """
        route_values = {}
        if service_type is not None:
            route_values['serviceType'] = self._serialize.url('service_type', service_type, 'str')
        response = self._send(http_method='GET',
                              location_id='d810a47d-f4f4-4a62-a03f-fa1860585c4c',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[ServiceDefinition]', self._unwrap_collection(response))

    def update_service_definitions(self, service_definitions):
        """UpdateServiceDefinitions.
        [Preview API]
        :param :class:`<VssJsonCollectionWrapper> <azure.devops.v5_0.location.models.VssJsonCollectionWrapper>` service_definitions:
        """
        content = self._serialize.body(service_definitions, 'VssJsonCollectionWrapper')
        self._send(http_method='PATCH',
                   location_id='d810a47d-f4f4-4a62-a03f-fa1860585c4c',
                   version='5.0-preview.1',
                   content=content)

