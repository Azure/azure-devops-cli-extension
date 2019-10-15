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
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class IdentityBase(Model):
    """
    Base Identity class to allow "trimmed" identity class in the GetConnectionData API Makes sure that on-the-wire representations of the derived classes are compatible with each other (e.g. Server responds with PublicIdentity object while client deserializes it as Identity object) Derived classes should not have additional [DataMember] properties

    :param custom_display_name: The custom display name for the identity (if any). Setting this property to an empty string will clear the existing custom display name. Setting this property to null will not affect the existing persisted value (since null values do not get sent over the wire or to the database)
    :type custom_display_name: str
    :param descriptor:
    :type descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param id:
    :type id: str
    :param is_active:
    :type is_active: bool
    :param is_container:
    :type is_container: bool
    :param master_id:
    :type master_id: str
    :param member_ids:
    :type member_ids: list of str
    :param member_of:
    :type member_of: list of :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param members:
    :type members: list of :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param meta_type_id:
    :type meta_type_id: int
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.object>`
    :param provider_display_name: The display name for the identity as specified by the source identity provider.
    :type provider_display_name: str
    :param resource_version:
    :type resource_version: int
    :param social_descriptor:
    :type social_descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param subject_descriptor:
    :type subject_descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param unique_user_id:
    :type unique_user_id: int
    """

    _attribute_map = {
        'custom_display_name': {'key': 'customDisplayName', 'type': 'str'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'master_id': {'key': 'masterId', 'type': 'str'},
        'member_ids': {'key': 'memberIds', 'type': '[str]'},
        'member_of': {'key': 'memberOf', 'type': '[str]'},
        'members': {'key': 'members', 'type': '[str]'},
        'meta_type_id': {'key': 'metaTypeId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'provider_display_name': {'key': 'providerDisplayName', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'social_descriptor': {'key': 'socialDescriptor', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'}
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, social_descriptor=None, subject_descriptor=None, unique_user_id=None):
        super(IdentityBase, self).__init__()
        self.custom_display_name = custom_display_name
        self.descriptor = descriptor
        self.id = id
        self.is_active = is_active
        self.is_container = is_container
        self.master_id = master_id
        self.member_ids = member_ids
        self.member_of = member_of
        self.members = members
        self.meta_type_id = meta_type_id
        self.properties = properties
        self.provider_display_name = provider_display_name
        self.resource_version = resource_version
        self.social_descriptor = social_descriptor
        self.subject_descriptor = subject_descriptor
        self.unique_user_id = unique_user_id


class IdentityData(Model):
    """
    :param identity_ids:
    :type identity_ids: list of str
    """

    _attribute_map = {
        'identity_ids': {'key': 'identityIds', 'type': '[str]'}
    }

    def __init__(self, identity_ids=None):
        super(IdentityData, self).__init__()
        self.identity_ids = identity_ids


class IdentityRef(GraphSubjectBase):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class OperationReference(Model):
    """
    Reference for an async operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class ProcessReference(Model):
    """
    :param name:
    :type name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(ProcessReference, self).__init__()
        self.name = name
        self.url = url


class ProjectAvatar(Model):
    """
    Contains the image data for project avatar.

    :param image: The avatar image represented as a byte array.
    :type image: str
    """

    _attribute_map = {
        'image': {'key': 'image', 'type': 'str'}
    }

    def __init__(self, image=None):
        super(ProjectAvatar, self).__init__()
        self.image = image


class ProjectInfo(Model):
    """
    Contains information describing a project.

    :param abbreviation: The abbreviated name of the project.
    :type abbreviation: str
    :param description: The description of the project.
    :type description: str
    :param id: The id of the project.
    :type id: str
    :param last_update_time: The time that this project was last updated.
    :type last_update_time: datetime
    :param name: The name of the project.
    :type name: str
    :param properties: A set of name-value pairs storing additional property data related to the project.
    :type properties: list of :class:`ProjectProperty <azure.devops.v5_1.core.models.ProjectProperty>`
    :param revision: The current revision of the project.
    :type revision: long
    :param state: The current state of the project.
    :type state: object
    :param uri: A Uri that can be used to refer to this project.
    :type uri: str
    :param version: The version number of the project.
    :type version: long
    :param visibility: Indicates whom the project is visible to.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[ProjectProperty]'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, last_update_time=None, name=None, properties=None, revision=None, state=None, uri=None, version=None, visibility=None):
        super(ProjectInfo, self).__init__()
        self.abbreviation = abbreviation
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.properties = properties
        self.revision = revision
        self.state = state
        self.uri = uri
        self.version = version
        self.visibility = visibility


class ProjectProperties(Model):
    """
    :param project_id: The team project Id
    :type project_id: str
    :param properties: The collection of team project properties
    :type properties: list of :class:`ProjectProperty <azure.devops.v5_1.core.models.ProjectProperty>`
    """

    _attribute_map = {
        'project_id': {'key': 'projectId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[ProjectProperty]'}
    }

    def __init__(self, project_id=None, properties=None):
        super(ProjectProperties, self).__init__()
        self.project_id = project_id
        self.properties = properties


class ProjectProperty(Model):
    """
    A named value associated with a project.

    :param name: The name of the property.
    :type name: str
    :param value: The value of the property.
    :type value: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, name=None, value=None):
        super(ProjectProperty, self).__init__()
        self.name = name
        self.value = value


class Proxy(Model):
    """
    :param authorization:
    :type authorization: :class:`ProxyAuthorization <azure.devops.v5_1.core.models.ProxyAuthorization>`
    :param description: This is a description string
    :type description: str
    :param friendly_name: The friendly name of the server
    :type friendly_name: str
    :param global_default:
    :type global_default: bool
    :param site: This is a string representation of the site that the proxy server is located in (e.g. "NA-WA-RED")
    :type site: str
    :param site_default:
    :type site_default: bool
    :param url: The URL of the proxy server
    :type url: str
    """

    _attribute_map = {
        'authorization': {'key': 'authorization', 'type': 'ProxyAuthorization'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'global_default': {'key': 'globalDefault', 'type': 'bool'},
        'site': {'key': 'site', 'type': 'str'},
        'site_default': {'key': 'siteDefault', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, authorization=None, description=None, friendly_name=None, global_default=None, site=None, site_default=None, url=None):
        super(Proxy, self).__init__()
        self.authorization = authorization
        self.description = description
        self.friendly_name = friendly_name
        self.global_default = global_default
        self.site = site
        self.site_default = site_default
        self.url = url


class ProxyAuthorization(Model):
    """
    :param authorization_url: Gets or sets the endpoint used to obtain access tokens from the configured token service.
    :type authorization_url: str
    :param client_id: Gets or sets the client identifier for this proxy.
    :type client_id: str
    :param identity: Gets or sets the user identity to authorize for on-prem.
    :type identity: :class:`str <azure.devops.v5_1.core.models.str>`
    :param public_key: Gets or sets the public key used to verify the identity of this proxy. Only specify on hosted.
    :type public_key: :class:`PublicKey <azure.devops.v5_1.core.models.PublicKey>`
    """

    _attribute_map = {
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'str'},
        'public_key': {'key': 'publicKey', 'type': 'PublicKey'}
    }

    def __init__(self, authorization_url=None, client_id=None, identity=None, public_key=None):
        super(ProxyAuthorization, self).__init__()
        self.authorization_url = authorization_url
        self.client_id = client_id
        self.identity = identity
        self.public_key = public_key


class PublicKey(Model):
    """
    Represents the public key portion of an RSA asymmetric key.

    :param exponent: Gets or sets the exponent for the public key.
    :type exponent: str
    :param modulus: Gets or sets the modulus for the public key.
    :type modulus: str
    """

    _attribute_map = {
        'exponent': {'key': 'exponent', 'type': 'str'},
        'modulus': {'key': 'modulus', 'type': 'str'}
    }

    def __init__(self, exponent=None, modulus=None):
        super(PublicKey, self).__init__()
        self.exponent = exponent
        self.modulus = modulus


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


class TeamMember(Model):
    """
    :param identity:
    :type identity: :class:`IdentityRef <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.IdentityRef>`
    :param is_team_admin:
    :type is_team_admin: bool
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'IdentityRef'},
        'is_team_admin': {'key': 'isTeamAdmin', 'type': 'bool'}
    }

    def __init__(self, identity=None, is_team_admin=None):
        super(TeamMember, self).__init__()
        self.identity = identity
        self.is_team_admin = is_team_admin


class TeamProjectCollectionReference(Model):
    """
    Reference object for a TeamProjectCollection.

    :param id: Collection Id.
    :type id: str
    :param name: Collection Name.
    :type name: str
    :param url: Collection REST Url.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(TeamProjectCollectionReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class TeamProjectReference(Model):
    """
    Represents a shallow reference to a TeamProject.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class WebApiConnectedServiceRef(Model):
    """
    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WebApiConnectedServiceRef, self).__init__()
        self.id = id
        self.url = url


class WebApiTeamRef(Model):
    """
    :param id: Team (Identity) Guid. A Team Foundation ID.
    :type id: str
    :param name: Team name
    :type name: str
    :param url: Team REST API Url
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WebApiTeamRef, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class Identity(IdentityBase):
    """
    :param custom_display_name: The custom display name for the identity (if any). Setting this property to an empty string will clear the existing custom display name. Setting this property to null will not affect the existing persisted value (since null values do not get sent over the wire or to the database)
    :type custom_display_name: str
    :param descriptor:
    :type descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param id:
    :type id: str
    :param is_active:
    :type is_active: bool
    :param is_container:
    :type is_container: bool
    :param master_id:
    :type master_id: str
    :param member_ids:
    :type member_ids: list of str
    :param member_of:
    :type member_of: list of :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param members:
    :type members: list of :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param meta_type_id:
    :type meta_type_id: int
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.object>`
    :param provider_display_name: The display name for the identity as specified by the source identity provider.
    :type provider_display_name: str
    :param resource_version:
    :type resource_version: int
    :param social_descriptor:
    :type social_descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param subject_descriptor:
    :type subject_descriptor: :class:`str <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.str>`
    :param unique_user_id:
    :type unique_user_id: int
    """

    _attribute_map = {
        'custom_display_name': {'key': 'customDisplayName', 'type': 'str'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'master_id': {'key': 'masterId', 'type': 'str'},
        'member_ids': {'key': 'memberIds', 'type': '[str]'},
        'member_of': {'key': 'memberOf', 'type': '[str]'},
        'members': {'key': 'members', 'type': '[str]'},
        'meta_type_id': {'key': 'metaTypeId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'provider_display_name': {'key': 'providerDisplayName', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'social_descriptor': {'key': 'socialDescriptor', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'},
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, social_descriptor=None, subject_descriptor=None, unique_user_id=None):
        super(Identity, self).__init__(custom_display_name=custom_display_name, descriptor=descriptor, id=id, is_active=is_active, is_container=is_container, master_id=master_id, member_ids=member_ids, member_of=member_of, members=members, meta_type_id=meta_type_id, properties=properties, provider_display_name=provider_display_name, resource_version=resource_version, social_descriptor=social_descriptor, subject_descriptor=subject_descriptor, unique_user_id=unique_user_id)


class Process(ProcessReference):
    """
    :param name:
    :type name: str
    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.core.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param is_default:
    :type is_default: bool
    :param type:
    :type type: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, name=None, url=None, _links=None, description=None, id=None, is_default=None, type=None):
        super(Process, self).__init__(name=name, url=url)
        self._links = _links
        self.description = description
        self.id = id
        self.is_default = is_default
        self.type = type


class TeamProject(TeamProjectReference):
    """
    Represents a Team Project object.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.core.models.ReferenceLinks>`
    :param capabilities: Set of capabilities this project has (such as process template & version control).
    :type capabilities: dict
    :param default_team: The shallow ref to the default team.
    :type default_team: :class:`WebApiTeamRef <azure.devops.v5_1.core.models.WebApiTeamRef>`
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, default_team_image_url=default_team_image_url, description=description, id=id, last_update_time=last_update_time, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team


class TeamProjectCollection(TeamProjectCollectionReference):
    """
    Data contract for a TeamProjectCollection.

    :param id: Collection Id.
    :type id: str
    :param name: Collection Name.
    :type name: str
    :param url: Collection REST Url.
    :type url: str
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.core.models.ReferenceLinks>`
    :param description: Project collection description.
    :type description: str
    :param process_customization_type: Process customization type on this collection. It can be Xml or Inherited.
    :type process_customization_type: object
    :param state: Project collection state.
    :type state: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'process_customization_type': {'key': 'processCustomizationType', 'type': 'object'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, description=None, process_customization_type=None, state=None):
        super(TeamProjectCollection, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.description = description
        self.process_customization_type = process_customization_type
        self.state = state


class WebApiConnectedService(WebApiConnectedServiceRef):
    """
    :param url:
    :type url: str
    :param authenticated_by: The user who did the OAuth authentication to created this service
    :type authenticated_by: :class:`IdentityRef <azure.devops.v5_1.core.models.IdentityRef>`
    :param description: Extra description on the service.
    :type description: str
    :param friendly_name: Friendly Name of service connection
    :type friendly_name: str
    :param id: Id/Name of the connection service. For Ex: Subscription Id for Azure Connection
    :type id: str
    :param kind: The kind of service.
    :type kind: str
    :param project: The project associated with this service
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.core.models.TeamProjectReference>`
    :param service_uri: Optional uri to connect directly to the service such as https://windows.azure.com
    :type service_uri: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'authenticated_by': {'key': 'authenticatedBy', 'type': 'IdentityRef'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'}
    }

    def __init__(self, url=None, authenticated_by=None, description=None, friendly_name=None, id=None, kind=None, project=None, service_uri=None):
        super(WebApiConnectedService, self).__init__(url=url)
        self.authenticated_by = authenticated_by
        self.description = description
        self.friendly_name = friendly_name
        self.id = id
        self.kind = kind
        self.project = project
        self.service_uri = service_uri


class WebApiConnectedServiceDetails(WebApiConnectedServiceRef):
    """
    :param id:
    :type id: str
    :param url:
    :type url: str
    :param connected_service_meta_data: Meta data for service connection
    :type connected_service_meta_data: :class:`WebApiConnectedService <azure.devops.v5_1.core.models.WebApiConnectedService>`
    :param credentials_xml: Credential info
    :type credentials_xml: str
    :param end_point: Optional uri to connect directly to the service such as https://windows.azure.com
    :type end_point: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'connected_service_meta_data': {'key': 'connectedServiceMetaData', 'type': 'WebApiConnectedService'},
        'credentials_xml': {'key': 'credentialsXml', 'type': 'str'},
        'end_point': {'key': 'endPoint', 'type': 'str'}
    }

    def __init__(self, id=None, url=None, connected_service_meta_data=None, credentials_xml=None, end_point=None):
        super(WebApiConnectedServiceDetails, self).__init__(id=id, url=url)
        self.connected_service_meta_data = connected_service_meta_data
        self.credentials_xml = credentials_xml
        self.end_point = end_point


class WebApiTeam(WebApiTeamRef):
    """
    :param id: Team (Identity) Guid. A Team Foundation ID.
    :type id: str
    :param name: Team name
    :type name: str
    :param url: Team REST API Url
    :type url: str
    :param description: Team description
    :type description: str
    :param identity: Team identity.
    :type identity: :class:`Identity <azure.devops.v5_1.core.models.Identity>`
    :param identity_url: Identity REST API Url to this team
    :type identity_url: str
    :param project_id:
    :type project_id: str
    :param project_name:
    :type project_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'identity_url': {'key': 'identityUrl', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'project_name': {'key': 'projectName', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, description=None, identity=None, identity_url=None, project_id=None, project_name=None):
        super(WebApiTeam, self).__init__(id=id, name=name, url=url)
        self.description = description
        self.identity = identity
        self.identity_url = identity_url
        self.project_id = project_id
        self.project_name = project_name


__all__ = [
    'GraphSubjectBase',
    'IdentityBase',
    'IdentityData',
    'IdentityRef',
    'JsonPatchOperation',
    'OperationReference',
    'ProcessReference',
    'ProjectAvatar',
    'ProjectInfo',
    'ProjectProperties',
    'ProjectProperty',
    'Proxy',
    'ProxyAuthorization',
    'PublicKey',
    'ReferenceLinks',
    'TeamMember',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'WebApiConnectedServiceRef',
    'WebApiTeamRef',
    'Identity',
    'Process',
    'TeamProject',
    'TeamProjectCollection',
    'WebApiConnectedService',
    'WebApiConnectedServiceDetails',
    'WebApiTeam',
]
