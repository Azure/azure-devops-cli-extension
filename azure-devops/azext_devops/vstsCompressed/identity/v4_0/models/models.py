# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AccessTokenResult(Model):
    """AccessTokenResult.

    :param access_token:
    :type access_token: :class:`JsonWebToken <microsoft.-visual-studio.-services.-web-api.v4_0.models.JsonWebToken>`
    :param access_token_error:
    :type access_token_error: object
    :param authorization_id:
    :type authorization_id: str
    :param error_description:
    :type error_description: str
    :param has_error:
    :type has_error: bool
    :param refresh_token:
    :type refresh_token: :class:`RefreshTokenGrant <microsoft.-visual-studio.-services.-web-api.v4_0.models.RefreshTokenGrant>`
    :param token_type:
    :type token_type: str
    :param valid_to:
    :type valid_to: datetime
    """

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'JsonWebToken'},
        'access_token_error': {'key': 'accessTokenError', 'type': 'object'},
        'authorization_id': {'key': 'authorizationId', 'type': 'str'},
        'error_description': {'key': 'errorDescription', 'type': 'str'},
        'has_error': {'key': 'hasError', 'type': 'bool'},
        'refresh_token': {'key': 'refreshToken', 'type': 'RefreshTokenGrant'},
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, access_token=None, access_token_error=None, authorization_id=None, error_description=None, has_error=None, refresh_token=None, token_type=None, valid_to=None):
        super(AccessTokenResult, self).__init__()
        self.access_token = access_token
        self.access_token_error = access_token_error
        self.authorization_id = authorization_id
        self.error_description = error_description
        self.has_error = has_error
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.valid_to = valid_to



class AuthorizationGrant(Model):
    """AuthorizationGrant.

    :param grant_type:
    :type grant_type: object
    """

    _attribute_map = {
        'grant_type': {'key': 'grantType', 'type': 'object'}
    }

    def __init__(self, grant_type=None):
        super(AuthorizationGrant, self).__init__()
        self.grant_type = grant_type



class ChangedIdentities(Model):
    """ChangedIdentities.

    :param identities: Changed Identities
    :type identities: list of :class:`Identity <identities.v4_0.models.Identity>`
    :param sequence_context: Last Identity SequenceId
    :type sequence_context: :class:`ChangedIdentitiesContext <identities.v4_0.models.ChangedIdentitiesContext>`
    """

    _attribute_map = {
        'identities': {'key': 'identities', 'type': '[Identity]'},
        'sequence_context': {'key': 'sequenceContext', 'type': 'ChangedIdentitiesContext'}
    }

    def __init__(self, identities=None, sequence_context=None):
        super(ChangedIdentities, self).__init__()
        self.identities = identities
        self.sequence_context = sequence_context



class ChangedIdentitiesContext(Model):
    """ChangedIdentitiesContext.

    :param group_sequence_id: Last Group SequenceId
    :type group_sequence_id: int
    :param identity_sequence_id: Last Identity SequenceId
    :type identity_sequence_id: int
    """

    _attribute_map = {
        'group_sequence_id': {'key': 'groupSequenceId', 'type': 'int'},
        'identity_sequence_id': {'key': 'identitySequenceId', 'type': 'int'}
    }

    def __init__(self, group_sequence_id=None, identity_sequence_id=None):
        super(ChangedIdentitiesContext, self).__init__()
        self.group_sequence_id = group_sequence_id
        self.identity_sequence_id = identity_sequence_id



class CreateScopeInfo(Model):
    """CreateScopeInfo.

    :param admin_group_description:
    :type admin_group_description: str
    :param admin_group_name:
    :type admin_group_name: str
    :param creator_id:
    :type creator_id: str
    :param parent_scope_id:
    :type parent_scope_id: str
    :param scope_name:
    :type scope_name: str
    :param scope_type:
    :type scope_type: object
    """

    _attribute_map = {
        'admin_group_description': {'key': 'adminGroupDescription', 'type': 'str'},
        'admin_group_name': {'key': 'adminGroupName', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'parent_scope_id': {'key': 'parentScopeId', 'type': 'str'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'}
    }

    def __init__(self, admin_group_description=None, admin_group_name=None, creator_id=None, parent_scope_id=None, scope_name=None, scope_type=None):
        super(CreateScopeInfo, self).__init__()
        self.admin_group_description = admin_group_description
        self.admin_group_name = admin_group_name
        self.creator_id = creator_id
        self.parent_scope_id = parent_scope_id
        self.scope_name = scope_name
        self.scope_type = scope_type



class FrameworkIdentityInfo(Model):
    """FrameworkIdentityInfo.

    :param display_name:
    :type display_name: str
    :param identifier:
    :type identifier: str
    :param identity_type:
    :type identity_type: object
    :param role:
    :type role: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'identity_type': {'key': 'identityType', 'type': 'object'},
        'role': {'key': 'role', 'type': 'str'}
    }

    def __init__(self, display_name=None, identifier=None, identity_type=None, role=None):
        super(FrameworkIdentityInfo, self).__init__()
        self.display_name = display_name
        self.identifier = identifier
        self.identity_type = identity_type
        self.role = role



class GroupMembership(Model):
    """GroupMembership.

    :param active:
    :type active: bool
    :param descriptor:
    :type descriptor: :class:`str <identities.v4_0.models.str>`
    :param id:
    :type id: str
    :param queried_id:
    :type queried_id: str
    """

    _attribute_map = {
        'active': {'key': 'active', 'type': 'bool'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'queried_id': {'key': 'queriedId', 'type': 'str'}
    }

    def __init__(self, active=None, descriptor=None, id=None, queried_id=None):
        super(GroupMembership, self).__init__()
        self.active = active
        self.descriptor = descriptor
        self.id = id
        self.queried_id = queried_id



class Identity(Model):
    """Identity.

    :param custom_display_name: The custom display name for the identity (if any). Setting this property to an empty string will clear the existing custom display name. Setting this property to null will not affect the existing persisted value (since null values do not get sent over the wire or to the database)
    :type custom_display_name: str
    :param descriptor:
    :type descriptor: :class:`str <identities.v4_0.models.str>`
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
    :type member_of: list of :class:`str <identities.v4_0.models.str>`
    :param members:
    :type members: list of :class:`str <identities.v4_0.models.str>`
    :param meta_type_id:
    :type meta_type_id: int
    :param properties:
    :type properties: :class:`object <identities.v4_0.models.object>`
    :param provider_display_name: The display name for the identity as specified by the source identity provider.
    :type provider_display_name: str
    :param resource_version:
    :type resource_version: int
    :param subject_descriptor:
    :type subject_descriptor: :class:`str <identities.v4_0.models.str>`
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



class IdentityBatchInfo(Model):
    """IdentityBatchInfo.

    :param descriptors:
    :type descriptors: list of :class:`str <identities.v4_0.models.str>`
    :param identity_ids:
    :type identity_ids: list of str
    :param include_restricted_visibility:
    :type include_restricted_visibility: bool
    :param property_names:
    :type property_names: list of str
    :param query_membership:
    :type query_membership: object
    """

    _attribute_map = {
        'descriptors': {'key': 'descriptors', 'type': '[str]'},
        'identity_ids': {'key': 'identityIds', 'type': '[str]'},
        'include_restricted_visibility': {'key': 'includeRestrictedVisibility', 'type': 'bool'},
        'property_names': {'key': 'propertyNames', 'type': '[str]'},
        'query_membership': {'key': 'queryMembership', 'type': 'object'}
    }

    def __init__(self, descriptors=None, identity_ids=None, include_restricted_visibility=None, property_names=None, query_membership=None):
        super(IdentityBatchInfo, self).__init__()
        self.descriptors = descriptors
        self.identity_ids = identity_ids
        self.include_restricted_visibility = include_restricted_visibility
        self.property_names = property_names
        self.query_membership = query_membership



class IdentityScope(Model):
    """IdentityScope.

    :param administrators:
    :type administrators: :class:`str <identities.v4_0.models.str>`
    :param id:
    :type id: str
    :param is_active:
    :type is_active: bool
    :param is_global:
    :type is_global: bool
    :param local_scope_id:
    :type local_scope_id: str
    :param name:
    :type name: str
    :param parent_id:
    :type parent_id: str
    :param scope_type:
    :type scope_type: object
    :param securing_host_id:
    :type securing_host_id: str
    :param subject_descriptor:
    :type subject_descriptor: :class:`str <identities.v4_0.models.str>`
    """

    _attribute_map = {
        'administrators': {'key': 'administrators', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_global': {'key': 'isGlobal', 'type': 'bool'},
        'local_scope_id': {'key': 'localScopeId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'securing_host_id': {'key': 'securingHostId', 'type': 'str'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'}
    }

    def __init__(self, administrators=None, id=None, is_active=None, is_global=None, local_scope_id=None, name=None, parent_id=None, scope_type=None, securing_host_id=None, subject_descriptor=None):
        super(IdentityScope, self).__init__()
        self.administrators = administrators
        self.id = id
        self.is_active = is_active
        self.is_global = is_global
        self.local_scope_id = local_scope_id
        self.name = name
        self.parent_id = parent_id
        self.scope_type = scope_type
        self.securing_host_id = securing_host_id
        self.subject_descriptor = subject_descriptor



class IdentitySelf(Model):
    """IdentitySelf.

    :param account_name:
    :type account_name: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param tenants:
    :type tenants: list of :class:`TenantInfo <identities.v4_0.models.TenantInfo>`
    """

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'tenants': {'key': 'tenants', 'type': '[TenantInfo]'}
    }

    def __init__(self, account_name=None, display_name=None, id=None, tenants=None):
        super(IdentitySelf, self).__init__()
        self.account_name = account_name
        self.display_name = display_name
        self.id = id
        self.tenants = tenants



class IdentitySnapshot(Model):
    """IdentitySnapshot.

    :param groups:
    :type groups: list of :class:`Identity <identities.v4_0.models.Identity>`
    :param identity_ids:
    :type identity_ids: list of str
    :param memberships:
    :type memberships: list of :class:`GroupMembership <identities.v4_0.models.GroupMembership>`
    :param scope_id:
    :type scope_id: str
    :param scopes:
    :type scopes: list of :class:`IdentityScope <identities.v4_0.models.IdentityScope>`
    """

    _attribute_map = {
        'groups': {'key': 'groups', 'type': '[Identity]'},
        'identity_ids': {'key': 'identityIds', 'type': '[str]'},
        'memberships': {'key': 'memberships', 'type': '[GroupMembership]'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': '[IdentityScope]'}
    }

    def __init__(self, groups=None, identity_ids=None, memberships=None, scope_id=None, scopes=None):
        super(IdentitySnapshot, self).__init__()
        self.groups = groups
        self.identity_ids = identity_ids
        self.memberships = memberships
        self.scope_id = scope_id
        self.scopes = scopes



class IdentityUpdateData(Model):
    """IdentityUpdateData.

    :param id:
    :type id: str
    :param index:
    :type index: int
    :param updated:
    :type updated: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'updated': {'key': 'updated', 'type': 'bool'}
    }

    def __init__(self, id=None, index=None, updated=None):
        super(IdentityUpdateData, self).__init__()
        self.id = id
        self.index = index
        self.updated = updated



class JsonWebToken(Model):
    """JsonWebToken.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(JsonWebToken, self).__init__()



class RefreshTokenGrant(AuthorizationGrant):
    """RefreshTokenGrant.

    :param grant_type:
    :type grant_type: object
    :param jwt:
    :type jwt: :class:`JsonWebToken <microsoft.-visual-studio.-services.-web-api.v4_0.models.JsonWebToken>`
    """

    _attribute_map = {
        'grant_type': {'key': 'grantType', 'type': 'object'},
        'jwt': {'key': 'jwt', 'type': 'JsonWebToken'}
    }

    def __init__(self, grant_type=None, jwt=None):
        super(RefreshTokenGrant, self).__init__(grant_type=grant_type)
        self.jwt = jwt



class TenantInfo(Model):
    """TenantInfo.

    :param home_tenant:
    :type home_tenant: bool
    :param tenant_id:
    :type tenant_id: str
    :param tenant_name:
    :type tenant_name: str
    """

    _attribute_map = {
        'home_tenant': {'key': 'homeTenant', 'type': 'bool'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'tenant_name': {'key': 'tenantName', 'type': 'str'}
    }

    def __init__(self, home_tenant=None, tenant_id=None, tenant_name=None):
        super(TenantInfo, self).__init__()
        self.home_tenant = home_tenant
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
