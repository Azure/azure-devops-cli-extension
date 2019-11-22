# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.test import models


class TestClient(Client):
    """Test
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TestClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'c2aa639c-3ccc-4740-b3b6-ce2a1e1d984e'

    def get_action_results(self, project, run_id, test_case_result_id, iteration_id, action_path=None):
        """GetActionResults.
        Gets the action results for an iteration in a test result.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result that contains the iterations.
        :param int iteration_id: ID of the iteration that contains the actions.
        :param str action_path: Path of a specific action, used to get just that action.
        :rtype: [TestActionResultModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        if action_path is not None:
            route_values['actionPath'] = self._serialize.url('action_path', action_path, 'str')
        response = self._send(http_method='GET',
                              location_id='eaf40c31-ff84-4062-aafd-d5664be11a37',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[TestActionResultModel]', self._unwrap_collection(response))

    def get_test_iteration(self, project, run_id, test_case_result_id, iteration_id, include_action_results=None):
        """GetTestIteration.
        Get iteration for a result
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result that contains the iterations.
        :param int iteration_id: Id of the test results Iteration.
        :param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.
        :rtype: :class:`<TestIterationDetailsModel> <azure.devops.v5_1.test.models.TestIterationDetailsModel>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if include_action_results is not None:
            query_parameters['includeActionResults'] = self._serialize.query('include_action_results', include_action_results, 'bool')
        response = self._send(http_method='GET',
                              location_id='73eb9074-3446-4c44-8296-2f811950ff8d',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestIterationDetailsModel', response)

    def get_test_iterations(self, project, run_id, test_case_result_id, include_action_results=None):
        """GetTestIterations.
        Get iterations for a result
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result that contains the iterations.
        :param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.
        :rtype: [TestIterationDetailsModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if include_action_results is not None:
            query_parameters['includeActionResults'] = self._serialize.query('include_action_results', include_action_results, 'bool')
        response = self._send(http_method='GET',
                              location_id='73eb9074-3446-4c44-8296-2f811950ff8d',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestIterationDetailsModel]', self._unwrap_collection(response))

    def get_result_parameters(self, project, run_id, test_case_result_id, iteration_id, param_name=None):
        """GetResultParameters.
        Get a list of parameterized results
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result that contains the iterations.
        :param int iteration_id: ID of the iteration that contains the parameterized results.
        :param str param_name: Name of the parameter.
        :rtype: [TestResultParameterModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if param_name is not None:
            query_parameters['paramName'] = self._serialize.query('param_name', param_name, 'str')
        response = self._send(http_method='GET',
                              location_id='7c69810d-3354-4af3-844a-180bd25db08a',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestResultParameterModel]', self._unwrap_collection(response))

    def get_point(self, project, plan_id, suite_id, point_ids, wit_fields=None):
        """GetPoint.
        Get a test point.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan.
        :param int suite_id: ID of the suite that contains the point.
        :param int point_ids: ID of the test point to get.
        :param str wit_fields: Comma-separated list of work item field names.
        :rtype: :class:`<TestPoint> <azure.devops.v5_1.test.models.TestPoint>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if point_ids is not None:
            route_values['pointIds'] = self._serialize.url('point_ids', point_ids, 'int')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        response = self._send(http_method='GET',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestPoint', response)

    def get_points(self, project, plan_id, suite_id, wit_fields=None, configuration_id=None, test_case_id=None, test_point_ids=None, include_point_details=None, skip=None, top=None):
        """GetPoints.
        Get a list of test points.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan.
        :param int suite_id: ID of the suite that contains the points.
        :param str wit_fields: Comma-separated list of work item field names.
        :param str configuration_id: Get test points for specific configuration.
        :param str test_case_id: Get test points for a specific test case, valid when configurationId is not set.
        :param str test_point_ids: Get test points for comma-separated list of test point IDs, valid only when configurationId and testCaseId are not set.
        :param bool include_point_details: Include all properties for the test point.
        :param int skip: Number of test points to skip..
        :param int top: Number of test points to return.
        :rtype: [TestPoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if configuration_id is not None:
            query_parameters['configurationId'] = self._serialize.query('configuration_id', configuration_id, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'str')
        if test_point_ids is not None:
            query_parameters['testPointIds'] = self._serialize.query('test_point_ids', test_point_ids, 'str')
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def update_test_points(self, point_update_model, project, plan_id, suite_id, point_ids):
        """UpdateTestPoints.
        Update test points.
        :param :class:`<PointUpdateModel> <azure.devops.v5_1.test.models.PointUpdateModel>` point_update_model: Data to update.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan.
        :param int suite_id: ID of the suite that contains the points.
        :param str point_ids: ID of the test point to get. Use a comma-separated list of IDs to update multiple test points.
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
        content = self._serialize.body(point_update_model, 'PointUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def add_test_results_to_test_run(self, results, project, run_id):
        """AddTestResultsToTestRun.
        Add test results to a test run.
        :param [TestCaseResult] results: List of test results to add.
        :param str project: Project ID or project name
        :param int run_id: Test run ID into which test results to add.
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='POST',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_result_by_id(self, project, run_id, test_case_result_id, details_to_include=None):
        """GetTestResultById.
        Get a test result for a test run.
        :param str project: Project ID or project name
        :param int run_id: Test run ID of a test result to fetch.
        :param int test_case_result_id: Test result ID.
        :param str details_to_include: Details to include with test results. Default is None. Other values are Iterations, WorkItems and SubResults.
        :rtype: :class:`<TestCaseResult> <azure.devops.v5_1.test.models.TestCaseResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        response = self._send(http_method='GET',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestCaseResult', response)

    def get_test_results(self, project, run_id, details_to_include=None, skip=None, top=None, outcomes=None):
        """GetTestResults.
        Get test results for a test run.
        :param str project: Project ID or project name
        :param int run_id: Test run ID of test results to fetch.
        :param str details_to_include: Details to include with test results. Default is None. Other values are Iterations and WorkItems.
        :param int skip: Number of test results to skip from beginning.
        :param int top: Number of test results to return. Maximum is 1000 when detailsToInclude is None and 200 otherwise.
        :param [TestOutcome] outcomes: Comma separated list of test outcomes to filter test results.
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        response = self._send(http_method='GET',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def update_test_results(self, results, project, run_id):
        """UpdateTestResults.
        Update test results in a test run.
        :param [TestCaseResult] results: List of test results to update.
        :param str project: Project ID or project name
        :param int run_id: Test run ID whose test results to update.
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='PATCH',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_run_statistics(self, project, run_id):
        """GetTestRunStatistics.
        Get test run statistics , used when we want to get summary of a run by outcome.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: :class:`<TestRunStatistic> <azure.devops.v5_1.test.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0a42c424-d764-4a16-a2d5-5c85f87d0ae8',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

    def create_test_run(self, test_run, project):
        """CreateTestRun.
        Create new test run.
        :param :class:`<RunCreateModel> <azure.devops.v5_1.test.models.RunCreateModel>` test_run: Run details RunCreateModel
        :param str project: Project ID or project name
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_run, 'RunCreateModel')
        response = self._send(http_method='POST',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def delete_test_run(self, project, run_id):
        """DeleteTestRun.
        Delete a test run by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        self._send(http_method='DELETE',
                   location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                   version='5.1',
                   route_values=route_values)

    def get_test_run_by_id(self, project, run_id, include_details=None):
        """GetTestRunById.
        Get a test run by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :param bool include_details: Default value is true. It includes details like run statistics, release, build, test environment, post process state, and more.
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None):
        """GetTestRuns.
        Get a list of test runs.
        :param str project: Project ID or project name
        :param str build_uri: URI of the build that the runs used.
        :param str owner: Team foundation ID of the owner of the runs.
        :param str tmi_run_id:
        :param int plan_id: ID of the test plan that the runs are a part of.
        :param bool include_run_details: If true, include all the properties of the runs.
        :param bool automated: If true, only returns automated runs.
        :param int skip: Number of test runs to skip.
        :param int top: Number of test runs to return.
        :rtype: [TestRun]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_uri is not None:
            query_parameters['buildUri'] = self._serialize.query('build_uri', build_uri, 'str')
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if tmi_run_id is not None:
            query_parameters['tmiRunId'] = self._serialize.query('tmi_run_id', tmi_run_id, 'str')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'int')
        if include_run_details is not None:
            query_parameters['includeRunDetails'] = self._serialize.query('include_run_details', include_run_details, 'bool')
        if automated is not None:
            query_parameters['automated'] = self._serialize.query('automated', automated, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def query_test_runs(self, project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None):
        """QueryTestRuns.
        Query Test Runs based on filters. Mandatory fields are minLastUpdatedDate and maxLastUpdatedDate.
        :param str project: Project ID or project name
        :param datetime min_last_updated_date: Minimum Last Modified Date of run to be queried (Mandatory).
        :param datetime max_last_updated_date: Maximum Last Modified Date of run to be queried (Mandatory, difference between min and max date can be atmost 7 days).
        :param str state: Current state of the Runs to be queried.
        :param [int] plan_ids: Plan Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param bool is_automated: Automation type of the Runs to be queried.
        :param str publish_context: PublishContext of the Runs to be queried.
        :param [int] build_ids: Build Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param [int] build_def_ids: Build Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param str branch_name: Source Branch name of the Runs to be queried.
        :param [int] release_ids: Release Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param [int] release_def_ids: Release Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param [int] release_env_ids: Release Environment Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param [int] release_env_def_ids: Release Environment Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).
        :param str run_title: Run Title of the Runs to be queried.
        :param int top: Number of runs to be queried. Limit is 100
        :param str continuation_token: continuationToken received from previous batch or null for first batch. It is not supposed to be created (or altered, if received from last batch) by user.
        :rtype: :class:`<QueryTestRunsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if min_last_updated_date is not None:
            query_parameters['minLastUpdatedDate'] = self._serialize.query('min_last_updated_date', min_last_updated_date, 'iso-8601')
        if max_last_updated_date is not None:
            query_parameters['maxLastUpdatedDate'] = self._serialize.query('max_last_updated_date', max_last_updated_date, 'iso-8601')
        if state is not None:
            query_parameters['state'] = self._serialize.query('state', state, 'str')
        if plan_ids is not None:
            plan_ids = ",".join(map(str, plan_ids))
            query_parameters['planIds'] = self._serialize.query('plan_ids', plan_ids, 'str')
        if is_automated is not None:
            query_parameters['isAutomated'] = self._serialize.query('is_automated', is_automated, 'bool')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if build_def_ids is not None:
            build_def_ids = ",".join(map(str, build_def_ids))
            query_parameters['buildDefIds'] = self._serialize.query('build_def_ids', build_def_ids, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if release_ids is not None:
            release_ids = ",".join(map(str, release_ids))
            query_parameters['releaseIds'] = self._serialize.query('release_ids', release_ids, 'str')
        if release_def_ids is not None:
            release_def_ids = ",".join(map(str, release_def_ids))
            query_parameters['releaseDefIds'] = self._serialize.query('release_def_ids', release_def_ids, 'str')
        if release_env_ids is not None:
            release_env_ids = ",".join(map(str, release_env_ids))
            query_parameters['releaseEnvIds'] = self._serialize.query('release_env_ids', release_env_ids, 'str')
        if release_env_def_ids is not None:
            release_env_def_ids = ",".join(map(str, release_env_def_ids))
            query_parameters['releaseEnvDefIds'] = self._serialize.query('release_env_def_ids', release_env_def_ids, 'str')
        if run_title is not None:
            query_parameters['runTitle'] = self._serialize.query('run_title', run_title, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TestRun]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.QueryTestRunsResponseValue(response_value, continuation_token)

    class QueryTestRunsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the query_test_runs method

            :param value:
            :type value: :class:`<[TestRun]> <azure.devops.v5_1.test.models.[TestRun]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_run(self, run_update_model, project, run_id):
        """UpdateTestRun.
        Update test run by its ID.
        :param :class:`<RunUpdateModel> <azure.devops.v5_1.test.models.RunUpdateModel>` run_update_model: Run details RunUpdateModel
        :param str project: Project ID or project name
        :param int run_id: ID of the run to update.
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(run_update_model, 'RunUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def add_test_cases_to_suite(self, project, plan_id, suite_id, test_case_ids):
        """AddTestCasesToSuite.
        Add test cases to suite.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suite.
        :param int suite_id: ID of the test suite to which the test cases must be added.
        :param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.
        :rtype: [SuiteTestCase]
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
        route_values['action'] = 'TestCases'
        response = self._send(http_method='POST',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def get_test_case_by_id(self, project, plan_id, suite_id, test_case_ids):
        """GetTestCaseById.
        Get a specific test case in a test suite with test case id.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :param int suite_id: ID of the suite that contains the test case.
        :param int test_case_ids: ID of the test case to get.
        :rtype: :class:`<SuiteTestCase> <azure.devops.v5_1.test.models.SuiteTestCase>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'int')
        route_values['action'] = 'TestCases'
        response = self._send(http_method='GET',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('SuiteTestCase', response)

    def get_test_cases(self, project, plan_id, suite_id):
        """GetTestCases.
        Get all test cases in a suite.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :param int suite_id: ID of the suite to get.
        :rtype: [SuiteTestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        route_values['action'] = 'TestCases'
        response = self._send(http_method='GET',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def remove_test_cases_from_suite_url(self, project, plan_id, suite_id, test_case_ids):
        """RemoveTestCasesFromSuiteUrl.
        The test points associated with the test cases are removed from the test suite. The test case work item is not deleted from the system. See test cases resource to delete a test case permanently.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suite.
        :param int suite_id: ID of the suite to get.
        :param str test_case_ids: IDs of the test cases to remove from the suite.
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
        route_values['action'] = 'TestCases'
        self._send(http_method='DELETE',
                   location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                   version='5.1',
                   route_values=route_values)

    def update_suite_test_cases(self, suite_test_case_update_model, project, plan_id, suite_id, test_case_ids):
        """UpdateSuiteTestCases.
        Updates the properties of the test case association in a suite.
        :param :class:`<SuiteTestCaseUpdateModel> <azure.devops.v5_1.test.models.SuiteTestCaseUpdateModel>` suite_test_case_update_model: Model for updation of the properties of test case suite association.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suite.
        :param int suite_id: ID of the test suite to which the test cases must be added.
        :param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.
        :rtype: [SuiteTestCase]
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
        route_values['action'] = 'TestCases'
        content = self._serialize.body(suite_test_case_update_model, 'SuiteTestCaseUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

