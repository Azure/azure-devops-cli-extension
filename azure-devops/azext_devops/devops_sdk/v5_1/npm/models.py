﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BatchOperationData(Model):
    """
    Do not attempt to use this type to create a new BatchOperationData. This type does not contain sufficient fields to create a new batch operation data.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(BatchOperationData, self).__init__()


class JsonPatchOperation(Model):
    """
    The JSON model for a JSON Patch operation

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


class MinimalPackageDetails(Model):
    """
    Minimal package details required to identify a package within a protocol.

    :param id: Package name.
    :type id: str
    :param version: Package version.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, version=None):
        super(MinimalPackageDetails, self).__init__()
        self.id = id
        self.version = version


class NpmPackagesBatchRequest(Model):
    """
    A batch of operations to apply to package versions.

    :param data: Data required to perform the operation. This is optional based on type of operation. Use BatchPromoteData if performing a promote operation.
    :type data: :class:`BatchOperationData <azure.devops.v5_1.npm.models.BatchOperationData>`
    :param operation: Type of operation that needs to be performed on packages.
    :type operation: object
    :param packages: The packages onto which the operation will be performed.
    :type packages: list of :class:`MinimalPackageDetails <azure.devops.v5_1.npm.models.MinimalPackageDetails>`
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(NpmPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class NpmPackageVersionDeletionState(Model):
    """
    Deletion state of an npm package.

    :param name: Name of the package.
    :type name: str
    :param unpublished_date: UTC date the package was unpublished.
    :type unpublished_date: datetime
    :param version: Version of the package.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'unpublished_date': {'key': 'unpublishedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, name=None, unpublished_date=None, version=None):
        super(NpmPackageVersionDeletionState, self).__init__()
        self.name = name
        self.unpublished_date = unpublished_date
        self.version = version


class NpmRecycleBinPackageVersionDetails(Model):
    """
    :param deleted: Setting to false will undo earlier deletion and restore the package to feed.
    :type deleted: bool
    """

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(NpmRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class Package(Model):
    """
    Package version metadata for an npm package

    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.npm.models.ReferenceLinks>`
    :param deprecate_message: Deprecated message, if any, for the package.
    :type deprecate_message: str
    :param id: Package Id.
    :type id: str
    :param name: The display name of the package.
    :type name: str
    :param permanently_deleted_date: If and when the package was permanently deleted.
    :type permanently_deleted_date: datetime
    :param source_chain: The history of upstream sources for this package. The first source in the list is the immediate source from which this package was saved.
    :type source_chain: list of :class:`UpstreamSourceInfo <azure.devops.v5_1.npm.models.UpstreamSourceInfo>`
    :param unpublished_date: If and when the package was deleted.
    :type unpublished_date: datetime
    :param version: The version of the package.
    :type version: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deprecate_message': {'key': 'deprecateMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSourceInfo]'},
        'unpublished_date': {'key': 'unpublishedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deprecate_message=None, id=None, name=None, permanently_deleted_date=None, source_chain=None, unpublished_date=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deprecate_message = deprecate_message
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.source_chain = source_chain
        self.unpublished_date = unpublished_date
        self.version = version


class PackageVersionDetails(Model):
    """
    :param deprecate_message: Indicates the deprecate message of a package version
    :type deprecate_message: str
    :param views: The view to which the package version will be added
    :type views: :class:`JsonPatchOperation <azure.devops.v5_1.npm.models.JsonPatchOperation>`
    """

    _attribute_map = {
        'deprecate_message': {'key': 'deprecateMessage', 'type': 'str'},
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, deprecate_message=None, views=None):
        super(PackageVersionDetails, self).__init__()
        self.deprecate_message = deprecate_message
        self.views = views


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpstreamSourceInfo(Model):
    """
    Upstream source definition, including its Identity, package type, and other associated information.

    :param display_location: Locator for connecting to the upstream source in a user friendly format, that may potentially change over time
    :type display_location: str
    :param id: Identity of the upstream source.
    :type id: str
    :param location: Locator for connecting to the upstream source
    :type location: str
    :param name: Display name.
    :type name: str
    :param source_type: Source type, such as Public or Internal.
    :type source_type: object
    """

    _attribute_map = {
        'display_location': {'key': 'displayLocation', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source_type': {'key': 'sourceType', 'type': 'object'}
    }

    def __init__(self, display_location=None, id=None, location=None, name=None, source_type=None):
        super(UpstreamSourceInfo, self).__init__()
        self.display_location = display_location
        self.id = id
        self.location = location
        self.name = name
        self.source_type = source_type


class BatchDeprecateData(BatchOperationData):
    """
    Data required to deprecate multiple package versions. Pass this while performing NpmBatchOperationTypes.Deprecate batch operation.

    :param message: Deprecate message that will be added to packages
    :type message: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(BatchDeprecateData, self).__init__()
        self.message = message


__all__ = [
    'BatchOperationData',
    'JsonPatchOperation',
    'MinimalPackageDetails',
    'NpmPackagesBatchRequest',
    'NpmPackageVersionDeletionState',
    'NpmRecycleBinPackageVersionDetails',
    'Package',
    'PackageVersionDetails',
    'ReferenceLinks',
    'UpstreamSourceInfo',
    'BatchDeprecateData',
]
