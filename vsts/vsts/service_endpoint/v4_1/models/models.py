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
    :type authentication_scheme: :class:`AuthenticationSchemeReference <service-endpoint.v4_1.models.AuthenticationSchemeReference>`
    :param endpoint_url:
    :type endpoint_url: str
    :param headers:
    :type headers: list of :class:`AuthorizationHeader <service-endpoint.v4_1.models.AuthorizationHeader>`
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

    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_1.models.AuthorizationHeader>`
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
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
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
    :type headers: list of :class:`AuthorizationHeader <service-endpoint.v4_1.models.AuthorizationHeader>`
    :param parameters: Gets the parameters of data source.
    :type parameters: dict
    :param resource_url: Gets or sets the resource url of data source.
    :type resource_url: str
    :param result_selector: Gets or sets the result selector.
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
    :type map: list of :class:`DependencyBinding <service-endpoint.v4_1.models.DependencyBinding>`
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
    :type depends_on: :class:`DependsOn <service-endpoint.v4_1.models.DependsOn>`
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
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_1.models.ReferenceLinks>`
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
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_1.models.ReferenceLinks>`
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
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
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
    :type validation: :class:`InputValidation <microsoft.-visual-studio.-services.-web-api.v4_1.models.InputValidation>`
    :param value_hint: A hint for input value. It can be used in the UI as the input placeholder.
    :type value_hint: str
    :param values: Information about possible values for this input
    :type values: :class:`InputValues <microsoft.-visual-studio.-services.-web-api.v4_1.models.InputValues>`
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
    :type error: :class:`InputValuesError <microsoft.-visual-studio.-services.-web-api.v4_1.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <microsoft.-visual-studio.-services.-web-api.v4_1.models.InputValue>`
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

    :param result_template: Gets or sets the template for result transformation.
    :type result_template: str
    """

    _attribute_map = {
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, result_template=None):
        super(ResultTransformationDetails, self).__init__()
        self.result_template = result_template



class ServiceEndpoint(Model):
    """ServiceEndpoint.

    :param administrators_group: Gets or sets the identity reference for the administrators group of the service endpoint.
    :type administrators_group: :class:`IdentityRef <service-endpoint.v4_1.models.IdentityRef>`
    :param authorization: Gets or sets the authorization data for talking to the endpoint.
    :type authorization: :class:`EndpointAuthorization <service-endpoint.v4_1.models.EndpointAuthorization>`
    :param created_by: Gets or sets the identity reference for the user who created the Service endpoint.
    :type created_by: :class:`IdentityRef <service-endpoint.v4_1.models.IdentityRef>`
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
    :param name: Gets or sets the friendly name of the endpoint.
    :type name: str
    :param operation_status: Error message during creation/deletion of endpoint
    :type operation_status: :class:`object <service-endpoint.v4_1.models.object>`
    :param readers_group: Gets or sets the identity reference for the readers group of the service endpoint.
    :type readers_group: :class:`IdentityRef <service-endpoint.v4_1.models.IdentityRef>`
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
        'name': {'key': 'name', 'type': 'str'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'readers_group': {'key': 'readersGroup', 'type': 'IdentityRef'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, administrators_group=None, authorization=None, created_by=None, data=None, description=None, group_scope_id=None, id=None, is_ready=None, name=None, operation_status=None, readers_group=None, type=None, url=None):
        super(ServiceEndpoint, self).__init__()
        self.administrators_group = administrators_group
        self.authorization = authorization
        self.created_by = created_by
        self.data = data
        self.description = description
        self.group_scope_id = group_scope_id
        self.id = id
        self.is_ready = is_ready
        self.name = name
        self.operation_status = operation_status
        self.readers_group = readers_group
        self.type = type
        self.url = url



class ServiceEndpointAuthenticationScheme(Model):
    """ServiceEndpointAuthenticationScheme.

    :param authorization_headers: Gets or sets the authorization headers of service endpoint authentication scheme.
    :type authorization_headers: list of :class:`AuthorizationHeader <service-endpoint.v4_1.models.AuthorizationHeader>`
    :param client_certificates: Gets or sets the certificates of service endpoint authentication scheme.
    :type client_certificates: list of :class:`ClientCertificate <service-endpoint.v4_1.models.ClientCertificate>`
    :param display_name: Gets or sets the display name for the service endpoint authentication scheme.
    :type display_name: str
    :param input_descriptors: Gets or sets the input descriptors for the service endpoint authentication scheme.
    :type input_descriptors: list of :class:`InputDescriptor <service-endpoint.v4_1.models.InputDescriptor>`
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

    :param authorization: Gets or sets the authorization of service endpoint.
    :type authorization: :class:`EndpointAuthorization <service-endpoint.v4_1.models.EndpointAuthorization>`
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
    :type definition: :class:`ServiceEndpointExecutionOwner <service-endpoint.v4_1.models.ServiceEndpointExecutionOwner>`
    :param finish_time: Gets the finish time of service endpoint execution.
    :type finish_time: datetime
    :param id: Gets the Id of service endpoint execution data.
    :type id: long
    :param owner: Gets the owner of service endpoint execution data.
    :type owner: :class:`ServiceEndpointExecutionOwner <service-endpoint.v4_1.models.ServiceEndpointExecutionOwner>`
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
    :type _links: :class:`ReferenceLinks <service-endpoint.v4_1.models.ReferenceLinks>`
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
    :type data: :class:`ServiceEndpointExecutionData <service-endpoint.v4_1.models.ServiceEndpointExecutionData>`
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
    :type data: :class:`ServiceEndpointExecutionData <service-endpoint.v4_1.models.ServiceEndpointExecutionData>`
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
    :type data_source_details: :class:`DataSourceDetails <service-endpoint.v4_1.models.DataSourceDetails>`
    :param result_transformation_details: Gets or sets the result transformation details for the service endpoint request.
    :type result_transformation_details: :class:`ResultTransformationDetails <service-endpoint.v4_1.models.ResultTransformationDetails>`
    :param service_endpoint_details: Gets or sets the service endpoint details for the service endpoint request.
    :type service_endpoint_details: :class:`ServiceEndpointDetails <service-endpoint.v4_1.models.ServiceEndpointDetails>`
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

    :param error_message: Gets or sets the error message of the service endpoint request result.
    :type error_message: str
    :param result: Gets or sets the result of service endpoint request.
    :type result: :class:`object <service-endpoint.v4_1.models.object>`
    :param status_code: Gets or sets the status code of the service endpoint request result.
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
    :type authentication_schemes: list of :class:`ServiceEndpointAuthenticationScheme <service-endpoint.v4_1.models.ServiceEndpointAuthenticationScheme>`
    :param data_sources: Data sources of service endpoint type.
    :type data_sources: list of :class:`DataSource <service-endpoint.v4_1.models.DataSource>`
    :param dependency_data: Dependency data of service endpoint type.
    :type dependency_data: list of :class:`DependencyData <service-endpoint.v4_1.models.DependencyData>`
    :param description: Gets or sets the description of service endpoint type.
    :type description: str
    :param display_name: Gets or sets the display name of service endpoint type.
    :type display_name: str
    :param endpoint_url: Gets or sets the endpoint url of service endpoint type.
    :type endpoint_url: :class:`EndpointUrl <service-endpoint.v4_1.models.EndpointUrl>`
    :param help_link: Gets or sets the help link of service endpoint type.
    :type help_link: :class:`HelpLink <service-endpoint.v4_1.models.HelpLink>`
    :param help_mark_down:
    :type help_mark_down: str
    :param icon_url: Gets or sets the icon url of service endpoint type.
    :type icon_url: str
    :param input_descriptors: Input descriptor of service endpoint type.
    :type input_descriptors: list of :class:`InputDescriptor <service-endpoint.v4_1.models.InputDescriptor>`
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

    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <service-endpoint.v4_1.models.AuthorizationHeader>`
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
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBinding, self).__init__(data_source_name=data_source_name, endpoint_id=endpoint_id, endpoint_url=endpoint_url, headers=headers, parameters=parameters, result_selector=result_selector, result_template=result_template, target=target)
