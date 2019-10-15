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


class TokenAdminClient(Client):
    """TokenAdmin
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TokenAdminClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'af68438b-ed04-4407-9eb6-f1dbae3f922e'

    def list_personal_access_tokens(self, subject_descriptor, page_size=None, continuation_token=None, is_public=None):
        """ListPersonalAccessTokens.
        [Preview API] Lists of all the session token details of the personal access tokens (PATs) for a particular user.
        :param :class:`<str> <azure.devops.v5_1.token_admin.models.str>` subject_descriptor: The descriptor of the target user.
        :param int page_size: The maximum number of results to return on each page.
        :param str continuation_token: An opaque data blob that allows the next page of data to resume immediately after where the previous page ended. The only reliable way to know if there is more data left is the presence of a continuation token.
        :param bool is_public: Set to false for PAT tokens and true for SSH tokens.
        :rtype: :class:`<TokenAdminPagedSessionTokens> <azure.devops.v5_1.token_admin.models.TokenAdminPagedSessionTokens>`
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
        response = self._send(http_method='GET',
                              location_id='af68438b-ed04-4407-9eb6-f1dbae3f922e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TokenAdminPagedSessionTokens', response)

    def create_revocation_rule(self, revocation_rule):
        """CreateRevocationRule.
        [Preview API] Creates a revocation rule to prevent the further usage of any OAuth authorizations that were created before the current point in time and which match the conditions in the rule.
        :param :class:`<TokenAdminRevocationRule> <azure.devops.v5_1.token_admin.models.TokenAdminRevocationRule>` revocation_rule: The revocation rule to create. The rule must specify a space-separated list of scopes, after which preexisting OAuth authorizations that match that any of the scopes will be rejected. For a list of all OAuth scopes supported by VSTS, see: https://docs.microsoft.com/en-us/vsts/integrate/get-started/authentication/oauth?view=vsts#scopes The rule may also specify the time before which to revoke tokens.
        """
        content = self._serialize.body(revocation_rule, 'TokenAdminRevocationRule')
        self._send(http_method='POST',
                   location_id='ee4afb16-e7ab-4ed8-9d4b-4ef3e78f97e4',
                   version='5.1-preview.1',
                   content=content)

    def revoke_authorizations(self, revocations, is_public=None):
        """RevokeAuthorizations.
        [Preview API] Revokes the listed OAuth authorizations.
        :param [TokenAdminRevocation] revocations: The list of objects containing the authorization IDs of the OAuth authorizations, such as session tokens retrieved by listed a users PATs, that should be revoked.
        :param bool is_public: Set to false for PAT tokens and true for SSH tokens.
        """
        query_parameters = {}
        if is_public is not None:
            query_parameters['isPublic'] = self._serialize.query('is_public', is_public, 'bool')
        content = self._serialize.body(revocations, '[TokenAdminRevocation]')
        self._send(http_method='POST',
                   location_id='a9c08b2c-5466-4e22-8626-1ff304ffdf0f',
                   version='5.1-preview.1',
                   query_parameters=query_parameters,
                   content=content)

