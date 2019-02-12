# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AccountMyWorkResult(Model):
    """AccountMyWorkResult.

    :param query_size_limit_exceeded: True, when length of WorkItemDetails is same as the limit
    :type query_size_limit_exceeded: bool
    :param work_item_details: WorkItem Details
    :type work_item_details: list of :class:`AccountWorkWorkItemModel <work-item-tracking.v4_0.models.AccountWorkWorkItemModel>`
    """

    _attribute_map = {
        'query_size_limit_exceeded': {'key': 'querySizeLimitExceeded', 'type': 'bool'},
        'work_item_details': {'key': 'workItemDetails', 'type': '[AccountWorkWorkItemModel]'}
    }

    def __init__(self, query_size_limit_exceeded=None, work_item_details=None):
        super(AccountMyWorkResult, self).__init__()
        self.query_size_limit_exceeded = query_size_limit_exceeded
        self.work_item_details = work_item_details



class AccountRecentActivityWorkItemModel(Model):
    """AccountRecentActivityWorkItemModel.

    :param activity_date: Date of the last Activity by the user
    :type activity_date: datetime
    :param activity_type: Type of the activity
    :type activity_type: object
    :param assigned_to: Assigned To
    :type assigned_to: str
    :param changed_date: Last changed date of the work item
    :type changed_date: datetime
    :param id: Work Item Id
    :type id: int
    :param identity_id: TeamFoundationId of the user this activity belongs to
    :type identity_id: str
    :param state: State of the work item
    :type state: str
    :param team_project: Team project the work item belongs to
    :type team_project: str
    :param title: Title of the work item
    :type title: str
    :param work_item_type: Type of Work Item
    :type work_item_type: str
    """

    _attribute_map = {
        'activity_date': {'key': 'activityDate', 'type': 'iso-8601'},
        'activity_type': {'key': 'activityType', 'type': 'object'},
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, activity_date=None, activity_type=None, assigned_to=None, changed_date=None, id=None, identity_id=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountRecentActivityWorkItemModel, self).__init__()
        self.activity_date = activity_date
        self.activity_type = activity_type
        self.assigned_to = assigned_to
        self.changed_date = changed_date
        self.id = id
        self.identity_id = identity_id
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type



class AccountRecentMentionWorkItemModel(Model):
    """AccountRecentMentionWorkItemModel.

    :param assigned_to: Assigned To
    :type assigned_to: str
    :param id: Work Item Id
    :type id: int
    :param mentioned_date_field: Lastest date that the user were mentioned
    :type mentioned_date_field: datetime
    :param state: State of the work item
    :type state: str
    :param team_project: Team project the work item belongs to
    :type team_project: str
    :param title: Title of the work item
    :type title: str
    :param work_item_type: Type of Work Item
    :type work_item_type: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'mentioned_date_field': {'key': 'mentionedDateField', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, mentioned_date_field=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountRecentMentionWorkItemModel, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.mentioned_date_field = mentioned_date_field
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type



class AccountWorkWorkItemModel(Model):
    """AccountWorkWorkItemModel.

    :param assigned_to:
    :type assigned_to: str
    :param changed_date:
    :type changed_date: datetime
    :param id:
    :type id: int
    :param state:
    :type state: str
    :param team_project:
    :type team_project: str
    :param title:
    :type title: str
    :param work_item_type:
    :type work_item_type: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'team_project': {'key': 'teamProject', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, changed_date=None, id=None, state=None, team_project=None, title=None, work_item_type=None):
        super(AccountWorkWorkItemModel, self).__init__()
        self.assigned_to = assigned_to
        self.changed_date = changed_date
        self.id = id
        self.state = state
        self.team_project = team_project
        self.title = title
        self.work_item_type = work_item_type



class ArtifactUriQuery(Model):
    """ArtifactUriQuery.

    :param artifact_uris:
    :type artifact_uris: list of str
    """

    _attribute_map = {
        'artifact_uris': {'key': 'artifactUris', 'type': '[str]'}
    }

    def __init__(self, artifact_uris=None):
        super(ArtifactUriQuery, self).__init__()
        self.artifact_uris = artifact_uris



class ArtifactUriQueryResult(Model):
    """ArtifactUriQueryResult.

    :param artifact_uris_query_result:
    :type artifact_uris_query_result: dict
    """

    _attribute_map = {
        'artifact_uris_query_result': {'key': 'artifactUrisQueryResult', 'type': '{[WorkItemReference]}'}
    }

    def __init__(self, artifact_uris_query_result=None):
        super(ArtifactUriQueryResult, self).__init__()
        self.artifact_uris_query_result = artifact_uris_query_result



class AttachmentReference(Model):
    """AttachmentReference.

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
        super(AttachmentReference, self).__init__()
        self.id = id
        self.url = url



class FieldsToEvaluate(Model):
    """FieldsToEvaluate.

    :param fields:
    :type fields: list of str
    :param field_updates:
    :type field_updates: dict
    :param field_values:
    :type field_values: dict
    :param rules_from:
    :type rules_from: list of str
    """

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[str]'},
        'field_updates': {'key': 'fieldUpdates', 'type': '{object}'},
        'field_values': {'key': 'fieldValues', 'type': '{object}'},
        'rules_from': {'key': 'rulesFrom', 'type': '[str]'}
    }

    def __init__(self, fields=None, field_updates=None, field_values=None, rules_from=None):
        super(FieldsToEvaluate, self).__init__()
        self.fields = fields
        self.field_updates = field_updates
        self.field_values = field_values
        self.rules_from = rules_from



class IdentityRef(Model):
    """IdentityRef.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
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
    :param url:
    :type url: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None):
        super(IdentityRef, self).__init__()
        self.directory_alias = directory_alias
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.profile_url = profile_url
        self.unique_name = unique_name
        self.url = url



class IdentityReference(IdentityRef):
    """IdentityReference.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
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
    :param url:
    :type url: str
    :param id:
    :type id: str
    :param name: Legacy back-compat property. This has been the WIT specific value from Constants. Will be hidden (but exists) on the client unless they are targeting the newest version
    :type name: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None, id=None, name=None):
        super(IdentityReference, self).__init__(directory_alias=directory_alias, display_name=display_name, image_url=image_url, inactive=inactive, is_aad_identity=is_aad_identity, is_container=is_container, profile_url=profile_url, unique_name=unique_name, url=url)
        self.id = id
        self.name = name



class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation
    :type path: str
    :param value: The value for the operation. This is either a primitive or a JToken.
    :type value: object
    """

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value



class Link(Model):
    """Link.

    :param attributes:
    :type attributes: dict
    :param rel:
    :type rel: str
    :param url:
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



class ProjectWorkItemStateColors(Model):
    """ProjectWorkItemStateColors.

    :param project_name: Project name
    :type project_name: str
    :param work_item_type_state_colors: State colors for all work item type in a project
    :type work_item_type_state_colors: list of :class:`WorkItemTypeStateColors <work-item-tracking.v4_0.models.WorkItemTypeStateColors>`
    """

    _attribute_map = {
        'project_name': {'key': 'projectName', 'type': 'str'},
        'work_item_type_state_colors': {'key': 'workItemTypeStateColors', 'type': '[WorkItemTypeStateColors]'}
    }

    def __init__(self, project_name=None, work_item_type_state_colors=None):
        super(ProjectWorkItemStateColors, self).__init__()
        self.project_name = project_name
        self.work_item_type_state_colors = work_item_type_state_colors



class ProvisioningResult(Model):
    """ProvisioningResult.

    :param provisioning_import_events:
    :type provisioning_import_events: list of str
    """

    _attribute_map = {
        'provisioning_import_events': {'key': 'provisioningImportEvents', 'type': '[str]'}
    }

    def __init__(self, provisioning_import_events=None):
        super(ProvisioningResult, self).__init__()
        self.provisioning_import_events = provisioning_import_events



class QueryHierarchyItemsResult(Model):
    """QueryHierarchyItemsResult.

    :param count:
    :type count: int
    :param has_more:
    :type has_more: bool
    :param value:
    :type value: list of :class:`QueryHierarchyItem <work-item-tracking.v4_0.models.QueryHierarchyItem>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'has_more': {'key': 'hasMore', 'type': 'bool'},
        'value': {'key': 'value', 'type': '[QueryHierarchyItem]'}
    }

    def __init__(self, count=None, has_more=None, value=None):
        super(QueryHierarchyItemsResult, self).__init__()
        self.count = count
        self.has_more = has_more
        self.value = value



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



class ReportingWorkItemLink(Model):
    """ReportingWorkItemLink.

    :param changed_by:
    :type changed_by: :class:`IdentityRef <work-item-tracking.v4_0.models.IdentityRef>`
    :param changed_date:
    :type changed_date: datetime
    :param changed_operation:
    :type changed_operation: object
    :param comment:
    :type comment: str
    :param is_active:
    :type is_active: bool
    :param link_type:
    :type link_type: str
    :param rel:
    :type rel: str
    :param source_id:
    :type source_id: int
    :param target_id:
    :type target_id: int
    """

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'changed_operation': {'key': 'changedOperation', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'link_type': {'key': 'linkType', 'type': 'str'},
        'rel': {'key': 'rel', 'type': 'str'},
        'source_id': {'key': 'sourceId', 'type': 'int'},
        'target_id': {'key': 'targetId', 'type': 'int'}
    }

    def __init__(self, changed_by=None, changed_date=None, changed_operation=None, comment=None, is_active=None, link_type=None, rel=None, source_id=None, target_id=None):
        super(ReportingWorkItemLink, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.changed_operation = changed_operation
        self.comment = comment
        self.is_active = is_active
        self.link_type = link_type
        self.rel = rel
        self.source_id = source_id
        self.target_id = target_id



class ReportingWorkItemRevisionsFilter(Model):
    """ReportingWorkItemRevisionsFilter.

    :param fields: A list of fields to return in work item revisions. Omit this parameter to get all reportable fields.
    :type fields: list of str
    :param include_deleted: Include deleted work item in the result.
    :type include_deleted: bool
    :param include_identity_ref: Return an identity reference instead of a string value for identity fields.
    :type include_identity_ref: bool
    :param include_latest_only: Include only the latest version of a work item, skipping over all previous revisions of the work item.
    :type include_latest_only: bool
    :param include_tag_ref: Include tag reference instead of string value for System.Tags field
    :type include_tag_ref: bool
    :param types: A list of types to filter the results to specific work item types. Omit this parameter to get work item revisions of all work item types.
    :type types: list of str
    """

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[str]'},
        'include_deleted': {'key': 'includeDeleted', 'type': 'bool'},
        'include_identity_ref': {'key': 'includeIdentityRef', 'type': 'bool'},
        'include_latest_only': {'key': 'includeLatestOnly', 'type': 'bool'},
        'include_tag_ref': {'key': 'includeTagRef', 'type': 'bool'},
        'types': {'key': 'types', 'type': '[str]'}
    }

    def __init__(self, fields=None, include_deleted=None, include_identity_ref=None, include_latest_only=None, include_tag_ref=None, types=None):
        super(ReportingWorkItemRevisionsFilter, self).__init__()
        self.fields = fields
        self.include_deleted = include_deleted
        self.include_identity_ref = include_identity_ref
        self.include_latest_only = include_latest_only
        self.include_tag_ref = include_tag_ref
        self.types = types



class StreamedBatch(Model):
    """StreamedBatch.

    :param continuation_token:
    :type continuation_token: str
    :param is_last_batch:
    :type is_last_batch: bool
    :param next_link:
    :type next_link: str
    :param values:
    :type values: list of object
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'is_last_batch': {'key': 'isLastBatch', 'type': 'bool'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'values': {'key': 'values', 'type': '[object]'}
    }

    def __init__(self, continuation_token=None, is_last_batch=None, next_link=None, values=None):
        super(StreamedBatch, self).__init__()
        self.continuation_token = continuation_token
        self.is_last_batch = is_last_batch
        self.next_link = next_link
        self.values = values



class TeamContext(Model):
    """TeamContext.

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



class Wiql(Model):
    """Wiql.

    :param query:
    :type query: str
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'}
    }

    def __init__(self, query=None):
        super(Wiql, self).__init__()
        self.query = query



class WorkArtifactLink(Model):
    """WorkArtifactLink.

    :param artifact_type:
    :type artifact_type: str
    :param link_type:
    :type link_type: str
    :param tool_type:
    :type tool_type: str
    """

    _attribute_map = {
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'link_type': {'key': 'linkType', 'type': 'str'},
        'tool_type': {'key': 'toolType', 'type': 'str'}
    }

    def __init__(self, artifact_type=None, link_type=None, tool_type=None):
        super(WorkArtifactLink, self).__init__()
        self.artifact_type = artifact_type
        self.link_type = link_type
        self.tool_type = tool_type



class WorkItemComments(Model):
    """WorkItemComments.

    :param comments:
    :type comments: list of :class:`WorkItemComment <work-item-tracking.v4_0.models.WorkItemComment>`
    :param count:
    :type count: int
    :param from_revision_count:
    :type from_revision_count: int
    :param total_count:
    :type total_count: int
    """

    _attribute_map = {
        'comments': {'key': 'comments', 'type': '[WorkItemComment]'},
        'count': {'key': 'count', 'type': 'int'},
        'from_revision_count': {'key': 'fromRevisionCount', 'type': 'int'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, comments=None, count=None, from_revision_count=None, total_count=None):
        super(WorkItemComments, self).__init__()
        self.comments = comments
        self.count = count
        self.from_revision_count = from_revision_count
        self.total_count = total_count



class WorkItemDeleteReference(Model):
    """WorkItemDeleteReference.

    :param code:
    :type code: int
    :param deleted_by:
    :type deleted_by: str
    :param deleted_date:
    :type deleted_date: str
    :param id:
    :type id: int
    :param message:
    :type message: str
    :param name:
    :type name: str
    :param project:
    :type project: str
    :param type:
    :type type: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'deleted_by': {'key': 'deletedBy', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, code=None, deleted_by=None, deleted_date=None, id=None, message=None, name=None, project=None, type=None, url=None):
        super(WorkItemDeleteReference, self).__init__()
        self.code = code
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.message = message
        self.name = name
        self.project = project
        self.type = type
        self.url = url



class WorkItemDeleteShallowReference(Model):
    """WorkItemDeleteShallowReference.

    :param id:
    :type id: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WorkItemDeleteShallowReference, self).__init__()
        self.id = id
        self.url = url



class WorkItemDeleteUpdate(Model):
    """WorkItemDeleteUpdate.

    :param is_deleted:
    :type is_deleted: bool
    """

    _attribute_map = {
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'}
    }

    def __init__(self, is_deleted=None):
        super(WorkItemDeleteUpdate, self).__init__()
        self.is_deleted = is_deleted



class WorkItemFieldOperation(Model):
    """WorkItemFieldOperation.

    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None):
        super(WorkItemFieldOperation, self).__init__()
        self.name = name
        self.reference_name = reference_name



class WorkItemFieldReference(Model):
    """WorkItemFieldReference.

    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    :param url:
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



class WorkItemFieldUpdate(Model):
    """WorkItemFieldUpdate.

    :param new_value:
    :type new_value: object
    :param old_value:
    :type old_value: object
    """

    _attribute_map = {
        'new_value': {'key': 'newValue', 'type': 'object'},
        'old_value': {'key': 'oldValue', 'type': 'object'}
    }

    def __init__(self, new_value=None, old_value=None):
        super(WorkItemFieldUpdate, self).__init__()
        self.new_value = new_value
        self.old_value = old_value



class WorkItemIcon(Model):
    """WorkItemIcon.

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
        super(WorkItemIcon, self).__init__()
        self.id = id
        self.url = url



class WorkItemLink(Model):
    """WorkItemLink.

    :param rel:
    :type rel: str
    :param source:
    :type source: :class:`WorkItemReference <work-item-tracking.v4_0.models.WorkItemReference>`
    :param target:
    :type target: :class:`WorkItemReference <work-item-tracking.v4_0.models.WorkItemReference>`
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



class WorkItemQueryClause(Model):
    """WorkItemQueryClause.

    :param clauses:
    :type clauses: list of :class:`WorkItemQueryClause <work-item-tracking.v4_0.models.WorkItemQueryClause>`
    :param field:
    :type field: :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    :param field_value:
    :type field_value: :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    :param is_field_value:
    :type is_field_value: bool
    :param logical_operator:
    :type logical_operator: object
    :param operator:
    :type operator: :class:`WorkItemFieldOperation <work-item-tracking.v4_0.models.WorkItemFieldOperation>`
    :param value:
    :type value: str
    """

    _attribute_map = {
        'clauses': {'key': 'clauses', 'type': '[WorkItemQueryClause]'},
        'field': {'key': 'field', 'type': 'WorkItemFieldReference'},
        'field_value': {'key': 'fieldValue', 'type': 'WorkItemFieldReference'},
        'is_field_value': {'key': 'isFieldValue', 'type': 'bool'},
        'logical_operator': {'key': 'logicalOperator', 'type': 'object'},
        'operator': {'key': 'operator', 'type': 'WorkItemFieldOperation'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, clauses=None, field=None, field_value=None, is_field_value=None, logical_operator=None, operator=None, value=None):
        super(WorkItemQueryClause, self).__init__()
        self.clauses = clauses
        self.field = field
        self.field_value = field_value
        self.is_field_value = is_field_value
        self.logical_operator = logical_operator
        self.operator = operator
        self.value = value



class WorkItemQueryResult(Model):
    """WorkItemQueryResult.

    :param as_of:
    :type as_of: datetime
    :param columns:
    :type columns: list of :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    :param query_result_type:
    :type query_result_type: object
    :param query_type:
    :type query_type: object
    :param sort_columns:
    :type sort_columns: list of :class:`WorkItemQuerySortColumn <work-item-tracking.v4_0.models.WorkItemQuerySortColumn>`
    :param work_item_relations:
    :type work_item_relations: list of :class:`WorkItemLink <work-item-tracking.v4_0.models.WorkItemLink>`
    :param work_items:
    :type work_items: list of :class:`WorkItemReference <work-item-tracking.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'as_of': {'key': 'asOf', 'type': 'iso-8601'},
        'columns': {'key': 'columns', 'type': '[WorkItemFieldReference]'},
        'query_result_type': {'key': 'queryResultType', 'type': 'object'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'sort_columns': {'key': 'sortColumns', 'type': '[WorkItemQuerySortColumn]'},
        'work_item_relations': {'key': 'workItemRelations', 'type': '[WorkItemLink]'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, as_of=None, columns=None, query_result_type=None, query_type=None, sort_columns=None, work_item_relations=None, work_items=None):
        super(WorkItemQueryResult, self).__init__()
        self.as_of = as_of
        self.columns = columns
        self.query_result_type = query_result_type
        self.query_type = query_type
        self.sort_columns = sort_columns
        self.work_item_relations = work_item_relations
        self.work_items = work_items



class WorkItemQuerySortColumn(Model):
    """WorkItemQuerySortColumn.

    :param descending:
    :type descending: bool
    :param field:
    :type field: :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    """

    _attribute_map = {
        'descending': {'key': 'descending', 'type': 'bool'},
        'field': {'key': 'field', 'type': 'WorkItemFieldReference'}
    }

    def __init__(self, descending=None, field=None):
        super(WorkItemQuerySortColumn, self).__init__()
        self.descending = descending
        self.field = field



class WorkItemReference(Model):
    """WorkItemReference.

    :param id:
    :type id: int
    :param url:
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
    """WorkItemRelation.

    :param attributes:
    :type attributes: dict
    :param rel:
    :type rel: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'rel': {'key': 'rel', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, attributes=None, rel=None, url=None):
        super(WorkItemRelation, self).__init__(attributes=attributes, rel=rel, url=url)



class WorkItemRelationUpdates(Model):
    """WorkItemRelationUpdates.

    :param added:
    :type added: list of :class:`WorkItemRelation <work-item-tracking.v4_0.models.WorkItemRelation>`
    :param removed:
    :type removed: list of :class:`WorkItemRelation <work-item-tracking.v4_0.models.WorkItemRelation>`
    :param updated:
    :type updated: list of :class:`WorkItemRelation <work-item-tracking.v4_0.models.WorkItemRelation>`
    """

    _attribute_map = {
        'added': {'key': 'added', 'type': '[WorkItemRelation]'},
        'removed': {'key': 'removed', 'type': '[WorkItemRelation]'},
        'updated': {'key': 'updated', 'type': '[WorkItemRelation]'}
    }

    def __init__(self, added=None, removed=None, updated=None):
        super(WorkItemRelationUpdates, self).__init__()
        self.added = added
        self.removed = removed
        self.updated = updated



class WorkItemStateColor(Model):
    """WorkItemStateColor.

    :param color: Color value
    :type color: str
    :param name: Work item type state name
    :type name: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, color=None, name=None):
        super(WorkItemStateColor, self).__init__()
        self.color = color
        self.name = name



class WorkItemStateTransition(Model):
    """WorkItemStateTransition.

    :param actions:
    :type actions: list of str
    :param to:
    :type to: str
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'to': {'key': 'to', 'type': 'str'}
    }

    def __init__(self, actions=None, to=None):
        super(WorkItemStateTransition, self).__init__()
        self.actions = actions
        self.to = to



class WorkItemTrackingResourceReference(Model):
    """WorkItemTrackingResourceReference.

    :param url:
    :type url: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(WorkItemTrackingResourceReference, self).__init__()
        self.url = url



class WorkItemTypeColor(Model):
    """WorkItemTypeColor.

    :param primary_color:
    :type primary_color: str
    :param secondary_color:
    :type secondary_color: str
    :param work_item_type_name:
    :type work_item_type_name: str
    """

    _attribute_map = {
        'primary_color': {'key': 'primaryColor', 'type': 'str'},
        'secondary_color': {'key': 'secondaryColor', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, primary_color=None, secondary_color=None, work_item_type_name=None):
        super(WorkItemTypeColor, self).__init__()
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.work_item_type_name = work_item_type_name



class WorkItemTypeColorAndIcon(Model):
    """WorkItemTypeColorAndIcon.

    :param color:
    :type color: str
    :param icon:
    :type icon: str
    :param work_item_type_name:
    :type work_item_type_name: str
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, color=None, icon=None, work_item_type_name=None):
        super(WorkItemTypeColorAndIcon, self).__init__()
        self.color = color
        self.icon = icon
        self.work_item_type_name = work_item_type_name



class WorkItemTypeFieldInstance(WorkItemFieldReference):
    """WorkItemTypeFieldInstance.

    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    :param url:
    :type url: str
    :param always_required:
    :type always_required: bool
    :param field:
    :type field: :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    :param help_text:
    :type help_text: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'always_required': {'key': 'alwaysRequired', 'type': 'bool'},
        'field': {'key': 'field', 'type': 'WorkItemFieldReference'},
        'help_text': {'key': 'helpText', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None, url=None, always_required=None, field=None, help_text=None):
        super(WorkItemTypeFieldInstance, self).__init__(name=name, reference_name=reference_name, url=url)
        self.always_required = always_required
        self.field = field
        self.help_text = help_text



class WorkItemTypeReference(WorkItemTrackingResourceReference):
    """WorkItemTypeReference.

    :param url:
    :type url: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, url=None, name=None):
        super(WorkItemTypeReference, self).__init__(url=url)
        self.name = name



class WorkItemTypeStateColors(Model):
    """WorkItemTypeStateColors.

    :param state_colors: Work item type state colors
    :type state_colors: list of :class:`WorkItemStateColor <work-item-tracking.v4_0.models.WorkItemStateColor>`
    :param work_item_type_name: Work item type name
    :type work_item_type_name: str
    """

    _attribute_map = {
        'state_colors': {'key': 'stateColors', 'type': '[WorkItemStateColor]'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, state_colors=None, work_item_type_name=None):
        super(WorkItemTypeStateColors, self).__init__()
        self.state_colors = state_colors
        self.work_item_type_name = work_item_type_name



class WorkItemTypeTemplate(Model):
    """WorkItemTypeTemplate.

    :param template:
    :type template: str
    """

    _attribute_map = {
        'template': {'key': 'template', 'type': 'str'}
    }

    def __init__(self, template=None):
        super(WorkItemTypeTemplate, self).__init__()
        self.template = template



class WorkItemTypeTemplateUpdateModel(Model):
    """WorkItemTypeTemplateUpdateModel.

    :param action_type:
    :type action_type: object
    :param methodology:
    :type methodology: str
    :param template:
    :type template: str
    :param template_type:
    :type template_type: object
    """

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'object'},
        'methodology': {'key': 'methodology', 'type': 'str'},
        'template': {'key': 'template', 'type': 'str'},
        'template_type': {'key': 'templateType', 'type': 'object'}
    }

    def __init__(self, action_type=None, methodology=None, template=None, template_type=None):
        super(WorkItemTypeTemplateUpdateModel, self).__init__()
        self.action_type = action_type
        self.methodology = methodology
        self.template = template
        self.template_type = template_type



class WorkItemUpdate(WorkItemTrackingResourceReference):
    """WorkItemUpdate.

    :param url:
    :type url: str
    :param fields:
    :type fields: dict
    :param id:
    :type id: int
    :param relations:
    :type relations: :class:`WorkItemRelationUpdates <work-item-tracking.v4_0.models.WorkItemRelationUpdates>`
    :param rev:
    :type rev: int
    :param revised_by:
    :type revised_by: :class:`IdentityReference <work-item-tracking.v4_0.models.IdentityReference>`
    :param revised_date:
    :type revised_date: datetime
    :param work_item_id:
    :type work_item_id: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '{WorkItemFieldUpdate}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': 'WorkItemRelationUpdates'},
        'rev': {'key': 'rev', 'type': 'int'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, url=None, fields=None, id=None, relations=None, rev=None, revised_by=None, revised_date=None, work_item_id=None):
        super(WorkItemUpdate, self).__init__(url=url)
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.work_item_id = work_item_id



class ReportingWorkItemLinksBatch(StreamedBatch):
    """ReportingWorkItemLinksBatch.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(ReportingWorkItemLinksBatch, self).__init__()



class ReportingWorkItemRevisionsBatch(StreamedBatch):
    """ReportingWorkItemRevisionsBatch.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(ReportingWorkItemRevisionsBatch, self).__init__()



class WorkItemDelete(WorkItemDeleteReference):
    """WorkItemDelete.

    :param code:
    :type code: int
    :param deleted_by:
    :type deleted_by: str
    :param deleted_date:
    :type deleted_date: str
    :param id:
    :type id: int
    :param message:
    :type message: str
    :param name:
    :type name: str
    :param project:
    :type project: str
    :param type:
    :type type: str
    :param url:
    :type url: str
    :param resource:
    :type resource: :class:`WorkItem <work-item-tracking.v4_0.models.WorkItem>`
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'deleted_by': {'key': 'deletedBy', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'WorkItem'}
    }

    def __init__(self, code=None, deleted_by=None, deleted_date=None, id=None, message=None, name=None, project=None, type=None, url=None, resource=None):
        super(WorkItemDelete, self).__init__(code=code, deleted_by=deleted_by, deleted_date=deleted_date, id=id, message=message, name=name, project=project, type=type, url=url)
        self.resource = resource



class WorkItemTrackingResource(WorkItemTrackingResourceReference):
    """WorkItemTrackingResource.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links



class WorkItemType(WorkItemTrackingResource):
    """WorkItemType.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param color:
    :type color: str
    :param description:
    :type description: str
    :param field_instances:
    :type field_instances: list of :class:`WorkItemTypeFieldInstance <work-item-tracking.v4_0.models.WorkItemTypeFieldInstance>`
    :param fields:
    :type fields: list of :class:`WorkItemTypeFieldInstance <work-item-tracking.v4_0.models.WorkItemTypeFieldInstance>`
    :param icon:
    :type icon: :class:`WorkItemIcon <work-item-tracking.v4_0.models.WorkItemIcon>`
    :param name:
    :type name: str
    :param transitions:
    :type transitions: dict
    :param xml_form:
    :type xml_form: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'color': {'key': 'color', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'field_instances': {'key': 'fieldInstances', 'type': '[WorkItemTypeFieldInstance]'},
        'fields': {'key': 'fields', 'type': '[WorkItemTypeFieldInstance]'},
        'icon': {'key': 'icon', 'type': 'WorkItemIcon'},
        'name': {'key': 'name', 'type': 'str'},
        'transitions': {'key': 'transitions', 'type': '{[WorkItemStateTransition]}'},
        'xml_form': {'key': 'xmlForm', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, color=None, description=None, field_instances=None, fields=None, icon=None, name=None, transitions=None, xml_form=None):
        super(WorkItemType, self).__init__(url=url, _links=_links)
        self.color = color
        self.description = description
        self.field_instances = field_instances
        self.fields = fields
        self.icon = icon
        self.name = name
        self.transitions = transitions
        self.xml_form = xml_form



class WorkItemTypeCategory(WorkItemTrackingResource):
    """WorkItemTypeCategory.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param default_work_item_type:
    :type default_work_item_type: :class:`WorkItemTypeReference <work-item-tracking.v4_0.models.WorkItemTypeReference>`
    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    :param work_item_types:
    :type work_item_types: list of :class:`WorkItemTypeReference <work-item-tracking.v4_0.models.WorkItemTypeReference>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_work_item_type': {'key': 'defaultWorkItemType', 'type': 'WorkItemTypeReference'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'work_item_types': {'key': 'workItemTypes', 'type': '[WorkItemTypeReference]'}
    }

    def __init__(self, url=None, _links=None, default_work_item_type=None, name=None, reference_name=None, work_item_types=None):
        super(WorkItemTypeCategory, self).__init__(url=url, _links=_links)
        self.default_work_item_type = default_work_item_type
        self.name = name
        self.reference_name = reference_name
        self.work_item_types = work_item_types



class FieldDependentRule(WorkItemTrackingResource):
    """FieldDependentRule.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param dependent_fields:
    :type dependent_fields: list of :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'}
    }

    def __init__(self, url=None, _links=None, dependent_fields=None):
        super(FieldDependentRule, self).__init__(url=url, _links=_links)
        self.dependent_fields = dependent_fields



class QueryHierarchyItem(WorkItemTrackingResource):
    """QueryHierarchyItem.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param children:
    :type children: list of :class:`QueryHierarchyItem <work-item-tracking.v4_0.models.QueryHierarchyItem>`
    :param clauses:
    :type clauses: :class:`WorkItemQueryClause <work-item-tracking.v4_0.models.WorkItemQueryClause>`
    :param columns:
    :type columns: list of :class:`WorkItemFieldReference <work-item-tracking.v4_0.models.WorkItemFieldReference>`
    :param created_by:
    :type created_by: :class:`IdentityReference <work-item-tracking.v4_0.models.IdentityReference>`
    :param created_date:
    :type created_date: datetime
    :param filter_options:
    :type filter_options: object
    :param has_children:
    :type has_children: bool
    :param id:
    :type id: str
    :param is_deleted:
    :type is_deleted: bool
    :param is_folder:
    :type is_folder: bool
    :param is_invalid_syntax:
    :type is_invalid_syntax: bool
    :param is_public:
    :type is_public: bool
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityReference <work-item-tracking.v4_0.models.IdentityReference>`
    :param last_modified_date:
    :type last_modified_date: datetime
    :param link_clauses:
    :type link_clauses: :class:`WorkItemQueryClause <work-item-tracking.v4_0.models.WorkItemQueryClause>`
    :param name:
    :type name: str
    :param path:
    :type path: str
    :param query_type:
    :type query_type: object
    :param sort_columns:
    :type sort_columns: list of :class:`WorkItemQuerySortColumn <work-item-tracking.v4_0.models.WorkItemQuerySortColumn>`
    :param source_clauses:
    :type source_clauses: :class:`WorkItemQueryClause <work-item-tracking.v4_0.models.WorkItemQueryClause>`
    :param target_clauses:
    :type target_clauses: :class:`WorkItemQueryClause <work-item-tracking.v4_0.models.WorkItemQueryClause>`
    :param wiql:
    :type wiql: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'children': {'key': 'children', 'type': '[QueryHierarchyItem]'},
        'clauses': {'key': 'clauses', 'type': 'WorkItemQueryClause'},
        'columns': {'key': 'columns', 'type': '[WorkItemFieldReference]'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityReference'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'filter_options': {'key': 'filterOptions', 'type': 'object'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_invalid_syntax': {'key': 'isInvalidSyntax', 'type': 'bool'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityReference'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
        'link_clauses': {'key': 'linkClauses', 'type': 'WorkItemQueryClause'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'sort_columns': {'key': 'sortColumns', 'type': '[WorkItemQuerySortColumn]'},
        'source_clauses': {'key': 'sourceClauses', 'type': 'WorkItemQueryClause'},
        'target_clauses': {'key': 'targetClauses', 'type': 'WorkItemQueryClause'},
        'wiql': {'key': 'wiql', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, children=None, clauses=None, columns=None, created_by=None, created_date=None, filter_options=None, has_children=None, id=None, is_deleted=None, is_folder=None, is_invalid_syntax=None, is_public=None, last_modified_by=None, last_modified_date=None, link_clauses=None, name=None, path=None, query_type=None, sort_columns=None, source_clauses=None, target_clauses=None, wiql=None):
        super(QueryHierarchyItem, self).__init__(url=url, _links=_links)
        self.children = children
        self.clauses = clauses
        self.columns = columns
        self.created_by = created_by
        self.created_date = created_date
        self.filter_options = filter_options
        self.has_children = has_children
        self.id = id
        self.is_deleted = is_deleted
        self.is_folder = is_folder
        self.is_invalid_syntax = is_invalid_syntax
        self.is_public = is_public
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        self.link_clauses = link_clauses
        self.name = name
        self.path = path
        self.query_type = query_type
        self.sort_columns = sort_columns
        self.source_clauses = source_clauses
        self.target_clauses = target_clauses
        self.wiql = wiql



class WorkItem(WorkItemTrackingResource):
    """WorkItem.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param fields:
    :type fields: dict
    :param id:
    :type id: int
    :param relations:
    :type relations: list of :class:`WorkItemRelation <work-item-tracking.v4_0.models.WorkItemRelation>`
    :param rev:
    :type rev: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'fields': {'key': 'fields', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'relations': {'key': 'relations', 'type': '[WorkItemRelation]'},
        'rev': {'key': 'rev', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, fields=None, id=None, relations=None, rev=None):
        super(WorkItem, self).__init__(url=url, _links=_links)
        self.fields = fields
        self.id = id
        self.relations = relations
        self.rev = rev



class WorkItemClassificationNode(WorkItemTrackingResource):
    """WorkItemClassificationNode.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param attributes:
    :type attributes: dict
    :param children:
    :type children: list of :class:`WorkItemClassificationNode <work-item-tracking.v4_0.models.WorkItemClassificationNode>`
    :param id:
    :type id: int
    :param identifier:
    :type identifier: str
    :param name:
    :type name: str
    :param structure_type:
    :type structure_type: object
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attributes': {'key': 'attributes', 'type': '{object}'},
        'children': {'key': 'children', 'type': '[WorkItemClassificationNode]'},
        'id': {'key': 'id', 'type': 'int'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'structure_type': {'key': 'structureType', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, attributes=None, children=None, id=None, identifier=None, name=None, structure_type=None):
        super(WorkItemClassificationNode, self).__init__(url=url, _links=_links)
        self.attributes = attributes
        self.children = children
        self.id = id
        self.identifier = identifier
        self.name = name
        self.structure_type = structure_type



class WorkItemComment(WorkItemTrackingResource):
    """WorkItemComment.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param revised_by:
    :type revised_by: :class:`IdentityReference <work-item-tracking.v4_0.models.IdentityReference>`
    :param revised_date:
    :type revised_date: datetime
    :param revision:
    :type revision: int
    :param text:
    :type text: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'revision': {'key': 'revision', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, revised_by=None, revised_date=None, revision=None, text=None):
        super(WorkItemComment, self).__init__(url=url, _links=_links)
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.revision = revision
        self.text = text



class WorkItemField(WorkItemTrackingResource):
    """WorkItemField.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param is_identity:
    :type is_identity: bool
    :param is_picklist:
    :type is_picklist: bool
    :param is_picklist_suggested:
    :type is_picklist_suggested: bool
    :param name:
    :type name: str
    :param read_only:
    :type read_only: bool
    :param reference_name:
    :type reference_name: str
    :param supported_operations:
    :type supported_operations: list of :class:`WorkItemFieldOperation <work-item-tracking.v4_0.models.WorkItemFieldOperation>`
    :param type:
    :type type: object
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'is_identity': {'key': 'isIdentity', 'type': 'bool'},
        'is_picklist': {'key': 'isPicklist', 'type': 'bool'},
        'is_picklist_suggested': {'key': 'isPicklistSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'supported_operations': {'key': 'supportedOperations', 'type': '[WorkItemFieldOperation]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, description=None, is_identity=None, is_picklist=None, is_picklist_suggested=None, name=None, read_only=None, reference_name=None, supported_operations=None, type=None):
        super(WorkItemField, self).__init__(url=url, _links=_links)
        self.description = description
        self.is_identity = is_identity
        self.is_picklist = is_picklist
        self.is_picklist_suggested = is_picklist_suggested
        self.name = name
        self.read_only = read_only
        self.reference_name = reference_name
        self.supported_operations = supported_operations
        self.type = type



class WorkItemHistory(WorkItemTrackingResource):
    """WorkItemHistory.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param rev:
    :type rev: int
    :param revised_by:
    :type revised_by: :class:`IdentityReference <work-item-tracking.v4_0.models.IdentityReference>`
    :param revised_date:
    :type revised_date: datetime
    :param value:
    :type value: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'rev': {'key': 'rev', 'type': 'int'},
        'revised_by': {'key': 'revisedBy', 'type': 'IdentityReference'},
        'revised_date': {'key': 'revisedDate', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, rev=None, revised_by=None, revised_date=None, value=None):
        super(WorkItemHistory, self).__init__(url=url, _links=_links)
        self.rev = rev
        self.revised_by = revised_by
        self.revised_date = revised_date
        self.value = value



class WorkItemTemplateReference(WorkItemTrackingResource):
    """WorkItemTemplateReference.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param work_item_type_name:
    :type work_item_type_name: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, description=None, id=None, name=None, work_item_type_name=None):
        super(WorkItemTemplateReference, self).__init__(url=url, _links=_links)
        self.description = description
        self.id = id
        self.name = name
        self.work_item_type_name = work_item_type_name



class WorkItemTrackingReference(WorkItemTrackingResource):
    """WorkItemTrackingReference.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, url=None, _links=None, name=None, reference_name=None):
        super(WorkItemTrackingReference, self).__init__(url=url, _links=_links)
        self.name = name
        self.reference_name = reference_name



class WorkItemRelationType(WorkItemTrackingReference):
    """WorkItemRelationType.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    :param attributes:
    :type attributes: dict
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': '{object}'}
    }

    def __init__(self, url=None, _links=None, name=None, reference_name=None, attributes=None):
        super(WorkItemRelationType, self).__init__(url=url, _links=_links, name=name, reference_name=reference_name)
        self.attributes = attributes



class WorkItemTemplate(WorkItemTemplateReference):
    """WorkItemTemplate.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param work_item_type_name:
    :type work_item_type_name: str
    :param fields:
    :type fields: dict
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_type_name': {'key': 'workItemTypeName', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '{str}'}
    }

    def __init__(self, url=None, _links=None, description=None, id=None, name=None, work_item_type_name=None, fields=None):
        super(WorkItemTemplate, self).__init__(url=url, _links=_links, description=description, id=id, name=name, work_item_type_name=work_item_type_name)
        self.fields = fields
