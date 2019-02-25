# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class FeedChange(Model):
    """FeedChange.

    :param change_type:
    :type change_type: object
    :param feed:
    :type feed: :class:`Feed <packaging.v4_1.models.Feed>`
    :param feed_continuation_token:
    :type feed_continuation_token: long
    :param latest_package_continuation_token:
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
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param count:
    :type count: int
    :param feed_changes:
    :type feed_changes: list of :class:`FeedChange <packaging.v4_1.models.FeedChange>`
    :param next_feed_continuation_token:
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

    :param allow_upstream_name_conflict: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param capabilities:
    :type capabilities: object
    :param fully_qualified_id:
    :type fully_qualified_id: str
    :param fully_qualified_name:
    :type fully_qualified_name: str
    :param id:
    :type id: str
    :param is_read_only:
    :type is_read_only: bool
    :param name:
    :type name: str
    :param upstream_enabled: If set, the feed can proxy packages from an upstream feed
    :type upstream_enabled: bool
    :param upstream_sources: External assemblies should use the extension methods to get the sources for a specific protocol.
    :type upstream_sources: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
    :param view:
    :type view: :class:`FeedView <packaging.v4_1.models.FeedView>`
    :param view_id:
    :type view_id: str
    :param view_name:
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
        'upstream_enabled': {'key': 'upstreamEnabled', 'type': 'bool'},
        'upstream_sources': {'key': 'upstreamSources', 'type': '[UpstreamSource]'},
        'view': {'key': 'view', 'type': 'FeedView'},
        'view_id': {'key': 'viewId', 'type': 'str'},
        'view_name': {'key': 'viewName', 'type': 'str'}
    }

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None):
        super(FeedCore, self).__init__()
        self.allow_upstream_name_conflict = allow_upstream_name_conflict
        self.capabilities = capabilities
        self.fully_qualified_id = fully_qualified_id
        self.fully_qualified_name = fully_qualified_name
        self.id = id
        self.is_read_only = is_read_only
        self.name = name
        self.upstream_enabled = upstream_enabled
        self.upstream_sources = upstream_sources
        self.view = view
        self.view_id = view_id
        self.view_name = view_name



class FeedPermission(Model):
    """FeedPermission.

    :param display_name: Display name for the identity
    :type display_name: str
    :param identity_descriptor:
    :type identity_descriptor: :class:`str <packaging.v4_1.models.str>`
    :param identity_id:
    :type identity_id: str
    :param role:
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

    :param age_limit_in_days:
    :type age_limit_in_days: int
    :param count_limit:
    :type count_limit: int
    """

    _attribute_map = {
        'age_limit_in_days': {'key': 'ageLimitInDays', 'type': 'int'},
        'count_limit': {'key': 'countLimit', 'type': 'int'}
    }

    def __init__(self, age_limit_in_days=None, count_limit=None):
        super(FeedRetentionPolicy, self).__init__()
        self.age_limit_in_days = age_limit_in_days
        self.count_limit = count_limit



class FeedUpdate(Model):
    """FeedUpdate.

    :param allow_upstream_name_conflict: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param badges_enabled:
    :type badges_enabled: bool
    :param default_view_id:
    :type default_view_id: str
    :param description:
    :type description: str
    :param hide_deleted_package_versions: If set, feed will hide all deleted/unpublished versions
    :type hide_deleted_package_versions: bool
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param upstream_enabled:
    :type upstream_enabled: bool
    :param upstream_sources:
    :type upstream_sources: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
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

    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param type:
    :type type: object
    :param url:
    :type url: str
    :param visibility:
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

    :param identity_descriptor:
    :type identity_descriptor: :class:`str <packaging.v4_1.models.str>`
    :param role:
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
    :param path: The path for the operation
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

    :param direct_upstream_source_id:
    :type direct_upstream_source_id: str
    :param id:
    :type id: str
    :param is_cached_version:
    :type is_cached_version: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_latest:
    :type is_latest: bool
    :param is_listed:
    :type is_listed: bool
    :param normalized_version: The normalized version representing the identity of a package version
    :type normalized_version: str
    :param package_description:
    :type package_description: str
    :param publish_date:
    :type publish_date: datetime
    :param storage_id:
    :type storage_id: str
    :param version: The display version of the package version
    :type version: str
    :param views:
    :type views: list of :class:`FeedView <packaging.v4_1.models.FeedView>`
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

    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param id:
    :type id: str
    :param is_cached:
    :type is_cached: bool
    :param name: The display name of the package
    :type name: str
    :param normalized_name: The normalized name representing the identity of this package for this protocol type
    :type normalized_name: str
    :param protocol_type:
    :type protocol_type: str
    :param star_count:
    :type star_count: int
    :param url:
    :type url: str
    :param versions:
    :type versions: list of :class:`MinimalPackageVersion <packaging.v4_1.models.MinimalPackageVersion>`
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

    :param package:
    :type package: :class:`Package <packaging.v4_1.models.Package>`
    :param package_version_change:
    :type package_version_change: :class:`PackageVersionChange <packaging.v4_1.models.PackageVersionChange>`
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

    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param count:
    :type count: int
    :param next_package_continuation_token:
    :type next_package_continuation_token: long
    :param package_changes:
    :type package_changes: list of :class:`PackageChange <packaging.v4_1.models.PackageChange>`
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

    :param group:
    :type group: str
    :param package_name:
    :type package_name: str
    :param version_range:
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

    :param children:
    :type children: list of :class:`PackageFile <packaging.v4_1.models.PackageFile>`
    :param name:
    :type name: str
    :param protocol_metadata:
    :type protocol_metadata: :class:`ProtocolMetadata <packaging.v4_1.models.ProtocolMetadata>`
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



class PackageVersion(MinimalPackageVersion):
    """PackageVersion.

    :param direct_upstream_source_id:
    :type direct_upstream_source_id: str
    :param id:
    :type id: str
    :param is_cached_version:
    :type is_cached_version: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_latest:
    :type is_latest: bool
    :param is_listed:
    :type is_listed: bool
    :param normalized_version: The normalized version representing the identity of a package version
    :type normalized_version: str
    :param package_description:
    :type package_description: str
    :param publish_date:
    :type publish_date: datetime
    :param storage_id:
    :type storage_id: str
    :param version: The display version of the package version
    :type version: str
    :param views:
    :type views: list of :class:`FeedView <packaging.v4_1.models.FeedView>`
    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param author:
    :type author: str
    :param deleted_date:
    :type deleted_date: datetime
    :param dependencies:
    :type dependencies: list of :class:`PackageDependency <packaging.v4_1.models.PackageDependency>`
    :param description:
    :type description: str
    :param files:
    :type files: list of :class:`PackageFile <packaging.v4_1.models.PackageFile>`
    :param other_versions:
    :type other_versions: list of :class:`MinimalPackageVersion <packaging.v4_1.models.MinimalPackageVersion>`
    :param protocol_metadata:
    :type protocol_metadata: :class:`ProtocolMetadata <packaging.v4_1.models.ProtocolMetadata>`
    :param source_chain:
    :type source_chain: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
    :param summary:
    :type summary: str
    :param tags:
    :type tags: list of str
    :param url:
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

    :param change_type:
    :type change_type: object
    :param continuation_token:
    :type continuation_token: long
    :param package_version:
    :type package_version: :class:`PackageVersion <packaging.v4_1.models.PackageVersion>`
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



class ProtocolMetadata(Model):
    """ProtocolMetadata.

    :param data:
    :type data: object
    :param schema_version:
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



class RecycleBinPackageVersion(PackageVersion):
    """RecycleBinPackageVersion.

    :param direct_upstream_source_id:
    :type direct_upstream_source_id: str
    :param id:
    :type id: str
    :param is_cached_version:
    :type is_cached_version: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_latest:
    :type is_latest: bool
    :param is_listed:
    :type is_listed: bool
    :param normalized_version: The normalized version representing the identity of a package version
    :type normalized_version: str
    :param package_description:
    :type package_description: str
    :param publish_date:
    :type publish_date: datetime
    :param storage_id:
    :type storage_id: str
    :param version: The display version of the package version
    :type version: str
    :param views:
    :type views: list of :class:`FeedView <packaging.v4_1.models.FeedView>`
    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param author:
    :type author: str
    :param deleted_date:
    :type deleted_date: datetime
    :param dependencies:
    :type dependencies: list of :class:`PackageDependency <packaging.v4_1.models.PackageDependency>`
    :param description:
    :type description: str
    :param files:
    :type files: list of :class:`PackageFile <packaging.v4_1.models.PackageFile>`
    :param other_versions:
    :type other_versions: list of :class:`MinimalPackageVersion <packaging.v4_1.models.MinimalPackageVersion>`
    :param protocol_metadata:
    :type protocol_metadata: :class:`ProtocolMetadata <packaging.v4_1.models.ProtocolMetadata>`
    :param source_chain:
    :type source_chain: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
    :param summary:
    :type summary: str
    :param tags:
    :type tags: list of str
    :param url:
    :type url: str
    :param scheduled_permanent_delete_date:
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

    :param deleted_date:
    :type deleted_date: datetime
    :param id:
    :type id: str
    :param internal_upstream_collection_id:
    :type internal_upstream_collection_id: str
    :param internal_upstream_feed_id:
    :type internal_upstream_feed_id: str
    :param internal_upstream_view_id:
    :type internal_upstream_view_id: str
    :param location:
    :type location: str
    :param name:
    :type name: str
    :param protocol:
    :type protocol: str
    :param upstream_source_type:
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

    :param allow_upstream_name_conflict: If set, the feed will allow upload of packages that exist on the upstream
    :type allow_upstream_name_conflict: bool
    :param capabilities:
    :type capabilities: object
    :param fully_qualified_id:
    :type fully_qualified_id: str
    :param fully_qualified_name:
    :type fully_qualified_name: str
    :param id:
    :type id: str
    :param is_read_only:
    :type is_read_only: bool
    :param name:
    :type name: str
    :param upstream_enabled: If set, the feed can proxy packages from an upstream feed
    :type upstream_enabled: bool
    :param upstream_sources: External assemblies should use the extension methods to get the sources for a specific protocol.
    :type upstream_sources: list of :class:`UpstreamSource <packaging.v4_1.models.UpstreamSource>`
    :param view:
    :type view: :class:`FeedView <packaging.v4_1.models.FeedView>`
    :param view_id:
    :type view_id: str
    :param view_name:
    :type view_name: str
    :param _links:
    :type _links: :class:`ReferenceLinks <packaging.v4_1.models.ReferenceLinks>`
    :param badges_enabled:
    :type badges_enabled: bool
    :param default_view_id:
    :type default_view_id: str
    :param deleted_date:
    :type deleted_date: datetime
    :param description:
    :type description: str
    :param hide_deleted_package_versions: If set, feed will hide all deleted/unpublished versions
    :type hide_deleted_package_versions: bool
    :param permissions:
    :type permissions: list of :class:`FeedPermission <packaging.v4_1.models.FeedPermission>`
    :param upstream_enabled_changed_date: If set, time that the UpstreamEnabled property was changed. Will be null if UpstreamEnabled was never changed after Feed creation.
    :type upstream_enabled_changed_date: datetime
    :param url:
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

    def __init__(self, allow_upstream_name_conflict=None, capabilities=None, fully_qualified_id=None, fully_qualified_name=None, id=None, is_read_only=None, name=None, upstream_enabled=None, upstream_sources=None, view=None, view_id=None, view_name=None, _links=None, badges_enabled=None, default_view_id=None, deleted_date=None, description=None, hide_deleted_package_versions=None, permissions=None, upstream_enabled_changed_date=None, url=None):
        super(Feed, self).__init__(allow_upstream_name_conflict=allow_upstream_name_conflict, capabilities=capabilities, fully_qualified_id=fully_qualified_id, fully_qualified_name=fully_qualified_name, id=id, is_read_only=is_read_only, name=name, upstream_enabled=upstream_enabled, upstream_sources=upstream_sources, view=view, view_id=view_id, view_name=view_name)
        self._links = _links
        self.badges_enabled = badges_enabled
        self.default_view_id = default_view_id
        self.deleted_date = deleted_date
        self.description = description
        self.hide_deleted_package_versions = hide_deleted_package_versions
        self.permissions = permissions
        self.upstream_enabled_changed_date = upstream_enabled_changed_date
        self.url = url
