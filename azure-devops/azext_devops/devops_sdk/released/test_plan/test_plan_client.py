# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.test_plan import models


class TestPlanClient(Client):
    """TestPlan
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TestPlanClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_suites_by_test_case_id(self, test_case_id):
        """GetSuitesByTestCaseId.
        Find the list of all test suites in which a given test case is present. This is helpful if you need to find out which test suites are using a test case, when you need to make changes to a test case.
        :param int test_case_id: ID of the test case for which suites need to be fetched.
        :rtype: [TestSuite]
        """
        query_parameters = {}
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        response = self._send(http_method='GET',
                              location_id='a4080e84-f17b-4fad-84f1-7960b6525bf2',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

