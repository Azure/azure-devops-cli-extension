# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging

from msrest.service_client import ServiceClient
from ._file_cache import RESOURCE_CACHE as RESOURCE_FILE_CACHE
from .client_configuration import ClientConfiguration
from .exceptions import AzureDevOpsClientRequestError
from .released.client_factory import ClientFactory
from .v5_0.location.location_client import LocationClient
from .v5_0.client_factory import ClientFactoryV5_0
from .v5_1.client_factory import ClientFactoryV5_1

logger = logging.getLogger(__name__)


class Connection(object):
    """Connection.
    """

    def __init__(self, base_url=None, creds=None, user_agent=None):
        self._config = ClientConfiguration(base_url)
        self._config.credentials = creds
        self._addition_user_agent = user_agent
        if user_agent is not None:
            self._config.add_user_agent(user_agent)
        self._client = ServiceClient(creds, self._config)
        self._client_cache = {}
        self.base_url = base_url
        self._creds = creds
        self._resource_areas = None
        self.clients = ClientFactory(self)
        self.clients_v5_0 = ClientFactoryV5_0(self)
        self.clients_v5_1 = ClientFactoryV5_1(self)
        self.use_fiddler = False

    def get_client(self, client_type):
        """get_client.
        """
        if client_type not in self._client_cache:
            client_class = self._get_class(client_type)
            self._client_cache[client_type] = self._get_client_instance(client_class)
        return self._client_cache[client_type]

    @staticmethod
    def _get_class(full_class_name):
        parts = full_class_name.split('.')
        module_name = ".".join(parts[:-1])
        imported = __import__(module_name)
        for comp in parts[1:]:
            imported = getattr(imported, comp)
        return imported

    def _get_client_instance(self, client_class):
        url = self._get_url_for_client_instance(client_class)
        client = client_class(url, self._creds)
        client.add_user_agent(self._addition_user_agent)
        if self.use_fiddler:
            self._configure_client_for_fiddler(client)
        return client

    def _get_url_for_client_instance(self, client_class):
        resource_id = client_class.resource_area_identifier
        if resource_id is None:
            return self.base_url
        else:
            resource_areas = self._get_resource_areas()
            if resource_areas is None:
                raise AzureDevOpsClientRequestError(('Failed to retrieve resource areas '
                                                     + 'from server: {url}').format(url=self.base_url))
            if not resource_areas:
                # For OnPrem environments we get an empty list.
                return self.base_url
            for resource_area in resource_areas:
                if resource_area.id.lower() == resource_id.lower():
                    return resource_area.location_url

            # Check SPS deployment level for the resource area
            resource_area = self._get_deployment_resource_area_from_sps(resource_id)
            if resource_area is not None:
                return resource_area.location_url

            raise AzureDevOpsClientRequestError(('Could not find information for resource area {id} '
                                                 + 'from server: {url}').format(id=resource_id,
                                                                                url=self.base_url))

    def _get_deployment_resource_area_from_sps(self, resource_id):
        resource_id = resource_id.lower()
        if resource_id in _deployment_level_resource_areas:
            return _deployment_level_resource_areas[resource_id]
        location_client = LocationClient(sps_url, self._creds)
        if self.use_fiddler:
            self._configure_client_for_fiddler(location_client)
        resource_area = location_client.get_resource_area(area_id=resource_id)
        _deployment_level_resource_areas[resource_id] = resource_area
        return resource_area

    def authenticate(self):
        self._get_resource_areas(force=True)

    def _get_resource_areas(self, force=False):
        if self._resource_areas is None or force:
            location_client = LocationClient(self.base_url, self._creds)
            if self.use_fiddler:
                self._configure_client_for_fiddler(location_client)
            if not force and RESOURCE_FILE_CACHE[location_client.normalized_url]:
                try:
                    logger.debug('File cache hit for resources on: %s', location_client.normalized_url)
                    self._resource_areas = location_client._base_deserialize.deserialize_data(RESOURCE_FILE_CACHE[location_client.normalized_url],
                                                                                              '[ResourceAreaInfo]')
                    return self._resource_areas
                except Exception as ex:
                    logger.debug(ex, exc_info=True)
            elif not force:
                logger.debug('File cache miss for resources on: %s', location_client.normalized_url)
            self._resource_areas = location_client.get_resource_areas()
            if self._resource_areas is None:
                # For OnPrem environments we get an empty collection wrapper.
                self._resource_areas = []
            try:
                serialized = location_client._base_serialize.serialize_data(self._resource_areas,
                                                                            '[ResourceAreaInfo]')
                RESOURCE_FILE_CACHE[location_client.normalized_url] = serialized
            except Exception as ex:
                logger.debug(ex, exc_info=True)
        return self._resource_areas

    @staticmethod
    def _combine_url(part1, part2):
        return part1.rstrip('/') + '/' + part2.strip('/')

    @staticmethod
    def _configure_client_for_fiddler(client):
        client.config.connection.verify = False
        client.config.proxies.add(protocol='https', proxy_url='https://127.0.0.1:8888')


_deployment_level_resource_areas = {}
sps_url = 'https://app.vssps.visualstudio.com'
