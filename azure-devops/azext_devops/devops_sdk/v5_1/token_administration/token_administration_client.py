# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TokenAdministrationClient(Client):
    """TokenAdministration
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TokenAdministrationClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '95935461-9e54-44bd-b9fb-04f4dd05d640'

    def list_identities_with_global_access_tokens(self, revocations, is_public=None):
        """ListIdentitiesWithGlobalAccessTokens.
        [Preview API] Revokes the listed OAuth authorizations.
        :param [TokenAdminRevocation] revocations: The list of identities containing the authorization IDs of the OAuth authorizations, such as session tokens retrieved by listed a users PATs, that should be checked for global access tokens.
        :param bool is_public: Set to false for PAT tokens and true for SSH tokens.
        :rtype: [str]
        """
        query_parameters = {}
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, '[TokenAdminRevocation]')
        response = self._send(http_method='POST',
                              location_id='30d3a12b-66c3-4669-b016-ecb0706c8d0f',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def list_personal_access_tokens(self, audience, subject_descriptor, page_size=None, continuation_token=None, is_public=None):
        """ListPersonalAccessTokens.
        [Preview API] Lists of all the session token details of the personal access tokens (PATs) for a particular user.
        :param [str] audience:
        :param :class:`<str> <azure.devops.v5_1.token_administration.models.str>` subject_descriptor: The descriptor of the target user.
        :param int page_size: The maximum number of results to return on each page.
        :param str continuation_token: An opaque data blob that allows the next page of data to resume immediately after where the previous page ended. The only reliable way to know if there is more data left is the presence of a continuation token.
        :param bool is_public: Set to false for PAT tokens and true for SSH tokens.
        :rtype: :class:`<TokenAdminPagedSessionTokens> <azure.devops.v5_1.token_administration.models.TokenAdminPagedSessionTokens>`
        """
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        query_parameters = {}
        if page_size is not None:
            query_parameters['pageSize'] = self._serialize.query('page_size', page_size, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(audience, '[str]')
        response = self._send(http_method='POST',
                              location_id='1bb7db14-87c5-4762-bf77-a70ad34a9ab3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TokenAdminPagedSessionTokens', response)

    def revoke_authorizations(self, revocations, host_id, is_public=None):
        """RevokeAuthorizations.
        [Preview API] Revokes the listed OAuth authorizations.
        :param :class:`<TokenAdministrationRevocation> <azure.devops.v5_1.token_administration.models.TokenAdministrationRevocation>` revocations: The list of objects containing the authorization IDs of the OAuth authorizations, such as session tokens retrieved by listed a users PATs, that should be revoked.
        :param str host_id: Host Id to display on the notification page to manage tokens.
        :param bool is_public: Set to false for PAT tokens and true for SSH tokens.
        :rtype: [SessionToken]
        """
        query_parameters = {}
        if host_id is not None:
            query_parameters['hostId'] = self._serialize.query('host_id', host_id, 'str')
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, 'TokenAdministrationRevocation')
        response = self._send(http_method='POST',
                              location_id='a2e4520b-1cc8-4526-871e-f3a8f865f221',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[SessionToken]', self._unwrap_collection(response))

