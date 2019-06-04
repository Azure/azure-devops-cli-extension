# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
logger = get_logger(__name__)

from azext_devops.dev.common.services import (get_new_task_agent_client,
                                              resolve_instance,
                                              resolve_instance_and_project)


def list_pools(pool_name=None, pool_type=None, action=None, properties=None, organization=None, detect=None):
    """
    List agent pools
    :param pool_name: Filter the list with matching pool name.
    :type pool_name: str
    :param pool_type: Filter the list with type of pool.
    :type pool_type: str
    :param action: Filter the list with user action permitted.
    :type action: str
    :param properties: Filter the list by agent pool properties.
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pools(
        pool_name=pool_name, properties=properties, pool_type=pool_type, action_filter=action)


def show_pool(pool_id, action=None, properties=None, organization=None, detect=None):
    """
    Show agent pool details
    :param pool_id: Id of the pool to list the details.
    :type pool_id: int
    :param action: Filter the list with user action permitted.
    :type action: str
    :param properties: Filter the list by agent pool properties.
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pool(pool_id=pool_id, properties=properties, action_filter=action)


def list_agents(pool_name=None, pool_type=None, action=None, properties=None, organization=None, detect=None):
    """
    List agents
    :param pool_name: Filter the list with matching pool name.
    :type pool_name: str
    :param pool_type: Filter the list with type of pool.
    :type pool_type: str
    :param action: Filter the list with user action permitted.
    :type action: str
    :param properties: Filter the list by agent pool properties.
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pools(
        pool_name=pool_name, properties=properties, pool_type=pool_type, action_filter=action)


def show_agent(pool_id, action=None, properties=None, organization=None, detect=None):
    """
    Show agent details
    :param pool_id: Id of the pool to which the agent belongs.
    :type pool_id: int
    :param agent_id: Id of the agent to list the details.
    :type agent_id: int
    :type properties: str
    """
    organization = resolve_instance(organization=organization, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    if properties:
        properties = list(map(str, properties.split(',')))
    return task_agent_client.get_agent_pool(pool_id=pool_id, properties=properties, action_filter=action)

def list_queues(queue_name=None, action=None, project=None, organization=None, detect=None):
    """
    List agent queues
    :param queue_name: Filter the list with matching queue name regex.
    e.g. *ubuntu* for queue with name 'Hosted Ubuntu 1604'
    :type queue_name: str
    :param action: Filter the list with user action permitted.
    :type action: str
    """
    organization, project = resolve_instance_and_project(organization=organization, project=project, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    return task_agent_client.get_agent_queues(project=project, queue_name=queue_name, action_filter=action)


def show_queue(queue_id=None, action=None, project=None, organization=None, detect=None):
    """
    Show details of agent queue
    :param queue_id: Filter the list with matching pool name.
    :type queue_id: str
    :param action: Filter the list with user action permitted.
    :type action: str
    """
    organization, project = resolve_instance_and_project(organization=organization, project=project, detect=detect)
    task_agent_client = get_new_task_agent_client(organization=organization)
    return task_agent_client.get_agent_queue(project=project, queue_id=queue_id, action_filter=action)
