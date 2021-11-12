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
        [Preview API] Gets the action results for an iteration in a test result.
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
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('[TestActionResultModel]', self._unwrap_collection(response))

    def create_test_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id):
        """CreateTestResultAttachment.
        [Preview API] Attach a file to a test result.
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v6_0.test.models.TestAttachmentRequestModel>` attachment_request_model: Attachment details TestAttachmentRequestModel
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result against which attachment has to be uploaded.
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v6_0.test.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def create_test_sub_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id, test_sub_result_id):
        """CreateTestSubResultAttachment.
        [Preview API] Attach a file to a test result
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v6_0.test.models.TestAttachmentRequestModel>` attachment_request_model: Attachment Request Model.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test results that contains sub result.
        :param int test_sub_result_id: ID of the test sub results against which attachment has to be uploaded.
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v6_0.test.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def get_test_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentContent.
        [Preview API] Download a test result attachment by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the testCaseResultId.
        :param int test_case_result_id: ID of the test result whose attachment has to be downloaded.
        :param int attachment_id: ID of the test result attachment to be downloaded.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_result_attachments(self, project, run_id, test_case_result_id):
        """GetTestResultAttachments.
        [Preview API] Get list of test result attachments reference.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result.
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentZip.
        [Preview API] Download a test result attachment by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the testCaseResultId.
        :param int test_case_result_id: ID of the test result whose attachment has to be downloaded.
        :param int attachment_id: ID of the test result attachment to be downloaded.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_sub_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentContent.
        [Preview API] Download a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test results that contains sub result.
        :param int attachment_id: ID of the test result attachment to be downloaded
        :param int test_sub_result_id: ID of the test sub result whose attachment has to be downloaded
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_sub_result_attachments(self, project, run_id, test_case_result_id, test_sub_result_id):
        """GetTestSubResultAttachments.
        [Preview API] Get list of test sub result attachments
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test results that contains sub result.
        :param int test_sub_result_id: ID of the test sub result whose attachment has to be downloaded
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_sub_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentZip.
        [Preview API] Download a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test results that contains sub result.
        :param int attachment_id: ID of the test result attachment to be downloaded
        :param int test_sub_result_id: ID of the test sub result whose attachment has to be downloaded
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2bffebe9-2f0f-4639-9af8-56129e9fed2d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_test_run_attachment(self, attachment_request_model, project, run_id):
        """CreateTestRunAttachment.
        [Preview API] Attach a file to a test run.
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v6_0.test.models.TestAttachmentRequestModel>` attachment_request_model: Attachment details TestAttachmentRequestModel
        :param str project: Project ID or project name
        :param int run_id: ID of the test run against which attachment has to be uploaded.
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v6_0.test.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='4f004af4-a507-489c-9b13-cb62060beb11',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def get_test_run_attachment_content(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentContent.
        [Preview API] Download a test run attachment by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run whose attachment has to be downloaded.
        :param int attachment_id: ID of the test run attachment to be downloaded.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='4f004af4-a507-489c-9b13-cb62060beb11',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_run_attachments(self, project, run_id):
        """GetTestRunAttachments.
        [Preview API] Get list of test run attachments reference.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run.
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='4f004af4-a507-489c-9b13-cb62060beb11',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_run_attachment_zip(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentZip.
        [Preview API] Download a test run attachment by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the test run whose attachment has to be downloaded.
        :param int attachment_id: ID of the test run attachment to be downloaded.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='4f004af4-a507-489c-9b13-cb62060beb11',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_code_coverage(self, project, build_id, flags):
        """GetBuildCodeCoverage.
        [Preview API] Get code coverage data for a build.
        :param str project: Project ID or project name
        :param int build_id: ID of the build for which code coverage data needs to be fetched.
        :param int flags: Value of flags determine the level of code coverage details to be fetched. Flags are additive. Expected Values are 1 for Modules, 2 for Functions, 4 for BlockData.
        :rtype: [BuildCoverage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='77560e8a-4e8c-4d59-894e-a5f264c24444',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildCoverage]', self._unwrap_collection(response))

    def get_test_run_code_coverage(self, project, run_id, flags):
        """GetTestRunCodeCoverage.
        [Preview API] Get code coverage data for a test run
        :param str project: Project ID or project name
        :param int run_id: ID of the test run for which code coverage data needs to be fetched.
        :param int flags: Value of flags determine the level of code coverage details to be fetched. Flags are additive. Expected Values are 1 for Modules, 2 for Functions, 4 for BlockData.
        :rtype: [TestRunCoverage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='9629116f-3b89-4ed8-b358-d4694efda160',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRunCoverage]', self._unwrap_collection(response))

    def get_test_iteration(self, project, run_id, test_case_result_id, iteration_id, include_action_results=None):
        """GetTestIteration.
        [Preview API] Get iteration for a result
        :param str project: Project ID or project name
        :param int run_id: ID of the test run that contains the result.
        :param int test_case_result_id: ID of the test result that contains the iterations.
        :param int iteration_id: Id of the test results Iteration.
        :param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.
        :rtype: :class:`<TestIterationDetailsModel> <azure.devops.v6_0.test.models.TestIterationDetailsModel>`
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestIterationDetailsModel', response)

    def get_test_iterations(self, project, run_id, test_case_result_id, include_action_results=None):
        """GetTestIterations.
        [Preview API] Get iterations for a result
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestIterationDetailsModel]', self._unwrap_collection(response))

    def get_result_parameters(self, project, run_id, test_case_result_id, iteration_id, param_name=None):
        """GetResultParameters.
        [Preview API] Get a list of parameterized results
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestResultParameterModel]', self._unwrap_collection(response))

    def get_point(self, project, plan_id, suite_id, point_ids, wit_fields=None):
        """GetPoint.
        [Preview API] Get a test point.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan.
        :param int suite_id: ID of the suite that contains the point.
        :param int point_ids: ID of the test point to get.
        :param str wit_fields: Comma-separated list of work item field names.
        :rtype: :class:`<TestPoint> <azure.devops.v6_0.test.models.TestPoint>`
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
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestPoint', response)

    def get_points(self, project, plan_id, suite_id, wit_fields=None, configuration_id=None, test_case_id=None, test_point_ids=None, include_point_details=None, skip=None, top=None):
        """GetPoints.
        [Preview API] Get a list of test points.
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
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def update_test_points(self, point_update_model, project, plan_id, suite_id, point_ids):
        """UpdateTestPoints.
        [Preview API] Update test points.
        :param :class:`<PointUpdateModel> <azure.devops.v6_0.test.models.PointUpdateModel>` point_update_model: Data to update.
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
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def get_points_by_query(self, query, project, skip=None, top=None):
        """GetPointsByQuery.
        [Preview API] Get test points using query.
        :param :class:`<TestPointsQuery> <azure.devops.v6_0.test.models.TestPointsQuery>` query: TestPointsQuery to get test points.
        :param str project: Project ID or project name
        :param int skip: Number of test points to skip..
        :param int top: Number of test points to return.
        :rtype: :class:`<TestPointsQuery> <azure.devops.v6_0.test.models.TestPointsQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(query, 'TestPointsQuery')
        response = self._send(http_method='POST',
                              location_id='b4264fd0-a5d1-43e2-82a5-b9c46b7da9ce',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestPointsQuery', response)

    def get_result_retention_settings(self, project):
        """GetResultRetentionSettings.
        [Preview API] Get test result retention settings
        :param str project: Project ID or project name
        :rtype: :class:`<ResultRetentionSettings> <azure.devops.v6_0.test.models.ResultRetentionSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='a3206d9e-fa8d-42d3-88cb-f75c51e69cde',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ResultRetentionSettings', response)

    def update_result_retention_settings(self, retention_settings, project):
        """UpdateResultRetentionSettings.
        [Preview API] Update test result retention settings
        :param :class:`<ResultRetentionSettings> <azure.devops.v6_0.test.models.ResultRetentionSettings>` retention_settings: Test result retention settings details to be updated
        :param str project: Project ID or project name
        :rtype: :class:`<ResultRetentionSettings> <azure.devops.v6_0.test.models.ResultRetentionSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(retention_settings, 'ResultRetentionSettings')
        response = self._send(http_method='PATCH',
                              location_id='a3206d9e-fa8d-42d3-88cb-f75c51e69cde',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ResultRetentionSettings', response)

    def add_test_results_to_test_run(self, results, project, run_id):
        """AddTestResultsToTestRun.
        [Preview API] Add test results to a test run.
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
                              version='6.0-preview.6',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_result_by_id(self, project, run_id, test_case_result_id, details_to_include=None):
        """GetTestResultById.
        [Preview API] Get a test result for a test run.
        :param str project: Project ID or project name
        :param int run_id: Test run ID of a test result to fetch.
        :param int test_case_result_id: Test result ID.
        :param str details_to_include: Details to include with test results. Default is None. Other values are Iterations, WorkItems and SubResults.
        :rtype: :class:`<TestCaseResult> <azure.devops.v6_0.test.models.TestCaseResult>`
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
                              version='6.0-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestCaseResult', response)

    def get_test_results(self, project, run_id, details_to_include=None, skip=None, top=None, outcomes=None):
        """GetTestResults.
        [Preview API] Get test results for a test run.
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
                              version='6.0-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def update_test_results(self, results, project, run_id):
        """UpdateTestResults.
        [Preview API] Update test results in a test run.
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
                              version='6.0-preview.6',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_run_statistics(self, project, run_id):
        """GetTestRunStatistics.
        [Preview API] Get test run statistics , used when we want to get summary of a run by outcome.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: :class:`<TestRunStatistic> <azure.devops.v6_0.test.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0a42c424-d764-4a16-a2d5-5c85f87d0ae8',
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

    def create_test_run(self, test_run, project):
        """CreateTestRun.
        [Preview API] Create new test run.
        :param :class:`<RunCreateModel> <azure.devops.v6_0.test.models.RunCreateModel>` test_run: Run details RunCreateModel
        :param str project: Project ID or project name
        :rtype: :class:`<TestRun> <azure.devops.v6_0.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_run, 'RunCreateModel')
        response = self._send(http_method='POST',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def delete_test_run(self, project, run_id):
        """DeleteTestRun.
        [Preview API] Delete a test run by its ID.
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
                   version='6.0-preview.3',
                   route_values=route_values)

    def get_test_run_by_id(self, project, run_id, include_details=None):
        """GetTestRunById.
        [Preview API] Get a test run by its ID.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :param bool include_details: Default value is true. It includes details like run statistics, release, build, test environment, post process state, and more.
        :rtype: :class:`<TestRun> <azure.devops.v6_0.test.models.TestRun>`
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None):
        """GetTestRuns.
        [Preview API] Get a list of test runs.
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def query_test_runs(self, project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None):
        """QueryTestRuns.
        [Preview API] Query Test Runs based on filters. Mandatory fields are minLastUpdatedDate and maxLastUpdatedDate.
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
        :rtype: :class:`<[TestRun]> <azure.devops.v6_0.test.models.[TestRun]>`
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def update_test_run(self, run_update_model, project, run_id):
        """UpdateTestRun.
        [Preview API] Update test run by its ID.
        :param :class:`<RunUpdateModel> <azure.devops.v6_0.test.models.RunUpdateModel>` run_update_model: Run details RunUpdateModel
        :param str project: Project ID or project name
        :param int run_id: ID of the run to update.
        :rtype: :class:`<TestRun> <azure.devops.v6_0.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(run_update_model, 'RunUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def create_test_session(self, test_session, team_context):
        """CreateTestSession.
        [Preview API] Create a test session
        :param :class:`<TestSession> <azure.devops.v6_0.test.models.TestSession>` test_session: Test session details for creation
        :param :class:`<TeamContext> <azure.devops.v6_0.test.models.TeamContext>` team_context: The team context for the operation
        :rtype: :class:`<TestSession> <azure.devops.v6_0.test.models.TestSession>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(test_session, 'TestSession')
        response = self._send(http_method='POST',
                              location_id='1500b4b4-6c69-4ca6-9b18-35e9e97fe2ac',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSession', response)

    def get_test_sessions(self, team_context, period=None, all_sessions=None, include_all_properties=None, source=None, include_only_completed_sessions=None):
        """GetTestSessions.
        [Preview API] Get a list of test sessions
        :param :class:`<TeamContext> <azure.devops.v6_0.test.models.TeamContext>` team_context: The team context for the operation
        :param int period: Period in days from now, for which test sessions are fetched.
        :param bool all_sessions: If false, returns test sessions for current user. Otherwise, it returns test sessions for all users
        :param bool include_all_properties: If true, it returns all properties of the test sessions. Otherwise, it returns the skinny version.
        :param str source: Source of the test session.
        :param bool include_only_completed_sessions: If true, it returns test sessions in completed state. Otherwise, it returns test sessions for all states
        :rtype: [TestSession]
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if period is not None:
            query_parameters['period'] = self._serialize.query('period', period, 'int')
        if all_sessions is not None:
            query_parameters['allSessions'] = self._serialize.query('all_sessions', all_sessions, 'bool')
        if include_all_properties is not None:
            query_parameters['includeAllProperties'] = self._serialize.query('include_all_properties', include_all_properties, 'bool')
        if source is not None:
            query_parameters['source'] = self._serialize.query('source', source, 'str')
        if include_only_completed_sessions is not None:
            query_parameters['includeOnlyCompletedSessions'] = self._serialize.query('include_only_completed_sessions', include_only_completed_sessions, 'bool')
        response = self._send(http_method='GET',
                              location_id='1500b4b4-6c69-4ca6-9b18-35e9e97fe2ac',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestSession]', self._unwrap_collection(response))

    def update_test_session(self, test_session, team_context):
        """UpdateTestSession.
        [Preview API] Update a test session
        :param :class:`<TestSession> <azure.devops.v6_0.test.models.TestSession>` test_session: Test session details for update
        :param :class:`<TeamContext> <azure.devops.v6_0.test.models.TeamContext>` team_context: The team context for the operation
        :rtype: :class:`<TestSession> <azure.devops.v6_0.test.models.TestSession>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(test_session, 'TestSession')
        response = self._send(http_method='PATCH',
                              location_id='1500b4b4-6c69-4ca6-9b18-35e9e97fe2ac',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSession', response)

    def add_test_cases_to_suite(self, project, plan_id, suite_id, test_case_ids):
        """AddTestCasesToSuite.
        [Preview API] Add test cases to suite.
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
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def get_test_case_by_id(self, project, plan_id, suite_id, test_case_ids):
        """GetTestCaseById.
        [Preview API] Get a specific test case in a test suite with test case id.
        :param str project: Project ID or project name
        :param int plan_id: ID of the test plan that contains the suites.
        :param int suite_id: ID of the suite that contains the test case.
        :param int test_case_ids: ID of the test case to get.
        :rtype: :class:`<SuiteTestCase> <azure.devops.v6_0.test.models.SuiteTestCase>`
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
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('SuiteTestCase', response)

    def get_test_cases(self, project, plan_id, suite_id):
        """GetTestCases.
        [Preview API] Get all test cases in a suite.
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
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def remove_test_cases_from_suite_url(self, project, plan_id, suite_id, test_case_ids):
        """RemoveTestCasesFromSuiteUrl.
        [Preview API] The test points associated with the test cases are removed from the test suite. The test case work item is not deleted from the system. See test cases resource to delete a test case permanently.
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
                   version='6.0-preview.3',
                   route_values=route_values)

    def update_suite_test_cases(self, suite_test_case_update_model, project, plan_id, suite_id, test_case_ids):
        """UpdateSuiteTestCases.
        [Preview API] Updates the properties of the test case association in a suite.
        :param :class:`<SuiteTestCaseUpdateModel> <azure.devops.v6_0.test.models.SuiteTestCaseUpdateModel>` suite_test_case_update_model: Model for updation of the properties of test case suite association.
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
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def delete_test_case(self, project, test_case_id):
        """DeleteTestCase.
        [Preview API] Delete a test case.
        :param str project: Project ID or project name
        :param int test_case_id: Id of test case to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_case_id is not None:
            route_values['testCaseId'] = self._serialize.url('test_case_id', test_case_id, 'int')
        self._send(http_method='DELETE',
                   location_id='4d472e0f-e32c-4ef8-adf4-a4078772889c',
                   version='6.0-preview.1',
                   route_values=route_values)

    def query_test_history(self, filter, project):
        """QueryTestHistory.
        [Preview API] Get history of a test method using TestHistoryQuery
        :param :class:`<TestHistoryQuery> <azure.devops.v6_0.test.models.TestHistoryQuery>` filter: TestHistoryQuery to get history
        :param str project: Project ID or project name
        :rtype: :class:`<TestHistoryQuery> <azure.devops.v6_0.test.models.TestHistoryQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestHistoryQuery')
        response = self._send(http_method='POST',
                              location_id='929fd86c-3e38-4d8c-b4b6-90df256e5971',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestHistoryQuery', response)

