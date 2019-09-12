# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class PipelinesAgentPoolQueueTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_pipeline_pools_and_agents(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        valid_pool_id = None

        # list agent pools
        list_pools_command = 'az pipelines pool list --pool-type automation --pool-name Hosted --detect false --output json'
        list_pools_output = self.cmd(list_pools_command).get_output_in_json()
        assert len(list_pools_output) > 0
        # if one of these fields are missing table output will break
        for pool in list_pools_output:
            assert pool['id'] is not None
            assert pool['name'] is not None
            assert pool['isHosted'] is not None
            assert pool['poolType'] is not None
            # get pool id for show command 
            if not valid_pool_id:
                valid_pool_id = pool['id']

        # show pool
        show_pool_command = 'az pipelines pool show --pool-id {} --detect false --output json'.format(valid_pool_id)
        show_pool_output = self.cmd(show_pool_command).get_output_in_json()
        assert len(show_pool_output) > 0
        # if one of these fields are missing table output will break
        assert show_pool_output['id'] == valid_pool_id
        assert show_pool_output['name'] is not None
        assert show_pool_output['isHosted'] is not None
        assert show_pool_output['poolType'] is not None

        
        valid_agent_id = None

        # list agents
        list_agents_command = 'az pipelines agent list --pool-id {} --detect false --output json'.format(valid_pool_id)
        list_agents_output = self.cmd(list_agents_command).get_output_in_json()
        assert len(list_agents_output) > 0
        # if one of these fields are missing table output will break
        for agent in list_agents_output:
            assert agent['id'] is not None
            assert agent['name'] is not None
            assert agent['enabled'] is not None
            assert agent['status'] is not None
            assert agent['version'] is not None
            # get pool id for show command 
            if not valid_agent_id:
                valid_agent_id = agent['id']

        # show agent
        show_agent_command = 'az pipelines agent show --pool-id {} --agent-id {} --detect false --output json'.format(valid_pool_id, valid_agent_id)
        show_agent_output = self.cmd(show_agent_command).get_output_in_json()
        # if one of these fields are missing table output will break
        assert len(show_agent_output) > 0
        assert agent['id'] is not None
        assert agent['name'] is not None
        assert agent['enabled'] is not None
        assert agent['status'] is not None
        assert agent['version'] is not None

    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_pipeline_queues(self):
        # Queues are at project level so create a project which we will clean up
        random_project_name = self.create_random_name(prefix='pipelineQueueTests', length=25)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            valid_queue_id = None

            # list agent pools
            list_queues_command = 'az pipelines queue list --detect false --output json'
            list_queues_output = self.cmd(list_queues_command).get_output_in_json()
            assert len(list_queues_output) > 0
            # if one of these fields are missing table output will break
            for queue in list_queues_output:
                assert queue['id'] is not None
                assert queue['name'] is not None
                assert queue['pool']['isHosted'] is not None
                assert queue['pool']['poolType'] is not None
                # get pool id for show command 
                if not valid_queue_id:
                    valid_queue_id = queue['id']

            # show pool
            show_queue_command = 'az pipelines queue show --queue-id {} --detect false --output json'.format(valid_queue_id)
            show_queue_output = self.cmd(show_queue_command).get_output_in_json()
            assert len(show_queue_output) > 0
            # if one of these fields are missing table output will break
            assert show_queue_output['id'] == valid_queue_id
            assert show_queue_output['name'] is not None
            assert show_queue_output['pool']['isHosted'] is not None
            assert show_queue_output['pool']['poolType'] is not None
        
        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
