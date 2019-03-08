# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_unreleased_task_agent_client,
                                              resolve_instance_and_project)
from .unreleased_models import EnvironmentCreateParameter

def create_environment(name, description=None, organization=None, project=None, detect=None):
    """
    Create an environment
    :param name: Name of the new environment to create
    :type name: str
    :param description: Description for the environment
    :type description: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    env_create_param = EnvironmentCreateParameter()
    env_create_param.name = name
    env_create_param.description = description
    return env_client.add_environment(environment_create_parameter=env_create_param, project=project)


def delete_environment(id=None, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """
    Delete an environment
    :param name: Id of the environment to delete
    :type name: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    return env_client.delete_environment(environment_id=id, project=project)


def get_environment(id=None, expand=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """
    Show details of an environment
    :param id: Id of the environment to show
    :type id: int
    :param expand: If this flag is present the details of resources in the environment is also fetched.
    :type expand: bool
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    expand = 1 if expand else 0
    return env_client.get_environment_by_id(environment_id=id, project=project, expands=expand)


def get_environments(organization=None, project=None, detect=None):
    """
    List all environments in the project
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    return env_client.get_environments(project=project)


def get_environment_resources(id=None, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """
    Show resources within an environment
    :param id: Id of the environment to show
    :type id: int
    """
    return get_environment(id=id, expand=True, organization=organization, project=project, detect=detect)
