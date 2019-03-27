# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ContributedFeature(Model):
    """ContributedFeature.

    :param _links: Named links describing the feature
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.feature_management.models.ReferenceLinks>`
    :param default_state: If true, the feature is enabled unless overridden at some scope
    :type default_state: bool
    :param default_value_rules: Rules for setting the default value if not specified by any setting/scope. Evaluated in order until a rule returns an Enabled or Disabled state (not Undefined)
    :type default_value_rules: list of :class:`ContributedFeatureValueRule <azure.devops.v5_1.feature_management.models.ContributedFeatureValueRule>`
    :param description: The description of the feature
    :type description: str
    :param feature_properties: Extra properties for the feature
    :type feature_properties: dict
    :param feature_state_changed_listeners: Handler for listening to setter calls on feature value. These listeners are only invoked after a successful set has occured
    :type feature_state_changed_listeners: list of :class:`ContributedFeatureListener <azure.devops.v5_1.feature_management.models.ContributedFeatureListener>`
    :param id: The full contribution id of the feature
    :type id: str
    :param include_as_claim: If this is set to true, then the id for this feature will be added to the list of claims for the request.
    :type include_as_claim: bool
    :param name: The friendly name of the feature
    :type name: str
    :param order: Suggested order to display feature in.
    :type order: int
    :param override_rules: Rules for overriding a feature value. These rules are run before explicit user/host state values are checked. They are evaluated in order until a rule returns an Enabled or Disabled state (not Undefined)
    :type override_rules: list of :class:`ContributedFeatureValueRule <azure.devops.v5_1.feature_management.models.ContributedFeatureValueRule>`
    :param scopes: The scopes/levels at which settings can set the enabled/disabled state of this feature
    :type scopes: list of :class:`ContributedFeatureSettingScope <azure.devops.v5_1.feature_management.models.ContributedFeatureSettingScope>`
    :param service_instance_type: The service instance id of the service that owns this feature
    :type service_instance_type: str
    :param tags: Tags associated with the feature.
    :type tags: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_state': {'key': 'defaultState', 'type': 'bool'},
        'default_value_rules': {'key': 'defaultValueRules', 'type': '[ContributedFeatureValueRule]'},
        'description': {'key': 'description', 'type': 'str'},
        'feature_properties': {'key': 'featureProperties', 'type': '{object}'},
        'feature_state_changed_listeners': {'key': 'featureStateChangedListeners', 'type': '[ContributedFeatureListener]'},
        'id': {'key': 'id', 'type': 'str'},
        'include_as_claim': {'key': 'includeAsClaim', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'override_rules': {'key': 'overrideRules', 'type': '[ContributedFeatureValueRule]'},
        'scopes': {'key': 'scopes', 'type': '[ContributedFeatureSettingScope]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_state=None, default_value_rules=None, description=None, feature_properties=None, feature_state_changed_listeners=None, id=None, include_as_claim=None, name=None, order=None, override_rules=None, scopes=None, service_instance_type=None, tags=None):
        super(ContributedFeature, self).__init__()
        self._links = _links
        self.default_state = default_state
        self.default_value_rules = default_value_rules
        self.description = description
        self.feature_properties = feature_properties
        self.feature_state_changed_listeners = feature_state_changed_listeners
        self.id = id
        self.include_as_claim = include_as_claim
        self.name = name
        self.order = order
        self.override_rules = override_rules
        self.scopes = scopes
        self.service_instance_type = service_instance_type
        self.tags = tags


class ContributedFeatureHandlerSettings(Model):
    """ContributedFeatureHandlerSettings.

    :param name: Name of the handler to run
    :type name: str
    :param properties: Properties to feed to the handler
    :type properties: dict
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureHandlerSettings, self).__init__()
        self.name = name
        self.properties = properties


class ContributedFeatureListener(ContributedFeatureHandlerSettings):
    """ContributedFeatureListener.

    :param name: Name of the handler to run
    :type name: str
    :param properties: Properties to feed to the handler
    :type properties: dict
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureListener, self).__init__(name=name, properties=properties)


class ContributedFeatureSettingScope(Model):
    """ContributedFeatureSettingScope.

    :param setting_scope: The name of the settings scope to use when reading/writing the setting
    :type setting_scope: str
    :param user_scoped: Whether this is a user-scope or this is a host-wide (all users) setting
    :type user_scoped: bool
    """

    _attribute_map = {
        'setting_scope': {'key': 'settingScope', 'type': 'str'},
        'user_scoped': {'key': 'userScoped', 'type': 'bool'}
    }

    def __init__(self, setting_scope=None, user_scoped=None):
        super(ContributedFeatureSettingScope, self).__init__()
        self.setting_scope = setting_scope
        self.user_scoped = user_scoped


class ContributedFeatureState(Model):
    """ContributedFeatureState.

    :param feature_id: The full contribution id of the feature
    :type feature_id: str
    :param overridden: True if the effective state was set by an override rule (indicating that the state cannot be managed by the end user)
    :type overridden: bool
    :param reason: Reason that the state was set (by a plugin/rule).
    :type reason: str
    :param scope: The scope at which this state applies
    :type scope: :class:`ContributedFeatureSettingScope <azure.devops.v5_1.feature_management.models.ContributedFeatureSettingScope>`
    :param state: The current state of this feature
    :type state: object
    """

    _attribute_map = {
        'feature_id': {'key': 'featureId', 'type': 'str'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'ContributedFeatureSettingScope'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, feature_id=None, overridden=None, reason=None, scope=None, state=None):
        super(ContributedFeatureState, self).__init__()
        self.feature_id = feature_id
        self.overridden = overridden
        self.reason = reason
        self.scope = scope
        self.state = state


class ContributedFeatureStateQuery(Model):
    """ContributedFeatureStateQuery.

    :param feature_ids: The list of feature ids to query
    :type feature_ids: list of str
    :param feature_states: The query result containing the current feature states for each of the queried feature ids
    :type feature_states: dict
    :param scope_values: A dictionary of scope values (project name, etc.) to use in the query (if querying across scopes)
    :type scope_values: dict
    """

    _attribute_map = {
        'feature_ids': {'key': 'featureIds', 'type': '[str]'},
        'feature_states': {'key': 'featureStates', 'type': '{ContributedFeatureState}'},
        'scope_values': {'key': 'scopeValues', 'type': '{str}'}
    }

    def __init__(self, feature_ids=None, feature_states=None, scope_values=None):
        super(ContributedFeatureStateQuery, self).__init__()
        self.feature_ids = feature_ids
        self.feature_states = feature_states
        self.scope_values = scope_values


class ContributedFeatureValueRule(ContributedFeatureHandlerSettings):
    """ContributedFeatureValueRule.

    :param name: Name of the handler to run
    :type name: str
    :param properties: Properties to feed to the handler
    :type properties: dict
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureValueRule, self).__init__(name=name, properties=properties)


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


__all__ = [
    'ContributedFeature',
    'ContributedFeatureHandlerSettings',
    'ContributedFeatureListener',
    'ContributedFeatureSettingScope',
    'ContributedFeatureState',
    'ContributedFeatureStateQuery',
    'ContributedFeatureValueRule',
    'ReferenceLinks',
]
