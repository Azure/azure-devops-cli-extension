# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v5_1.models.ReferenceLinks>`
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
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v5_1.models.ReferenceLinks>`
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



class WorkItemCommentCreateRequest(Model):
    """WorkItemCommentCreateRequest.

    :param text: The text of the comment.
    :type text: str
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(WorkItemCommentCreateRequest, self).__init__()
        self.text = text



class WorkItemCommentUpdateRequest(Model):
    """WorkItemCommentUpdateRequest.

    :param text: The updated text of the comment.
    :type text: str
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, text=None):
        super(WorkItemCommentUpdateRequest, self).__init__()
        self.text = text



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



class WorkItemTrackingResource(WorkItemTrackingResourceReference):
    """WorkItemTrackingResource.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, url=None, _links=None):
        super(WorkItemTrackingResource, self).__init__(url=url)
        self._links = _links



class WorkItemCommentsResponse(WorkItemTrackingResource):
    """WorkItemCommentsResponse.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    :param comments: List of comments in the current batch.
    :type comments: list of :class:`WorkItemCommentResponse <work-item-tracking.v5_1.models.WorkItemCommentResponse>`
    :param continuation_token: A string token that can be used to retrieving next page of comments if available. Otherwise null.
    :type continuation_token: str
    :param count: The count of comments in the current batch.
    :type count: int
    :param next_page: Uri to the next page of comments if it is available. Otherwise null.
    :type next_page: str
    :param total_count: Total count of comments on a work item.
    :type total_count: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[WorkItemCommentResponse]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None):
        super(WorkItemCommentsResponse, self).__init__(url=url, _links=_links)
        self.comments = comments
        self.continuation_token = continuation_token
        self.count = count
        self.next_page = next_page
        self.total_count = total_count



class WorkItemCommentReactionResponse(WorkItemTrackingResource):
    """WorkItemCommentReactionResponse.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    :param comment_id: The id of the comment this reaction belongs to.
    :type comment_id: int
    :param count: Total number of reactions for the WorkItemCommentReactionType.
    :type count: int
    :param is_current_user_engaged: Flag to indicate if the current user has engaged on this particular EngagementType (e.g. if they liked the associated comment).
    :type is_current_user_engaged: bool
    :param type: Type of the reaction.
    :type type: object
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'is_current_user_engaged': {'key': 'isCurrentUserEngaged', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, count=None, is_current_user_engaged=None, type=None):
        super(WorkItemCommentReactionResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.count = count
        self.is_current_user_engaged = is_current_user_engaged
        self.type = type



class WorkItemCommentResponse(WorkItemTrackingResource):
    """WorkItemCommentResponse.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    :param comment_id: The id assigned to the comment.
    :type comment_id: int
    :param created_by: IdentityRef of the creator of the comment.
    :type created_by: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param created_date: The creation date of the comment.
    :type created_date: datetime
    :param created_on_behalf_date: Effective Date/time value for adding the comment. Can be optionally different from CreatedDate.
    :type created_on_behalf_date: datetime
    :param created_on_behalf_of: Identity on whose behalf this comment has been added. Can be optionally different from CreatedBy.
    :type created_on_behalf_of: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param is_deleted: Indicates if the comment has been deleted.
    :type is_deleted: bool
    :param modified_by: IdentityRef of the user who last modified the comment.
    :type modified_by: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param modified_date: The last modification date of the comment.
    :type modified_date: datetime
    :param reactions: The reactions of the comment.
    :type reactions: list of :class:`WorkItemCommentReactionResponse <work-item-tracking.v5_1.models.WorkItemCommentReactionResponse>`
    :param text: The text of the comment.
    :type text: str
    :param version: The current version of the comment.
    :type version: int
    :param work_item_id: The id of the work item this comment belongs to.
    :type work_item_id: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'reactions': {'key': 'reactions', 'type': '[WorkItemCommentReactionResponse]'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'work_item_id': {'key': 'workItemId', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, is_deleted=None, modified_by=None, modified_date=None, reactions=None, text=None, version=None, work_item_id=None):
        super(WorkItemCommentResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.is_deleted = is_deleted
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.reactions = reactions
        self.text = text
        self.version = version
        self.work_item_id = work_item_id



class WorkItemCommentVersionResponse(WorkItemTrackingResource):
    """WorkItemCommentVersionResponse.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    :param comment_id: The id assigned to the comment.
    :type comment_id: int
    :param created_by: IdentityRef of the creator of the comment.
    :type created_by: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param created_date: The creation date of the comment.
    :type created_date: datetime
    :param created_on_behalf_date: Effective Date/time value for adding the comment. Can be optionally different from CreatedDate.
    :type created_on_behalf_date: datetime
    :param created_on_behalf_of: Identity on whose behalf this comment has been added. Can be optionally different from CreatedBy.
    :type created_on_behalf_of: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param is_deleted: Indicates if the comment has been deleted at this version.
    :type is_deleted: bool
    :param modified_by: IdentityRef of the user who modified the comment at this version.
    :type modified_by: :class:`IdentityRef <work-item-tracking.v5_1.models.IdentityRef>`
    :param modified_date: The modification date of the comment for this version.
    :type modified_date: datetime
    :param rendered_text: The rendered content of the comment at this version.
    :type rendered_text: str
    :param text: The text of the comment at this version.
    :type text: str
    :param version: The version number.
    :type version: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_on_behalf_date': {'key': 'createdOnBehalfDate', 'type': 'iso-8601'},
        'created_on_behalf_of': {'key': 'createdOnBehalfOf', 'type': 'IdentityRef'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'rendered_text': {'key': 'renderedText', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, _links=None, comment_id=None, created_by=None, created_date=None, created_on_behalf_date=None, created_on_behalf_of=None, is_deleted=None, modified_by=None, modified_date=None, rendered_text=None, text=None, version=None):
        super(WorkItemCommentVersionResponse, self).__init__(url=url, _links=_links)
        self.comment_id = comment_id
        self.created_by = created_by
        self.created_date = created_date
        self.created_on_behalf_date = created_on_behalf_date
        self.created_on_behalf_of = created_on_behalf_of
        self.is_deleted = is_deleted
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.rendered_text = rendered_text
        self.text = text
        self.version = version



class WorkItemCommentsReportingResponse(WorkItemCommentsResponse):
    """WorkItemCommentsReportingResponse.

    :param url:
    :type url: str
    :param _links: Link references to related REST resources.
    :type _links: :class:`ReferenceLinks <work-item-tracking.v5_1.models.ReferenceLinks>`
    :param comments: List of comments in the current batch.
    :type comments: list of :class:`WorkItemCommentResponse <work-item-tracking.v5_1.models.WorkItemCommentResponse>`
    :param continuation_token: A string token that can be used to retrieving next page of comments if available. Otherwise null.
    :type continuation_token: str
    :param count: The count of comments in the current batch.
    :type count: int
    :param next_page: Uri to the next page of comments if it is available. Otherwise null.
    :type next_page: str
    :param total_count: Total count of comments on a work item.
    :type total_count: int
    :param is_last_batch: Indicates if this is the last batch.
    :type is_last_batch: bool
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[WorkItemCommentResponse]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'is_last_batch': {'key': 'isLastBatch', 'type': 'bool'}
    }

    def __init__(self, url=None, _links=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None, is_last_batch=None):
        super(WorkItemCommentsReportingResponse, self).__init__(url=url, _links=_links, comments=comments, continuation_token=continuation_token, count=count, next_page=next_page, total_count=total_count)
        self.is_last_batch = is_last_batch
