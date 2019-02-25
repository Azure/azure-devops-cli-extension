# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class IdentityData(Model):
    """IdentityData.

    :param identity_ids:
    :type identity_ids: list of str
    """

    _attribute_map = {
        'identity_ids': {'key': 'identityIds', 'type': '[str]'}
    }

    def __init__(self, identity_ids=None):
        super(IdentityData, self).__init__()
        self.identity_ids = identity_ids



class IdentityRef(Model):
    """IdentityRef.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None):
        super(IdentityRef, self).__init__()
        self.directory_alias = directory_alias
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.profile_url = profile_url
        self.unique_name = unique_name
        self.url = url



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



class OperationReference(Model):
    """OperationReference.

    :param id: The identifier for this operation.
    :type id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: Url to get the full object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.status = status
        self.url = url



class ProcessReference(Model):
    """ProcessReference.

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



class ProjectInfo(Model):
    """ProjectInfo.

    :param abbreviation:
    :type abbreviation: str
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param last_update_time:
    :type last_update_time: datetime
    :param name:
    :type name: str
    :param properties:
    :type properties: list of :class:`ProjectProperty <core.v4_0.models.ProjectProperty>`
    :param revision: Current revision of the project
    :type revision: long
    :param state:
    :type state: object
    :param uri:
    :type uri: str
    :param version:
    :type version: long
    :param visibility:
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



class ProjectProperty(Model):
    """ProjectProperty.

    :param name:
    :type name: str
    :param value:
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
    """Proxy.

    :param authorization:
    :type authorization: :class:`ProxyAuthorization <core.v4_0.models.ProxyAuthorization>`
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
    """ProxyAuthorization.

    :param authorization_url: Gets or sets the endpoint used to obtain access tokens from the configured token service.
    :type authorization_url: str
    :param client_id: Gets or sets the client identifier for this proxy.
    :type client_id: str
    :param identity: Gets or sets the user identity to authorize for on-prem.
    :type identity: :class:`str <core.v4_0.models.str>`
    :param public_key: Gets or sets the public key used to verify the identity of this proxy. Only specify on hosted.
    :type public_key: :class:`PublicKey <core.v4_0.models.PublicKey>`
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
    """PublicKey.

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



class TeamProjectCollectionReference(Model):
    """TeamProjectCollectionReference.

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
    """TeamProjectReference.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
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
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.description = description
        self.id = id
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility



class WebApiConnectedServiceRef(Model):
    """WebApiConnectedServiceRef.

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
    """WebApiTeamRef.

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



class Process(ProcessReference):
    """Process.

    :param name:
    :type name: str
    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <core.v4_0.models.ReferenceLinks>`
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
    """TeamProject.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
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
    :type _links: :class:`ReferenceLinks <core.v4_0.models.ReferenceLinks>`
    :param capabilities: Set of capabilities this project has (such as process template & version control).
    :type capabilities: dict
    :param default_team: The shallow ref to the default team.
    :type default_team: :class:`WebApiTeamRef <core.v4_0.models.WebApiTeamRef>`
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, description=description, id=id, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team



class TeamProjectCollection(TeamProjectCollectionReference):
    """TeamProjectCollection.

    :param id: Collection Id.
    :type id: str
    :param name: Collection Name.
    :type name: str
    :param url: Collection REST Url.
    :type url: str
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <core.v4_0.models.ReferenceLinks>`
    :param description: Project collection description.
    :type description: str
    :param state: Project collection state.
    :type state: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, description=None, state=None):
        super(TeamProjectCollection, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.description = description
        self.state = state



class WebApiConnectedService(WebApiConnectedServiceRef):
    """WebApiConnectedService.

    :param url:
    :type url: str
    :param authenticated_by: The user who did the OAuth authentication to created this service
    :type authenticated_by: :class:`IdentityRef <core.v4_0.models.IdentityRef>`
    :param description: Extra description on the service.
    :type description: str
    :param friendly_name: Friendly Name of service connection
    :type friendly_name: str
    :param id: Id/Name of the connection service. For Ex: Subscription Id for Azure Connection
    :type id: str
    :param kind: The kind of service.
    :type kind: str
    :param project: The project associated with this service
    :type project: :class:`TeamProjectReference <core.v4_0.models.TeamProjectReference>`
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
    """WebApiConnectedServiceDetails.

    :param id:
    :type id: str
    :param url:
    :type url: str
    :param connected_service_meta_data: Meta data for service connection
    :type connected_service_meta_data: :class:`WebApiConnectedService <core.v4_0.models.WebApiConnectedService>`
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
    """WebApiTeam.

    :param id: Team (Identity) Guid. A Team Foundation ID.
    :type id: str
    :param name: Team name
    :type name: str
    :param url: Team REST API Url
    :type url: str
    :param description: Team description
    :type description: str
    :param identity_url: Identity REST API Url to this team
    :type identity_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'identity_url': {'key': 'identityUrl', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, description=None, identity_url=None):
        super(WebApiTeam, self).__init__(id=id, name=name, url=url)
        self.description = description
        self.identity_url = identity_url
