# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


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
    :type value: list of :class:`AzureManagementGroup <azure.devops.v5_0.service_endpoint.models.AzureManagementGroup>`
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
    :type value: list of :class:`AzureSubscription <azure.devops.v5_0.service_endpoint.models.AzureSubscription>`
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
    :type authentication_scheme: :class:`AuthenticationSchemeReference <azure.devops.v5_0.service_endpoint.models.AuthenticationSchemeReference>`
    :param callback_context_template:
    :type callback_context_template: str
    :param callback_required_template:
    :type callback_required_template: str
    :param endpoint_url:
    :type endpoint_url: str
    :param headers:
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_0.service_endpoint.models.AuthorizationHeader>`
    :param initial_context_template:
    :type initial_context_template: str
    :param name:
    :type name: str
    :param request_content:
    :type request_content: str
    :param request_verb:
    :type request_verb: str
    :param resource_url:
    :type resource_url: str
    :param result_selector:
    :type result_selector: str
    """

    _attribute_map = {
        'authentication_scheme': {'key': 'authenticationScheme', 'type': 'AuthenticationSchemeReference'},
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, authentication_scheme=None, callback_context_template=None, callback_required_template=None, endpoint_url=None, headers=None, initial_context_template=None, name=None, request_content=None, request_verb=None, resource_url=None, result_selector=None):
        super(DataSource, self).__init__()
        self.authentication_scheme = authentication_scheme
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.name = name
        self.request_content = request_content
        self.request_verb = request_verb
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
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_0.microsoft._team_foundation._distributed_task._common._contracts.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
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
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DataSourceDetails(Model):
    """DataSourceDetails.

    :param data_source_name: Gets or sets the data source name.
    :type data_source_name: str
    :param data_source_url: Gets or sets the data source url.
    :type data_source_url: str
    :param headers: Gets or sets the request headers.
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_0.service_endpoint.models.AuthorizationHeader>`
    :param initial_context_template: Gets or sets the initialization context used for the initial call to the data source
    :type initial_context_template: str
    :param parameters: Gets the parameters of data source.
    :type parameters: dict
    :param request_content: Gets or sets the data source request content.
    :type request_content: str
    :param request_verb: Gets or sets the data source request verb. Get/Post are the only implemented types
    :type request_verb: str
    :param resource_url: Gets or sets the resource url of data source.
    :type resource_url: str
    :param result_selector: Gets or sets the result selector.
    :type result_selector: str
    """

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'data_source_url': {'key': 'dataSourceUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'resource_url': {'key': 'resourceUrl', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, data_source_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, resource_url=None, result_selector=None):
        super(DataSourceDetails, self).__init__()
        self.data_source_name = data_source_name
        self.data_source_url = data_source_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
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
    :type map: list of :class:`DependencyBinding <azure.devops.v5_0.service_endpoint.models.DependencyBinding>`
    """

    _attribute_map = {
        'input': {'key': 'input', 'type': 'str'},
        'map': {'key': 'map', 'type': '[DependencyBinding]'}
    }

    def __init__(self, input=None, map=None):
        super(DependsOn, self).__init__()
        self.input = input
        self.map = map


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
    :type depends_on: :class:`DependsOn <azure.devops.v5_0.service_endpoint.models.DependsOn>`
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


class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias:
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
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
    :type validation: :class:`InputValidation <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.InputValidation>`
    :param value_hint: A hint for input value. It can be used in the UI as the input placeholder.
    :type value_hint: str
    :param values: Information about possible values for this input
    :type values: :class:`InputValues <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.InputValues>`
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
    :type error: :class:`InputValuesError <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.InputValue>`
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


class OAuthConfiguration(Model):
    """OAuthConfiguration.

    :param client_id: Gets or sets the ClientId
    :type client_id: str
    :param client_secret: Gets or sets the ClientSecret
    :type client_secret: str
    :param created_by: Gets or sets the identity who created the config.
    :type created_by: :class:`IdentityRef <azure.devops.v5_0.service_endpoint.models.IdentityRef>`
    :param created_on: Gets or sets the time when config was created.
    :type created_on: datetime
    :param endpoint_type: Gets or sets the type of the endpoint.
    :type endpoint_type: str
    :param id: Gets or sets the unique identifier of this field
    :type id: str
    :param modified_by: Gets or sets the identity who modified the config.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_0.service_endpoint.models.IdentityRef>`
    :param modified_on: Gets or sets the time when variable group was modified
    :type modified_on: datetime
    :param name: Gets or sets the name
    :type name: str
    :param url: Gets or sets the Url
    :type url: str
    """

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, client_id=None, client_secret=None, created_by=None, created_on=None, endpoint_type=None, id=None, modified_by=None, modified_on=None, name=None, url=None):
        super(OAuthConfiguration, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.created_by = created_by
        self.created_on = created_on
        self.endpoint_type = endpoint_type
        self.id = id
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.url = url


class OAuthConfigurationParams(Model):
    """OAuthConfigurationParams.

    :param client_id: Gets or sets the ClientId
    :type client_id: str
    :param client_secret: Gets or sets the ClientSecret
    :type client_secret: str
    :param endpoint_type: Gets or sets the type of the endpoint.
    :type endpoint_type: str
    :param name: Gets or sets the name
    :type name: str
    :param url: Gets or sets the Url
    :type url: str
    """

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, client_id=None, client_secret=None, endpoint_type=None, name=None, url=None):
        super(OAuthConfigurationParams, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.endpoint_type = endpoint_type
        self.name = name
        self.url = url


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


class ResultTransformationDetails(Model):
    """ResultTransformationDetails.

    :param callback_context_template: Gets or sets the template for callback parameters
    :type callback_context_template: str
    :param callback_required_template: Gets or sets the template to decide whether to callback or not
    :type callback_required_template: str
    :param result_template: Gets or sets the template for result transformation.
    :type result_template: str
    """

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, result_template=None):
        super(ResultTransformationDetails, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.result_template = result_template


class ServiceEndpoint(Model):
    """ServiceEndpoint.

    :param administrators_group: Gets or sets the identity reference for the administrators group of the service endpoint.
    :type administrators_group: :class:`IdentityRef <azure.devops.v5_0.service_endpoint.models.IdentityRef>`
    :param authorization: Gets or sets the authorization data for talking to the endpoint.
    :type authorization: :class:`EndpointAuthorization <azure.devops.v5_0.service_endpoint.models.EndpointAuthorization>`
    :param created_by: Gets or sets the identity reference for the user who created the Service endpoint.
    :type created_by: :class:`IdentityRef <azure.devops.v5_0.service_endpoint.models.IdentityRef>`
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
    :type operation_status: :class:`object <azure.devops.v5_0.service_endpoint.models.object>`
    :param owner: Owner of the endpoint Supported values are "library", "agentcloud"
    :type owner: str
    :param readers_group: Gets or sets the identity reference for the readers group of the service endpoint.
    :type readers_group: :class:`IdentityRef <azure.devops.v5_0.service_endpoint.models.IdentityRef>`
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
        'owner': {'key': 'owner', 'type': 'str'},
        'readers_group': {'key': 'readersGroup', 'type': 'IdentityRef'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, administrators_group=None, authorization=None, created_by=None, data=None, description=None, group_scope_id=None, id=None, is_ready=None, is_shared=None, name=None, operation_status=None, owner=None, readers_group=None, type=None, url=None):
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
        self.owner = owner
        self.readers_group = readers_group
        self.type = type
        self.url = url


class ServiceEndpointAuthenticationScheme(Model):
    """ServiceEndpointAuthenticationScheme.

    :param authorization_headers: Gets or sets the authorization headers of service endpoint authentication scheme.
    :type authorization_headers: list of :class:`AuthorizationHeader <azure.devops.v5_0.service_endpoint.models.AuthorizationHeader>`
    :param authorization_url: Gets or sets the Authorization url required to authenticate using OAuth2
    :type authorization_url: str
    :param client_certificates: Gets or sets the certificates of service endpoint authentication scheme.
    :type client_certificates: list of :class:`ClientCertificate <azure.devops.v5_0.service_endpoint.models.ClientCertificate>`
    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBinding <azure.devops.v5_0.service_endpoint.models.DataSourceBinding>`
    :param display_name: Gets or sets the display name for the service endpoint authentication scheme.
    :type display_name: str
    :param input_descriptors: Gets or sets the input descriptors for the service endpoint authentication scheme.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_0.service_endpoint.models.InputDescriptor>`
    :param scheme: Gets or sets the scheme for service endpoint authentication.
    :type scheme: str
    """

    _attribute_map = {
        'authorization_headers': {'key': 'authorizationHeaders', 'type': '[AuthorizationHeader]'},
        'authorization_url': {'key': 'authorizationUrl', 'type': 'str'},
        'client_certificates': {'key': 'clientCertificates', 'type': '[ClientCertificate]'},
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBinding]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, authorization_headers=None, authorization_url=None, client_certificates=None, data_source_bindings=None, display_name=None, input_descriptors=None, scheme=None):
        super(ServiceEndpointAuthenticationScheme, self).__init__()
        self.authorization_headers = authorization_headers
        self.authorization_url = authorization_url
        self.client_certificates = client_certificates
        self.data_source_bindings = data_source_bindings
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.scheme = scheme


class ServiceEndpointDetails(Model):
    """ServiceEndpointDetails.

    :param authorization: Gets or sets the authorization of service endpoint.
    :type authorization: :class:`EndpointAuthorization <azure.devops.v5_0.service_endpoint.models.EndpointAuthorization>`
    :param data: Gets or sets the data of service endpoint.
    :type data: dict
    :param type: Gets or sets the type of service endpoint.
    :type type: str
    :param url: Gets or sets the connection url of service endpoint.
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
    :type definition: :class:`ServiceEndpointExecutionOwner <azure.devops.v5_0.service_endpoint.models.ServiceEndpointExecutionOwner>`
    :param finish_time: Gets the finish time of service endpoint execution.
    :type finish_time: datetime
    :param id: Gets the Id of service endpoint execution data.
    :type id: long
    :param owner: Gets the owner of service endpoint execution data.
    :type owner: :class:`ServiceEndpointExecutionOwner <azure.devops.v5_0.service_endpoint.models.ServiceEndpointExecutionOwner>`
    :param plan_type: Gets the plan type of service endpoint execution data.
    :type plan_type: str
    :param result: Gets the result of service endpoint execution.
    :type result: object
    :param start_time: Gets the start time of service endpoint execution.
    :type start_time: datetime
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'ServiceEndpointExecutionOwner'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'ServiceEndpointExecutionOwner'},
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


class ServiceEndpointExecutionOwner(Model):
    """ServiceEndpointExecutionOwner.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.service_endpoint.models.ReferenceLinks>`
    :param id: Gets or sets the Id of service endpoint execution owner.
    :type id: int
    :param name: Gets or sets the name of service endpoint execution owner.
    :type name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(ServiceEndpointExecutionOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class ServiceEndpointExecutionRecord(Model):
    """ServiceEndpointExecutionRecord.

    :param data: Gets the execution data of service endpoint execution.
    :type data: :class:`ServiceEndpointExecutionData <azure.devops.v5_0.service_endpoint.models.ServiceEndpointExecutionData>`
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
    :type data: :class:`ServiceEndpointExecutionData <azure.devops.v5_0.service_endpoint.models.ServiceEndpointExecutionData>`
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

    :param data_source_details: Gets or sets the data source details for the service endpoint request.
    :type data_source_details: :class:`DataSourceDetails <azure.devops.v5_0.service_endpoint.models.DataSourceDetails>`
    :param result_transformation_details: Gets or sets the result transformation details for the service endpoint request.
    :type result_transformation_details: :class:`ResultTransformationDetails <azure.devops.v5_0.service_endpoint.models.ResultTransformationDetails>`
    :param service_endpoint_details: Gets or sets the service endpoint details for the service endpoint request.
    :type service_endpoint_details: :class:`ServiceEndpointDetails <azure.devops.v5_0.service_endpoint.models.ServiceEndpointDetails>`
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

    :param callback_context_parameters: Gets or sets the parameters used to make subsequent calls to the data source
    :type callback_context_parameters: dict
    :param callback_required: Gets or sets the flat that decides if another call to the data source is to be made
    :type callback_required: bool
    :param error_message: Gets or sets the error message of the service endpoint request result.
    :type error_message: str
    :param result: Gets or sets the result of service endpoint request.
    :type result: :class:`object <azure.devops.v5_0.service_endpoint.models.object>`
    :param status_code: Gets or sets the status code of the service endpoint request result.
    :type status_code: object
    """

    _attribute_map = {
        'callback_context_parameters': {'key': 'callbackContextParameters', 'type': '{str}'},
        'callback_required': {'key': 'callbackRequired', 'type': 'bool'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'status_code': {'key': 'statusCode', 'type': 'object'}
    }

    def __init__(self, callback_context_parameters=None, callback_required=None, error_message=None, result=None, status_code=None):
        super(ServiceEndpointRequestResult, self).__init__()
        self.callback_context_parameters = callback_context_parameters
        self.callback_required = callback_required
        self.error_message = error_message
        self.result = result
        self.status_code = status_code


class ServiceEndpointType(Model):
    """ServiceEndpointType.

    :param authentication_schemes: Authentication scheme of service endpoint type.
    :type authentication_schemes: list of :class:`ServiceEndpointAuthenticationScheme <azure.devops.v5_0.service_endpoint.models.ServiceEndpointAuthenticationScheme>`
    :param data_sources: Data sources of service endpoint type.
    :type data_sources: list of :class:`DataSource <azure.devops.v5_0.service_endpoint.models.DataSource>`
    :param dependency_data: Dependency data of service endpoint type.
    :type dependency_data: list of :class:`DependencyData <azure.devops.v5_0.service_endpoint.models.DependencyData>`
    :param description: Gets or sets the description of service endpoint type.
    :type description: str
    :param display_name: Gets or sets the display name of service endpoint type.
    :type display_name: str
    :param endpoint_url: Gets or sets the endpoint url of service endpoint type.
    :type endpoint_url: :class:`EndpointUrl <azure.devops.v5_0.service_endpoint.models.EndpointUrl>`
    :param help_link: Gets or sets the help link of service endpoint type.
    :type help_link: :class:`HelpLink <azure.devops.v5_0.service_endpoint.models.HelpLink>`
    :param help_mark_down:
    :type help_mark_down: str
    :param icon_url: Gets or sets the icon url of service endpoint type.
    :type icon_url: str
    :param input_descriptors: Input descriptor of service endpoint type.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_0.service_endpoint.models.InputDescriptor>`
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
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_0.service_endpoint.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
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
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBinding, self).__init__(callback_context_template=callback_context_template, callback_required_template=callback_required_template, data_source_name=data_source_name, endpoint_id=endpoint_id, endpoint_url=endpoint_url, headers=headers, initial_context_template=initial_context_template, parameters=parameters, result_selector=result_selector, result_template=result_template, target=target)


__all__ = [
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
    'EndpointAuthorization',
    'EndpointUrl',
    'GraphSubjectBase',
    'HelpLink',
    'IdentityRef',
    'InputDescriptor',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'OAuthConfiguration',
    'OAuthConfigurationParams',
    'ProjectReference',
    'ReferenceLinks',
    'ResultTransformationDetails',
    'ServiceEndpoint',
    'ServiceEndpointAuthenticationScheme',
    'ServiceEndpointDetails',
    'ServiceEndpointExecutionData',
    'ServiceEndpointExecutionOwner',
    'ServiceEndpointExecutionRecord',
    'ServiceEndpointExecutionRecordsInput',
    'ServiceEndpointRequest',
    'ServiceEndpointRequestResult',
    'ServiceEndpointType',
    'DataSourceBinding',
]
