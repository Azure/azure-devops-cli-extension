# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests
from azext_devops.devops_sdk.v5_1.task_agent.task_agent_client import TaskAgentClient
from azext_devops.dev.pipelines.agent_pool_queue import list_pools, show_pool, list_agents, show_agent, list_queues, show_queue

class TestPipelinesRunsArtifactsMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'MyProject'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()

        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client')
        #start the patchers
        self.mock_get_client = self.get_client_patcher.start()
        # Set return values which will be same across tests
        self.mock_get_client.return_value = TaskAgentClient(base_url=self._TEST_DEVOPS_ORGANIZATION)
        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_pool_list_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_pools') as mock_get_pools:
            # pool listing
            pools = list_pools(pool_name=None, pool_type=None, action=None, properties=None, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_pools.assert_called_once_with(pool_name=None, properties=None, pool_type=None, action_filter=None)

    def test_pool_list_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_pools') as mock_get_pools:
            # pool listing
            pools = list_pools(pool_name='PoolName', pool_type='PoolType', action='ActionUse', properties='prop1,prop2', organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_pools.assert_called_once_with(pool_name='PoolName', properties=['prop1', 'prop2'], pool_type='PoolType', action_filter='ActionUse')

    def test_pool_show_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_pool') as mock_get_pool:
            # pool show
            pool = show_pool(pool_id='123', action=None, properties=None, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_pool.assert_called_once_with(pool_id='123', properties=None, action_filter=None)

    def test_pool_show_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_pool') as mock_get_pool:
            # pool show
            pool = show_pool(pool_id='123', action='ActionUse', properties='prop1,prop2', organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_pool.assert_called_once_with(pool_id='123', properties=['prop1', 'prop2'], action_filter='ActionUse')

    def test_agent_list_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agents') as mock_get_agents:
            # agent listing
            agents = list_agents(pool_id='123', agent_name=None, include_capabilities=None, include_assigned_request=None, properties=None,
                include_last_completed_request=None, demands=None, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_agents.assert_called_once_with(pool_id='123', agent_name=None, include_capabilities=None,
        include_last_completed_request=None, include_assigned_request=None, property_filters=None, demands=None)

    def test_agent_list_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agents') as mock_get_agents:
            # agent listing
            agents = list_agents(pool_id='123', agent_name='myagent', include_capabilities=True, include_assigned_request=True, properties='prop1,prop2',
                include_last_completed_request=True, demands='demand1,demand2', organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_agents.assert_called_once_with(pool_id='123', agent_name='myagent', include_capabilities=True,
        include_last_completed_request=True, include_assigned_request=True, property_filters=['prop1', 'prop2'], demands=['demand1', 'demand2'])

    def test_agent_show_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent') as mock_get_agent:
            # agent Show
            agents = show_agent(pool_id='123', agent_id='1234', include_capabilities=None, include_assigned_request=None, properties=None,
               include_last_completed_request=None, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_agent.assert_called_once_with(
                pool_id='123', agent_id='1234', include_capabilities=None,
                include_assigned_request=None, include_last_completed_request=None, property_filters=None)

    def test_agent_show_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent') as mock_get_agent:
            # agent Show
            agents = show_agent(pool_id='123', agent_id='1234', include_capabilities=True, include_assigned_request=True, properties='prop1,prop2',
               include_last_completed_request=True, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_agent.assert_called_once_with(
                pool_id='123', agent_id='1234', include_capabilities=True,
                include_assigned_request=True, include_last_completed_request=True, property_filters=['prop1', 'prop2'])

    def test_queue_list_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_queues') as mock_get_queues:
            # queue listing
            queues = list_queues(queue_name=None, action=None, project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_queues.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, queue_name=None, action_filter=None)

    def test_queue_list_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_queues') as mock_get_queues:
            # queue listing
            queues = list_queues(queue_name='Ubuntu', action='ActionUse', project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_queues.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, queue_name='Ubuntu', action_filter='ActionUse')

    def test_queue_show_with_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_queue') as mock_get_queue:
            # queue listing
            queues = show_queue(queue_id='123', action=None, project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_queue.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, queue_id='123', action_filter=None)

    def test_queue_show_without_defaults(self):
        with patch('azext_devops.devops_sdk.v5_1.task_agent.task_agent_client.TaskAgentClient.get_agent_queue') as mock_get_queue:
            # queue listing
            queues = show_queue(queue_id='123', action='ActionUse', project=self._TEST_DEVOPS_PROJECT, organization=self._TEST_DEVOPS_ORGANIZATION)
            # assert
            mock_get_queue.assert_called_once_with(project=self._TEST_DEVOPS_PROJECT, queue_id='123', action_filter='ActionUse')
