# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.test_results import models


class TestResultsClient(Client):
    """TestResults
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TestResultsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_test_run_statistics(self, project, run_id):
        """GetTestRunStatistics.
        Get test run statistics , used when we want to get summary of a run by outcome.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: :class:`<TestRunStatistic> <azure.devops.v5_1.test_results.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='82b986e8-ca9e-4a89-b39e-f65c69bc104a',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

