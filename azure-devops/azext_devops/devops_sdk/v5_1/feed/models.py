# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FeedBatchData(Model):
    """FeedBatchData.

    :param data:
    :type data: :class:`FeedBatchOperationData <azure.devops.v5_1.packaging.models.FeedBatchOperationData>`
    :param operation:
    :type operation: object
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'FeedBatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'}
    }

    def __init__(self, data=None, operation=None):
        super(FeedBatchData, self).__init__()
        self.data = data
        self.operation = operation


class FeedBatchOperationData(Model):
    """FeedBatchOperationData.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(FeedBatchOperationData, self).__init__()


class FeedChange(Model):
    """FeedChange.

    :param change_type: The type of operation.
    :type change_type: object
    :param feed: The state of the feed after a after a create, update, or delete operation completed.
    :type feed: :class:`Feed <azure.devops.v5_1.packaging.models.Feed>`
    :param feed_continuation_token: A token that identifies the next change in the log of changes.
    :type feed_continuation_token: long
    :param latest_package_continuation_token: A token that identifies the latest package change for this feed.  This can be used to quickly determine if there have been any changes to packages in a specific feed.
    :type latest_package_continuation_token: long
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'feed': {'key': 'feed', 'type': 'Feed'},
        'feed_continuation_token': {'key': 'feedContinuationToken', 'type': 'long'},
        'latest_package_continuation_token': {'key': 'latestPackageContinuationToken', 'type': 'long'}
    }

    def __init__(self, change_type=None, feed=None, feed_continuation_token=None, latest_package_continuation_token=None):
        super(FeedChange, self).__init__()
        self.change_type = change_type
        self.feed = feed
        self.feed_continuation_token = feed_continuation_token
        self.latest_package_continuation_token = latest_package_continuation_token


class FeedChangesResponse(Model):
    """FeedChangesResponse.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param count: The number of changes in this set.
    :type count: int
    :param feed_changes: A container that encapsulates the state of the feed after a create, update, or delete.
    :type feed_changes: list of :class:`FeedChange <azure.devops.v5_1.packaging.models.FeedChange>`
    :param next_feed_continuation_token: When iterating through the log of changes this value indicates the value that should be used for the next continuation token.
    :type next_feed_continuation_token: long
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'count': {'key': 'count', 'type': 'int'},
        'feed_changes': {'key': 'feedChanges', 'type': '[FeedChange]'},
        'next_feed_continuation_token': {'key': 'nextFeedContinuationToken', 'type': 'long'}
    }

    def __init__(self, _links=None, count=None, feed_changes=None, next_feed_continuation_token=None):
        super(FeedChangesResponse, self).__init__()
        self._links = _links
        self.count = count
        self.feed_changes = feed_changes
        self.next_feed_continuation_token = next_feed_continuation_token


class FeedCore(Model):
    """FeedCore.

    :param allow_upstream_name_conflict: OBSOLETE: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param capabilities: Supported capabilities of a feed.
    :type capabilities: object
    :param fully_qualified_id: This will either be the feed GUID or the feed GUID and view GUID depending on how the feed was accessed.
    :type fully_qualified_id: str
    :param fully_qualified_name: Full name of the view, in feed@view format.
    :type fully_qualified_name: str
    :param id: A GUID that uniquely identifies this feed.
    :type id: str
    :param is_read_only: If set, all packages in the feed are immutable.  It is important to note that feed views are immutable; therefore, this flag will always be set for views.
    :type is_read_only: bool
    :param name: A name for the feed. feed names must follow these rules: <list type="bullet"><item><description> Must not exceed 64 characters </description></item><item><description> Must not contain whitespaces </description></item><item><description> Must not start with an underscore or a period </description></item><item><description> Must not end with a period </description></item><item><description> Must not contain any of the following illegal characters: <![CDATA[ @, ~, ;, {, }, \, +, =, <, >, |, /, \\, ?, :, &, $, *, \", #, [, ] ]]></description></item></list>
    :type name: str
    :param project: The project that this feed is associated with.
    :type project: :class:`ProjectReference <azure.devops.v5_1.packaging.models.ProjectReference>`
    :param upstream_enabled: OBSOLETE: This should always be true.  Setting to false will override all sources in UpstreamSources.
    :type upstream_enabled: bool
    :param upstream_sources: A list of sources that this feed will fetch packages from.  An empty list indicates that this feed will not search any additional sources for packages.
    :type upstream_sources: list of :class:`UpstreamSource <azure.devops.v5_1.packaging.models.UpstreamSource>`
    :param view: Definition of the view.
    :type view: :class:`FeedView <azure.devops.v5_1.packaging.models.FeedView>`
    :param view_id: View Id.
    :type view_id: str
    :param view_name: View name.
    :type view_name: str
    """

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'capabilities': {'key': 'capabilities', 'type': 'object'},
        'fully_qualified_id': {'key': 'fullyQualifiedId', 'type': 'str'},
        'fully_qualified_name': {'key': 'fullyQualifiedName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'view': {'key': 'view', 'type': 'FeedView'},
        'view_id': {'key': 'viewId', 'type': 'str'},
        'view_name': {'key': 'viewName', 'type': 'str'}
    }

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, project=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None):
        super(FeedCore, self).__init__()
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.capabilities = capabilities
        self.fully_qualified_id = fully_qualified_id
        self.fully_qualified_name = fully_qualified_name
        self.id = id
        self.is_read_only = is_read_only
        self.name = name
        self.project = project
        self.upstream_enabled = upstream_enabled
        self.upstream_sources = upstream_sources
        self.view = view
        self.view_id = view_id
        self.view_name = view_name


class FeedPermission(Model):
    """FeedPermission.

    :param display_name: Display name for the identity.
    :type display_name: str
    :param identity_descriptor: Identity associated with this role.
    :type identity_descriptor: :class:`str <azure.devops.v5_1.packaging.models.str>`
    :param identity_id: Id of the identity associated with this role.
    :type identity_id: str
    :param role: The role for this identity on a feed.
    :type role: object
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identity_descriptor': {'key': 'identityDescriptor', 'type': 'str'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'role': {'key': 'role', 'type': 'object'}
    }

    def __init__(self, display_name=None, identity_descriptor=None, identity_id=None, role=None):
        super(FeedPermission, self).__init__()
        self.display_name = display_name
        self.identity_descriptor = identity_descriptor
        self.identity_id = identity_id
        self.role = role


class FeedRetentionPolicy(Model):
    """FeedRetentionPolicy.

    :param age_limit_in_days: This attribute is deprecated and is not honoured by retention
    :type age_limit_in_days: int
    :param count_limit: Maximum versions to preserve per package and package type.
    :type count_limit: int
    :param days_to_keep_recently_downloaded_packages: Number of days to preserve a package version after its latest download.
    :type days_to_keep_recently_downloaded_packages: int
    """

    _attribute_map = {
        'age_limit_in_days': {'key': 'ageLimitInDays', 'type': 'int'},
        'count_limit': {'key': 'countLimit', 'type': 'int'},
        'days_to_keep_recently_downloaded_packages': {'key': 'daysToKeepRecentlyDownloadedPackages', 'type': 'int'}
    }

    def __init__(self, age_limit_in_days=None, count_limit=None, days_to_keep_recently_downloaded_packages=None):
        super(FeedRetentionPolicy, self).__init__()
        self.age_limit_in_days = age_limit_in_days
        self.count_limit = count_limit
        self.days_to_keep_recently_downloaded_packages = days_to_keep_recently_downloaded_packages


class FeedUpdate(Model):
    """FeedUpdate.

    :param allow_upstream_name_conflict: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param badges_enabled: If set, this feed supports generation of package badges.
    :type badges_enabled: bool
    :param default_view_id: The view that the feed administrator has indicated is the default experience for readers.
    :type default_view_id: str
    :param description: A description for the feed.  Descriptions must not exceed 255 characters.
    :type description: str
    :param hide_deleted_package_versions: If set, feed will hide all deleted/unpublished versions
    :type hide_deleted_package_versions: bool
    :param id: A GUID that uniquely identifies this feed.
    :type id: str
    :param name: A name for the feed. feed names must follow these rules: <list type="bullet"><item><description> Must not exceed 64 characters </description></item><item><description> Must not contain whitespaces </description></item><item><description> Must not start with an underscore or a period </description></item><item><description> Must not end with a period </description></item><item><description> Must not contain any of the following illegal characters: <![CDATA[ @, ~, ;, {, }, \, +, =, <, >, |, /, \\, ?, :, &, $, *, \", #, [, ] ]]></description></item></list>
    :type name: str
    :param upstream_enabled: OBSOLETE: If set, the feed can proxy packages from an upstream feed
    :type upstream_enabled: bool
    :param upstream_sources: A list of sources that this feed will fetch packages from.  An empty list indicates that this feed will not search any additional sources for packages.
    :type upstream_sources: list of :class:`UpstreamSource <azure.devops.v5_1.packaging.models.UpstreamSource>`
    """

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'badges_enabled': {'key': 'badgesEnabled', 'type': 'bool'},
        'default_view_id': {'key': 'defaultViewId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'hide_deleted_package_versions': {'key': 'hideDeletedPackageVersions', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'}
    }

    def __init__(self, allow_upstream_name_conflict=None, badges_enabled=None, default_view_id=None, description=None, hide_deleted_package_versions=None, id=None, name=None, upstream_enabled=None, upstream_sources=None):
        super(FeedUpdate, self).__init__()
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.badges_enabled = badges_enabled
        self.default_view_id = default_view_id
        self.description = description
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.id = id
        self.name = name
        self.upstream_enabled = upstream_enabled
        self.upstream_sources = upstream_sources


class FeedView(Model):
    """FeedView.

    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param id: Id of the view.
    :type id: str
    :param name: Name of the view.
    :type name: str
    :param type: Type of view.
    :type type: object
    :param url: Url of the view.
    :type url: str
    :param visibility: Visibility status of the view.
    :type visibility: object
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, _links=None, id=None, name=None, type=None, url=None, visibility=None):
        super(FeedView, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.type = type
        self.url = url
        self.visibility = visibility


class GlobalPermission(Model):
    """GlobalPermission.

    :param identity_descriptor: Identity of the user with the provided Role.
    :type identity_descriptor: :class:`str <azure.devops.v5_1.packaging.models.str>`
    :param role: Role associated with the Identity.
    :type role: object
    """

    _attribute_map = {
        'identity_descriptor': {'key': 'identityDescriptor', 'type': 'str'},
        'role': {'key': 'role', 'type': 'object'}
    }

    def __init__(self, identity_descriptor=None, role=None):
        super(GlobalPermission, self).__init__()
        self.identity_descriptor = identity_descriptor
        self.role = role


class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation. In the case of an array, a zero based index can be used to specify the position in the array (e.g. /biscuits/0/name). The "-" character can be used instead of an index to insert at the end of the array (e.g. /biscuits/-).
    :type path: str
    :param value: The value for the operation. This is either a primitive or a JToken.
    :type value: object
    """

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class MinimalPackageVersion(Model):
    """MinimalPackageVersion.

    :param direct_upstream_source_id: Upstream source this package was ingested from.
    :type direct_upstream_source_id: str
    :param id: Id for the package.
    :type id: str
    :param is_cached_version: [Obsolete] Used for legacy scenarios and may be removed in future versions.
    :type is_cached_version: bool
    :param is_deleted: True if this package has been deleted.
    :type is_deleted: bool
    :param is_latest: True if this is the latest version of the package by package type sort order.
    :type is_latest: bool
    :param is_listed: (NuGet Only) True if this package is listed.
    :type is_listed: bool
    :param normalized_version: Normalized version using normalization rules specific to a package type.
    :type normalized_version: str
    :param package_description: Package description.
    :type package_description: str
    :param publish_date: UTC Date the package was published to the service.
    :type publish_date: datetime
    :param storage_id: Internal storage id.
    :type storage_id: str
    :param version: Display version.
    :type version: str
    :param views: List of views containing this package version.
    :type views: list of :class:`FeedView <azure.devops.v5_1.packaging.models.FeedView>`
    """

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None):
        super(MinimalPackageVersion, self).__init__()
        self.direct_upstream_source_id = direct_upstream_source_id
        self.id = id
        self.is_cached_version = is_cached_version
        self.is_deleted = is_deleted
        self.is_latest = is_latest
        self.is_listed = is_listed
        self.normalized_version = normalized_version
        self.package_description = package_description
        self.publish_date = publish_date
        self.storage_id = storage_id
        self.version = version
        self.views = views


class Package(Model):
    """Package.

    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param id: Id of the package.
    :type id: str
    :param is_cached: Used for legacy scenarios and may be removed in future versions.
    :type is_cached: bool
    :param name: The display name of the package.
    :type name: str
    :param normalized_name: The normalized name representing the identity of this package within its package type.
    :type normalized_name: str
    :param protocol_type: Type of the package.
    :type protocol_type: str
    :param star_count: [Obsolete] - this field is unused and will be removed in a future release.
    :type star_count: int
    :param url: Url for this package.
    :type url: str
    :param versions: All versions for this package within its feed.
    :type versions: list of :class:`MinimalPackageVersion <azure.devops.v5_1.packaging.models.MinimalPackageVersion>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached': {'key': 'isCached', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'normalized_name': {'key': 'normalizedName', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'},
        'star_count': {'key': 'starCount', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[MinimalPackageVersion]'}
    }

    def __init__(self, _links=None, id=None, is_cached=None, name=None, normalized_name=None, protocol_type=None, star_count=None, url=None, versions=None):
        super(Package, self).__init__()
        self._links = _links
        self.id = id
        self.is_cached = is_cached
        self.name = name
        self.normalized_name = normalized_name
        self.protocol_type = protocol_type
        self.star_count = star_count
        self.url = url
        self.versions = versions


class PackageChange(Model):
    """PackageChange.

    :param package: Package that was changed.
    :type package: :class:`Package <azure.devops.v5_1.packaging.models.Package>`
    :param package_version_change: Change that was performed on a package version.
    :type package_version_change: :class:`PackageVersionChange <azure.devops.v5_1.packaging.models.PackageVersionChange>`
    """

    _attribute_map = {
        'package': {'key': 'package', 'type': 'Package'},
        'package_version_change': {'key': 'packageVersionChange', 'type': 'PackageVersionChange'}
    }

    def __init__(self, package=None, package_version_change=None):
        super(PackageChange, self).__init__()
        self.package = package
        self.package_version_change = package_version_change


class PackageChangesResponse(Model):
    """PackageChangesResponse.

    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param count: Number of changes in this batch.
    :type count: int
    :param next_package_continuation_token: Token that should be used in future calls for this feed to retrieve new changes.
    :type next_package_continuation_token: long
    :param package_changes: List of changes.
    :type package_changes: list of :class:`PackageChange <azure.devops.v5_1.packaging.models.PackageChange>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'count': {'key': 'count', 'type': 'int'},
        'next_package_continuation_token': {'key': 'nextPackageContinuationToken', 'type': 'long'},
        'package_changes': {'key': 'packageChanges', 'type': '[PackageChange]'}
    }

    def __init__(self, _links=None, count=None, next_package_continuation_token=None, package_changes=None):
        super(PackageChangesResponse, self).__init__()
        self._links = _links
        self.count = count
        self.next_package_continuation_token = next_package_continuation_token
        self.package_changes = package_changes


class PackageDependency(Model):
    """PackageDependency.

    :param group: Dependency package group (an optional classification within some package types).
    :type group: str
    :param package_name: Dependency package name.
    :type package_name: str
    :param version_range: Dependency package version range.
    :type version_range: str
    """

    _attribute_map = {
        'group': {'key': 'group', 'type': 'str'},
        'package_name': {'key': 'packageName', 'type': 'str'},
        'version_range': {'key': 'versionRange', 'type': 'str'}
    }

    def __init__(self, group=None, package_name=None, version_range=None):
        super(PackageDependency, self).__init__()
        self.group = group
        self.package_name = package_name
        self.version_range = version_range


class PackageFile(Model):
    """PackageFile.

    :param children: Hierarchical representation of files.
    :type children: list of :class:`PackageFile <azure.devops.v5_1.packaging.models.PackageFile>`
    :param name: File name.
    :type name: str
    :param protocol_metadata: Extended data unique to a specific package type.
    :type protocol_metadata: :class:`ProtocolMetadata <azure.devops.v5_1.packaging.models.ProtocolMetadata>`
    """

    _attribute_map = {
        'children': {'key': 'children', 'type': '[PackageFile]'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'}
    }

    def __init__(self, children=None, name=None, protocol_metadata=None):
        super(PackageFile, self).__init__()
        self.children = children
        self.name = name
        self.protocol_metadata = protocol_metadata


class PackageMetrics(Model):
    """PackageMetrics.

    :param download_count: Total count of downloads per package id.
    :type download_count: float
    :param download_unique_users: Number of downloads per unique user per package id.
    :type download_unique_users: float
    :param last_downloaded: UTC date and time when package was last downloaded.
    :type last_downloaded: datetime
    :param package_id: Package id.
    :type package_id: str
    """

    _attribute_map = {
        'download_count': {'key': 'downloadCount', 'type': 'float'},
        'download_unique_users': {'key': 'downloadUniqueUsers', 'type': 'float'},
        'last_downloaded': {'key': 'lastDownloaded', 'type': 'iso-8601'},
        'package_id': {'key': 'packageId', 'type': 'str'}
    }

    def __init__(self, download_count=None, download_unique_users=None, last_downloaded=None, package_id=None):
        super(PackageMetrics, self).__init__()
        self.download_count = download_count
        self.download_unique_users = download_unique_users
        self.last_downloaded = last_downloaded
        self.package_id = package_id


class PackageMetricsQuery(Model):
    """PackageMetricsQuery.

    :param package_ids: List of package ids
    :type package_ids: list of str
    """

    _attribute_map = {
        'package_ids': {'key': 'packageIds', 'type': '[str]'}
    }

    def __init__(self, package_ids=None):
        super(PackageMetricsQuery, self).__init__()
        self.package_ids = package_ids


class PackageVersion(MinimalPackageVersion):
    """PackageVersion.

    :param direct_upstream_source_id: Upstream source this package was ingested from.
    :type direct_upstream_source_id: str
    :param id: Id for the package.
    :type id: str
    :param is_cached_version: [Obsolete] Used for legacy scenarios and may be removed in future versions.
    :type is_cached_version: bool
    :param is_deleted: True if this package has been deleted.
    :type is_deleted: bool
    :param is_latest: True if this is the latest version of the package by package type sort order.
    :type is_latest: bool
    :param is_listed: (NuGet Only) True if this package is listed.
    :type is_listed: bool
    :param normalized_version: Normalized version using normalization rules specific to a package type.
    :type normalized_version: str
    :param package_description: Package description.
    :type package_description: str
    :param publish_date: UTC Date the package was published to the service.
    :type publish_date: datetime
    :param storage_id: Internal storage id.
    :type storage_id: str
    :param version: Display version.
    :type version: str
    :param views: List of views containing this package version.
    :type views: list of :class:`FeedView <azure.devops.v5_1.packaging.models.FeedView>`
    :param _links: Related links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param author: Package version author.
    :type author: str
    :param deleted_date: UTC date that this package version was deleted.
    :type deleted_date: datetime
    :param dependencies: List of dependencies for this package version.
    :type dependencies: list of :class:`PackageDependency <azure.devops.v5_1.packaging.models.PackageDependency>`
    :param description: Package version description.
    :type description: str
    :param files: Files associated with this package version, only relevant for multi-file package types.
    :type files: list of :class:`PackageFile <azure.devops.v5_1.packaging.models.PackageFile>`
    :param other_versions: Other versions of this package.
    :type other_versions: list of :class:`MinimalPackageVersion <azure.devops.v5_1.packaging.models.MinimalPackageVersion>`
    :param protocol_metadata: Extended data specific to a package type.
    :type protocol_metadata: :class:`ProtocolMetadata <azure.devops.v5_1.packaging.models.ProtocolMetadata>`
    :param source_chain: List of upstream sources through which a package version moved to land in this feed.
    :type source_chain: list of :class:`UpstreamSource <azure.devops.v5_1.packaging.models.UpstreamSource>`
    :param summary: Package version summary.
    :type summary: str
    :param tags: Package version tags.
    :type tags: list of str
    :param url: Package version url.
    :type url: str
    """

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'dependencies': {'key': 'dependencies', 'type': '[PackageDependency]'},
        'description': {'key': 'description', 'type': 'str'},
        'files': {'key': 'files', 'type': '[PackageFile]'},
        'other_versions': {'key': 'otherVersions', 'type': '[MinimalPackageVersion]'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSource]'},
        'summary': {'key': 'summary', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None, _links=None, author=None, deleted_date=None, dependencies=None, description=None, files=None, other_versions=None, protocol_metadata=None, source_chain=None, summary=None, tags=None, url=None):
        super(PackageVersion, self).__init__(direct_upstream_source_id=direct_upstream_source_id, id=id, is_cached_version=is_cached_version, is_deleted=is_deleted, is_latest=is_latest, is_listed=is_listed, normalized_version=normalized_version, package_description=package_description, publish_date=publish_date, storage_id=storage_id, version=version, views=views)
        self._links = _links
        self.author = author
        self.deleted_date = deleted_date
        self.dependencies = dependencies
        self.description = description
        self.files = files
        self.other_versions = other_versions
        self.protocol_metadata = protocol_metadata
        self.source_chain = source_chain
        self.summary = summary
        self.tags = tags
        self.url = url


class PackageVersionChange(Model):
    """PackageVersionChange.

    :param change_type: The type of change that was performed.
    :type change_type: object
    :param continuation_token: Token marker for this change, allowing the caller to send this value back to the service and receive changes beyond this one.
    :type continuation_token: long
    :param package_version: Package version that was changed.
    :type package_version: :class:`PackageVersion <azure.devops.v5_1.packaging.models.PackageVersion>`
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'continuation_token': {'key': 'continuationToken', 'type': 'long'},
        'package_version': {'key': 'packageVersion', 'type': 'PackageVersion'}
    }

    def __init__(self, change_type=None, continuation_token=None, package_version=None):
        super(PackageVersionChange, self).__init__()
        self.change_type = change_type
        self.continuation_token = continuation_token
        self.package_version = package_version


class PackageVersionMetrics(Model):
    """PackageVersionMetrics.

    :param download_count: Total count of downloads per package version id.
    :type download_count: float
    :param download_unique_users: Number of downloads per unique user per package version id.
    :type download_unique_users: float
    :param last_downloaded: UTC date and time when package version was last downloaded.
    :type last_downloaded: datetime
    :param package_id: Package id.
    :type package_id: str
    :param package_version_id: Package version id.
    :type package_version_id: str
    """

    _attribute_map = {
        'download_count': {'key': 'downloadCount', 'type': 'float'},
        'download_unique_users': {'key': 'downloadUniqueUsers', 'type': 'float'},
        'last_downloaded': {'key': 'lastDownloaded', 'type': 'iso-8601'},
        'package_id': {'key': 'packageId', 'type': 'str'},
        'package_version_id': {'key': 'packageVersionId', 'type': 'str'}
    }

    def __init__(self, download_count=None, download_unique_users=None, last_downloaded=None, package_id=None, package_version_id=None):
        super(PackageVersionMetrics, self).__init__()
        self.download_count = download_count
        self.download_unique_users = download_unique_users
        self.last_downloaded = last_downloaded
        self.package_id = package_id
        self.package_version_id = package_version_id


class PackageVersionMetricsQuery(Model):
    """PackageVersionMetricsQuery.

    :param package_version_ids: List of package version ids
    :type package_version_ids: list of str
    """

    _attribute_map = {
        'package_version_ids': {'key': 'packageVersionIds', 'type': '[str]'}
    }

    def __init__(self, package_version_ids=None):
        super(PackageVersionMetricsQuery, self).__init__()
        self.package_version_ids = package_version_ids


class PackageVersionProvenance(Model):
    """PackageVersionProvenance.

    :param feed_id: Name or Id of the feed.
    :type feed_id: str
    :param package_id: Id of the package (GUID Id, not name).
    :type package_id: str
    :param package_version_id: Id of the package version (GUID Id, not name).
    :type package_version_id: str
    :param provenance: Provenance information for this package version.
    :type provenance: :class:`Provenance <azure.devops.v5_1.packaging.models.Provenance>`
    """

    _attribute_map = {
        'feed_id': {'key': 'feedId', 'type': 'str'},
        'package_id': {'key': 'packageId', 'type': 'str'},
        'package_version_id': {'key': 'packageVersionId', 'type': 'str'},
        'provenance': {'key': 'provenance', 'type': 'Provenance'}
    }

    def __init__(self, feed_id=None, package_id=None, package_version_id=None, provenance=None):
        super(PackageVersionProvenance, self).__init__()
        self.feed_id = feed_id
        self.package_id = package_id
        self.package_version_id = package_version_id
        self.provenance = provenance


class ProjectReference(Model):
    """ProjectReference.

    :param id: Gets or sets id of the project.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, id=None):
        super(ProjectReference, self).__init__()
        self.id = id


class ProtocolMetadata(Model):
    """ProtocolMetadata.

    :param data: Extended metadata for a specific package type, formatted to the associated schema version definition.
    :type data: object
    :param schema_version: Schema version.
    :type schema_version: int
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'object'},
        'schema_version': {'key': 'schemaVersion', 'type': 'int'}
    }

    def __init__(self, data=None, schema_version=None):
        super(ProtocolMetadata, self).__init__()
        self.data = data
        self.schema_version = schema_version


class Provenance(Model):
    """Provenance.

    :param data: Other provenance data.
    :type data: dict
    :param provenance_source: Type of provenance source, for example "InternalBuild", "InternalRelease"
    :type provenance_source: str
    :param publisher_user_identity: Identity of user that published the package
    :type publisher_user_identity: str
    :param user_agent: HTTP User-Agent used when pushing the package.
    :type user_agent: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'provenance_source': {'key': 'provenanceSource', 'type': 'str'},
        'publisher_user_identity': {'key': 'publisherUserIdentity', 'type': 'str'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, data=None, provenance_source=None, publisher_user_identity=None, user_agent=None):
        super(Provenance, self).__init__()
        self.data = data
        self.provenance_source = provenance_source
        self.publisher_user_identity = publisher_user_identity
        self.user_agent = user_agent


class RecycleBinPackageVersion(PackageVersion):
    """RecycleBinPackageVersion.

    :param direct_upstream_source_id: Upstream source this package was ingested from.
    :type direct_upstream_source_id: str
    :param id: Id for the package.
    :type id: str
    :param is_cached_version: [Obsolete] Used for legacy scenarios and may be removed in future versions.
    :type is_cached_version: bool
    :param is_deleted: True if this package has been deleted.
    :type is_deleted: bool
    :param is_latest: True if this is the latest version of the package by package type sort order.
    :type is_latest: bool
    :param is_listed: (NuGet Only) True if this package is listed.
    :type is_listed: bool
    :param normalized_version: Normalized version using normalization rules specific to a package type.
    :type normalized_version: str
    :param package_description: Package description.
    :type package_description: str
    :param publish_date: UTC Date the package was published to the service.
    :type publish_date: datetime
    :param storage_id: Internal storage id.
    :type storage_id: str
    :param version: Display version.
    :type version: str
    :param views: List of views containing this package version.
    :type views: list of :class:`FeedView <azure.devops.v5_1.packaging.models.FeedView>`
    :param _links: Related links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param author: Package version author.
    :type author: str
    :param deleted_date: UTC date that this package version was deleted.
    :type deleted_date: datetime
    :param dependencies: List of dependencies for this package version.
    :type dependencies: list of :class:`PackageDependency <azure.devops.v5_1.packaging.models.PackageDependency>`
    :param description: Package version description.
    :type description: str
    :param files: Files associated with this package version, only relevant for multi-file package types.
    :type files: list of :class:`PackageFile <azure.devops.v5_1.packaging.models.PackageFile>`
    :param other_versions: Other versions of this package.
    :type other_versions: list of :class:`MinimalPackageVersion <azure.devops.v5_1.packaging.models.MinimalPackageVersion>`
    :param protocol_metadata: Extended data specific to a package type.
    :type protocol_metadata: :class:`ProtocolMetadata <azure.devops.v5_1.packaging.models.ProtocolMetadata>`
    :param source_chain: List of upstream sources through which a package version moved to land in this feed.
    :type source_chain: list of :class:`UpstreamSource <azure.devops.v5_1.packaging.models.UpstreamSource>`
    :param summary: Package version summary.
    :type summary: str
    :param tags: Package version tags.
    :type tags: list of str
    :param url: Package version url.
    :type url: str
    :param scheduled_permanent_delete_date: UTC date on which the package will automatically be removed from the recycle bin and permanently deleted.
    :type scheduled_permanent_delete_date: datetime
    """

    _attribute_map = {
        'direct_upstream_source_id': {'key': 'directUpstreamSourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_cached_version': {'key': 'isCachedVersion', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_latest': {'key': 'isLatest', 'type': 'bool'},
        'is_listed': {'key': 'isListed', 'type': 'bool'},
        'normalized_version': {'key': 'normalizedVersion', 'type': 'str'},
        'package_description': {'key': 'packageDescription', 'type': 'str'},
        'publish_date': {'key': 'publishDate', 'type': 'iso-8601'},
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'views': {'key': 'views', 'type': '[FeedView]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'dependencies': {'key': 'dependencies', 'type': '[PackageDependency]'},
        'description': {'key': 'description', 'type': 'str'},
        'files': {'key': 'files', 'type': '[PackageFile]'},
        'other_versions': {'key': 'otherVersions', 'type': '[MinimalPackageVersion]'},
        'protocol_metadata': {'key': 'protocolMetadata', 'type': 'ProtocolMetadata'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSource]'},
        'summary': {'key': 'summary', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'},
        'scheduled_permanent_delete_date': {'key': 'scheduledPermanentDeleteDate', 'type': 'iso-8601'}
    }

    def __init__(self, direct_upstream_source_id=None, id=None, is_cached_version=None, is_deleted=None, is_latest=None, is_listed=None, normalized_version=None, package_description=None, publish_date=None, storage_id=None, version=None, views=None, _links=None, author=None, deleted_date=None, dependencies=None, description=None, files=None, other_versions=None, protocol_metadata=None, source_chain=None, summary=None, tags=None, url=None, scheduled_permanent_delete_date=None):
        super(RecycleBinPackageVersion, self).__init__(direct_upstream_source_id=direct_upstream_source_id, id=id, is_cached_version=is_cached_version, is_deleted=is_deleted, is_latest=is_latest, is_listed=is_listed, normalized_version=normalized_version, package_description=package_description, publish_date=publish_date, storage_id=storage_id, version=version, views=views, _links=_links, author=author, deleted_date=deleted_date, dependencies=dependencies, description=description, files=files, other_versions=other_versions, protocol_metadata=protocol_metadata, source_chain=source_chain, summary=summary, tags=tags, url=url)
        self.scheduled_permanent_delete_date = scheduled_permanent_delete_date


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpstreamSource(Model):
    """UpstreamSource.

    :param deleted_date: UTC date that this upstream was deleted.
    :type deleted_date: datetime
    :param id: Identity of the upstream source.
    :type id: str
    :param internal_upstream_collection_id: For an internal upstream type, track the Azure DevOps organization that contains it.
    :type internal_upstream_collection_id: str
    :param internal_upstream_feed_id: For an internal upstream type, track the feed id being referenced.
    :type internal_upstream_feed_id: str
    :param internal_upstream_view_id: For an internal upstream type, track the view of the feed being referenced.
    :type internal_upstream_view_id: str
    :param location: Locator for connecting to the upstream source.
    :type location: str
    :param name: Display name.
    :type name: str
    :param protocol: Package type associated with the upstream source.
    :type protocol: str
    :param upstream_source_type: Source type, such as Public or Internal.
    :type upstream_source_type: object
    """

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'internal_upstream_collection_id': {'key': 'internalUpstreamCollectionId', 'type': 'str'},
        'internal_upstream_feed_id': {'key': 'internalUpstreamFeedId', 'type': 'str'},
        'internal_upstream_view_id': {'key': 'internalUpstreamViewId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'upstream_source_type': {'key': 'upstreamSourceType', 'type': 'object'}
    }

    def __init__(self, deleted_date=None, id=None, internal_upstream_collection_id=None, internal_upstream_feed_id=None, internal_upstream_view_id=None, location=None, name=None, protocol=None, upstream_source_type=None):
        super(UpstreamSource, self).__init__()
        self.deleted_date = deleted_date
        self.id = id
        self.internal_upstream_collection_id = internal_upstream_collection_id
        self.internal_upstream_feed_id = internal_upstream_feed_id
        self.internal_upstream_view_id = internal_upstream_view_id
        self.location = location
        self.name = name
        self.protocol = protocol
        self.upstream_source_type = upstream_source_type


class Feed(FeedCore):
    """Feed.

    :param allow_upstream_name_conflict: OBSOLETE: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param capabilities: Supported capabilities of a feed.
    :type capabilities: object
    :param fully_qualified_id: This will either be the feed GUID or the feed GUID and view GUID depending on how the feed was accessed.
    :type fully_qualified_id: str
    :param fully_qualified_name: Full name of the view, in feed@view format.
    :type fully_qualified_name: str
    :param id: A GUID that uniquely identifies this feed.
    :type id: str
    :param is_read_only: If set, all packages in the feed are immutable.  It is important to note that feed views are immutable; therefore, this flag will always be set for views.
    :type is_read_only: bool
    :param name: A name for the feed. feed names must follow these rules: <list type="bullet"><item><description> Must not exceed 64 characters </description></item><item><description> Must not contain whitespaces </description></item><item><description> Must not start with an underscore or a period </description></item><item><description> Must not end with a period </description></item><item><description> Must not contain any of the following illegal characters: <![CDATA[ @, ~, ;, {, }, \, +, =, <, >, |, /, \\, ?, :, &, $, *, \", #, [, ] ]]></description></item></list>
    :type name: str
    :param project: The project that this feed is associated with.
    :type project: :class:`ProjectReference <azure.devops.v5_1.packaging.models.ProjectReference>`
    :param upstream_enabled: OBSOLETE: This should always be true.  Setting to false will override all sources in UpstreamSources.
    :type upstream_enabled: bool
    :param upstream_sources: A list of sources that this feed will fetch packages from.  An empty list indicates that this feed will not search any additional sources for packages.
    :type upstream_sources: list of :class:`UpstreamSource <azure.devops.v5_1.packaging.models.UpstreamSource>`
    :param view: Definition of the view.
    :type view: :class:`FeedView <azure.devops.v5_1.packaging.models.FeedView>`
    :param view_id: View Id.
    :type view_id: str
    :param view_name: View name.
    :type view_name: str
    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.packaging.models.ReferenceLinks>`
    :param badges_enabled: If set, this feed supports generation of package badges.
    :type badges_enabled: bool
    :param default_view_id: The view that the feed administrator has indicated is the default experience for readers.
    :type default_view_id: str
    :param deleted_date: The date that this feed was deleted.
    :type deleted_date: datetime
    :param description: A description for the feed.  Descriptions must not exceed 255 characters.
    :type description: str
    :param hide_deleted_package_versions: If set, the feed will hide all deleted/unpublished versions
    :type hide_deleted_package_versions: bool
    :param permissions: Explicit permissions for the feed.
    :type permissions: list of :class:`FeedPermission <azure.devops.v5_1.packaging.models.FeedPermission>`
    :param upstream_enabled_changed_date: If set, time that the UpstreamEnabled property was changed. Will be null if UpstreamEnabled was never changed after Feed creation.
    :type upstream_enabled_changed_date: datetime
    :param url: The URL of the base feed in GUID form.
    :type url: str
    """

    _attribute_map = {
        'allow_upstream_name_conflict': {'key': 'allowUpstreamNameConflict', 'type': 'bool'},
        'capabilities': {'key': 'capabilities', 'type': 'object'},
        'fully_qualified_id': {'key': 'fullyQualifiedId', 'type': 'str'},
        'fully_qualified_name': {'key': 'fullyQualifiedName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'view': {'key': 'view', 'type': 'FeedView'},
        'view_id': {'key': 'viewId', 'type': 'str'},
        'view_name': {'key': 'viewName', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'badges_enabled': {'key': 'badgesEnabled', 'type': 'bool'},
        'default_view_id': {'key': 'defaultViewId', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'hide_deleted_package_versions': {'key': 'hideDeletedPackageVersions', 'type': 'bool'},
        'permissions': {'key': 'permissions', 'type': '[FeedPermission]'},
        'upstream_enabled_changed_date': {'key': 'upstreamEnabledChangedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, project=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None, _links=None, badges_enabled=None, default_view_id=None, deleted_date=None, description=None, hide_deleted_package_versions=None, permissions=None, upstream_enabled_changed_date=None, url=None):
        super(Feed, self).__init__(allow_upstream_name_conflict=allow_upstream_name_conflict, capabilities=capabilities, fully_qualified_id=fully_qualified_id, fully_qualified_name=fully_qualified_name, id=id, is_read_only=is_read_only, name=name, project=project, upstream_enabled=upstream_enabled, upstream_sources=upstream_sources, view=view, view_id=view_id, view_name=view_name)
        self._links = _links
        self.badges_enabled = badges_enabled
        self.default_view_id = default_view_id
        self.deleted_date = deleted_date
        self.description = description
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.permissions = permissions
        self.upstream_enabled_changed_date = upstream_enabled_changed_date
        self.url = url


__all__ = [
    'FeedBatchData',
    'FeedBatchOperationData',
    'FeedChange',
    'FeedChangesResponse',
    'FeedCore',
    'FeedPermission',
    'FeedRetentionPolicy',
    'FeedUpdate',
    'FeedView',
    'GlobalPermission',
    'JsonPatchOperation',
    'MinimalPackageVersion',
    'Package',
    'PackageChange',
    'PackageChangesResponse',
    'PackageDependency',
    'PackageFile',
    'PackageMetrics',
    'PackageMetricsQuery',
    'PackageVersion',
    'PackageVersionChange',
    'PackageVersionMetrics',
    'PackageVersionMetricsQuery',
    'PackageVersionProvenance',
    'ProjectReference',
    'ProtocolMetadata',
    'Provenance',
    'RecycleBinPackageVersion',
    'ReferenceLinks',
    'UpstreamSource',
    'Feed',
]
