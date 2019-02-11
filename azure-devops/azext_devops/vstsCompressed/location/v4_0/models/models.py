# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AccessMapping(Model):
    """AccessMapping.

    :param access_point:
    :type access_point: str
    :param display_name:
    :type display_name: str
    :param moniker:
    :type moniker: str
    :param service_owner: The service which owns this access mapping e.g. TFS, ELS, etc.
    :type service_owner: str
    :param virtual_directory: Part of the access mapping which applies context after the access point of the server.
    :type virtual_directory: str
    """

    _attribute_map = {
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'moniker': {'key': 'moniker', 'type': 'str'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'virtual_directory': {'key': 'virtualDirectory', 'type': 'str'}
    }

    def __init__(self, access_point=None, display_name=None, moniker=None, service_owner=None, virtual_directory=None):
        super(AccessMapping, self).__init__()
        self.access_point = access_point
        self.display_name = display_name
        self.moniker = moniker
        self.service_owner = service_owner
        self.virtual_directory = virtual_directory



class ConnectionData(Model):
    """ConnectionData.

    :param authenticated_user: The Id of the authenticated user who made this request. More information about the user can be obtained by passing this Id to the Identity service
    :type authenticated_user: :class:`Identity <locations.v4_0.models.Identity>`
    :param authorized_user: The Id of the authorized user who made this request. More information about the user can be obtained by passing this Id to the Identity service
    :type authorized_user: :class:`Identity <locations.v4_0.models.Identity>`
    :param deployment_id: The id for the server.
    :type deployment_id: str
    :param instance_id: The instance id for this host.
    :type instance_id: str
    :param last_user_access: The last user access for this instance.  Null if not requested specifically.
    :type last_user_access: datetime
    :param location_service_data: Data that the location service holds.
    :type location_service_data: :class:`LocationServiceData <locations.v4_0.models.LocationServiceData>`
    :param web_application_relative_directory: The virtual directory of the host we are talking to.
    :type web_application_relative_directory: str
    """

    _attribute_map = {
        'authenticated_user': {'key': 'authenticatedUser', 'type': 'Identity'},
        'authorized_user': {'key': 'authorizedUser', 'type': 'Identity'},
        'deployment_id': {'key': 'deploymentId', 'type': 'str'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
        'last_user_access': {'key': 'lastUserAccess', 'type': 'iso-8601'},
        'location_service_data': {'key': 'locationServiceData', 'type': 'LocationServiceData'},
        'web_application_relative_directory': {'key': 'webApplicationRelativeDirectory', 'type': 'str'}
    }

    def __init__(self, authenticated_user=None, authorized_user=None, deployment_id=None, instance_id=None, last_user_access=None, location_service_data=None, web_application_relative_directory=None):
        super(ConnectionData, self).__init__()
        self.authenticated_user = authenticated_user
        self.authorized_user = authorized_user
        self.deployment_id = deployment_id
        self.instance_id = instance_id
        self.last_user_access = last_user_access
        self.location_service_data = location_service_data
        self.web_application_relative_directory = web_application_relative_directory



class Identity(Model):
    """Identity.

    :param custom_display_name: The custom display name for the identity (if any). Setting this property to an empty string will clear the existing custom display name. Setting this property to null will not affect the existing persisted value (since null values do not get sent over the wire or to the database)
    :type custom_display_name: str
    :param descriptor:
    :type descriptor: :class:`str <microsoft.-visual-studio.-services.-web-api.v4_0.models.str>`
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
    :type member_of: list of :class:`str <microsoft.-visual-studio.-services.-web-api.v4_0.models.str>`
    :param members:
    :type members: list of :class:`str <microsoft.-visual-studio.-services.-web-api.v4_0.models.str>`
    :param meta_type_id:
    :type meta_type_id: int
    :param properties:
    :type properties: :class:`object <microsoft.-visual-studio.-services.-web-api.v4_0.models.object>`
    :param provider_display_name: The display name for the identity as specified by the source identity provider.
    :type provider_display_name: str
    :param resource_version:
    :type resource_version: int
    :param subject_descriptor:
    :type subject_descriptor: :class:`str <microsoft.-visual-studio.-services.-web-api.v4_0.models.str>`
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
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'unique_user_id': {'key': 'uniqueUserId', 'type': 'int'}
    }

    def __init__(self, custom_display_name=None, descriptor=None, id=None, is_active=None, is_container=None, master_id=None, member_ids=None, member_of=None, members=None, meta_type_id=None, properties=None, provider_display_name=None, resource_version=None, subject_descriptor=None, unique_user_id=None):
        super(Identity, self).__init__()
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
        self.subject_descriptor = subject_descriptor
        self.unique_user_id = unique_user_id



class LocationMapping(Model):
    """LocationMapping.

    :param access_mapping_moniker:
    :type access_mapping_moniker: str
    :param location:
    :type location: str
    """

    _attribute_map = {
        'access_mapping_moniker': {'key': 'accessMappingMoniker', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, access_mapping_moniker=None, location=None):
        super(LocationMapping, self).__init__()
        self.access_mapping_moniker = access_mapping_moniker
        self.location = location



class LocationServiceData(Model):
    """LocationServiceData.

    :param access_mappings: Data about the access mappings contained by this location service.
    :type access_mappings: list of :class:`AccessMapping <locations.v4_0.models.AccessMapping>`
    :param client_cache_fresh: Data that the location service holds.
    :type client_cache_fresh: bool
    :param client_cache_time_to_live: The time to live on the location service cache.
    :type client_cache_time_to_live: int
    :param default_access_mapping_moniker: The default access mapping moniker for the server.
    :type default_access_mapping_moniker: str
    :param last_change_id: The obsolete id for the last change that took place on the server (use LastChangeId64).
    :type last_change_id: int
    :param last_change_id64: The non-truncated 64-bit id for the last change that took place on the server.
    :type last_change_id64: long
    :param service_definitions: Data about the service definitions contained by this location service.
    :type service_definitions: list of :class:`ServiceDefinition <locations.v4_0.models.ServiceDefinition>`
    :param service_owner: The identifier of the deployment which is hosting this location data (e.g. SPS, TFS, ELS, Napa, etc.)
    :type service_owner: str
    """

    _attribute_map = {
        'access_mappings': {'key': 'accessMappings', 'type': '[AccessMapping]'},
        'client_cache_fresh': {'key': 'clientCacheFresh', 'type': 'bool'},
        'client_cache_time_to_live': {'key': 'clientCacheTimeToLive', 'type': 'int'},
        'default_access_mapping_moniker': {'key': 'defaultAccessMappingMoniker', 'type': 'str'},
        'last_change_id': {'key': 'lastChangeId', 'type': 'int'},
        'last_change_id64': {'key': 'lastChangeId64', 'type': 'long'},
        'service_definitions': {'key': 'serviceDefinitions', 'type': '[ServiceDefinition]'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'}
    }

    def __init__(self, access_mappings=None, client_cache_fresh=None, client_cache_time_to_live=None, default_access_mapping_moniker=None, last_change_id=None, last_change_id64=None, service_definitions=None, service_owner=None):
        super(LocationServiceData, self).__init__()
        self.access_mappings = access_mappings
        self.client_cache_fresh = client_cache_fresh
        self.client_cache_time_to_live = client_cache_time_to_live
        self.default_access_mapping_moniker = default_access_mapping_moniker
        self.last_change_id = last_change_id
        self.last_change_id64 = last_change_id64
        self.service_definitions = service_definitions
        self.service_owner = service_owner



class ResourceAreaInfo(Model):
    """ResourceAreaInfo.

    :param id:
    :type id: str
    :param location_url:
    :type location_url: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location_url': {'key': 'locationUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, location_url=None, name=None):
        super(ResourceAreaInfo, self).__init__()
        self.id = id
        self.location_url = location_url
        self.name = name



class ServiceDefinition(Model):
    """ServiceDefinition.

    :param description:
    :type description: str
    :param display_name:
    :type display_name: str
    :param identifier:
    :type identifier: str
    :param inherit_level:
    :type inherit_level: object
    :param location_mappings:
    :type location_mappings: list of :class:`LocationMapping <locations.v4_0.models.LocationMapping>`
    :param max_version: Maximum api version that this resource supports (current server version for this resource). Copied from <c>ApiResourceLocation</c>.
    :type max_version: str
    :param min_version: Minimum api version that this resource supports. Copied from <c>ApiResourceLocation</c>.
    :type min_version: str
    :param parent_identifier:
    :type parent_identifier: str
    :param parent_service_type:
    :type parent_service_type: str
    :param properties:
    :type properties: :class:`object <locations.v4_0.models.object>`
    :param relative_path:
    :type relative_path: str
    :param relative_to_setting:
    :type relative_to_setting: object
    :param released_version: The latest version of this resource location that is in "Release" (non-preview) mode. Copied from <c>ApiResourceLocation</c>.
    :type released_version: str
    :param resource_version: The current resource version supported by this resource location. Copied from <c>ApiResourceLocation</c>.
    :type resource_version: int
    :param service_owner: The service which owns this definition e.g. TFS, ELS, etc.
    :type service_owner: str
    :param service_type:
    :type service_type: str
    :param status:
    :type status: object
    :param tool_id:
    :type tool_id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'inherit_level': {'key': 'inheritLevel', 'type': 'object'},
        'location_mappings': {'key': 'locationMappings', 'type': '[LocationMapping]'},
        'max_version': {'key': 'maxVersion', 'type': 'str'},
        'min_version': {'key': 'minVersion', 'type': 'str'},
        'parent_identifier': {'key': 'parentIdentifier', 'type': 'str'},
        'parent_service_type': {'key': 'parentServiceType', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'relative_to_setting': {'key': 'relativeToSetting', 'type': 'object'},
        'released_version': {'key': 'releasedVersion', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'service_type': {'key': 'serviceType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tool_id': {'key': 'toolId', 'type': 'str'}
    }

    def __init__(self, description=None, display_name=None, identifier=None, inherit_level=None, location_mappings=None, max_version=None, min_version=None, parent_identifier=None, parent_service_type=None, properties=None, relative_path=None, relative_to_setting=None, released_version=None, resource_version=None, service_owner=None, service_type=None, status=None, tool_id=None):
        super(ServiceDefinition, self).__init__()
        self.description = description
        self.display_name = display_name
        self.identifier = identifier
        self.inherit_level = inherit_level
        self.location_mappings = location_mappings
        self.max_version = max_version
        self.min_version = min_version
        self.parent_identifier = parent_identifier
        self.parent_service_type = parent_service_type
        self.properties = properties
        self.relative_path = relative_path
        self.relative_to_setting = relative_to_setting
        self.released_version = released_version
        self.resource_version = resource_version
        self.service_owner = service_owner
        self.service_type = service_type
        self.status = status
        self.tool_id = tool_id
