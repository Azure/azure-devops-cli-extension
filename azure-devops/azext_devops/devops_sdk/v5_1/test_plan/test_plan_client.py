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

    def create_test_configuration(self, test_configuration_create_update_parameters, project):
        """CreateTestConfiguration.
        [Preview API] Create a test configuration.
        :param :class:`<TestConfigurationCreateUpdateParameters> <azure.devops.v5_1.test_plan.models.TestConfigurationCreateUpdateParameters>` test_configuration_create_update_parameters: TestConfigurationCreateUpdateParameters
        :param str project: Project ID or project name
        :rtype: :class:`<TestConfiguration> <azure.devops.v5_1.test_plan.models.TestConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_configuration_create_update_parameters, 'TestConfigurationCreateUpdateParameters')
        response = self._send(http_method='POST',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestConfiguration', response)

    def delete_test_confguration(self, project, test_configuartion_id):
        """DeleteTestConfguration.
        [Preview API] Delete a test configuration by its ID.
        :param str project: Project ID or project name
        :param int test_configuartion_id: ID of the test configuration to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_configuartion_id is not None:
            query_parameters['testConfiguartionId'] = self._serialize.query('test_configuartion_id', test_configuartion_id, 'int')
        self._send(http_method='DELETE',
                   location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                   version='5.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_test_configuration_by_id(self, project, test_configuration_id):
        """GetTestConfigurationById.
        [Preview API] Get a test configuration
        :param str project: Project ID or project name
        :param int test_configuration_id: ID of the test configuration to get.
        :rtype: :class:`<TestConfiguration> <azure.devops.v5_1.test_plan.models.TestConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_configuration_id is not None:
            route_values['testConfigurationId'] = self._serialize.url('test_configuration_id', test_configuration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TestConfiguration', response)

    def get_test_configurations(self, project, continuation_token=None):
        """GetTestConfigurations.
        [Preview API] Get a list of test configurations.
        :param str project: Project ID or project name
        :param str continuation_token: If the list of configurations returned is not complete, a continuation token to query next batch of configurations is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test configurations.
        :rtype: :class:`<GetTestConfigurationsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestConfiguration]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestConfigurationsResponseValue(response_value, continuation_token)

    class GetTestConfigurationsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_configurations method

            :param value:
            :type value: :class:`<[TestConfiguration]> <azure.devops.v5_1.test_plan.models.[TestConfiguration]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_configuration(self, test_configuration_create_update_parameters, project, test_configuartion_id):
        """UpdateTestConfiguration.
        [Preview API] Update a test configuration by its ID.
        :param :class:`<TestConfigurationCreateUpdateParameters> <azure.devops.v5_1.test_plan.models.TestConfigurationCreateUpdateParameters>` test_configuration_create_update_parameters: TestConfigurationCreateUpdateParameters
        :param str project: Project ID or project name
        :param int test_configuartion_id: ID of the test configuration to update.
        :rtype: :class:`<TestConfiguration> <azure.devops.v5_1.test_plan.models.TestConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_configuartion_id is not None:
            query_parameters['testConfiguartionId'] = self._serialize.query('test_configuartion_id', test_configuartion_id, 'int')
        content = self._serialize.body(test_configuration_create_update_parameters, 'TestConfigurationCreateUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='8369318e-38fa-4e84-9043-4b2a75d2c256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestConfiguration', response)

    def create_test_plan(self, test_plan_create_params, project):
        """CreateTestPlan.
        [Preview API] Create a test plan.
        :param :class:`<TestPlanCreateParams> <azure.devops.v5_1.test_plan.models.TestPlanCreateParams>` test_plan_create_params: A testPlanCreateParams object.TestPlanCreateParams
        :param str project: Project ID or project name
        :rtype: :class:`<TestPlan> <azure.devops.v5_1.test_plan.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_plan_create_params, 'TestPlanCreateParams')
        response = self._send(http_method='POST',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def delete_test_plan(self, project, plan_id):
        """DeleteTestPlan.
        [Preview API] Delete a test plan.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan to be deleted.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        self._send(http_method='DELETE',
                   location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_plan_by_id(self, project, plan_id):
        """GetTestPlanById.
        [Preview API] Get a test plan by Id.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan to get.
        :rtype: :class:`<TestPlan> <azure.devops.v5_1.test_plan.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TestPlan', response)

    def get_test_plans(self, project, owner=None, continuation_token=None, include_plan_details=None, filter_active_plans=None):
        """GetTestPlans.
        [Preview API] Get a list of test plans
        :param str project: Project ID or project name
        :param str owner: Filter for test plan by owner ID or name
        :param str continuation_token: If the list of plans returned is not complete, a continuation token to query next batch of plans is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test plans.
        :param bool include_plan_details: Get all properties of the test plan
        :param bool filter_active_plans: Get just the active plans
        :rtype: :class:`<GetTestPlansResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if include_plan_details is not None:
            query_parameters['includePlanDetails'] = self._serialize.query('include_plan_details', include_plan_details, 'bool')
        if filter_active_plans is not None:
            query_parameters['filterActivePlans'] = self._serialize.query('filter_active_plans', filter_active_plans, 'bool')
        response = self._send(http_method='GET',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestPlan]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestPlansResponseValue(response_value, continuation_token)

    class GetTestPlansResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_plans method

            :param value:
            :type value: :class:`<[TestPlan]> <azure.devops.v5_1.test_plan.models.[TestPlan]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_plan(self, test_plan_update_params, project, plan_id):
        """UpdateTestPlan.
        [Preview API] Update a test plan.
        :param :class:`<TestPlanUpdateParams> <azure.devops.v5_1.test_plan.models.TestPlanUpdateParams>` test_plan_update_params: A testPlanUpdateParams object.TestPlanUpdateParams
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan to be updated.
        :rtype: :class:`<TestPlan> <azure.devops.v5_1.test_plan.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        content = self._serialize.body(test_plan_update_params, 'TestPlanUpdateParams')
        response = self._send(http_method='PATCH',
                              location_id='0e292477-a0c2-47f3-a9b6-34f153d627f4',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def get_suite_entries(self, project, suite_id, suite_entry_type=None):
        """GetSuiteEntries.
        [Preview API] Get a list of test suite entries in the test suite.
        :param str project: Project ID or project name
        :param int suite_id: Id of the parent suite.
        :param str suite_entry_type:
        :rtype: [SuiteEntry]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if suite_entry_type is not None:
            query_parameters['suiteEntryType'] = self._serialize.query('suite_entry_type', suite_entry_type, 'str')
        response = self._send(http_method='GET',
                              location_id='d6733edf-72f1-4252-925b-c560dfe9b75a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SuiteEntry]', self._unwrap_collection(response))

    def reorder_suite_entries(self, suite_entries, project, suite_id):
        """ReorderSuiteEntries.
        [Preview API] Reorder test suite entries in the test suite.
        :param [SuiteEntryUpdateParams] suite_entries: List of SuiteEntry to reorder.
        :param str project: Project ID or project name
        :param int suite_id: Id of the parent test suite.
        :rtype: [SuiteEntry]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_entries, '[SuiteEntryUpdateParams]')
        response = self._send(http_method='PATCH',
                              location_id='d6733edf-72f1-4252-925b-c560dfe9b75a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[SuiteEntry]', self._unwrap_collection(response))

    def create_test_suite(self, test_suite_create_params, project, plan_id):
        """CreateTestSuite.
        [Preview API] Create test suite.
        :param :class:`<TestSuiteCreateParams> <azure.devops.v5_1.test_plan.models.TestSuiteCreateParams>` test_suite_create_params: Parameters for suite creation
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :rtype: :class:`<TestSuite> <azure.devops.v5_1.test_plan.models.TestSuite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        content = self._serialize.body(test_suite_create_params, 'TestSuiteCreateParams')
        response = self._send(http_method='POST',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSuite', response)

    def delete_test_suite(self, project, plan_id, suite_id):
        """DeleteTestSuite.
        [Preview API] Delete test suite.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suite.
        :param int suite_id: ID of the test suite to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        self._send(http_method='DELETE',
                   location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_suite_by_id(self, project, plan_id, suite_id, expand=None):
        """GetTestSuiteById.
        [Preview API] Get test suite by suite id.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :param int suite_id: ID of the suite to get.
        :param str expand: Include the children suites and testers details
        :rtype: :class:`<TestSuite> <azure.devops.v5_1.test_plan.models.TestSuite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestSuite', response)

    def get_test_suites_for_plan(self, project, plan_id, expand=None, continuation_token=None, as_tree_view=None):
        """GetTestSuitesForPlan.
        [Preview API] Get test suites for plan.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which suites are requested.
        :param str expand: Include the children suites and testers details.
        :param str continuation_token: If the list of suites returned is not complete, a continuation token to query next batch of suites is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test suites.
        :param bool as_tree_view: If the suites returned should be in a tree structure.
        :rtype: :class:`<GetTestSuitesForPlanResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if as_tree_view is not None:
            query_parameters['asTreeView'] = self._serialize.query('as_tree_view', as_tree_view, 'bool')
        response = self._send(http_method='GET',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestSuite]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestSuitesForPlanResponseValue(response_value, continuation_token)

    class GetTestSuitesForPlanResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_suites_for_plan method

            :param value:
            :type value: :class:`<[TestSuite]> <azure.devops.v5_1.test_plan.models.[TestSuite]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_suite(self, test_suite_update_params, project, plan_id, suite_id):
        """UpdateTestSuite.
        [Preview API] Update test suite.
        :param :class:`<TestSuiteUpdateParams> <azure.devops.v5_1.test_plan.models.TestSuiteUpdateParams>` test_suite_update_params: Parameters for suite updation
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :param int suite_id: ID of the parent suite.
        :rtype: :class:`<TestSuite> <azure.devops.v5_1.test_plan.models.TestSuite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(test_suite_update_params, 'TestSuiteUpdateParams')
        response = self._send(http_method='PATCH',
                              location_id='1046d5d3-ab61-4ca7-a65a-36118a978256',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSuite', response)

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

    def add_test_cases_to_suite(self, suite_test_case_create_update_parameters, project, plan_id, suite_id):
        """AddTestCasesToSuite.
        [Preview API] Add test cases to a suite with specified configurations
        :param [SuiteTestCaseCreateUpdateParameters] suite_test_case_create_update_parameters: SuiteTestCaseCreateUpdateParameters object.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan to which test cases are to be added.
        :param int suite_id: ID of the test suite to which test cases are to be added.
        :rtype: [TestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_test_case_create_update_parameters, '[SuiteTestCaseCreateUpdateParameters]')
        response = self._send(http_method='POST',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def get_test_case(self, project, plan_id, suite_id, test_case_ids, wit_fields=None, return_identity_ref=None):
        """GetTestCase.
        [Preview API] Get Test Cases For a Suite.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which test cases are requested.
        :param int suite_id: ID of the test suite for which test cases are requested.
        :param str test_case_ids: Test Case Ids to be fetched.
        :param str wit_fields: Get the list of witFields.
        :param bool return_identity_ref: If set to true, returns all identity fields, like AssignedTo, ActivatedBy etc., as IdentityRef objects. If set to false, these fields are returned as unique names in string format. This is false by default.
        :rtype: [TestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        response = self._send(http_method='GET',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def get_test_case_list(self, project, plan_id, suite_id, test_ids=None, configuration_ids=None, wit_fields=None, continuation_token=None, return_identity_ref=None, expand=None):
        """GetTestCaseList.
        [Preview API] Get Test Case List return those test cases which have all the configuration Ids as mentioned in the optional paramter. If configuration Ids is null, it return all the test cases
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which test cases are requested.
        :param int suite_id: ID of the test suite for which test cases are requested.
        :param str test_ids: Test Case Ids to be fetched.
        :param str configuration_ids: Fetch Test Cases which contains all the configuration Ids specified.
        :param str wit_fields: Get the list of witFields.
        :param str continuation_token: If the list of test cases returned is not complete, a continuation token to query next batch of test cases is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test cases.
        :param bool return_identity_ref: If set to true, returns all identity fields, like AssignedTo, ActivatedBy etc., as IdentityRef objects. If set to false, these fields are returned as unique names in string format. This is false by default.
        :param bool expand: If set to false, will get a smaller payload containing only basic details about the suite test case object
        :rtype: :class:`<GetTestCaseListResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if test_ids is not None:
            query_parameters['testIds'] = self._serialize.query('test_ids', test_ids, 'str')
        if configuration_ids is not None:
            query_parameters['configurationIds'] = self._serialize.query('configuration_ids', configuration_ids, 'str')
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        if expand is not None:
            query_parameters['expand'] = self._serialize.query('expand', expand, 'bool')
        response = self._send(http_method='GET',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestCase]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestCaseListResponseValue(response_value, continuation_token)

    class GetTestCaseListResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_case_list method

            :param value:
            :type value: :class:`<[TestCase]> <azure.devops.v5_1.test_plan.models.[TestCase]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def remove_test_cases_from_suite(self, project, plan_id, suite_id, test_case_ids):
        """RemoveTestCasesFromSuite.
        [Preview API] Removes test cases from a suite based on the list of test case Ids provided.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan from which test cases are to be removed.
        :param int suite_id: ID of the test suite from which test cases are to be removed.
        :param str test_case_ids: Test Case Ids to be removed.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        self._send(http_method='DELETE',
                   location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                   version='5.1-preview.2',
                   route_values=route_values)

    def update_suite_test_cases(self, suite_test_case_create_update_parameters, project, plan_id, suite_id):
        """UpdateSuiteTestCases.
        [Preview API] Update the configurations for test cases
        :param [SuiteTestCaseCreateUpdateParameters] suite_test_case_create_update_parameters: A SuiteTestCaseCreateUpdateParameters object.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan to which test cases are to be updated.
        :param int suite_id: ID of the test suite to which test cases are to be updated.
        :rtype: [TestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_test_case_create_update_parameters, '[SuiteTestCaseCreateUpdateParameters]')
        response = self._send(http_method='PATCH',
                              location_id='a9bd61ac-45cf-4d13-9441-43dcd01edf8d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCase]', self._unwrap_collection(response))

    def delete_test_case(self, project, test_case_id):
        """DeleteTestCase.
        [Preview API] Delete a test case.
        :param str project: Project ID or project name
        :param int test_case_id: Id of test case to be deleted.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_case_id is not None:
            route_values['testCaseId'] = self._serialize.url('test_case_id', test_case_id, 'int')
        self._send(http_method='DELETE',
                   location_id='29006fb5-816b-4ff7-a329-599943569229',
                   version='5.1-preview.1',
                   route_values=route_values)

    def clone_test_plan(self, clone_request_body, project, deep_clone=None):
        """CloneTestPlan.
        [Preview API] Clone test plan
        :param :class:`<CloneTestPlanParams> <azure.devops.v5_1.test_plan.models.CloneTestPlanParams>` clone_request_body: Plan Clone Request Body detail TestPlanCloneRequest
        :param str project: Project ID or project name
        :param bool deep_clone: Clones all the associated test cases as well
        :rtype: :class:`<CloneTestPlanOperationInformation> <azure.devops.v5_1.test_plan.models.CloneTestPlanOperationInformation>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if deep_clone is not None:
            query_parameters['deepClone'] = self._serialize.query('deep_clone', deep_clone, 'bool')
        content = self._serialize.body(clone_request_body, 'CloneTestPlanParams')
        response = self._send(http_method='POST',
                              location_id='e65df662-d8a3-46c7-ae1c-14e2d4df57e1',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('CloneTestPlanOperationInformation', response)

    def get_clone_information(self, project, clone_operation_id):
        """GetCloneInformation.
        [Preview API] Get clone information.
        :param str project: Project ID or project name
        :param int clone_operation_id: Operation ID returned when we queue a clone operation
        :rtype: :class:`<CloneTestPlanOperationInformation> <azure.devops.v5_1.test_plan.models.CloneTestPlanOperationInformation>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if clone_operation_id is not None:
            route_values['cloneOperationId'] = self._serialize.url('clone_operation_id', clone_operation_id, 'int')
        response = self._send(http_method='GET',
                              location_id='e65df662-d8a3-46c7-ae1c-14e2d4df57e1',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('CloneTestPlanOperationInformation', response)

    def get_points(self, project, plan_id, suite_id, point_ids, return_identity_ref=None):
        """GetPoints.
        [Preview API] Get a list of points based on point Ids provided.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which test points are requested.
        :param int suite_id: ID of the test suite for which test points are requested.
        :param str point_ids: ID of test points to be fetched.
        :param bool return_identity_ref: If set to true, returns the AssignedTo field in TestCaseReference as IdentityRef object.
        :rtype: [TestPoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if point_ids is not None:
            route_values['pointIds'] = self._serialize.url('point_ids', point_ids, 'str')
        query_parameters = {}
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        response = self._send(http_method='GET',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def get_points_list(self, project, plan_id, suite_id, test_point_ids=None, test_case_id=None, continuation_token=None, return_identity_ref=None, include_point_details=None):
        """GetPointsList.
        [Preview API] Get all the points inside a suite based on some filters
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which test points are requested.
        :param int suite_id: ID of the test suite for which test points are requested
        :param str test_point_ids: ID of test points to fetch.
        :param str test_case_id: Get Test Points for specific test case Ids.
        :param str continuation_token: If the list of test point returned is not complete, a continuation token to query next batch of test points is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test points.
        :param bool return_identity_ref: If set to true, returns the AssignedTo field in TestCaseReference as IdentityRef object.
        :param bool include_point_details: If set to false, returns only necessary information
        :rtype: :class:`<GetPointsListResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if test_point_ids is not None:
            query_parameters['testPointIds'] = self._serialize.query('test_point_ids', test_point_ids, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if return_identity_ref is not None:
            query_parameters['returnIdentityRef'] = self._serialize.query('return_identity_ref', return_identity_ref, 'bool')
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestPoint]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetPointsListResponseValue(response_value, continuation_token)

    class GetPointsListResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_points_list method

            :param value:
            :type value: :class:`<[TestPoint]> <azure.devops.v5_1.test_plan.models.[TestPoint]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_points(self, test_point_update_params, project, plan_id, suite_id):
        """UpdateTestPoints.
        [Preview API] Update Test Points. This is used to Reset test point to active, update the outcome of a test point or update the tester of a test point
        :param [TestPointUpdateParams] test_point_update_params: A TestPointUpdateParams Object.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan for which test points are requested.
        :param int suite_id: ID of the test suite for which test points are requested.
        :rtype: [TestPoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(test_point_update_params, '[TestPointUpdateParams]')
        response = self._send(http_method='PATCH',
                              location_id='52df686e-bae4-4334-b0ee-b6cf4e6f6b73',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def clone_test_suite(self, clone_request_body, project, deep_clone=None):
        """CloneTestSuite.
        [Preview API] Clone test suite
        :param :class:`<CloneTestSuiteParams> <azure.devops.v5_1.test_plan.models.CloneTestSuiteParams>` clone_request_body: Suite Clone Request Body detail TestSuiteCloneRequest
        :param str project: Project ID or project name
        :param bool deep_clone: Clones all the associated test cases as well
        :rtype: :class:`<CloneTestSuiteOperationInformation> <azure.devops.v5_1.test_plan.models.CloneTestSuiteOperationInformation>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if deep_clone is not None:
            query_parameters['deepClone'] = self._serialize.query('deep_clone', deep_clone, 'bool')
        content = self._serialize.body(clone_request_body, 'CloneTestSuiteParams')
        response = self._send(http_method='POST',
                              location_id='181d4c97-0e98-4ee2-ad6a-4cada675e555',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('CloneTestSuiteOperationInformation', response)

    def get_suite_clone_information(self, project, clone_operation_id):
        """GetSuiteCloneInformation.
        [Preview API] Get clone information.
        :param str project: Project ID or project name
        :param int clone_operation_id: Operation ID returned when we queue a clone operation
        :rtype: :class:`<CloneTestSuiteOperationInformation> <azure.devops.v5_1.test_plan.models.CloneTestSuiteOperationInformation>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if clone_operation_id is not None:
            route_values['cloneOperationId'] = self._serialize.url('clone_operation_id', clone_operation_id, 'int')
        response = self._send(http_method='GET',
                              location_id='181d4c97-0e98-4ee2-ad6a-4cada675e555',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('CloneTestSuiteOperationInformation', response)

    def create_test_variable(self, test_variable_create_update_parameters, project):
        """CreateTestVariable.
        [Preview API] Create a test variable.
        :param :class:`<TestVariableCreateUpdateParameters> <azure.devops.v5_1.test_plan.models.TestVariableCreateUpdateParameters>` test_variable_create_update_parameters: TestVariableCreateUpdateParameters
        :param str project: Project ID or project name
        :rtype: :class:`<TestVariable> <azure.devops.v5_1.test_plan.models.TestVariable>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_variable_create_update_parameters, 'TestVariableCreateUpdateParameters')
        response = self._send(http_method='POST',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestVariable', response)

    def delete_test_variable(self, project, test_variable_id):
        """DeleteTestVariable.
        [Preview API] Delete a test variable by its ID.
        :param str project: Project ID or project name
        :param int test_variable_id: ID of the test variable to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_variable_by_id(self, project, test_variable_id):
        """GetTestVariableById.
        [Preview API] Get a test variable by its ID.
        :param str project: Project ID or project name
        :param int test_variable_id: ID of the test variable to get.
        :rtype: :class:`<TestVariable> <azure.devops.v5_1.test_plan.models.TestVariable>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TestVariable', response)

    def get_test_variables(self, project, continuation_token=None):
        """GetTestVariables.
        [Preview API] Get a list of test variables.
        :param str project: Project ID or project name
        :param str continuation_token: If the list of variables returned is not complete, a continuation token to query next batch of variables is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of test variables.
        :rtype: :class:`<GetTestVariablesResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestVariable]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestVariablesResponseValue(response_value, continuation_token)

    class GetTestVariablesResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_variables method

            :param value:
            :type value: :class:`<[TestVariable]> <azure.devops.v5_1.test_plan.models.[TestVariable]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_variable(self, test_variable_create_update_parameters, project, test_variable_id):
        """UpdateTestVariable.
        [Preview API] Update a test variable by its ID.
        :param :class:`<TestVariableCreateUpdateParameters> <azure.devops.v5_1.test_plan.models.TestVariableCreateUpdateParameters>` test_variable_create_update_parameters: TestVariableCreateUpdateParameters
        :param str project: Project ID or project name
        :param int test_variable_id: ID of the test variable to update.
        :rtype: :class:`<TestVariable> <azure.devops.v5_1.test_plan.models.TestVariable>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_variable_id is not None:
            route_values['testVariableId'] = self._serialize.url('test_variable_id', test_variable_id, 'int')
        content = self._serialize.body(test_variable_create_update_parameters, 'TestVariableCreateUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='2c61fac6-ac4e-45a5-8c38-1c2b8fd8ea6c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestVariable', response)

