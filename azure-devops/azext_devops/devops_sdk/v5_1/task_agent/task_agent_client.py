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


class TaskAgentClient(Client):
    """TaskAgent
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TaskAgentClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'a85b8835-c1a1-4aac-ae97-1c3d0ba72dbd'

    def add_agent_cloud(self, agent_cloud):
        """AddAgentCloud.
        [Preview API]
        :param :class:`<TaskAgentCloud> <azure.devops.v5_1.task_agent.models.TaskAgentCloud>` agent_cloud:
        :rtype: :class:`<TaskAgentCloud> <azure.devops.v5_1.task-agent.models.TaskAgentCloud>`
        """
        content = self._serialize.body(agent_cloud, 'TaskAgentCloud')
        response = self._send(http_method='POST',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('TaskAgentCloud', response)

    def delete_agent_cloud(self, agent_cloud_id):
        """DeleteAgentCloud.
        [Preview API]
        :param int agent_cloud_id:
        :rtype: :class:`<TaskAgentCloud> <azure.devops.v5_1.task-agent.models.TaskAgentCloud>`
        """
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentCloud', response)

    def get_agent_cloud(self, agent_cloud_id):
        """GetAgentCloud.
        [Preview API]
        :param int agent_cloud_id:
        :rtype: :class:`<TaskAgentCloud> <azure.devops.v5_1.task-agent.models.TaskAgentCloud>`
        """
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='GET',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentCloud', response)

    def get_agent_clouds(self):
        """GetAgentClouds.
        [Preview API]
        :rtype: [TaskAgentCloud]
        """
        response = self._send(http_method='GET',
                              location_id='bfa72b3d-0fc6-43fb-932b-a7f6559f93b9',
                              version='5.1-preview.1')
        return self._deserialize('[TaskAgentCloud]', self._unwrap_collection(response))

    def get_agent_cloud_types(self):
        """GetAgentCloudTypes.
        [Preview API] Get agent cloud types.
        :rtype: [TaskAgentCloudType]
        """
        response = self._send(http_method='GET',
                              location_id='5932e193-f376-469d-9c3e-e5588ce12cb5',
                              version='5.1-preview.1')
        return self._deserialize('[TaskAgentCloudType]', self._unwrap_collection(response))

    def add_deployment_group(self, deployment_group, project):
        """AddDeploymentGroup.
        [Preview API] Create a deployment group.
        :param :class:`<DeploymentGroupCreateParameter> <azure.devops.v5_1.task_agent.models.DeploymentGroupCreateParameter>` deployment_group: Deployment group to create.
        :param str project: Project ID or project name
        :rtype: :class:`<DeploymentGroup> <azure.devops.v5_1.task-agent.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(deployment_group, 'DeploymentGroupCreateParameter')
        response = self._send(http_method='POST',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def delete_deployment_group(self, project, deployment_group_id):
        """DeleteDeploymentGroup.
        [Preview API] Delete a deployment group.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group to be deleted.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_deployment_group(self, project, deployment_group_id, action_filter=None, expand=None):
        """GetDeploymentGroup.
        [Preview API] Get a deployment group by its ID.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group.
        :param str action_filter: Get the deployment group only if this action can be performed on it.
        :param str expand: Include these additional details in the returned object.
        :rtype: :class:`<DeploymentGroup> <azure.devops.v5_1.task-agent.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentGroup', response)

    def get_deployment_groups(self, project, name=None, action_filter=None, expand=None, continuation_token=None, top=None, ids=None):
        """GetDeploymentGroups.
        [Preview API] Get a list of deployment groups by name or IDs.
        :param str project: Project ID or project name
        :param str name: Name of the deployment group.
        :param str action_filter: Get only deployment groups on which this action can be performed.
        :param str expand: Include these additional details in the returned objects.
        :param str continuation_token: Get deployment groups with names greater than this continuationToken lexicographically.
        :param int top: Maximum number of deployment groups to return. Default is **1000**.
        :param [int] ids: Comma separated list of IDs of the deployment groups.
        :rtype: [DeploymentGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DeploymentGroup]', self._unwrap_collection(response))

    def update_deployment_group(self, deployment_group, project, deployment_group_id):
        """UpdateDeploymentGroup.
        [Preview API] Update a deployment group.
        :param :class:`<DeploymentGroupUpdateParameter> <azure.devops.v5_1.task_agent.models.DeploymentGroupUpdateParameter>` deployment_group: Deployment group to update.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group.
        :rtype: :class:`<DeploymentGroup> <azure.devops.v5_1.task-agent.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(deployment_group, 'DeploymentGroupUpdateParameter')
        response = self._send(http_method='PATCH',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def get_agent_cloud_requests(self, agent_cloud_id):
        """GetAgentCloudRequests.
        [Preview API]
        :param int agent_cloud_id:
        :rtype: [TaskAgentCloudRequest]
        """
        route_values = {}
        if agent_cloud_id is not None:
            route_values['agentCloudId'] = self._serialize.url('agent_cloud_id', agent_cloud_id, 'int')
        response = self._send(http_method='GET',
                              location_id='20189bd7-5134-49c2-b8e9-f9e856eea2b2',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[TaskAgentCloudRequest]', self._unwrap_collection(response))

    def delete_deployment_target(self, project, deployment_group_id, target_id):
        """DeleteDeploymentTarget.
        [Preview API] Delete a deployment target in a deployment group. This deletes the agent from associated deployment pool too.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group in which deployment target is deleted.
        :param int target_id: ID of the deployment target to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_deployment_target(self, project, deployment_group_id, target_id, expand=None):
        """GetDeploymentTarget.
        [Preview API] Get a deployment target by its ID in a deployment group
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group to which deployment target belongs.
        :param int target_id: ID of the deployment target to return.
        :param str expand: Include these additional details in the returned objects.
        :rtype: :class:`<DeploymentMachine> <azure.devops.v5_1.task-agent.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentMachine', response)

    def get_deployment_targets(self, project, deployment_group_id, tags=None, name=None, partial_name_match=None, expand=None, agent_status=None, agent_job_result=None, continuation_token=None, top=None, enabled=None, property_filters=None):
        """GetDeploymentTargets.
        [Preview API] Get a list of deployment targets in a deployment group.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group.
        :param [str] tags: Get only the deployment targets that contain all these comma separted list of tags.
        :param str name: Name pattern of the deployment targets to return.
        :param bool partial_name_match: When set to true, treats **name** as pattern. Else treats it as absolute match. Default is **false**.
        :param str expand: Include these additional details in the returned objects.
        :param str agent_status: Get only deployment targets that have this status.
        :param str agent_job_result: Get only deployment targets that have this last job result.
        :param str continuation_token: Get deployment targets with names greater than this continuationToken lexicographically.
        :param int top: Maximum number of deployment targets to return. Default is **1000**.
        :param bool enabled: Get only deployment targets that are enabled or disabled. Default is 'null' which returns all the targets.
        :param [str] property_filters:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if tags is not None:
            tags = ",".join(tags)
            query_parameters['tags'] = self._serialize.query('tags', tags, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if partial_name_match is not None:
            query_parameters['partialNameMatch'] = self._serialize.query('partial_name_match', partial_name_match, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if agent_status is not None:
            query_parameters['agentStatus'] = self._serialize.query('agent_status', agent_status, 'str')
        if agent_job_result is not None:
            query_parameters['agentJobResult'] = self._serialize.query('agent_job_result', agent_job_result, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if enabled is not None:
            query_parameters['enabled'] = self._serialize.query('enabled', enabled, 'bool')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[DeploymentMachine]', self._unwrap_collection(response))

    def update_deployment_targets(self, machines, project, deployment_group_id):
        """UpdateDeploymentTargets.
        [Preview API] Update tags of a list of deployment targets in a deployment group.
        :param [DeploymentTargetUpdateParameter] machines: Deployment targets with tags to udpdate.
        :param str project: Project ID or project name
        :param int deployment_group_id: ID of the deployment group in which deployment targets are updated.
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machines, '[DeploymentTargetUpdateParameter]')
        response = self._send(http_method='PATCH',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[DeploymentMachine]', self._unwrap_collection(response))

    def add_task_group(self, task_group, project):
        """AddTaskGroup.
        [Preview API] Create a task group.
        :param :class:`<TaskGroupCreateParameter> <azure.devops.v5_1.task_agent.models.TaskGroupCreateParameter>` task_group: Task group object to create.
        :param str project: Project ID or project name
        :rtype: :class:`<TaskGroup> <azure.devops.v5_1.task-agent.models.TaskGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(task_group, 'TaskGroupCreateParameter')
        response = self._send(http_method='POST',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def delete_task_group(self, project, task_group_id, comment=None):
        """DeleteTaskGroup.
        [Preview API] Delete a task group.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group to be deleted.
        :param str comment: Comments to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        self._send(http_method='DELETE',
                   location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                   version='5.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_task_groups(self, project, task_group_id=None, expanded=None, task_id_filter=None, deleted=None, top=None, continuation_token=None, query_order=None):
        """GetTaskGroups.
        [Preview API] List task groups.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group.
        :param bool expanded: 'true' to recursively expand task groups. Default is 'false'.
        :param str task_id_filter: Guid of the taskId to filter.
        :param bool deleted: 'true'to include deleted task groups. Default is 'false'.
        :param int top: Number of task groups to get.
        :param datetime continuation_token: Gets the task groups after the continuation token provided.
        :param str query_order: Gets the results in the defined order. Default is 'CreatedOnDescending'.
        :rtype: [TaskGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if expanded is not None:
            query_parameters['expanded'] = self._serialize.query('expanded', expanded, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'iso-8601')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TaskGroup]', self._unwrap_collection(response))

    def update_task_group(self, task_group, project, task_group_id=None):
        """UpdateTaskGroup.
        [Preview API] Update a task group.
        :param :class:`<TaskGroupUpdateParameter> <azure.devops.v5_1.task_agent.models.TaskGroupUpdateParameter>` task_group: Task group to update.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group to update.
        :rtype: :class:`<TaskGroup> <azure.devops.v5_1.task-agent.models.TaskGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        content = self._serialize.body(task_group, 'TaskGroupUpdateParameter')
        response = self._send(http_method='PUT',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def add_variable_group(self, group, project):
        """AddVariableGroup.
        [Preview API] Add a variable group.
        :param :class:`<VariableGroupParameters> <azure.devops.v5_1.task_agent.models.VariableGroupParameters>` group: Variable group to add.
        :param str project: Project ID or project name
        :rtype: :class:`<VariableGroup> <azure.devops.v5_1.task-agent.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(group, 'VariableGroupParameters')
        response = self._send(http_method='POST',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

    def delete_variable_group(self, project, group_id):
        """DeleteVariableGroup.
        [Preview API] Delete a variable group
        :param str project: Project ID or project name
        :param int group_id: Id of the variable group.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_variable_group(self, project, group_id):
        """GetVariableGroup.
        [Preview API] Get a variable group.
        :param str project: Project ID or project name
        :param int group_id: Id of the variable group.
        :rtype: :class:`<VariableGroup> <azure.devops.v5_1.task-agent.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('VariableGroup', response)

    def get_variable_groups(self, project, group_name=None, action_filter=None, top=None, continuation_token=None, query_order=None):
        """GetVariableGroups.
        [Preview API] Get variable groups.
        :param str project: Project ID or project name
        :param str group_name: Name of variable group.
        :param str action_filter: Action filter for the variable group. It specifies the action which can be performed on the variable groups.
        :param int top: Number of variable groups to get.
        :param int continuation_token: Gets the variable groups after the continuation token provided.
        :param str query_order: Gets the results in the defined order. Default is 'IdDescending'.
        :rtype: [VariableGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_name is not None:
            query_parameters['groupName'] = self._serialize.query('group_name', group_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'int')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[VariableGroup]', self._unwrap_collection(response))

    def get_variable_groups_by_id(self, project, group_ids):
        """GetVariableGroupsById.
        [Preview API] Get variable groups by ids.
        :param str project: Project ID or project name
        :param [int] group_ids: Comma separated list of Ids of variable groups.
        :rtype: [VariableGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_ids is not None:
            group_ids = ",".join(map(str, group_ids))
            query_parameters['groupIds'] = self._serialize.query('group_ids', group_ids, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[VariableGroup]', self._unwrap_collection(response))

    def update_variable_group(self, group, project, group_id):
        """UpdateVariableGroup.
        [Preview API] Update a variable group.
        :param :class:`<VariableGroupParameters> <azure.devops.v5_1.task_agent.models.VariableGroupParameters>` group: Variable group to update.
        :param str project: Project ID or project name
        :param int group_id: Id of the variable group to update.
        :rtype: :class:`<VariableGroup> <azure.devops.v5_1.task-agent.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        content = self._serialize.body(group, 'VariableGroupParameters')
        response = self._send(http_method='PUT',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

    def get_yaml_schema(self):
        """GetYamlSchema.
        [Preview API]
        :rtype: object
        """
        response = self._send(http_method='GET',
                              location_id='1f9990b9-1dba-441f-9c2e-6485888c42b6',
                              version='5.1-preview.1')
        return self._deserialize('object', response)

