# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BaseSubscriptionFilter(Model):
    """
    :param event_type:
    :type event_type: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, type=None):
        super(BaseSubscriptionFilter, self).__init__()
        self.event_type = event_type
        self.type = type


class BatchNotificationOperation(Model):
    """
    :param notification_operation:
    :type notification_operation: object
    :param notification_query_conditions:
    :type notification_query_conditions: list of :class:`NotificationQueryCondition <azure.devops.v6_0.notification.models.NotificationQueryCondition>`
    """

    _attribute_map = {
        'notification_operation': {'key': 'notificationOperation', 'type': 'object'},
        'notification_query_conditions': {'key': 'notificationQueryConditions', 'type': '[NotificationQueryCondition]'}
    }

    def __init__(self, notification_operation=None, notification_query_conditions=None):
        super(BatchNotificationOperation, self).__init__()
        self.notification_operation = notification_operation
        self.notification_query_conditions = notification_query_conditions


class EventActor(Model):
    """
    Defines an "actor" for an event.

    :param id: Required: This is the identity of the user for the specified role.
    :type id: str
    :param role: Required: The event specific name of a role.
    :type role: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'}
    }

    def __init__(self, id=None, role=None):
        super(EventActor, self).__init__()
        self.id = id
        self.role = role


class EventScope(Model):
    """
    Defines a scope for an event.

    :param id: Required: This is the identity of the scope for the type.
    :type id: str
    :param name: Optional: The display name of the scope
    :type name: str
    :param type: Required: The event specific type of a scope.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(EventScope, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class EventsEvaluationResult(Model):
    """
    Encapsulates events result properties. It defines the total number of events used and the number of matched events.

    :param count: Count of events evaluated.
    :type count: int
    :param matched_count: Count of matched events.
    :type matched_count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'matched_count': {'key': 'matchedCount', 'type': 'int'}
    }

    def __init__(self, count=None, matched_count=None):
        super(EventsEvaluationResult, self).__init__()
        self.count = count
        self.matched_count = matched_count


class EventTransformRequest(Model):
    """
    A transform request specify the properties of a notification event to be transformed.

    :param event_payload: Event payload.
    :type event_payload: str
    :param event_type: Event type.
    :type event_type: str
    :param system_inputs: System inputs.
    :type system_inputs: dict
    """

    _attribute_map = {
        'event_payload': {'key': 'eventPayload', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'system_inputs': {'key': 'systemInputs', 'type': '{str}'}
    }

    def __init__(self, event_payload=None, event_type=None, system_inputs=None):
        super(EventTransformRequest, self).__init__()
        self.event_payload = event_payload
        self.event_type = event_type
        self.system_inputs = system_inputs


class EventTransformResult(Model):
    """
    Result of transforming a notification event.

    :param content: Transformed html content.
    :type content: str
    :param data: Calculated data.
    :type data: object
    :param system_inputs: Calculated system inputs.
    :type system_inputs: dict
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'system_inputs': {'key': 'systemInputs', 'type': '{str}'}
    }

    def __init__(self, content=None, data=None, system_inputs=None):
        super(EventTransformResult, self).__init__()
        self.content = content
        self.data = data
        self.system_inputs = system_inputs


class ExpressionFilterClause(Model):
    """
    Subscription Filter Clause represents a single clause in a subscription filter e.g. If the subscription has the following criteria "Project Name = [Current Project] AND Assigned To = [Me] it will be represented as two Filter Clauses Clause 1: Index = 1, Logical Operator: NULL  , FieldName = 'Project Name', Operator = '=', Value = '[Current Project]' Clause 2: Index = 2, Logical Operator: 'AND' , FieldName = 'Assigned To' , Operator = '=', Value = '[Me]'

    :param field_name:
    :type field_name: str
    :param index: The order in which this clause appeared in the filter query
    :type index: int
    :param logical_operator: Logical Operator 'AND', 'OR' or NULL (only for the first clause in the filter)
    :type logical_operator: str
    :param operator:
    :type operator: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
        'logical_operator': {'key': 'logicalOperator', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, field_name=None, index=None, logical_operator=None, operator=None, value=None):
        super(ExpressionFilterClause, self).__init__()
        self.field_name = field_name
        self.index = index
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value


class ExpressionFilterGroup(Model):
    """
    Represents a hierarchy of SubscritionFilterClauses that have been grouped together through either adding a group in the WebUI or using parethesis in the Subscription condition string

    :param end: The index of the last FilterClause in this group
    :type end: int
    :param level: Level of the group, since groups can be nested for each nested group the level will increase by 1
    :type level: int
    :param start: The index of the first FilterClause in this group
    :type start: int
    """

    _attribute_map = {
        'end': {'key': 'end', 'type': 'int'},
        'level': {'key': 'level', 'type': 'int'},
        'start': {'key': 'start', 'type': 'int'}
    }

    def __init__(self, end=None, level=None, start=None):
        super(ExpressionFilterGroup, self).__init__()
        self.end = end
        self.level = level
        self.start = start


class ExpressionFilterModel(Model):
    """
    :param clauses: Flat list of clauses in this subscription
    :type clauses: list of :class:`ExpressionFilterClause <azure.devops.v6_0.notification.models.ExpressionFilterClause>`
    :param groups: Grouping of clauses in the subscription
    :type groups: list of :class:`ExpressionFilterGroup <azure.devops.v6_0.notification.models.ExpressionFilterGroup>`
    :param max_group_level: Max depth of the Subscription tree
    :type max_group_level: int
    """

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[ExpressionFilterClause]'},
        'groups': {'key': 'groups', 'type': '[ExpressionFilterGroup]'},
        'max_group_level': {'key': 'maxGroupLevel', 'type': 'int'}
    }

    def __init__(self, clauses=None, groups=None, max_group_level=None):
        super(ExpressionFilterModel, self).__init__()
        self.clauses = clauses
        self.groups = groups
        self.max_group_level = max_group_level


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class INotificationDiagnosticLog(Model):
    """
    Abstraction interface for the diagnostic log.  Primarily for deserialization.

    :param activity_id: Identifier used for correlating to other diagnostics that may have been recorded elsewhere.
    :type activity_id: str
    :param description: Description of what subscription or notification job is being logged.
    :type description: str
    :param end_time: Time the log ended.
    :type end_time: datetime
    :param id: Unique instance identifier.
    :type id: str
    :param log_type: Type of information being logged.
    :type log_type: str
    :param messages: List of log messages.
    :type messages: list of :class:`NotificationDiagnosticLogMessage <azure.devops.v6_0.notification.models.NotificationDiagnosticLogMessage>`
    :param properties: Dictionary of log properties and settings for the job.
    :type properties: dict
    :param source: This identifier depends on the logType.  For notification jobs, this will be the job Id. For subscription tracing, this will be a special root Guid with the subscription Id encoded.
    :type source: str
    :param start_time: Time the log started.
    :type start_time: datetime
    """

    _attribute_map = {
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'log_type': {'key': 'logType', 'type': 'str'},
        'messages': {'key': 'messages', 'type': '[NotificationDiagnosticLogMessage]'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'source': {'key': 'source', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'}
    }

    def __init__(self, activity_id=None, description=None, end_time=None, id=None, log_type=None, messages=None, properties=None, source=None, start_time=None):
        super(INotificationDiagnosticLog, self).__init__()
        self.activity_id = activity_id
        self.description = description
        self.end_time = end_time
        self.id = id
        self.log_type = log_type
        self.messages = messages
        self.properties = properties
        self.source = source
        self.start_time = start_time


class InputValue(Model):
    """
    Information about a single value for an input

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
    """
    Information about the possible/allowed values for a given subscription input

    :param default_value: The default value to use for this input
    :type default_value: str
    :param error: Errors encountered while computing dynamic values.
    :type error: :class:`InputValuesError <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.InputValue>`
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
    """
    Error information related to a subscription input value.

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
    """
    :param current_values:
    :type current_values: dict
    :param input_values: The input values to return on input, and the result from the consumer on output.
    :type input_values: list of :class:`InputValues <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.InputValues>`
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


class ISubscriptionChannel(Model):
    """
    :param type:
    :type type: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, type=None):
        super(ISubscriptionChannel, self).__init__()
        self.type = type


class ISubscriptionFilter(Model):
    """
    :param event_type:
    :type event_type: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, type=None):
        super(ISubscriptionFilter, self).__init__()
        self.event_type = event_type
        self.type = type


class NotificationAdminSettings(Model):
    """
    :param default_group_delivery_preference: The default group delivery preference for groups in this collection
    :type default_group_delivery_preference: object
    """

    _attribute_map = {
        'default_group_delivery_preference': {'key': 'defaultGroupDeliveryPreference', 'type': 'object'}
    }

    def __init__(self, default_group_delivery_preference=None):
        super(NotificationAdminSettings, self).__init__()
        self.default_group_delivery_preference = default_group_delivery_preference


class NotificationAdminSettingsUpdateParameters(Model):
    """
    :param default_group_delivery_preference:
    :type default_group_delivery_preference: object
    """

    _attribute_map = {
        'default_group_delivery_preference': {'key': 'defaultGroupDeliveryPreference', 'type': 'object'}
    }

    def __init__(self, default_group_delivery_preference=None):
        super(NotificationAdminSettingsUpdateParameters, self).__init__()
        self.default_group_delivery_preference = default_group_delivery_preference


class NotificationDiagnosticLogMessage(Model):
    """
    :param level: Corresponds to .Net TraceLevel enumeration
    :type level: int
    :param message:
    :type message: str
    :param time:
    :type time: object
    """

    _attribute_map = {
        'level': {'key': 'level', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'object'}
    }

    def __init__(self, level=None, message=None, time=None):
        super(NotificationDiagnosticLogMessage, self).__init__()
        self.level = level
        self.message = message
        self.time = time


class NotificationEventField(Model):
    """
    Encapsulates the properties of a filterable field. A filterable field is a field in an event that can used to filter notifications for a certain event type.

    :param field_type: Gets or sets the type of this field.
    :type field_type: :class:`NotificationEventFieldType <azure.devops.v6_0.notification.models.NotificationEventFieldType>`
    :param id: Gets or sets the unique identifier of this field.
    :type id: str
    :param name: Gets or sets the name of this field.
    :type name: str
    :param path: Gets or sets the path to the field in the event object. This path can be either Json Path or XPath, depending on if the event will be serialized into Json or XML
    :type path: str
    :param supported_scopes: Gets or sets the scopes that this field supports. If not specified then the event type scopes apply.
    :type supported_scopes: list of str
    """

    _attribute_map = {
        'field_type': {'key': 'fieldType', 'type': 'NotificationEventFieldType'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'}
    }

    def __init__(self, field_type=None, id=None, name=None, path=None, supported_scopes=None):
        super(NotificationEventField, self).__init__()
        self.field_type = field_type
        self.id = id
        self.name = name
        self.path = path
        self.supported_scopes = supported_scopes


class NotificationEventFieldOperator(Model):
    """
    Encapsulates the properties of a field type. It includes a unique id for the operator and a localized string for display name

    :param display_name: Gets or sets the display name of an operator
    :type display_name: str
    :param id: Gets or sets the id of an operator
    :type id: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None):
        super(NotificationEventFieldOperator, self).__init__()
        self.display_name = display_name
        self.id = id


class NotificationEventFieldType(Model):
    """
    Encapsulates the properties of a field type. It describes the data type of a field, the operators it support and how to populate it in the UI

    :param id: Gets or sets the unique identifier of this field type.
    :type id: str
    :param operator_constraints:
    :type operator_constraints: list of :class:`OperatorConstraint <azure.devops.v6_0.notification.models.OperatorConstraint>`
    :param operators: Gets or sets the list of operators that this type supports.
    :type operators: list of :class:`NotificationEventFieldOperator <azure.devops.v6_0.notification.models.NotificationEventFieldOperator>`
    :param subscription_field_type:
    :type subscription_field_type: object
    :param value: Gets or sets the value definition of this field like the getValuesMethod and template to display in the UI
    :type value: :class:`ValueDefinition <azure.devops.v6_0.notification.models.ValueDefinition>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'operator_constraints': {'key': 'operatorConstraints', 'type': '[OperatorConstraint]'},
        'operators': {'key': 'operators', 'type': '[NotificationEventFieldOperator]'},
        'subscription_field_type': {'key': 'subscriptionFieldType', 'type': 'object'},
        'value': {'key': 'value', 'type': 'ValueDefinition'}
    }

    def __init__(self, id=None, operator_constraints=None, operators=None, subscription_field_type=None, value=None):
        super(NotificationEventFieldType, self).__init__()
        self.id = id
        self.operator_constraints = operator_constraints
        self.operators = operators
        self.subscription_field_type = subscription_field_type
        self.value = value


class NotificationEventPublisher(Model):
    """
    Encapsulates the properties of a notification event publisher.

    :param id:
    :type id: str
    :param subscription_management_info:
    :type subscription_management_info: :class:`SubscriptionManagement <azure.devops.v6_0.notification.models.SubscriptionManagement>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_management_info': {'key': 'subscriptionManagementInfo', 'type': 'SubscriptionManagement'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, subscription_management_info=None, url=None):
        super(NotificationEventPublisher, self).__init__()
        self.id = id
        self.subscription_management_info = subscription_management_info
        self.url = url


class NotificationEventRole(Model):
    """
    Encapsulates the properties of an event role.  An event Role is used for role based subscription for example for a buildCompletedEvent, one role is request by field

    :param id: Gets or sets an Id for that role, this id is used by the event.
    :type id: str
    :param name: Gets or sets the Name for that role, this name is used for UI display.
    :type name: str
    :param supports_groups: Gets or sets whether this role can be a group or just an individual user
    :type supports_groups: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'supports_groups': {'key': 'supportsGroups', 'type': 'bool'}
    }

    def __init__(self, id=None, name=None, supports_groups=None):
        super(NotificationEventRole, self).__init__()
        self.id = id
        self.name = name
        self.supports_groups = supports_groups


class NotificationEventType(Model):
    """
    Encapsulates the properties of an event type. It defines the fields, that can be used for filtering, for that event type.

    :param category:
    :type category: :class:`NotificationEventTypeCategory <azure.devops.v6_0.notification.models.NotificationEventTypeCategory>`
    :param color: Gets or sets the color representing this event type. Example: rgb(128,245,211) or #fafafa
    :type color: str
    :param custom_subscriptions_allowed:
    :type custom_subscriptions_allowed: bool
    :param event_publisher:
    :type event_publisher: :class:`NotificationEventPublisher <azure.devops.v6_0.notification.models.NotificationEventPublisher>`
    :param fields:
    :type fields: dict
    :param has_initiator:
    :type has_initiator: bool
    :param icon: Gets or sets the icon representing this event type. Can be a URL or a CSS class. Example: css://some-css-class
    :type icon: str
    :param id: Gets or sets the unique identifier of this event definition.
    :type id: str
    :param name: Gets or sets the name of this event definition.
    :type name: str
    :param roles:
    :type roles: list of :class:`NotificationEventRole <azure.devops.v6_0.notification.models.NotificationEventRole>`
    :param supported_scopes: Gets or sets the scopes that this event type supports
    :type supported_scopes: list of str
    :param url: Gets or sets the rest end point to get this event type details (fields, fields types)
    :type url: str
    """

    _attribute_map = {
        'category': {'key': 'category', 'type': 'NotificationEventTypeCategory'},
        'color': {'key': 'color', 'type': 'str'},
        'custom_subscriptions_allowed': {'key': 'customSubscriptionsAllowed', 'type': 'bool'},
        'event_publisher': {'key': 'eventPublisher', 'type': 'NotificationEventPublisher'},
        'fields': {'key': 'fields', 'type': '{NotificationEventField}'},
        'has_initiator': {'key': 'hasInitiator', 'type': 'bool'},
        'icon': {'key': 'icon', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[NotificationEventRole]'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, category=None, color=None, custom_subscriptions_allowed=None, event_publisher=None, fields=None, has_initiator=None, icon=None, id=None, name=None, roles=None, supported_scopes=None, url=None):
        super(NotificationEventType, self).__init__()
        self.category = category
        self.color = color
        self.custom_subscriptions_allowed = custom_subscriptions_allowed
        self.event_publisher = event_publisher
        self.fields = fields
        self.has_initiator = has_initiator
        self.icon = icon
        self.id = id
        self.name = name
        self.roles = roles
        self.supported_scopes = supported_scopes
        self.url = url


class NotificationEventTypeCategory(Model):
    """
    Encapsulates the properties of a category. A category will be used by the UI to group event types

    :param id: Gets or sets the unique identifier of this category.
    :type id: str
    :param name: Gets or sets the friendly name of this category.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(NotificationEventTypeCategory, self).__init__()
        self.id = id
        self.name = name


class NotificationQueryCondition(Model):
    """
    :param event_initiator:
    :type event_initiator: str
    :param event_type:
    :type event_type: str
    :param subscriber:
    :type subscriber: str
    :param subscription_id:
    :type subscription_id: str
    """

    _attribute_map = {
        'event_initiator': {'key': 'eventInitiator', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'subscriber': {'key': 'subscriber', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, event_initiator=None, event_type=None, subscriber=None, subscription_id=None):
        super(NotificationQueryCondition, self).__init__()
        self.event_initiator = event_initiator
        self.event_type = event_type
        self.subscriber = subscriber
        self.subscription_id = subscription_id


class NotificationReason(Model):
    """
    :param notification_reason_type:
    :type notification_reason_type: object
    :param target_identities:
    :type target_identities: list of :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    """

    _attribute_map = {
        'notification_reason_type': {'key': 'notificationReasonType', 'type': 'object'},
        'target_identities': {'key': 'targetIdentities', 'type': '[IdentityRef]'}
    }

    def __init__(self, notification_reason_type=None, target_identities=None):
        super(NotificationReason, self).__init__()
        self.notification_reason_type = notification_reason_type
        self.target_identities = target_identities


class NotificationsEvaluationResult(Model):
    """
    Encapsulates notifications result properties. It defines the number of notifications and the recipients of notifications.

    :param count: Count of generated notifications
    :type count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'}
    }

    def __init__(self, count=None):
        super(NotificationsEvaluationResult, self).__init__()
        self.count = count


class NotificationStatistic(Model):
    """
    :param date:
    :type date: datetime
    :param hit_count:
    :type hit_count: int
    :param path:
    :type path: str
    :param type:
    :type type: object
    :param user:
    :type user: :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'hit_count': {'key': 'hitCount', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'user': {'key': 'user', 'type': 'IdentityRef'}
    }

    def __init__(self, date=None, hit_count=None, path=None, type=None, user=None):
        super(NotificationStatistic, self).__init__()
        self.date = date
        self.hit_count = hit_count
        self.path = path
        self.type = type
        self.user = user


class NotificationStatisticsQuery(Model):
    """
    :param conditions:
    :type conditions: list of :class:`NotificationStatisticsQueryConditions <azure.devops.v6_0.notification.models.NotificationStatisticsQueryConditions>`
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[NotificationStatisticsQueryConditions]'}
    }

    def __init__(self, conditions=None):
        super(NotificationStatisticsQuery, self).__init__()
        self.conditions = conditions


class NotificationStatisticsQueryConditions(Model):
    """
    :param end_date:
    :type end_date: datetime
    :param hit_count_minimum:
    :type hit_count_minimum: int
    :param path:
    :type path: str
    :param start_date:
    :type start_date: datetime
    :param type:
    :type type: object
    :param user:
    :type user: :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    """

    _attribute_map = {
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'hit_count_minimum': {'key': 'hitCountMinimum', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'object'},
        'user': {'key': 'user', 'type': 'IdentityRef'}
    }

    def __init__(self, end_date=None, hit_count_minimum=None, path=None, start_date=None, type=None, user=None):
        super(NotificationStatisticsQueryConditions, self).__init__()
        self.end_date = end_date
        self.hit_count_minimum = hit_count_minimum
        self.path = path
        self.start_date = start_date
        self.type = type
        self.user = user


class NotificationSubscriber(Model):
    """
    A subscriber is a user or group that has the potential to receive notifications.

    :param delivery_preference: Indicates how the subscriber should be notified by default.
    :type delivery_preference: object
    :param flags:
    :type flags: object
    :param id: Identifier of the subscriber.
    :type id: str
    :param preferred_email_address: Preferred email address of the subscriber. A null or empty value indicates no preferred email address has been set.
    :type preferred_email_address: str
    """

    _attribute_map = {
        'delivery_preference': {'key': 'deliveryPreference', 'type': 'object'},
        'flags': {'key': 'flags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'preferred_email_address': {'key': 'preferredEmailAddress', 'type': 'str'}
    }

    def __init__(self, delivery_preference=None, flags=None, id=None, preferred_email_address=None):
        super(NotificationSubscriber, self).__init__()
        self.delivery_preference = delivery_preference
        self.flags = flags
        self.id = id
        self.preferred_email_address = preferred_email_address


class NotificationSubscriberUpdateParameters(Model):
    """
    Updates to a subscriber. Typically used to change (or set) a preferred email address or default delivery preference.

    :param delivery_preference: New delivery preference for the subscriber (indicates how the subscriber should be notified).
    :type delivery_preference: object
    :param preferred_email_address: New preferred email address for the subscriber. Specify an empty string to clear the current address.
    :type preferred_email_address: str
    """

    _attribute_map = {
        'delivery_preference': {'key': 'deliveryPreference', 'type': 'object'},
        'preferred_email_address': {'key': 'preferredEmailAddress', 'type': 'str'}
    }

    def __init__(self, delivery_preference=None, preferred_email_address=None):
        super(NotificationSubscriberUpdateParameters, self).__init__()
        self.delivery_preference = delivery_preference
        self.preferred_email_address = preferred_email_address


class NotificationSubscription(Model):
    """
    A subscription defines criteria for matching events and how the subscription's subscriber should be notified about those events.

    :param _links: Links to related resources, APIs, and views for the subscription.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.notification.models.ReferenceLinks>`
    :param admin_settings: Admin-managed settings for the subscription. Only applies when the subscriber is a group.
    :type admin_settings: :class:`SubscriptionAdminSettings <azure.devops.v6_0.notification.models.SubscriptionAdminSettings>`
    :param channel: Channel for delivering notifications triggered by the subscription.
    :type channel: :class:`ISubscriptionChannel <azure.devops.v6_0.notification.models.ISubscriptionChannel>`
    :param description: Description of the subscription. Typically describes filter criteria which helps identity the subscription.
    :type description: str
    :param diagnostics: Diagnostics for this subscription.
    :type diagnostics: :class:`SubscriptionDiagnostics <azure.devops.v6_0.notification.models.SubscriptionDiagnostics>`
    :param extended_properties: Any extra properties like detailed description for different contexts, user/group contexts
    :type extended_properties: dict
    :param filter: Matching criteria for the subscription. ExpressionFilter
    :type filter: :class:`ISubscriptionFilter <azure.devops.v6_0.notification.models.ISubscriptionFilter>`
    :param flags: Read-only indicators that further describe the subscription.
    :type flags: object
    :param id: Subscription identifier.
    :type id: str
    :param last_modified_by: User that last modified (or created) the subscription.
    :type last_modified_by: :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    :param modified_date: Date when the subscription was last modified. If the subscription has not been updated since it was created, this value will indicate when the subscription was created.
    :type modified_date: datetime
    :param permissions: The permissions the user have for this subscriptions.
    :type permissions: object
    :param scope: The container in which events must be published from in order to be matched by the subscription. If empty, the scope is the current host (typically an account or project collection). For example, a subscription scoped to project A will not produce notifications for events published from project B.
    :type scope: :class:`SubscriptionScope <azure.devops.v6_0.notification.models.SubscriptionScope>`
    :param status: Status of the subscription. Typically indicates whether the subscription is enabled or not.
    :type status: object
    :param status_message: Message that provides more details about the status of the subscription.
    :type status_message: str
    :param subscriber: User or group that will receive notifications for events matching the subscription's filter criteria.
    :type subscriber: :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    :param url: REST API URL of the subscriotion.
    :type url: str
    :param user_settings: User-managed settings for the subscription. Only applies when the subscriber is a group. Typically used to indicate whether the calling user is opted in or out of a group subscription.
    :type user_settings: :class:`SubscriptionUserSettings <azure.devops.v6_0.notification.models.SubscriptionUserSettings>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'admin_settings': {'key': 'adminSettings', 'type': 'SubscriptionAdminSettings'},
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'diagnostics': {'key': 'diagnostics', 'type': 'SubscriptionDiagnostics'},
        'extended_properties': {'key': 'extendedProperties', 'type': '{str}'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'flags': {'key': 'flags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'permissions': {'key': 'permissions', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'user_settings': {'key': 'userSettings', 'type': 'SubscriptionUserSettings'}
    }

    def __init__(self, _links=None, admin_settings=None, channel=None, description=None, diagnostics=None, extended_properties=None, filter=None, flags=None, id=None, last_modified_by=None, modified_date=None, permissions=None, scope=None, status=None, status_message=None, subscriber=None, url=None, user_settings=None):
        super(NotificationSubscription, self).__init__()
        self._links = _links
        self.admin_settings = admin_settings
        self.channel = channel
        self.description = description
        self.diagnostics = diagnostics
        self.extended_properties = extended_properties
        self.filter = filter
        self.flags = flags
        self.id = id
        self.last_modified_by = last_modified_by
        self.modified_date = modified_date
        self.permissions = permissions
        self.scope = scope
        self.status = status
        self.status_message = status_message
        self.subscriber = subscriber
        self.url = url
        self.user_settings = user_settings


class NotificationSubscriptionCreateParameters(Model):
    """
    Parameters for creating a new subscription. A subscription defines criteria for matching events and how the subscription's subscriber should be notified about those events.

    :param channel: Channel for delivering notifications triggered by the new subscription.
    :type channel: :class:`ISubscriptionChannel <azure.devops.v6_0.notification.models.ISubscriptionChannel>`
    :param description: Brief description for the new subscription. Typically describes filter criteria which helps identity the subscription.
    :type description: str
    :param filter: Matching criteria for the new subscription. ExpressionFilter
    :type filter: :class:`ISubscriptionFilter <azure.devops.v6_0.notification.models.ISubscriptionFilter>`
    :param scope: The container in which events must be published from in order to be matched by the new subscription. If not specified, defaults to the current host (typically an account or project collection). For example, a subscription scoped to project A will not produce notifications for events published from project B.
    :type scope: :class:`SubscriptionScope <azure.devops.v6_0.notification.models.SubscriptionScope>`
    :param subscriber: User or group that will receive notifications for events matching the subscription's filter criteria. If not specified, defaults to the calling user.
    :type subscriber: :class:`IdentityRef <azure.devops.v6_0.notification.models.IdentityRef>`
    """

    _attribute_map = {
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'subscriber': {'key': 'subscriber', 'type': 'IdentityRef'}
    }

    def __init__(self, channel=None, description=None, filter=None, scope=None, subscriber=None):
        super(NotificationSubscriptionCreateParameters, self).__init__()
        self.channel = channel
        self.description = description
        self.filter = filter
        self.scope = scope
        self.subscriber = subscriber


class NotificationSubscriptionTemplate(Model):
    """
    :param description:
    :type description: str
    :param filter:
    :type filter: :class:`ISubscriptionFilter <azure.devops.v6_0.notification.models.ISubscriptionFilter>`
    :param id:
    :type id: str
    :param notification_event_information:
    :type notification_event_information: :class:`NotificationEventType <azure.devops.v6_0.notification.models.NotificationEventType>`
    :param type:
    :type type: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'id': {'key': 'id', 'type': 'str'},
        'notification_event_information': {'key': 'notificationEventInformation', 'type': 'NotificationEventType'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, filter=None, id=None, notification_event_information=None, type=None):
        super(NotificationSubscriptionTemplate, self).__init__()
        self.description = description
        self.filter = filter
        self.id = id
        self.notification_event_information = notification_event_information
        self.type = type


class NotificationSubscriptionUpdateParameters(Model):
    """
    Parameters for updating an existing subscription. A subscription defines criteria for matching events and how the subscription's subscriber should be notified about those events. Note: only the fields to be updated should be set.

    :param admin_settings: Admin-managed settings for the subscription. Only applies to subscriptions where the subscriber is a group.
    :type admin_settings: :class:`SubscriptionAdminSettings <azure.devops.v6_0.notification.models.SubscriptionAdminSettings>`
    :param channel: Channel for delivering notifications triggered by the subscription.
    :type channel: :class:`ISubscriptionChannel <azure.devops.v6_0.notification.models.ISubscriptionChannel>`
    :param description: Updated description for the subscription. Typically describes filter criteria which helps identity the subscription.
    :type description: str
    :param filter: Matching criteria for the subscription. ExpressionFilter
    :type filter: :class:`ISubscriptionFilter <azure.devops.v6_0.notification.models.ISubscriptionFilter>`
    :param scope: The container in which events must be published from in order to be matched by the new subscription. If not specified, defaults to the current host (typically the current account or project collection). For example, a subscription scoped to project A will not produce notifications for events published from project B.
    :type scope: :class:`SubscriptionScope <azure.devops.v6_0.notification.models.SubscriptionScope>`
    :param status: Updated status for the subscription. Typically used to enable or disable a subscription.
    :type status: object
    :param status_message: Optional message that provides more details about the updated status.
    :type status_message: str
    :param user_settings: User-managed settings for the subscription. Only applies to subscriptions where the subscriber is a group. Typically used to opt-in or opt-out a user from a group subscription.
    :type user_settings: :class:`SubscriptionUserSettings <azure.devops.v6_0.notification.models.SubscriptionUserSettings>`
    """

    _attribute_map = {
        'admin_settings': {'key': 'adminSettings', 'type': 'SubscriptionAdminSettings'},
        'channel': {'key': 'channel', 'type': 'ISubscriptionChannel'},
        'description': {'key': 'description', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'scope': {'key': 'scope', 'type': 'SubscriptionScope'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'user_settings': {'key': 'userSettings', 'type': 'SubscriptionUserSettings'}
    }

    def __init__(self, admin_settings=None, channel=None, description=None, filter=None, scope=None, status=None, status_message=None, user_settings=None):
        super(NotificationSubscriptionUpdateParameters, self).__init__()
        self.admin_settings = admin_settings
        self.channel = channel
        self.description = description
        self.filter = filter
        self.scope = scope
        self.status = status
        self.status_message = status_message
        self.user_settings = user_settings


class OperatorConstraint(Model):
    """
    Encapsulates the properties of an operator constraint. An operator constraint defines if some operator is available only for specific scope like a project scope.

    :param operator:
    :type operator: str
    :param supported_scopes: Gets or sets the list of scopes that this type supports.
    :type supported_scopes: list of str
    """

    _attribute_map = {
        'operator': {'key': 'operator', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[str]'}
    }

    def __init__(self, operator=None, supported_scopes=None):
        super(OperatorConstraint, self).__init__()
        self.operator = operator
        self.supported_scopes = supported_scopes


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class SubscriptionAdminSettings(Model):
    """
    Admin-managed settings for a group subscription.

    :param block_user_opt_out: If true, members of the group subscribed to the associated subscription cannot opt (choose not to get notified)
    :type block_user_opt_out: bool
    """

    _attribute_map = {
        'block_user_opt_out': {'key': 'blockUserOptOut', 'type': 'bool'}
    }

    def __init__(self, block_user_opt_out=None):
        super(SubscriptionAdminSettings, self).__init__()
        self.block_user_opt_out = block_user_opt_out


class SubscriptionChannelWithAddress(Model):
    """
    :param address:
    :type address: str
    :param type:
    :type type: str
    :param use_custom_address:
    :type use_custom_address: bool
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'use_custom_address': {'key': 'useCustomAddress', 'type': 'bool'}
    }

    def __init__(self, address=None, type=None, use_custom_address=None):
        super(SubscriptionChannelWithAddress, self).__init__()
        self.address = address
        self.type = type
        self.use_custom_address = use_custom_address


class SubscriptionDiagnostics(Model):
    """
    Contains all the diagnostics settings for a subscription.

    :param delivery_results: Diagnostics settings for retaining delivery results.  Used for Service Hooks subscriptions.
    :type delivery_results: :class:`SubscriptionTracing <azure.devops.v6_0.notification.models.SubscriptionTracing>`
    :param delivery_tracing: Diagnostics settings for troubleshooting notification delivery.
    :type delivery_tracing: :class:`SubscriptionTracing <azure.devops.v6_0.notification.models.SubscriptionTracing>`
    :param evaluation_tracing: Diagnostics settings for troubleshooting event matching.
    :type evaluation_tracing: :class:`SubscriptionTracing <azure.devops.v6_0.notification.models.SubscriptionTracing>`
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


class SubscriptionEvaluationRequest(Model):
    """
    Encapsulates the properties of a SubscriptionEvaluationRequest. It defines the subscription to be evaluated and time interval for events used in evaluation.

    :param min_events_created_date: The min created date for the events used for matching in UTC. Use all events created since this date
    :type min_events_created_date: datetime
    :param subscription_create_parameters: User or group that will receive notifications for events matching the subscription's filter criteria. If not specified, defaults to the calling user.
    :type subscription_create_parameters: :class:`NotificationSubscriptionCreateParameters <azure.devops.v6_0.notification.models.NotificationSubscriptionCreateParameters>`
    """

    _attribute_map = {
        'min_events_created_date': {'key': 'minEventsCreatedDate', 'type': 'iso-8601'},
        'subscription_create_parameters': {'key': 'subscriptionCreateParameters', 'type': 'NotificationSubscriptionCreateParameters'}
    }

    def __init__(self, min_events_created_date=None, subscription_create_parameters=None):
        super(SubscriptionEvaluationRequest, self).__init__()
        self.min_events_created_date = min_events_created_date
        self.subscription_create_parameters = subscription_create_parameters


class SubscriptionEvaluationResult(Model):
    """
    Encapsulates the subscription evaluation results. It defines the Date Interval that was used, number of events evaluated and events and notifications results

    :param evaluation_job_status: Subscription evaluation job status
    :type evaluation_job_status: object
    :param events: Subscription evaluation events results.
    :type events: :class:`EventsEvaluationResult <azure.devops.v6_0.notification.models.EventsEvaluationResult>`
    :param id: The requestId which is the subscription evaluation jobId
    :type id: str
    :param notifications: Subscription evaluation  notification results.
    :type notifications: :class:`NotificationsEvaluationResult <azure.devops.v6_0.notification.models.NotificationsEvaluationResult>`
    """

    _attribute_map = {
        'evaluation_job_status': {'key': 'evaluationJobStatus', 'type': 'object'},
        'events': {'key': 'events', 'type': 'EventsEvaluationResult'},
        'id': {'key': 'id', 'type': 'str'},
        'notifications': {'key': 'notifications', 'type': 'NotificationsEvaluationResult'}
    }

    def __init__(self, evaluation_job_status=None, events=None, id=None, notifications=None):
        super(SubscriptionEvaluationResult, self).__init__()
        self.evaluation_job_status = evaluation_job_status
        self.events = events
        self.id = id
        self.notifications = notifications


class SubscriptionEvaluationSettings(Model):
    """
    Encapsulates the subscription evaluation settings needed for the UI

    :param enabled: Indicates whether subscription evaluation before saving is enabled or not
    :type enabled: bool
    :param interval: Time interval to check on subscription evaluation job in seconds
    :type interval: int
    :param threshold: Threshold on the number of notifications for considering a subscription too noisy
    :type threshold: int
    :param time_out: Time out for the subscription evaluation check in seconds
    :type time_out: int
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'interval': {'key': 'interval', 'type': 'int'},
        'threshold': {'key': 'threshold', 'type': 'int'},
        'time_out': {'key': 'timeOut', 'type': 'int'}
    }

    def __init__(self, enabled=None, interval=None, threshold=None, time_out=None):
        super(SubscriptionEvaluationSettings, self).__init__()
        self.enabled = enabled
        self.interval = interval
        self.threshold = threshold
        self.time_out = time_out


class SubscriptionManagement(Model):
    """
    Encapsulates the properties needed to manage subscriptions, opt in and out of subscriptions.

    :param service_instance_type:
    :type service_instance_type: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, service_instance_type=None, url=None):
        super(SubscriptionManagement, self).__init__()
        self.service_instance_type = service_instance_type
        self.url = url


class SubscriptionQuery(Model):
    """
    Notification subscriptions query input.

    :param conditions: One or more conditions to query on. If more than 2 conditions are specified, the combined results of each condition is returned (i.e. conditions are logically OR'ed).
    :type conditions: list of :class:`SubscriptionQueryCondition <azure.devops.v6_0.notification.models.SubscriptionQueryCondition>`
    :param query_flags: Flags the refine the types of subscriptions that will be returned from the query.
    :type query_flags: object
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[SubscriptionQueryCondition]'},
        'query_flags': {'key': 'queryFlags', 'type': 'object'}
    }

    def __init__(self, conditions=None, query_flags=None):
        super(SubscriptionQuery, self).__init__()
        self.conditions = conditions
        self.query_flags = query_flags


class SubscriptionQueryCondition(Model):
    """
    Conditions a subscription must match to qualify for the query result set. Not all fields are required. A subscription must match all conditions specified in order to qualify for the result set.

    :param filter: Filter conditions that matching subscriptions must have. Typically only the filter's type and event type are used for matching.
    :type filter: :class:`ISubscriptionFilter <azure.devops.v6_0.notification.models.ISubscriptionFilter>`
    :param flags: Flags to specify the the type subscriptions to query for.
    :type flags: object
    :param scope: Scope that matching subscriptions must have.
    :type scope: str
    :param subscriber_id: ID of the subscriber (user or group) that matching subscriptions must be subscribed to.
    :type subscriber_id: str
    :param subscription_id: ID of the subscription to query for.
    :type subscription_id: str
    """

    _attribute_map = {
        'filter': {'key': 'filter', 'type': 'ISubscriptionFilter'},
        'flags': {'key': 'flags', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'subscriber_id': {'key': 'subscriberId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'}
    }

    def __init__(self, filter=None, flags=None, scope=None, subscriber_id=None, subscription_id=None):
        super(SubscriptionQueryCondition, self).__init__()
        self.filter = filter
        self.flags = flags
        self.scope = scope
        self.subscriber_id = subscriber_id
        self.subscription_id = subscription_id


class SubscriptionScope(EventScope):
    """
    A resource, typically an account or project, in which events are published from.

    :param id: Required: This is the identity of the scope for the type.
    :type id: str
    :param name: Optional: The display name of the scope
    :type name: str
    :param type: Required: The event specific type of a scope.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None):
        super(SubscriptionScope, self).__init__(id=id, name=name, type=type)


class SubscriptionTracing(Model):
    """
    Data controlling a single diagnostic setting for a subscription.

    :param enabled: Indicates whether the diagnostic tracing is enabled or not.
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


class SubscriptionUserSettings(Model):
    """
    User-managed settings for a group subscription.

    :param opted_out: Indicates whether the user will receive notifications for the associated group subscription.
    :type opted_out: bool
    """

    _attribute_map = {
        'opted_out': {'key': 'optedOut', 'type': 'bool'}
    }

    def __init__(self, opted_out=None):
        super(SubscriptionUserSettings, self).__init__()
        self.opted_out = opted_out


class UpdateSubscripitonDiagnosticsParameters(Model):
    """
    Parameters to update diagnostics settings for a subscription.

    :param delivery_results: Diagnostics settings for retaining delivery results.  Used for Service Hooks subscriptions.
    :type delivery_results: :class:`UpdateSubscripitonTracingParameters <azure.devops.v6_0.notification.models.UpdateSubscripitonTracingParameters>`
    :param delivery_tracing: Diagnostics settings for troubleshooting notification delivery.
    :type delivery_tracing: :class:`UpdateSubscripitonTracingParameters <azure.devops.v6_0.notification.models.UpdateSubscripitonTracingParameters>`
    :param evaluation_tracing: Diagnostics settings for troubleshooting event matching.
    :type evaluation_tracing: :class:`UpdateSubscripitonTracingParameters <azure.devops.v6_0.notification.models.UpdateSubscripitonTracingParameters>`
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
    """
    Parameters to update a specific diagnostic setting.

    :param enabled: Indicates whether to enable to disable the diagnostic tracing.
    :type enabled: bool
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'}
    }

    def __init__(self, enabled=None):
        super(UpdateSubscripitonTracingParameters, self).__init__()
        self.enabled = enabled


class ValueDefinition(Model):
    """
    Encapsulates the properties of a field value definition. It has the information needed to retrieve the list of possible values for a certain field and how to handle that field values in the UI. This information includes what type of object this value represents, which property to use for UI display and which property to use for saving the subscription

    :param data_source: Gets or sets the data source.
    :type data_source: list of :class:`InputValue <azure.devops.v6_0.notification.models.InputValue>`
    :param end_point: Gets or sets the rest end point.
    :type end_point: str
    :param result_template: Gets or sets the result template.
    :type result_template: str
    """

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': '[InputValue]'},
        'end_point': {'key': 'endPoint', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'}
    }

    def __init__(self, data_source=None, end_point=None, result_template=None):
        super(ValueDefinition, self).__init__()
        self.data_source = data_source
        self.end_point = end_point
        self.result_template = result_template


class VssNotificationEvent(Model):
    """
    This is the type used for firing notifications intended for the subsystem in the Notifications SDK. For components that can't take a dependency on the Notifications SDK directly, they can use ITeamFoundationEventService.PublishNotification and the Notifications SDK ISubscriber implementation will get it.

    :param actors: Optional: A list of actors which are additional identities with corresponding roles that are relevant to the event.
    :type actors: list of :class:`EventActor <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.EventActor>`
    :param artifact_uris: Optional: A list of artifacts referenced or impacted by this event.
    :type artifact_uris: list of str
    :param data: Required: The event payload.  If Data is a string, it must be in Json or XML format.  Otherwise it must have a serialization format attribute.
    :type data: object
    :param event_type: Required: The name of the event.  This event must be registered in the context it is being fired.
    :type event_type: str
    :param expires_in: How long before the event expires and will be cleaned up.  The default is to use the system default.
    :type expires_in: object
    :param item_id: The id of the item, artifact, extension, project, etc.
    :type item_id: str
    :param process_delay: How long to wait before processing this event.  The default is to process immediately.
    :type process_delay: object
    :param scopes: Optional: A list of scopes which are are relevant to the event.
    :type scopes: list of :class:`EventScope <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.EventScope>`
    :param source_event_created_time: This is the time the original source event for this VssNotificationEvent was created.  For example, for something like a build completion notification SourceEventCreatedTime should be the time the build finished not the time this event was raised.
    :type source_event_created_time: datetime
    """

    _attribute_map = {
        'actors': {'key': 'actors', 'type': '[EventActor]'},
        'artifact_uris': {'key': 'artifactUris', 'type': '[str]'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'expires_in': {'key': 'expiresIn', 'type': 'object'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'process_delay': {'key': 'processDelay', 'type': 'object'},
        'scopes': {'key': 'scopes', 'type': '[EventScope]'},
        'source_event_created_time': {'key': 'sourceEventCreatedTime', 'type': 'iso-8601'}
    }

    def __init__(self, actors=None, artifact_uris=None, data=None, event_type=None, expires_in=None, item_id=None, process_delay=None, scopes=None, source_event_created_time=None):
        super(VssNotificationEvent, self).__init__()
        self.actors = actors
        self.artifact_uris = artifact_uris
        self.data = data
        self.event_type = event_type
        self.expires_in = expires_in
        self.item_id = item_id
        self.process_delay = process_delay
        self.scopes = scopes
        self.source_event_created_time = source_event_created_time


class ArtifactFilter(BaseSubscriptionFilter):
    """
    Artifact filter options. Used in "follow" subscriptions.

    :param event_type:
    :type event_type: str
    :param artifact_id:
    :type artifact_id: str
    :param artifact_type:
    :type artifact_type: str
    :param artifact_uri:
    :type artifact_uri: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'event_type': {'key': 'eventType', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, event_type=None, artifact_id=None, artifact_type=None, artifact_uri=None, type=None):
        super(ArtifactFilter, self).__init__(event_type=event_type)
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.artifact_uri = artifact_uri
        self.type = type


class FieldInputValues(InputValues):
    """
    :param default_value: The default value to use for this input
    :type default_value: str
    :param error: Errors encountered while computing dynamic values.
    :type error: :class:`InputValuesError <azure.devops.v6_0.notification.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <azure.devops.v6_0.notification.models.InputValue>`
    :param operators:
    :type operators: str
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'},
        'operators': {'key': 'operators', 'type': 'str'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None, operators=None):
        super(FieldInputValues, self).__init__(default_value=default_value, error=error, input_id=input_id, is_disabled=is_disabled, is_limited_to_possible_values=is_limited_to_possible_values, is_read_only=is_read_only, possible_values=possible_values)
        self.operators = operators


class FieldValuesQuery(InputValuesQuery):
    """
    :param current_values:
    :type current_values: dict
    :param resource: Subscription containing information about the publisher/consumer and the current input values
    :type resource: object
    :param input_values:
    :type input_values: list of :class:`FieldInputValues <azure.devops.v6_0.notification.models.FieldInputValues>`
    :param scope:
    :type scope: str
    """

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'resource': {'key': 'resource', 'type': 'object'},
        'input_values': {'key': 'inputValues', 'type': '[FieldInputValues]'},
        'scope': {'key': 'scope', 'type': 'str'}
    }

    def __init__(self, current_values=None, resource=None, input_values=None, scope=None):
        super(FieldValuesQuery, self).__init__(current_values=current_values, resource=resource)
        self.input_values = input_values
        self.scope = scope


__all__ = [
    'BaseSubscriptionFilter',
    'BatchNotificationOperation',
    'EventActor',
    'EventScope',
    'EventsEvaluationResult',
    'EventTransformRequest',
    'EventTransformResult',
    'ExpressionFilterClause',
    'ExpressionFilterGroup',
    'ExpressionFilterModel',
    'GraphSubjectBase',
    'IdentityRef',
    'INotificationDiagnosticLog',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'ISubscriptionChannel',
    'ISubscriptionFilter',
    'NotificationAdminSettings',
    'NotificationAdminSettingsUpdateParameters',
    'NotificationDiagnosticLogMessage',
    'NotificationEventField',
    'NotificationEventFieldOperator',
    'NotificationEventFieldType',
    'NotificationEventPublisher',
    'NotificationEventRole',
    'NotificationEventType',
    'NotificationEventTypeCategory',
    'NotificationQueryCondition',
    'NotificationReason',
    'NotificationsEvaluationResult',
    'NotificationStatistic',
    'NotificationStatisticsQuery',
    'NotificationStatisticsQueryConditions',
    'NotificationSubscriber',
    'NotificationSubscriberUpdateParameters',
    'NotificationSubscription',
    'NotificationSubscriptionCreateParameters',
    'NotificationSubscriptionTemplate',
    'NotificationSubscriptionUpdateParameters',
    'OperatorConstraint',
    'ReferenceLinks',
    'SubscriptionAdminSettings',
    'SubscriptionChannelWithAddress',
    'SubscriptionDiagnostics',
    'SubscriptionEvaluationRequest',
    'SubscriptionEvaluationResult',
    'SubscriptionEvaluationSettings',
    'SubscriptionManagement',
    'SubscriptionQuery',
    'SubscriptionQueryCondition',
    'SubscriptionScope',
    'SubscriptionTracing',
    'SubscriptionUserSettings',
    'UpdateSubscripitonDiagnosticsParameters',
    'UpdateSubscripitonTracingParameters',
    'ValueDefinition',
    'VssNotificationEvent',
    'ArtifactFilter',
    'FieldInputValues',
    'FieldValuesQuery',
]
