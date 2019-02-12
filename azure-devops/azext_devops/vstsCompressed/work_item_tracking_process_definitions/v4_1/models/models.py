# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class BehaviorCreateModel(Model):
    """BehaviorCreateModel.

    :param color: Color
    :type color: str
    :param inherits: Parent behavior id
    :type inherits: str
    :param name: Name of the behavior
    :type name: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, color=None, inherits=None, name=None):
        super(BehaviorCreateModel, self).__init__()
        self.color = color
        self.inherits = inherits
        self.name = name



class BehaviorModel(Model):
    """BehaviorModel.

    :param abstract: Is the behavior abstract (i.e. can not be associated with any work item type)
    :type abstract: bool
    :param color: Color
    :type color: str
    :param description: Description
    :type description: str
    :param id: Behavior Id
    :type id: str
    :param inherits: Parent behavior reference
    :type inherits: :class:`WorkItemBehaviorReference <work-item-tracking.v4_1.models.WorkItemBehaviorReference>`
    :param name: Behavior Name
    :type name: str
    :param overridden: Is the behavior overrides a behavior from system process
    :type overridden: bool
    :param rank: Rank
    :type rank: int
    :param url: Url of the behavior
    :type url: str
    """

    _attribute_map = {
        'abstract': {'key': 'abstract', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'WorkItemBehaviorReference'},
        'name': {'key': 'name', 'type': 'str'},
        'overridden': {'key': 'overridden', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, abstract=None, color=None, description=None, id=None, inherits=None, name=None, overridden=None, rank=None, url=None):
        super(BehaviorModel, self).__init__()
        self.abstract = abstract
        self.color = color
        self.description = description
        self.id = id
        self.inherits = inherits
        self.name = name
        self.overridden = overridden
        self.rank = rank
        self.url = url



class BehaviorReplaceModel(Model):
    """BehaviorReplaceModel.

    :param color: Color
    :type color: str
    :param name: Behavior Name
    :type name: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, color=None, name=None):
        super(BehaviorReplaceModel, self).__init__()
        self.color = color
        self.name = name



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

    :param description: Description about field
    :type description: str
    :param id: ID of the field
    :type id: str
    :param name: Name of the field
    :type name: str
    :param pick_list: Reference to picklist in this field
    :type pick_list: :class:`PickListMetadataModel <work-item-tracking.v4_1.models.PickListMetadataModel>`
    :param type: Type of field
    :type type: object
    :param url: Url to the field
    :type url: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pick_list': {'key': 'pickList', 'type': 'PickListMetadataModel'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, name=None, pick_list=None, type=None, url=None):
        super(FieldModel, self).__init__()
        self.description = description
        self.id = id
        self.name = name
        self.pick_list = pick_list
        self.type = type
        self.url = url



class FieldUpdate(Model):
    """FieldUpdate.

    :param description:
    :type description: str
    :param id:
    :type id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, description=None, id=None):
        super(FieldUpdate, self).__init__()
        self.description = description
        self.id = id



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



class HideStateModel(Model):
    """HideStateModel.

    :param hidden:
    :type hidden: bool
    """

    _attribute_map = {
        'hidden': {'key': 'hidden', 'type': 'bool'}
    }

    def __init__(self, hidden=None):
        super(HideStateModel, self).__init__()
        self.hidden = hidden



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



class PickListItemModel(Model):
    """PickListItemModel.

    :param id:
    :type id: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, id=None, value=None):
        super(PickListItemModel, self).__init__()
        self.id = id
        self.value = value



class PickListMetadataModel(Model):
    """PickListMetadataModel.

    :param id: ID of the picklist
    :type id: str
    :param is_suggested: Is input values by user only limited to suggested values
    :type is_suggested: bool
    :param name: Name of the picklist
    :type name: str
    :param type: Type of picklist
    :type type: str
    :param url: Url of the picklist
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_suggested': {'key': 'isSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, is_suggested=None, name=None, type=None, url=None):
        super(PickListMetadataModel, self).__init__()
        self.id = id
        self.is_suggested = is_suggested
        self.name = name
        self.type = type
        self.url = url



class PickListModel(PickListMetadataModel):
    """PickListModel.

    :param id: ID of the picklist
    :type id: str
    :param is_suggested: Is input values by user only limited to suggested values
    :type is_suggested: bool
    :param name: Name of the picklist
    :type name: str
    :param type: Type of picklist
    :type type: str
    :param url: Url of the picklist
    :type url: str
    :param items: A list of PicklistItemModel
    :type items: list of :class:`PickListItemModel <work-item-tracking.v4_1.models.PickListItemModel>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_suggested': {'key': 'isSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'items': {'key': 'items', 'type': '[PickListItemModel]'}
    }

    def __init__(self, id=None, is_suggested=None, name=None, type=None, url=None, items=None):
        super(PickListModel, self).__init__(id=id, is_suggested=is_suggested, name=name, type=type, url=url)
        self.items = items



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



class WorkItemBehaviorReference(Model):
    """WorkItemBehaviorReference.

    :param id: The ID of the reference behavior
    :type id: str
    :param url: The url of the reference behavior
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



class WorkItemStateInputModel(Model):
    """WorkItemStateInputModel.

    :param color: Color of the state
    :type color: str
    :param name: Name of the state
    :type name: str
    :param order: Order in which state should appear
    :type order: int
    :param state_category: Category of the state
    :type state_category: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'state_category': {'key': 'stateCategory', 'type': 'str'}
    }

    def __init__(self, color=None, name=None, order=None, state_category=None):
        super(WorkItemStateInputModel, self).__init__()
        self.color = color
        self.name = name
        self.order = order
        self.state_category = state_category



class WorkItemStateResultModel(Model):
    """WorkItemStateResultModel.

    :param color: Color of the state
    :type color: str
    :param hidden: Is the state hidden
    :type hidden: bool
    :param id: The ID of the State
    :type id: str
    :param name: Name of the state
    :type name: str
    :param order: Order in which state should appear
    :type order: int
    :param state_category: Category of the state
    :type state_category: str
    :param url: Url of the state
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



class WorkItemTypeFieldModel(Model):
    """WorkItemTypeFieldModel.

    :param allow_groups:
    :type allow_groups: bool
    :param default_value:
    :type default_value: str
    :param name:
    :type name: str
    :param pick_list:
    :type pick_list: :class:`PickListMetadataModel <work-item-tracking.v4_1.models.PickListMetadataModel>`
    :param read_only:
    :type read_only: bool
    :param reference_name:
    :type reference_name: str
    :param required:
    :type required: bool
    :param type:
    :type type: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        'allow_groups': {'key': 'allowGroups', 'type': 'bool'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pick_list': {'key': 'pickList', 'type': 'PickListMetadataModel'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, allow_groups=None, default_value=None, name=None, pick_list=None, read_only=None, reference_name=None, required=None, type=None, url=None):
        super(WorkItemTypeFieldModel, self).__init__()
        self.allow_groups = allow_groups
        self.default_value = default_value
        self.name = name
        self.pick_list = pick_list
        self.read_only = read_only
        self.reference_name = reference_name
        self.required = required
        self.type = type
        self.url = url



class WorkItemTypeModel(Model):
    """WorkItemTypeModel.

    :param behaviors: Behaviors of the work item type
    :type behaviors: list of :class:`WorkItemTypeBehavior <work-item-tracking.v4_1.models.WorkItemTypeBehavior>`
    :param class_: Class of the work item type
    :type class_: object
    :param color: Color of the work item type
    :type color: str
    :param description: Description of the work item type
    :type description: str
    :param icon: Icon of the work item type
    :type icon: str
    :param id: The ID of the work item type
    :type id: str
    :param inherits: Parent WIT Id/Internal ReferenceName that it inherits from
    :type inherits: str
    :param is_disabled: Is work item type disabled
    :type is_disabled: bool
    :param layout: Layout of the work item type
    :type layout: :class:`FormLayout <work-item-tracking.v4_1.models.FormLayout>`
    :param name: Name of the work item type
    :type name: str
    :param states: States of the work item type
    :type states: list of :class:`WorkItemStateResultModel <work-item-tracking.v4_1.models.WorkItemStateResultModel>`
    :param url: Url of the work item type
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



class WorkItemTypeUpdateModel(Model):
    """WorkItemTypeUpdateModel.

    :param color: Color of the work item type
    :type color: str
    :param description: Description of the work item type
    :type description: str
    :param icon: Icon of the work item type
    :type icon: str
    :param is_disabled: Is the workitem type to be disabled
    :type is_disabled: bool
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'}
    }

    def __init__(self, color=None, description=None, icon=None, is_disabled=None):
        super(WorkItemTypeUpdateModel, self).__init__()
        self.color = color
        self.description = description
        self.icon = icon
        self.is_disabled = is_disabled
