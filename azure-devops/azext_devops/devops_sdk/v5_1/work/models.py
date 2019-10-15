# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Activity(Model):
    """
    :param capacity_per_day:
    :type capacity_per_day: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'capacity_per_day': {'key': 'capacityPerDay', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, capacity_per_day=None, name=None):
        super(Activity, self).__init__()
        self.capacity_per_day = capacity_per_day
        self.name = name


class BacklogColumn(Model):
    """
    :param column_field_reference:
    :type column_field_reference: :class:`WorkItemFieldReference <azure.devops.v5_1.work.models.WorkItemFieldReference>`
    :param width:
    :type width: int
    """

    _attribute_map = {
        'column_field_reference': {'key': 'columnFieldReference', 'type': 'WorkItemFieldReference'},
        'width': {'key': 'width', 'type': 'int'}
    }

    def __init__(self, column_field_reference=None, width=None):
        super(BacklogColumn, self).__init__()
        self.column_field_reference = column_field_reference
        self.width = width


class BacklogConfiguration(Model):
    """
    :param backlog_fields: Behavior/type field mapping
    :type backlog_fields: :class:`BacklogFields <azure.devops.v5_1.work.models.BacklogFields>`
    :param bugs_behavior: Bugs behavior
    :type bugs_behavior: object
    :param hidden_backlogs: Hidden Backlog
    :type hidden_backlogs: list of str
    :param is_bugs_behavior_configured: Is BugsBehavior Configured in the process
    :type is_bugs_behavior_configured: bool
    :param portfolio_backlogs: Portfolio backlog descriptors
    :type portfolio_backlogs: list of :class:`BacklogLevelConfiguration <azure.devops.v5_1.work.models.BacklogLevelConfiguration>`
    :param requirement_backlog: Requirement backlog
    :type requirement_backlog: :class:`BacklogLevelConfiguration <azure.devops.v5_1.work.models.BacklogLevelConfiguration>`
    :param task_backlog: Task backlog
    :type task_backlog: :class:`BacklogLevelConfiguration <azure.devops.v5_1.work.models.BacklogLevelConfiguration>`
    :param url:
    :type url: str
    :param work_item_type_mapped_states: Mapped states for work item types
    :type work_item_type_mapped_states: list of :class:`WorkItemTypeStateInfo <azure.devops.v5_1.work.models.WorkItemTypeStateInfo>`
    """

    _attribute_map = {
        'backlog_fields': {'key': 'backlogFields', 'type': 'BacklogFields'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'hidden_backlogs': {'key': 'hiddenBacklogs', 'type': '[str]'},
        'is_bugs_behavior_configured': {'key': 'isBugsBehaviorConfigured', 'type': 'bool'},
        'portfolio_backlogs': {'key': 'portfolioBacklogs', 'type': '[BacklogLevelConfiguration]'},
        'requirement_backlog': {'key': 'requirementBacklog', 'type': 'BacklogLevelConfiguration'},
        'task_backlog': {'key': 'taskBacklog', 'type': 'BacklogLevelConfiguration'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_type_mapped_states': {'key': 'workItemTypeMappedStates', 'type': '[WorkItemTypeStateInfo]'}
    }

    def __init__(self, backlog_fields=None, bugs_behavior=None, hidden_backlogs=None, is_bugs_behavior_configured=None, portfolio_backlogs=None, requirement_backlog=None, task_backlog=None, url=None, work_item_type_mapped_states=None):
        super(BacklogConfiguration, self).__init__()
        self.backlog_fields = backlog_fields
        self.bugs_behavior = bugs_behavior
        self.hidden_backlogs = hidden_backlogs
        self.is_bugs_behavior_configured = is_bugs_behavior_configured
        self.portfolio_backlogs = portfolio_backlogs
        self.requirement_backlog = requirement_backlog
        self.task_backlog = task_backlog
        self.url = url
        self.work_item_type_mapped_states = work_item_type_mapped_states


class BacklogFields(Model):
    """
    :param type_fields: Field Type (e.g. Order, Activity) to Field Reference Name map
    :type type_fields: dict
    """

    _attribute_map = {
        'type_fields': {'key': 'typeFields', 'type': '{str}'}
    }

    def __init__(self, type_fields=None):
        super(BacklogFields, self).__init__()
        self.type_fields = type_fields


class BacklogLevel(Model):
    """
    Contract representing a backlog level

    :param category_reference_name: Reference name of the corresponding WIT category
    :type category_reference_name: str
    :param plural_name: Plural name for the backlog level
    :type plural_name: str
    :param work_item_states: Collection of work item states that are included in the plan. The server will filter to only these work item types.
    :type work_item_states: list of str
    :param work_item_types: Collection of valid workitem type names for the given backlog level
    :type work_item_types: list of str
    """

    _attribute_map = {
        'category_reference_name': {'key': 'categoryReferenceName', 'type': 'str'},
        'plural_name': {'key': 'pluralName', 'type': 'str'},
        'work_item_states': {'key': 'workItemStates', 'type': '[str]'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[str]'}
    }

    def __init__(self, category_reference_name=None, plural_name=None, work_item_states=None, work_item_types=None):
        super(BacklogLevel, self).__init__()
        self.category_reference_name = category_reference_name
        self.plural_name = plural_name
        self.work_item_states = work_item_states
        self.work_item_types = work_item_types


class BacklogLevelConfiguration(Model):
    """
    :param add_panel_fields: List of fields to include in Add Panel
    :type add_panel_fields: list of :class:`WorkItemFieldReference <azure.devops.v5_1.work.models.WorkItemFieldReference>`
    :param color: Color for the backlog level
    :type color: str
    :param column_fields: Default list of columns for the backlog
    :type column_fields: list of :class:`BacklogColumn <azure.devops.v5_1.work.models.BacklogColumn>`
    :param default_work_item_type: Default Work Item Type for the backlog
    :type default_work_item_type: :class:`WorkItemTypeReference <azure.devops.v5_1.work.models.WorkItemTypeReference>`
    :param id: Backlog Id (for Legacy Backlog Level from process config it can be categoryref name)
    :type id: str
    :param is_hidden: Indicates whether the backlog level is hidden
    :type is_hidden: bool
    :param name: Backlog Name
    :type name: str
    :param rank: Backlog Rank (Taskbacklog is 0)
    :type rank: int
    :param type: The type of this backlog level
    :type type: object
    :param work_item_count_limit: Max number of work items to show in the given backlog
    :type work_item_count_limit: int
    :param work_item_types: Work Item types participating in this backlog as known by the project/Process, can be overridden by team settings for bugs
    :type work_item_types: list of :class:`WorkItemTypeReference <azure.devops.v5_1.work.models.WorkItemTypeReference>`
    """

    _attribute_map = {
        'add_panel_fields': {'key': 'addPanelFields', 'type': '[WorkItemFieldReference]'},
        'color': {'key': 'color', 'type': 'str'},
        'column_fields': {'key': 'columnFields', 'type': '[BacklogColumn]'},
        'default_work_item_type': {'key': 'defaultWorkItemType', 'type': 'WorkItemTypeReference'},
        'id': {'key': 'id', 'type': 'str'},
        'is_hidden': {'key': 'isHidden', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'work_item_count_limit': {'key': 'workItemCountLimit', 'type': 'int'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, add_panel_fields=None, color=None, column_fields=None, default_work_item_type=None, id=None, is_hidden=None, name=None, rank=None, type=None, work_item_count_limit=None, work_item_types=None):
        super(BacklogLevelConfiguration, self).__init__()
        self.add_panel_fields = add_panel_fields
        self.color = color
        self.column_fields = column_fields
        self.default_work_item_type = default_work_item_type
        self.id = id
        self.is_hidden = is_hidden
        self.name = name
        self.rank = rank
        self.type = type
        self.work_item_count_limit = work_item_count_limit
        self.work_item_types = work_item_types


class BacklogLevelWorkItems(Model):
    """
    Represents work items in a backlog level

    :param work_items: A list of work items within a backlog level
    :type work_items: list of :class:`WorkItemLink <azure.devops.v5_1.work.models.WorkItemLink>`
    """

    _attribute_map = {
        'work_items': {'key': 'workItems', 'type': '[WorkItemLink]'}
    }

    def __init__(self, work_items=None):
        super(BacklogLevelWorkItems, self).__init__()
        self.work_items = work_items


class BoardBadge(Model):
    """
    Represents a board badge.

    :param board_id: The ID of the board represented by this badge.
    :type board_id: str
    :param image_url: A link to the SVG resource.
    :type image_url: str
    """

    _attribute_map = {
        'board_id': {'key': 'boardId', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'}
    }

    def __init__(self, board_id=None, image_url=None):
        super(BoardBadge, self).__init__()
        self.board_id = board_id
        self.image_url = image_url


class BoardCardRuleSettings(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param rules:
    :type rules: dict
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'rules': {'key': 'rules', 'type': '{[Rule]}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, rules=None, url=None):
        super(BoardCardRuleSettings, self).__init__()
        self._links = _links
        self.rules = rules
        self.url = url


class BoardCardSettings(Model):
    """
    :param cards:
    :type cards: dict
    """

    _attribute_map = {
        'cards': {'key': 'cards', 'type': '{[FieldSetting]}'}
    }

    def __init__(self, cards=None):
        super(BoardCardSettings, self).__init__()
        self.cards = cards


class BoardChartReference(Model):
    """
    :param name: Name of the resource
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(BoardChartReference, self).__init__()
        self.name = name
        self.url = url


class BoardColumn(Model):
    """
    :param column_type:
    :type column_type: object
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param is_split:
    :type is_split: bool
    :param item_limit:
    :type item_limit: int
    :param name:
    :type name: str
    :param state_mappings:
    :type state_mappings: dict
    """

    _attribute_map = {
        'column_type': {'key': 'columnType', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_split': {'key': 'isSplit', 'type': 'bool'},
        'item_limit': {'key': 'itemLimit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'state_mappings': {'key': 'stateMappings', 'type': '{str}'}
    }

    def __init__(self, column_type=None, description=None, id=None, is_split=None, item_limit=None, name=None, state_mappings=None):
        super(BoardColumn, self).__init__()
        self.column_type = column_type
        self.description = description
        self.id = id
        self.is_split = is_split
        self.item_limit = item_limit
        self.name = name
        self.state_mappings = state_mappings


class BoardFields(Model):
    """
    :param column_field:
    :type column_field: :class:`FieldReference <azure.devops.v5_1.work.models.FieldReference>`
    :param done_field:
    :type done_field: :class:`FieldReference <azure.devops.v5_1.work.models.FieldReference>`
    :param row_field:
    :type row_field: :class:`FieldReference <azure.devops.v5_1.work.models.FieldReference>`
    """

    _attribute_map = {
        'column_field': {'key': 'columnField', 'type': 'FieldReference'},
        'done_field': {'key': 'doneField', 'type': 'FieldReference'},
        'row_field': {'key': 'rowField', 'type': 'FieldReference'}
    }

    def __init__(self, column_field=None, done_field=None, row_field=None):
        super(BoardFields, self).__init__()
        self.column_field = column_field
        self.done_field = done_field
        self.row_field = row_field


class BoardReference(Model):
    """
    :param id: Id of the resource
    :type id: str
    :param name: Name of the resource
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(BoardReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class BoardRow(Model):
    """
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
        super(BoardRow, self).__init__()
        self.id = id
        self.name = name


class BoardSuggestedValue(Model):
    """
    :param name:
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(BoardSuggestedValue, self).__init__()
        self.name = name


class BoardUserSettings(Model):
    """
    :param auto_refresh_state:
    :type auto_refresh_state: bool
    """

    _attribute_map = {
        'auto_refresh_state': {'key': 'autoRefreshState', 'type': 'bool'}
    }

    def __init__(self, auto_refresh_state=None):
        super(BoardUserSettings, self).__init__()
        self.auto_refresh_state = auto_refresh_state


class CapacityPatch(Model):
    """
    Expected data from PATCH

    :param activities:
    :type activities: list of :class:`Activity <azure.devops.v5_1.work.models.Activity>`
    :param days_off:
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    """

    _attribute_map = {
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, activities=None, days_off=None):
        super(CapacityPatch, self).__init__()
        self.activities = activities
        self.days_off = days_off


class CategoryConfiguration(Model):
    """
    Details about a given backlog category

    :param name: Name
    :type name: str
    :param reference_name: Category Reference Name
    :type reference_name: str
    :param work_item_types: Work item types for the backlog category
    :type work_item_types: list of :class:`WorkItemTypeReference <azure.devops.v5_1.work.models.WorkItemTypeReference>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, name=None, reference_name=None, work_item_types=None):
        super(CategoryConfiguration, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.work_item_types = work_item_types


class CreatePlan(Model):
    """
    :param description: Description of the plan
    :type description: str
    :param name: Name of the plan to create.
    :type name: str
    :param properties: Plan properties.
    :type properties: object
    :param type: Type of plan to create.
    :type type: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, properties=None, type=None):
        super(CreatePlan, self).__init__()
        self.description = description
        self.name = name
        self.properties = properties
        self.type = type


class DateRange(Model):
    """
    :param end: End of the date range.
    :type end: datetime
    :param start: Start of the date range.
    :type start: datetime
    """

    _attribute_map = {
        'end': {'key': 'end', 'type': 'iso-8601'},
        'start': {'key': 'start', 'type': 'iso-8601'}
    }

    def __init__(self, end=None, start=None):
        super(DateRange, self).__init__()
        self.end = end
        self.start = start


class FieldReference(Model):
    """
    An abstracted reference to a field

    :param reference_name: fieldRefName for the field
    :type reference_name: str
    :param url: Full http link to more information about the field
    :type url: str
    """

    _attribute_map = {
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, reference_name=None, url=None):
        super(FieldReference, self).__init__()
        self.reference_name = reference_name
        self.url = url


class FilterClause(Model):
    """
    :param field_name:
    :type field_name: str
    :param index:
    :type index: int
    :param logical_operator:
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
        super(FilterClause, self).__init__()
        self.field_name = field_name
        self.index = index
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value


class GraphSubjectBase(Model):
    """
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
    """
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


class Link(Model):
    """
    Link description.

    :param attributes: Collection of link attributes.
    :type attributes: dict
    :param rel: Relation type.
    :type rel: str
    :param url: Link url.
    :type url: str
    """

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(Link, self).__init__()
        self.attributes = attributes
        self.rel = rel
        self.url = url


class Member(Model):
    """
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, image_url=None, unique_name=None, url=None):
        super(Member, self).__init__()
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.unique_name = unique_name
        self.url = url


class ParentChildWIMap(Model):
    """
    :param child_work_item_ids:
    :type child_work_item_ids: list of int
    :param id:
    :type id: int
    :param title:
    :type title: str
    """

    _attribute_map = {
        'child_work_item_ids': {'key': 'childWorkItemIds', 'type': '[int]'},
        'id': {'key': 'id', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, child_work_item_ids=None, id=None, title=None):
        super(ParentChildWIMap, self).__init__()
        self.child_work_item_ids = child_work_item_ids
        self.id = id
        self.title = title


class Plan(Model):
    """
    Data contract for the plan definition

    :param created_by_identity: Identity that created this plan. Defaults to null for records before upgrading to ScaledAgileViewComponent4.
    :type created_by_identity: :class:`IdentityRef <azure.devops.v5_1.work.models.IdentityRef>`
    :param created_date: Date when the plan was created
    :type created_date: datetime
    :param description: Description of the plan
    :type description: str
    :param id: Id of the plan
    :type id: str
    :param modified_by_identity: Identity that last modified this plan. Defaults to null for records before upgrading to ScaledAgileViewComponent4.
    :type modified_by_identity: :class:`IdentityRef <azure.devops.v5_1.work.models.IdentityRef>`
    :param modified_date: Date when the plan was last modified. Default to CreatedDate when the plan is first created.
    :type modified_date: datetime
    :param name: Name of the plan
    :type name: str
    :param properties: The PlanPropertyCollection instance associated with the plan. These are dependent on the type of the plan. For example, DeliveryTimelineView, it would be of type DeliveryViewPropertyCollection.
    :type properties: object
    :param revision: Revision of the plan. Used to safeguard users from overwriting each other's changes.
    :type revision: int
    :param type: Type of the plan
    :type type: object
    :param url: The resource url to locate the plan via rest api
    :type url: str
    :param user_permissions: Bit flag indicating set of permissions a user has to the plan.
    :type user_permissions: object
    """

    _attribute_map = {
        'created_by_identity': {'key': 'createdByIdentity', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'modified_by_identity': {'key': 'modifiedByIdentity', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'user_permissions': {'key': 'userPermissions', 'type': 'object'}
    }

    def __init__(self, created_by_identity=None, created_date=None, description=None, id=None, modified_by_identity=None, modified_date=None, name=None, properties=None, revision=None, type=None, url=None, user_permissions=None):
        super(Plan, self).__init__()
        self.created_by_identity = created_by_identity
        self.created_date = created_date
        self.description = description
        self.id = id
        self.modified_by_identity = modified_by_identity
        self.modified_date = modified_date
        self.name = name
        self.properties = properties
        self.revision = revision
        self.type = type
        self.url = url
        self.user_permissions = user_permissions


class PlanViewData(Model):
    """
    Base class for plan view data contracts. Anything common goes here.

    :param id:
    :type id: str
    :param revision:
    :type revision: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, revision=None):
        super(PlanViewData, self).__init__()
        self.id = id
        self.revision = revision


class PredefinedQuery(Model):
    """
    Represents a single pre-defined query.

    :param has_more: Whether or not the query returned the complete set of data or if the data was truncated.
    :type has_more: bool
    :param id: Id of the query
    :type id: str
    :param name: Localized name of the query
    :type name: str
    :param results: The results of the query.  This will be a set of WorkItem objects with only the 'id' set.  The client is responsible for paging in the data as needed.
    :type results: list of :class:`WorkItem <azure.devops.v5_1.work.models.WorkItem>`
    :param url: REST API Url to use to retrieve results for this query
    :type url: str
    :param web_url: Url to use to display a page in the browser with the results of this query
    :type web_url: str
    """

    _attribute_map = {
        'has_more': {'key': 'hasMore', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'results': {'key': 'results', 'type': '[WorkItem]'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, has_more=None, id=None, name=None, results=None, url=None, web_url=None):
        super(PredefinedQuery, self).__init__()
        self.has_more = has_more
        self.id = id
        self.name = name
        self.results = results
        self.url = url
        self.web_url = web_url


class ProcessConfiguration(Model):
    """
    Process Configurations for the project

    :param bug_work_items: Details about bug work items
    :type bug_work_items: :class:`CategoryConfiguration <azure.devops.v5_1.work.models.CategoryConfiguration>`
    :param portfolio_backlogs: Details about portfolio backlogs
    :type portfolio_backlogs: list of :class:`CategoryConfiguration <azure.devops.v5_1.work.models.CategoryConfiguration>`
    :param requirement_backlog: Details of requirement backlog
    :type requirement_backlog: :class:`CategoryConfiguration <azure.devops.v5_1.work.models.CategoryConfiguration>`
    :param task_backlog: Details of task backlog
    :type task_backlog: :class:`CategoryConfiguration <azure.devops.v5_1.work.models.CategoryConfiguration>`
    :param type_fields: Type fields for the process configuration
    :type type_fields: dict
    :param url:
    :type url: str
    """

    _attribute_map = {
        'bug_work_items': {'key': 'bugWorkItems', 'type': 'CategoryConfiguration'},
        'portfolio_backlogs': {'key': 'portfolioBacklogs', 'type': '[CategoryConfiguration]'},
        'requirement_backlog': {'key': 'requirementBacklog', 'type': 'CategoryConfiguration'},
        'task_backlog': {'key': 'taskBacklog', 'type': 'CategoryConfiguration'},
        'type_fields': {'key': 'typeFields', 'type': '{WorkItemFieldReference}'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, bug_work_items=None, portfolio_backlogs=None, requirement_backlog=None, task_backlog=None, type_fields=None, url=None):
        super(ProcessConfiguration, self).__init__()
        self.bug_work_items = bug_work_items
        self.portfolio_backlogs = portfolio_backlogs
        self.requirement_backlog = requirement_backlog
        self.task_backlog = task_backlog
        self.type_fields = type_fields
        self.url = url


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


class ReorderOperation(Model):
    """
    Represents a reorder request for one or more work items.

    :param ids: IDs of the work items to be reordered.  Must be valid WorkItem Ids.
    :type ids: list of int
    :param iteration_path: IterationPath for reorder operation. This is only used when we reorder from the Iteration Backlog
    :type iteration_path: str
    :param next_id: ID of the work item that should be after the reordered items. Can use 0 to specify the end of the list.
    :type next_id: int
    :param parent_id: Parent ID for all of the work items involved in this operation. Can use 0 to indicate the items don't have a parent.
    :type parent_id: int
    :param previous_id: ID of the work item that should be before the reordered items. Can use 0 to specify the beginning of the list.
    :type previous_id: int
    """

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'iteration_path': {'key': 'iterationPath', 'type': 'str'},
        'next_id': {'key': 'nextId', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'previous_id': {'key': 'previousId', 'type': 'int'}
    }

    def __init__(self, ids=None, iteration_path=None, next_id=None, parent_id=None, previous_id=None):
        super(ReorderOperation, self).__init__()
        self.ids = ids
        self.iteration_path = iteration_path
        self.next_id = next_id
        self.parent_id = parent_id
        self.previous_id = previous_id


class ReorderResult(Model):
    """
    Represents a reorder result for a work item.

    :param id: The ID of the work item that was reordered.
    :type id: int
    :param order: The updated order value of the work item that was reordered.
    :type order: float
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'order': {'key': 'order', 'type': 'float'}
    }

    def __init__(self, id=None, order=None):
        super(ReorderResult, self).__init__()
        self.id = id
        self.order = order


class Rule(Model):
    """
    :param clauses:
    :type clauses: list of :class:`FilterClause <azure.devops.v5_1.work.models.FilterClause>`
    :param filter:
    :type filter: str
    :param is_enabled:
    :type is_enabled: str
    :param name:
    :type name: str
    :param settings:
    :type settings: dict
    """

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[FilterClause]'},
        'filter': {'key': 'filter', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'}
    }

    def __init__(self, clauses=None, filter=None, is_enabled=None, name=None, settings=None):
        super(Rule, self).__init__()
        self.clauses = clauses
        self.filter = filter
        self.is_enabled = is_enabled
        self.name = name
        self.settings = settings


class TeamContext(Model):
    """
    The Team Context for an operation.

    :param project: The team project Id or name.  Ignored if ProjectId is set.
    :type project: str
    :param project_id: The Team Project ID.  Required if Project is not set.
    :type project_id: str
    :param team: The Team Id or name.  Ignored if TeamId is set.
    :type team: str
    :param team_id: The Team Id
    :type team_id: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'team': {'key': 'team', 'type': 'str'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, project=None, project_id=None, team=None, team_id=None):
        super(TeamContext, self).__init__()
        self.project = project
        self.project_id = project_id
        self.team = team
        self.team_id = team_id


class TeamFieldValue(Model):
    """
    Represents a single TeamFieldValue

    :param include_children:
    :type include_children: bool
    :param value:
    :type value: str
    """

    _attribute_map = {
        'include_children': {'key': 'includeChildren', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, include_children=None, value=None):
        super(TeamFieldValue, self).__init__()
        self.include_children = include_children
        self.value = value


class TeamFieldValuesPatch(Model):
    """
    Expected data from PATCH

    :param default_value:
    :type default_value: str
    :param values:
    :type values: list of :class:`TeamFieldValue <azure.devops.v5_1.work.models.TeamFieldValue>`
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'values': {'key': 'values', 'type': '[TeamFieldValue]'}
    }

    def __init__(self, default_value=None, values=None):
        super(TeamFieldValuesPatch, self).__init__()
        self.default_value = default_value
        self.values = values


class TeamIterationAttributes(Model):
    """
    :param finish_date: Finish date of the iteration. Date-only, correct unadjusted at midnight in UTC.
    :type finish_date: datetime
    :param start_date: Start date of the iteration. Date-only, correct unadjusted at midnight in UTC.
    :type start_date: datetime
    :param time_frame: Time frame of the iteration, such as past, current or future.
    :type time_frame: object
    """

    _attribute_map = {
        'finish_date': {'key': 'finishDate', 'type': 'iso-8601'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'time_frame': {'key': 'timeFrame', 'type': 'object'}
    }

    def __init__(self, finish_date=None, start_date=None, time_frame=None):
        super(TeamIterationAttributes, self).__init__()
        self.finish_date = finish_date
        self.start_date = start_date
        self.time_frame = time_frame


class TeamSettingsDataContractBase(Model):
    """
    Base class for TeamSettings data contracts. Anything common goes here.

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, url=None):
        super(TeamSettingsDataContractBase, self).__init__()
        self._links = _links
        self.url = url


class TeamSettingsDaysOff(TeamSettingsDataContractBase):
    """
    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param days_off:
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, _links=None, url=None, days_off=None):
        super(TeamSettingsDaysOff, self).__init__(_links=_links, url=url)
        self.days_off = days_off


class TeamSettingsDaysOffPatch(Model):
    """
    :param days_off:
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    """

    _attribute_map = {
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, days_off=None):
        super(TeamSettingsDaysOffPatch, self).__init__()
        self.days_off = days_off


class TeamSettingsIteration(TeamSettingsDataContractBase):
    """
    Represents a shallow ref for a single iteration.

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param attributes: Attributes of the iteration such as start and end date.
    :type attributes: :class:`TeamIterationAttributes <azure.devops.v5_1.work.models.TeamIterationAttributes>`
    :param id: Id of the iteration.
    :type id: str
    :param name: Name of the iteration.
    :type name: str
    :param path: Relative path of the iteration.
    :type path: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'TeamIterationAttributes'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, _links=None, url=None, attributes=None, id=None, name=None, path=None):
        super(TeamSettingsIteration, self).__init__(_links=_links, url=url)
        self.attributes = attributes
        self.id = id
        self.name = name
        self.path = path


class TeamSettingsPatch(Model):
    """
    Data contract for what we expect to receive when PATCH

    :param backlog_iteration:
    :type backlog_iteration: str
    :param backlog_visibilities:
    :type backlog_visibilities: dict
    :param bugs_behavior:
    :type bugs_behavior: object
    :param default_iteration:
    :type default_iteration: str
    :param default_iteration_macro:
    :type default_iteration_macro: str
    :param working_days:
    :type working_days: list of str
    """

    _attribute_map = {
        'backlog_iteration': {'key': 'backlogIteration', 'type': 'str'},
        'backlog_visibilities': {'key': 'backlogVisibilities', 'type': '{bool}'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'default_iteration': {'key': 'defaultIteration', 'type': 'str'},
        'default_iteration_macro': {'key': 'defaultIterationMacro', 'type': 'str'},
        'working_days': {'key': 'workingDays', 'type': '[object]'}
    }

    def __init__(self, backlog_iteration=None, backlog_visibilities=None, bugs_behavior=None, default_iteration=None, default_iteration_macro=None, working_days=None):
        super(TeamSettingsPatch, self).__init__()
        self.backlog_iteration = backlog_iteration
        self.backlog_visibilities = backlog_visibilities
        self.bugs_behavior = bugs_behavior
        self.default_iteration = default_iteration
        self.default_iteration_macro = default_iteration_macro
        self.working_days = working_days


class TimelineCriteriaStatus(Model):
    """
    :param message:
    :type message: str
    :param type:
    :type type: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineCriteriaStatus, self).__init__()
        self.message = message
        self.type = type


class TimelineIterationStatus(Model):
    """
    :param message:
    :type message: str
    :param type:
    :type type: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineIterationStatus, self).__init__()
        self.message = message
        self.type = type


class TimelineTeamData(Model):
    """
    :param backlog: Backlog matching the mapped backlog associated with this team.
    :type backlog: :class:`BacklogLevel <azure.devops.v5_1.work.models.BacklogLevel>`
    :param field_reference_names: The field reference names of the work item data
    :type field_reference_names: list of str
    :param id: The id of the team
    :type id: str
    :param is_expanded: Was iteration and work item data retrieved for this team. <remarks> Teams with IsExpanded false have not had their iteration, work item, and field related data queried and will never contain this data. If true then these items are queried and, if there are items in the queried range, there will be data. </remarks>
    :type is_expanded: bool
    :param iterations: The iteration data, including the work items, in the queried date range.
    :type iterations: list of :class:`TimelineTeamIteration <azure.devops.v5_1.work.models.TimelineTeamIteration>`
    :param name: The name of the team
    :type name: str
    :param order_by_field: The order by field name of this team
    :type order_by_field: str
    :param partially_paged_field_reference_names: The field reference names of the partially paged work items, such as ID, WorkItemType
    :type partially_paged_field_reference_names: list of str
    :param project_id: The project id the team belongs team
    :type project_id: str
    :param status: Status for this team.
    :type status: :class:`TimelineTeamStatus <azure.devops.v5_1.work.models.TimelineTeamStatus>`
    :param team_field_default_value: The team field default value
    :type team_field_default_value: str
    :param team_field_name: The team field name of this team
    :type team_field_name: str
    :param team_field_values: The team field values
    :type team_field_values: list of :class:`TeamFieldValue <azure.devops.v5_1.work.models.TeamFieldValue>`
    :param work_item_type_colors: Colors for the work item types.
    :type work_item_type_colors: list of :class:`WorkItemColor <azure.devops.v5_1.work.models.WorkItemColor>`
    """

    _attribute_map = {
        'backlog': {'key': 'backlog', 'type': 'BacklogLevel'},
        'field_reference_names': {'key': 'fieldReferenceNames', 'type': '[str]'},
        'id': {'key': 'id', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'iterations': {'key': 'iterations', 'type': '[TimelineTeamIteration]'},
        'name': {'key': 'name', 'type': 'str'},
        'order_by_field': {'key': 'orderByField', 'type': 'str'},
        'partially_paged_field_reference_names': {'key': 'partiallyPagedFieldReferenceNames', 'type': '[str]'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'TimelineTeamStatus'},
        'team_field_default_value': {'key': 'teamFieldDefaultValue', 'type': 'str'},
        'team_field_name': {'key': 'teamFieldName', 'type': 'str'},
        'team_field_values': {'key': 'teamFieldValues', 'type': '[TeamFieldValue]'},
        'work_item_type_colors': {'key': 'workItemTypeColors', 'type': '[WorkItemColor]'}
    }

    def __init__(self, backlog=None, field_reference_names=None, id=None, is_expanded=None, iterations=None, name=None, order_by_field=None, partially_paged_field_reference_names=None, project_id=None, status=None, team_field_default_value=None, team_field_name=None, team_field_values=None, work_item_type_colors=None):
        super(TimelineTeamData, self).__init__()
        self.backlog = backlog
        self.field_reference_names = field_reference_names
        self.id = id
        self.is_expanded = is_expanded
        self.iterations = iterations
        self.name = name
        self.order_by_field = order_by_field
        self.partially_paged_field_reference_names = partially_paged_field_reference_names
        self.project_id = project_id
        self.status = status
        self.team_field_default_value = team_field_default_value
        self.team_field_name = team_field_name
        self.team_field_values = team_field_values
        self.work_item_type_colors = work_item_type_colors


class TimelineTeamIteration(Model):
    """
    :param css_node_id: The iteration CSS Node Id
    :type css_node_id: str
    :param finish_date: The end date of the iteration
    :type finish_date: datetime
    :param name: The iteration name
    :type name: str
    :param partially_paged_work_items: All the partially paged workitems in this iteration.
    :type partially_paged_work_items: list of [object]
    :param path: The iteration path
    :type path: str
    :param start_date: The start date of the iteration
    :type start_date: datetime
    :param status: The status of this iteration
    :type status: :class:`TimelineIterationStatus <azure.devops.v5_1.work.models.TimelineIterationStatus>`
    :param work_items: The work items that have been paged in this iteration
    :type work_items: list of [object]
    """

    _attribute_map = {
        'css_node_id': {'key': 'cssNodeId', 'type': 'str'},
        'finish_date': {'key': 'finishDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'partially_paged_work_items': {'key': 'partiallyPagedWorkItems', 'type': '[[object]]'},
        'path': {'key': 'path', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'TimelineIterationStatus'},
        'work_items': {'key': 'workItems', 'type': '[[object]]'}
    }

    def __init__(self, css_node_id=None, finish_date=None, name=None, partially_paged_work_items=None, path=None, start_date=None, status=None, work_items=None):
        super(TimelineTeamIteration, self).__init__()
        self.css_node_id = css_node_id
        self.finish_date = finish_date
        self.name = name
        self.partially_paged_work_items = partially_paged_work_items
        self.path = path
        self.start_date = start_date
        self.status = status
        self.work_items = work_items


class TimelineTeamStatus(Model):
    """
    :param message:
    :type message: str
    :param type:
    :type type: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, type=None):
        super(TimelineTeamStatus, self).__init__()
        self.message = message
        self.type = type


class UpdatePlan(Model):
    """
    :param description: Description of the plan
    :type description: str
    :param name: Name of the plan to create.
    :type name: str
    :param properties: Plan properties.
    :type properties: object
    :param revision: Revision of the plan that was updated - the value used here should match the one the server gave the client in the Plan.
    :type revision: int
    :param type: Type of the plan
    :type type: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, properties=None, revision=None, type=None):
        super(UpdatePlan, self).__init__()
        self.description = description
        self.name = name
        self.properties = properties
        self.revision = revision
        self.type = type


class WorkItemColor(Model):
    """
    Work item color and icon.

    :param icon:
    :type icon: str
    :param primary_color:
    :type primary_color: str
    :param work_item_type_name:
    :type work_item_type_name: str
    """

    _attribute_map = {
        'icon': {'key': 'icon', 'type': 'str'},
        'primary_color': {'key': 'primaryColor', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, icon=None, primary_color=None, work_item_type_name=None):
        super(WorkItemColor, self).__init__()
        self.icon = icon
        self.primary_color = primary_color
        self.work_item_type_name = work_item_type_name


class WorkItemFieldReference(Model):
    """
    Reference to a field in a work item

    :param name: The friendly name of the field.
    :type name: str
    :param reference_name: The reference name of the field.
    :type reference_name: str
    :param url: The REST URL of the resource.
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None):
        super(WorkItemFieldReference, self).__init__()
        self.name = name
        self.reference_name = reference_name
        self.url = url


class WorkItemLink(Model):
    """
    A link between two work items.

    :param rel: The type of link.
    :type rel: str
    :param source: The source work item.
    :type source: :class:`WorkItemReference <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.WorkItemReference>`
    :param target: The target work item.
    :type target: :class:`WorkItemReference <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.WorkItemReference>`
    """

    _attribute_map = {
        'rel': {'key': 'rel', 'type': 'str'},
        'source': {'key': 'source', 'type': 'WorkItemReference'},
        'target': {'key': 'target', 'type': 'WorkItemReference'}
    }

    def __init__(self, rel=None, source=None, target=None):
        super(WorkItemLink, self).__init__()
        self.rel = rel
        self.source = source
        self.target = target


class WorkItemReference(Model):
    """
    Contains reference to a work item.

    :param id: Work item ID.
    :type id: int
    :param url: REST API URL of the resource
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemReference, self).__init__()
        self.id = id
        self.url = url


class WorkItemRelation(Link):
    """
    :param attributes: Collection of link attributes.
    :type attributes: dict
    :param rel: Relation type.
    :type rel: str
    :param url: Link url.
    :type url: str
    """

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(WorkItemRelation, self).__init__(attributes=attributes, rel=rel, url=url)


class WorkItemTrackingResourceReference(Model):
    """
    Base class for work item tracking resource references.

    :param url:
    :type url: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(WorkItemTrackingResourceReference, self).__init__()
        self.url = url


class WorkItemTypeReference(WorkItemTrackingResourceReference):
    """
    Reference to a work item type.

    :param url:
    :type url: str
    :param name: Name of the work item type.
    :type name: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, url=None, name=None):
        super(WorkItemTypeReference, self).__init__(url=url)
        self.name = name


class WorkItemTypeStateInfo(Model):
    """
    :param states: State name to state category map
    :type states: dict
    :param work_item_type_name: Work Item type name
    :type work_item_type_name: str
    """

    _attribute_map = {
        'states': {'key': 'states', 'type': '{str}'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, states=None, work_item_type_name=None):
        super(WorkItemTypeStateInfo, self).__init__()
        self.states = states
        self.work_item_type_name = work_item_type_name


class Board(BoardReference):
    """
    :param id: Id of the resource
    :type id: str
    :param name: Name of the resource
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param allowed_mappings:
    :type allowed_mappings: dict
    :param can_edit:
    :type can_edit: bool
    :param columns:
    :type columns: list of :class:`BoardColumn <azure.devops.v5_1.work.models.BoardColumn>`
    :param fields:
    :type fields: :class:`BoardFields <azure.devops.v5_1.work.models.BoardFields>`
    :param is_valid:
    :type is_valid: bool
    :param revision:
    :type revision: int
    :param rows:
    :type rows: list of :class:`BoardRow <azure.devops.v5_1.work.models.BoardRow>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_mappings': {'key': 'allowedMappings', 'type': '{{[str]}}'},
        'can_edit': {'key': 'canEdit', 'type': 'bool'},
        'columns': {'key': 'columns', 'type': '[BoardColumn]'},
        'fields': {'key': 'fields', 'type': 'BoardFields'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'revision': {'key': 'revision', 'type': 'int'},
        'rows': {'key': 'rows', 'type': '[BoardRow]'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, allowed_mappings=None, can_edit=None, columns=None, fields=None, is_valid=None, revision=None, rows=None):
        super(Board, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.allowed_mappings = allowed_mappings
        self.can_edit = can_edit
        self.columns = columns
        self.fields = fields
        self.is_valid = is_valid
        self.revision = revision
        self.rows = rows


class BoardChart(BoardChartReference):
    """
    :param name: Name of the resource
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    :param _links: The links for the resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param settings: The settings for the resource
    :type settings: dict
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'settings': {'key': 'settings', 'type': '{object}'}
    }

    def __init__(self, name=None, url=None, _links=None, settings=None):
        super(BoardChart, self).__init__(name=name, url=url)
        self._links = _links
        self.settings = settings


class CapacityContractBase(TeamSettingsDataContractBase):
    """
    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param activities: Collection of capacities associated with the team member
    :type activities: list of :class:`Activity <azure.devops.v5_1.work.models.Activity>`
    :param days_off: The days off associated with the team member
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None):
        super(CapacityContractBase, self).__init__(_links=_links, url=url)
        self.activities = activities
        self.days_off = days_off


class DeliveryViewData(PlanViewData):
    """
    Data contract for Data of Delivery View

    :param id:
    :type id: str
    :param revision:
    :type revision: int
    :param child_id_to_parent_id_map: Work item child id to parent id map
    :type child_id_to_parent_id_map: dict
    :param criteria_status: Filter criteria status of the timeline
    :type criteria_status: :class:`TimelineCriteriaStatus <azure.devops.v5_1.work.models.TimelineCriteriaStatus>`
    :param end_date: The end date of the delivery view data
    :type end_date: datetime
    :param max_expanded_teams: Max number of teams can be configured for a delivery plan.
    :type max_expanded_teams: int
    :param start_date: The start date for the delivery view data
    :type start_date: datetime
    :param teams: All the team data
    :type teams: list of :class:`TimelineTeamData <azure.devops.v5_1.work.models.TimelineTeamData>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'child_id_to_parent_id_map': {'key': 'childIdToParentIdMap', 'type': '{int}'},
        'criteria_status': {'key': 'criteriaStatus', 'type': 'TimelineCriteriaStatus'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'max_expanded_teams': {'key': 'maxExpandedTeams', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'teams': {'key': 'teams', 'type': '[TimelineTeamData]'}
    }

    def __init__(self, id=None, revision=None, child_id_to_parent_id_map=None, criteria_status=None, end_date=None, max_expanded_teams=None, start_date=None, teams=None):
        super(DeliveryViewData, self).__init__(id=id, revision=revision)
        self.child_id_to_parent_id_map = child_id_to_parent_id_map
        self.criteria_status = criteria_status
        self.end_date = end_date
        self.max_expanded_teams = max_expanded_teams
        self.start_date = start_date
        self.teams = teams


class IterationWorkItems(TeamSettingsDataContractBase):
    """
    Represents work items in an iteration backlog

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param work_item_relations: Work item relations
    :type work_item_relations: list of :class:`WorkItemLink <azure.devops.v5_1.work.models.WorkItemLink>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_relations': {'key': 'workItemRelations', 'type': '[WorkItemLink]'}
    }

    def __init__(self, _links=None, url=None, work_item_relations=None):
        super(IterationWorkItems, self).__init__(_links=_links, url=url)
        self.work_item_relations = work_item_relations


class TeamFieldValues(TeamSettingsDataContractBase):
    """
    Essentially a collection of team field values

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param default_value: The default team field value
    :type default_value: str
    :param field: Shallow ref to the field being used as a team field
    :type field: :class:`FieldReference <azure.devops.v5_1.work.models.FieldReference>`
    :param values: Collection of all valid team field values
    :type values: list of :class:`TeamFieldValue <azure.devops.v5_1.work.models.TeamFieldValue>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'field': {'key': 'field', 'type': 'FieldReference'},
        'values': {'key': 'values', 'type': '[TeamFieldValue]'}
    }

    def __init__(self, _links=None, url=None, default_value=None, field=None, values=None):
        super(TeamFieldValues, self).__init__(_links=_links, url=url)
        self.default_value = default_value
        self.field = field
        self.values = values


class TeamMemberCapacity(CapacityContractBase):
    """
    Represents capacity for a specific team member

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param activities: Collection of capacities associated with the team member
    :type activities: list of :class:`Activity <azure.devops.v5_1.work.models.Activity>`
    :param days_off: The days off associated with the team member
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    :param team_member: Shallow Ref to the associated team member
    :type team_member: :class:`Member <azure.devops.v5_1.work.models.Member>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'},
        'team_member': {'key': 'teamMember', 'type': 'Member'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None, team_member=None):
        super(TeamMemberCapacity, self).__init__(_links=_links, url=url, activities=activities, days_off=days_off)
        self.team_member = team_member


class TeamMemberCapacityIdentityRef(CapacityContractBase):
    """
    Represents capacity for a specific team member

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param activities: Collection of capacities associated with the team member
    :type activities: list of :class:`Activity <azure.devops.v5_1.work.models.Activity>`
    :param days_off: The days off associated with the team member
    :type days_off: list of :class:`DateRange <azure.devops.v5_1.work.models.DateRange>`
    :param team_member: Identity ref of the associated team member
    :type team_member: :class:`IdentityRef <azure.devops.v5_1.work.models.IdentityRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'activities': {'key': 'activities', 'type': '[Activity]'},
        'days_off': {'key': 'daysOff', 'type': '[DateRange]'},
        'team_member': {'key': 'teamMember', 'type': 'IdentityRef'}
    }

    def __init__(self, _links=None, url=None, activities=None, days_off=None, team_member=None):
        super(TeamMemberCapacityIdentityRef, self).__init__(_links=_links, url=url, activities=activities, days_off=days_off)
        self.team_member = team_member


class TeamSetting(TeamSettingsDataContractBase):
    """
    Data contract for TeamSettings

    :param _links: Collection of links relevant to resource
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.work.models.ReferenceLinks>`
    :param url: Full http link to the resource
    :type url: str
    :param backlog_iteration: Backlog Iteration
    :type backlog_iteration: :class:`TeamSettingsIteration <azure.devops.v5_1.work.models.TeamSettingsIteration>`
    :param backlog_visibilities: Information about categories that are visible on the backlog.
    :type backlog_visibilities: dict
    :param bugs_behavior: BugsBehavior (Off, AsTasks, AsRequirements, ...)
    :type bugs_behavior: object
    :param default_iteration: Default Iteration, the iteration used when creating a new work item on the queries page.
    :type default_iteration: :class:`TeamSettingsIteration <azure.devops.v5_1.work.models.TeamSettingsIteration>`
    :param default_iteration_macro: Default Iteration macro (if any)
    :type default_iteration_macro: str
    :param working_days: Days that the team is working
    :type working_days: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'url': {'key': 'url', 'type': 'str'},
        'backlog_iteration': {'key': 'backlogIteration', 'type': 'TeamSettingsIteration'},
        'backlog_visibilities': {'key': 'backlogVisibilities', 'type': '{bool}'},
        'bugs_behavior': {'key': 'bugsBehavior', 'type': 'object'},
        'default_iteration': {'key': 'defaultIteration', 'type': 'TeamSettingsIteration'},
        'default_iteration_macro': {'key': 'defaultIterationMacro', 'type': 'str'},
        'working_days': {'key': 'workingDays', 'type': '[object]'}
    }

    def __init__(self, _links=None, url=None, backlog_iteration=None, backlog_visibilities=None, bugs_behavior=None, default_iteration=None, default_iteration_macro=None, working_days=None):
        super(TeamSetting, self).__init__(_links=_links, url=url)
        self.backlog_iteration = backlog_iteration
        self.backlog_visibilities = backlog_visibilities
        self.bugs_behavior = bugs_behavior
        self.default_iteration = default_iteration
        self.default_iteration_macro = default_iteration_macro
        self.working_days = working_days


class WorkItemCommentVersionRef(WorkItemTrackingResourceReference):
    """
    Represents the reference to a specific version of a comment on a Work Item.

    :param url:
    :type url: str
    :param comment_id: The id assigned to the comment.
    :type comment_id: int
    :param created_in_revision: [Internal] The work item revision where this comment was originally added.
    :type created_in_revision: int
    :param is_deleted: [Internal] Specifies whether comment was deleted.
    :type is_deleted: bool
    :param text: [Internal] The text of the comment.
    :type text: str
    :param version: The version number.
    :type version: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_in_revision': {'key': 'createdInRevision', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, comment_id=None, created_in_revision=None, is_deleted=None, text=None, version=None):
        super(WorkItemCommentVersionRef, self).__init__(url=url)
        self.comment_id = comment_id
        self.created_in_revision = created_in_revision
        self.is_deleted = is_deleted
        self.text = text
        self.version = version


class WorkItemTrackingResource(WorkItemTrackingResourceReference):
    """
    Base class for WIT REST resources.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.ReferenceLinks>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links


class WorkItem(WorkItemTrackingResource):
    """
    Describes a work item.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.ReferenceLinks>`
    :param comment_version_ref: Reference to a specific version of the comment added/edited/deleted in this revision.
    :type comment_version_ref: :class:`WorkItemCommentVersionRef <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.WorkItemCommentVersionRef>`
    :param fields: Map of field and values for the work item.
    :type fields: dict
    :param id: The work item ID.
    :type id: int
    :param relations: Relations of the work item.
    :type relations: list of :class:`WorkItemRelation <azure.devops.v5_1.microsoft._team_foundation._work_item_tracking._web_api.models.WorkItemRelation>`
    :param rev: Revision number of the work item.
    :type rev: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_version_ref': {'key': 'commentVersionRef', 'type': 'WorkItemCommentVersionRef'},
        'fields': {'key': 'fields', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': '[WorkItemRelation]'},
        'rev': {'key': 'rev', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_version_ref=None, fields=None, id=None, relations=None, rev=None):
        super(WorkItem, self).__init__(url=url, _links=_links)
        self.comment_version_ref = comment_version_ref
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev


__all__ = [
    'Activity',
    'BacklogColumn',
    'BacklogConfiguration',
    'BacklogFields',
    'BacklogLevel',
    'BacklogLevelConfiguration',
    'BacklogLevelWorkItems',
    'BoardBadge',
    'BoardCardRuleSettings',
    'BoardCardSettings',
    'BoardChartReference',
    'BoardColumn',
    'BoardFields',
    'BoardReference',
    'BoardRow',
    'BoardSuggestedValue',
    'BoardUserSettings',
    'CapacityPatch',
    'CategoryConfiguration',
    'CreatePlan',
    'DateRange',
    'FieldReference',
    'FilterClause',
    'GraphSubjectBase',
    'IdentityRef',
    'Link',
    'Member',
    'ParentChildWIMap',
    'Plan',
    'PlanViewData',
    'PredefinedQuery',
    'ProcessConfiguration',
    'ReferenceLinks',
    'ReorderOperation',
    'ReorderResult',
    'Rule',
    'TeamContext',
    'TeamFieldValue',
    'TeamFieldValuesPatch',
    'TeamIterationAttributes',
    'TeamSettingsDataContractBase',
    'TeamSettingsDaysOff',
    'TeamSettingsDaysOffPatch',
    'TeamSettingsIteration',
    'TeamSettingsPatch',
    'TimelineCriteriaStatus',
    'TimelineIterationStatus',
    'TimelineTeamData',
    'TimelineTeamIteration',
    'TimelineTeamStatus',
    'UpdatePlan',
    'WorkItemColor',
    'WorkItemFieldReference',
    'WorkItemLink',
    'WorkItemReference',
    'WorkItemRelation',
    'WorkItemTrackingResourceReference',
    'WorkItemTypeReference',
    'WorkItemTypeStateInfo',
    'Board',
    'BoardChart',
    'CapacityContractBase',
    'DeliveryViewData',
    'IterationWorkItems',
    'TeamFieldValues',
    'TeamMemberCapacity',
    'TeamMemberCapacityIdentityRef',
    'TeamSetting',
    'WorkItemCommentVersionRef',
    'WorkItemTrackingResource',
    'WorkItem',
]
