# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_devops.dev.common.services import (get_unreleased_task_agent_client,
                                              resolve_instance_and_project)
from .unreleased_models import (EnvironmentCreateParameter, KubernetesResourceCreateParameters,
                                VirtualMachineGroupCreateParameters)

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


def delete_environment(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
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


def get_environment(id, expand=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
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


def get_environment_resources(environment_id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """
    Show all resources in an environment
    :param environment_id: Id of the environment
    :type environment_id: int
    """
    return get_environment(id=environment_id, expand=True, organization=organization, project=project, detect=detect)


def add_environment_resource(environment_id, resource_name, resource_type=None, kubernetes_namespace=None,
                             service_connection_id=None, organization=None, project=None, detect=None):
    """
    Add a resource to an environment
    :param environment_id: Id of the environment to add the resource to
    :type environment_id: int
    :param resource_type: Type of resource
    :type resource_type: str
    :param resource_name: Name of resource
    :type resource_name: str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    resource_type = resource_type.lower()
    if resource_type == 'kubernetes':
        if not resource_name or not kubernetes_namespace or not service_connection_id:
            raise CLIError('--resource-name, --kubernetes-namespace and'
                           '--service-connection-id is required for adding a Kubernetes resource.')
        res_params = KubernetesResourceCreateParameters()
        res_params.name = resource_name
        res_params.namespace = kubernetes_namespace
        res_params.service_endpoint_id = service_connection_id
        return env_client.add_kubernetes_resource(create_parameters=res_params,
                                                  environment_id=environment_id, project=project)
    if resource_type == 'vm':
        if not resource_name:
            raise CLIError('--resource-name is required for adding a Virtual Machine resource.')
        res_params = VirtualMachineGroupCreateParameters()
        res_params.name = resource_name
        return env_client.add_virtual_machine_group(create_parameters=res_params,
                                                    environment_id=environment_id, project=project)


def delete_environment_resource(environment_id, resource_id, resource_type=None,
                                organization=None, project=None, detect=None):
    """
    Delete a resource from an environment
    :param environment_id: Id of the environment
    :type environment_id: int
    :param resource_id: Id of the resource
    :type resource_id: int
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project,
                                                         project_required=True)
    env_client = get_unreleased_task_agent_client(organization=organization)
    if not resource_type:
        environment_details = get_environment(id=environment_id, expand=True,
                                              organization=organization, project=project, detect=detect)
        resources = environment_details.resources
        resource_found = False
        for resource in resources:
            if resource.id == int(resource_id):
                resource_type = resource.type
                resource_found = True
                break
        if not resource_found:
            raise CLIError('Could not find a matching resource with id {res_id} in the environment {env_id}.'
                           .format(res_id=resource_id, env_id=environment_details.name))
        # delete based on resource type
        if resource_type == 'kubernetes':
            env_client.delete_kubernetes_resource(project=project, environment_id=environment_id,
                                                  resource_id=resource_id)
        if resource_type == 'vm' or resource_type.lower() == 'virtualmachine':
            env_client.delete_virtual_machine_group(project=project, environment_id=environment_id,
                                                    resource_id=resource_id)
