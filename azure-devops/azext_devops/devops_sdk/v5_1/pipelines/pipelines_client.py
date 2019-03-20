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


class PipelinesClient(Client):
    """Pipelines
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(PipelinesClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_pipeline(self, project, pipeline_id, revision=None):
        """GetPipeline.
        [Preview API]
        :param str project: Project ID or project name
        :param int pipeline_id:
        :param int revision:
        :rtype: :class:`<Pipeline> <azure.devops.v5_1.pipelines.models.Pipeline>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        response = self._send(http_method='GET',
                              location_id='28e1305e-2afe-47bf-abaf-cbb0e6a91988',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Pipeline', response)

