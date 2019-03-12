# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AadOauthTokenRequest(Model):
    """AadOauthTokenRequest.

    :param refresh:
    :type refresh: bool
    :param resource:
    :type resource: str
    :param tenant_id:
    :type tenant_id: str
    :param token:
    :type token: str
    """

    _attribute_map = {
        'refresh': {'key': 'refresh', 'type': 'bool'},
        'resource': {'key': 'resource', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'}
    }

    def __init__(self, refresh=None, resource=None, tenant_id=None, token=None):
        super(AadOauthTokenRequest, self).__init__()
        self.refresh = refresh
        self.resource = resource
        self.tenant_id = tenant_id
        self.token = token


class AadOauthTokenResult(Model):
    """AadOauthTokenResult.

    :param access_token:
    :type access_token: str
    :param refresh_token_cache:
    :type refresh_token_cache: str
    """

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'str'},
        'refresh_token_cache': {'key': 'refreshTokenCache', 'type': 'str'}
    }

    def __init__(self, access_token=None, refresh_token_cache=None):
        super(AadOauthTokenResult, self).__init__()
        self.access_token = access_token
        self.refresh_token_cache = refresh_token_cache


class AuthenticationSchemeReference(Model):
    """AuthenticationSchemeReference.

    :param inputs:
    :type inputs: dict
    :param type:
    :type type: str
    """

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, inputs=None, type=None):
        super(AuthenticationSchemeReference, self).__init__()
        self.inputs = inputs
        self.type = type


class AuthorizationHeader(Model):
    """AuthorizationHeader.

    :param name: Gets or sets the name of authorization header.
    :type name: str
    :param value: Gets or sets the value of authorization header.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(AuthorizationHeader, self).__init__()
        self.name = name
        self.value = value


class AzureManagementGroup(Model):
    """AzureManagementGroup.

    :param display_name: Display name of azure management group
    :type display_name: str
    :param id: Id of azure management group
    :type id: str
    :param name: Azure management group name
    :type name: str
    :param tenant_id: Id of tenant from which azure management group belogs
    :type tenant_id: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, name=None, tenant_id=None):
        super(AzureManagementGroup, self).__init__()
        self.display_name = display_name
        self.id = id
        self.name = name
        self.tenant_id = tenant_id


class AzureManagementGroupQueryResult(Model):
    """AzureManagementGroupQueryResult.

    :param error_message: Error message in case of an exception
    :type error_message: str
    :param value: List of azure management groups
    :type value: list of :class:`AzureManagementGroup <azure.devops.v5_1.task_agent.models.AzureManagementGroup>`
    """

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'value': {'key': 'value', 'type': '[AzureManagementGroup]'}
    }

    def __init__(self, error_message=None, value=None):
        super(AzureManagementGroupQueryResult, self).__init__()
        self.error_message = error_message
        self.value = value


class AzureSubscription(Model):
    """AzureSubscription.

    :param display_name:
    :type display_name: str
    :param subscription_id:
    :type subscription_id: str
    :param subscription_tenant_id:
    :type subscription_tenant_id: str
    :param subscription_tenant_name:
    :type subscription_tenant_name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'subscription_tenant_id': {'key': 'subscriptionTenantId', 'type': 'str'},
        'subscription_tenant_name': {'key': 'subscriptionTenantName', 'type': 'str'}
    }

    def __init__(self, display_name=None, subscription_id=None, subscription_tenant_id=None, subscription_tenant_name=None):
        super(AzureSubscription, self).__init__()
        self.display_name = display_name
        self.subscription_id = subscription_id
        self.subscription_tenant_id = subscription_tenant_id
        self.subscription_tenant_name = subscription_tenant_name


class AzureSubscriptionQueryResult(Model):
    """AzureSubscriptionQueryResult.

    :param error_message:
    :type error_message: str
    :param value:
    :type value: list of :class:`AzureSubscription <azure.devops.v5_1.task_agent.models.AzureSubscription>`
    """

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'value': {'key': 'value', 'type': '[AzureSubscription]'}
    }

    def __init__(self, error_message=None, value=None):
        super(AzureSubscriptionQueryResult, self).__init__()
        self.error_message = error_message
        self.value = value


class ClientCertificate(Model):
    """ClientCertificate.

    :param value: Gets or sets the value of client certificate.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, value=None):
        super(ClientCertificate, self).__init__()
        self.value = value


class DataSource(Model):
    """DataSource.

    :param authentication_scheme:
    :type authentication_scheme: :class:`AuthenticationSchemeReference <azure.devops.v5_1.task_agent.models.AuthenticationSchemeReference>`
    :param endpoint_url:
    :type endpoint_url: str
    :param headers:
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.task_agent.models.AuthorizationHeader>`
    :param name:
    :type name: str
    :param resource_url:
    :type resource_url: str
    :param result_selector:
    :type result_selector: str
    """

    _attribute_map = {
        'authentication_scheme': {'key': 'authenticationScheme', 'type': 'AuthenticationSchemeReference'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'name': {'key': 'name', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, authentication_scheme=None, endpoint_url=None, headers=None, name=None, resource_url=None, result_selector=None):
        super(DataSource, self).__init__()
        self.authentication_scheme = authentication_scheme
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.name = name
        self.resource_url = resource_url
        self.result_selector = result_selector


class DataSourceBindingBase(Model):
    """DataSourceBindingBase.

    :param callback_context_template: Pagination format supported by this data source(ContinuationToken/SkipTop).
    :type callback_context_template: str
    :param callback_required_template: Subsequent calls needed?
    :type callback_required_template: str
    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
    :param request_content: Gets or sets http request body
    :type request_content: str
    :param request_verb: Gets or sets http request verb
    :type request_verb: str
    :param result_selector: Gets or sets the result selector.
    :type result_selector: str
    :param result_template: Gets or sets the result template.
    :type result_template: str
    :param target: Gets or sets the target of the data source.
    :type target: str
    """

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DataSourceDetails(Model):
    """DataSourceDetails.

    :param data_source_name:
    :type data_source_name: str
    :param data_source_url:
    :type data_source_url: str
    :param headers:
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.task_agent.models.AuthorizationHeader>`
    :param parameters:
    :type parameters: dict
    :param resource_url:
    :type resource_url: str
    :param result_selector:
    :type result_selector: str
    """

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'data_source_url': {'key': 'dataSourceUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, data_source_url=None, headers=None, parameters=None, resource_url=None, result_selector=None):
        super(DataSourceDetails, self).__init__()
        self.data_source_name = data_source_name
        self.data_source_url = data_source_url
        self.headers = headers
        self.parameters = parameters
        self.resource_url = resource_url
        self.result_selector = result_selector


class DependencyBinding(Model):
    """DependencyBinding.

    :param key:
    :type key: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, key=None, value=None):
        super(DependencyBinding, self).__init__()
        self.key = key
        self.value = value


class DependencyData(Model):
    """DependencyData.

    :param input:
    :type input: str
    :param map:
    :type map: list of { key: str; value: [{ key: str; value: str }] }
    """

    _attribute_map = {
        'input': {'key': 'input', 'type': 'str'},
        'map': {'key': 'map', 'type': '[{ key: str; value: [{ key: str; value: str }] }]'}
    }

    def __init__(self, input=None, map=None):
        super(DependencyData, self).__init__()
        self.input = input
        self.map = map


class DependsOn(Model):
    """DependsOn.

    :param input:
    :type input: str
    :param map:
    :type map: list of :class:`DependencyBinding <azure.devops.v5_1.task_agent.models.DependencyBinding>`
    """

    _attribute_map = {
        'input': {'key': 'input', 'type': 'str'},
        'map': {'key': 'map', 'type': '[DependencyBinding]'}
    }

    def __init__(self, input=None, map=None):
        super(DependsOn, self).__init__()
        self.input = input
        self.map = map


class DeploymentGroupCreateParameter(Model):
    """DeploymentGroupCreateParameter.

    :param description: Description of the deployment group.
    :type description: str
    :param name: Name of the deployment group.
    :type name: str
    :param pool: Deployment pool in which deployment agents are registered. This is obsolete. Kept for compatibility. Will be marked obsolete explicitly by M132.
    :type pool: :class:`DeploymentGroupCreateParameterPoolProperty <azure.devops.v5_1.task_agent.models.DeploymentGroupCreateParameterPoolProperty>`
    :param pool_id: Identifier of the deployment pool in which deployment agents are registered.
    :type pool_id: int
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'DeploymentGroupCreateParameterPoolProperty'},
        'pool_id': {'key': 'poolId', 'type': 'int'}
    }

    def __init__(self, description=None, name=None, pool=None, pool_id=None):
        super(DeploymentGroupCreateParameter, self).__init__()
        self.description = description
        self.name = name
        self.pool = pool
        self.pool_id = pool_id


class DeploymentGroupCreateParameterPoolProperty(Model):
    """DeploymentGroupCreateParameterPoolProperty.

    :param id: Deployment pool identifier.
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(DeploymentGroupCreateParameterPoolProperty, self).__init__()
        self.id = id


class DeploymentGroupMetrics(Model):
    """DeploymentGroupMetrics.

    :param columns_header: List of deployment group properties. And types of metrics provided for those properties.
    :type columns_header: :class:`MetricsColumnsHeader <azure.devops.v5_1.task_agent.models.MetricsColumnsHeader>`
    :param deployment_group: Deployment group.
    :type deployment_group: :class:`DeploymentGroupReference <azure.devops.v5_1.task_agent.models.DeploymentGroupReference>`
    :param rows: Values of properties and the metrics. E.g. 1: total count of deployment targets for which 'TargetState' is 'offline'. E.g. 2: Average time of deployment to the deployment targets for which 'LastJobStatus' is 'passed' and 'TargetState' is 'online'.
    :type rows: list of :class:`MetricsRow <azure.devops.v5_1.task_agent.models.MetricsRow>`
    """

    _attribute_map = {
        'columns_header': {'key': 'columnsHeader', 'type': 'MetricsColumnsHeader'},
        'deployment_group': {'key': 'deploymentGroup', 'type': 'DeploymentGroupReference'},
        'rows': {'key': 'rows', 'type': '[MetricsRow]'}
    }

    def __init__(self, columns_header=None, deployment_group=None, rows=None):
        super(DeploymentGroupMetrics, self).__init__()
        self.columns_header = columns_header
        self.deployment_group = deployment_group
        self.rows = rows


class DeploymentGroupReference(Model):
    """DeploymentGroupReference.

    :param id: Deployment group identifier.
    :type id: int
    :param name: Name of the deployment group.
    :type name: str
    :param pool: Deployment pool in which deployment agents are registered.
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param project: Project to which the deployment group belongs.
    :type project: :class:`ProjectReference <azure.devops.v5_1.task_agent.models.ProjectReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None):
        super(DeploymentGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project = project


class DeploymentGroupUpdateParameter(Model):
    """DeploymentGroupUpdateParameter.

    :param description: Description of the deployment group.
    :type description: str
    :param name: Name of the deployment group.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(DeploymentGroupUpdateParameter, self).__init__()
        self.description = description
        self.name = name


class DeploymentMachine(Model):
    """DeploymentMachine.

    :param agent: Deployment agent.
    :type agent: :class:`TaskAgent <azure.devops.v5_1.task_agent.models.TaskAgent>`
    :param id: Deployment target Identifier.
    :type id: int
    :param properties: Properties of the deployment target.
    :type properties: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param tags: Tags of the deployment target.
    :type tags: list of str
    """

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgent'},
        'id': {'key': 'id', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, agent=None, id=None, properties=None, tags=None):
        super(DeploymentMachine, self).__init__()
        self.agent = agent
        self.id = id
        self.properties = properties
        self.tags = tags


class DeploymentMachineGroupReference(Model):
    """DeploymentMachineGroupReference.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param pool:
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param project:
    :type project: :class:`ProjectReference <azure.devops.v5_1.task_agent.models.ProjectReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None):
        super(DeploymentMachineGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project = project


class DeploymentPoolSummary(Model):
    """DeploymentPoolSummary.

    :param deployment_groups: List of deployment groups referring to the deployment pool.
    :type deployment_groups: list of :class:`DeploymentGroupReference <azure.devops.v5_1.task_agent.models.DeploymentGroupReference>`
    :param offline_agents_count: Number of deployment agents that are offline.
    :type offline_agents_count: int
    :param online_agents_count: Number of deployment agents that are online.
    :type online_agents_count: int
    :param pool: Deployment pool.
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    """

    _attribute_map = {
        'deployment_groups': {'key': 'deploymentGroups', 'type': '[DeploymentGroupReference]'},
        'offline_agents_count': {'key': 'offlineAgentsCount', 'type': 'int'},
        'online_agents_count': {'key': 'onlineAgentsCount', 'type': 'int'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'}
    }

    def __init__(self, deployment_groups=None, offline_agents_count=None, online_agents_count=None, pool=None):
        super(DeploymentPoolSummary, self).__init__()
        self.deployment_groups = deployment_groups
        self.offline_agents_count = offline_agents_count
        self.online_agents_count = online_agents_count
        self.pool = pool


class DeploymentTargetUpdateParameter(Model):
    """DeploymentTargetUpdateParameter.

    :param id: Identifier of the deployment target.
    :type id: int
    :param tags:
    :type tags: list of str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, id=None, tags=None):
        super(DeploymentTargetUpdateParameter, self).__init__()
        self.id = id
        self.tags = tags


class EndpointAuthorization(Model):
    """EndpointAuthorization.

    :param parameters: Gets or sets the parameters for the selected authorization scheme.
    :type parameters: dict
    :param scheme: Gets or sets the scheme used for service endpoint authentication.
    :type scheme: str
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, parameters=None, scheme=None):
        super(EndpointAuthorization, self).__init__()
        self.parameters = parameters
        self.scheme = scheme


class EndpointUrl(Model):
    """EndpointUrl.

    :param depends_on: Gets or sets the dependency bindings.
    :type depends_on: :class:`DependsOn <azure.devops.v5_1.task_agent.models.DependsOn>`
    :param display_name: Gets or sets the display name of service endpoint url.
    :type display_name: str
    :param help_text: Gets or sets the help text of service endpoint url.
    :type help_text: str
    :param is_visible: Gets or sets the visibility of service endpoint url.
    :type is_visible: str
    :param value: Gets or sets the value of service endpoint url.
    :type value: str
    """

    _attribute_map = {
        'depends_on': {'key': 'dependsOn', 'type': 'DependsOn'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'help_text': {'key': 'helpText', 'type': 'str'},
        'is_visible': {'key': 'isVisible', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, depends_on=None, display_name=None, help_text=None, is_visible=None, value=None):
        super(EndpointUrl, self).__init__()
        self.depends_on = depends_on
        self.display_name = display_name
        self.help_text = help_text
        self.is_visible = is_visible
        self.value = value


class EnvironmentCreateParameter(Model):
    """EnvironmentCreateParameter.

    :param description: Description of the environment.
    :type description: str
    :param name: Name of the environment.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(EnvironmentCreateParameter, self).__init__()
        self.description = description
        self.name = name


class EnvironmentDeploymentExecutionRecord(Model):
    """EnvironmentDeploymentExecutionRecord.

    :param definition: Definition of the environment deployment execution owner
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param environment_id: Id of the Environment
    :type environment_id: int
    :param finish_time: Finish time of the environment deployment execution
    :type finish_time: datetime
    :param id: Id of the Environment deployment execution history record
    :type id: long
    :param owner: Owner of the environment deployment execution record
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param plan_id: Plan Id
    :type plan_id: str
    :param plan_type: Plan type of the environment deployment execution record
    :type plan_type: str
    :param queue_time: Queue time of the environment deployment execution
    :type queue_time: datetime
    :param request_identifier: Request identifier of the Environment deployment execution history record
    :type request_identifier: str
    :param result: Result of the environment deployment execution
    :type result: object
    :param scope_id: Project Id
    :type scope_id: str
    :param service_group_id: Service group Id
    :type service_group_id: int
    :param service_owner: Service owner Id
    :type service_owner: str
    :param start_time: Start time of the environment deployment execution
    :type start_time: datetime
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'environment_id': {'key': 'environmentId', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'request_identifier': {'key': 'requestIdentifier', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'service_group_id': {'key': 'serviceGroupId', 'type': 'int'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'}
    }

    def __init__(self, definition=None, environment_id=None, finish_time=None, id=None, owner=None, plan_id=None, plan_type=None, queue_time=None, request_identifier=None, result=None, scope_id=None, service_group_id=None, service_owner=None, start_time=None):
        super(EnvironmentDeploymentExecutionRecord, self).__init__()
        self.definition = definition
        self.environment_id = environment_id
        self.finish_time = finish_time
        self.id = id
        self.owner = owner
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.queue_time = queue_time
        self.request_identifier = request_identifier
        self.result = result
        self.scope_id = scope_id
        self.service_group_id = service_group_id
        self.service_owner = service_owner
        self.start_time = start_time


class EnvironmentInstance(Model):
    """EnvironmentInstance.

    :param created_by: Identity reference of the user who created the Environment.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on: Creation time of the Environment
    :type created_on: datetime
    :param description: Description of the Environment.
    :type description: str
    :param id: Id of the Environment
    :type id: int
    :param last_modified_by: Identity reference of the user who last modified the Environment.
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param last_modified_on: Last modified time of the Environment
    :type last_modified_on: datetime
    :param name: Name of the Environment.
    :type name: str
    :param service_groups:
    :type service_groups: list of :class:`ServiceGroupReference <azure.devops.v5_1.task_agent.models.ServiceGroupReference>`
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'service_groups': {'key': 'serviceGroups', 'type': '[ServiceGroupReference]'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, last_modified_by=None, last_modified_on=None, name=None, service_groups=None):
        super(EnvironmentInstance, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.name = name
        self.service_groups = service_groups


class EnvironmentReference(Model):
    """EnvironmentReference.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(EnvironmentReference, self).__init__()
        self.id = id
        self.name = name


class EnvironmentUpdateParameter(Model):
    """EnvironmentUpdateParameter.

    :param description: Description of the environment.
    :type description: str
    :param name: Name of the environment.
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(EnvironmentUpdateParameter, self).__init__()
        self.description = description
        self.name = name


class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class HelpLink(Model):
    """HelpLink.

    :param text:
    :type text: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, text=None, url=None):
        super(HelpLink, self).__init__()
        self.text = text
        self.url = url


class IdentityRef(GraphSubjectBase):
    """IdentityRef.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class InputDescriptor(Model):
    """InputDescriptor.

    :param dependency_input_ids: The ids of all inputs that the value of this input is dependent on.
    :type dependency_input_ids: list of str
    :param description: Description of what this input is used for
    :type description: str
    :param group_name: The group localized name to which this input belongs and can be shown as a header for the container that will include all the inputs in the group.
    :type group_name: str
    :param has_dynamic_value_information: If true, the value information for this input is dynamic and should be fetched when the value of dependency inputs change.
    :type has_dynamic_value_information: bool
    :param id: Identifier for the subscription input
    :type id: str
    :param input_mode: Mode in which the value of this input should be entered
    :type input_mode: object
    :param is_confidential: Gets whether this input is confidential, such as for a password or application key
    :type is_confidential: bool
    :param name: Localized name which can be shown as a label for the subscription input
    :type name: str
    :param properties: Custom properties for the input which can be used by the service provider
    :type properties: dict
    :param type: Underlying data type for the input value. When this value is specified, InputMode, Validation and Values are optional.
    :type type: str
    :param use_in_default_description: Gets whether this input is included in the default generated action description.
    :type use_in_default_description: bool
    :param validation: Information to use to validate this input's value
    :type validation: :class:`InputValidation <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValidation>`
    :param value_hint: A hint for input value. It can be used in the UI as the input placeholder.
    :type value_hint: str
    :param values: Information about possible values for this input
    :type values: :class:`InputValues <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValues>`
    """

    _attribute_map = {
        'dependency_input_ids': {'key': 'dependencyInputIds', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'has_dynamic_value_information': {'key': 'hasDynamicValueInformation', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'input_mode': {'key': 'inputMode', 'type': 'object'},
        'is_confidential': {'key': 'isConfidential', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'use_in_default_description': {'key': 'useInDefaultDescription', 'type': 'bool'},
        'validation': {'key': 'validation', 'type': 'InputValidation'},
        'value_hint': {'key': 'valueHint', 'type': 'str'},
        'values': {'key': 'values', 'type': 'InputValues'}
    }

    def __init__(self, dependency_input_ids=None, description=None, group_name=None, has_dynamic_value_information=None, id=None, input_mode=None, is_confidential=None, name=None, properties=None, type=None, use_in_default_description=None, validation=None, value_hint=None, values=None):
        super(InputDescriptor, self).__init__()
        self.dependency_input_ids = dependency_input_ids
        self.description = description
        self.group_name = group_name
        self.has_dynamic_value_information = has_dynamic_value_information
        self.id = id
        self.input_mode = input_mode
        self.is_confidential = is_confidential
        self.name = name
        self.properties = properties
        self.type = type
        self.use_in_default_description = use_in_default_description
        self.validation = validation
        self.value_hint = value_hint
        self.values = values


class InputValidation(Model):
    """InputValidation.

    :param data_type:
    :type data_type: object
    :param is_required:
    :type is_required: bool
    :param max_length:
    :type max_length: int
    :param max_value:
    :type max_value: decimal
    :param min_length:
    :type min_length: int
    :param min_value:
    :type min_value: decimal
    :param pattern:
    :type pattern: str
    :param pattern_mismatch_error_message:
    :type pattern_mismatch_error_message: str
    """

    _attribute_map = {
        'data_type': {'key': 'dataType', 'type': 'object'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'max_length': {'key': 'maxLength', 'type': 'int'},
        'max_value': {'key': 'maxValue', 'type': 'decimal'},
        'min_length': {'key': 'minLength', 'type': 'int'},
        'min_value': {'key': 'minValue', 'type': 'decimal'},
        'pattern': {'key': 'pattern', 'type': 'str'},
        'pattern_mismatch_error_message': {'key': 'patternMismatchErrorMessage', 'type': 'str'}
    }

    def __init__(self, data_type=None, is_required=None, max_length=None, max_value=None, min_length=None, min_value=None, pattern=None, pattern_mismatch_error_message=None):
        super(InputValidation, self).__init__()
        self.data_type = data_type
        self.is_required = is_required
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.pattern = pattern
        self.pattern_mismatch_error_message = pattern_mismatch_error_message


class InputValidationRequest(Model):
    """InputValidationRequest.

    :param inputs:
    :type inputs: dict
    """

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '{ValidationItem}'}
    }

    def __init__(self, inputs=None):
        super(InputValidationRequest, self).__init__()
        self.inputs = inputs


class InputValue(Model):
    """InputValue.

    :param data: Any other data about this input
    :type data: dict
    :param display_value: The text to show for the display of this value
    :type display_value: str
    :param value: The value to store for this input
    :type value: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, data=None, display_value=None, value=None):
        super(InputValue, self).__init__()
        self.data = data
        self.display_value = display_value
        self.value = value


class InputValues(Model):
    """InputValues.

    :param default_value: The default value to use for this input
    :type default_value: str
    :param error: Errors encountered while computing dynamic values.
    :type error: :class:`InputValuesError <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValue>`
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None):
        super(InputValues, self).__init__()
        self.default_value = default_value
        self.error = error
        self.input_id = input_id
        self.is_disabled = is_disabled
        self.is_limited_to_possible_values = is_limited_to_possible_values
        self.is_read_only = is_read_only
        self.possible_values = possible_values


class InputValuesError(Model):
    """InputValuesError.

    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(InputValuesError, self).__init__()
        self.message = message


class KubernetesServiceGroupCreateParameters(Model):
    """KubernetesServiceGroupCreateParameters.

    :param name:
    :type name: str
    :param namespace:
    :type namespace: str
    :param service_endpoint_id:
    :type service_endpoint_id: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'}
    }

    def __init__(self, name=None, namespace=None, service_endpoint_id=None):
        super(KubernetesServiceGroupCreateParameters, self).__init__()
        self.name = name
        self.namespace = namespace
        self.service_endpoint_id = service_endpoint_id


class MarketplacePurchasedLicense(Model):
    """MarketplacePurchasedLicense.

    :param marketplace_name: The Marketplace display name.
    :type marketplace_name: str
    :param purchaser_name: The name of the identity making the purchase as seen by the marketplace
    :type purchaser_name: str
    :param purchase_unit_count: The quantity purchased.
    :type purchase_unit_count: int
    """

    _attribute_map = {
        'marketplace_name': {'key': 'marketplaceName', 'type': 'str'},
        'purchaser_name': {'key': 'purchaserName', 'type': 'str'},
        'purchase_unit_count': {'key': 'purchaseUnitCount', 'type': 'int'}
    }

    def __init__(self, marketplace_name=None, purchaser_name=None, purchase_unit_count=None):
        super(MarketplacePurchasedLicense, self).__init__()
        self.marketplace_name = marketplace_name
        self.purchaser_name = purchaser_name
        self.purchase_unit_count = purchase_unit_count


class MetricsColumnMetaData(Model):
    """MetricsColumnMetaData.

    :param column_name: Name.
    :type column_name: str
    :param column_value_type: Data type.
    :type column_value_type: str
    """

    _attribute_map = {
        'column_name': {'key': 'columnName', 'type': 'str'},
        'column_value_type': {'key': 'columnValueType', 'type': 'str'}
    }

    def __init__(self, column_name=None, column_value_type=None):
        super(MetricsColumnMetaData, self).__init__()
        self.column_name = column_name
        self.column_value_type = column_value_type


class MetricsColumnsHeader(Model):
    """MetricsColumnsHeader.

    :param dimensions: Properties of deployment group for which metrics are provided. E.g. 1: LastJobStatus E.g. 2: TargetState
    :type dimensions: list of :class:`MetricsColumnMetaData <azure.devops.v5_1.task_agent.models.MetricsColumnMetaData>`
    :param metrics: The types of metrics. E.g. 1: total count of deployment targets. E.g. 2: Average time of deployment to the deployment targets.
    :type metrics: list of :class:`MetricsColumnMetaData <azure.devops.v5_1.task_agent.models.MetricsColumnMetaData>`
    """

    _attribute_map = {
        'dimensions': {'key': 'dimensions', 'type': '[MetricsColumnMetaData]'},
        'metrics': {'key': 'metrics', 'type': '[MetricsColumnMetaData]'}
    }

    def __init__(self, dimensions=None, metrics=None):
        super(MetricsColumnsHeader, self).__init__()
        self.dimensions = dimensions
        self.metrics = metrics


class MetricsRow(Model):
    """MetricsRow.

    :param dimensions: The values of the properties mentioned as 'Dimensions' in column header. E.g. 1: For a property 'LastJobStatus' - metrics will be provided for 'passed', 'failed', etc. E.g. 2: For a property 'TargetState' - metrics will be provided for 'online', 'offline' targets.
    :type dimensions: list of str
    :param metrics: Metrics in serialized format. Should be deserialized based on the data type provided in header.
    :type metrics: list of str
    """

    _attribute_map = {
        'dimensions': {'key': 'dimensions', 'type': '[str]'},
        'metrics': {'key': 'metrics', 'type': '[str]'}
    }

    def __init__(self, dimensions=None, metrics=None):
        super(MetricsRow, self).__init__()
        self.dimensions = dimensions
        self.metrics = metrics


class PackageMetadata(Model):
    """PackageMetadata.

    :param created_on: The date the package was created
    :type created_on: datetime
    :param download_url: A direct link to download the package.
    :type download_url: str
    :param filename: The UI uses this to display instructions, i.e. "unzip MyAgent.zip"
    :type filename: str
    :param hash_value: MD5 hash as a base64 string
    :type hash_value: str
    :param info_url: A link to documentation
    :type info_url: str
    :param platform: The platform (win7, linux, etc.)
    :type platform: str
    :param type: The type of package (e.g. "agent")
    :type type: str
    :param version: The package version.
    :type version: :class:`PackageVersion <azure.devops.v5_1.task_agent.models.PackageVersion>`
    """

    _attribute_map = {
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'download_url': {'key': 'downloadUrl', 'type': 'str'},
        'filename': {'key': 'filename', 'type': 'str'},
        'hash_value': {'key': 'hashValue', 'type': 'str'},
        'info_url': {'key': 'infoUrl', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'version': {'key': 'version', 'type': 'PackageVersion'}
    }

    def __init__(self, created_on=None, download_url=None, filename=None, hash_value=None, info_url=None, platform=None, type=None, version=None):
        super(PackageMetadata, self).__init__()
        self.created_on = created_on
        self.download_url = download_url
        self.filename = filename
        self.hash_value = hash_value
        self.info_url = info_url
        self.platform = platform
        self.type = type
        self.version = version


class PackageVersion(Model):
    """PackageVersion.

    :param major:
    :type major: int
    :param minor:
    :type minor: int
    :param patch:
    :type patch: int
    """

    _attribute_map = {
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, major=None, minor=None, patch=None):
        super(PackageVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.patch = patch


class ProjectReference(Model):
    """ProjectReference.

    :param id:
    :type id: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class PublishTaskGroupMetadata(Model):
    """PublishTaskGroupMetadata.

    :param comment:
    :type comment: str
    :param parent_definition_revision:
    :type parent_definition_revision: int
    :param preview:
    :type preview: bool
    :param task_group_id:
    :type task_group_id: str
    :param task_group_revision:
    :type task_group_revision: int
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parent_definition_revision': {'key': 'parentDefinitionRevision', 'type': 'int'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'task_group_id': {'key': 'taskGroupId', 'type': 'str'},
        'task_group_revision': {'key': 'taskGroupRevision', 'type': 'int'}
    }

    def __init__(self, comment=None, parent_definition_revision=None, preview=None, task_group_id=None, task_group_revision=None):
        super(PublishTaskGroupMetadata, self).__init__()
        self.comment = comment
        self.parent_definition_revision = parent_definition_revision
        self.preview = preview
        self.task_group_id = task_group_id
        self.task_group_revision = task_group_revision


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceLimit(Model):
    """ResourceLimit.

    :param failed_to_reach_all_providers:
    :type failed_to_reach_all_providers: bool
    :param host_id:
    :type host_id: str
    :param is_hosted:
    :type is_hosted: bool
    :param is_premium:
    :type is_premium: bool
    :param parallelism_tag:
    :type parallelism_tag: str
    :param resource_limits_data:
    :type resource_limits_data: dict
    :param total_count:
    :type total_count: int
    :param total_minutes:
    :type total_minutes: int
    """

    _attribute_map = {
        'failed_to_reach_all_providers': {'key': 'failedToReachAllProviders', 'type': 'bool'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'is_premium': {'key': 'isPremium', 'type': 'bool'},
        'parallelism_tag': {'key': 'parallelismTag', 'type': 'str'},
        'resource_limits_data': {'key': 'resourceLimitsData', 'type': '{str}'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'total_minutes': {'key': 'totalMinutes', 'type': 'int'}
    }

    def __init__(self, failed_to_reach_all_providers=None, host_id=None, is_hosted=None, is_premium=None, parallelism_tag=None, resource_limits_data=None, total_count=None, total_minutes=None):
        super(ResourceLimit, self).__init__()
        self.failed_to_reach_all_providers = failed_to_reach_all_providers
        self.host_id = host_id
        self.is_hosted = is_hosted
        self.is_premium = is_premium
        self.parallelism_tag = parallelism_tag
        self.resource_limits_data = resource_limits_data
        self.total_count = total_count
        self.total_minutes = total_minutes


class ResourceUsage(Model):
    """ResourceUsage.

    :param resource_limit:
    :type resource_limit: :class:`ResourceLimit <azure.devops.v5_1.task_agent.models.ResourceLimit>`
    :param running_requests:
    :type running_requests: list of :class:`TaskAgentJobRequest <azure.devops.v5_1.task_agent.models.TaskAgentJobRequest>`
    :param used_count:
    :type used_count: int
    :param used_minutes:
    :type used_minutes: int
    """

    _attribute_map = {
        'resource_limit': {'key': 'resourceLimit', 'type': 'ResourceLimit'},
        'running_requests': {'key': 'runningRequests', 'type': '[TaskAgentJobRequest]'},
        'used_count': {'key': 'usedCount', 'type': 'int'},
        'used_minutes': {'key': 'usedMinutes', 'type': 'int'}
    }

    def __init__(self, resource_limit=None, running_requests=None, used_count=None, used_minutes=None):
        super(ResourceUsage, self).__init__()
        self.resource_limit = resource_limit
        self.running_requests = running_requests
        self.used_count = used_count
        self.used_minutes = used_minutes


class ResultTransformationDetails(Model):
    """ResultTransformationDetails.

    :param result_template:
    :type result_template: str
    """

    _attribute_map = {
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, result_template=None):
        super(ResultTransformationDetails, self).__init__()
        self.result_template = result_template


class SecureFile(Model):
    """SecureFile.

    :param created_by:
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on:
    :type created_on: datetime
    :param id:
    :type id: str
    :param modified_by:
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param modified_on:
    :type modified_on: datetime
    :param name:
    :type name: str
    :param properties:
    :type properties: dict
    :param ticket:
    :type ticket: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'ticket': {'key': 'ticket', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, id=None, modified_by=None, modified_on=None, name=None, properties=None, ticket=None):
        super(SecureFile, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.id = id
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.properties = properties
        self.ticket = ticket


class ServiceEndpoint(Model):
    """ServiceEndpoint.

    :param administrators_group: Gets or sets the identity reference for the administrators group of the service endpoint.
    :type administrators_group: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param authorization: Gets or sets the authorization data for talking to the endpoint.
    :type authorization: :class:`EndpointAuthorization <azure.devops.v5_1.task_agent.models.EndpointAuthorization>`
    :param created_by: Gets or sets the identity reference for the user who created the Service endpoint.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param data:
    :type data: dict
    :param description: Gets or sets the description of endpoint.
    :type description: str
    :param group_scope_id:
    :type group_scope_id: str
    :param id: Gets or sets the identifier of this endpoint.
    :type id: str
    :param is_ready: EndPoint state indictor
    :type is_ready: bool
    :param is_shared: Indicates whether service endpoint is shared with other projects or not.
    :type is_shared: bool
    :param name: Gets or sets the friendly name of the endpoint.
    :type name: str
    :param operation_status: Error message during creation/deletion of endpoint
    :type operation_status: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param readers_group: Gets or sets the identity reference for the readers group of the service endpoint.
    :type readers_group: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param type: Gets or sets the type of the endpoint.
    :type type: str
    :param url: Gets or sets the url of the endpoint.
    :type url: str
    """

    _attribute_map = {
        'administrators_group': {'key': 'administratorsGroup', 'type': 'IdentityRef'},
        'authorization': {'key': 'authorization', 'type': 'EndpointAuthorization'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'data': {'key': 'data', 'type': '{str}'},
        'description': {'key': 'description', 'type': 'str'},
        'group_scope_id': {'key': 'groupScopeId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_ready': {'key': 'isReady', 'type': 'bool'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'readers_group': {'key': 'readersGroup', 'type': 'IdentityRef'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, administrators_group=None, authorization=None, created_by=None, data=None, description=None, group_scope_id=None, id=None, is_ready=None, is_shared=None, name=None, operation_status=None, readers_group=None, type=None, url=None):
        super(ServiceEndpoint, self).__init__()
        self.administrators_group = administrators_group
        self.authorization = authorization
        self.created_by = created_by
        self.data = data
        self.description = description
        self.group_scope_id = group_scope_id
        self.id = id
        self.is_ready = is_ready
        self.is_shared = is_shared
        self.name = name
        self.operation_status = operation_status
        self.readers_group = readers_group
        self.type = type
        self.url = url


class ServiceEndpointAuthenticationScheme(Model):
    """ServiceEndpointAuthenticationScheme.

    :param authorization_headers: Gets or sets the authorization headers of service endpoint authentication scheme.
    :type authorization_headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.task_agent.models.AuthorizationHeader>`
    :param client_certificates: Gets or sets the certificates of service endpoint authentication scheme.
    :type client_certificates: list of :class:`ClientCertificate <azure.devops.v5_1.task_agent.models.ClientCertificate>`
    :param display_name: Gets or sets the display name for the service endpoint authentication scheme.
    :type display_name: str
    :param input_descriptors: Gets or sets the input descriptors for the service endpoint authentication scheme.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.task_agent.models.InputDescriptor>`
    :param scheme: Gets or sets the scheme for service endpoint authentication.
    :type scheme: str
    """

    _attribute_map = {
        'authorization_headers': {'key': 'authorizationHeaders', 'type': '[AuthorizationHeader]'},
        'client_certificates': {'key': 'clientCertificates', 'type': '[ClientCertificate]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, authorization_headers=None, client_certificates=None, display_name=None, input_descriptors=None, scheme=None):
        super(ServiceEndpointAuthenticationScheme, self).__init__()
        self.authorization_headers = authorization_headers
        self.client_certificates = client_certificates
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.scheme = scheme


class ServiceEndpointDetails(Model):
    """ServiceEndpointDetails.

    :param authorization:
    :type authorization: :class:`EndpointAuthorization <azure.devops.v5_1.task_agent.models.EndpointAuthorization>`
    :param data:
    :type data: dict
    :param type:
    :type type: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'authorization': {'key': 'authorization', 'type': 'EndpointAuthorization'},
        'data': {'key': 'data', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, authorization=None, data=None, type=None, url=None):
        super(ServiceEndpointDetails, self).__init__()
        self.authorization = authorization
        self.data = data
        self.type = type
        self.url = url


class ServiceEndpointExecutionData(Model):
    """ServiceEndpointExecutionData.

    :param definition: Gets the definition of service endpoint execution owner.
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param finish_time: Gets the finish time of service endpoint execution.
    :type finish_time: datetime
    :param id: Gets the Id of service endpoint execution data.
    :type id: long
    :param owner: Gets the owner of service endpoint execution data.
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param plan_type: Gets the plan type of service endpoint execution data.
    :type plan_type: str
    :param result: Gets the result of service endpoint execution.
    :type result: object
    :param start_time: Gets the start time of service endpoint execution.
    :type start_time: datetime
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'}
    }

    def __init__(self, definition=None, finish_time=None, id=None, owner=None, plan_type=None, result=None, start_time=None):
        super(ServiceEndpointExecutionData, self).__init__()
        self.definition = definition
        self.finish_time = finish_time
        self.id = id
        self.owner = owner
        self.plan_type = plan_type
        self.result = result
        self.start_time = start_time


class ServiceEndpointExecutionRecord(Model):
    """ServiceEndpointExecutionRecord.

    :param data: Gets the execution data of service endpoint execution.
    :type data: :class:`ServiceEndpointExecutionData <azure.devops.v5_1.task_agent.models.ServiceEndpointExecutionData>`
    :param endpoint_id: Gets the Id of service endpoint.
    :type endpoint_id: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'ServiceEndpointExecutionData'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'}
    }

    def __init__(self, data=None, endpoint_id=None):
        super(ServiceEndpointExecutionRecord, self).__init__()
        self.data = data
        self.endpoint_id = endpoint_id


class ServiceEndpointExecutionRecordsInput(Model):
    """ServiceEndpointExecutionRecordsInput.

    :param data:
    :type data: :class:`ServiceEndpointExecutionData <azure.devops.v5_1.task_agent.models.ServiceEndpointExecutionData>`
    :param endpoint_ids:
    :type endpoint_ids: list of str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'ServiceEndpointExecutionData'},
        'endpoint_ids': {'key': 'endpointIds', 'type': '[str]'}
    }

    def __init__(self, data=None, endpoint_ids=None):
        super(ServiceEndpointExecutionRecordsInput, self).__init__()
        self.data = data
        self.endpoint_ids = endpoint_ids


class ServiceEndpointRequest(Model):
    """ServiceEndpointRequest.

    :param data_source_details:
    :type data_source_details: :class:`DataSourceDetails <azure.devops.v5_1.task_agent.models.DataSourceDetails>`
    :param result_transformation_details:
    :type result_transformation_details: :class:`ResultTransformationDetails <azure.devops.v5_1.task_agent.models.ResultTransformationDetails>`
    :param service_endpoint_details:
    :type service_endpoint_details: :class:`ServiceEndpointDetails <azure.devops.v5_1.task_agent.models.ServiceEndpointDetails>`
    """

    _attribute_map = {
        'data_source_details': {'key': 'dataSourceDetails', 'type': 'DataSourceDetails'},
        'result_transformation_details': {'key': 'resultTransformationDetails', 'type': 'ResultTransformationDetails'},
        'service_endpoint_details': {'key': 'serviceEndpointDetails', 'type': 'ServiceEndpointDetails'}
    }

    def __init__(self, data_source_details=None, result_transformation_details=None, service_endpoint_details=None):
        super(ServiceEndpointRequest, self).__init__()
        self.data_source_details = data_source_details
        self.result_transformation_details = result_transformation_details
        self.service_endpoint_details = service_endpoint_details


class ServiceEndpointRequestResult(Model):
    """ServiceEndpointRequestResult.

    :param error_message:
    :type error_message: str
    :param result:
    :type result: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param status_code:
    :type status_code: object
    """

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'status_code': {'key': 'statusCode', 'type': 'object'}
    }

    def __init__(self, error_message=None, result=None, status_code=None):
        super(ServiceEndpointRequestResult, self).__init__()
        self.error_message = error_message
        self.result = result
        self.status_code = status_code


class ServiceEndpointType(Model):
    """ServiceEndpointType.

    :param authentication_schemes: Authentication scheme of service endpoint type.
    :type authentication_schemes: list of :class:`ServiceEndpointAuthenticationScheme <azure.devops.v5_1.task_agent.models.ServiceEndpointAuthenticationScheme>`
    :param data_sources: Data sources of service endpoint type.
    :type data_sources: list of :class:`DataSource <azure.devops.v5_1.task_agent.models.DataSource>`
    :param dependency_data: Dependency data of service endpoint type.
    :type dependency_data: list of :class:`DependencyData <azure.devops.v5_1.task_agent.models.DependencyData>`
    :param description: Gets or sets the description of service endpoint type.
    :type description: str
    :param display_name: Gets or sets the display name of service endpoint type.
    :type display_name: str
    :param endpoint_url: Gets or sets the endpoint url of service endpoint type.
    :type endpoint_url: :class:`EndpointUrl <azure.devops.v5_1.task_agent.models.EndpointUrl>`
    :param help_link: Gets or sets the help link of service endpoint type.
    :type help_link: :class:`HelpLink <azure.devops.v5_1.task_agent.models.HelpLink>`
    :param help_mark_down:
    :type help_mark_down: str
    :param icon_url: Gets or sets the icon url of service endpoint type.
    :type icon_url: str
    :param input_descriptors: Input descriptor of service endpoint type.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.task_agent.models.InputDescriptor>`
    :param name: Gets or sets the name of service endpoint type.
    :type name: str
    :param trusted_hosts: Trusted hosts of a service endpoint type.
    :type trusted_hosts: list of str
    :param ui_contribution_id: Gets or sets the ui contribution id of service endpoint type.
    :type ui_contribution_id: str
    """

    _attribute_map = {
        'authentication_schemes': {'key': 'authenticationSchemes', 'type': '[ServiceEndpointAuthenticationScheme]'},
        'data_sources': {'key': 'dataSources', 'type': '[DataSource]'},
        'dependency_data': {'key': 'dependencyData', 'type': '[DependencyData]'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'EndpointUrl'},
        'help_link': {'key': 'helpLink', 'type': 'HelpLink'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'trusted_hosts': {'key': 'trustedHosts', 'type': '[str]'},
        'ui_contribution_id': {'key': 'uiContributionId', 'type': 'str'}
    }

    def __init__(self, authentication_schemes=None, data_sources=None, dependency_data=None, description=None, display_name=None, endpoint_url=None, help_link=None, help_mark_down=None, icon_url=None, input_descriptors=None, name=None, trusted_hosts=None, ui_contribution_id=None):
        super(ServiceEndpointType, self).__init__()
        self.authentication_schemes = authentication_schemes
        self.data_sources = data_sources
        self.dependency_data = dependency_data
        self.description = description
        self.display_name = display_name
        self.endpoint_url = endpoint_url
        self.help_link = help_link
        self.help_mark_down = help_mark_down
        self.icon_url = icon_url
        self.input_descriptors = input_descriptors
        self.name = name
        self.trusted_hosts = trusted_hosts
        self.ui_contribution_id = ui_contribution_id


class ServiceGroup(Model):
    """ServiceGroup.

    :param created_by:
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on:
    :type created_on: datetime
    :param environment_reference:
    :type environment_reference: :class:`EnvironmentReference <azure.devops.v5_1.task_agent.models.EnvironmentReference>`
    :param id:
    :type id: int
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param last_modified_on:
    :type last_modified_on: datetime
    :param name:
    :type name: str
    :param type:
    :type type: object
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'environment_reference': {'key': 'environmentReference', 'type': 'EnvironmentReference'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_on=None, environment_reference=None, id=None, last_modified_by=None, last_modified_on=None, name=None, type=None):
        super(ServiceGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.environment_reference = environment_reference
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.name = name
        self.type = type


class ServiceGroupReference(Model):
    """ServiceGroupReference.

    :param id: Id of the Service Group.
    :type id: int
    :param name: Name of the service group.
    :type name: str
    :param type: Type of the service group.
    :type type: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(ServiceGroupReference, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class TaskAgentAuthorization(Model):
    """TaskAgentAuthorization.

    :param authorization_url: Gets or sets the endpoint used to obtain access tokens from the configured token service.
    :type authorization_url: str
    :param client_id: Gets or sets the client identifier for this agent.
    :type client_id: str
    :param public_key: Gets or sets the public key used to verify the identity of this agent.
    :type public_key: :class:`TaskAgentPublicKey <azure.devops.v5_1.task_agent.models.TaskAgentPublicKey>`
    """

    _attribute_map = {
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'public_key': {'key': 'publicKey', 'type': 'TaskAgentPublicKey'}
    }

    def __init__(self, authorization_url=None, client_id=None, public_key=None):
        super(TaskAgentAuthorization, self).__init__()
        self.authorization_url = authorization_url
        self.client_id = client_id
        self.public_key = public_key


class TaskAgentCloud(Model):
    """TaskAgentCloud.

    :param acquire_agent_endpoint: Gets or sets a AcquireAgentEndpoint using which a request can be made to acquire new agent
    :type acquire_agent_endpoint: str
    :param acquisition_timeout:
    :type acquisition_timeout: int
    :param agent_cloud_id:
    :type agent_cloud_id: int
    :param get_agent_definition_endpoint:
    :type get_agent_definition_endpoint: str
    :param get_agent_request_status_endpoint:
    :type get_agent_request_status_endpoint: str
    :param internal: Signifies that this Agent Cloud is internal and should not be user-manageable
    :type internal: bool
    :param name:
    :type name: str
    :param release_agent_endpoint:
    :type release_agent_endpoint: str
    :param shared_secret:
    :type shared_secret: str
    :param type: Gets or sets the type of the endpoint.
    :type type: str
    """

    _attribute_map = {
        'acquire_agent_endpoint': {'key': 'acquireAgentEndpoint', 'type': 'str'},
        'acquisition_timeout': {'key': 'acquisitionTimeout', 'type': 'int'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'get_agent_definition_endpoint': {'key': 'getAgentDefinitionEndpoint', 'type': 'str'},
        'get_agent_request_status_endpoint': {'key': 'getAgentRequestStatusEndpoint', 'type': 'str'},
        'internal': {'key': 'internal', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'release_agent_endpoint': {'key': 'releaseAgentEndpoint', 'type': 'str'},
        'shared_secret': {'key': 'sharedSecret', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, acquire_agent_endpoint=None, acquisition_timeout=None, agent_cloud_id=None, get_agent_definition_endpoint=None, get_agent_request_status_endpoint=None, internal=None, name=None, release_agent_endpoint=None, shared_secret=None, type=None):
        super(TaskAgentCloud, self).__init__()
        self.acquire_agent_endpoint = acquire_agent_endpoint
        self.acquisition_timeout = acquisition_timeout
        self.agent_cloud_id = agent_cloud_id
        self.get_agent_definition_endpoint = get_agent_definition_endpoint
        self.get_agent_request_status_endpoint = get_agent_request_status_endpoint
        self.internal = internal
        self.name = name
        self.release_agent_endpoint = release_agent_endpoint
        self.shared_secret = shared_secret
        self.type = type


class TaskAgentCloudRequest(Model):
    """TaskAgentCloudRequest.

    :param agent:
    :type agent: :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    :param agent_cloud_id:
    :type agent_cloud_id: int
    :param agent_connected_time:
    :type agent_connected_time: datetime
    :param agent_data:
    :type agent_data: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param agent_specification:
    :type agent_specification: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param pool:
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param provisioned_time:
    :type provisioned_time: datetime
    :param provision_request_time:
    :type provision_request_time: datetime
    :param release_request_time:
    :type release_request_time: datetime
    :param request_id:
    :type request_id: str
    """

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'agent_connected_time': {'key': 'agentConnectedTime', 'type': 'iso-8601'},
        'agent_data': {'key': 'agentData', 'type': 'object'},
        'agent_specification': {'key': 'agentSpecification', 'type': 'object'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'provisioned_time': {'key': 'provisionedTime', 'type': 'iso-8601'},
        'provision_request_time': {'key': 'provisionRequestTime', 'type': 'iso-8601'},
        'release_request_time': {'key': 'releaseRequestTime', 'type': 'iso-8601'},
        'request_id': {'key': 'requestId', 'type': 'str'}
    }

    def __init__(self, agent=None, agent_cloud_id=None, agent_connected_time=None, agent_data=None, agent_specification=None, pool=None, provisioned_time=None, provision_request_time=None, release_request_time=None, request_id=None):
        super(TaskAgentCloudRequest, self).__init__()
        self.agent = agent
        self.agent_cloud_id = agent_cloud_id
        self.agent_connected_time = agent_connected_time
        self.agent_data = agent_data
        self.agent_specification = agent_specification
        self.pool = pool
        self.provisioned_time = provisioned_time
        self.provision_request_time = provision_request_time
        self.release_request_time = release_request_time
        self.request_id = request_id


class TaskAgentCloudType(Model):
    """TaskAgentCloudType.

    :param display_name: Gets or sets the display name of agnet cloud type.
    :type display_name: str
    :param input_descriptors: Gets or sets the input descriptors
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.task_agent.models.InputDescriptor>`
    :param name: Gets or sets the name of agent cloud type.
    :type name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, display_name=None, input_descriptors=None, name=None):
        super(TaskAgentCloudType, self).__init__()
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.name = name


class TaskAgentDelaySource(Model):
    """TaskAgentDelaySource.

    :param delays:
    :type delays: list of object
    :param task_agent:
    :type task_agent: :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    """

    _attribute_map = {
        'delays': {'key': 'delays', 'type': '[object]'},
        'task_agent': {'key': 'taskAgent', 'type': 'TaskAgentReference'}
    }

    def __init__(self, delays=None, task_agent=None):
        super(TaskAgentDelaySource, self).__init__()
        self.delays = delays
        self.task_agent = task_agent


class TaskAgentJobRequest(Model):
    """TaskAgentJobRequest.

    :param agent_delays:
    :type agent_delays: list of :class:`TaskAgentDelaySource <azure.devops.v5_1.task_agent.models.TaskAgentDelaySource>`
    :param agent_specification:
    :type agent_specification: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param assign_time:
    :type assign_time: datetime
    :param data:
    :type data: dict
    :param definition:
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param demands:
    :type demands: list of :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param expected_duration:
    :type expected_duration: object
    :param finish_time:
    :type finish_time: datetime
    :param host_id:
    :type host_id: str
    :param job_id:
    :type job_id: str
    :param job_name:
    :type job_name: str
    :param locked_until:
    :type locked_until: datetime
    :param matched_agents:
    :type matched_agents: list of :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    :param matches_all_agents_in_pool:
    :type matches_all_agents_in_pool: bool
    :param orchestration_id:
    :type orchestration_id: str
    :param owner:
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v5_1.task_agent.models.TaskOrchestrationOwner>`
    :param plan_group:
    :type plan_group: str
    :param plan_id:
    :type plan_id: str
    :param plan_type:
    :type plan_type: str
    :param pool_id:
    :type pool_id: int
    :param queue_id:
    :type queue_id: int
    :param queue_time:
    :type queue_time: datetime
    :param receive_time:
    :type receive_time: datetime
    :param request_id:
    :type request_id: long
    :param reserved_agent:
    :type reserved_agent: :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    :param result:
    :type result: object
    :param scope_id:
    :type scope_id: str
    :param service_owner:
    :type service_owner: str
    :param status_message:
    :type status_message: str
    """

    _attribute_map = {
        'agent_delays': {'key': 'agentDelays', 'type': '[TaskAgentDelaySource]'},
        'agent_specification': {'key': 'agentSpecification', 'type': 'object'},
        'assign_time': {'key': 'assignTime', 'type': 'iso-8601'},
        'data': {'key': 'data', 'type': '{str}'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'expected_duration': {'key': 'expectedDuration', 'type': 'object'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'job_name': {'key': 'jobName', 'type': 'str'},
        'locked_until': {'key': 'lockedUntil', 'type': 'iso-8601'},
        'matched_agents': {'key': 'matchedAgents', 'type': '[TaskAgentReference]'},
        'matches_all_agents_in_pool': {'key': 'matchesAllAgentsInPool', 'type': 'bool'},
        'orchestration_id': {'key': 'orchestrationId', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'receive_time': {'key': 'receiveTime', 'type': 'iso-8601'},
        'request_id': {'key': 'requestId', 'type': 'long'},
        'reserved_agent': {'key': 'reservedAgent', 'type': 'TaskAgentReference'},
        'result': {'key': 'result', 'type': 'object'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'service_owner': {'key': 'serviceOwner', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'str'}
    }

    def __init__(self, agent_delays=None, agent_specification=None, assign_time=None, data=None, definition=None, demands=None, expected_duration=None, finish_time=None, host_id=None, job_id=None, job_name=None, locked_until=None, matched_agents=None, matches_all_agents_in_pool=None, orchestration_id=None, owner=None, plan_group=None, plan_id=None, plan_type=None, pool_id=None, queue_id=None, queue_time=None, receive_time=None, request_id=None, reserved_agent=None, result=None, scope_id=None, service_owner=None, status_message=None):
        super(TaskAgentJobRequest, self).__init__()
        self.agent_delays = agent_delays
        self.agent_specification = agent_specification
        self.assign_time = assign_time
        self.data = data
        self.definition = definition
        self.demands = demands
        self.expected_duration = expected_duration
        self.finish_time = finish_time
        self.host_id = host_id
        self.job_id = job_id
        self.job_name = job_name
        self.locked_until = locked_until
        self.matched_agents = matched_agents
        self.matches_all_agents_in_pool = matches_all_agents_in_pool
        self.orchestration_id = orchestration_id
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.pool_id = pool_id
        self.queue_id = queue_id
        self.queue_time = queue_time
        self.receive_time = receive_time
        self.request_id = request_id
        self.reserved_agent = reserved_agent
        self.result = result
        self.scope_id = scope_id
        self.service_owner = service_owner
        self.status_message = status_message


class TaskAgentMessage(Model):
    """TaskAgentMessage.

    :param body: Gets or sets the body of the message. If the <c>IV</c> property is provided the body will need to be decrypted using the <c>TaskAgentSession.EncryptionKey</c> value in addition to the <c>IV</c>.
    :type body: str
    :param iV: Gets or sets the intialization vector used to encrypt this message.
    :type iV: str
    :param message_id: Gets or sets the message identifier.
    :type message_id: long
    :param message_type: Gets or sets the message type, describing the data contract found in <c>TaskAgentMessage.Body</c>.
    :type message_type: str
    """

    _attribute_map = {
        'body': {'key': 'body', 'type': 'str'},
        'iV': {'key': 'iV', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'long'},
        'message_type': {'key': 'messageType', 'type': 'str'}
    }

    def __init__(self, body=None, iV=None, message_id=None, message_type=None):
        super(TaskAgentMessage, self).__init__()
        self.body = body
        self.iV = iV
        self.message_id = message_id
        self.message_type = message_type


class TaskAgentPoolMaintenanceDefinition(Model):
    """TaskAgentPoolMaintenanceDefinition.

    :param enabled: Enable maintenance
    :type enabled: bool
    :param id: Id
    :type id: int
    :param job_timeout_in_minutes: Maintenance job timeout per agent
    :type job_timeout_in_minutes: int
    :param max_concurrent_agents_percentage: Max percentage of agents within a pool running maintenance job at given time
    :type max_concurrent_agents_percentage: int
    :param options:
    :type options: :class:`TaskAgentPoolMaintenanceOptions <azure.devops.v5_1.task_agent.models.TaskAgentPoolMaintenanceOptions>`
    :param pool: Pool reference for the maintenance definition
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param retention_policy:
    :type retention_policy: :class:`TaskAgentPoolMaintenanceRetentionPolicy <azure.devops.v5_1.task_agent.models.TaskAgentPoolMaintenanceRetentionPolicy>`
    :param schedule_setting:
    :type schedule_setting: :class:`TaskAgentPoolMaintenanceSchedule <azure.devops.v5_1.task_agent.models.TaskAgentPoolMaintenanceSchedule>`
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'job_timeout_in_minutes': {'key': 'jobTimeoutInMinutes', 'type': 'int'},
        'max_concurrent_agents_percentage': {'key': 'maxConcurrentAgentsPercentage', 'type': 'int'},
        'options': {'key': 'options', 'type': 'TaskAgentPoolMaintenanceOptions'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'TaskAgentPoolMaintenanceRetentionPolicy'},
        'schedule_setting': {'key': 'scheduleSetting', 'type': 'TaskAgentPoolMaintenanceSchedule'}
    }

    def __init__(self, enabled=None, id=None, job_timeout_in_minutes=None, max_concurrent_agents_percentage=None, options=None, pool=None, retention_policy=None, schedule_setting=None):
        super(TaskAgentPoolMaintenanceDefinition, self).__init__()
        self.enabled = enabled
        self.id = id
        self.job_timeout_in_minutes = job_timeout_in_minutes
        self.max_concurrent_agents_percentage = max_concurrent_agents_percentage
        self.options = options
        self.pool = pool
        self.retention_policy = retention_policy
        self.schedule_setting = schedule_setting


class TaskAgentPoolMaintenanceJob(Model):
    """TaskAgentPoolMaintenanceJob.

    :param definition_id: The maintenance definition for the maintenance job
    :type definition_id: int
    :param error_count: The total error counts during the maintenance job
    :type error_count: int
    :param finish_time: Time that the maintenance job was completed
    :type finish_time: datetime
    :param job_id: Id of the maintenance job
    :type job_id: int
    :param logs_download_url: The log download url for the maintenance job
    :type logs_download_url: str
    :param orchestration_id: Orchestration/Plan Id for the maintenance job
    :type orchestration_id: str
    :param pool: Pool reference for the maintenance job
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param queue_time: Time that the maintenance job was queued
    :type queue_time: datetime
    :param requested_by: The identity that queued the maintenance job
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param result: The maintenance job result
    :type result: object
    :param start_time: Time that the maintenance job was started
    :type start_time: datetime
    :param status: Status of the maintenance job
    :type status: object
    :param target_agents:
    :type target_agents: list of :class:`TaskAgentPoolMaintenanceJobTargetAgent <azure.devops.v5_1.task_agent.models.TaskAgentPoolMaintenanceJobTargetAgent>`
    :param warning_count: The total warning counts during the maintenance job
    :type warning_count: int
    """

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'job_id': {'key': 'jobId', 'type': 'int'},
        'logs_download_url': {'key': 'logsDownloadUrl', 'type': 'str'},
        'orchestration_id': {'key': 'orchestrationId', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'result': {'key': 'result', 'type': 'object'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'target_agents': {'key': 'targetAgents', 'type': '[TaskAgentPoolMaintenanceJobTargetAgent]'},
        'warning_count': {'key': 'warningCount', 'type': 'int'}
    }

    def __init__(self, definition_id=None, error_count=None, finish_time=None, job_id=None, logs_download_url=None, orchestration_id=None, pool=None, queue_time=None, requested_by=None, result=None, start_time=None, status=None, target_agents=None, warning_count=None):
        super(TaskAgentPoolMaintenanceJob, self).__init__()
        self.definition_id = definition_id
        self.error_count = error_count
        self.finish_time = finish_time
        self.job_id = job_id
        self.logs_download_url = logs_download_url
        self.orchestration_id = orchestration_id
        self.pool = pool
        self.queue_time = queue_time
        self.requested_by = requested_by
        self.result = result
        self.start_time = start_time
        self.status = status
        self.target_agents = target_agents
        self.warning_count = warning_count


class TaskAgentPoolMaintenanceJobTargetAgent(Model):
    """TaskAgentPoolMaintenanceJobTargetAgent.

    :param agent:
    :type agent: :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    :param job_id:
    :type job_id: int
    :param result:
    :type result: object
    :param status:
    :type status: object
    """

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'job_id': {'key': 'jobId', 'type': 'int'},
        'result': {'key': 'result', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, agent=None, job_id=None, result=None, status=None):
        super(TaskAgentPoolMaintenanceJobTargetAgent, self).__init__()
        self.agent = agent
        self.job_id = job_id
        self.result = result
        self.status = status


class TaskAgentPoolMaintenanceOptions(Model):
    """TaskAgentPoolMaintenanceOptions.

    :param working_directory_expiration_in_days: time to consider a System.DefaultWorkingDirectory is stale
    :type working_directory_expiration_in_days: int
    """

    _attribute_map = {
        'working_directory_expiration_in_days': {'key': 'workingDirectoryExpirationInDays', 'type': 'int'}
    }

    def __init__(self, working_directory_expiration_in_days=None):
        super(TaskAgentPoolMaintenanceOptions, self).__init__()
        self.working_directory_expiration_in_days = working_directory_expiration_in_days


class TaskAgentPoolMaintenanceRetentionPolicy(Model):
    """TaskAgentPoolMaintenanceRetentionPolicy.

    :param number_of_history_records_to_keep: Number of records to keep for maintenance job executed with this definition.
    :type number_of_history_records_to_keep: int
    """

    _attribute_map = {
        'number_of_history_records_to_keep': {'key': 'numberOfHistoryRecordsToKeep', 'type': 'int'}
    }

    def __init__(self, number_of_history_records_to_keep=None):
        super(TaskAgentPoolMaintenanceRetentionPolicy, self).__init__()
        self.number_of_history_records_to_keep = number_of_history_records_to_keep


class TaskAgentPoolMaintenanceSchedule(Model):
    """TaskAgentPoolMaintenanceSchedule.

    :param days_to_build: Days for a build (flags enum for days of the week)
    :type days_to_build: object
    :param schedule_job_id: The Job Id of the Scheduled job that will queue the pool maintenance job.
    :type schedule_job_id: str
    :param start_hours: Local timezone hour to start
    :type start_hours: int
    :param start_minutes: Local timezone minute to start
    :type start_minutes: int
    :param time_zone_id: Time zone of the build schedule (string representation of the time zone id)
    :type time_zone_id: str
    """

    _attribute_map = {
        'days_to_build': {'key': 'daysToBuild', 'type': 'object'},
        'schedule_job_id': {'key': 'scheduleJobId', 'type': 'str'},
        'start_hours': {'key': 'startHours', 'type': 'int'},
        'start_minutes': {'key': 'startMinutes', 'type': 'int'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'str'}
    }

    def __init__(self, days_to_build=None, schedule_job_id=None, start_hours=None, start_minutes=None, time_zone_id=None):
        super(TaskAgentPoolMaintenanceSchedule, self).__init__()
        self.days_to_build = days_to_build
        self.schedule_job_id = schedule_job_id
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.time_zone_id = time_zone_id


class TaskAgentPoolReference(Model):
    """TaskAgentPoolReference.

    :param id:
    :type id: int
    :param is_hosted: Gets or sets a value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param name:
    :type name: str
    :param pool_type: Gets or sets the type of the pool
    :type pool_type: object
    :param scope:
    :type scope: str
    :param size: Gets the current size of the pool.
    :type size: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'}
    }

    def __init__(self, id=None, is_hosted=None, name=None, pool_type=None, scope=None, size=None):
        super(TaskAgentPoolReference, self).__init__()
        self.id = id
        self.is_hosted = is_hosted
        self.name = name
        self.pool_type = pool_type
        self.scope = scope
        self.size = size


class TaskAgentPublicKey(Model):
    """TaskAgentPublicKey.

    :param exponent: Gets or sets the exponent for the public key.
    :type exponent: str
    :param modulus: Gets or sets the modulus for the public key.
    :type modulus: str
    """

    _attribute_map = {
        'exponent': {'key': 'exponent', 'type': 'str'},
        'modulus': {'key': 'modulus', 'type': 'str'}
    }

    def __init__(self, exponent=None, modulus=None):
        super(TaskAgentPublicKey, self).__init__()
        self.exponent = exponent
        self.modulus = modulus


class TaskAgentQueue(Model):
    """TaskAgentQueue.

    :param id: Id of the queue
    :type id: int
    :param name: Name of the queue
    :type name: str
    :param pool: Pool reference for this queue
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param project_id: Project Id
    :type project_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project_id': {'key': 'projectId', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, pool=None, project_id=None):
        super(TaskAgentQueue, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project_id = project_id


class TaskAgentReference(Model):
    """TaskAgentReference.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.task_agent.models.ReferenceLinks>`
    :param access_point: Gets the access point of the agent.
    :type access_point: str
    :param enabled: Gets or sets a value indicating whether or not this agent should be enabled for job execution.
    :type enabled: bool
    :param id: Gets the identifier of the agent.
    :type id: int
    :param name: Gets the name of the agent.
    :type name: str
    :param oSDescription: Gets the OS of the agent.
    :type oSDescription: str
    :param provisioning_state: Gets or sets the current provisioning state of this agent
    :type provisioning_state: str
    :param status: Gets the current connectivity status of the agent.
    :type status: object
    :param version: Gets the version of the agent.
    :type version: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'oSDescription': {'key': 'oSDescription', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, access_point=None, enabled=None, id=None, name=None, oSDescription=None, provisioning_state=None, status=None, version=None):
        super(TaskAgentReference, self).__init__()
        self._links = _links
        self.access_point = access_point
        self.enabled = enabled
        self.id = id
        self.name = name
        self.oSDescription = oSDescription
        self.provisioning_state = provisioning_state
        self.status = status
        self.version = version


class TaskAgentSession(Model):
    """TaskAgentSession.

    :param agent: Gets or sets the agent which is the target of the session.
    :type agent: :class:`TaskAgentReference <azure.devops.v5_1.task_agent.models.TaskAgentReference>`
    :param encryption_key: Gets the key used to encrypt message traffic for this session.
    :type encryption_key: :class:`TaskAgentSessionKey <azure.devops.v5_1.task_agent.models.TaskAgentSessionKey>`
    :param owner_name: Gets or sets the owner name of this session. Generally this will be the machine of origination.
    :type owner_name: str
    :param session_id: Gets the unique identifier for this session.
    :type session_id: str
    :param system_capabilities:
    :type system_capabilities: dict
    """

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgentReference'},
        'encryption_key': {'key': 'encryptionKey', 'type': 'TaskAgentSessionKey'},
        'owner_name': {'key': 'ownerName', 'type': 'str'},
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'system_capabilities': {'key': 'systemCapabilities', 'type': '{str}'}
    }

    def __init__(self, agent=None, encryption_key=None, owner_name=None, session_id=None, system_capabilities=None):
        super(TaskAgentSession, self).__init__()
        self.agent = agent
        self.encryption_key = encryption_key
        self.owner_name = owner_name
        self.session_id = session_id
        self.system_capabilities = system_capabilities


class TaskAgentSessionKey(Model):
    """TaskAgentSessionKey.

    :param encrypted: Gets or sets a value indicating whether or not the key value is encrypted. If this value is true, the Value property should be decrypted using the <c>RSA</c> key exchanged with the server during registration.
    :type encrypted: bool
    :param value: Gets or sets the symmetric key value.
    :type value: str
    """

    _attribute_map = {
        'encrypted': {'key': 'encrypted', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, encrypted=None, value=None):
        super(TaskAgentSessionKey, self).__init__()
        self.encrypted = encrypted
        self.value = value


class TaskAgentUpdate(Model):
    """TaskAgentUpdate.

    :param current_state: The current state of this agent update
    :type current_state: str
    :param reason: The reason of this agent update
    :type reason: :class:`TaskAgentUpdateReason <azure.devops.v5_1.task_agent.models.TaskAgentUpdateReason>`
    :param requested_by: The identity that request the agent update
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param request_time: Gets the date on which this agent update was requested.
    :type request_time: datetime
    :param source_version: Gets or sets the source agent version of the agent update
    :type source_version: :class:`PackageVersion <azure.devops.v5_1.task_agent.models.PackageVersion>`
    :param target_version: Gets or sets the target agent version of the agent update
    :type target_version: :class:`PackageVersion <azure.devops.v5_1.task_agent.models.PackageVersion>`
    """

    _attribute_map = {
        'current_state': {'key': 'currentState', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'TaskAgentUpdateReason'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'request_time': {'key': 'requestTime', 'type': 'iso-8601'},
        'source_version': {'key': 'sourceVersion', 'type': 'PackageVersion'},
        'target_version': {'key': 'targetVersion', 'type': 'PackageVersion'}
    }

    def __init__(self, current_state=None, reason=None, requested_by=None, request_time=None, source_version=None, target_version=None):
        super(TaskAgentUpdate, self).__init__()
        self.current_state = current_state
        self.reason = reason
        self.requested_by = requested_by
        self.request_time = request_time
        self.source_version = source_version
        self.target_version = target_version


class TaskAgentUpdateReason(Model):
    """TaskAgentUpdateReason.

    :param code:
    :type code: object
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'object'}
    }

    def __init__(self, code=None):
        super(TaskAgentUpdateReason, self).__init__()
        self.code = code


class TaskDefinition(Model):
    """TaskDefinition.

    :param agent_execution:
    :type agent_execution: :class:`TaskExecution <azure.devops.v5_1.task_agent.models.TaskExecution>`
    :param author:
    :type author: str
    :param category:
    :type category: str
    :param contents_uploaded:
    :type contents_uploaded: bool
    :param contribution_identifier:
    :type contribution_identifier: str
    :param contribution_version:
    :type contribution_version: str
    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBinding <azure.devops.v5_1.task_agent.models.DataSourceBinding>`
    :param definition_type:
    :type definition_type: str
    :param demands:
    :type demands: list of :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param deprecated:
    :type deprecated: bool
    :param description:
    :type description: str
    :param disabled:
    :type disabled: bool
    :param ecosystem:
    :type ecosystem: str
    :param execution:
    :type execution: dict
    :param friendly_name:
    :type friendly_name: str
    :param groups:
    :type groups: list of :class:`TaskGroupDefinition <azure.devops.v5_1.task_agent.models.TaskGroupDefinition>`
    :param help_mark_down:
    :type help_mark_down: str
    :param host_type:
    :type host_type: str
    :param icon_url:
    :type icon_url: str
    :param id:
    :type id: str
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinition <azure.devops.v5_1.task_agent.models.TaskInputDefinition>`
    :param instance_name_format:
    :type instance_name_format: str
    :param minimum_agent_version:
    :type minimum_agent_version: str
    :param name:
    :type name: str
    :param output_variables:
    :type output_variables: list of :class:`TaskOutputVariable <azure.devops.v5_1.task_agent.models.TaskOutputVariable>`
    :param package_location:
    :type package_location: str
    :param package_type:
    :type package_type: str
    :param post_job_execution:
    :type post_job_execution: dict
    :param pre_job_execution:
    :type pre_job_execution: dict
    :param preview:
    :type preview: bool
    :param release_notes:
    :type release_notes: str
    :param runs_on:
    :type runs_on: list of str
    :param satisfies:
    :type satisfies: list of str
    :param server_owned:
    :type server_owned: bool
    :param show_environment_variables:
    :type show_environment_variables: bool
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinition <azure.devops.v5_1.task_agent.models.TaskSourceDefinition>`
    :param source_location:
    :type source_location: str
    :param version:
    :type version: :class:`TaskVersion <azure.devops.v5_1.task_agent.models.TaskVersion>`
    :param visibility:
    :type visibility: list of str
    """

    _attribute_map = {
        'agent_execution': {'key': 'agentExecution', 'type': 'TaskExecution'},
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'contents_uploaded': {'key': 'contentsUploaded', 'type': 'bool'},
        'contribution_identifier': {'key': 'contributionIdentifier', 'type': 'str'},
        'contribution_version': {'key': 'contributionVersion', 'type': 'str'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deprecated': {'key': 'deprecated', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'ecosystem': {'key': 'ecosystem', 'type': 'str'},
        'execution': {'key': 'execution', 'type': '{object}'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[TaskGroupDefinition]'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'host_type': {'key': 'hostType', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'minimum_agent_version': {'key': 'minimumAgentVersion', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'output_variables': {'key': 'outputVariables', 'type': '[TaskOutputVariable]'},
        'package_location': {'key': 'packageLocation', 'type': 'str'},
        'package_type': {'key': 'packageType', 'type': 'str'},
        'post_job_execution': {'key': 'postJobExecution', 'type': '{object}'},
        'pre_job_execution': {'key': 'preJobExecution', 'type': '{object}'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'release_notes': {'key': 'releaseNotes', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'satisfies': {'key': 'satisfies', 'type': '[str]'},
        'server_owned': {'key': 'serverOwned', 'type': 'bool'},
        'show_environment_variables': {'key': 'showEnvironmentVariables', 'type': 'bool'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinition]'},
        'source_location': {'key': 'sourceLocation', 'type': 'str'},
        'version': {'key': 'version', 'type': 'TaskVersion'},
        'visibility': {'key': 'visibility', 'type': '[str]'}
    }

    def __init__(self, agent_execution=None, author=None, category=None, contents_uploaded=None, contribution_identifier=None, contribution_version=None, data_source_bindings=None, definition_type=None, demands=None, deprecated=None, description=None, disabled=None, ecosystem=None, execution=None, friendly_name=None, groups=None, help_mark_down=None, host_type=None, icon_url=None, id=None, inputs=None, instance_name_format=None, minimum_agent_version=None, name=None, output_variables=None, package_location=None, package_type=None, post_job_execution=None, pre_job_execution=None, preview=None, release_notes=None, runs_on=None, satisfies=None, server_owned=None, show_environment_variables=None, source_definitions=None, source_location=None, version=None, visibility=None):
        super(TaskDefinition, self).__init__()
        self.agent_execution = agent_execution
        self.author = author
        self.category = category
        self.contents_uploaded = contents_uploaded
        self.contribution_identifier = contribution_identifier
        self.contribution_version = contribution_version
        self.data_source_bindings = data_source_bindings
        self.definition_type = definition_type
        self.demands = demands
        self.deprecated = deprecated
        self.description = description
        self.disabled = disabled
        self.ecosystem = ecosystem
        self.execution = execution
        self.friendly_name = friendly_name
        self.groups = groups
        self.help_mark_down = help_mark_down
        self.host_type = host_type
        self.icon_url = icon_url
        self.id = id
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.minimum_agent_version = minimum_agent_version
        self.name = name
        self.output_variables = output_variables
        self.package_location = package_location
        self.package_type = package_type
        self.post_job_execution = post_job_execution
        self.pre_job_execution = pre_job_execution
        self.preview = preview
        self.release_notes = release_notes
        self.runs_on = runs_on
        self.satisfies = satisfies
        self.server_owned = server_owned
        self.show_environment_variables = show_environment_variables
        self.source_definitions = source_definitions
        self.source_location = source_location
        self.version = version
        self.visibility = visibility


class TaskDefinitionEndpoint(Model):
    """TaskDefinitionEndpoint.

    :param connection_id: An ID that identifies a service connection to be used for authenticating endpoint requests.
    :type connection_id: str
    :param key_selector: An Json based keyselector to filter response returned by fetching the endpoint <c>Url</c>.A Json based keyselector must be prefixed with "jsonpath:". KeySelector can be used to specify the filter to get the keys for the values specified with Selector. <example> The following keyselector defines an Json for extracting nodes named 'ServiceName'. <code> endpoint.KeySelector = "jsonpath://ServiceName"; </code></example>
    :type key_selector: str
    :param scope: The scope as understood by Connected Services. Essentialy, a project-id for now.
    :type scope: str
    :param selector: An XPath/Json based selector to filter response returned by fetching the endpoint <c>Url</c>. An XPath based selector must be prefixed with the string "xpath:". A Json based selector must be prefixed with "jsonpath:". <example> The following selector defines an XPath for extracting nodes named 'ServiceName'. <code> endpoint.Selector = "xpath://ServiceName"; </code></example>
    :type selector: str
    :param task_id: TaskId that this endpoint belongs to.
    :type task_id: str
    :param url: URL to GET.
    :type url: str
    """

    _attribute_map = {
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, connection_id=None, key_selector=None, scope=None, selector=None, task_id=None, url=None):
        super(TaskDefinitionEndpoint, self).__init__()
        self.connection_id = connection_id
        self.key_selector = key_selector
        self.scope = scope
        self.selector = selector
        self.task_id = task_id
        self.url = url


class TaskDefinitionReference(Model):
    """TaskDefinitionReference.

    :param definition_type: Gets or sets the definition type. Values can be 'task' or 'metaTask'.
    :type definition_type: str
    :param id: Gets or sets the unique identifier of task.
    :type id: str
    :param version_spec: Gets or sets the version specification of task.
    :type version_spec: str
    """

    _attribute_map = {
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'version_spec': {'key': 'versionSpec', 'type': 'str'}
    }

    def __init__(self, definition_type=None, id=None, version_spec=None):
        super(TaskDefinitionReference, self).__init__()
        self.definition_type = definition_type
        self.id = id
        self.version_spec = version_spec


class TaskExecution(Model):
    """TaskExecution.

    :param exec_task: The utility task to run.  Specifying this means that this task definition is simply a meta task to call another task. This is useful for tasks that call utility tasks like powershell and commandline
    :type exec_task: :class:`TaskReference <azure.devops.v5_1.task_agent.models.TaskReference>`
    :param platform_instructions: If a task is going to run code, then this provides the type/script etc... information by platform. For example, it might look like. net45: { typeName: "Microsoft.TeamFoundation.Automation.Tasks.PowerShellTask", assemblyName: "Microsoft.TeamFoundation.Automation.Tasks.PowerShell.dll" } net20: { typeName: "Microsoft.TeamFoundation.Automation.Tasks.PowerShellTask", assemblyName: "Microsoft.TeamFoundation.Automation.Tasks.PowerShell.dll" } java: { jar: "powershelltask.tasks.automation.teamfoundation.microsoft.com", } node: { script: "powershellhost.js", }
    :type platform_instructions: dict
    """

    _attribute_map = {
        'exec_task': {'key': 'execTask', 'type': 'TaskReference'},
        'platform_instructions': {'key': 'platformInstructions', 'type': '{{str}}'}
    }

    def __init__(self, exec_task=None, platform_instructions=None):
        super(TaskExecution, self).__init__()
        self.exec_task = exec_task
        self.platform_instructions = platform_instructions


class TaskGroup(TaskDefinition):
    """TaskGroup.

    :param agent_execution:
    :type agent_execution: :class:`TaskExecution <azure.devops.v5_1.task_agent.models.TaskExecution>`
    :param author:
    :type author: str
    :param category:
    :type category: str
    :param contents_uploaded:
    :type contents_uploaded: bool
    :param contribution_identifier:
    :type contribution_identifier: str
    :param contribution_version:
    :type contribution_version: str
    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBinding <azure.devops.v5_1.task_agent.models.DataSourceBinding>`
    :param definition_type:
    :type definition_type: str
    :param demands:
    :type demands: list of :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param deprecated:
    :type deprecated: bool
    :param description:
    :type description: str
    :param disabled:
    :type disabled: bool
    :param ecosystem:
    :type ecosystem: str
    :param execution:
    :type execution: dict
    :param friendly_name:
    :type friendly_name: str
    :param groups:
    :type groups: list of :class:`TaskGroupDefinition <azure.devops.v5_1.task_agent.models.TaskGroupDefinition>`
    :param help_mark_down:
    :type help_mark_down: str
    :param host_type:
    :type host_type: str
    :param icon_url:
    :type icon_url: str
    :param id:
    :type id: str
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinition <azure.devops.v5_1.task_agent.models.TaskInputDefinition>`
    :param instance_name_format:
    :type instance_name_format: str
    :param minimum_agent_version:
    :type minimum_agent_version: str
    :param name:
    :type name: str
    :param output_variables:
    :type output_variables: list of :class:`TaskOutputVariable <azure.devops.v5_1.task_agent.models.TaskOutputVariable>`
    :param package_location:
    :type package_location: str
    :param package_type:
    :type package_type: str
    :param post_job_execution:
    :type post_job_execution: dict
    :param pre_job_execution:
    :type pre_job_execution: dict
    :param preview:
    :type preview: bool
    :param release_notes:
    :type release_notes: str
    :param runs_on:
    :type runs_on: list of str
    :param satisfies:
    :type satisfies: list of str
    :param server_owned:
    :type server_owned: bool
    :param show_environment_variables:
    :type show_environment_variables: bool
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinition <azure.devops.v5_1.task_agent.models.TaskSourceDefinition>`
    :param source_location:
    :type source_location: str
    :param version:
    :type version: :class:`TaskVersion <azure.devops.v5_1.task_agent.models.TaskVersion>`
    :param visibility:
    :type visibility: list of str
    :param comment: Gets or sets comment.
    :type comment: str
    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on: Gets or sets date on which it got created.
    :type created_on: datetime
    :param deleted: Gets or sets as 'true' to indicate as deleted, 'false' otherwise.
    :type deleted: bool
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param modified_on: Gets or sets date on which it got modified.
    :type modified_on: datetime
    :param owner: Gets or sets the owner.
    :type owner: str
    :param parent_definition_id: Gets or sets parent task group Id. This is used while creating a draft task group.
    :type parent_definition_id: str
    :param revision: Gets or sets revision.
    :type revision: int
    :param tasks: Gets or sets the tasks.
    :type tasks: list of :class:`TaskGroupStep <azure.devops.v5_1.task_agent.models.TaskGroupStep>`
    """

    _attribute_map = {
        'agent_execution': {'key': 'agentExecution', 'type': 'TaskExecution'},
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'contents_uploaded': {'key': 'contentsUploaded', 'type': 'bool'},
        'contribution_identifier': {'key': 'contributionIdentifier', 'type': 'str'},
        'contribution_version': {'key': 'contributionVersion', 'type': 'str'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deprecated': {'key': 'deprecated', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'ecosystem': {'key': 'ecosystem', 'type': 'str'},
        'execution': {'key': 'execution', 'type': '{object}'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[TaskGroupDefinition]'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'host_type': {'key': 'hostType', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'minimum_agent_version': {'key': 'minimumAgentVersion', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'output_variables': {'key': 'outputVariables', 'type': '[TaskOutputVariable]'},
        'package_location': {'key': 'packageLocation', 'type': 'str'},
        'package_type': {'key': 'packageType', 'type': 'str'},
        'post_job_execution': {'key': 'postJobExecution', 'type': '{object}'},
        'pre_job_execution': {'key': 'preJobExecution', 'type': '{object}'},
        'preview': {'key': 'preview', 'type': 'bool'},
        'release_notes': {'key': 'releaseNotes', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'satisfies': {'key': 'satisfies', 'type': '[str]'},
        'server_owned': {'key': 'serverOwned', 'type': 'bool'},
        'show_environment_variables': {'key': 'showEnvironmentVariables', 'type': 'bool'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinition]'},
        'source_location': {'key': 'sourceLocation', 'type': 'str'},
        'version': {'key': 'version', 'type': 'TaskVersion'},
        'visibility': {'key': 'visibility', 'type': '[str]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'deleted': {'key': 'deleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'}
    }

    def __init__(self, agent_execution=None, author=None, category=None, contents_uploaded=None, contribution_identifier=None, contribution_version=None, data_source_bindings=None, definition_type=None, demands=None, deprecated=None, description=None, disabled=None, ecosystem=None, execution=None, friendly_name=None, groups=None, help_mark_down=None, host_type=None, icon_url=None, id=None, inputs=None, instance_name_format=None, minimum_agent_version=None, name=None, output_variables=None, package_location=None, package_type=None, post_job_execution=None, pre_job_execution=None, preview=None, release_notes=None, runs_on=None, satisfies=None, server_owned=None, show_environment_variables=None, source_definitions=None, source_location=None, version=None, visibility=None, comment=None, created_by=None, created_on=None, deleted=None, modified_by=None, modified_on=None, owner=None, parent_definition_id=None, revision=None, tasks=None):
        super(TaskGroup, self).__init__(agent_execution=agent_execution, author=author, category=category, contents_uploaded=contents_uploaded, contribution_identifier=contribution_identifier, contribution_version=contribution_version, data_source_bindings=data_source_bindings, definition_type=definition_type, demands=demands, deprecated=deprecated, description=description, disabled=disabled, ecosystem=ecosystem, execution=execution, friendly_name=friendly_name, groups=groups, help_mark_down=help_mark_down, host_type=host_type, icon_url=icon_url, id=id, inputs=inputs, instance_name_format=instance_name_format, minimum_agent_version=minimum_agent_version, name=name, output_variables=output_variables, package_location=package_location, package_type=package_type, post_job_execution=post_job_execution, pre_job_execution=pre_job_execution, preview=preview, release_notes=release_notes, runs_on=runs_on, satisfies=satisfies, server_owned=server_owned, show_environment_variables=show_environment_variables, source_definitions=source_definitions, source_location=source_location, version=version, visibility=visibility)
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.deleted = deleted
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.owner = owner
        self.parent_definition_id = parent_definition_id
        self.revision = revision
        self.tasks = tasks


class TaskGroupCreateParameter(Model):
    """TaskGroupCreateParameter.

    :param author: Sets author name of the task group.
    :type author: str
    :param category: Sets category of the task group.
    :type category: str
    :param description: Sets description of the task group.
    :type description: str
    :param friendly_name: Sets friendly name of the task group.
    :type friendly_name: str
    :param icon_url: Sets url icon of the task group.
    :type icon_url: str
    :param inputs: Sets input for the task group.
    :type inputs: list of :class:`TaskInputDefinition <azure.devops.v5_1.task_agent.models.TaskInputDefinition>`
    :param instance_name_format: Sets display name of the task group.
    :type instance_name_format: str
    :param name: Sets name of the task group.
    :type name: str
    :param parent_definition_id: Sets parent task group Id. This is used while creating a draft task group.
    :type parent_definition_id: str
    :param runs_on: Sets RunsOn of the task group. Value can be 'Agent', 'Server' or 'DeploymentGroup'.
    :type runs_on: list of str
    :param tasks: Sets tasks for the task group.
    :type tasks: list of :class:`TaskGroupStep <azure.devops.v5_1.task_agent.models.TaskGroupStep>`
    :param version: Sets version of the task group.
    :type version: :class:`TaskVersion <azure.devops.v5_1.task_agent.models.TaskVersion>`
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'},
        'version': {'key': 'version', 'type': 'TaskVersion'}
    }

    def __init__(self, author=None, category=None, description=None, friendly_name=None, icon_url=None, inputs=None, instance_name_format=None, name=None, parent_definition_id=None, runs_on=None, tasks=None, version=None):
        super(TaskGroupCreateParameter, self).__init__()
        self.author = author
        self.category = category
        self.description = description
        self.friendly_name = friendly_name
        self.icon_url = icon_url
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.name = name
        self.parent_definition_id = parent_definition_id
        self.runs_on = runs_on
        self.tasks = tasks
        self.version = version


class TaskGroupDefinition(Model):
    """TaskGroupDefinition.

    :param display_name:
    :type display_name: str
    :param is_expanded:
    :type is_expanded: bool
    :param name:
    :type name: str
    :param tags:
    :type tags: list of str
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, display_name=None, is_expanded=None, name=None, tags=None, visible_rule=None):
        super(TaskGroupDefinition, self).__init__()
        self.display_name = display_name
        self.is_expanded = is_expanded
        self.name = name
        self.tags = tags
        self.visible_rule = visible_rule


class TaskGroupRevision(Model):
    """TaskGroupRevision.

    :param changed_by:
    :type changed_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param changed_date:
    :type changed_date: datetime
    :param change_type:
    :type change_type: object
    :param comment:
    :type comment: str
    :param file_id:
    :type file_id: int
    :param revision:
    :type revision: int
    :param task_group_id:
    :type task_group_id: str
    """

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'},
        'task_group_id': {'key': 'taskGroupId', 'type': 'str'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_type=None, comment=None, file_id=None, revision=None, task_group_id=None):
        super(TaskGroupRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.file_id = file_id
        self.revision = revision
        self.task_group_id = task_group_id


class TaskGroupStep(Model):
    """TaskGroupStep.

    :param always_run: Gets or sets as 'true' to run the task always, 'false' otherwise.
    :type always_run: bool
    :param condition: Gets or sets condition for the task.
    :type condition: str
    :param continue_on_error: Gets or sets as 'true' to continue on error, 'false' otherwise.
    :type continue_on_error: bool
    :param display_name: Gets or sets the display name.
    :type display_name: str
    :param enabled: Gets or sets as task is enabled or not.
    :type enabled: bool
    :param environment: Gets dictionary of environment variables.
    :type environment: dict
    :param inputs: Gets or sets dictionary of inputs.
    :type inputs: dict
    :param task: Gets or sets the reference of the task.
    :type task: :class:`TaskDefinitionReference <azure.devops.v5_1.task_agent.models.TaskDefinitionReference>`
    :param timeout_in_minutes: Gets or sets the maximum time, in minutes, that a task is allowed to execute on agent before being cancelled by server. A zero value indicates an infinite timeout.
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'task': {'key': 'task', 'type': 'TaskDefinitionReference'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, display_name=None, enabled=None, environment=None, inputs=None, task=None, timeout_in_minutes=None):
        super(TaskGroupStep, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes


class TaskGroupUpdateParameter(Model):
    """TaskGroupUpdateParameter.

    :param author: Sets author name of the task group.
    :type author: str
    :param category: Sets category of the task group.
    :type category: str
    :param comment: Sets comment of the task group.
    :type comment: str
    :param description: Sets description of the task group.
    :type description: str
    :param friendly_name: Sets friendly name of the task group.
    :type friendly_name: str
    :param icon_url: Sets url icon of the task group.
    :type icon_url: str
    :param id: Sets the unique identifier of this field.
    :type id: str
    :param inputs: Sets input for the task group.
    :type inputs: list of :class:`TaskInputDefinition <azure.devops.v5_1.task_agent.models.TaskInputDefinition>`
    :param instance_name_format: Sets display name of the task group.
    :type instance_name_format: str
    :param name: Sets name of the task group.
    :type name: str
    :param parent_definition_id: Gets or sets parent task group Id. This is used while creating a draft task group.
    :type parent_definition_id: str
    :param revision: Sets revision of the task group.
    :type revision: int
    :param runs_on: Sets RunsOn of the task group. Value can be 'Agent', 'Server' or 'DeploymentGroup'.
    :type runs_on: list of str
    :param tasks: Sets tasks for the task group.
    :type tasks: list of :class:`TaskGroupStep <azure.devops.v5_1.task_agent.models.TaskGroupStep>`
    :param version: Sets version of the task group.
    :type version: :class:`TaskVersion <azure.devops.v5_1.task_agent.models.TaskVersion>`
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinition]'},
        'instance_name_format': {'key': 'instanceNameFormat', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_definition_id': {'key': 'parentDefinitionId', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'runs_on': {'key': 'runsOn', 'type': '[str]'},
        'tasks': {'key': 'tasks', 'type': '[TaskGroupStep]'},
        'version': {'key': 'version', 'type': 'TaskVersion'}
    }

    def __init__(self, author=None, category=None, comment=None, description=None, friendly_name=None, icon_url=None, id=None, inputs=None, instance_name_format=None, name=None, parent_definition_id=None, revision=None, runs_on=None, tasks=None, version=None):
        super(TaskGroupUpdateParameter, self).__init__()
        self.author = author
        self.category = category
        self.comment = comment
        self.description = description
        self.friendly_name = friendly_name
        self.icon_url = icon_url
        self.id = id
        self.inputs = inputs
        self.instance_name_format = instance_name_format
        self.name = name
        self.parent_definition_id = parent_definition_id
        self.revision = revision
        self.runs_on = runs_on
        self.tasks = tasks
        self.version = version


class TaskHubLicenseDetails(Model):
    """TaskHubLicenseDetails.

    :param enterprise_users_count:
    :type enterprise_users_count: int
    :param failed_to_reach_all_providers:
    :type failed_to_reach_all_providers: bool
    :param free_hosted_license_count:
    :type free_hosted_license_count: int
    :param free_license_count:
    :type free_license_count: int
    :param has_license_count_ever_updated:
    :type has_license_count_ever_updated: bool
    :param hosted_agent_minutes_free_count:
    :type hosted_agent_minutes_free_count: int
    :param hosted_agent_minutes_used_count:
    :type hosted_agent_minutes_used_count: int
    :param hosted_licenses_are_premium:
    :type hosted_licenses_are_premium: bool
    :param marketplace_purchased_hosted_licenses:
    :type marketplace_purchased_hosted_licenses: list of :class:`MarketplacePurchasedLicense <azure.devops.v5_1.task_agent.models.MarketplacePurchasedLicense>`
    :param msdn_users_count:
    :type msdn_users_count: int
    :param purchased_hosted_license_count: Microsoft-hosted licenses purchased from VSTS directly.
    :type purchased_hosted_license_count: int
    :param purchased_license_count: Self-hosted licenses purchased from VSTS directly.
    :type purchased_license_count: int
    :param total_hosted_license_count:
    :type total_hosted_license_count: int
    :param total_license_count:
    :type total_license_count: int
    :param total_private_license_count:
    :type total_private_license_count: int
    """

    _attribute_map = {
        'enterprise_users_count': {'key': 'enterpriseUsersCount', 'type': 'int'},
        'failed_to_reach_all_providers': {'key': 'failedToReachAllProviders', 'type': 'bool'},
        'free_hosted_license_count': {'key': 'freeHostedLicenseCount', 'type': 'int'},
        'free_license_count': {'key': 'freeLicenseCount', 'type': 'int'},
        'has_license_count_ever_updated': {'key': 'hasLicenseCountEverUpdated', 'type': 'bool'},
        'hosted_agent_minutes_free_count': {'key': 'hostedAgentMinutesFreeCount', 'type': 'int'},
        'hosted_agent_minutes_used_count': {'key': 'hostedAgentMinutesUsedCount', 'type': 'int'},
        'hosted_licenses_are_premium': {'key': 'hostedLicensesArePremium', 'type': 'bool'},
        'marketplace_purchased_hosted_licenses': {'key': 'marketplacePurchasedHostedLicenses', 'type': '[MarketplacePurchasedLicense]'},
        'msdn_users_count': {'key': 'msdnUsersCount', 'type': 'int'},
        'purchased_hosted_license_count': {'key': 'purchasedHostedLicenseCount', 'type': 'int'},
        'purchased_license_count': {'key': 'purchasedLicenseCount', 'type': 'int'},
        'total_hosted_license_count': {'key': 'totalHostedLicenseCount', 'type': 'int'},
        'total_license_count': {'key': 'totalLicenseCount', 'type': 'int'},
        'total_private_license_count': {'key': 'totalPrivateLicenseCount', 'type': 'int'}
    }

    def __init__(self, enterprise_users_count=None, failed_to_reach_all_providers=None, free_hosted_license_count=None, free_license_count=None, has_license_count_ever_updated=None, hosted_agent_minutes_free_count=None, hosted_agent_minutes_used_count=None, hosted_licenses_are_premium=None, marketplace_purchased_hosted_licenses=None, msdn_users_count=None, purchased_hosted_license_count=None, purchased_license_count=None, total_hosted_license_count=None, total_license_count=None, total_private_license_count=None):
        super(TaskHubLicenseDetails, self).__init__()
        self.enterprise_users_count = enterprise_users_count
        self.failed_to_reach_all_providers = failed_to_reach_all_providers
        self.free_hosted_license_count = free_hosted_license_count
        self.free_license_count = free_license_count
        self.has_license_count_ever_updated = has_license_count_ever_updated
        self.hosted_agent_minutes_free_count = hosted_agent_minutes_free_count
        self.hosted_agent_minutes_used_count = hosted_agent_minutes_used_count
        self.hosted_licenses_are_premium = hosted_licenses_are_premium
        self.marketplace_purchased_hosted_licenses = marketplace_purchased_hosted_licenses
        self.msdn_users_count = msdn_users_count
        self.purchased_hosted_license_count = purchased_hosted_license_count
        self.purchased_license_count = purchased_license_count
        self.total_hosted_license_count = total_hosted_license_count
        self.total_license_count = total_license_count
        self.total_private_license_count = total_private_license_count


class TaskInputDefinitionBase(Model):
    """TaskInputDefinitionBase.

    :param aliases:
    :type aliases: list of str
    :param default_value:
    :type default_value: str
    :param group_name:
    :type group_name: str
    :param help_mark_down:
    :type help_mark_down: str
    :param label:
    :type label: str
    :param name:
    :type name: str
    :param options:
    :type options: dict
    :param properties:
    :type properties: dict
    :param required:
    :type required: bool
    :param type:
    :type type: str
    :param validation:
    :type validation: :class:`TaskInputValidation <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
        self.aliases = aliases
        self.default_value = default_value
        self.group_name = group_name
        self.help_mark_down = help_mark_down
        self.label = label
        self.name = name
        self.options = options
        self.properties = properties
        self.required = required
        self.type = type
        self.validation = validation
        self.visible_rule = visible_rule


class TaskInputValidation(Model):
    """TaskInputValidation.

    :param expression: Conditional expression
    :type expression: str
    :param message: Message explaining how user can correct if validation fails
    :type message: str
    """

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, expression=None, message=None):
        super(TaskInputValidation, self).__init__()
        self.expression = expression
        self.message = message


class TaskOrchestrationOwner(Model):
    """TaskOrchestrationOwner.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.task_agent.models.ReferenceLinks>`
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(TaskOrchestrationOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class TaskOutputVariable(Model):
    """TaskOutputVariable.

    :param description:
    :type description: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(TaskOutputVariable, self).__init__()
        self.description = description
        self.name = name


class TaskPackageMetadata(Model):
    """TaskPackageMetadata.

    :param type: Gets the name of the package.
    :type type: str
    :param url: Gets the url of the package.
    :type url: str
    :param version: Gets the version of the package.
    :type version: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, type=None, url=None, version=None):
        super(TaskPackageMetadata, self).__init__()
        self.type = type
        self.url = url
        self.version = version


class TaskReference(Model):
    """TaskReference.

    :param id:
    :type id: str
    :param inputs:
    :type inputs: dict
    :param name:
    :type name: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, inputs=None, name=None, version=None):
        super(TaskReference, self).__init__()
        self.id = id
        self.inputs = inputs
        self.name = name
        self.version = version


class TaskSourceDefinitionBase(Model):
    """TaskSourceDefinitionBase.

    :param auth_key:
    :type auth_key: str
    :param endpoint:
    :type endpoint: str
    :param key_selector:
    :type key_selector: str
    :param selector:
    :type selector: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinitionBase, self).__init__()
        self.auth_key = auth_key
        self.endpoint = endpoint
        self.key_selector = key_selector
        self.selector = selector
        self.target = target


class TaskVersion(Model):
    """TaskVersion.

    :param is_test:
    :type is_test: bool
    :param major:
    :type major: int
    :param minor:
    :type minor: int
    :param patch:
    :type patch: int
    """

    _attribute_map = {
        'is_test': {'key': 'isTest', 'type': 'bool'},
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, is_test=None, major=None, minor=None, patch=None):
        super(TaskVersion, self).__init__()
        self.is_test = is_test
        self.major = major
        self.minor = minor
        self.patch = patch


class ValidationItem(Model):
    """ValidationItem.

    :param is_valid: Tells whether the current input is valid or not
    :type is_valid: bool
    :param reason: Reason for input validation failure
    :type reason: str
    :param type: Type of validation item
    :type type: str
    :param value: Value to validate. The conditional expression to validate for the input for "expression" type Eg:eq(variables['Build.SourceBranch'], 'refs/heads/master');eq(value, 'refs/heads/master')
    :type value: str
    """

    _attribute_map = {
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_valid=None, reason=None, type=None, value=None):
        super(ValidationItem, self).__init__()
        self.is_valid = is_valid
        self.reason = reason
        self.type = type
        self.value = value


class VariableGroup(Model):
    """VariableGroup.

    :param created_by: Gets or sets the identity who created the variable group.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on: Gets or sets the time when variable group was created.
    :type created_on: datetime
    :param description: Gets or sets description of the variable group.
    :type description: str
    :param id: Gets or sets id of the variable group.
    :type id: int
    :param is_shared: Indicates whether variable group is shared with other projects or not.
    :type is_shared: bool
    :param modified_by: Gets or sets the identity who modified the variable group.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param modified_on: Gets or sets the time when variable group was modified
    :type modified_on: datetime
    :param name: Gets or sets name of the variable group.
    :type name: str
    :param provider_data: Gets or sets provider data.
    :type provider_data: :class:`VariableGroupProviderData <azure.devops.v5_1.task_agent.models.VariableGroupProviderData>`
    :param type: Gets or sets type of the variable group.
    :type type: str
    :param variables: Gets or sets variables contained in the variable group.
    :type variables: dict
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, is_shared=None, modified_by=None, modified_on=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.is_shared = is_shared
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupParameters(Model):
    """VariableGroupParameters.

    :param description: Sets description of the variable group.
    :type description: str
    :param name: Sets name of the variable group.
    :type name: str
    :param provider_data: Sets provider data.
    :type provider_data: :class:`VariableGroupProviderData <azure.devops.v5_1.task_agent.models.VariableGroupProviderData>`
    :param type: Sets type of the variable group.
    :type type: str
    :param variables: Sets variables contained in the variable group.
    :type variables: dict
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, description=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroupParameters, self).__init__()
        self.description = description
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupProviderData(Model):
    """VariableGroupProviderData.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(VariableGroupProviderData, self).__init__()


class VariableValue(Model):
    """VariableValue.

    :param is_secret:
    :type is_secret: bool
    :param value:
    :type value: str
    """

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value


class VirtualMachine(Model):
    """VirtualMachine.

    :param agent:
    :type agent: :class:`TaskAgent <azure.devops.v5_1.task_agent.models.TaskAgent>`
    :param id:
    :type id: int
    :param tags:
    :type tags: list of str
    """

    _attribute_map = {
        'agent': {'key': 'agent', 'type': 'TaskAgent'},
        'id': {'key': 'id', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, agent=None, id=None, tags=None):
        super(VirtualMachine, self).__init__()
        self.agent = agent
        self.id = id
        self.tags = tags


class VirtualMachineGroup(ServiceGroup):
    """VirtualMachineGroup.

    :param created_by:
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on:
    :type created_on: datetime
    :param environment_reference:
    :type environment_reference: :class:`EnvironmentReference <azure.devops.v5_1.task_agent.models.EnvironmentReference>`
    :param id:
    :type id: int
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param last_modified_on:
    :type last_modified_on: datetime
    :param name:
    :type name: str
    :param type:
    :type type: object
    :param pool_id:
    :type pool_id: int
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'environment_reference': {'key': 'environmentReference', 'type': 'EnvironmentReference'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'pool_id': {'key': 'poolId', 'type': 'int'}
    }

    def __init__(self, created_by=None, created_on=None, environment_reference=None, id=None, last_modified_by=None, last_modified_on=None, name=None, type=None, pool_id=None):
        super(VirtualMachineGroup, self).__init__(created_by=created_by, created_on=created_on, environment_reference=environment_reference, id=id, last_modified_by=last_modified_by, last_modified_on=last_modified_on, name=name, type=type)
        self.pool_id = pool_id


class VirtualMachineGroupCreateParameters(Model):
    """VirtualMachineGroupCreateParameters.

    :param name:
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(VirtualMachineGroupCreateParameters, self).__init__()
        self.name = name


class DataSourceBinding(DataSourceBindingBase):
    """DataSourceBinding.

    :param callback_context_template: Pagination format supported by this data source(ContinuationToken/SkipTop).
    :type callback_context_template: str
    :param callback_required_template: Subsequent calls needed?
    :type callback_required_template: str
    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.task_agent.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
    :param request_content: Gets or sets http request body
    :type request_content: str
    :param request_verb: Gets or sets http request verb
    :type request_verb: str
    :param result_selector: Gets or sets the result selector.
    :type result_selector: str
    :param result_template: Gets or sets the result template.
    :type result_template: str
    :param target: Gets or sets the target of the data source.
    :type target: str
    """

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBinding, self).__init__(callback_context_template=callback_context_template, callback_required_template=callback_required_template, data_source_name=data_source_name, endpoint_id=endpoint_id, endpoint_url=endpoint_url, headers=headers, initial_context_template=initial_context_template, parameters=parameters, request_content=request_content, request_verb=request_verb, result_selector=result_selector, result_template=result_template, target=target)


class DeploymentGroup(DeploymentGroupReference):
    """DeploymentGroup.

    :param id: Deployment group identifier.
    :type id: int
    :param name: Name of the deployment group.
    :type name: str
    :param pool: Deployment pool in which deployment agents are registered.
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param project: Project to which the deployment group belongs.
    :type project: :class:`ProjectReference <azure.devops.v5_1.task_agent.models.ProjectReference>`
    :param description: Description of the deployment group.
    :type description: str
    :param machine_count: Number of deployment targets in the deployment group.
    :type machine_count: int
    :param machines: List of deployment targets in the deployment group.
    :type machines: list of :class:`DeploymentMachine <azure.devops.v5_1.task_agent.models.DeploymentMachine>`
    :param machine_tags: List of unique tags across all deployment targets in the deployment group.
    :type machine_tags: list of str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'description': {'key': 'description', 'type': 'str'},
        'machine_count': {'key': 'machineCount', 'type': 'int'},
        'machines': {'key': 'machines', 'type': '[DeploymentMachine]'},
        'machine_tags': {'key': 'machineTags', 'type': '[str]'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None, description=None, machine_count=None, machines=None, machine_tags=None):
        super(DeploymentGroup, self).__init__(id=id, name=name, pool=pool, project=project)
        self.description = description
        self.machine_count = machine_count
        self.machines = machines
        self.machine_tags = machine_tags


class DeploymentMachineGroup(DeploymentMachineGroupReference):
    """DeploymentMachineGroup.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param pool:
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.task_agent.models.TaskAgentPoolReference>`
    :param project:
    :type project: :class:`ProjectReference <azure.devops.v5_1.task_agent.models.ProjectReference>`
    :param machines:
    :type machines: list of :class:`DeploymentMachine <azure.devops.v5_1.task_agent.models.DeploymentMachine>`
    :param size:
    :type size: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'machines': {'key': 'machines', 'type': '[DeploymentMachine]'},
        'size': {'key': 'size', 'type': 'int'}
    }

    def __init__(self, id=None, name=None, pool=None, project=None, machines=None, size=None):
        super(DeploymentMachineGroup, self).__init__(id=id, name=name, pool=pool, project=project)
        self.machines = machines
        self.size = size


class KubernetesServiceGroup(ServiceGroup):
    """KubernetesServiceGroup.

    :param created_by:
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on:
    :type created_on: datetime
    :param environment_reference:
    :type environment_reference: :class:`EnvironmentReference <azure.devops.v5_1.task_agent.models.EnvironmentReference>`
    :param id:
    :type id: int
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param last_modified_on:
    :type last_modified_on: datetime
    :param name:
    :type name: str
    :param type:
    :type type: object
    :param namespace:
    :type namespace: str
    :param service_endpoint_id:
    :type service_endpoint_id: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'environment_reference': {'key': 'environmentReference', 'type': 'EnvironmentReference'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, environment_reference=None, id=None, last_modified_by=None, last_modified_on=None, name=None, type=None, namespace=None, service_endpoint_id=None):
        super(KubernetesServiceGroup, self).__init__(created_by=created_by, created_on=created_on, environment_reference=environment_reference, id=id, last_modified_by=last_modified_by, last_modified_on=last_modified_on, name=name, type=type)
        self.namespace = namespace
        self.service_endpoint_id = service_endpoint_id


class TaskAgent(TaskAgentReference):
    """TaskAgent.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.task_agent.models.ReferenceLinks>`
    :param access_point: Gets the access point of the agent.
    :type access_point: str
    :param enabled: Gets or sets a value indicating whether or not this agent should be enabled for job execution.
    :type enabled: bool
    :param id: Gets the identifier of the agent.
    :type id: int
    :param name: Gets the name of the agent.
    :type name: str
    :param oSDescription: Gets the OS of the agent.
    :type oSDescription: str
    :param provisioning_state: Gets or sets the current provisioning state of this agent
    :type provisioning_state: str
    :param status: Gets the current connectivity status of the agent.
    :type status: object
    :param version: Gets the version of the agent.
    :type version: str
    :param assigned_agent_cloud_request: Gets the Agent Cloud Request that's currently associated with this agent
    :type assigned_agent_cloud_request: :class:`TaskAgentCloudRequest <azure.devops.v5_1.task_agent.models.TaskAgentCloudRequest>`
    :param assigned_request: Gets the request which is currently assigned to this agent.
    :type assigned_request: :class:`TaskAgentJobRequest <azure.devops.v5_1.task_agent.models.TaskAgentJobRequest>`
    :param authorization: Gets or sets the authorization information for this agent.
    :type authorization: :class:`TaskAgentAuthorization <azure.devops.v5_1.task_agent.models.TaskAgentAuthorization>`
    :param created_on: Gets the date on which this agent was created.
    :type created_on: datetime
    :param last_completed_request: Gets the last request which was completed by this agent.
    :type last_completed_request: :class:`TaskAgentJobRequest <azure.devops.v5_1.task_agent.models.TaskAgentJobRequest>`
    :param max_parallelism: Gets or sets the maximum job parallelism allowed on this host.
    :type max_parallelism: int
    :param pending_update: Gets the pending update for this agent.
    :type pending_update: :class:`TaskAgentUpdate <azure.devops.v5_1.task_agent.models.TaskAgentUpdate>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param status_changed_on: Gets the date on which the last connectivity status change occurred.
    :type status_changed_on: datetime
    :param system_capabilities:
    :type system_capabilities: dict
    :param user_capabilities:
    :type user_capabilities: dict
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'access_point': {'key': 'accessPoint', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'oSDescription': {'key': 'oSDescription', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'assigned_agent_cloud_request': {'key': 'assignedAgentCloudRequest', 'type': 'TaskAgentCloudRequest'},
        'assigned_request': {'key': 'assignedRequest', 'type': 'TaskAgentJobRequest'},
        'authorization': {'key': 'authorization', 'type': 'TaskAgentAuthorization'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_completed_request': {'key': 'lastCompletedRequest', 'type': 'TaskAgentJobRequest'},
        'max_parallelism': {'key': 'maxParallelism', 'type': 'int'},
        'pending_update': {'key': 'pendingUpdate', 'type': 'TaskAgentUpdate'},
        'properties': {'key': 'properties', 'type': 'object'},
        'status_changed_on': {'key': 'statusChangedOn', 'type': 'iso-8601'},
        'system_capabilities': {'key': 'systemCapabilities', 'type': '{str}'},
        'user_capabilities': {'key': 'userCapabilities', 'type': '{str}'}
    }

    def __init__(self, _links=None, access_point=None, enabled=None, id=None, name=None, oSDescription=None, provisioning_state=None, status=None, version=None, assigned_agent_cloud_request=None, assigned_request=None, authorization=None, created_on=None, last_completed_request=None, max_parallelism=None, pending_update=None, properties=None, status_changed_on=None, system_capabilities=None, user_capabilities=None):
        super(TaskAgent, self).__init__(_links=_links, access_point=access_point, enabled=enabled, id=id, name=name, oSDescription=oSDescription, provisioning_state=provisioning_state, status=status, version=version)
        self.assigned_agent_cloud_request = assigned_agent_cloud_request
        self.assigned_request = assigned_request
        self.authorization = authorization
        self.created_on = created_on
        self.last_completed_request = last_completed_request
        self.max_parallelism = max_parallelism
        self.pending_update = pending_update
        self.properties = properties
        self.status_changed_on = status_changed_on
        self.system_capabilities = system_capabilities
        self.user_capabilities = user_capabilities


class TaskAgentPool(TaskAgentPoolReference):
    """TaskAgentPool.

    :param id:
    :type id: int
    :param is_hosted: Gets or sets a value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param name:
    :type name: str
    :param pool_type: Gets or sets the type of the pool
    :type pool_type: object
    :param scope:
    :type scope: str
    :param size: Gets the current size of the pool.
    :type size: int
    :param agent_cloud_id: Gets or sets an agentCloudId
    :type agent_cloud_id: int
    :param auto_provision: Gets or sets a value indicating whether or not a queue should be automatically provisioned for each project collection or not.
    :type auto_provision: bool
    :param auto_size: Gets or sets a value indicating whether or not the pool should autosize itself based on the Agent Cloud Provider settings
    :type auto_size: bool
    :param created_by: Gets the identity who created this pool. The creator of the pool is automatically added into the administrators group for the pool on creation.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param created_on: Gets the date/time of the pool creation.
    :type created_on: datetime
    :param owner: Gets the identity who owns or administrates this pool.
    :type owner: :class:`IdentityRef <azure.devops.v5_1.task_agent.models.IdentityRef>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.task_agent.models.object>`
    :param target_size: Gets or sets a value indicating target parallelism
    :type target_size: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'auto_provision': {'key': 'autoProvision', 'type': 'bool'},
        'auto_size': {'key': 'autoSize', 'type': 'bool'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'properties': {'key': 'properties', 'type': 'object'},
        'target_size': {'key': 'targetSize', 'type': 'int'}
    }

    def __init__(self, id=None, is_hosted=None, name=None, pool_type=None, scope=None, size=None, agent_cloud_id=None, auto_provision=None, auto_size=None, created_by=None, created_on=None, owner=None, properties=None, target_size=None):
        super(TaskAgentPool, self).__init__(id=id, is_hosted=is_hosted, name=name, pool_type=pool_type, scope=scope, size=size)
        self.agent_cloud_id = agent_cloud_id
        self.auto_provision = auto_provision
        self.auto_size = auto_size
        self.created_by = created_by
        self.created_on = created_on
        self.owner = owner
        self.properties = properties
        self.target_size = target_size


class TaskInputDefinition(TaskInputDefinitionBase):
    """TaskInputDefinition.

    :param aliases:
    :type aliases: list of str
    :param default_value:
    :type default_value: str
    :param group_name:
    :type group_name: str
    :param help_mark_down:
    :type help_mark_down: str
    :param label:
    :type label: str
    :param name:
    :type name: str
    :param options:
    :type options: dict
    :param properties:
    :type properties: dict
    :param required:
    :type required: bool
    :param type:
    :type type: str
    :param validation:
    :type validation: :class:`TaskInputValidation <azure.devops.v5_1.task_agent.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'},
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinition, self).__init__(aliases=aliases, default_value=default_value, group_name=group_name, help_mark_down=help_mark_down, label=label, name=name, options=options, properties=properties, required=required, type=type, validation=validation, visible_rule=visible_rule)


class TaskSourceDefinition(TaskSourceDefinitionBase):
    """TaskSourceDefinition.

    :param auth_key:
    :type auth_key: str
    :param endpoint:
    :type endpoint: str
    :param key_selector:
    :type key_selector: str
    :param selector:
    :type selector: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinition, self).__init__(auth_key=auth_key, endpoint=endpoint, key_selector=key_selector, selector=selector, target=target)


__all__ = [
    'AadOauthTokenRequest',
    'AadOauthTokenResult',
    'AuthenticationSchemeReference',
    'AuthorizationHeader',
    'AzureManagementGroup',
    'AzureManagementGroupQueryResult',
    'AzureSubscription',
    'AzureSubscriptionQueryResult',
    'ClientCertificate',
    'DataSource',
    'DataSourceBindingBase',
    'DataSourceDetails',
    'DependencyBinding',
    'DependencyData',
    'DependsOn',
    'DeploymentGroupCreateParameter',
    'DeploymentGroupCreateParameterPoolProperty',
    'DeploymentGroupMetrics',
    'DeploymentGroupReference',
    'DeploymentGroupUpdateParameter',
    'DeploymentMachine',
    'DeploymentMachineGroupReference',
    'DeploymentPoolSummary',
    'DeploymentTargetUpdateParameter',
    'EndpointAuthorization',
    'EndpointUrl',
    'EnvironmentCreateParameter',
    'EnvironmentDeploymentExecutionRecord',
    'EnvironmentInstance',
    'EnvironmentReference',
    'EnvironmentUpdateParameter',
    'GraphSubjectBase',
    'HelpLink',
    'IdentityRef',
    'InputDescriptor',
    'InputValidation',
    'InputValidationRequest',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'KubernetesServiceGroupCreateParameters',
    'MarketplacePurchasedLicense',
    'MetricsColumnMetaData',
    'MetricsColumnsHeader',
    'MetricsRow',
    'PackageMetadata',
    'PackageVersion',
    'ProjectReference',
    'PublishTaskGroupMetadata',
    'ReferenceLinks',
    'ResourceLimit',
    'ResourceUsage',
    'ResultTransformationDetails',
    'SecureFile',
    'ServiceEndpoint',
    'ServiceEndpointAuthenticationScheme',
    'ServiceEndpointDetails',
    'ServiceEndpointExecutionData',
    'ServiceEndpointExecutionRecord',
    'ServiceEndpointExecutionRecordsInput',
    'ServiceEndpointRequest',
    'ServiceEndpointRequestResult',
    'ServiceEndpointType',
    'ServiceGroup',
    'ServiceGroupReference',
    'TaskAgentAuthorization',
    'TaskAgentCloud',
    'TaskAgentCloudRequest',
    'TaskAgentCloudType',
    'TaskAgentDelaySource',
    'TaskAgentJobRequest',
    'TaskAgentMessage',
    'TaskAgentPoolMaintenanceDefinition',
    'TaskAgentPoolMaintenanceJob',
    'TaskAgentPoolMaintenanceJobTargetAgent',
    'TaskAgentPoolMaintenanceOptions',
    'TaskAgentPoolMaintenanceRetentionPolicy',
    'TaskAgentPoolMaintenanceSchedule',
    'TaskAgentPoolReference',
    'TaskAgentPublicKey',
    'TaskAgentQueue',
    'TaskAgentReference',
    'TaskAgentSession',
    'TaskAgentSessionKey',
    'TaskAgentUpdate',
    'TaskAgentUpdateReason',
    'TaskDefinition',
    'TaskDefinitionEndpoint',
    'TaskDefinitionReference',
    'TaskExecution',
    'TaskGroup',
    'TaskGroupCreateParameter',
    'TaskGroupDefinition',
    'TaskGroupRevision',
    'TaskGroupStep',
    'TaskGroupUpdateParameter',
    'TaskHubLicenseDetails',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskOrchestrationOwner',
    'TaskOutputVariable',
    'TaskPackageMetadata',
    'TaskReference',
    'TaskSourceDefinitionBase',
    'TaskVersion',
    'ValidationItem',
    'VariableGroup',
    'VariableGroupParameters',
    'VariableGroupProviderData',
    'VariableValue',
    'VirtualMachine',
    'VirtualMachineGroup',
    'VirtualMachineGroupCreateParameters',
    'DataSourceBinding',
    'DeploymentGroup',
    'DeploymentMachineGroup',
    'KubernetesServiceGroup',
    'TaskAgent',
    'TaskAgentPool',
    'TaskInputDefinition',
    'TaskSourceDefinition',
]
