# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.task_agent import models


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

    def add_agent(self, agent, pool_id):
        """AddAgent.
        Adds an agent to a pool.  You probably don't want to call this endpoint directly. Instead, [configure an agent](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) using the agent download package.
        :param :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>` agent: Details about the agent being added
        :param int pool_id: The agent pool in which to add the agent
        :rtype: :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='POST',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def delete_agent(self, pool_id, agent_id):
        """DeleteAgent.
        Delete an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove an agent from your organization.
        :param int pool_id: The pool ID to remove the agent from
        :param int agent_id: The agent ID to remove
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        self._send(http_method='DELETE',
                   location_id='e298ef32-5878-4cab-993c-043836571f42',
                   version='5.1',
                   route_values=route_values)

    def get_agent(self, pool_id, agent_id, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None):
        """GetAgent.
        Get information about an agent.
        :param int pool_id: The agent pool containing the agent
        :param int agent_id: The agent ID to get information about
        :param bool include_capabilities: Whether to include the agent's capabilities in the response
        :param bool include_assigned_request: Whether to include details about the agent's current work
        :param bool include_last_completed_request: Whether to include details about the agents' most recent completed work
        :param [str] property_filters: Filter which custom properties will be returned
        :rtype: :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        query_parameters = {}
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_assigned_request is not None:
            query_parameters['includeAssignedRequest'] = self._serialize.query('include_assigned_request', include_assigned_request, 'bool')
        if include_last_completed_request is not None:
            query_parameters['includeLastCompletedRequest'] = self._serialize.query('include_last_completed_request', include_last_completed_request, 'bool')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgent', response)

    def get_agents(self, pool_id, agent_name=None, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None, demands=None):
        """GetAgents.
        Get a list of agents.
        :param int pool_id: The agent pool containing the agents
        :param str agent_name: Filter on agent name
        :param bool include_capabilities: Whether to include the agents' capabilities in the response
        :param bool include_assigned_request: Whether to include details about the agents' current work
        :param bool include_last_completed_request: Whether to include details about the agents' most recent completed work
        :param [str] property_filters: Filter which custom properties will be returned
        :param [str] demands: Filter by demands the agents can satisfy
        :rtype: [TaskAgent]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if agent_name is not None:
            query_parameters['agentName'] = self._serialize.query('agent_name', agent_name, 'str')
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_assigned_request is not None:
            query_parameters['includeAssignedRequest'] = self._serialize.query('include_assigned_request', include_assigned_request, 'bool')
        if include_last_completed_request is not None:
            query_parameters['includeLastCompletedRequest'] = self._serialize.query('include_last_completed_request', include_last_completed_request, 'bool')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if demands is not None:
            demands = ",".join(demands)
            query_parameters['demands'] = self._serialize.query('demands', demands, 'str')
        response = self._send(http_method='GET',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TaskAgent]', self._unwrap_collection(response))

    def replace_agent(self, agent, pool_id, agent_id):
        """ReplaceAgent.
        Replace an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove and reconfigure an agent from your organization.
        :param :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>` agent: Updated details about the replacing agent
        :param int pool_id: The agent pool to use
        :param int agent_id: The agent to replace
        :rtype: :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='PUT',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def update_agent(self, agent, pool_id, agent_id):
        """UpdateAgent.
        Update agent details.
        :param :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>` agent: Updated details about the agent
        :param int pool_id: The agent pool to use
        :param int agent_id: The agent to update
        :rtype: :class:`<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='PATCH',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def add_agent_pool(self, pool):
        """AddAgentPool.
        Create an agent pool.
        :param :class:`<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>` pool: Details about the new agent pool
        :rtype: :class:`<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
        """
        content = self._serialize.body(pool, 'TaskAgentPool')
        response = self._send(http_method='POST',
                              location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                              version='5.1',
                              content=content)
        return self._deserialize('TaskAgentPool', response)

    def delete_agent_pool(self, pool_id):
        """DeleteAgentPool.
        Delete an agent pool.
        :param int pool_id: ID of the agent pool to delete
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        self._send(http_method='DELETE',
                   location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                   version='5.1',
                   route_values=route_values)

    def get_agent_pool(self, pool_id, properties=None, action_filter=None):
        """GetAgentPool.
        Get information about an agent pool.
        :param int pool_id: An agent pool ID
        :param [str] properties: Agent pool properties (comma-separated)
        :param str action_filter: Filter by whether the calling user has use or manage permissions
        :rtype: :class:`<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if properties is not None:
            properties = ",".join(properties)
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgentPool', response)

    def get_agent_pools(self, pool_name=None, properties=None, pool_type=None, action_filter=None):
        """GetAgentPools.
        Get a list of agent pools.
        :param str pool_name: Filter by name
        :param [str] properties: Filter by agent pool properties (comma-separated)
        :param str pool_type: Filter by pool type
        :param str action_filter: Filter by whether the calling user has use or manage permissions
        :rtype: [TaskAgentPool]
        """
        query_parameters = {}
        if pool_name is not None:
            query_parameters['poolName'] = self._serialize.query('pool_name', pool_name, 'str')
        if properties is not None:
            properties = ",".join(properties)
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if pool_type is not None:
            query_parameters['poolType'] = self._serialize.query('pool_type', pool_type, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TaskAgentPool]', self._unwrap_collection(response))

    def get_agent_pools_by_ids(self, pool_ids, action_filter=None):
        """GetAgentPoolsByIds.
        Get a list of agent pools.
        :param [int] pool_ids: pool Ids to fetch
        :param str action_filter: Filter by whether the calling user has use or manage permissions
        :rtype: [TaskAgentPool]
        """
        query_parameters = {}
        if pool_ids is not None:
            pool_ids = ",".join(map(str, pool_ids))
            query_parameters['poolIds'] = self._serialize.query('pool_ids', pool_ids, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TaskAgentPool]', self._unwrap_collection(response))

    def update_agent_pool(self, pool, pool_id):
        """UpdateAgentPool.
        Update properties on an agent pool
        :param :class:`<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>` pool: Updated agent pool details
        :param int pool_id: The agent pool to update
        :rtype: :class:`<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(pool, 'TaskAgentPool')
        response = self._send(http_method='PATCH',
                              location_id='a8c47e17-4d56-4a56-92bb-de7ea7dc65be',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentPool', response)

    def get_yaml_schema(self):
        """GetYamlSchema.
        :rtype: object
        """
        response = self._send(http_method='GET',
                              location_id='1f9990b9-1dba-441f-9c2e-6485888c42b6',
                              version='5.1')
        return self._deserialize('object', response)

