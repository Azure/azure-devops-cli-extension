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
    :type _links: :class:`ReferenceLinks <feature-management.v4_1.models.ReferenceLinks>`
    :param default_state: If true, the feature is enabled unless overridden at some scope
    :type default_state: bool
    :param default_value_rules: Rules for setting the default value if not specified by any setting/scope. Evaluated in order until a rule returns an Enabled or Disabled state (not Undefined)
    :type default_value_rules: list of :class:`ContributedFeatureValueRule <feature-management.v4_1.models.ContributedFeatureValueRule>`
    :param description: The description of the feature
    :type description: str
    :param id: The full contribution id of the feature
    :type id: str
    :param name: The friendly name of the feature
    :type name: str
    :param override_rules: Rules for overriding a feature value. These rules are run before explicit user/host state values are checked. They are evaluated in order until a rule returns an Enabled or Disabled state (not Undefined)
    :type override_rules: list of :class:`ContributedFeatureValueRule <feature-management.v4_1.models.ContributedFeatureValueRule>`
    :param scopes: The scopes/levels at which settings can set the enabled/disabled state of this feature
    :type scopes: list of :class:`ContributedFeatureSettingScope <feature-management.v4_1.models.ContributedFeatureSettingScope>`
    :param service_instance_type: The service instance id of the service that owns this feature
    :type service_instance_type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_state': {'key': 'defaultState', 'type': 'bool'},
        'default_value_rules': {'key': 'defaultValueRules', 'type': '[ContributedFeatureValueRule]'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'override_rules': {'key': 'overrideRules', 'type': '[ContributedFeatureValueRule]'},
        'scopes': {'key': 'scopes', 'type': '[ContributedFeatureSettingScope]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'}
    }

    def __init__(self, _links=None, default_state=None, default_value_rules=None, description=None, id=None, name=None, override_rules=None, scopes=None, service_instance_type=None):
        super(ContributedFeature, self).__init__()
        self._links = _links
        self.default_state = default_state
        self.default_value_rules = default_value_rules
        self.description = description
        self.id = id
        self.name = name
        self.override_rules = override_rules
        self.scopes = scopes
        self.service_instance_type = service_instance_type



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
    :type scope: :class:`ContributedFeatureSettingScope <feature-management.v4_1.models.ContributedFeatureSettingScope>`
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



class ContributedFeatureValueRule(Model):
    """ContributedFeatureValueRule.

    :param name: Name of the IContributedFeatureValuePlugin to run
    :type name: str
    :param properties: Properties to feed to the IContributedFeatureValuePlugin
    :type properties: dict
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, name=None, properties=None):
        super(ContributedFeatureValueRule, self).__init__()
        self.name = name
        self.properties = properties



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
