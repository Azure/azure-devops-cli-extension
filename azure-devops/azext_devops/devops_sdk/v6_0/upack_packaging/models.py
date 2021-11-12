# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UPackLimitedPackageMetadata(Model):
    """
    :param version:
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(UPackLimitedPackageMetadata, self).__init__()
        self.version = version


class UPackLimitedPackageMetadataListResponse(Model):
    """
    :param count:
    :type count: int
    :param value:
    :type value: list of :class:`UPackLimitedPackageMetadata <azure.devops.v6_0.upack.models.UPackLimitedPackageMetadata>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'value': {'key': 'value', 'type': '[UPackLimitedPackageMetadata]'}
    }

    def __init__(self, count=None, value=None):
        super(UPackLimitedPackageMetadataListResponse, self).__init__()
        self.count = count
        self.value = value


class UPackPackageMetadata(Model):
    """
    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    :param super_root_id:
    :type super_root_id: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, description=None, manifest_id=None, super_root_id=None, version=None):
        super(UPackPackageMetadata, self).__init__()
        self.description = description
        self.manifest_id = manifest_id
        self.super_root_id = super_root_id
        self.version = version


class UPackPackagePushMetadata(UPackPackageMetadata):
    """
    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    :param super_root_id:
    :type super_root_id: str
    :param version:
    :type version: str
    :param proof_nodes:
    :type proof_nodes: list of str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'proof_nodes': {'key': 'proofNodes', 'type': '[str]'}
    }

    def __init__(self, description=None, manifest_id=None, super_root_id=None, version=None, proof_nodes=None):
        super(UPackPackagePushMetadata, self).__init__(description=description, manifest_id=manifest_id, super_root_id=super_root_id, version=version)
        self.proof_nodes = proof_nodes


class UPackPackageVersionDeletionState(Model):
    """
    Deletion state of a Universal package.

    :param deleted_date: UTC date the package was deleted.
    :type deleted_date: datetime
    :param name: Name of the package.
    :type name: str
    :param version: Version of the package.
    :type version: str
    """

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(UPackPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


__all__ = [
    'UPackLimitedPackageMetadata',
    'UPackLimitedPackageMetadataListResponse',
    'UPackPackageMetadata',
    'UPackPackagePushMetadata',
    'UPackPackageVersionDeletionState',
]
