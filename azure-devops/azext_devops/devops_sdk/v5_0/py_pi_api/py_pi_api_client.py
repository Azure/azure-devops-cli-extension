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


class PyPiApiClient(Client):
    """PyPiApi
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(PyPiApiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '92f0314b-06c5-46e0-abe7-15fd9d13276a'

    def download_package(self, feed_id, package_name, package_version, file_name):
        """DownloadPackage.
        [Preview API] Download a python package file directly. This API is intended for manual UI download options, not for programmatic access and scripting.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str file_name: Name of the file in the package
        :rtype: object
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='97218bae-a64d-4381-9257-b5b7951f0b98',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('object', response)

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version):
        """DeletePackageVersionFromRecycleBin.
        [Preview API] Delete a package version from the feed, moving it to the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        self._send(http_method='DELETE',
                   location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API] Get information about a package version in the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :rtype: :class:`<PyPiPackageVersionDeletionState> <azure.devops.v5_0.py_pi_api.models.PyPiPackageVersionDeletionState>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('PyPiPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version):
        """RestorePackageVersionFromRecycleBin.
        [Preview API] Restore a package version from the recycle bin to its associated feed.
        :param :class:`<PyPiRecycleBinPackageVersionDetails> <azure.devops.v5_0.py_pi_api.models.PyPiRecycleBinPackageVersionDetails>` package_version_details: Set the 'Deleted' state to 'false' to restore the package to its feed.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PyPiRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version):
        """DeletePackageVersion.
        [Preview API] Delete a package version, moving it to the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :rtype: :class:`<Package> <azure.devops.v5_0.py_pi_api.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='DELETE',
                              location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, show_deleted=None):
        """GetPackageVersion.
        [Preview API] Get information about a package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param bool show_deleted: True to show information for deleted package versions.
        :rtype: :class:`<Package> <azure.devops.v5_0.py_pi_api.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version):
        """UpdatePackageVersion.
        [Preview API] Update state for a package version.
        :param :class:`<PackageVersionDetails> <azure.devops.v5_0.py_pi_api.models.PackageVersionDetails>` package_version_details: Details to be updated.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

