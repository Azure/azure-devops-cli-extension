# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Consumer(Model):
    """Consumer.

    :param _links: Reference Links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.service_hooks.models.ReferenceLinks>`
    :param actions: Gets this consumer's actions.
    :type actions: list of :class:`ConsumerAction <azure.devops.v5_1.service_hooks.models.ConsumerAction>`
    :param authentication_type: Gets or sets this consumer's authentication type.
    :type authentication_type: object
    :param description: Gets or sets this consumer's localized description.
    :type description: str
    :param external_configuration: Non-null only if subscriptions for this consumer are configured externally.
    :type external_configuration: :class:`ExternalConfigurationDescriptor <azure.devops.v5_1.service_hooks.models.ExternalConfigurationDescriptor>`
    :param id: Gets or sets this consumer's identifier.
    :type id: str
    :param image_url: Gets or sets this consumer's image URL, if any.
    :type image_url: str
    :param information_url: Gets or sets this consumer's information URL, if any.
    :type information_url: str
    :param input_descriptors: Gets or sets this consumer's input descriptors.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.service_hooks.models.InputDescriptor>`
    :param name: Gets or sets this consumer's localized name.
    :type name: str
    :param url: The url for this resource
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'actions': {'key': 'actions', 'type': '[ConsumerAction]'},
        'authentication_type': {'key': 'authenticationType', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'external_configuration': {'key': 'externalConfiguration', 'type': 'ExternalConfigurationDescriptor'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'information_url': {'key': 'informationUrl', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, actions=None, authentication_type=None, description=None, external_configuration=None, id=None, image_url=None, information_url=None, input_descriptors=None, name=None, url=None):
        super(Consumer, self).__init__()
        self._links = _links
        self.actions = actions
        self.authentication_type = authentication_type
        self.description = description
        self.external_configuration = external_configuration
        self.id = id
        self.image_url = image_url
        self.information_url = information_url
        self.input_descriptors = input_descriptors
        self.name = name
        self.url = url


class ConsumerAction(Model):
    """ConsumerAction.

    :param _links: Reference Links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.service_hooks.models.ReferenceLinks>`
    :param allow_resource_version_override: Gets or sets the flag indicating if resource version can be overridden when creating or editing a subscription.
    :type allow_resource_version_override: bool
    :param consumer_id: Gets or sets the identifier of the consumer to which this action belongs.
    :type consumer_id: str
    :param description: Gets or sets this action's localized description.
    :type description: str
    :param id: Gets or sets this action's identifier.
    :type id: str
    :param input_descriptors: Gets or sets this action's input descriptors.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.service_hooks.models.InputDescriptor>`
    :param name: Gets or sets this action's localized name.
    :type name: str
    :param supported_event_types: Gets or sets this action's supported event identifiers.
    :type supported_event_types: list of str
    :param supported_resource_versions: Gets or sets this action's supported resource versions.
    :type supported_resource_versions: dict
    :param url: The url for this resource
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allow_resource_version_override': {'key': 'allowResourceVersionOverride', 'type': 'bool'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'supported_event_types': {'key': 'supportedEventTypes', 'type': '[str]'},
        'supported_resource_versions': {'key': 'supportedResourceVersions', 'type': '{[str]}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, allow_resource_version_override=None, consumer_id=None, description=None, id=None, input_descriptors=None, name=None, supported_event_types=None, supported_resource_versions=None, url=None):
        super(ConsumerAction, self).__init__()
        self._links = _links
        self.allow_resource_version_override = allow_resource_version_override
        self.consumer_id = consumer_id
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.supported_event_types = supported_event_types
        self.supported_resource_versions = supported_resource_versions
        self.url = url


class Event(Model):
    """Event.

    :param created_date: Gets or sets the UTC-based date and time that this event was created.
    :type created_date: datetime
    :param detailed_message: Gets or sets the detailed message associated with this event.
    :type detailed_message: :class:`FormattedEventMessage <azure.devops.v5_1.service_hooks.models.FormattedEventMessage>`
    :param event_type: Gets or sets the type of this event.
    :type event_type: str
    :param id: Gets or sets the unique identifier of this event.
    :type id: str
    :param message: Gets or sets the (brief) message associated with this event.
    :type message: :class:`FormattedEventMessage <azure.devops.v5_1.service_hooks.models.FormattedEventMessage>`
    :param publisher_id: Gets or sets the identifier of the publisher that raised this event.
    :type publisher_id: str
    :param resource: Gets or sets the data associated with this event.
    :type resource: object
    :param resource_containers: Gets or sets the resource containers.
    :type resource_containers: dict
    :param resource_version: Gets or sets the version of the data associated with this event.
    :type resource_version: str
    :param session_token: Gets or sets the Session Token that can be used in further interactions
    :type session_token: :class:`SessionToken <azure.devops.v5_1.service_hooks.models.SessionToken>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'FormattedEventMessage'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'message': {'key': 'message', 'type': 'FormattedEventMessage'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'object'},
        'resource_containers': {'key': 'resourceContainers', 'type': '{ResourceContainer}'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'},
        'session_token': {'key': 'sessionToken', 'type': 'SessionToken'}
    }

    def __init__(self, created_date=None, detailed_message=None, event_type=None, id=None, message=None, publisher_id=None, resource=None, resource_containers=None, resource_version=None, session_token=None):
        super(Event, self).__init__()
        self.created_date = created_date
        self.detailed_message = detailed_message
        self.event_type = event_type
        self.id = id
        self.message = message
        self.publisher_id = publisher_id
        self.resource = resource
        self.resource_containers = resource_containers
        self.resource_version = resource_version
        self.session_token = session_token


class EventTypeDescriptor(Model):
    """EventTypeDescriptor.

    :param description: A localized description of the event type
    :type description: str
    :param id: A unique id for the event type
    :type id: str
    :param input_descriptors: Event-specific inputs
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.service_hooks.models.InputDescriptor>`
    :param name: A localized friendly name for the event type
    :type name: str
    :param publisher_id: A unique id for the publisher of this event type
    :type publisher_id: str
    :param supported_resource_versions: Supported versions for the event's resource payloads.
    :type supported_resource_versions: list of str
    :param url: The url for this resource
    :type url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'supported_resource_versions': {'key': 'supportedResourceVersions', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, input_descriptors=None, name=None, publisher_id=None, supported_resource_versions=None, url=None):
        super(EventTypeDescriptor, self).__init__()
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.publisher_id = publisher_id
        self.supported_resource_versions = supported_resource_versions
        self.url = url


class ExternalConfigurationDescriptor(Model):
    """ExternalConfigurationDescriptor.

    :param create_subscription_url: Url of the site to create this type of subscription.
    :type create_subscription_url: str
    :param edit_subscription_property_name: The name of an input property that contains the URL to edit a subscription.
    :type edit_subscription_property_name: str
    :param hosted_only: True if the external configuration applies only to hosted.
    :type hosted_only: bool
    """

    _attribute_map = {
        'create_subscription_url': {'key': 'createSubscriptionUrl', 'type': 'str'},
        'edit_subscription_property_name': {'key': 'editSubscriptionPropertyName', 'type': 'str'},
        'hosted_only': {'key': 'hostedOnly', 'type': 'bool'}
    }

    def __init__(self, create_subscription_url=None, edit_subscription_property_name=None, hosted_only=None):
        super(ExternalConfigurationDescriptor, self).__init__()
        self.create_subscription_url = create_subscription_url
        self.edit_subscription_property_name = edit_subscription_property_name
        self.hosted_only = hosted_only


class FormattedEventMessage(Model):
    """FormattedEventMessage.

    :param html: Gets or sets the html format of the message
    :type html: str
    :param markdown: Gets or sets the markdown format of the message
    :type markdown: str
    :param text: Gets or sets the raw text of the message
    :type text: str
    """

    _attribute_map = {
        'html': {'key': 'html', 'type': 'str'},
        'markdown': {'key': 'markdown', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, html=None, markdown=None, text=None):
        super(FormattedEventMessage, self).__init__()
        self.html = html
        self.markdown = markdown
        self.text = text


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


class InputFilter(Model):
    """InputFilter.

    :param conditions: Groups of input filter expressions. This filter matches a set of inputs if any (one or more) of the groups evaluates to true.
    :type conditions: list of :class:`InputFilterCondition <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputFilterCondition>`
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[InputFilterCondition]'}
    }

    def __init__(self, conditions=None):
        super(InputFilter, self).__init__()
        self.conditions = conditions


class InputFilterCondition(Model):
    """InputFilterCondition.

    :param case_sensitive: Whether or not to do a case sensitive match
    :type case_sensitive: bool
    :param input_id: The Id of the input to filter on
    :type input_id: str
    :param input_value: The "expected" input value to compare with the actual input value
    :type input_value: str
    :param operator: The operator applied between the expected and actual input value
    :type operator: object
    """

    _attribute_map = {
        'case_sensitive': {'key': 'caseSensitive', 'type': 'bool'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'input_value': {'key': 'inputValue', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'object'}
    }

    def __init__(self, case_sensitive=None, input_id=None, input_value=None, operator=None):
        super(InputFilterCondition, self).__init__()
        self.case_sensitive = case_sensitive
        self.input_id = input_id
        self.input_value = input_value
        self.operator = operator


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


class InputValuesQuery(Model):
    """InputValuesQuery.

    :param current_values:
    :type current_values: dict
    :param input_values: The input values to return on input, and the result from the consumer on output.
    :type input_values: list of :class:`InputValues <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValues>`
    :param resource: Subscription containing information about the publisher/consumer and the current input values
    :type resource: object
    """

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'input_values': {'key': 'inputValues', 'type': '[InputValues]'},
        'resource': {'key': 'resource', 'type': 'object'}
    }

    def __init__(self, current_values=None, input_values=None, resource=None):
        super(InputValuesQuery, self).__init__()
        self.current_values = current_values
        self.input_values = input_values
        self.resource = resource


class Notification(Model):
    """Notification.

    :param created_date: Gets or sets date and time that this result was created.
    :type created_date: datetime
    :param details: Details about this notification (if available)
    :type details: :class:`NotificationDetails <azure.devops.v5_1.service_hooks.models.NotificationDetails>`
    :param event_id: The event id associated with this notification
    :type event_id: str
    :param id: The notification id
    :type id: int
    :param modified_date: Gets or sets date and time that this result was last modified.
    :type modified_date: datetime
    :param result: Result of the notification
    :type result: object
    :param status: Status of the notification
    :type status: object
    :param subscriber_id: The subscriber Id  associated with this notification. This is the last identity who touched in the subscription. In case of test notifications it can be the tester if the subscription is not created yet.
    :type subscriber_id: str
    :param subscription_id: The subscription id associated with this notification
    :type subscription_id: str
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'details': {'key': 'details', 'type': 'NotificationDetails'},
        'event_id': {'key': 'eventId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, created_date=None, details=None, event_id=None, id=None, modified_date=None, result=None, status=None, subscriber_id=None, subscription_id=None):
        super(Notification, self).__init__()
        self.created_date = created_date
        self.details = details
        self.event_id = event_id
        self.id = id
        self.modified_date = modified_date
        self.result = result
        self.status = status
        self.subscriber_id = subscriber_id
        self.subscription_id = subscription_id


class NotificationDetails(Model):
    """NotificationDetails.

    :param completed_date: Gets or sets the time that this notification was completed (response received from the consumer)
    :type completed_date: datetime
    :param consumer_action_id: Gets or sets this notification detail's consumer action identifier.
    :type consumer_action_id: str
    :param consumer_id: Gets or sets this notification detail's consumer identifier.
    :type consumer_id: str
    :param consumer_inputs: Gets or sets this notification detail's consumer inputs.
    :type consumer_inputs: dict
    :param dequeued_date: Gets or sets the time that this notification was dequeued for processing
    :type dequeued_date: datetime
    :param error_detail: Gets or sets this notification detail's error detail.
    :type error_detail: str
    :param error_message: Gets or sets this notification detail's error message.
    :type error_message: str
    :param event: Gets or sets this notification detail's event content.
    :type event: :class:`Event <azure.devops.v5_1.service_hooks.models.Event>`
    :param event_type: Gets or sets this notification detail's event type.
    :type event_type: str
    :param processed_date: Gets or sets the time that this notification was finished processing (just before the request is sent to the consumer)
    :type processed_date: datetime
    :param publisher_id: Gets or sets this notification detail's publisher identifier.
    :type publisher_id: str
    :param publisher_inputs: Gets or sets this notification detail's publisher inputs.
    :type publisher_inputs: dict
    :param queued_date: Gets or sets the time that this notification was queued (created)
    :type queued_date: datetime
    :param request: Gets or sets this notification detail's request.
    :type request: str
    :param request_attempts: Number of requests attempted to be sent to the consumer
    :type request_attempts: int
    :param request_duration: Duration of the request to the consumer in seconds
    :type request_duration: float
    :param response: Gets or sets this notification detail's reponse.
    :type response: str
    """

    _attribute_map = {
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_inputs': {'key': 'consumerInputs', 'type': '{str}'},
        'dequeued_date': {'key': 'dequeuedDate', 'type': 'iso-8601'},
        'error_detail': {'key': 'errorDetail', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'event': {'key': 'event', 'type': 'Event'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'processed_date': {'key': 'processedDate', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'queued_date': {'key': 'queuedDate', 'type': 'iso-8601'},
        'request': {'key': 'request', 'type': 'str'},
        'request_attempts': {'key': 'requestAttempts', 'type': 'int'},
        'request_duration': {'key': 'requestDuration', 'type': 'float'},
        'response': {'key': 'response', 'type': 'str'}
    }

    def __init__(self, completed_date=None, consumer_action_id=None, consumer_id=None, consumer_inputs=None, dequeued_date=None, error_detail=None, error_message=None, event=None, event_type=None, processed_date=None, publisher_id=None, publisher_inputs=None, queued_date=None, request=None, request_attempts=None, request_duration=None, response=None):
        super(NotificationDetails, self).__init__()
        self.completed_date = completed_date
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_inputs = consumer_inputs
        self.dequeued_date = dequeued_date
        self.error_detail = error_detail
        self.error_message = error_message
        self.event = event
        self.event_type = event_type
        self.processed_date = processed_date
        self.publisher_id = publisher_id
        self.publisher_inputs = publisher_inputs
        self.queued_date = queued_date
        self.request = request
        self.request_attempts = request_attempts
        self.request_duration = request_duration
        self.response = response


class NotificationResultsSummaryDetail(Model):
    """NotificationResultsSummaryDetail.

    :param notification_count: Count of notification sent out with a matching result.
    :type notification_count: int
    :param result: Result of the notification
    :type result: object
    """

    _attribute_map = {
        'notification_count': {'key': 'notificationCount', 'type': 'int'},
        'result': {'key': 'result', 'type': 'object'}
    }

    def __init__(self, notification_count=None, result=None):
        super(NotificationResultsSummaryDetail, self).__init__()
        self.notification_count = notification_count
        self.result = result


class NotificationsQuery(Model):
    """NotificationsQuery.

    :param associated_subscriptions: The subscriptions associated with the notifications returned from the query
    :type associated_subscriptions: list of :class:`Subscription <azure.devops.v5_1.service_hooks.models.Subscription>`
    :param include_details: If true, we will return all notification history for the query provided; otherwise, the summary is returned.
    :type include_details: bool
    :param max_created_date: Optional maximum date at which the notification was created
    :type max_created_date: datetime
    :param max_results: Optional maximum number of overall results to include
    :type max_results: int
    :param max_results_per_subscription: Optional maximum number of results for each subscription. Only takes effect when a list of subscription ids is supplied in the query.
    :type max_results_per_subscription: int
    :param min_created_date: Optional minimum date at which the notification was created
    :type min_created_date: datetime
    :param publisher_id: Optional publisher id to restrict the results to
    :type publisher_id: str
    :param results: Results from the query
    :type results: list of :class:`Notification <azure.devops.v5_1.service_hooks.models.Notification>`
    :param result_type: Optional notification result type to filter results to
    :type result_type: object
    :param status: Optional notification status to filter results to
    :type status: object
    :param subscription_ids: Optional list of subscription ids to restrict the results to
    :type subscription_ids: list of str
    :param summary: Summary of notifications - the count of each result type (success, fail, ..).
    :type summary: list of :class:`NotificationSummary <azure.devops.v5_1.service_hooks.models.NotificationSummary>`
    """

    _attribute_map = {
        'associated_subscriptions': {'key': 'associatedSubscriptions', 'type': '[Subscription]'},
        'include_details': {'key': 'includeDetails', 'type': 'bool'},
        'max_created_date': {'key': 'maxCreatedDate', 'type': 'iso-8601'},
        'max_results': {'key': 'maxResults', 'type': 'int'},
        'max_results_per_subscription': {'key': 'maxResultsPerSubscription', 'type': 'int'},
        'min_created_date': {'key': 'minCreatedDate', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'results': {'key': 'results', 'type': '[Notification]'},
        'result_type': {'key': 'resultType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'subscription_ids': {'key': 'subscriptionIds', 'type': '[str]'},
        'summary': {'key': 'summary', 'type': '[NotificationSummary]'}
    }

    def __init__(self, associated_subscriptions=None, include_details=None, max_created_date=None, max_results=None, max_results_per_subscription=None, min_created_date=None, publisher_id=None, results=None, result_type=None, status=None, subscription_ids=None, summary=None):
        super(NotificationsQuery, self).__init__()
        self.associated_subscriptions = associated_subscriptions
        self.include_details = include_details
        self.max_created_date = max_created_date
        self.max_results = max_results
        self.max_results_per_subscription = max_results_per_subscription
        self.min_created_date = min_created_date
        self.publisher_id = publisher_id
        self.results = results
        self.result_type = result_type
        self.status = status
        self.subscription_ids = subscription_ids
        self.summary = summary


class NotificationSummary(Model):
    """NotificationSummary.

    :param results: The notification results for this particular subscription.
    :type results: list of :class:`NotificationResultsSummaryDetail <azure.devops.v5_1.service_hooks.models.NotificationResultsSummaryDetail>`
    :param subscription_id: The subscription id associated with this notification
    :type subscription_id: str
    """

    _attribute_map = {
        'results': {'key': 'results', 'type': '[NotificationResultsSummaryDetail]'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, results=None, subscription_id=None):
        super(NotificationSummary, self).__init__()
        self.results = results
        self.subscription_id = subscription_id


class Publisher(Model):
    """Publisher.

    :param _links: Reference Links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.service_hooks.models.ReferenceLinks>`
    :param description: Gets this publisher's localized description.
    :type description: str
    :param id: Gets this publisher's identifier.
    :type id: str
    :param input_descriptors: Publisher-specific inputs
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.service_hooks.models.InputDescriptor>`
    :param name: Gets this publisher's localized name.
    :type name: str
    :param service_instance_type: The service instance type of the first party publisher.
    :type service_instance_type: str
    :param supported_events: Gets this publisher's supported event types.
    :type supported_events: list of :class:`EventTypeDescriptor <azure.devops.v5_1.service_hooks.models.EventTypeDescriptor>`
    :param url: The url for this resource
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'supported_events': {'key': 'supportedEvents', 'type': '[EventTypeDescriptor]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, description=None, id=None, input_descriptors=None, name=None, service_instance_type=None, supported_events=None, url=None):
        super(Publisher, self).__init__()
        self._links = _links
        self.description = description
        self.id = id
        self.input_descriptors = input_descriptors
        self.name = name
        self.service_instance_type = service_instance_type
        self.supported_events = supported_events
        self.url = url


class PublisherEvent(Model):
    """PublisherEvent.

    :param diagnostics: Add key/value pairs which will be stored with a published notification in the SH service DB.  This key/value pairs are for diagnostic purposes only and will have not effect on the delivery of a notificaton.
    :type diagnostics: dict
    :param event: The event being published
    :type event: :class:`Event <azure.devops.v5_1.service_hooks.models.Event>`
    :param is_filtered_event: Gets or sets flag for filtered events
    :type is_filtered_event: bool
    :param notification_data: Additional data that needs to be sent as part of notification to complement the Resource data in the Event
    :type notification_data: dict
    :param other_resource_versions: Gets or sets the array of older supported resource versions.
    :type other_resource_versions: list of :class:`VersionedResource <azure.devops.v5_1.service_hooks.models.VersionedResource>`
    :param publisher_input_filters: Optional publisher-input filters which restricts the set of subscriptions which are triggered by the event
    :type publisher_input_filters: list of :class:`InputFilter <azure.devops.v5_1.service_hooks.models.InputFilter>`
    :param subscription: Gets or sets matchd hooks subscription which caused this event.
    :type subscription: :class:`Subscription <azure.devops.v5_1.service_hooks.models.Subscription>`
    """

    _attribute_map = {
        'diagnostics': {'key': 'diagnostics', 'type': '{str}'},
        'event': {'key': 'event', 'type': 'Event'},
        'is_filtered_event': {'key': 'isFilteredEvent', 'type': 'bool'},
        'notification_data': {'key': 'notificationData', 'type': '{str}'},
        'other_resource_versions': {'key': 'otherResourceVersions', 'type': '[VersionedResource]'},
        'publisher_input_filters': {'key': 'publisherInputFilters', 'type': '[InputFilter]'},
        'subscription': {'key': 'subscription', 'type': 'Subscription'}
    }

    def __init__(self, diagnostics=None, event=None, is_filtered_event=None, notification_data=None, other_resource_versions=None, publisher_input_filters=None, subscription=None):
        super(PublisherEvent, self).__init__()
        self.diagnostics = diagnostics
        self.event = event
        self.is_filtered_event = is_filtered_event
        self.notification_data = notification_data
        self.other_resource_versions = other_resource_versions
        self.publisher_input_filters = publisher_input_filters
        self.subscription = subscription


class PublishersQuery(Model):
    """PublishersQuery.

    :param publisher_ids: Optional list of publisher ids to restrict the results to
    :type publisher_ids: list of str
    :param publisher_inputs: Filter for publisher inputs
    :type publisher_inputs: dict
    :param results: Results from the query
    :type results: list of :class:`Publisher <azure.devops.v5_1.service_hooks.models.Publisher>`
    """

    _attribute_map = {
        'publisher_ids': {'key': 'publisherIds', 'type': '[str]'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'results': {'key': 'results', 'type': '[Publisher]'}
    }

    def __init__(self, publisher_ids=None, publisher_inputs=None, results=None):
        super(PublishersQuery, self).__init__()
        self.publisher_ids = publisher_ids
        self.publisher_inputs = publisher_inputs
        self.results = results


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


class ResourceContainer(Model):
    """ResourceContainer.

    :param base_url: Gets or sets the container's base URL, i.e. the URL of the host (collection, application, or deploument) containing the container resource.
    :type base_url: str
    :param id: Gets or sets the container's specific Id.
    :type id: str
    :param name: Gets or sets the container's name.
    :type name: str
    :param url: Gets or sets the container's REST API URL.
    :type url: str
    """

    _attribute_map = {
        'base_url': {'key': 'baseUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, base_url=None, id=None, name=None, url=None):
        super(ResourceContainer, self).__init__()
        self.base_url = base_url
        self.id = id
        self.name = name
        self.url = url


class SessionToken(Model):
    """SessionToken.

    :param error: The error message in case of error
    :type error: str
    :param token: The access token
    :type token: str
    :param valid_to: The expiration date in UTC
    :type valid_to: datetime
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, error=None, token=None, valid_to=None):
        super(SessionToken, self).__init__()
        self.error = error
        self.token = token
        self.valid_to = valid_to


class Subscription(Model):
    """Subscription.

    :param _links: Reference Links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.service_hooks.models.ReferenceLinks>`
    :param action_description:
    :type action_description: str
    :param consumer_action_id:
    :type consumer_action_id: str
    :param consumer_id:
    :type consumer_id: str
    :param consumer_inputs: Consumer input values
    :type consumer_inputs: dict
    :param created_by:
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.service_hooks.models.IdentityRef>`
    :param created_date:
    :type created_date: datetime
    :param event_description:
    :type event_description: str
    :param event_type:
    :type event_type: str
    :param id:
    :type id: str
    :param modified_by:
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.service_hooks.models.IdentityRef>`
    :param modified_date:
    :type modified_date: datetime
    :param probation_retries:
    :type probation_retries: str
    :param publisher_id:
    :type publisher_id: str
    :param publisher_inputs: Publisher input values
    :type publisher_inputs: dict
    :param resource_version:
    :type resource_version: str
    :param status:
    :type status: object
    :param subscriber:
    :type subscriber: :class:`IdentityRef <azure.devops.v5_1.service_hooks.models.IdentityRef>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'action_description': {'key': 'actionDescription', 'type': 'str'},
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_inputs': {'key': 'consumerInputs', 'type': '{str}'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'event_description': {'key': 'eventDescription', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'probation_retries': {'key': 'probationRetries', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_inputs': {'key': 'publisherInputs', 'type': '{str}'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, action_description=None, consumer_action_id=None, consumer_id=None, consumer_inputs=None, created_by=None, created_date=None, event_description=None, event_type=None, id=None, modified_by=None, modified_date=None, probation_retries=None, publisher_id=None, publisher_inputs=None, resource_version=None, status=None, subscriber=None, url=None):
        super(Subscription, self).__init__()
        self._links = _links
        self.action_description = action_description
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_inputs = consumer_inputs
        self.created_by = created_by
        self.created_date = created_date
        self.event_description = event_description
        self.event_type = event_type
        self.id = id
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.probation_retries = probation_retries
        self.publisher_id = publisher_id
        self.publisher_inputs = publisher_inputs
        self.resource_version = resource_version
        self.status = status
        self.subscriber = subscriber
        self.url = url


class SubscriptionDiagnostics(Model):
    """SubscriptionDiagnostics.

    :param delivery_results:
    :type delivery_results: :class:`SubscriptionTracing <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.SubscriptionTracing>`
    :param delivery_tracing:
    :type delivery_tracing: :class:`SubscriptionTracing <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.SubscriptionTracing>`
    :param evaluation_tracing:
    :type evaluation_tracing: :class:`SubscriptionTracing <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.SubscriptionTracing>`
    """

    _attribute_map = {
        'delivery_results': {'key': 'deliveryResults', 'type': 'SubscriptionTracing'},
        'delivery_tracing': {'key': 'deliveryTracing', 'type': 'SubscriptionTracing'},
        'evaluation_tracing': {'key': 'evaluationTracing', 'type': 'SubscriptionTracing'}
    }

    def __init__(self, delivery_results=None, delivery_tracing=None, evaluation_tracing=None):
        super(SubscriptionDiagnostics, self).__init__()
        self.delivery_results = delivery_results
        self.delivery_tracing = delivery_tracing
        self.evaluation_tracing = evaluation_tracing


class SubscriptionsQuery(Model):
    """SubscriptionsQuery.

    :param consumer_action_id: Optional consumer action id to restrict the results to (null for any)
    :type consumer_action_id: str
    :param consumer_id: Optional consumer id to restrict the results to (null for any)
    :type consumer_id: str
    :param consumer_input_filters: Filter for subscription consumer inputs
    :type consumer_input_filters: list of :class:`InputFilter <azure.devops.v5_1.service_hooks.models.InputFilter>`
    :param event_type: Optional event type id to restrict the results to (null for any)
    :type event_type: str
    :param publisher_id: Optional publisher id to restrict the results to (null for any)
    :type publisher_id: str
    :param publisher_input_filters: Filter for subscription publisher inputs
    :type publisher_input_filters: list of :class:`InputFilter <azure.devops.v5_1.service_hooks.models.InputFilter>`
    :param results: Results from the query
    :type results: list of :class:`Subscription <azure.devops.v5_1.service_hooks.models.Subscription>`
    :param subscriber_id: Optional subscriber filter.
    :type subscriber_id: str
    """

    _attribute_map = {
        'consumer_action_id': {'key': 'consumerActionId', 'type': 'str'},
        'consumer_id': {'key': 'consumerId', 'type': 'str'},
        'consumer_input_filters': {'key': 'consumerInputFilters', 'type': '[InputFilter]'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_input_filters': {'key': 'publisherInputFilters', 'type': '[InputFilter]'},
        'results': {'key': 'results', 'type': '[Subscription]'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'}
    }

    def __init__(self, consumer_action_id=None, consumer_id=None, consumer_input_filters=None, event_type=None, publisher_id=None, publisher_input_filters=None, results=None, subscriber_id=None):
        super(SubscriptionsQuery, self).__init__()
        self.consumer_action_id = consumer_action_id
        self.consumer_id = consumer_id
        self.consumer_input_filters = consumer_input_filters
        self.event_type = event_type
        self.publisher_id = publisher_id
        self.publisher_input_filters = publisher_input_filters
        self.results = results
        self.subscriber_id = subscriber_id


class SubscriptionTracing(Model):
    """SubscriptionTracing.

    :param enabled:
    :type enabled: bool
    :param end_date: Trace until the specified end date.
    :type end_date: datetime
    :param max_traced_entries: The maximum number of result details to trace.
    :type max_traced_entries: int
    :param start_date: The date and time tracing started.
    :type start_date: datetime
    :param traced_entries: Trace until remaining count reaches 0.
    :type traced_entries: int
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'max_traced_entries': {'key': 'maxTracedEntries', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'traced_entries': {'key': 'tracedEntries', 'type': 'int'}
    }

    def __init__(self, enabled=None, end_date=None, max_traced_entries=None, start_date=None, traced_entries=None):
        super(SubscriptionTracing, self).__init__()
        self.enabled = enabled
        self.end_date = end_date
        self.max_traced_entries = max_traced_entries
        self.start_date = start_date
        self.traced_entries = traced_entries


class UpdateSubscripitonDiagnosticsParameters(Model):
    """UpdateSubscripitonDiagnosticsParameters.

    :param delivery_results:
    :type delivery_results: :class:`UpdateSubscripitonTracingParameters <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.UpdateSubscripitonTracingParameters>`
    :param delivery_tracing:
    :type delivery_tracing: :class:`UpdateSubscripitonTracingParameters <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.UpdateSubscripitonTracingParameters>`
    :param evaluation_tracing:
    :type evaluation_tracing: :class:`UpdateSubscripitonTracingParameters <azure.devops.v5_1.microsoft._visual_studio._services._notifications._web_api.models.UpdateSubscripitonTracingParameters>`
    """

    _attribute_map = {
        'delivery_results': {'key': 'deliveryResults', 'type': 'UpdateSubscripitonTracingParameters'},
        'delivery_tracing': {'key': 'deliveryTracing', 'type': 'UpdateSubscripitonTracingParameters'},
        'evaluation_tracing': {'key': 'evaluationTracing', 'type': 'UpdateSubscripitonTracingParameters'}
    }

    def __init__(self, delivery_results=None, delivery_tracing=None, evaluation_tracing=None):
        super(UpdateSubscripitonDiagnosticsParameters, self).__init__()
        self.delivery_results = delivery_results
        self.delivery_tracing = delivery_tracing
        self.evaluation_tracing = evaluation_tracing


class UpdateSubscripitonTracingParameters(Model):
    """UpdateSubscripitonTracingParameters.

    :param enabled:
    :type enabled: bool
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'}
    }

    def __init__(self, enabled=None):
        super(UpdateSubscripitonTracingParameters, self).__init__()
        self.enabled = enabled


class VersionedResource(Model):
    """VersionedResource.

    :param compatible_with: Gets or sets the reference to the compatible version.
    :type compatible_with: str
    :param resource: Gets or sets the resource data.
    :type resource: object
    :param resource_version: Gets or sets the version of the resource data.
    :type resource_version: str
    """

    _attribute_map = {
        'compatible_with': {'key': 'compatibleWith', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'object'},
        'resource_version': {'key': 'resourceVersion', 'type': 'str'}
    }

    def __init__(self, compatible_with=None, resource=None, resource_version=None):
        super(VersionedResource, self).__init__()
        self.compatible_with = compatible_with
        self.resource = resource
        self.resource_version = resource_version


__all__ = [
    'Consumer',
    'ConsumerAction',
    'Event',
    'EventTypeDescriptor',
    'ExternalConfigurationDescriptor',
    'FormattedEventMessage',
    'GraphSubjectBase',
    'IdentityRef',
    'InputDescriptor',
    'InputFilter',
    'InputFilterCondition',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'Notification',
    'NotificationDetails',
    'NotificationResultsSummaryDetail',
    'NotificationsQuery',
    'NotificationSummary',
    'Publisher',
    'PublisherEvent',
    'PublishersQuery',
    'ReferenceLinks',
    'ResourceContainer',
    'SessionToken',
    'Subscription',
    'SubscriptionDiagnostics',
    'SubscriptionsQuery',
    'SubscriptionTracing',
    'UpdateSubscripitonDiagnosticsParameters',
    'UpdateSubscripitonTracingParameters',
    'VersionedResource',
]
