# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class Control(Model):
    """Control.

    :param contribution: Contribution for the control.
    :type contribution: :class:`WitContribution <work-item-tracking.v4_1.models.WitContribution>`
    :param control_type: Type of the control.
    :type control_type: str
    :param height: Height of the control, for html controls.
    :type height: int
    :param id: The id for the layout node.
    :type id: str
    :param inherited: A value indicating whether this layout node has been inherited from a parent layout.  This is expected to only be only set by the combiner.
    :type inherited: bool
    :param is_contribution: A value indicating if the layout node is contribution or not.
    :type is_contribution: bool
    :param label: Label for the field
    :type label: str
    :param metadata: Inner text of the control.
    :type metadata: str
    :param order:
    :type order: int
    :param overridden: A value indicating whether this layout node has been overridden by a child layout.
    :type overridden: bool
    :param read_only: A value indicating if the control is readonly.
    :type read_only: bool
    :param visible: A value indicating if the control should be hidden or not.
    :type visible: bool
    :param watermark: Watermark text for the textbox.
    :type watermark: str
    """

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'control_type': {'key': 'controlType', 'type': 'str'},
        'height': {'key': 'height', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'visible': {'key': 'visible', 'type': 'bool'},
        'watermark': {'key': 'watermark', 'type': 'str'}
    }

    def __init__(self, contribution=None, control_type=None, height=None, id=None, inherited=None, is_contribution=None, label=None, metadata=None, order=None, overridden=None, read_only=None, visible=None, watermark=None):
        super(Control, self).__init__()
        self.contribution = contribution
        self.control_type = control_type
        self.height = height
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.metadata = metadata
        self.order = order
        self.overridden = overridden
        self.read_only = read_only
        self.visible = visible
        self.watermark = watermark



class CreateProcessModel(Model):
    """CreateProcessModel.

    :param description: Description of the process
    :type description: str
    :param name: Name of the process
    :type name: str
    :param parent_process_type_id: The ID of the parent process
    :type parent_process_type_id: str
    :param reference_name: Reference name of the process
    :type reference_name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_process_type_id': {'key': 'parentProcessTypeId', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, parent_process_type_id=None, reference_name=None):
        super(CreateProcessModel, self).__init__()
        self.description = description
        self.name = name
        self.parent_process_type_id = parent_process_type_id
        self.reference_name = reference_name



class Extension(Model):
    """Extension.

    :param id:
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, id=None):
        super(Extension, self).__init__()
        self.id = id



class FieldModel(Model):
    """FieldModel.

    :param description:
    :type description: str
    :param id:
    :type id: str
    :param is_identity:
    :type is_identity: bool
    :param name:
    :type name: str
    :param type:
    :type type: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_identity': {'key': 'isIdentity', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, is_identity=None, name=None, type=None, url=None):
        super(FieldModel, self).__init__()
        self.description = description
        self.id = id
        self.is_identity = is_identity
        self.name = name
        self.type = type
        self.url = url



class FieldRuleModel(Model):
    """FieldRuleModel.

    :param actions:
    :type actions: list of :class:`RuleActionModel <work-item-tracking.v4_1.models.RuleActionModel>`
    :param conditions:
    :type conditions: list of :class:`RuleConditionModel <work-item-tracking.v4_1.models.RuleConditionModel>`
    :param friendly_name:
    :type friendly_name: str
    :param id:
    :type id: str
    :param is_disabled:
    :type is_disabled: bool
    :param is_system:
    :type is_system: bool
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[RuleActionModel]'},
        'conditions': {'key': 'conditions', 'type': '[RuleConditionModel]'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_system': {'key': 'isSystem', 'type': 'bool'}
    }

    def __init__(self, actions=None, conditions=None, friendly_name=None, id=None, is_disabled=None, is_system=None):
        super(FieldRuleModel, self).__init__()
        self.actions = actions
        self.conditions = conditions
        self.friendly_name = friendly_name
        self.id = id
        self.is_disabled = is_disabled
        self.is_system = is_system



class FormLayout(Model):
    """FormLayout.

    :param extensions: Gets and sets extensions list
    :type extensions: list of :class:`Extension <work-item-tracking.v4_1.models.Extension>`
    :param pages: Top level tabs of the layout.
    :type pages: list of :class:`Page <work-item-tracking.v4_1.models.Page>`
    :param system_controls: Headers controls of the layout.
    :type system_controls: list of :class:`Control <work-item-tracking.v4_1.models.Control>`
    """

    _attribute_map = {
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'pages': {'key': 'pages', 'type': '[Page]'},
        'system_controls': {'key': 'systemControls', 'type': '[Control]'}
    }

    def __init__(self, extensions=None, pages=None, system_controls=None):
        super(FormLayout, self).__init__()
        self.extensions = extensions
        self.pages = pages
        self.system_controls = system_controls



class Group(Model):
    """Group.

    :param contribution: Contribution for the group.
    :type contribution: :class:`WitContribution <work-item-tracking.v4_1.models.WitContribution>`
    :param controls: Controls to be put in the group.
    :type controls: list of :class:`Control <work-item-tracking.v4_1.models.Control>`
    :param height: The height for the contribution.
    :type height: int
    :param id: The id for the layout node.
    :type id: str
    :param inherited: A value indicating whether this layout node has been inherited from a parent layout.  This is expected to only be only set by the combiner.
    :type inherited: bool
    :param is_contribution: A value indicating if the layout node is contribution are not.
    :type is_contribution: bool
    :param label: Label for the group.
    :type label: str
    :param order: Order in which the group should appear in the section.
    :type order: int
    :param overridden: A value indicating whether this layout node has been overridden by a child layout.
    :type overridden: bool
    :param visible: A value indicating if the group should be hidden or not.
    :type visible: bool
    """

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'controls': {'key': 'controls', 'type': '[Control]'},
        'height': {'key': 'height', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'visible': {'key': 'visible', 'type': 'bool'}
    }

    def __init__(self, contribution=None, controls=None, height=None, id=None, inherited=None, is_contribution=None, label=None, order=None, overridden=None, visible=None):
        super(Group, self).__init__()
        self.contribution = contribution
        self.controls = controls
        self.height = height
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.order = order
        self.overridden = overridden
        self.visible = visible



class Page(Model):
    """Page.

    :param contribution: Contribution for the page.
    :type contribution: :class:`WitContribution <work-item-tracking.v4_1.models.WitContribution>`
    :param id: The id for the layout node.
    :type id: str
    :param inherited: A value indicating whether this layout node has been inherited from a parent layout.  This is expected to only be only set by the combiner.
    :type inherited: bool
    :param is_contribution: A value indicating if the layout node is contribution are not.
    :type is_contribution: bool
    :param label: The label for the page.
    :type label: str
    :param locked: A value indicating whether any user operations are permitted on this page and the contents of this page
    :type locked: bool
    :param order: Order in which the page should appear in the layout.
    :type order: int
    :param overridden: A value indicating whether this layout node has been overridden by a child layout.
    :type overridden: bool
    :param page_type: The icon for the page.
    :type page_type: object
    :param sections: The sections of the page.
    :type sections: list of :class:`Section <work-item-tracking.v4_1.models.Section>`
    :param visible: A value indicating if the page should be hidden or not.
    :type visible: bool
    """

    _attribute_map = {
        'contribution': {'key': 'contribution', 'type': 'WitContribution'},
        'id': {'key': 'id', 'type': 'str'},
        'inherited': {'key': 'inherited', 'type': 'bool'},
        'is_contribution': {'key': 'isContribution', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'page_type': {'key': 'pageType', 'type': 'object'},
        'sections': {'key': 'sections', 'type': '[Section]'},
        'visible': {'key': 'visible', 'type': 'bool'}
    }

    def __init__(self, contribution=None, id=None, inherited=None, is_contribution=None, label=None, locked=None, order=None, overridden=None, page_type=None, sections=None, visible=None):
        super(Page, self).__init__()
        self.contribution = contribution
        self.id = id
        self.inherited = inherited
        self.is_contribution = is_contribution
        self.label = label
        self.locked = locked
        self.order = order
        self.overridden = overridden
        self.page_type = page_type
        self.sections = sections
        self.visible = visible



class ProcessModel(Model):
    """ProcessModel.

    :param description: Description of the process
    :type description: str
    :param name: Name of the process
    :type name: str
    :param projects: Projects in this process
    :type projects: list of :class:`ProjectReference <work-item-tracking.v4_1.models.ProjectReference>`
    :param properties: Properties of the process
    :type properties: :class:`ProcessProperties <work-item-tracking.v4_1.models.ProcessProperties>`
    :param reference_name: Reference name of the process
    :type reference_name: str
    :param type_id: The ID of the process
    :type type_id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'projects': {'key': 'projects', 'type': '[ProjectReference]'},
        'properties': {'key': 'properties', 'type': 'ProcessProperties'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, projects=None, properties=None, reference_name=None, type_id=None):
        super(ProcessModel, self).__init__()
        self.description = description
        self.name = name
        self.projects = projects
        self.properties = properties
        self.reference_name = reference_name
        self.type_id = type_id



class ProcessProperties(Model):
    """ProcessProperties.

    :param class_: Class of the process
    :type class_: object
    :param is_default: Is the process default process
    :type is_default: bool
    :param is_enabled: Is the process enabled
    :type is_enabled: bool
    :param parent_process_type_id: ID of the parent process
    :type parent_process_type_id: str
    :param version: Version of the process
    :type version: str
    """

    _attribute_map = {
        'class_': {'key': 'class', 'type': 'object'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'parent_process_type_id': {'key': 'parentProcessTypeId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, class_=None, is_default=None, is_enabled=None, parent_process_type_id=None, version=None):
        super(ProcessProperties, self).__init__()
        self.class_ = class_
        self.is_default = is_default
        self.is_enabled = is_enabled
        self.parent_process_type_id = parent_process_type_id
        self.version = version



class ProjectReference(Model):
    """ProjectReference.

    :param description: Description of the project
    :type description: str
    :param id: The ID of the project
    :type id: str
    :param name: Name of the project
    :type name: str
    :param url: Url of the project
    :type url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, name=None, url=None):
        super(ProjectReference, self).__init__()
        self.description = description
        self.id = id
        self.name = name
        self.url = url



class RuleActionModel(Model):
    """RuleActionModel.

    :param action_type:
    :type action_type: str
    :param target_field:
    :type target_field: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'str'},
        'target_field': {'key': 'targetField', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, action_type=None, target_field=None, value=None):
        super(RuleActionModel, self).__init__()
        self.action_type = action_type
        self.target_field = target_field
        self.value = value



class RuleConditionModel(Model):
    """RuleConditionModel.

    :param condition_type:
    :type condition_type: str
    :param field:
    :type field: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, condition_type=None, field=None, value=None):
        super(RuleConditionModel, self).__init__()
        self.condition_type = condition_type
        self.field = field
        self.value = value



class Section(Model):
    """Section.

    :param groups:
    :type groups: list of :class:`Group <work-item-tracking.v4_1.models.Group>`
    :param id: The id for the layout node.
    :type id: str
    :param overridden: A value indicating whether this layout node has been overridden by a child layout.
    :type overridden: bool
    """

    _attribute_map = {
        'groups': {'key': 'groups', 'type': '[Group]'},
        'id': {'key': 'id', 'type': 'str'},
        'overridden': {'key': 'overridden', 'type': 'bool'}
    }

    def __init__(self, groups=None, id=None, overridden=None):
        super(Section, self).__init__()
        self.groups = groups
        self.id = id
        self.overridden = overridden



class UpdateProcessModel(Model):
    """UpdateProcessModel.

    :param description:
    :type description: str
    :param is_default:
    :type is_default: bool
    :param is_enabled:
    :type is_enabled: bool
    :param name:
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, is_default=None, is_enabled=None, name=None):
        super(UpdateProcessModel, self).__init__()
        self.description = description
        self.is_default = is_default
        self.is_enabled = is_enabled
        self.name = name



class WitContribution(Model):
    """WitContribution.

    :param contribution_id: The id for the contribution.
    :type contribution_id: str
    :param height: The height for the contribution.
    :type height: int
    :param inputs: A dictionary holding key value pairs for contribution inputs.
    :type inputs: dict
    :param show_on_deleted_work_item: A value indicating if the contribution should be show on deleted workItem.
    :type show_on_deleted_work_item: bool
    """

    _attribute_map = {
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'height': {'key': 'height', 'type': 'int'},
        'inputs': {'key': 'inputs', 'type': '{object}'},
        'show_on_deleted_work_item': {'key': 'showOnDeletedWorkItem', 'type': 'bool'}
    }

    def __init__(self, contribution_id=None, height=None, inputs=None, show_on_deleted_work_item=None):
        super(WitContribution, self).__init__()
        self.contribution_id = contribution_id
        self.height = height
        self.inputs = inputs
        self.show_on_deleted_work_item = show_on_deleted_work_item



class WorkItemBehavior(Model):
    """WorkItemBehavior.

    :param abstract:
    :type abstract: bool
    :param color:
    :type color: str
    :param description:
    :type description: str
    :param fields:
    :type fields: list of :class:`WorkItemBehaviorField <work-item-tracking.v4_1.models.WorkItemBehaviorField>`
    :param id:
    :type id: str
    :param inherits:
    :type inherits: :class:`WorkItemBehaviorReference <work-item-tracking.v4_1.models.WorkItemBehaviorReference>`
    :param name:
    :type name: str
    :param overriden:
    :type overriden: bool
    :param rank:
    :type rank: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'abstract': {'key': 'abstract', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[WorkItemBehaviorField]'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'WorkItemBehaviorReference'},
        'name': {'key': 'name', 'type': 'str'},
        'overriden': {'key': 'overriden', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, abstract=None, color=None, description=None, fields=None, id=None, inherits=None, name=None, overriden=None, rank=None, url=None):
        super(WorkItemBehavior, self).__init__()
        self.abstract = abstract
        self.color = color
        self.description = description
        self.fields = fields
        self.id = id
        self.inherits = inherits
        self.name = name
        self.overriden = overriden
        self.rank = rank
        self.url = url



class WorkItemBehaviorField(Model):
    """WorkItemBehaviorField.

    :param behavior_field_id:
    :type behavior_field_id: str
    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'behavior_field_id': {'key': 'behaviorFieldId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behavior_field_id=None, id=None, url=None):
        super(WorkItemBehaviorField, self).__init__()
        self.behavior_field_id = behavior_field_id
        self.id = id
        self.url = url



class WorkItemBehaviorReference(Model):
    """WorkItemBehaviorReference.

    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemBehaviorReference, self).__init__()
        self.id = id
        self.url = url



class WorkItemStateResultModel(Model):
    """WorkItemStateResultModel.

    :param color:
    :type color: str
    :param hidden:
    :type hidden: bool
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param order:
    :type order: int
    :param state_category:
    :type state_category: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'hidden': {'key': 'hidden', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'state_category': {'key': 'stateCategory', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, color=None, hidden=None, id=None, name=None, order=None, state_category=None, url=None):
        super(WorkItemStateResultModel, self).__init__()
        self.color = color
        self.hidden = hidden
        self.id = id
        self.name = name
        self.order = order
        self.state_category = state_category
        self.url = url



class WorkItemTypeBehavior(Model):
    """WorkItemTypeBehavior.

    :param behavior:
    :type behavior: :class:`WorkItemBehaviorReference <work-item-tracking.v4_1.models.WorkItemBehaviorReference>`
    :param is_default:
    :type is_default: bool
    :param url:
    :type url: str
    """

    _attribute_map = {
        'behavior': {'key': 'behavior', 'type': 'WorkItemBehaviorReference'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behavior=None, is_default=None, url=None):
        super(WorkItemTypeBehavior, self).__init__()
        self.behavior = behavior
        self.is_default = is_default
        self.url = url



class WorkItemTypeModel(Model):
    """WorkItemTypeModel.

    :param behaviors:
    :type behaviors: list of :class:`WorkItemTypeBehavior <work-item-tracking.v4_1.models.WorkItemTypeBehavior>`
    :param class_:
    :type class_: object
    :param color:
    :type color: str
    :param description:
    :type description: str
    :param icon:
    :type icon: str
    :param id:
    :type id: str
    :param inherits: Parent WIT Id/Internal ReferenceName that it inherits from
    :type inherits: str
    :param is_disabled:
    :type is_disabled: bool
    :param layout:
    :type layout: :class:`FormLayout <work-item-tracking.v4_1.models.FormLayout>`
    :param name:
    :type name: str
    :param states:
    :type states: list of :class:`WorkItemStateResultModel <work-item-tracking.v4_1.models.WorkItemStateResultModel>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'behaviors': {'key': 'behaviors', 'type': '[WorkItemTypeBehavior]'},
        'class_': {'key': 'class', 'type': 'object'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'layout': {'key': 'layout', 'type': 'FormLayout'},
        'name': {'key': 'name', 'type': 'str'},
        'states': {'key': 'states', 'type': '[WorkItemStateResultModel]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, behaviors=None, class_=None, color=None, description=None, icon=None, id=None, inherits=None, is_disabled=None, layout=None, name=None, states=None, url=None):
        super(WorkItemTypeModel, self).__init__()
        self.behaviors = behaviors
        self.class_ = class_
        self.color = color
        self.description = description
        self.icon = icon
        self.id = id
        self.inherits = inherits
        self.is_disabled = is_disabled
        self.layout = layout
        self.name = name
        self.states = states
        self.url = url
