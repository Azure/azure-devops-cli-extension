﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.policy import models


class PolicyClient(Client):
    """Policy
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(PolicyClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'fb13a388-40dd-4a04-b530-013a739c72ef'

    def create_policy_configuration(self, configuration, project, configuration_id=None):
        """CreatePolicyConfiguration.
        Create a policy configuration of a given policy type.
        :param :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>` configuration: The policy configuration to create.
        :param str project: Project ID or project name
        :param int configuration_id:
        :rtype: :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        content = self._serialize.body(configuration, 'PolicyConfiguration')
        response = self._send(http_method='POST',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PolicyConfiguration', response)

    def delete_policy_configuration(self, project, configuration_id):
        """DeletePolicyConfiguration.
        Delete a policy configuration by its ID.
        :param str project: Project ID or project name
        :param int configuration_id: ID of the policy configuration to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        self._send(http_method='DELETE',
                   location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                   version='5.1',
                   route_values=route_values)

    def get_policy_configuration(self, project, configuration_id):
        """GetPolicyConfiguration.
        Get a policy configuration by its ID.
        :param str project: Project ID or project name
        :param int configuration_id: ID of the policy configuration
        :rtype: :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_configurations(self, project, scope=None, top=None, continuation_token=None, policy_type=None):
        """GetPolicyConfigurations.
        Get a list of policy configurations in a project.
        :param str project: Project ID or project name
        :param str scope: [Provided for legacy reasons] The scope on which a subset of policies is defined.
        :param int top: Maximum number of policies to return.
        :param str continuation_token: The continuation token used for pagination.
        :param str policy_type: Filter returned policies to only this type
        :rtype: :class:`<GetPolicyConfigurationsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if policy_type is not None:
            query_parameters['policyType'] = self._serialize.query('policy_type', policy_type, 'str')
        response = self._send(http_method='GET',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[PolicyConfiguration]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetPolicyConfigurationsResponseValue(response_value, continuation_token)

    class GetPolicyConfigurationsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_policy_configurations method

            :param value:
            :type value: :class:`<[PolicyConfiguration]> <azure.devops.v5_1.policy.models.[PolicyConfiguration]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_policy_configuration(self, configuration, project, configuration_id):
        """UpdatePolicyConfiguration.
        Update a policy configuration by its ID.
        :param :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>` configuration: The policy configuration to update.
        :param str project: Project ID or project name
        :param int configuration_id: ID of the existing policy configuration to be updated.
        :rtype: :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        content = self._serialize.body(configuration, 'PolicyConfiguration')
        response = self._send(http_method='PUT',
                              location_id='dad91cbe-d183-45f8-9c6e-9c1164472121',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_configuration_revision(self, project, configuration_id, revision_id):
        """GetPolicyConfigurationRevision.
        Retrieve a specific revision of a given policy by ID.
        :param str project: Project ID or project name
        :param int configuration_id: The policy configuration ID.
        :param int revision_id: The revision ID.
        :rtype: :class:`<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        if revision_id is not None:
            route_values['revisionId'] = self._serialize.url('revision_id', revision_id, 'int')
        response = self._send(http_method='GET',
                              location_id='fe1e68a2-60d3-43cb-855b-85e41ae97c95',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyConfiguration', response)

    def get_policy_configuration_revisions(self, project, configuration_id, top=None, skip=None):
        """GetPolicyConfigurationRevisions.
        Retrieve all revisions for a given policy.
        :param str project: Project ID or project name
        :param int configuration_id: The policy configuration ID.
        :param int top: The number of revisions to retrieve.
        :param int skip: The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.
        :rtype: [PolicyConfiguration]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if configuration_id is not None:
            route_values['configurationId'] = self._serialize.url('configuration_id', configuration_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='fe1e68a2-60d3-43cb-855b-85e41ae97c95',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[PolicyConfiguration]', self._unwrap_collection(response))

    def get_policy_type(self, project, type_id):
        """GetPolicyType.
        Retrieve a specific policy type by ID.
        :param str project: Project ID or project name
        :param str type_id: The policy ID.
        :rtype: :class:`<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type_id is not None:
            route_values['typeId'] = self._serialize.url('type_id', type_id, 'str')
        response = self._send(http_method='GET',
                              location_id='44096322-2d3d-466a-bb30-d1b7de69f61f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('PolicyType', response)

    def get_policy_types(self, project):
        """GetPolicyTypes.
        Retrieve all available policy types.
        :param str project: Project ID or project name
        :rtype: [PolicyType]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='44096322-2d3d-466a-bb30-d1b7de69f61f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[PolicyType]', self._unwrap_collection(response))

