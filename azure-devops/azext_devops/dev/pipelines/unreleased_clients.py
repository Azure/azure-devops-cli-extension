# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Taken from task_agent_client.py from python sdk for devops
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from azext_devops.vstsCompressed.vss_client import VssClient
from . import unreleased_models as models


class TaskAgentClient(VssClient):
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

    def add_environment(self, environment_create_parameter, project):
        """AddEnvironment.
        [Preview API] Create an environment.
        :param :class:`<EnvironmentCreateParameter> <azure.devops.v5_1.task_agent.models.EnvironmentCreateParameter>` environment_create_parameter: Environment to create.
        :param str project: Project ID or project name
        :rtype: :class:`<EnvironmentInstance> <azure.devops.v5_1.task-agent.models.EnvironmentInstance>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(environment_create_parameter, 'EnvironmentCreateParameter')
        response = self._send(http_method='POST',
                              location_id='8572b1fc-2482-47fa-8f74-7e3ed53ee54b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('EnvironmentInstance', response)

    def delete_environment(self, project, environment_id):
        """DeleteEnvironment.
        [Preview API] Delete the specified environment.
        :param str project: Project ID or project name
        :param int environment_id: ID of the environment.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='8572b1fc-2482-47fa-8f74-7e3ed53ee54b',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_environment_by_id(self, project, environment_id, expands=None):
        """GetEnvironmentById.
        [Preview API] Get an environment by its ID.
        :param str project: Project ID or project name
        :param int environment_id: ID of the environment.
        :param str expands: Include these additional details in the returned objects.
        :rtype: :class:`<EnvironmentInstance> <azure.devops.v5_1.task-agent.models.EnvironmentInstance>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        query_parameters = {}
        if expands is not None:
            query_parameters['expands'] = self._serialize.query('expands', expands, 'str')
        response = self._send(http_method='GET',
                              location_id='8572b1fc-2482-47fa-8f74-7e3ed53ee54b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('EnvironmentInstance', response)

    def get_environments(self, project, name=None, continuation_token=None, top=None):
        """GetEnvironments.
        [Preview API] Get all environments.
        :param str project: Project ID or project name
        :param str name:
        :param str continuation_token:
        :param int top:
        :rtype: [EnvironmentInstance]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='8572b1fc-2482-47fa-8f74-7e3ed53ee54b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[EnvironmentInstance]', self._unwrap_collection(response))

    def update_environment(self, environment_update_parameter, project, environment_id):
        """UpdateEnvironment.
        [Preview API] Update the specified environment.
        :param :class:`<EnvironmentUpdateParameter> <azure.devops.v5_1.task_agent.models.EnvironmentUpdateParameter>` environment_update_parameter: Environment data to update.
        :param str project: Project ID or project name
        :param int environment_id: ID of the environment.
        :rtype: :class:`<EnvironmentInstance> <azure.devops.v5_1.task-agent.models.EnvironmentInstance>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        content = self._serialize.body(environment_update_parameter, 'EnvironmentUpdateParameter')
        response = self._send(http_method='PATCH',
                              location_id='8572b1fc-2482-47fa-8f74-7e3ed53ee54b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('EnvironmentInstance', response)

    def add_kubernetes_resource(self, create_parameters, project, environment_id):
        """AddKubernetesResource.
        [Preview API]
        :param :class:`<KubernetesResourceCreateParameters> <azure.devops.v5_1.task_agent.models.KubernetesResourceCreateParameters>` create_parameters:
        :param str project: Project ID or project name
        :param int environment_id:
        :rtype: :class:`<KubernetesResource> <azure.devops.v5_1.task-agent.models.KubernetesResource>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        content = self._serialize.body(create_parameters, 'KubernetesResourceCreateParameters')
        response = self._send(http_method='POST',
                              location_id='73fba52f-15ab-42b3-a538-ce67a9223a04',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('KubernetesResource', response)

    def delete_kubernetes_resource(self, project, environment_id, resource_id):
        """DeleteKubernetesResource.
        [Preview API]
        :param str project: Project ID or project name
        :param int environment_id:
        :param int resource_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        if resource_id is not None:
            route_values['resourceId'] = self._serialize.url('resource_id', resource_id, 'int')
        self._send(http_method='DELETE',
                   location_id='73fba52f-15ab-42b3-a538-ce67a9223a04',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_kubernetes_resource(self, project, environment_id, resource_id):
        """GetKubernetesResource.
        [Preview API]
        :param str project: Project ID or project name
        :param int environment_id:
        :param int resource_id:
        :rtype: :class:`<KubernetesResource> <azure.devops.v5_1.task-agent.models.KubernetesResource>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        if resource_id is not None:
            route_values['resourceId'] = self._serialize.url('resource_id', resource_id, 'int')
        response = self._send(http_method='GET',
                              location_id='73fba52f-15ab-42b3-a538-ce67a9223a04',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('KubernetesResource', response)

    def update_kubernetes_resource(self, resource, project, environment_id):
        """UpdateKubernetesResource.
        [Preview API]
        :param :class:`<KubernetesResource> <azure.devops.v5_1.task_agent.models.KubernetesResource>` resource:
        :param str project: Project ID or project name
        :param int environment_id:
        :rtype: :class:`<KubernetesResource> <azure.devops.v5_1.task-agent.models.KubernetesResource>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if environment_id is not None:
            route_values['environmentId'] = self._serialize.url('environment_id', environment_id, 'int')
        content = self._serialize.body(resource, 'KubernetesResource')
        response = self._send(http_method='PATCH',
                              location_id='73fba52f-15ab-42b3-a538-ce67a9223a04',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('KubernetesResource', response)

    def get_agent_queues(self, project=None, queue_name=None, action_filter=None):
        """GetAgentQueues.
        [Preview API] Get a list of agent queues.
        :param str project: Project ID or project name
        :param str queue_name: Filter on the agent queue name
        :param str action_filter: Filter by whether the calling user has use or manage permissions
        :rtype: [TaskAgentQueue]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if queue_name is not None:
            query_parameters['queueName'] = self._serialize.query('queue_name', queue_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TaskAgentQueue]', self._unwrap_collection(response))
