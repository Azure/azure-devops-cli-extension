# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class WorkItemTrackingCommentsClient(VssClient):
    """WorkItemTrackingComments
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingCommentsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def add_comment(self, request, project, work_item_id):
        """AddComment.
        [Preview API] Add a comment on a work item.
        :param :class:`<WorkItemCommentCreateRequest> <work-item-tracking-comments.v5_1.models.WorkItemCommentCreateRequest>` request: Comment create request.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :rtype: :class:`<WorkItemCommentResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        content = self._serialize.body(request, 'WorkItemCommentCreateRequest')
        response = self._send(http_method='POST',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemCommentResponse', response)

    def delete_comment(self, project, work_item_id, comment_id):
        """DeleteComment.
        [Preview API] Delete a comment on a work item.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :param int comment_id:
        :rtype: :class:`<WorkItemCommentResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemCommentResponse', response)

    def get_comment(self, project, work_item_id, comment_id, expand=None):
        """GetComment.
        [Preview API] Returns a work item comment.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get the comment.
        :param int comment_id: Id of the comment to return.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :rtype: :class:`<WorkItemCommentResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentResponse', response)

    def get_comments(self, project, work_item_id, top=None, continuation_token=None, expand=None):
        """GetComments.
        [Preview API] Returns a list of work item comments, pageable.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get comments for.
        :param int top: Max number of comments to return.
        :param str continuation_token: Used to query for the next page of comments.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :rtype: :class:`<WorkItemCommentsResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentsResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsResponse', response)

    def get_comments_batch(self, project, work_item_id, ids, expand=None):
        """GetCommentsBatch.
        [Preview API] Returns a list of work item comments by ids.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get comments for.
        :param [int] ids: Comma-separated list of comment ids to return.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :rtype: :class:`<WorkItemCommentsResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentsResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsResponse', response)

    def update_comment(self, request, project, work_item_id, comment_id):
        """UpdateComment.
        [Preview API] Update a comment on a work item.
        :param :class:`<WorkItemCommentUpdateRequest> <work-item-tracking-comments.v5_1.models.WorkItemCommentUpdateRequest>` request: Comment update request.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :param int comment_id:
        :rtype: :class:`<WorkItemCommentResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        content = self._serialize.body(request, 'WorkItemCommentUpdateRequest')
        response = self._send(http_method='PATCH',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemCommentResponse', response)

    def create_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        """CreateCommentReaction.
        [Preview API] Add a new reaction to a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :param str reaction_type: Type of the reaction
        :rtype: :class:`<WorkItemCommentReactionResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentReactionResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if reaction_type is not None:
            query_parameters['reactionType'] = self._serialize.query('reaction_type', reaction_type, 'str')
        response = self._send(http_method='POST',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentReactionResponse', response)

    def delete_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        """DeleteCommentReaction.
        [Preview API] Deletes an existing reaction on a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :param str reaction_type: Type of the reaction
        :rtype: :class:`<WorkItemCommentReactionResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentReactionResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if reaction_type is not None:
            query_parameters['reactionType'] = self._serialize.query('reaction_type', reaction_type, 'str')
        response = self._send(http_method='DELETE',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentReactionResponse', response)

    def get_comment_reactions(self, project, work_item_id, comment_id):
        """GetCommentReactions.
        [Preview API] Gets reactions of a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :rtype: [WorkItemCommentReactionResponse]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemCommentReactionResponse]', self._unwrap_collection(response))

    def read_reporting_comments(self, project, continuation_token=None, top=None, expand=None):
        """ReadReportingComments.
        [Preview API]
        :param str project: Project ID or project name
        :param str continuation_token:
        :param int top:
        :param str expand:
        :rtype: :class:`<WorkItemCommentsReportingResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentsReportingResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='370b8590-9562-42be-b0d8-ac06668fc5dc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemCommentsReportingResponse', response)

    def get_comment_version(self, project, work_item_id, comment_id, version):
        """GetCommentVersion.
        [Preview API]
        :param str project: Project ID or project name
        :param int work_item_id:
        :param int comment_id:
        :param int version:
        :rtype: :class:`<WorkItemCommentVersionResponse> <work-item-tracking-comments.v5_1.models.WorkItemCommentVersionResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemCommentVersionResponse', response)

    def get_comment_versions(self, project, work_item_id, comment_id):
        """GetCommentVersions.
        [Preview API]
        :param str project: Project ID or project name
        :param int work_item_id:
        :param int comment_id:
        :rtype: [WorkItemCommentVersionResponse]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemCommentVersionResponse]', self._unwrap_collection(response))

