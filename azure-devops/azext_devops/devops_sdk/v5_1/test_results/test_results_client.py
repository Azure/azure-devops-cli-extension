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

    def create_test_iteration_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id, iteration_id, action_path=None):
        """CreateTestIterationResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v5_1.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int iteration_id:
        :param str action_path:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v5_1.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query('iteration_id', iteration_id, 'int')
        if action_path is not None:
            query_parameters['actionPath'] = self._serialize.query('action_path', action_path, 'str')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def create_test_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id):
        """CreateTestResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v5_1.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v5_1.test_results.models.TestAttachmentReference>`
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def create_test_sub_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id, test_sub_result_id):
        """CreateTestSubResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v5_1.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int test_sub_result_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v5_1.test_results.models.TestAttachmentReference>`
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def delete_test_result_attachment(self, project, run_id, test_case_result_id, attachment_id):
        """DeleteTestResultAttachment.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
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
        self._send(http_method='DELETE',
                   location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentContent.
        [Preview API] Returns a test result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_result_attachments(self, project, run_id, test_case_result_id):
        """GetTestResultAttachments.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentZip.
        [Preview API] Returns a test result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_sub_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentContent.
        [Preview API] Returns a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int test_sub_result_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
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
        [Preview API] Returns attachment references for test sub result.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int test_sub_result_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_sub_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentZip.
        [Preview API] Returns a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int test_sub_result_id:
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
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='5.1-preview.1',
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
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v5_1.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v5_1.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def delete_test_run_attachment(self, project, run_id, attachment_id):
        """DeleteTestRunAttachment.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_run_attachment_content(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentContent.
        [Preview API] Returns a test run attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
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
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_run_attachments(self, project, run_id):
        """GetTestRunAttachments.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_run_attachment_zip(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentZip.
        [Preview API] Returns a test run attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
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
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_bugs_linked_to_test_result(self, project, run_id, test_case_result_id):
        """GetBugsLinkedToTestResult.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: [WorkItemReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='d8dbf98f-eb34-4f8d-8365-47972af34f29',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemReference]', self._unwrap_collection(response))

    def get_build_code_coverage(self, project, build_id, flags):
        """GetBuildCodeCoverage.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param int flags:
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
                              location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildCoverage]', self._unwrap_collection(response))

    def get_code_coverage_summary(self, project, build_id, delta_build_id=None):
        """GetCodeCoverageSummary.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param int delta_build_id:
        :rtype: :class:`<CodeCoverageSummary> <azure.devops.v5_1.test_results.models.CodeCoverageSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if delta_build_id is not None:
            query_parameters['deltaBuildId'] = self._serialize.query('delta_build_id', delta_build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CodeCoverageSummary', response)

    def update_code_coverage_summary(self, project, build_id, coverage_data=None):
        """UpdateCodeCoverageSummary.
        [Preview API] http://(tfsserver):8080/tfs/DefaultCollection/_apis/test/CodeCoverage?buildId=10 Request: Json of code coverage summary
        :param str project: Project ID or project name
        :param int build_id:
        :param :class:`<CodeCoverageData> <azure.devops.v5_1.test_results.models.CodeCoverageData>` coverage_data:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        content = self._serialize.body(coverage_data, 'CodeCoverageData')
        self._send(http_method='POST',
                   location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                   version='5.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters,
                   content=content)

    def get_test_run_code_coverage(self, project, run_id, flags):
        """GetTestRunCodeCoverage.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int flags:
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
                              location_id='5641efbc-6f9b-401a-baeb-d3da22489e5e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRunCoverage]', self._unwrap_collection(response))

    def query_test_result_history(self, filter, project):
        """QueryTestResultHistory.
        [Preview API]
        :param :class:`<ResultsFilter> <azure.devops.v5_1.test_results.models.ResultsFilter>` filter:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultHistory> <azure.devops.v5_1.test_results.models.TestResultHistory>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'ResultsFilter')
        response = self._send(http_method='POST',
                              location_id='bdf7a97b-0395-4da8-9d5d-f957619327d1',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultHistory', response)

    def get_test_result_details_for_build(self, project, build_id, publish_context=None, group_by=None, filter=None, orderby=None, should_include_results=None, query_run_summary_for_in_progress=None):
        """GetTestResultDetailsForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param str group_by:
        :param str filter:
        :param str orderby:
        :param bool should_include_results:
        :param bool query_run_summary_for_in_progress:
        :rtype: :class:`<TestResultsDetails> <azure.devops.v5_1.test_results.models.TestResultsDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query('group_by', group_by, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if should_include_results is not None:
            query_parameters['shouldIncludeResults'] = self._serialize.query('should_include_results', should_include_results, 'bool')
        if query_run_summary_for_in_progress is not None:
            query_parameters['queryRunSummaryForInProgress'] = self._serialize.query('query_run_summary_for_in_progress', query_run_summary_for_in_progress, 'bool')
        response = self._send(http_method='GET',
                              location_id='a518c749-4524-45b2-a7ef-1ac009b312cd',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsDetails', response)

    def get_test_result_details_for_release(self, project, release_id, release_env_id, publish_context=None, group_by=None, filter=None, orderby=None, should_include_results=None, query_run_summary_for_in_progress=None):
        """GetTestResultDetailsForRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param int release_env_id:
        :param str publish_context:
        :param str group_by:
        :param str filter:
        :param str orderby:
        :param bool should_include_results:
        :param bool query_run_summary_for_in_progress:
        :rtype: :class:`<TestResultsDetails> <azure.devops.v5_1.test_results.models.TestResultsDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query('group_by', group_by, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if should_include_results is not None:
            query_parameters['shouldIncludeResults'] = self._serialize.query('should_include_results', should_include_results, 'bool')
        if query_run_summary_for_in_progress is not None:
            query_parameters['queryRunSummaryForInProgress'] = self._serialize.query('query_run_summary_for_in_progress', query_run_summary_for_in_progress, 'bool')
        response = self._send(http_method='GET',
                              location_id='19a8183a-69fb-47d7-bfbf-1b6b0d921294',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsDetails', response)

    def get_test_results_by_query(self, query, project):
        """GetTestResultsByQuery.
        [Preview API]
        :param :class:`<TestResultsQuery> <azure.devops.v5_1.test_results.models.TestResultsQuery>` query:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultsQuery> <azure.devops.v5_1.test_results.models.TestResultsQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(query, 'TestResultsQuery')
        response = self._send(http_method='POST',
                              location_id='14033a2c-af25-4af1-9e39-8ef6900482e3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultsQuery', response)

    def get_test_results_by_query_wiql(self, query_model, project, include_result_details=None, include_iteration_details=None, skip=None, top=None):
        """GetTestResultsByQueryWiql.
        [Preview API]
        :param :class:`<QueryModel> <azure.devops.v5_1.test_results.models.QueryModel>` query_model:
        :param str project: Project ID or project name
        :param bool include_result_details:
        :param bool include_iteration_details:
        :param int skip:
        :param int top:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_result_details is not None:
            query_parameters['includeResultDetails'] = self._serialize.query('include_result_details', include_result_details, 'bool')
        if include_iteration_details is not None:
            query_parameters['includeIterationDetails'] = self._serialize.query('include_iteration_details', include_iteration_details, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(query_model, 'QueryModel')
        response = self._send(http_method='POST',
                              location_id='5ea78be3-2f5a-4110-8034-c27f24c62db1',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def add_test_results_to_test_run(self, results, project, run_id):
        """AddTestResultsToTestRun.
        [Preview API]
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='POST',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_result_by_id(self, project, run_id, test_result_id, details_to_include=None):
        """GetTestResultById.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_result_id:
        :param str details_to_include:
        :rtype: :class:`<TestCaseResult> <azure.devops.v5_1.test_results.models.TestCaseResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_result_id is not None:
            route_values['testResultId'] = self._serialize.url('test_result_id', test_result_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        response = self._send(http_method='GET',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestCaseResult', response)

    def get_test_results(self, project, run_id, details_to_include=None, skip=None, top=None, outcomes=None):
        """GetTestResults.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param str details_to_include:
        :param int skip:
        :param int top:
        :param [TestOutcome] outcomes:
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
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def update_test_results(self, results, project, run_id):
        """UpdateTestResults.
        [Preview API]
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='PATCH',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def query_test_results_report_for_build(self, project, build_id, publish_context=None, include_failure_details=None, build_to_compare=None):
        """QueryTestResultsReportForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param bool include_failure_details:
        :param :class:`<BuildReference> <azure.devops.v5_1.test_results.models.BuildReference>` build_to_compare:
        :rtype: :class:`<TestResultSummary> <azure.devops.v5_1.test_results.models.TestResultSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if include_failure_details is not None:
            query_parameters['includeFailureDetails'] = self._serialize.query('include_failure_details', include_failure_details, 'bool')
        if build_to_compare is not None:
            if build_to_compare.id is not None:
                query_parameters['buildToCompare.id'] = build_to_compare.id
            if build_to_compare.definition_id is not None:
                query_parameters['buildToCompare.definitionId'] = build_to_compare.definition_id
            if build_to_compare.number is not None:
                query_parameters['buildToCompare.number'] = build_to_compare.number
            if build_to_compare.uri is not None:
                query_parameters['buildToCompare.uri'] = build_to_compare.uri
            if build_to_compare.build_system is not None:
                query_parameters['buildToCompare.buildSystem'] = build_to_compare.build_system
            if build_to_compare.branch_name is not None:
                query_parameters['buildToCompare.branchName'] = build_to_compare.branch_name
            if build_to_compare.repository_id is not None:
                query_parameters['buildToCompare.repositoryId'] = build_to_compare.repository_id
        response = self._send(http_method='GET',
                              location_id='e009fa95-95a5-4ad4-9681-590043ce2423',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultSummary', response)

    def query_test_results_report_for_release(self, project, release_id, release_env_id, publish_context=None, include_failure_details=None, release_to_compare=None):
        """QueryTestResultsReportForRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param int release_env_id:
        :param str publish_context:
        :param bool include_failure_details:
        :param :class:`<ReleaseReference> <azure.devops.v5_1.test_results.models.ReleaseReference>` release_to_compare:
        :rtype: :class:`<TestResultSummary> <azure.devops.v5_1.test_results.models.TestResultSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if include_failure_details is not None:
            query_parameters['includeFailureDetails'] = self._serialize.query('include_failure_details', include_failure_details, 'bool')
        if release_to_compare is not None:
            if release_to_compare.id is not None:
                query_parameters['releaseToCompare.id'] = release_to_compare.id
            if release_to_compare.name is not None:
                query_parameters['releaseToCompare.name'] = release_to_compare.name
            if release_to_compare.environment_id is not None:
                query_parameters['releaseToCompare.environmentId'] = release_to_compare.environment_id
            if release_to_compare.environment_name is not None:
                query_parameters['releaseToCompare.environmentName'] = release_to_compare.environment_name
            if release_to_compare.definition_id is not None:
                query_parameters['releaseToCompare.definitionId'] = release_to_compare.definition_id
            if release_to_compare.environment_definition_id is not None:
                query_parameters['releaseToCompare.environmentDefinitionId'] = release_to_compare.environment_definition_id
            if release_to_compare.environment_definition_name is not None:
                query_parameters['releaseToCompare.environmentDefinitionName'] = release_to_compare.environment_definition_name
            if release_to_compare.creation_date is not None:
                query_parameters['releaseToCompare.creationDate'] = release_to_compare.creation_date
            if release_to_compare.environment_creation_date is not None:
                query_parameters['releaseToCompare.environmentCreationDate'] = release_to_compare.environment_creation_date
            if release_to_compare.attempt is not None:
                query_parameters['releaseToCompare.attempt'] = release_to_compare.attempt
        response = self._send(http_method='GET',
                              location_id='f10f9577-2c04-45ab-8c99-b26567a7cd55',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultSummary', response)

    def query_test_results_summary_for_releases(self, releases, project):
        """QueryTestResultsSummaryForReleases.
        [Preview API]
        :param [ReleaseReference] releases:
        :param str project: Project ID or project name
        :rtype: [TestResultSummary]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(releases, '[ReleaseReference]')
        response = self._send(http_method='POST',
                              location_id='f10f9577-2c04-45ab-8c99-b26567a7cd55',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestResultSummary]', self._unwrap_collection(response))

    def query_test_summary_by_requirement(self, results_context, project, work_item_ids=None):
        """QueryTestSummaryByRequirement.
        [Preview API]
        :param :class:`<TestResultsContext> <azure.devops.v5_1.test_results.models.TestResultsContext>` results_context:
        :param str project: Project ID or project name
        :param [int] work_item_ids:
        :rtype: [TestSummaryForWorkItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if work_item_ids is not None:
            work_item_ids = ",".join(map(str, work_item_ids))
            query_parameters['workItemIds'] = self._serialize.query('work_item_ids', work_item_ids, 'str')
        content = self._serialize.body(results_context, 'TestResultsContext')
        response = self._send(http_method='POST',
                              location_id='3b7fd26f-c335-4e55-afc1-a588f5e2af3c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestSummaryForWorkItem]', self._unwrap_collection(response))

    def query_result_trend_for_build(self, filter, project):
        """QueryResultTrendForBuild.
        [Preview API]
        :param :class:`<TestResultTrendFilter> <azure.devops.v5_1.test_results.models.TestResultTrendFilter>` filter:
        :param str project: Project ID or project name
        :rtype: [AggregatedDataForResultTrend]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestResultTrendFilter')
        response = self._send(http_method='POST',
                              location_id='0886a7ae-315a-4dba-9122-bcce93301f3a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AggregatedDataForResultTrend]', self._unwrap_collection(response))

    def query_result_trend_for_release(self, filter, project):
        """QueryResultTrendForRelease.
        [Preview API]
        :param :class:`<TestResultTrendFilter> <azure.devops.v5_1.test_results.models.TestResultTrendFilter>` filter:
        :param str project: Project ID or project name
        :rtype: [AggregatedDataForResultTrend]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestResultTrendFilter')
        response = self._send(http_method='POST',
                              location_id='107f23c3-359a-460a-a70c-63ee739f9f9a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AggregatedDataForResultTrend]', self._unwrap_collection(response))

    def create_test_run(self, test_run, project):
        """CreateTestRun.
        [Preview API]
        :param :class:`<RunCreateModel> <azure.devops.v5_1.test_results.models.RunCreateModel>` test_run:
        :param str project: Project ID or project name
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_run, 'RunCreateModel')
        response = self._send(http_method='POST',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def delete_test_run(self, project, run_id):
        """DeleteTestRun.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        self._send(http_method='DELETE',
                   location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_test_run_by_id(self, project, run_id, include_details=None, include_tags=None):
        """GetTestRunById.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param bool include_details:
        :param bool include_tags:
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        if include_tags is not None:
            query_parameters['includeTags'] = self._serialize.query('include_tags', include_tags, 'bool')
        response = self._send(http_method='GET',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None):
        """GetTestRuns.
        [Preview API]
        :param str project: Project ID or project name
        :param str build_uri:
        :param str owner:
        :param str tmi_run_id:
        :param int plan_id:
        :param bool include_run_details:
        :param bool automated:
        :param int skip:
        :param int top:
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
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='5.1-preview.1',
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
        :param [int] plan_ids: Plan Ids of the Runs to be queried, comma seperated list of valid ids.
        :param bool is_automated: Automation type of the Runs to be queried.
        :param str publish_context: PublishContext of the Runs to be queried.
        :param [int] build_ids: Build Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] build_def_ids: Build Definition Ids of the Runs to be queried, comma seperated list of valid ids.
        :param str branch_name: Source Branch name of the Runs to be queried.
        :param [int] release_ids: Release Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_def_ids: Release Definition Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_env_ids: Release Environment Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_env_def_ids: Release Environment Definition Ids of the Runs to be queried, comma seperated list of valid ids.
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
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='5.1-preview.1',
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
            :type value: :class:`<[TestRun]> <azure.devops.v5_1.test_results.models.[TestRun]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_test_run(self, run_update_model, project, run_id):
        """UpdateTestRun.
        [Preview API]
        :param :class:`<RunUpdateModel> <azure.devops.v5_1.test_results.models.RunUpdateModel>` run_update_model:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestRun> <azure.devops.v5_1.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(run_update_model, 'RunUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

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

    def get_test_results_settings(self, project, settings_type=None):
        """GetTestResultsSettings.
        [Preview API] Get TestResultsSettings data
        :param str project: Project ID or project name
        :param str settings_type:
        :rtype: :class:`<TestResultsSettings> <azure.devops.v5_1.test_results.models.TestResultsSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if settings_type is not None:
            query_parameters['settingsType'] = self._serialize.query('settings_type', settings_type, 'str')
        response = self._send(http_method='GET',
                              location_id='7319952e-e5a9-4e19-a006-84f3be8b7c68',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsSettings', response)

    def update_pipelines_test_settings(self, test_results_update_settings, project):
        """UpdatePipelinesTestSettings.
        [Preview API] Update project settings of test results
        :param :class:`<TestResultsUpdateSettings> <azure.devops.v5_1.test_results.models.TestResultsUpdateSettings>` test_results_update_settings:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultsSettings> <azure.devops.v5_1.test_results.models.TestResultsSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_results_update_settings, 'TestResultsUpdateSettings')
        response = self._send(http_method='PATCH',
                              location_id='7319952e-e5a9-4e19-a006-84f3be8b7c68',
                              version='5.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultsSettings', response)

    def query_test_history(self, filter, project):
        """QueryTestHistory.
        [Preview API] Get history of a test method using TestHistoryQuery
        :param :class:`<TestHistoryQuery> <azure.devops.v5_1.test_results.models.TestHistoryQuery>` filter: TestHistoryQuery to get history
        :param str project: Project ID or project name
        :rtype: :class:`<TestHistoryQuery> <azure.devops.v5_1.test_results.models.TestHistoryQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestHistoryQuery')
        response = self._send(http_method='POST',
                              location_id='2a41bd6a-8118-4403-b74e-5ba7492aed9d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestHistoryQuery', response)

    def get_test_logs_for_build(self, project, build_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestLogsForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str type:
        :param str directory_path:
        :param str file_name_prefix:
        :param bool fetch_meta_data:
        :param int top:
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<GetTestLogsForBuildResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='dff8ce3a-e539-4817-a405-d968491a88f1',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        response_value = self._deserialize('[TestLog]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestLogsForBuildResponseValue(response_value, continuation_token)

    class GetTestLogsForBuildResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_logs_for_build method

            :param value:
            :type value: :class:`<[TestLog]> <azure.devops.v5_1.test_results.models.[TestLog]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_test_result_logs(self, project, run_id, result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestResultLogs.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int result_id:
        :param str type:
        :param str directory_path:
        :param str file_name_prefix:
        :param bool fetch_meta_data:
        :param int top:
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<GetTestResultLogsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        response_value = self._deserialize('[TestLog]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestResultLogsResponseValue(response_value, continuation_token)

    class GetTestResultLogsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_result_logs method

            :param value:
            :type value: :class:`<[TestLog]> <azure.devops.v5_1.test_results.models.[TestLog]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_test_sub_result_logs(self, project, run_id, result_id, sub_result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestSubResultLogs.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int result_id:
        :param int sub_result_id:
        :param str type:
        :param str directory_path:
        :param str file_name_prefix:
        :param bool fetch_meta_data:
        :param int top:
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<GetTestSubResultLogsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        response_value = self._deserialize('[TestLog]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestSubResultLogsResponseValue(response_value, continuation_token)

    class GetTestSubResultLogsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_sub_result_logs method

            :param value:
            :type value: :class:`<[TestLog]> <azure.devops.v5_1.test_results.models.[TestLog]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_test_run_logs(self, project, run_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestRunLogs.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param str type:
        :param str directory_path:
        :param str file_name_prefix:
        :param bool fetch_meta_data:
        :param int top:
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<GetTestRunLogsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='5b47b946-e875-4c9a-acdc-2a20996caebe',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        response_value = self._deserialize('[TestLog]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetTestRunLogsResponseValue(response_value, continuation_token)

    class GetTestRunLogsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_test_run_logs method

            :param value:
            :type value: :class:`<[TestLog]> <azure.devops.v5_1.test_results.models.[TestLog]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_test_log_store_endpoint_details_for_build_log(self, project, build, type, file_path):
        """GetTestLogStoreEndpointDetailsForBuildLog.
        [Preview API]
        :param str project: Project ID or project name
        :param int build:
        :param str type:
        :param str file_path:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build is not None:
            query_parameters['build'] = self._serialize.query('build', build, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='39b09be7-f0c9-4a83-a513-9ae31b45c56f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_build(self, project, build_id, test_log_store_operation_type):
        """TestLogStoreEndpointDetailsForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str test_log_store_operation_type:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if test_log_store_operation_type is not None:
            query_parameters['testLogStoreOperationType'] = self._serialize.query('test_log_store_operation_type', test_log_store_operation_type, 'str')
        response = self._send(http_method='POST',
                              location_id='39b09be7-f0c9-4a83-a513-9ae31b45c56f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_result_log(self, project, run_id, result_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForResultLog.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int result_id:
        :param str type:
        :param str file_path:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_sub_result_log(self, project, run_id, result_id, sub_result_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForSubResultLog.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int result_id:
        :param int sub_result_id:
        :param str type:
        :param str file_path:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_result(self, project, run_id, result_id, sub_result_id, file_path, type):
        """TestLogStoreEndpointDetailsForResult.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int result_id:
        :param int sub_result_id:
        :param str file_path:
        :param str type:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_run_log(self, project, run_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForRunLog.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param str type:
        :param str file_path:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_run(self, project, run_id, test_log_store_operation_type, file_path=None, type=None):
        """TestLogStoreEndpointDetailsForRun.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param str test_log_store_operation_type:
        :param str file_path:
        :param str type:
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v5_1.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if test_log_store_operation_type is not None:
            query_parameters['testLogStoreOperationType'] = self._serialize.query('test_log_store_operation_type', test_log_store_operation_type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def create_test_settings(self, test_settings, project):
        """CreateTestSettings.
        [Preview API]
        :param :class:`<TestSettings> <azure.devops.v5_1.test_results.models.TestSettings>` test_settings:
        :param str project: Project ID or project name
        :rtype: int
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_settings, 'TestSettings')
        response = self._send(http_method='POST',
                              location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('int', response)

    def delete_test_settings(self, project, test_settings_id):
        """DeleteTestSettings.
        [Preview API]
        :param str project: Project ID or project name
        :param int test_settings_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_settings_id is not None:
            query_parameters['testSettingsId'] = self._serialize.query('test_settings_id', test_settings_id, 'int')
        self._send(http_method='DELETE',
                   location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                   version='5.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_test_settings_by_id(self, project, test_settings_id):
        """GetTestSettingsById.
        [Preview API]
        :param str project: Project ID or project name
        :param int test_settings_id:
        :rtype: :class:`<TestSettings> <azure.devops.v5_1.test_results.models.TestSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_settings_id is not None:
            query_parameters['testSettingsId'] = self._serialize.query('test_settings_id', test_settings_id, 'int')
        response = self._send(http_method='GET',
                              location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestSettings', response)

    def add_work_item_to_test_links(self, work_item_to_test_links, project):
        """AddWorkItemToTestLinks.
        [Preview API]
        :param :class:`<WorkItemToTestLinks> <azure.devops.v5_1.test_results.models.WorkItemToTestLinks>` work_item_to_test_links:
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemToTestLinks> <azure.devops.v5_1.test_results.models.WorkItemToTestLinks>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_to_test_links, 'WorkItemToTestLinks')
        response = self._send(http_method='POST',
                              location_id='4e3abe63-ca46-4fe0-98b2-363f7ec7aa5f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemToTestLinks', response)

    def delete_test_method_to_work_item_link(self, project, test_name, work_item_id):
        """DeleteTestMethodToWorkItemLink.
        [Preview API]
        :param str project: Project ID or project name
        :param str test_name:
        :param int work_item_id:
        :rtype: bool
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_name is not None:
            query_parameters['testName'] = self._serialize.query('test_name', test_name, 'str')
        if work_item_id is not None:
            query_parameters['workItemId'] = self._serialize.query('work_item_id', work_item_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='cbd50bd7-f7ed-4e35-b127-4408ae6bfa2c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def query_test_method_linked_work_items(self, project, test_name):
        """QueryTestMethodLinkedWorkItems.
        [Preview API]
        :param str project: Project ID or project name
        :param str test_name:
        :rtype: :class:`<TestToWorkItemLinks> <azure.devops.v5_1.test_results.models.TestToWorkItemLinks>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_name is not None:
            query_parameters['testName'] = self._serialize.query('test_name', test_name, 'str')
        response = self._send(http_method='POST',
                              location_id='cbd50bd7-f7ed-4e35-b127-4408ae6bfa2c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestToWorkItemLinks', response)

    def query_test_result_work_items(self, project, work_item_category, automated_test_name=None, test_case_id=None, max_complete_date=None, days=None, work_item_count=None):
        """QueryTestResultWorkItems.
        [Preview API]
        :param str project: Project ID or project name
        :param str work_item_category:
        :param str automated_test_name:
        :param int test_case_id:
        :param datetime max_complete_date:
        :param int days:
        :param int work_item_count:
        :rtype: [WorkItemReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if work_item_category is not None:
            query_parameters['workItemCategory'] = self._serialize.query('work_item_category', work_item_category, 'str')
        if automated_test_name is not None:
            query_parameters['automatedTestName'] = self._serialize.query('automated_test_name', automated_test_name, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        if max_complete_date is not None:
            query_parameters['maxCompleteDate'] = self._serialize.query('max_complete_date', max_complete_date, 'iso-8601')
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if work_item_count is not None:
            query_parameters['$workItemCount'] = self._serialize.query('work_item_count', work_item_count, 'int')
        response = self._send(http_method='GET',
                              location_id='f7401a26-331b-44fe-a470-f7ed35138e4a',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemReference]', self._unwrap_collection(response))

