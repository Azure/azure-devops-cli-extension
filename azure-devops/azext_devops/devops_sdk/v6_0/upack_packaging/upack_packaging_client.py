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


class UPackPackagingClient(Client):
    """UPackPackaging
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(UPackPackagingClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'd397749b-f115-4027-b6dd-77a65dd10d21'

    def add_package(self, metadata, feed_id, package_name, package_version, project=None):
        """AddPackage.
        [Preview API]
        :param :class:`<UPackPackagePushMetadata> <azure.devops.v6_0.upack_packaging.models.UPackPackagePushMetadata>` metadata:
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(metadata, 'UPackPackagePushMetadata')
        self._send(http_method='PUT',
                   location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_package_metadata(self, feed_id, package_name, package_version, project=None, intent=None):
        """GetPackageMetadata.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :param str project: Project ID or project name
        :param str intent:
        :rtype: :class:`<UPackPackageMetadata> <azure.devops.v6_0.upack_packaging.models.UPackPackageMetadata>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if intent is not None:
            query_parameters['intent'] = self._serialize.query('intent', intent, 'str')
        response = self._send(http_method='GET',
                              location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('UPackPackageMetadata', response)

    def get_package_versions_metadata(self, feed_id, package_name, project=None):
        """GetPackageVersionsMetadata.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str project: Project ID or project name
        :rtype: :class:`<UPackLimitedPackageMetadataListResponse> <azure.devops.v6_0.upack_packaging.models.UPackLimitedPackageMetadataListResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='4cdb2ced-0758-4651-8032-010f070dd7e5',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UPackLimitedPackageMetadataListResponse', response)

