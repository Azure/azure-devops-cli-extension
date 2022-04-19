# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class Permission(Model):
    """
    :param authorized:
    :type authorized: bool
    :param authorized_by:
    :type authorized_by: :class:`IdentityRef <azure.devops.v6_0.pipeline_permissions.models.IdentityRef>`
    :param authorized_on:
    :type authorized_on: datetime
    """

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'authorized_by': {'key': 'authorizedBy', 'type': 'IdentityRef'},
        'authorized_on': {'key': 'authorizedOn', 'type': 'iso-8601'}
    }

    def __init__(self, authorized=None, authorized_by=None, authorized_on=None):
        super(Permission, self).__init__()
        self.authorized = authorized
        self.authorized_by = authorized_by
        self.authorized_on = authorized_on


class PipelinePermission(Permission):
    """
    :param authorized:
    :type authorized: bool
    :param authorized_by:
    :type authorized_by: :class:`IdentityRef <azure.devops.v6_0.pipeline_permissions.models.IdentityRef>`
    :param authorized_on:
    :type authorized_on: datetime
    :param id:
    :type id: int
    """

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'authorized_by': {'key': 'authorizedBy', 'type': 'IdentityRef'},
        'authorized_on': {'key': 'authorizedOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, authorized=None, authorized_by=None, authorized_on=None, id=None):
        super(PipelinePermission, self).__init__(authorized=authorized, authorized_by=authorized_by, authorized_on=authorized_on)
        self.id = id


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


class Resource(Model):
    """
    :param id: Id of the resource.
    :type id: str
    :param name: Name of the resource.
    :type name: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(Resource, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class ResourcePipelinePermissions(Model):
    """
    :param all_pipelines:
    :type all_pipelines: :class:`Permission <azure.devops.v6_0.pipeline_permissions.models.Permission>`
    :param pipelines:
    :type pipelines: list of :class:`PipelinePermission <azure.devops.v6_0.pipeline_permissions.models.PipelinePermission>`
    :param resource:
    :type resource: :class:`Resource <azure.devops.v6_0.pipeline_permissions.models.Resource>`
    """

    _attribute_map = {
        'all_pipelines': {'key': 'allPipelines', 'type': 'Permission'},
        'pipelines': {'key': 'pipelines', 'type': '[PipelinePermission]'},
        'resource': {'key': 'resource', 'type': 'Resource'}
    }

    def __init__(self, all_pipelines=None, pipelines=None, resource=None):
        super(ResourcePipelinePermissions, self).__init__()
        self.all_pipelines = all_pipelines
        self.pipelines = pipelines
        self.resource = resource


__all__ = [
    'GraphSubjectBase',
    'IdentityRef',
    'Permission',
    'PipelinePermission',
    'ReferenceLinks',
    'Resource',
    'ResourcePipelinePermissions',
]
