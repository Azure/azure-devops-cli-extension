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


class PipelinePermissionsClient(Client):
    """PipelinePermissions
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(PipelinePermissionsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'a81a0441-de52-4000-aa15-ff0e07bfbbaa'

    def get_pipeline_permissions_for_resource(self, project, resource_type, resource_id):
        """GetPipelinePermissionsForResource.
        [Preview API] Given a ResourceType and ResourceId, returns authorized definitions for that resource.
        :param str project: Project ID or project name
        :param str resource_type:
        :param str resource_id:
        :rtype: :class:`<ResourcePipelinePermissions> <azure.devops.v6_0.pipeline_permissions.models.ResourcePipelinePermissions>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if resource_type is not None:
            route_values['resourceType'] = self._serialize.url('resource_type', resource_type, 'str')
        if resource_id is not None:
            route_values['resourceId'] = self._serialize.url('resource_id', resource_id, 'str')
        response = self._send(http_method='GET',
                              location_id='b5b9a4a4-e6cd-4096-853c-ab7d8b0c4eb2',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ResourcePipelinePermissions', response)

    def update_pipeline_permisions_for_resource(self, resource_authorization, project, resource_type, resource_id):
        """UpdatePipelinePermisionsForResource.
        [Preview API] Authorizes/Unauthorizes a list of definitions for a given resource.
        :param :class:`<ResourcePipelinePermissions> <azure.devops.v6_0.pipeline_permissions.models.ResourcePipelinePermissions>` resource_authorization:
        :param str project: Project ID or project name
        :param str resource_type:
        :param str resource_id:
        :rtype: :class:`<ResourcePipelinePermissions> <azure.devops.v6_0.pipeline_permissions.models.ResourcePipelinePermissions>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if resource_type is not None:
            route_values['resourceType'] = self._serialize.url('resource_type', resource_type, 'str')
        if resource_id is not None:
            route_values['resourceId'] = self._serialize.url('resource_id', resource_id, 'str')
        content = self._serialize.body(resource_authorization, 'ResourcePipelinePermissions')
        response = self._send(http_method='PATCH',
                              location_id='b5b9a4a4-e6cd-4096-853c-ab7d8b0c4eb2',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ResourcePipelinePermissions', response)

    def update_pipeline_permisions_for_resources(self, resource_authorizations, project):
        """UpdatePipelinePermisionsForResources.
        [Preview API] Batch API to authorize/unauthorize a list of definitions for a multiple resources.
        :param [ResourcePipelinePermissions] resource_authorizations:
        :param str project: Project ID or project name
        :rtype: [ResourcePipelinePermissions]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(resource_authorizations, '[ResourcePipelinePermissions]')
        response = self._send(http_method='PATCH',
                              location_id='b5b9a4a4-e6cd-4096-853c-ab7d8b0c4eb2',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[ResourcePipelinePermissions]', self._unwrap_collection(response))

