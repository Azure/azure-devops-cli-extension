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


class FeedClient(Client):
    """Feed
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(FeedClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '7ab4e64e-c4d8-4f50-ae73-5ef2e21642a5'

    def get_badge(self, feed_id, package_id, project=None):
        """GetBadge.
        [Preview API] Generate a SVG badge for the latest version of a package.  The generated SVG is typically used as the image in an HTML link which takes users to the feed containing the package to accelerate discovery and consumption.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: Id of the package (GUID Id, not name).
        :param str project: Project ID or project name
        :rtype: str
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        response = self._send(http_method='GET',
                              location_id='61d885fd-10f3-4a55-82b6-476d866b673f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def get_feed_change(self, feed_id, project=None):
        """GetFeedChange.
        [Preview API] Query a feed to determine its current state.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedChange> <azure.devops.v5_1.feed.models.FeedChange>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='29ba2dad-389a-4661-b5d3-de76397ca05b',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedChange', response)

    def get_feed_changes(self, project=None, include_deleted=None, continuation_token=None, batch_size=None):
        """GetFeedChanges.
        [Preview API] Query to determine which feeds have changed since the last call, tracked through the provided continuationToken. Only changes to a feed itself are returned and impact the continuationToken, not additions or alterations to packages within the feeds.
        :param str project: Project ID or project name
        :param bool include_deleted: If true, get changes for all feeds including deleted feeds. The default value is false.
        :param long continuation_token: A continuation token which acts as a bookmark to a previously retrieved change. This token allows the user to continue retrieving changes in batches, picking up where the previous batch left off. If specified, all the changes that occur strictly after the token will be returned. If not specified or 0, iteration will start with the first change.
        :param int batch_size: Number of package changes to fetch. The default value is 1000. The maximum value is 2000.
        :rtype: :class:`<FeedChangesResponse> <azure.devops.v5_1.feed.models.FeedChangesResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'long')
        if batch_size is not None:
            query_parameters['batchSize'] = self._serialize.query('batch_size', batch_size, 'int')
        response = self._send(http_method='GET',
                              location_id='29ba2dad-389a-4661-b5d3-de76397ca05b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('FeedChangesResponse', response)

    def create_feed(self, feed, project=None):
        """CreateFeed.
        [Preview API] Create a feed, a container for various package types.
        :param :class:`<Feed> <azure.devops.v5_1.feed.models.Feed>` feed: A JSON object containing both required and optional attributes for the feed. Name is the only required value.
        :param str project: Project ID or project name
        :rtype: :class:`<Feed> <azure.devops.v5_1.feed.models.Feed>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(feed, 'Feed')
        response = self._send(http_method='POST',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Feed', response)

    def delete_feed(self, feed_id, project=None):
        """DeleteFeed.
        [Preview API] Remove a feed and all its packages. The action does not result in packages moving to the RecycleBin and is not reversible.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        self._send(http_method='DELETE',
                   location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed(self, feed_id, project=None, include_deleted_upstreams=None):
        """GetFeed.
        [Preview API] Get the settings for a specific feed.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :param bool include_deleted_upstreams: Include upstreams that have been deleted in the response.
        :rtype: :class:`<Feed> <azure.devops.v5_1.feed.models.Feed>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if include_deleted_upstreams is not None:
            query_parameters['includeDeletedUpstreams'] = self._serialize.query('include_deleted_upstreams', include_deleted_upstreams, 'bool')
        response = self._send(http_method='GET',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Feed', response)

    def get_feeds(self, project=None, feed_role=None, include_deleted_upstreams=None):
        """GetFeeds.
        [Preview API] Get all feeds in an account where you have the provided role access.
        :param str project: Project ID or project name
        :param str feed_role: Filter by this role, either Administrator(4), Contributor(3), or Reader(2) level permissions.
        :param bool include_deleted_upstreams: Include upstreams that have been deleted in the response.
        :rtype: [Feed]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if feed_role is not None:
            query_parameters['feedRole'] = self._serialize.query('feed_role', feed_role, 'str')
        if include_deleted_upstreams is not None:
            query_parameters['includeDeletedUpstreams'] = self._serialize.query('include_deleted_upstreams', include_deleted_upstreams, 'bool')
        response = self._send(http_method='GET',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Feed]', self._unwrap_collection(response))

    def update_feed(self, feed, feed_id, project=None):
        """UpdateFeed.
        [Preview API] Change the attributes of a feed.
        :param :class:`<FeedUpdate> <azure.devops.v5_1.feed.models.FeedUpdate>` feed: A JSON object containing the feed settings to be updated.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :rtype: :class:`<Feed> <azure.devops.v5_1.feed.models.Feed>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(feed, 'FeedUpdate')
        response = self._send(http_method='PATCH',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Feed', response)

    def get_global_permissions(self):
        """GetGlobalPermissions.
        [Preview API] Get all service-wide feed creation and administration permissions.
        :rtype: [GlobalPermission]
        """
        response = self._send(http_method='GET',
                              location_id='a74419ef-b477-43df-8758-3cd1cd5f56c6',
                              version='5.1-preview.1')
        return self._deserialize('[GlobalPermission]', self._unwrap_collection(response))

    def set_global_permissions(self, global_permissions):
        """SetGlobalPermissions.
        [Preview API] Set service-wide permissions that govern feed creation and administration.
        :param [GlobalPermission] global_permissions: New permissions for the organization.
        :rtype: [GlobalPermission]
        """
        content = self._serialize.body(global_permissions, '[GlobalPermission]')
        response = self._send(http_method='PATCH',
                              location_id='a74419ef-b477-43df-8758-3cd1cd5f56c6',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('[GlobalPermission]', self._unwrap_collection(response))

    def get_package_changes(self, feed_id, project=None, continuation_token=None, batch_size=None):
        """GetPackageChanges.
        [Preview API] Get a batch of package changes made to a feed.  The changes returned are 'most recent change' so if an Add is followed by an Update before you begin enumerating, you'll only see one change in the batch.  While consuming batches using the continuation token, you may see changes to the same package version multiple times if they are happening as you enumerate.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :param long continuation_token: A continuation token which acts as a bookmark to a previously retrieved change. This token allows the user to continue retrieving changes in batches, picking up where the previous batch left off. If specified, all the changes that occur strictly after the token will be returned. If not specified or 0, iteration will start with the first change.
        :param int batch_size: Number of package changes to fetch. The default value is 1000. The maximum value is 2000.
        :rtype: :class:`<PackageChangesResponse> <azure.devops.v5_1.feed.models.PackageChangesResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'long')
        if batch_size is not None:
            query_parameters['batchSize'] = self._serialize.query('batch_size', batch_size, 'int')
        response = self._send(http_method='GET',
                              location_id='323a0631-d083-4005-85ae-035114dfb681',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PackageChangesResponse', response)

    def query_package_metrics(self, package_id_query, feed_id, project=None):
        """QueryPackageMetrics.
        [Preview API]
        :param :class:`<PackageMetricsQuery> <azure.devops.v5_1.feed.models.PackageMetricsQuery>` package_id_query:
        :param str feed_id:
        :param str project: Project ID or project name
        :rtype: [PackageMetrics]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(package_id_query, 'PackageMetricsQuery')
        response = self._send(http_method='POST',
                              location_id='bddc9b3c-8a59-4a9f-9b40-ee1dcaa2cc0d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[PackageMetrics]', self._unwrap_collection(response))

    def get_package(self, feed_id, package_id, project=None, include_all_versions=None, include_urls=None, is_listed=None, is_release=None, include_deleted=None, include_description=None):
        """GetPackage.
        [Preview API] Get details about a specific package.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: The package Id (GUID Id, not the package name).
        :param str project: Project ID or project name
        :param bool include_all_versions: True to return all versions of the package in the response. Default is false (latest version only).
        :param bool include_urls: True to return REST Urls with the response. Default is True.
        :param bool is_listed: Only applicable for NuGet packages, setting it for other package types will result in a 404. If false, delisted package versions will be returned. Use this to filter the response when includeAllVersions is set to true. Default is unset (do not return delisted packages).
        :param bool is_release: Only applicable for Nuget packages. Use this to filter the response when includeAllVersions is set to true.  Default is True (only return packages without prerelease versioning).
        :param bool include_deleted: Return deleted or unpublished versions of packages in the response. Default is False.
        :param bool include_description: Return the description for every version of each package in the response. Default is False.
        :rtype: :class:`<Package> <azure.devops.v5_1.feed.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_release is not None:
            query_parameters['isRelease'] = self._serialize.query('is_release', is_release, 'bool')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_description is not None:
            query_parameters['includeDescription'] = self._serialize.query('include_description', include_description, 'bool')
        response = self._send(http_method='GET',
                              location_id='7a20d846-c929-4acc-9ea2-0d5a7df1b197',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def get_packages(self, feed_id, project=None, protocol_type=None, package_name_query=None, normalized_package_name=None, include_urls=None, include_all_versions=None, is_listed=None, get_top_package_versions=None, is_release=None, include_description=None, top=None, skip=None, include_deleted=None, is_cached=None, direct_upstream_id=None):
        """GetPackages.
        [Preview API] Get details about all of the packages in the feed. Use the various filters to include or exclude information from the result set.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :param str protocol_type: One of the supported artifact package types.
        :param str package_name_query: Filter to packages that contain the provided string. Characters in the string must conform to the package name constraints.
        :param str normalized_package_name: [Obsolete] Used for legacy scenarios and may be removed in future versions.
        :param bool include_urls: True to return REST Urls with the response. Default is True.
        :param bool include_all_versions: True to return all versions of the package in the response. Default is false (latest version only).
        :param bool is_listed: Only applicable for NuGet packages, setting it for other package types will result in a 404. If false, delisted package versions will be returned. Use this to filter the response when includeAllVersions is set to true. Default is unset (do not return delisted packages).
        :param bool get_top_package_versions: Changes the behavior of $top and $skip to return all versions of each package up to $top. Must be used in conjunction with includeAllVersions=true
        :param bool is_release: Only applicable for Nuget packages. Use this to filter the response when includeAllVersions is set to true. Default is True (only return packages without prerelease versioning).
        :param bool include_description: Return the description for every version of each package in the response. Default is False.
        :param int top: Get the top N packages (or package versions where getTopPackageVersions=true)
        :param int skip: Skip the first N packages (or package versions where getTopPackageVersions=true)
        :param bool include_deleted: Return deleted or unpublished versions of packages in the response. Default is False.
        :param bool is_cached: [Obsolete] Used for legacy scenarios and may be removed in future versions.
        :param str direct_upstream_id: Filter results to return packages from a specific upstream.
        :rtype: [Package]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if protocol_type is not None:
            query_parameters['protocolType'] = self._serialize.query('protocol_type', protocol_type, 'str')
        if package_name_query is not None:
            query_parameters['packageNameQuery'] = self._serialize.query('package_name_query', package_name_query, 'str')
        if normalized_package_name is not None:
            query_parameters['normalizedPackageName'] = self._serialize.query('normalized_package_name', normalized_package_name, 'str')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if get_top_package_versions is not None:
            query_parameters['getTopPackageVersions'] = self._serialize.query('get_top_package_versions', get_top_package_versions, 'bool')
        if is_release is not None:
            query_parameters['isRelease'] = self._serialize.query('is_release', is_release, 'bool')
        if include_description is not None:
            query_parameters['includeDescription'] = self._serialize.query('include_description', include_description, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if is_cached is not None:
            query_parameters['isCached'] = self._serialize.query('is_cached', is_cached, 'bool')
        if direct_upstream_id is not None:
            query_parameters['directUpstreamId'] = self._serialize.query('direct_upstream_id', direct_upstream_id, 'str')
        response = self._send(http_method='GET',
                              location_id='7a20d846-c929-4acc-9ea2-0d5a7df1b197',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Package]', self._unwrap_collection(response))

    def get_feed_permissions(self, feed_id, project=None, include_ids=None, exclude_inherited_permissions=None, identity_descriptor=None):
        """GetFeedPermissions.
        [Preview API] Get the permissions for a feed.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :param bool include_ids: True to include user Ids in the response.  Default is false.
        :param bool exclude_inherited_permissions: True to only return explicitly set permissions on the feed.  Default is false.
        :param str identity_descriptor: Filter permissions to the provided identity.
        :rtype: [FeedPermission]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if include_ids is not None:
            query_parameters['includeIds'] = self._serialize.query('include_ids', include_ids, 'bool')
        if exclude_inherited_permissions is not None:
            query_parameters['excludeInheritedPermissions'] = self._serialize.query('exclude_inherited_permissions', exclude_inherited_permissions, 'bool')
        if identity_descriptor is not None:
            query_parameters['identityDescriptor'] = self._serialize.query('identity_descriptor', identity_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='be8c1476-86a7-44ed-b19d-aec0e9275cd8',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[FeedPermission]', self._unwrap_collection(response))

    def set_feed_permissions(self, feed_permission, feed_id, project=None):
        """SetFeedPermissions.
        [Preview API] Update the permissions on a feed.
        :param [FeedPermission] feed_permission: Permissions to set.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :rtype: [FeedPermission]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(feed_permission, '[FeedPermission]')
        response = self._send(http_method='PATCH',
                              location_id='be8c1476-86a7-44ed-b19d-aec0e9275cd8',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[FeedPermission]', self._unwrap_collection(response))

    def get_package_version_provenance(self, feed_id, package_id, package_version_id, project=None):
        """GetPackageVersionProvenance.
        [Preview API] Gets provenance for a package version.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: Id of the package (GUID Id, not name).
        :param str package_version_id: Id of the package version (GUID Id, not name).
        :param str project: Project ID or project name
        :rtype: :class:`<PackageVersionProvenance> <azure.devops.v5_1.feed.models.PackageVersionProvenance>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        response = self._send(http_method='GET',
                              location_id='0aaeabd4-85cd-4686-8a77-8d31c15690b8',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PackageVersionProvenance', response)

    def get_recycle_bin_package(self, feed_id, package_id, project=None, include_urls=None):
        """GetRecycleBinPackage.
        [Preview API] Get information about a package and all its versions within the recycle bin.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: The package Id (GUID Id, not the package name).
        :param str project: Project ID or project name
        :param bool include_urls: True to return REST Urls with the response.  Default is True.
        :rtype: :class:`<Package> <azure.devops.v5_1.feed.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='2704e72c-f541-4141-99be-2004b50b05fa',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def get_recycle_bin_packages(self, feed_id, project=None, protocol_type=None, package_name_query=None, include_urls=None, top=None, skip=None, include_all_versions=None):
        """GetRecycleBinPackages.
        [Preview API] Query for packages within the recycle bin.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :param str protocol_type: Type of package (e.g. NuGet, npm, ...).
        :param str package_name_query: Filter to packages matching this name.
        :param bool include_urls: True to return REST Urls with the response.  Default is True.
        :param int top: Get the top N packages.
        :param int skip: Skip the first N packages.
        :param bool include_all_versions: True to return all versions of the package in the response.  Default is false (latest version only).
        :rtype: [Package]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if protocol_type is not None:
            query_parameters['protocolType'] = self._serialize.query('protocol_type', protocol_type, 'str')
        if package_name_query is not None:
            query_parameters['packageNameQuery'] = self._serialize.query('package_name_query', package_name_query, 'str')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        response = self._send(http_method='GET',
                              location_id='2704e72c-f541-4141-99be-2004b50b05fa',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Package]', self._unwrap_collection(response))

    def get_recycle_bin_package_version(self, feed_id, package_id, package_version_id, project=None, include_urls=None):
        """GetRecycleBinPackageVersion.
        [Preview API] Get information about a package version within the recycle bin.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: The package Id (GUID Id, not the package name).
        :param str package_version_id: The package version Id 9guid Id, not the version string).
        :param str project: Project ID or project name
        :param bool include_urls: True to return REST Urls with the response.  Default is True.
        :rtype: :class:`<RecycleBinPackageVersion> <azure.devops.v5_1.feed.models.RecycleBinPackageVersion>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='aceb4be7-8737-4820-834c-4c549e10fdc7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('RecycleBinPackageVersion', response)

    def get_recycle_bin_package_versions(self, feed_id, package_id, project=None, include_urls=None):
        """GetRecycleBinPackageVersions.
        [Preview API] Get a list of package versions within the recycle bin.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: The package Id (GUID Id, not the package name).
        :param str project: Project ID or project name
        :param bool include_urls: True to return REST Urls with the response.  Default is True.
        :rtype: [RecycleBinPackageVersion]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='aceb4be7-8737-4820-834c-4c549e10fdc7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RecycleBinPackageVersion]', self._unwrap_collection(response))

    def delete_feed_retention_policies(self, feed_id, project=None):
        """DeleteFeedRetentionPolicies.
        [Preview API] Delete the retention policy for a feed.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        self._send(http_method='DELETE',
                   location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed_retention_policies(self, feed_id, project=None):
        """GetFeedRetentionPolicies.
        [Preview API] Get the retention policy for a feed.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedRetentionPolicy> <azure.devops.v5_1.feed.models.FeedRetentionPolicy>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedRetentionPolicy', response)

    def set_feed_retention_policies(self, policy, feed_id, project=None):
        """SetFeedRetentionPolicies.
        [Preview API] Set the retention policy for a feed.
        :param :class:`<FeedRetentionPolicy> <azure.devops.v5_1.feed.models.FeedRetentionPolicy>` policy: Feed retention policy.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedRetentionPolicy> <azure.devops.v5_1.feed.models.FeedRetentionPolicy>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(policy, 'FeedRetentionPolicy')
        response = self._send(http_method='PUT',
                              location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedRetentionPolicy', response)

    def query_package_version_metrics(self, package_version_id_query, feed_id, package_id, project=None):
        """QueryPackageVersionMetrics.
        [Preview API]
        :param :class:`<PackageVersionMetricsQuery> <azure.devops.v5_1.feed.models.PackageVersionMetricsQuery>` package_version_id_query:
        :param str feed_id:
        :param str package_id:
        :param str project: Project ID or project name
        :rtype: [PackageVersionMetrics]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        content = self._serialize.body(package_version_id_query, 'PackageVersionMetricsQuery')
        response = self._send(http_method='POST',
                              location_id='e6ae8caa-b6a8-4809-b840-91b2a42c19ad',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[PackageVersionMetrics]', self._unwrap_collection(response))

    def get_package_version(self, feed_id, package_id, package_version_id, project=None, include_urls=None, is_listed=None, is_deleted=None):
        """GetPackageVersion.
        [Preview API] Get details about a specific package version.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: Id of the package (GUID Id, not name).
        :param str package_version_id: Id of the package version (GUID Id, not name).
        :param str project: Project ID or project name
        :param bool include_urls: True to include urls for each version. Default is true.
        :param bool is_listed: Only applicable for NuGet packages. If false, delisted package versions will be returned.
        :param bool is_deleted: This does not have any effect on the requested package version, for other versions returned specifies whether to return only deleted or non-deleted versions of packages in the response. Default is unset (return all versions).
        :rtype: :class:`<PackageVersion> <azure.devops.v5_1.feed.models.PackageVersion>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='3b331909-6a86-44cc-b9ec-c1834c35498f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PackageVersion', response)

    def get_package_versions(self, feed_id, package_id, project=None, include_urls=None, is_listed=None, is_deleted=None):
        """GetPackageVersions.
        [Preview API] Get a list of package versions, optionally filtering by state.
        :param str feed_id: Name or Id of the feed.
        :param str package_id: Id of the package (GUID Id, not name).
        :param str project: Project ID or project name
        :param bool include_urls: True to include urls for each version. Default is true.
        :param bool is_listed: Only applicable for NuGet packages. If false, delisted package versions will be returned.
        :param bool is_deleted: If set specifies whether to return only deleted or non-deleted versions of packages in the response. Default is unset (return all versions).
        :rtype: [PackageVersion]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='3b331909-6a86-44cc-b9ec-c1834c35498f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[PackageVersion]', self._unwrap_collection(response))

    def create_feed_view(self, view, feed_id, project=None):
        """CreateFeedView.
        [Preview API] Create a new view on the referenced feed.
        :param :class:`<FeedView> <azure.devops.v5_1.feed.models.FeedView>` view: View to be created.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedView> <azure.devops.v5_1.feed.models.FeedView>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(view, 'FeedView')
        response = self._send(http_method='POST',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedView', response)

    def delete_feed_view(self, feed_id, view_id, project=None):
        """DeleteFeedView.
        [Preview API] Delete a feed view.
        :param str feed_id: Name or Id of the feed.
        :param str view_id: Name or Id of the view.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        self._send(http_method='DELETE',
                   location_id='42a8502a-6785-41bc-8c16-89477d930877',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed_view(self, feed_id, view_id, project=None):
        """GetFeedView.
        [Preview API] Get a view by Id.
        :param str feed_id: Name or Id of the feed.
        :param str view_id: Name or Id of the view.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedView> <azure.devops.v5_1.feed.models.FeedView>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        response = self._send(http_method='GET',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedView', response)

    def get_feed_views(self, feed_id, project=None):
        """GetFeedViews.
        [Preview API] Get all views for a feed.
        :param str feed_id: Name or Id of the feed.
        :param str project: Project ID or project name
        :rtype: [FeedView]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[FeedView]', self._unwrap_collection(response))

    def update_feed_view(self, view, feed_id, view_id, project=None):
        """UpdateFeedView.
        [Preview API] Update a view.
        :param :class:`<FeedView> <azure.devops.v5_1.feed.models.FeedView>` view: New settings to apply to the specified view.
        :param str feed_id: Name or Id of the feed.
        :param str view_id: Name or Id of the view.
        :param str project: Project ID or project name
        :rtype: :class:`<FeedView> <azure.devops.v5_1.feed.models.FeedView>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        content = self._serialize.body(view, 'FeedView')
        response = self._send(http_method='PATCH',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedView', response)

