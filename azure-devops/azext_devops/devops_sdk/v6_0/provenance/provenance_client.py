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


class ProvenanceClient(Client):
    """Provenance
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(ProvenanceClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'b40c1171-807a-493a-8f3f-5c26d5e2f5aa'

    def create_session(self, session_request, protocol, project=None):
        """CreateSession.
        [Preview API] Creates a session, a wrapper around a feed that can store additional metadata on the packages published to it.
        :param :class:`<SessionRequest> <azure.devops.v6_0.provenance.models.SessionRequest>` session_request: The feed and metadata for the session
        :param str protocol: The protocol that the session will target
        :param str project: Project ID or project name
        :rtype: :class:`<SessionResponse> <azure.devops.v6_0.provenance.models.SessionResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if protocol is not None:
            route_values['protocol'] = self._serialize.url('protocol', protocol, 'str')
        content = self._serialize.body(session_request, 'SessionRequest')
        response = self._send(http_method='POST',
                              location_id='503b4e54-ebf4-4d04-8eee-21c00823c2ac',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('SessionResponse', response)

