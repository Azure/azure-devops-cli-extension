# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from azext_devops.dev.common.services import (get_new_task_agent_client,
                                              resolve_instance,
                                              resolve_instance_and_project)

logger = get_logger(__name__)


def list_pools(pool_name=None, pool_type=None, action=None, properties=None, organization=None, detect=None):
    """ (PREVIEW) List agent pools
    :param pool_name: Filter the list with matching pool name.
    :type pool_name: str
    :param pool_type: Filter the list with type of pool.
    :type pool_type: str
    :param action: Filter the list with user action permitted.
    :type action: str
    :param properties: Filter the list by agent pool properties. Comma separated list.
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pools(
        pool_name=pool_name, properties=properties, pool_type=pool_type, action_filter=action)


def show_pool(pool_id, action=None, properties=None, organization=None, detect=None):
    """ (PREVIEW) Show agent pool details
    :param pool_id: Id of the pool to list the details.
    :type pool_id: int
    :param action: Filter the list with user action permitted.
    :type action: str
    :param properties: Filter the list by agent pool properties. Comma separated list.
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pool(pool_id=pool_id, properties=properties, action_filter=action)


def list_agents(pool_id, agent_name=None, include_capabilities=None, include_assigned_request=None, properties=None,
                include_last_completed_request=None, demands=None, organization=None, detect=None):
    """ (PREVIEW) Get a list of agents in a pool
    :param pool_id: The agent pool containing the agents.
    :type pool_id: int
    :param agent_name: Filter on agent name.
    :type agent_name: str
    :param include_capabilities: Whether to include the agents' capabilities in the response.
    :type include_capabilities: bool
    :param include_assigned_request: Whether to include details about the agents' current work.
    :type include_assigned_request: bool
    :param include_last_completed_request: Whether to include details about the agents' most recent completed work.
    :type include_last_completed_request: bool
    :param properties: Filter which custom properties will be returned. Comma separated list.
    :type properties: str
    :param demands: Filter by demands the agents can satisfy. Comma separated list.
    :type demands: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    if demands:
        demands = list(map(str, demands.split(',')))
    return task_agent_client.get_agents(
        pool_id=pool_id, agent_name=agent_name, include_capabilities=include_capabilities,
        include_last_completed_request=include_last_completed_request,
        include_assigned_request=include_assigned_request, property_filters=properties, demands=demands)


def show_agent(pool_id, agent_id, include_capabilities=None, include_assigned_request=None, properties=None,
               include_last_completed_request=None, organization=None, detect=None):
    """ (PREVIEW) Show agent details
    :param pool_id: The agent pool containing the agent.
    :type pool_id: int
    :param agent_id: The agent ID to get information about.
    :type agent_id: str
    :param include_capabilities: Whether to include the agents' capabilities in the response.
    :type include_capabilities: bool
    :param include_assigned_request: Whether to include details about the agents' current work.
    :type include_assigned_request: bool
    :param include_last_completed_request: Whether to include details about the agents' most recent completed work.
    :type include_last_completed_request: bool
    :param properties: Filter which custom properties will be returned. Comma separated list.
    :type properties: [str]
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent(
        pool_id=pool_id, agent_id=agent_id, include_capabilities=include_capabilities,
        include_assigned_request=include_assigned_request,
        include_last_completed_request=include_last_completed_request, property_filters=properties)


def list_queues(queue_name=None, action=None, project=None, organization=None, detect=None):
    """ (PREVIEW) List agent queues
    :param queue_name: Filter the list with matching queue name regex.
    e.g. *ubuntu* for queue with name 'Hosted Ubuntu 1604'
    :type queue_name: str
    :param action: Filter by whether the calling user has use or manage permissions
    :type action: str
    """
    organization, project = resolve_instance_and_project(organization=organization, project=project, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    return task_agent_client.get_agent_queues(project=project, queue_name=queue_name, action_filter=action)


def show_queue(queue_id, action=None, project=None, organization=None, detect=None):
    """ (PREVIEW) Show details of agent queue
    :param queue_id: Id of the agent queue to get information about.
    :type queue_id: str
    :param action: Filter by whether the calling user has use or manage permissions
    :type action: str
    """
    organization, project = resolve_instance_and_project(organization=organization, project=project, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    return task_agent_client.get_agent_queue(project=project, queue_id=queue_id, action_filter=action)
