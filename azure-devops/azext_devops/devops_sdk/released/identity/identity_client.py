# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.identity import models


class IdentityClient(Client):
    """Identity
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(IdentityClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8a3d49b8-91f0-46ef-b33d-dda338c25db3'

    def create_groups(self, container):
        """CreateGroups.
        :param :class:`<object> <azure.devops.v5_1.identity.models.object>` container:
        :rtype: [Identity]
        """
        content = self._serialize.body(container, 'object')
        response = self._send(http_method='POST',
                              location_id='5966283b-4196-4d57-9211-1b68f41ec1c2',
                              version='5.1',
                              content=content)
        return self._deserialize('[Identity]', self._unwrap_collection(response))

    def delete_group(self, group_id):
        """DeleteGroup.
        :param str group_id:
        """
        route_values = {}
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        self._send(http_method='DELETE',
                   location_id='5966283b-4196-4d57-9211-1b68f41ec1c2',
                   version='5.1',
                   route_values=route_values)

    def list_groups(self, scope_ids=None, recurse=None, deleted=None, properties=None):
        """ListGroups.
        :param str scope_ids:
        :param bool recurse:
        :param bool deleted:
        :param str properties:
        :rtype: [Identity]
        """
        query_parameters = {}
        if scope_ids is not None:
            query_parameters['scopeIds'] = self._serialize.query('scope_ids', scope_ids, 'str')
        if recurse is not None:
            query_parameters['recurse'] = self._serialize.query('recurse', recurse, 'bool')
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        if properties is not None:
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        response = self._send(http_method='GET',
                              location_id='5966283b-4196-4d57-9211-1b68f41ec1c2',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[Identity]', self._unwrap_collection(response))

    def get_identity_changes(self, identity_sequence_id, group_sequence_id, organization_identity_sequence_id=None, page_size=None, scope_id=None):
        """GetIdentityChanges.
        :param int identity_sequence_id:
        :param int group_sequence_id:
        :param int organization_identity_sequence_id:
        :param int page_size:
        :param str scope_id:
        :rtype: :class:`<ChangedIdentities> <azure.devops.v5_1.identity.models.ChangedIdentities>`
        """
        query_parameters = {}
        if identity_sequence_id is not None:
            query_parameters['identitySequenceId'] = self._serialize.query('identity_sequence_id', identity_sequence_id, 'int')
        if group_sequence_id is not None:
            query_parameters['groupSequenceId'] = self._serialize.query('group_sequence_id', group_sequence_id, 'int')
        if organization_identity_sequence_id is not None:
            query_parameters['organizationIdentitySequenceId'] = self._serialize.query('organization_identity_sequence_id', organization_identity_sequence_id, 'int')
        if page_size is not None:
            query_parameters['pageSize'] = self._serialize.query('page_size', page_size, 'int')
        if scope_id is not None:
            query_parameters['scopeId'] = self._serialize.query('scope_id', scope_id, 'str')
        response = self._send(http_method='GET',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('ChangedIdentities', response)

    def get_user_identity_ids_by_domain_id(self, domain_id):
        """GetUserIdentityIdsByDomainId.
        :param str domain_id:
        :rtype: [str]
        """
        query_parameters = {}
        if domain_id is not None:
            query_parameters['domainId'] = self._serialize.query('domain_id', domain_id, 'str')
        response = self._send(http_method='GET',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def read_identities(self, descriptors=None, identity_ids=None, subject_descriptors=None, social_descriptors=None, search_filter=None, filter_value=None, query_membership=None, properties=None, include_restricted_visibility=None, options=None):
        """ReadIdentities.
        :param str descriptors:
        :param str identity_ids:
        :param str subject_descriptors:
        :param str social_descriptors:
        :param str search_filter:
        :param str filter_value:
        :param str query_membership:
        :param str properties:
        :param bool include_restricted_visibility:
        :param str options:
        :rtype: [Identity]
        """
        query_parameters = {}
        if descriptors is not None:
            query_parameters['descriptors'] = self._serialize.query('descriptors', descriptors, 'str')
        if identity_ids is not None:
            query_parameters['identityIds'] = self._serialize.query('identity_ids', identity_ids, 'str')
        if subject_descriptors is not None:
            query_parameters['subjectDescriptors'] = self._serialize.query('subject_descriptors', subject_descriptors, 'str')
        if social_descriptors is not None:
            query_parameters['socialDescriptors'] = self._serialize.query('social_descriptors', social_descriptors, 'str')
        if search_filter is not None:
            query_parameters['searchFilter'] = self._serialize.query('search_filter', search_filter, 'str')
        if filter_value is not None:
            query_parameters['filterValue'] = self._serialize.query('filter_value', filter_value, 'str')
        if query_membership is not None:
            query_parameters['queryMembership'] = self._serialize.query('query_membership', query_membership, 'str')
        if properties is not None:
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if include_restricted_visibility is not None:
            query_parameters['includeRestrictedVisibility'] = self._serialize.query('include_restricted_visibility', include_restricted_visibility, 'bool')
        if options is not None:
            query_parameters['options'] = self._serialize.query('options', options, 'str')
        response = self._send(http_method='GET',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[Identity]', self._unwrap_collection(response))

    def read_identities_by_scope(self, scope_id, query_membership=None, properties=None):
        """ReadIdentitiesByScope.
        :param str scope_id:
        :param str query_membership:
        :param str properties:
        :rtype: [Identity]
        """
        query_parameters = {}
        if scope_id is not None:
            query_parameters['scopeId'] = self._serialize.query('scope_id', scope_id, 'str')
        if query_membership is not None:
            query_parameters['queryMembership'] = self._serialize.query('query_membership', query_membership, 'str')
        if properties is not None:
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        response = self._send(http_method='GET',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[Identity]', self._unwrap_collection(response))

    def read_identity(self, identity_id, query_membership=None, properties=None):
        """ReadIdentity.
        :param str identity_id:
        :param str query_membership:
        :param str properties:
        :rtype: :class:`<Identity> <azure.devops.v5_1.identity.models.Identity>`
        """
        route_values = {}
        if identity_id is not None:
            route_values['identityId'] = self._serialize.url('identity_id', identity_id, 'str')
        query_parameters = {}
        if query_membership is not None:
            query_parameters['queryMembership'] = self._serialize.query('query_membership', query_membership, 'str')
        if properties is not None:
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        response = self._send(http_method='GET',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Identity', response)

    def update_identities(self, identities):
        """UpdateIdentities.
        :param :class:`<VssJsonCollectionWrapper> <azure.devops.v5_1.identity.models.VssJsonCollectionWrapper>` identities:
        :rtype: [IdentityUpdateData]
        """
        content = self._serialize.body(identities, 'VssJsonCollectionWrapper')
        response = self._send(http_method='PUT',
                              location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                              version='5.1',
                              content=content)
        return self._deserialize('[IdentityUpdateData]', self._unwrap_collection(response))

    def update_identity(self, identity, identity_id):
        """UpdateIdentity.
        :param :class:`<Identity> <azure.devops.v5_1.identity.models.Identity>` identity:
        :param str identity_id:
        """
        route_values = {}
        if identity_id is not None:
            route_values['identityId'] = self._serialize.url('identity_id', identity_id, 'str')
        content = self._serialize.body(identity, 'Identity')
        self._send(http_method='PUT',
                   location_id='28010c54-d0c0-4c89-a5b0-1c9e188b9fb7',
                   version='5.1',
                   route_values=route_values,
                   content=content)

    def create_identity(self, framework_identity_info):
        """CreateIdentity.
        :param :class:`<FrameworkIdentityInfo> <azure.devops.v5_1.identity.models.FrameworkIdentityInfo>` framework_identity_info:
        :rtype: :class:`<Identity> <azure.devops.v5_1.identity.models.Identity>`
        """
        content = self._serialize.body(framework_identity_info, 'FrameworkIdentityInfo')
        response = self._send(http_method='PUT',
                              location_id='dd55f0eb-6ea2-4fe4-9ebe-919e7dd1dfb4',
                              version='5.1',
                              content=content)
        return self._deserialize('Identity', response)

    def get_max_sequence_id(self):
        """GetMaxSequenceId.
        Read the max sequence id of all the identities.
        :rtype: long
        """
        response = self._send(http_method='GET',
                              location_id='e4a70778-cb2c-4e85-b7cc-3f3c7ae2d408',
                              version='5.1')
        return self._deserialize('long', response)

    def get_self(self):
        """GetSelf.
        Read identity of the home tenant request user.
        :rtype: :class:`<IdentitySelf> <azure.devops.v5_1.identity.models.IdentitySelf>`
        """
        response = self._send(http_method='GET',
                              location_id='4bb02b5b-c120-4be2-b68e-21f7c50a4b82',
                              version='5.1')
        return self._deserialize('IdentitySelf', response)

