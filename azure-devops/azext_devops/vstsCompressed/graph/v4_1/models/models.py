# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class GraphCachePolicies(Model):
    """GraphCachePolicies.

    :param cache_size: Size of the cache
    :type cache_size: int
    """

    _attribute_map = {
        'cache_size': {'key': 'cacheSize', 'type': 'int'}
    }

    def __init__(self, cache_size=None):
        super(GraphCachePolicies, self).__init__()
        self.cache_size = cache_size



class GraphDescriptorResult(Model):
    """GraphDescriptorResult.

    :param _links: This field contains zero or more interesting links about the graph descriptor. These links may be invoked to obtain additional relationships or more detailed information about this graph descriptor.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param value:
    :type value: :class:`str <graph.v4_1.models.str>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, _links=None, value=None):
        super(GraphDescriptorResult, self).__init__()
        self._links = _links
        self.value = value



class GraphGlobalExtendedPropertyBatch(Model):
    """GraphGlobalExtendedPropertyBatch.

    :param property_name_filters:
    :type property_name_filters: list of str
    :param subject_descriptors:
    :type subject_descriptors: list of :class:`str <graph.v4_1.models.str>`
    """

    _attribute_map = {
        'property_name_filters': {'key': 'propertyNameFilters', 'type': '[str]'},
        'subject_descriptors': {'key': 'subjectDescriptors', 'type': '[str]'}
    }

    def __init__(self, property_name_filters=None, subject_descriptors=None):
        super(GraphGlobalExtendedPropertyBatch, self).__init__()
        self.property_name_filters = property_name_filters
        self.subject_descriptors = subject_descriptors



class GraphGroupCreationContext(Model):
    """GraphGroupCreationContext.

    :param storage_key: Optional: If provided, we will use this identifier for the storage key of the created group
    :type storage_key: str
    """

    _attribute_map = {
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, storage_key=None):
        super(GraphGroupCreationContext, self).__init__()
        self.storage_key = storage_key



class GraphMembership(Model):
    """GraphMembership.

    :param _links: This field contains zero or more interesting links about the graph membership. These links may be invoked to obtain additional relationships or more detailed information about this graph membership.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param container_descriptor:
    :type container_descriptor: str
    :param member_descriptor:
    :type member_descriptor: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'container_descriptor': {'key': 'containerDescriptor', 'type': 'str'},
        'member_descriptor': {'key': 'memberDescriptor', 'type': 'str'}
    }

    def __init__(self, _links=None, container_descriptor=None, member_descriptor=None):
        super(GraphMembership, self).__init__()
        self._links = _links
        self.container_descriptor = container_descriptor
        self.member_descriptor = member_descriptor



class GraphMembershipState(Model):
    """GraphMembershipState.

    :param _links: This field contains zero or more interesting links about the graph membership state. These links may be invoked to obtain additional relationships or more detailed information about this graph membership state.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param active: When true, the membership is active
    :type active: bool
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'active': {'key': 'active', 'type': 'bool'}
    }

    def __init__(self, _links=None, active=None):
        super(GraphMembershipState, self).__init__()
        self._links = _links
        self.active = active



class GraphMembershipTraversal(Model):
    """GraphMembershipTraversal.

    :param incompleteness_reason: Reason why the subject could not be traversed completely
    :type incompleteness_reason: str
    :param is_complete: When true, the subject is traversed completely
    :type is_complete: bool
    :param subject_descriptor: The traversed subject descriptor
    :type subject_descriptor: :class:`str <graph.v4_1.models.str>`
    :param traversed_subject_ids: Subject descriptor ids of the traversed members
    :type traversed_subject_ids: list of str
    :param traversed_subjects: Subject descriptors of the traversed members
    :type traversed_subjects: list of :class:`str <graph.v4_1.models.str>`
    """

    _attribute_map = {
        'incompleteness_reason': {'key': 'incompletenessReason', 'type': 'str'},
        'is_complete': {'key': 'isComplete', 'type': 'bool'},
        'subject_descriptor': {'key': 'subjectDescriptor', 'type': 'str'},
        'traversed_subject_ids': {'key': 'traversedSubjectIds', 'type': '[str]'},
        'traversed_subjects': {'key': 'traversedSubjects', 'type': '[str]'}
    }

    def __init__(self, incompleteness_reason=None, is_complete=None, subject_descriptor=None, traversed_subject_ids=None, traversed_subjects=None):
        super(GraphMembershipTraversal, self).__init__()
        self.incompleteness_reason = incompleteness_reason
        self.is_complete = is_complete
        self.subject_descriptor = subject_descriptor
        self.traversed_subject_ids = traversed_subject_ids
        self.traversed_subjects = traversed_subjects



class GraphScopeCreationContext(Model):
    """GraphScopeCreationContext.

    :param admin_group_description: Set this field to override the default description of this scope's admin group.
    :type admin_group_description: str
    :param admin_group_name: All scopes have an Administrator Group that controls access to the contents of the scope. Set this field to use a non-default group name for that administrators group.
    :type admin_group_name: str
    :param creator_id: Set this optional field if this scope is created on behalf of a user other than the user making the request. This should be the Id of the user that is not the requester.
    :type creator_id: str
    :param name: The scope must be provided with a unique name within the parent scope. This means the created scope can have a parent or child with the same name, but no siblings with the same name.
    :type name: str
    :param scope_type: The type of scope being created.
    :type scope_type: object
    :param storage_key: An optional ID that uniquely represents the scope within it's parent scope. If this parameter is not provided, Vsts will generate on automatically.
    :type storage_key: str
    """

    _attribute_map = {
        'admin_group_description': {'key': 'adminGroupDescription', 'type': 'str'},
        'admin_group_name': {'key': 'adminGroupName', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, admin_group_description=None, admin_group_name=None, creator_id=None, name=None, scope_type=None, storage_key=None):
        super(GraphScopeCreationContext, self).__init__()
        self.admin_group_description = admin_group_description
        self.admin_group_name = admin_group_name
        self.creator_id = creator_id
        self.name = name
        self.scope_type = scope_type
        self.storage_key = storage_key



class GraphStorageKeyResult(Model):
    """GraphStorageKeyResult.

    :param _links: This field contains zero or more interesting links about the graph storage key. These links may be invoked to obtain additional relationships or more detailed information about this graph storage key.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param value:
    :type value: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, _links=None, value=None):
        super(GraphStorageKeyResult, self).__init__()
        self._links = _links
        self.value = value



class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
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



class GraphSubjectLookup(Model):
    """GraphSubjectLookup.

    :param lookup_keys:
    :type lookup_keys: list of :class:`GraphSubjectLookupKey <graph.v4_1.models.GraphSubjectLookupKey>`
    """

    _attribute_map = {
        'lookup_keys': {'key': 'lookupKeys', 'type': '[GraphSubjectLookupKey]'}
    }

    def __init__(self, lookup_keys=None):
        super(GraphSubjectLookup, self).__init__()
        self.lookup_keys = lookup_keys



class GraphSubjectLookupKey(Model):
    """GraphSubjectLookupKey.

    :param descriptor:
    :type descriptor: :class:`str <graph.v4_1.models.str>`
    """

    _attribute_map = {
        'descriptor': {'key': 'descriptor', 'type': 'str'}
    }

    def __init__(self, descriptor=None):
        super(GraphSubjectLookupKey, self).__init__()
        self.descriptor = descriptor



class GraphUserCreationContext(Model):
    """GraphUserCreationContext.

    :param storage_key: Optional: If provided, we will use this identifier for the storage key of the created user
    :type storage_key: str
    """

    _attribute_map = {
        'storage_key': {'key': 'storageKey', 'type': 'str'}
    }

    def __init__(self, storage_key=None):
        super(GraphUserCreationContext, self).__init__()
        self.storage_key = storage_key



class IdentityKeyMap(Model):
    """IdentityKeyMap.

    :param cuid:
    :type cuid: str
    :param storage_key:
    :type storage_key: str
    :param subject_type:
    :type subject_type: str
    """

    _attribute_map = {
        'cuid': {'key': 'cuid', 'type': 'str'},
        'storage_key': {'key': 'storageKey', 'type': 'str'},
        'subject_type': {'key': 'subjectType', 'type': 'str'}
    }

    def __init__(self, cuid=None, storage_key=None, subject_type=None):
        super(IdentityKeyMap, self).__init__()
        self.cuid = cuid
        self.storage_key = storage_key
        self.subject_type = subject_type



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



class PagedGraphGroups(Model):
    """PagedGraphGroups.

    :param continuation_token: This will be non-null if there is another page of data. There will never be more than one continuation token returned by a request.
    :type continuation_token: list of str
    :param graph_groups: The enumerable list of groups found within a page.
    :type graph_groups: list of :class:`GraphGroup <graph.v4_1.models.GraphGroup>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'graph_groups': {'key': 'graphGroups', 'type': '[GraphGroup]'}
    }

    def __init__(self, continuation_token=None, graph_groups=None):
        super(PagedGraphGroups, self).__init__()
        self.continuation_token = continuation_token
        self.graph_groups = graph_groups



class PagedGraphUsers(Model):
    """PagedGraphUsers.

    :param continuation_token: This will be non-null if there is another page of data. There will never be more than one continuation token returned by a request.
    :type continuation_token: list of str
    :param graph_users: The enumerable set of users found within a page.
    :type graph_users: list of :class:`GraphUser <graph.v4_1.models.GraphUser>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'graph_users': {'key': 'graphUsers', 'type': '[GraphUser]'}
    }

    def __init__(self, continuation_token=None, graph_users=None):
        super(PagedGraphUsers, self).__init__()
        self.continuation_token = continuation_token
        self.graph_users = graph_users



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



class GraphSubject(GraphSubjectBase):
    """GraphSubject.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None):
        super(GraphSubject, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.legacy_descriptor = legacy_descriptor
        self.origin = origin
        self.origin_id = origin_id
        self.subject_kind = subject_kind



class GraphMember(GraphSubject):
    """GraphMember.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param cuid: The Consistently Unique Identifier of the subject
    :type cuid: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'cuid': {'key': 'cuid', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, cuid=None, domain=None, mail_address=None, principal_name=None):
        super(GraphMember, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind)
        self.cuid = cuid
        self.domain = domain
        self.mail_address = mail_address
        self.principal_name = principal_name



class GraphScope(GraphSubject):
    """GraphScope.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param administrator_descriptor: The subject descriptor that references the administrators group for this scope. Only members of this group can change the contents of this scope or assign other users permissions to access this scope.
    :type administrator_descriptor: str
    :param is_global: When true, this scope is also a securing host for one or more scopes.
    :type is_global: bool
    :param parent_descriptor: The subject descriptor for the closest account or organization in the ancestor tree of this scope.
    :type parent_descriptor: str
    :param scope_type: The type of this scope. Typically ServiceHost or TeamProject.
    :type scope_type: object
    :param securing_host_descriptor: The subject descriptor for the containing organization in the ancestor tree of this scope.
    :type securing_host_descriptor: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'administrator_descriptor': {'key': 'administratorDescriptor', 'type': 'str'},
        'is_global': {'key': 'isGlobal', 'type': 'bool'},
        'parent_descriptor': {'key': 'parentDescriptor', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'securing_host_descriptor': {'key': 'securingHostDescriptor', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, administrator_descriptor=None, is_global=None, parent_descriptor=None, scope_type=None, securing_host_descriptor=None):
        super(GraphScope, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind)
        self.administrator_descriptor = administrator_descriptor
        self.is_global = is_global
        self.parent_descriptor = parent_descriptor
        self.scope_type = scope_type
        self.securing_host_descriptor = securing_host_descriptor



class GraphUser(GraphMember):
    """GraphUser.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param cuid: The Consistently Unique Identifier of the subject
    :type cuid: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    :param meta_type: The meta type of the user in the origin, such as "member", "guest", etc. See UserMetaType for the set of possible values.
    :type meta_type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'cuid': {'key': 'cuid', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'meta_type': {'key': 'metaType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, cuid=None, domain=None, mail_address=None, principal_name=None, meta_type=None):
        super(GraphUser, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, cuid=cuid, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.meta_type = meta_type



class GraphGroup(GraphMember):
    """GraphGroup.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param cuid: The Consistently Unique Identifier of the subject
    :type cuid: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    :param description: A short phrase to help human readers disambiguate groups with similar names
    :type description: str
    :param is_cross_project:
    :type is_cross_project: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_global_scope:
    :type is_global_scope: bool
    :param is_restricted_visible:
    :type is_restricted_visible: bool
    :param local_scope_id:
    :type local_scope_id: str
    :param scope_id:
    :type scope_id: str
    :param scope_name:
    :type scope_name: str
    :param scope_type:
    :type scope_type: str
    :param securing_host_id:
    :type securing_host_id: str
    :param special_type:
    :type special_type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'cuid': {'key': 'cuid', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_cross_project': {'key': 'isCrossProject', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_global_scope': {'key': 'isGlobalScope', 'type': 'bool'},
        'is_restricted_visible': {'key': 'isRestrictedVisible', 'type': 'bool'},
        'local_scope_id': {'key': 'localScopeId', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'str'},
        'securing_host_id': {'key': 'securingHostId', 'type': 'str'},
        'special_type': {'key': 'specialType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, cuid=None, domain=None, mail_address=None, principal_name=None, description=None, is_cross_project=None, is_deleted=None, is_global_scope=None, is_restricted_visible=None, local_scope_id=None, scope_id=None, scope_name=None, scope_type=None, securing_host_id=None, special_type=None):
        super(GraphGroup, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, cuid=cuid, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.description = description
        self.is_cross_project = is_cross_project
        self.is_deleted = is_deleted
        self.is_global_scope = is_global_scope
        self.is_restricted_visible = is_restricted_visible
        self.local_scope_id = local_scope_id
        self.scope_id = scope_id
        self.scope_name = scope_name
        self.scope_type = scope_type
        self.securing_host_id = securing_host_id
        self.special_type = special_type
