﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ReleaseClient(Client):
    """Release
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(ReleaseClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'efc2f575-36ef-48e9-b672-0c6fb4a48ac5'

    def get_approvals(self, project, assigned_to_filter=None, status_filter=None, release_ids_filter=None, type_filter=None, top=None, continuation_token=None, query_order=None, include_my_group_approvals=None):
        """GetApprovals.
        Get a list of approvals
        :param str project: Project ID or project name
        :param str assigned_to_filter: Approvals assigned to this user.
        :param str status_filter: Approvals with this status. Default is 'pending'.
        :param [int] release_ids_filter: Approvals for release id(s) mentioned in the filter. Multiple releases can be mentioned by separating them with ',' e.g. releaseIdsFilter=1,2,3,4.
        :param str type_filter: Approval with this type.
        :param int top: Number of approvals to get. Default is 50.
        :param int continuation_token: Gets the approvals after the continuation token provided.
        :param str query_order: Gets the results in the defined order of created approvals. Default is 'descending'.
        :param bool include_my_group_approvals: 'true' to include my group approvals. Default is 'false'.
        :rtype: :class:`<GetApprovalsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if assigned_to_filter is not None:
            query_parameters['assignedToFilter'] = self._serialize.query('assigned_to_filter', assigned_to_filter, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if release_ids_filter is not None:
            release_ids_filter = ",".join(map(str, release_ids_filter))
            query_parameters['releaseIdsFilter'] = self._serialize.query('release_ids_filter', release_ids_filter, 'str')
        if type_filter is not None:
            query_parameters['typeFilter'] = self._serialize.query('type_filter', type_filter, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if include_my_group_approvals is not None:
            query_parameters['includeMyGroupApprovals'] = self._serialize.query('include_my_group_approvals', include_my_group_approvals, 'bool')
        response = self._send(http_method='GET',
                              location_id='b47c6458-e73b-47cb-a770-4df1e8813a91',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[ReleaseApproval]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetApprovalsResponseValue(response_value, continuation_token)

    class GetApprovalsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_approvals method

            :param value:
            :type value: :class:`<[ReleaseApproval]> <azure.devops.v5_1.release.models.[ReleaseApproval]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_release_approval(self, approval, project, approval_id):
        """UpdateReleaseApproval.
        Update status of an approval
        :param :class:`<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval>` approval: ReleaseApproval object having status, approver and comments.
        :param str project: Project ID or project name
        :param int approval_id: Id of the approval.
        :rtype: :class:`<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if approval_id is not None:
            route_values['approvalId'] = self._serialize.url('approval_id', approval_id, 'int')
        content = self._serialize.body(approval, 'ReleaseApproval')
        response = self._send(http_method='PATCH',
                              location_id='9328e074-59fb-465a-89d9-b09c82ee5109',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseApproval', response)

    def get_release_task_attachment_content(self, project, release_id, environment_id, attempt_id, plan_id, timeline_id, record_id, type, name, **kwargs):
        """GetReleaseTaskAttachmentContent.
        [Preview API] Get a release task attachment.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int environment_id: Id of the release environment.
        :param int attempt_id: Attempt number of deployment.
        :param str plan_id: Plan Id of the deploy phase.
        :param str timeline_id: Timeline Id of the task.
        :param str record_id: Record Id of attachment.
        :param str type: Type of the attachment.
        :param str name: Name of the attachment.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        if attempt_id is not None:
            route_values['attemptId'] = self._serialize.url('attempt_id', attempt_id, 'int')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='60b86efb-7b8c-4853-8f9f-aa142b77b479',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_release_task_attachments(self, project, release_id, environment_id, attempt_id, plan_id, type):
        """GetReleaseTaskAttachments.
        [Preview API] Get the release task attachments.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int environment_id: Id of the release environment.
        :param int attempt_id: Attempt number of deployment.
        :param str plan_id: Plan Id of the deploy phase.
        :param str type: Type of the attachment.
        :rtype: [ReleaseTaskAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        if attempt_id is not None:
            route_values['attemptId'] = self._serialize.url('attempt_id', attempt_id, 'int')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='a4d06688-0dfa-4895-82a5-f43ec9452306',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[ReleaseTaskAttachment]', self._unwrap_collection(response))

    def create_release_definition(self, release_definition, project):
        """CreateReleaseDefinition.
        Create a release definition
        :param :class:`<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>` release_definition: release definition object to create.
        :param str project: Project ID or project name
        :rtype: :class:`<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='POST',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)

    def delete_release_definition(self, project, definition_id, comment=None, force_delete=None):
        """DeleteReleaseDefinition.
        Delete a release definition.
        :param str project: Project ID or project name
        :param int definition_id: Id of the release definition.
        :param str comment: Comment for deleting a release definition.
        :param bool force_delete: 'true' to automatically cancel any in-progress release deployments and proceed with release definition deletion . Default is 'false'.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if force_delete is not None:
            query_parameters['forceDelete'] = self._serialize.query('force_delete', force_delete, 'bool')
        self._send(http_method='DELETE',
                   location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                   version='5.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_release_definition(self, project, definition_id, property_filters=None):
        """GetReleaseDefinition.
        Get a release definition.
        :param str project: Project ID or project name
        :param int definition_id: Id of the release definition.
        :param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definition will contain values for the specified property Ids (if they exist). If not set, properties will not be included.
        :rtype: :class:`<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReleaseDefinition', response)

    def get_release_definitions(self, project, search_text=None, expand=None, artifact_type=None, artifact_source_id=None, top=None, continuation_token=None, query_order=None, path=None, is_exact_name_match=None, tag_filter=None, property_filters=None, definition_id_filter=None, is_deleted=None, search_text_contains_folder_name=None):
        """GetReleaseDefinitions.
        Get a list of release definitions.
        :param str project: Project ID or project name
        :param str search_text: Get release definitions with names containing searchText.
        :param str expand: The properties that should be expanded in the list of Release definitions.
        :param str artifact_type: Release definitions with given artifactType will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild.
        :param str artifact_source_id: Release definitions with given artifactSourceId will be returned. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json at https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions.
        :param int top: Number of release definitions to get.
        :param str continuation_token: Gets the release definitions after the continuation token provided.
        :param str query_order: Gets the results in the defined order. Default is 'IdAscending'.
        :param str path: Gets the release definitions under the specified path.
        :param bool is_exact_name_match: 'true'to gets the release definitions with exact match as specified in searchText. Default is 'false'.
        :param [str] tag_filter: A comma-delimited list of tags. Only release definitions with these tags will be returned.
        :param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definitions will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release Definition from results irrespective of whether it has property set or not.
        :param [str] definition_id_filter: A comma-delimited list of release definitions to retrieve.
        :param bool is_deleted: 'true' to get release definitions that has been deleted. Default is 'false'
        :param bool search_text_contains_folder_name: 'true' to get the release definitions under the folder with name as specified in searchText. Default is 'false'.
        :rtype: :class:`<GetReleaseDefinitionsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if search_text is not None:
            query_parameters['searchText'] = self._serialize.query('search_text', search_text, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if artifact_type is not None:
            query_parameters['artifactType'] = self._serialize.query('artifact_type', artifact_type, 'str')
        if artifact_source_id is not None:
            query_parameters['artifactSourceId'] = self._serialize.query('artifact_source_id', artifact_source_id, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if is_exact_name_match is not None:
            query_parameters['isExactNameMatch'] = self._serialize.query('is_exact_name_match', is_exact_name_match, 'bool')
        if tag_filter is not None:
            tag_filter = ",".join(tag_filter)
            query_parameters['tagFilter'] = self._serialize.query('tag_filter', tag_filter, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if definition_id_filter is not None:
            definition_id_filter = ",".join(definition_id_filter)
            query_parameters['definitionIdFilter'] = self._serialize.query('definition_id_filter', definition_id_filter, 'str')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        if search_text_contains_folder_name is not None:
            query_parameters['searchTextContainsFolderName'] = self._serialize.query('search_text_contains_folder_name', search_text_contains_folder_name, 'bool')
        response = self._send(http_method='GET',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[ReleaseDefinition]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetReleaseDefinitionsResponseValue(response_value, continuation_token)

    class GetReleaseDefinitionsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_release_definitions method

            :param value:
            :type value: :class:`<[ReleaseDefinition]> <azure.devops.v5_1.release.models.[ReleaseDefinition]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_release_definition(self, release_definition, project):
        """UpdateReleaseDefinition.
        Update a release definition.
        :param :class:`<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>` release_definition: Release definition object to update.
        :param str project: Project ID or project name
        :rtype: :class:`<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='PUT',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)

    def get_deployments(self, project, definition_id=None, definition_environment_id=None, created_by=None, min_modified_time=None, max_modified_time=None, deployment_status=None, operation_status=None, latest_attempts_only=None, query_order=None, top=None, continuation_token=None, created_for=None, min_started_time=None, max_started_time=None, source_branch=None):
        """GetDeployments.
        :param str project: Project ID or project name
        :param int definition_id:
        :param int definition_environment_id:
        :param str created_by:
        :param datetime min_modified_time:
        :param datetime max_modified_time:
        :param str deployment_status:
        :param str operation_status:
        :param bool latest_attempts_only:
        :param str query_order:
        :param int top:
        :param int continuation_token:
        :param str created_for:
        :param datetime min_started_time:
        :param datetime max_started_time:
        :param str source_branch:
        :rtype: :class:`<GetDeploymentsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if definition_environment_id is not None:
            query_parameters['definitionEnvironmentId'] = self._serialize.query('definition_environment_id', definition_environment_id, 'int')
        if created_by is not None:
            query_parameters['createdBy'] = self._serialize.query('created_by', created_by, 'str')
        if min_modified_time is not None:
            query_parameters['minModifiedTime'] = self._serialize.query('min_modified_time', min_modified_time, 'iso-8601')
        if max_modified_time is not None:
            query_parameters['maxModifiedTime'] = self._serialize.query('max_modified_time', max_modified_time, 'iso-8601')
        if deployment_status is not None:
            query_parameters['deploymentStatus'] = self._serialize.query('deployment_status', deployment_status, 'str')
        if operation_status is not None:
            query_parameters['operationStatus'] = self._serialize.query('operation_status', operation_status, 'str')
        if latest_attempts_only is not None:
            query_parameters['latestAttemptsOnly'] = self._serialize.query('latest_attempts_only', latest_attempts_only, 'bool')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if created_for is not None:
            query_parameters['createdFor'] = self._serialize.query('created_for', created_for, 'str')
        if min_started_time is not None:
            query_parameters['minStartedTime'] = self._serialize.query('min_started_time', min_started_time, 'iso-8601')
        if max_started_time is not None:
            query_parameters['maxStartedTime'] = self._serialize.query('max_started_time', max_started_time, 'iso-8601')
        if source_branch is not None:
            query_parameters['sourceBranch'] = self._serialize.query('source_branch', source_branch, 'str')
        response = self._send(http_method='GET',
                              location_id='b005ef73-cddc-448e-9ba2-5193bf36b19f',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Deployment]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetDeploymentsResponseValue(response_value, continuation_token)

    class GetDeploymentsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_deployments method

            :param value:
            :type value: :class:`<[Deployment]> <azure.devops.v5_1.release.models.[Deployment]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_release_environment(self, project, release_id, environment_id):
        """GetReleaseEnvironment.
        [Preview API] Get a release environment.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int environment_id: Id of the release environment.
        :rtype: :class:`<ReleaseEnvironment> <azure.devops.v5_1.release.models.ReleaseEnvironment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='a7e426b1-03dc-48af-9dfe-c98bac612dcb',
                              version='5.1-preview.6',
                              route_values=route_values)
        return self._deserialize('ReleaseEnvironment', response)

    def update_release_environment(self, environment_update_data, project, release_id, environment_id):
        """UpdateReleaseEnvironment.
        [Preview API] Update the status of a release environment
        :param :class:`<ReleaseEnvironmentUpdateMetadata> <azure.devops.v5_1.release.models.ReleaseEnvironmentUpdateMetadata>` environment_update_data: Environment update meta data.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int environment_id: Id of release environment.
        :rtype: :class:`<ReleaseEnvironment> <azure.devops.v5_1.release.models.ReleaseEnvironment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        content = self._serialize.body(environment_update_data, 'ReleaseEnvironmentUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='a7e426b1-03dc-48af-9dfe-c98bac612dcb',
                              version='5.1-preview.6',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseEnvironment', response)

    def delete_folder(self, project, path):
        """DeleteFolder.
        [Preview API] Deletes a definition folder for given folder name and path and all it's existing definitions.
        :param str project: Project ID or project name
        :param str path: Path of the folder to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        self._send(http_method='DELETE',
                   location_id='f7ddf76d-ce0c-4d68-94ff-becaec5d9dea',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_folders(self, project, path=None, query_order=None):
        """GetFolders.
        [Preview API] Gets folders.
        :param str project: Project ID or project name
        :param str path: Path of the folder.
        :param str query_order: Gets the results in the defined order. Default is 'None'.
        :rtype: [Folder]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='f7ddf76d-ce0c-4d68-94ff-becaec5d9dea',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Folder]', self._unwrap_collection(response))

    def update_folder(self, folder, project, path):
        """UpdateFolder.
        [Preview API] Updates an existing folder at given existing path.
        :param :class:`<Folder> <azure.devops.v5_1.release.models.Folder>` folder: folder.
        :param str project: Project ID or project name
        :param str path: Path of the folder to update.
        :rtype: :class:`<Folder> <azure.devops.v5_1.release.models.Folder>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        content = self._serialize.body(folder, 'Folder')
        response = self._send(http_method='PATCH',
                              location_id='f7ddf76d-ce0c-4d68-94ff-becaec5d9dea',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Folder', response)

    def update_gates(self, gate_update_metadata, project, gate_step_id):
        """UpdateGates.
        [Preview API] Updates the gate for a deployment.
        :param :class:`<GateUpdateMetadata> <azure.devops.v5_1.release.models.GateUpdateMetadata>` gate_update_metadata: Metadata to patch the Release Gates.
        :param str project: Project ID or project name
        :param int gate_step_id: Gate step Id.
        :rtype: :class:`<ReleaseGates> <azure.devops.v5_1.release.models.ReleaseGates>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if gate_step_id is not None:
            route_values['gateStepId'] = self._serialize.url('gate_step_id', gate_step_id, 'int')
        content = self._serialize.body(gate_update_metadata, 'GateUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='2666a539-2001-4f80-bcc7-0379956749d4',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseGates', response)

    def get_logs(self, project, release_id, **kwargs):
        """GetLogs.
        [Preview API] Get logs for a release Id.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        response = self._send(http_method='GET',
                              location_id='c37fbab5-214b-48e4-a55b-cb6b4f6e4038',
                              version='5.1-preview.2',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_task_log(self, project, release_id, environment_id, release_deploy_phase_id, task_id, start_line=None, end_line=None, **kwargs):
        """GetTaskLog.
        [Preview API] Gets the task log of a release as a plain text file.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int environment_id: Id of release environment.
        :param int release_deploy_phase_id: Release deploy phase Id.
        :param int task_id: ReleaseTask Id for the log.
        :param long start_line: Starting line number for logs
        :param long end_line: Ending line number for logs
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        if release_deploy_phase_id is not None:
            route_values['releaseDeployPhaseId'] = self._serialize.url('release_deploy_phase_id', release_deploy_phase_id, 'int')
        if task_id is not None:
            route_values['taskId'] = self._serialize.url('task_id', task_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='17c91af7-09fd-4256-bff1-c24ee4f73bc0',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_manual_intervention(self, project, release_id, manual_intervention_id):
        """GetManualIntervention.
        Get manual intervention for a given release and manual intervention id.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int manual_intervention_id: Id of the manual intervention.
        :rtype: :class:`<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if manual_intervention_id is not None:
            route_values['manualInterventionId'] = self._serialize.url('manual_intervention_id', manual_intervention_id, 'int')
        response = self._send(http_method='GET',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('ManualIntervention', response)

    def get_manual_interventions(self, project, release_id):
        """GetManualInterventions.
        List all manual interventions for a given release.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :rtype: [ManualIntervention]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        response = self._send(http_method='GET',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[ManualIntervention]', self._unwrap_collection(response))

    def update_manual_intervention(self, manual_intervention_update_metadata, project, release_id, manual_intervention_id):
        """UpdateManualIntervention.
        Update manual intervention.
        :param :class:`<ManualInterventionUpdateMetadata> <azure.devops.v5_1.release.models.ManualInterventionUpdateMetadata>` manual_intervention_update_metadata: Meta data to update manual intervention.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int manual_intervention_id: Id of the manual intervention.
        :rtype: :class:`<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        if manual_intervention_id is not None:
            route_values['manualInterventionId'] = self._serialize.url('manual_intervention_id', manual_intervention_id, 'int')
        content = self._serialize.body(manual_intervention_update_metadata, 'ManualInterventionUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='616c46e4-f370-4456-adaa-fbaf79c7b79e',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ManualIntervention', response)

    def get_releases(self, project=None, definition_id=None, definition_environment_id=None, search_text=None, created_by=None, status_filter=None, environment_status_filter=None, min_created_time=None, max_created_time=None, query_order=None, top=None, continuation_token=None, expand=None, artifact_type_id=None, source_id=None, artifact_version_id=None, source_branch_filter=None, is_deleted=None, tag_filter=None, property_filters=None, release_id_filter=None, path=None):
        """GetReleases.
        Get a list of releases
        :param str project: Project ID or project name
        :param int definition_id: Releases from this release definition Id.
        :param int definition_environment_id:
        :param str search_text: Releases with names containing searchText.
        :param str created_by: Releases created by this user.
        :param str status_filter: Releases that have this status.
        :param int environment_status_filter:
        :param datetime min_created_time: Releases that were created after this time.
        :param datetime max_created_time: Releases that were created before this time.
        :param str query_order: Gets the results in the defined order of created date for releases. Default is descending.
        :param int top: Number of releases to get. Default is 50.
        :param int continuation_token: Gets the releases after the continuation token provided.
        :param str expand: The property that should be expanded in the list of releases.
        :param str artifact_type_id: Releases with given artifactTypeId will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild.
        :param str source_id: Unique identifier of the artifact used. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions.
        :param str artifact_version_id: Releases with given artifactVersionId will be returned. E.g. in case of Build artifactType, it is buildId.
        :param str source_branch_filter: Releases with given sourceBranchFilter will be returned.
        :param bool is_deleted: Gets the soft deleted releases, if true.
        :param [str] tag_filter: A comma-delimited list of tags. Only releases with these tags will be returned.
        :param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Releases will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release from results irrespective of whether it has property set or not.
        :param [int] release_id_filter: A comma-delimited list of releases Ids. Only releases with these Ids will be returned.
        :param str path: Releases under this folder path will be returned
        :rtype: :class:`<GetReleasesResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if definition_environment_id is not None:
            query_parameters['definitionEnvironmentId'] = self._serialize.query('definition_environment_id', definition_environment_id, 'int')
        if search_text is not None:
            query_parameters['searchText'] = self._serialize.query('search_text', search_text, 'str')
        if created_by is not None:
            query_parameters['createdBy'] = self._serialize.query('created_by', created_by, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if environment_status_filter is not None:
            query_parameters['environmentStatusFilter'] = self._serialize.query('environment_status_filter', environment_status_filter, 'int')
        if min_created_time is not None:
            query_parameters['minCreatedTime'] = self._serialize.query('min_created_time', min_created_time, 'iso-8601')
        if max_created_time is not None:
            query_parameters['maxCreatedTime'] = self._serialize.query('max_created_time', max_created_time, 'iso-8601')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if artifact_type_id is not None:
            query_parameters['artifactTypeId'] = self._serialize.query('artifact_type_id', artifact_type_id, 'str')
        if source_id is not None:
            query_parameters['sourceId'] = self._serialize.query('source_id', source_id, 'str')
        if artifact_version_id is not None:
            query_parameters['artifactVersionId'] = self._serialize.query('artifact_version_id', artifact_version_id, 'str')
        if source_branch_filter is not None:
            query_parameters['sourceBranchFilter'] = self._serialize.query('source_branch_filter', source_branch_filter, 'str')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        if tag_filter is not None:
            tag_filter = ",".join(tag_filter)
            query_parameters['tagFilter'] = self._serialize.query('tag_filter', tag_filter, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if release_id_filter is not None:
            release_id_filter = ",".join(map(str, release_id_filter))
            query_parameters['releaseIdFilter'] = self._serialize.query('release_id_filter', release_id_filter, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Release]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetReleasesResponseValue(response_value, continuation_token)

    class GetReleasesResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_releases method

            :param value:
            :type value: :class:`<[Release]> <azure.devops.v5_1.release.models.[Release]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def create_release(self, release_start_metadata, project):
        """CreateRelease.
        Create a release.
        :param :class:`<ReleaseStartMetadata> <azure.devops.v5_1.release.models.ReleaseStartMetadata>` release_start_metadata: Metadata to create a release.
        :param str project: Project ID or project name
        :rtype: :class:`<Release> <azure.devops.v5_1.release.models.Release>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_start_metadata, 'ReleaseStartMetadata')
        response = self._send(http_method='POST',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

    def get_release(self, project, release_id, approval_filters=None, property_filters=None, expand=None, top_gate_records=None):
        """GetRelease.
        Get a Release
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param str approval_filters: A filter which would allow fetching approval steps selectively based on whether it is automated, or manual. This would also decide whether we should fetch pre and post approval snapshots. Assumes All by default
        :param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release will contain values for the specified property Ids (if they exist). If not set, properties will not be included.
        :param str expand: A property that should be expanded in the release.
        :param int top_gate_records: Number of release gate records to get. Default is 5.
        :rtype: :class:`<Release> <azure.devops.v5_1.release.models.Release>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        query_parameters = {}
        if approval_filters is not None:
            query_parameters['approvalFilters'] = self._serialize.query('approval_filters', approval_filters, 'str')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if top_gate_records is not None:
            query_parameters['$topGateRecords'] = self._serialize.query('top_gate_records', top_gate_records, 'int')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Release', response)

    def get_release_revision(self, project, release_id, definition_snapshot_revision, **kwargs):
        """GetReleaseRevision.
        Get release for a given revision number.
        :param str project: Project ID or project name
        :param int release_id: Id of the release.
        :param int definition_snapshot_revision: Definition snapshot revision number.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        query_parameters = {}
        if definition_snapshot_revision is not None:
            query_parameters['definitionSnapshotRevision'] = self._serialize.query('definition_snapshot_revision', definition_snapshot_revision, 'int')
        response = self._send(http_method='GET',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_release(self, release, project, release_id):
        """UpdateRelease.
        Update a complete release object.
        :param :class:`<Release> <azure.devops.v5_1.release.models.Release>` release: Release object for update.
        :param str project: Project ID or project name
        :param int release_id: Id of the release to update.
        :rtype: :class:`<Release> <azure.devops.v5_1.release.models.Release>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        content = self._serialize.body(release, 'Release')
        response = self._send(http_method='PUT',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

    def update_release_resource(self, release_update_metadata, project, release_id):
        """UpdateReleaseResource.
        Update few properties of a release.
        :param :class:`<ReleaseUpdateMetadata> <azure.devops.v5_1.release.models.ReleaseUpdateMetadata>` release_update_metadata: Properties of release to update.
        :param str project: Project ID or project name
        :param int release_id: Id of the release to update.
        :rtype: :class:`<Release> <azure.devops.v5_1.release.models.Release>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if release_id is not None:
            route_values['releaseId'] = self._serialize.url('release_id', release_id, 'int')
        content = self._serialize.body(release_update_metadata, 'ReleaseUpdateMetadata')
        response = self._send(http_method='PATCH',
                              location_id='a166fde7-27ad-408e-ba75-703c2cc9d500',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Release', response)

    def get_definition_revision(self, project, definition_id, revision, **kwargs):
        """GetDefinitionRevision.
        [Preview API] Get release definition for a given definitionId and revision
        :param str project: Project ID or project name
        :param int definition_id: Id of the definition.
        :param int revision: Id of the revision.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        if revision is not None:
            route_values['revision'] = self._serialize.url('revision', revision, 'int')
        response = self._send(http_method='GET',
                              location_id='258b82e0-9d41-43f3-86d6-fef14ddd44bc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_release_definition_history(self, project, definition_id):
        """GetReleaseDefinitionHistory.
        [Preview API] Get revision history for a release definition
        :param str project: Project ID or project name
        :param int definition_id: Id of the definition.
        :rtype: [ReleaseDefinitionRevision]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='258b82e0-9d41-43f3-86d6-fef14ddd44bc',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[ReleaseDefinitionRevision]', self._unwrap_collection(response))

