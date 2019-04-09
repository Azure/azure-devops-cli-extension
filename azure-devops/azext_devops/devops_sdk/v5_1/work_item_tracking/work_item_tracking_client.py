# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingClient(Client):
    """WorkItemTracking
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def get_recent_activity_data(self):
        """GetRecentActivityData.
        [Preview API] Gets recent work item activities
        :rtype: [AccountRecentActivityWorkItemModel2]
        """
        response = self._send(http_method='GET',
                              location_id='1bc988f4-c15f-4072-ad35-497c87e3a909',
                              version='5.1-preview.2')
        return self._deserialize('[AccountRecentActivityWorkItemModel2]', self._unwrap_collection(response))

    def get_work_artifact_link_types(self):
        """GetWorkArtifactLinkTypes.
        [Preview API] Get the list of work item tracking outbound artifact link types.
        :rtype: [WorkArtifactLink]
        """
        response = self._send(http_method='GET',
                              location_id='1a31de40-e318-41cd-a6c6-881077df52e3',
                              version='5.1-preview.1')
        return self._deserialize('[WorkArtifactLink]', self._unwrap_collection(response))

    def query_work_items_for_artifact_uris(self, artifact_uri_query, project=None):
        """QueryWorkItemsForArtifactUris.
        [Preview API] Queries work items linked to a given list of artifact URI.
        :param :class:`<ArtifactUriQuery> <azure.devops.v5_1.work_item_tracking.models.ArtifactUriQuery>` artifact_uri_query: Defines a list of artifact URI for querying work items.
        :param str project: Project ID or project name
        :rtype: :class:`<ArtifactUriQueryResult> <azure.devops.v5_1.work-item-tracking.models.ArtifactUriQueryResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(artifact_uri_query, 'ArtifactUriQuery')
        response = self._send(http_method='POST',
                              location_id='a9a9aa7a-8c09-44d3-ad1b-46e855c1e3d3',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ArtifactUriQueryResult', response)

    def create_attachment(self, upload_stream, project=None, file_name=None, upload_type=None, area_path=None, **kwargs):
        """CreateAttachment.
        [Preview API] Uploads an attachment.
        :param object upload_stream: Stream to upload
        :param str project: Project ID or project name
        :param str file_name: The name of the file
        :param str upload_type: Attachment upload type: Simple or Chunked
        :param str area_path: Target project Area Path
        :rtype: :class:`<AttachmentReference> <azure.devops.v5_1.work-item-tracking.models.AttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if upload_type is not None:
            query_parameters['uploadType'] = self._serialize.query('upload_type', upload_type, 'str')
        if area_path is not None:
            query_parameters['areaPath'] = self._serialize.query('area_path', area_path, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('AttachmentReference', response)

    def get_attachment_content(self, id, project=None, file_name=None, download=None, **kwargs):
        """GetAttachmentContent.
        [Preview API] Downloads an attachment.
        :param str id: Attachment ID
        :param str project: Project ID or project name
        :param str file_name: Name of the file
        :param bool download: If set to <c>true</c> always download attachment
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        response = self._send(http_method='GET',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachment_zip(self, id, project=None, file_name=None, download=None, **kwargs):
        """GetAttachmentZip.
        [Preview API] Downloads an attachment.
        :param str id: Attachment ID
        :param str project: Project ID or project name
        :param str file_name: Name of the file
        :param bool download: If set to <c>true</c> always download attachment
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        response = self._send(http_method='GET',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_classification_nodes(self, project, ids, depth=None, error_policy=None):
        """GetClassificationNodes.
        [Preview API] Gets root classification nodes or list of classification nodes for a given list of nodes ids, for a given project. In case ids parameter is supplied you will  get list of classification nodes for those ids. Otherwise you will get root classification nodes for this project.
        :param str project: Project ID or project name
        :param [int] ids: Comma seperated integer classification nodes ids. It's not required, if you want root nodes.
        :param int depth: Depth of children to fetch.
        :param str error_policy: Flag to handle errors in getting some nodes. Possible options are Fail and Omit.
        :rtype: [WorkItemClassificationNode]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if error_policy is not None:
            query_parameters['errorPolicy'] = self._serialize.query('error_policy', error_policy, 'str')
        response = self._send(http_method='GET',
                              location_id='a70579d1-f53a-48ee-a5be-7be8659023b9',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemClassificationNode]', self._unwrap_collection(response))

    def get_root_nodes(self, project, depth=None):
        """GetRootNodes.
        [Preview API] Gets root classification nodes under the project.
        :param str project: Project ID or project name
        :param int depth: Depth of children to fetch.
        :rtype: [WorkItemClassificationNode]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        response = self._send(http_method='GET',
                              location_id='a70579d1-f53a-48ee-a5be-7be8659023b9',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemClassificationNode]', self._unwrap_collection(response))

    def create_or_update_classification_node(self, posted_node, project, structure_group, path=None):
        """CreateOrUpdateClassificationNode.
        [Preview API] Create new or update an existing classification node.
        :param :class:`<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>` posted_node: Node to create or update.
        :param str project: Project ID or project name
        :param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.
        :param str path: Path of the classification node.
        :rtype: :class:`<WorkItemClassificationNode> <azure.devops.v5_1.work-item-tracking.models.WorkItemClassificationNode>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        content = self._serialize.body(posted_node, 'WorkItemClassificationNode')
        response = self._send(http_method='POST',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemClassificationNode', response)

    def delete_classification_node(self, project, structure_group, path=None, reclassify_id=None):
        """DeleteClassificationNode.
        [Preview API] Delete an existing classification node.
        :param str project: Project ID or project name
        :param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.
        :param str path: Path of the classification node.
        :param int reclassify_id: Id of the target classification node for reclassification.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if reclassify_id is not None:
            query_parameters['$reclassifyId'] = self._serialize.query('reclassify_id', reclassify_id, 'int')
        self._send(http_method='DELETE',
                   location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                   version='5.1-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_classification_node(self, project, structure_group, path=None, depth=None):
        """GetClassificationNode.
        [Preview API] Gets the classification node for a given node path.
        :param str project: Project ID or project name
        :param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.
        :param str path: Path of the classification node.
        :param int depth: Depth of children to fetch.
        :rtype: :class:`<WorkItemClassificationNode> <azure.devops.v5_1.work-item-tracking.models.WorkItemClassificationNode>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        response = self._send(http_method='GET',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemClassificationNode', response)

    def update_classification_node(self, posted_node, project, structure_group, path=None):
        """UpdateClassificationNode.
        [Preview API] Update an existing classification node.
        :param :class:`<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>` posted_node: Node to create or update.
        :param str project: Project ID or project name
        :param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.
        :param str path: Path of the classification node.
        :rtype: :class:`<WorkItemClassificationNode> <azure.devops.v5_1.work-item-tracking.models.WorkItemClassificationNode>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        content = self._serialize.body(posted_node, 'WorkItemClassificationNode')
        response = self._send(http_method='PATCH',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemClassificationNode', response)

    def add_comment(self, request, project, work_item_id):
        """AddComment.
        [Preview API] Add a comment on a work item.
        :param :class:`<CommentCreate> <azure.devops.v5_1.work_item_tracking.models.CommentCreate>` request: Comment create request.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :rtype: :class:`<Comment> <azure.devops.v5_1.work-item-tracking.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        content = self._serialize.body(request, 'CommentCreate')
        response = self._send(http_method='POST',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def delete_comment(self, project, work_item_id, comment_id):
        """DeleteComment.
        [Preview API] Delete a comment on a work item.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :param int comment_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                   version='5.1-preview.3',
                   route_values=route_values)

    def get_comment(self, project, work_item_id, comment_id, include_deleted=None, expand=None):
        """GetComment.
        [Preview API] Returns a work item comment.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get the comment.
        :param int comment_id: Id of the comment to return.
        :param bool include_deleted: Specify if the deleted comment should be retrieved.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :rtype: :class:`<Comment> <azure.devops.v5_1.work-item-tracking.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Comment', response)

    def get_comments(self, project, work_item_id, top=None, continuation_token=None, include_deleted=None, expand=None, order=None):
        """GetComments.
        [Preview API] Returns a list of work item comments, pageable.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get comments for.
        :param int top: Max number of comments to return.
        :param str continuation_token: Used to query for the next page of comments.
        :param bool include_deleted: Specify if the deleted comments should be retrieved.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :param str order: Order in which the comments should be returned.
        :rtype: :class:`<CommentList> <azure.devops.v5_1.work-item-tracking.models.CommentList>`
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
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if order is not None:
            query_parameters['order'] = self._serialize.query('order', order, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CommentList', response)

    def get_comments_batch(self, project, work_item_id, ids, include_deleted=None, expand=None):
        """GetCommentsBatch.
        [Preview API] Returns a list of work item comments by ids.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item to get comments for.
        :param [int] ids: Comma-separated list of comment ids to return.
        :param bool include_deleted: Specify if the deleted comments should be retrieved.
        :param str expand: Specifies the additional data retrieval options for work item comments.
        :rtype: :class:`<CommentList> <azure.devops.v5_1.work-item-tracking.models.CommentList>`
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
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CommentList', response)

    def update_comment(self, request, project, work_item_id, comment_id):
        """UpdateComment.
        [Preview API] Update a comment on a work item.
        :param :class:`<CommentUpdate> <azure.devops.v5_1.work_item_tracking.models.CommentUpdate>` request: Comment update request.
        :param str project: Project ID or project name
        :param int work_item_id: Id of a work item.
        :param int comment_id:
        :rtype: :class:`<Comment> <azure.devops.v5_1.work-item-tracking.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        content = self._serialize.body(request, 'CommentUpdate')
        response = self._send(http_method='PATCH',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='5.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def create_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        """CreateCommentReaction.
        [Preview API] Adds a new reaction to a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :param CommentReactionType reaction_type: Type of the reaction
        :rtype: :class:`<CommentReaction> <azure.devops.v5_1.work-item-tracking.models.CommentReaction>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if reaction_type is not None:
            route_values['reactionType'] = self._serialize.url('reaction_type', reaction_type, 'CommentReactionType')
        response = self._send(http_method='PUT',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('CommentReaction', response)

    def delete_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        """DeleteCommentReaction.
        [Preview API] Deletes an existing reaction on a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :param CommentReactionType reaction_type: Type of the reaction
        :rtype: :class:`<CommentReaction> <azure.devops.v5_1.work-item-tracking.models.CommentReaction>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if reaction_type is not None:
            route_values['reactionType'] = self._serialize.url('reaction_type', reaction_type, 'CommentReactionType')
        response = self._send(http_method='DELETE',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('CommentReaction', response)

    def get_comment_reactions(self, project, work_item_id, comment_id):
        """GetCommentReactions.
        [Preview API] Gets reactions of a comment.
        :param str project: Project ID or project name
        :param int work_item_id: WorkItem ID
        :param int comment_id: Comment ID
        :rtype: [CommentReaction]
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
        return self._deserialize('[CommentReaction]', self._unwrap_collection(response))

    def read_reporting_comments(self, project, continuation_token=None, top=None, include_deleted=None, expand=None):
        """ReadReportingComments.
        [Preview API]
        :param str project: Project ID or project name
        :param str continuation_token:
        :param int top:
        :param bool include_deleted:
        :param str expand:
        :rtype: :class:`<CommentReportingList> <azure.devops.v5_1.work-item-tracking.models.CommentReportingList>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='370b8590-9562-42be-b0d8-ac06668fc5dc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CommentReportingList', response)

    def get_comment_version(self, project, work_item_id, comment_id, version):
        """GetCommentVersion.
        [Preview API]
        :param str project: Project ID or project name
        :param int work_item_id:
        :param int comment_id:
        :param int version:
        :rtype: :class:`<CommentVersion> <azure.devops.v5_1.work-item-tracking.models.CommentVersion>`
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
        return self._deserialize('CommentVersion', response)

    def get_comment_versions(self, project, work_item_id, comment_id):
        """GetCommentVersions.
        [Preview API]
        :param str project: Project ID or project name
        :param int work_item_id:
        :param int comment_id:
        :rtype: [CommentVersion]
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
        return self._deserialize('[CommentVersion]', self._unwrap_collection(response))

    def create_field(self, work_item_field, project=None):
        """CreateField.
        [Preview API] Create a new field.
        :param :class:`<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>` work_item_field: New field definition
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemField> <azure.devops.v5_1.work-item-tracking.models.WorkItemField>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_field, 'WorkItemField')
        response = self._send(http_method='POST',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemField', response)

    def delete_field(self, field_name_or_ref_name, project=None):
        """DeleteField.
        [Preview API] Deletes the field.
        :param str field_name_or_ref_name: Field simple name or reference name
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if field_name_or_ref_name is not None:
            route_values['fieldNameOrRefName'] = self._serialize.url('field_name_or_ref_name', field_name_or_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_field(self, field_name_or_ref_name, project=None):
        """GetField.
        [Preview API] Gets information on a specific field.
        :param str field_name_or_ref_name: Field simple name or reference name
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemField> <azure.devops.v5_1.work-item-tracking.models.WorkItemField>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if field_name_or_ref_name is not None:
            route_values['fieldNameOrRefName'] = self._serialize.url('field_name_or_ref_name', field_name_or_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemField', response)

    def get_fields(self, project=None, expand=None):
        """GetFields.
        [Preview API] Returns information for all fields.
        :param str project: Project ID or project name
        :param str expand: Use ExtensionFields to include extension fields, otherwise exclude them. Unless the feature flag for this parameter is enabled, extension fields are always included.
        :rtype: [WorkItemField]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemField]', self._unwrap_collection(response))

    def create_query(self, posted_query, project, query, validate_wiql_only=None):
        """CreateQuery.
        [Preview API] Creates a query, or moves a query.
        :param :class:`<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>` posted_query: The query to create.
        :param str project: Project ID or project name
        :param str query: The parent id or path under which the query is to be created.
        :param bool validate_wiql_only: If you only want to validate your WIQL query without actually creating one, set it to true. Default is false.
        :rtype: :class:`<QueryHierarchyItem> <azure.devops.v5_1.work-item-tracking.models.QueryHierarchyItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if validate_wiql_only is not None:
            query_parameters['validateWiqlOnly'] = self._serialize.query('validate_wiql_only', validate_wiql_only, 'bool')
        content = self._serialize.body(posted_query, 'QueryHierarchyItem')
        response = self._send(http_method='POST',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('QueryHierarchyItem', response)

    def delete_query(self, project, query):
        """DeleteQuery.
        [Preview API] Delete a query or a folder. This deletes any permission change on the deleted query or folder and any of its descendants if it is a folder. It is important to note that the deleted permission changes cannot be recovered upon undeleting the query or folder.
        :param str project: Project ID or project name
        :param str query: ID or path of the query or folder to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        self._send(http_method='DELETE',
                   location_id='a67d190c-c41f-424b-814d-0e906f659301',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_queries(self, project, expand=None, depth=None, include_deleted=None):
        """GetQueries.
        [Preview API] Gets the root queries and their children
        :param str project: Project ID or project name
        :param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.
        :param int depth: In the folder of queries, return child queries and folders to this depth.
        :param bool include_deleted: Include deleted queries and folders
        :rtype: [QueryHierarchyItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[QueryHierarchyItem]', self._unwrap_collection(response))

    def get_query(self, project, query, expand=None, depth=None, include_deleted=None):
        """GetQuery.
        [Preview API] Retrieves an individual query and its children
        :param str project: Project ID or project name
        :param str query: ID or path of the query.
        :param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.
        :param int depth: In the folder of queries, return child queries and folders to this depth.
        :param bool include_deleted: Include deleted queries and folders
        :rtype: :class:`<QueryHierarchyItem> <azure.devops.v5_1.work-item-tracking.models.QueryHierarchyItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QueryHierarchyItem', response)

    def search_queries(self, project, filter, top=None, expand=None, include_deleted=None):
        """SearchQueries.
        [Preview API] Searches all queries the user has access to in the current project
        :param str project: Project ID or project name
        :param str filter: The text to filter the queries with.
        :param int top: The number of queries to return (Default is 50 and maximum is 200).
        :param str expand:
        :param bool include_deleted: Include deleted queries and folders
        :rtype: :class:`<QueryHierarchyItemsResult> <azure.devops.v5_1.work-item-tracking.models.QueryHierarchyItemsResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QueryHierarchyItemsResult', response)

    def update_query(self, query_update, project, query, undelete_descendants=None):
        """UpdateQuery.
        [Preview API] Update a query or a folder. This allows you to update, rename and move queries and folders.
        :param :class:`<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>` query_update: The query to update.
        :param str project: Project ID or project name
        :param str query: The ID or path for the query to update.
        :param bool undelete_descendants: Undelete the children of this folder. It is important to note that this will not bring back the permission changes that were previously applied to the descendants.
        :rtype: :class:`<QueryHierarchyItem> <azure.devops.v5_1.work-item-tracking.models.QueryHierarchyItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if undelete_descendants is not None:
            query_parameters['$undeleteDescendants'] = self._serialize.query('undelete_descendants', undelete_descendants, 'bool')
        content = self._serialize.body(query_update, 'QueryHierarchyItem')
        response = self._send(http_method='PATCH',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('QueryHierarchyItem', response)

    def get_queries_batch(self, query_get_request, project):
        """GetQueriesBatch.
        [Preview API] Gets a list of queries by ids (Maximum 1000)
        :param :class:`<QueryBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.QueryBatchGetRequest>` query_get_request:
        :param str project: Project ID or project name
        :rtype: [QueryHierarchyItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(query_get_request, 'QueryBatchGetRequest')
        response = self._send(http_method='POST',
                              location_id='549816f9-09b0-4e75-9e81-01fbfcd07426',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[QueryHierarchyItem]', self._unwrap_collection(response))

    def destroy_work_item(self, id, project=None):
        """DestroyWorkItem.
        [Preview API] Destroys the specified work item permanently from the Recycle Bin. This action can not be undone.
        :param int id: ID of the work item to be destroyed permanently
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        self._send(http_method='DELETE',
                   location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_deleted_work_item(self, id, project=None):
        """GetDeletedWorkItem.
        [Preview API] Gets a deleted work item from Recycle Bin.
        :param int id: ID of the work item to be returned
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemDelete> <azure.devops.v5_1.work-item-tracking.models.WorkItemDelete>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemDelete', response)

    def get_deleted_work_items(self, ids, project=None):
        """GetDeletedWorkItems.
        [Preview API] Gets the work items from the recycle bin, whose IDs have been specified in the parameters
        :param [int] ids: Comma separated list of IDs of the deleted work items to be returned
        :param str project: Project ID or project name
        :rtype: [WorkItemDeleteReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemDeleteReference]', self._unwrap_collection(response))

    def get_deleted_work_item_shallow_references(self, project=None):
        """GetDeletedWorkItemShallowReferences.
        [Preview API] Gets a list of the IDs and the URLs of the deleted the work items in the Recycle Bin.
        :param str project: Project ID or project name
        :rtype: [WorkItemDeleteShallowReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemDeleteShallowReference]', self._unwrap_collection(response))

    def restore_work_item(self, payload, id, project=None):
        """RestoreWorkItem.
        [Preview API] Restores the deleted work item from Recycle Bin.
        :param :class:`<WorkItemDeleteUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemDeleteUpdate>` payload: Paylod with instructions to update the IsDeleted flag to false
        :param int id: ID of the work item to be restored
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemDelete> <azure.devops.v5_1.work-item-tracking.models.WorkItemDelete>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        content = self._serialize.body(payload, 'WorkItemDeleteUpdate')
        response = self._send(http_method='PATCH',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemDelete', response)

    def get_revision(self, id, revision_number, project=None, expand=None):
        """GetRevision.
        [Preview API] Returns a fully hydrated work item for the requested revision
        :param int id:
        :param int revision_number:
        :param str project: Project ID or project name
        :param str expand:
        :rtype: :class:`<WorkItem> <azure.devops.v5_1.work-item-tracking.models.WorkItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        if revision_number is not None:
            route_values['revisionNumber'] = self._serialize.url('revision_number', revision_number, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='a00c85a5-80fa-4565-99c3-bcd2181434bb',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def get_revisions(self, id, project=None, top=None, skip=None, expand=None):
        """GetRevisions.
        [Preview API] Returns the list of fully hydrated work item revisions, paged.
        :param int id:
        :param str project: Project ID or project name
        :param int top:
        :param int skip:
        :param str expand:
        :rtype: [WorkItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='a00c85a5-80fa-4565-99c3-bcd2181434bb',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def create_template(self, template, team_context):
        """CreateTemplate.
        [Preview API] Creates a template
        :param :class:`<WorkItemTemplate> <azure.devops.v5_1.work_item_tracking.models.WorkItemTemplate>` template: Template contents
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :rtype: :class:`<WorkItemTemplate> <azure.devops.v5_1.work-item-tracking.models.WorkItemTemplate>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(template, 'WorkItemTemplate')
        response = self._send(http_method='POST',
                              location_id='6a90345f-a676-4969-afce-8e163e1d5642',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTemplate', response)

    def get_templates(self, team_context, workitemtypename=None):
        """GetTemplates.
        [Preview API] Gets template
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param str workitemtypename: Optional, When specified returns templates for given Work item type.
        :rtype: [WorkItemTemplateReference]
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if workitemtypename is not None:
            query_parameters['workitemtypename'] = self._serialize.query('workitemtypename', workitemtypename, 'str')
        response = self._send(http_method='GET',
                              location_id='6a90345f-a676-4969-afce-8e163e1d5642',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemTemplateReference]', self._unwrap_collection(response))

    def delete_template(self, team_context, template_id):
        """DeleteTemplate.
        [Preview API] Deletes the template with given id
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param str template_id: Template id
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        self._send(http_method='DELETE',
                   location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_template(self, team_context, template_id):
        """GetTemplate.
        [Preview API] Gets the template with specified id
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param str template_id: Template Id
        :rtype: :class:`<WorkItemTemplate> <azure.devops.v5_1.work-item-tracking.models.WorkItemTemplate>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        response = self._send(http_method='GET',
                              location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemTemplate', response)

    def replace_template(self, template_content, team_context, template_id):
        """ReplaceTemplate.
        [Preview API] Replace template contents
        :param :class:`<WorkItemTemplate> <azure.devops.v5_1.work_item_tracking.models.WorkItemTemplate>` template_content: Template contents to replace with
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param str template_id: Template id
        :rtype: :class:`<WorkItemTemplate> <azure.devops.v5_1.work-item-tracking.models.WorkItemTemplate>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template_content, 'WorkItemTemplate')
        response = self._send(http_method='PUT',
                              location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTemplate', response)

    def get_update(self, id, update_number, project=None):
        """GetUpdate.
        [Preview API] Returns a single update for a work item
        :param int id:
        :param int update_number:
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemUpdate> <azure.devops.v5_1.work-item-tracking.models.WorkItemUpdate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        if update_number is not None:
            route_values['updateNumber'] = self._serialize.url('update_number', update_number, 'int')
        response = self._send(http_method='GET',
                              location_id='6570bf97-d02c-4a91-8d93-3abe9895b1a9',
                              version='5.1-preview.3',
                              route_values=route_values)
        return self._deserialize('WorkItemUpdate', response)

    def get_updates(self, id, project=None, top=None, skip=None):
        """GetUpdates.
        [Preview API] Returns a the deltas between work item revisions
        :param int id:
        :param str project: Project ID or project name
        :param int top:
        :param int skip:
        :rtype: [WorkItemUpdate]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='6570bf97-d02c-4a91-8d93-3abe9895b1a9',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemUpdate]', self._unwrap_collection(response))

    def query_by_wiql(self, wiql, team_context=None, time_precision=None, top=None):
        """QueryByWiql.
        [Preview API] Gets the results of the query given its WIQL.
        :param :class:`<Wiql> <azure.devops.v5_1.work_item_tracking.models.Wiql>` wiql: The query containing the WIQL.
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param bool time_precision: Whether or not to use time precision.
        :param int top: The max number of results to return.
        :rtype: :class:`<WorkItemQueryResult> <azure.devops.v5_1.work-item-tracking.models.WorkItemQueryResult>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(wiql, 'Wiql')
        response = self._send(http_method='POST',
                              location_id='1a9c53f7-f243-4447-b110-35ef023636e4',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('WorkItemQueryResult', response)

    def get_query_result_count(self, id, team_context=None, time_precision=None, top=None):
        """GetQueryResultCount.
        [Preview API] Gets the results of the query given the query ID.
        :param str id: The query ID.
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param bool time_precision: Whether or not to use time precision.
        :param int top: The max number of results to return.
        :rtype: int
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='HEAD',
                              location_id='a02355f5-5f8a-4671-8e32-369d23aac83d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('int', response)

    def query_by_id(self, id, team_context=None, time_precision=None, top=None):
        """QueryById.
        [Preview API] Gets the results of the query given the query ID.
        :param str id: The query ID.
        :param :class:`<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext>` team_context: The team context for the operation
        :param bool time_precision: Whether or not to use time precision.
        :param int top: The max number of results to return.
        :rtype: :class:`<WorkItemQueryResult> <azure.devops.v5_1.work-item-tracking.models.WorkItemQueryResult>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='a02355f5-5f8a-4671-8e32-369d23aac83d',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemQueryResult', response)

    def get_work_item_icon_json(self, icon, color=None, v=None):
        """GetWorkItemIconJson.
        [Preview API] Get a work item icon given the friendly name and icon color.
        :param str icon: The name of the icon
        :param str color: The 6-digit hex color for the icon
        :param int v: The version of the icon (used only for cache invalidation)
        :rtype: :class:`<WorkItemIcon> <azure.devops.v5_1.work-item-tracking.models.WorkItemIcon>`
        """
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemIcon', response)

    def get_work_item_icons(self):
        """GetWorkItemIcons.
        [Preview API] Get a list of all work item icons.
        :rtype: [WorkItemIcon]
        """
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='5.1-preview.1')
        return self._deserialize('[WorkItemIcon]', self._unwrap_collection(response))

    def get_work_item_icon_svg(self, icon, color=None, v=None, **kwargs):
        """GetWorkItemIconSvg.
        [Preview API] Get a work item icon given the friendly name and icon color.
        :param str icon: The name of the icon
        :param str color: The 6-digit hex color for the icon
        :param int v: The version of the icon (used only for cache invalidation)
        :rtype: object
        """
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='image/svg+xml')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_work_item_icon_xaml(self, icon, color=None, v=None, **kwargs):
        """GetWorkItemIconXaml.
        [Preview API] Get a work item icon given the friendly name and icon color.
        :param str icon: The name of the icon
        :param str color: The 6-digit hex color for the icon
        :param int v: The version of the icon (used only for cache invalidation)
        :rtype: object
        """
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='image/xaml+xml')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_reporting_links_by_link_type(self, project=None, link_types=None, types=None, continuation_token=None, start_date_time=None):
        """GetReportingLinksByLinkType.
        [Preview API] Get a batch of work item links
        :param str project: Project ID or project name
        :param [str] link_types: A list of types to filter the results to specific link types. Omit this parameter to get work item links of all link types.
        :param [str] types: A list of types to filter the results to specific work item types. Omit this parameter to get work item links of all work item types.
        :param str continuation_token: Specifies the continuationToken to start the batch from. Omit this parameter to get the first batch of links.
        :param datetime start_date_time: Date/time to use as a starting point for link changes. Only link changes that occurred after that date/time will be returned. Cannot be used in conjunction with 'watermark' parameter.
        :rtype: :class:`<ReportingWorkItemLinksBatch> <azure.devops.v5_1.work-item-tracking.models.ReportingWorkItemLinksBatch>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if link_types is not None:
            link_types = ",".join(link_types)
            query_parameters['linkTypes'] = self._serialize.query('link_types', link_types, 'str')
        if types is not None:
            types = ",".join(types)
            query_parameters['types'] = self._serialize.query('types', types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='b5b5b6d0-0308-40a1-b3f4-b9bb3c66878f',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemLinksBatch', response)

    def get_relation_type(self, relation):
        """GetRelationType.
        [Preview API] Gets the work item relation type definition.
        :param str relation: The relation name
        :rtype: :class:`<WorkItemRelationType> <azure.devops.v5_1.work-item-tracking.models.WorkItemRelationType>`
        """
        route_values = {}
        if relation is not None:
            route_values['relation'] = self._serialize.url('relation', relation, 'str')
        response = self._send(http_method='GET',
                              location_id='f5d33bc9-5b49-4a3c-a9bd-f3cd46dd2165',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemRelationType', response)

    def get_relation_types(self):
        """GetRelationTypes.
        [Preview API] Gets the work item relation types.
        :rtype: [WorkItemRelationType]
        """
        response = self._send(http_method='GET',
                              location_id='f5d33bc9-5b49-4a3c-a9bd-f3cd46dd2165',
                              version='5.1-preview.2')
        return self._deserialize('[WorkItemRelationType]', self._unwrap_collection(response))

    def read_reporting_revisions_get(self, project=None, fields=None, types=None, continuation_token=None, start_date_time=None, include_identity_ref=None, include_deleted=None, include_tag_ref=None, include_latest_only=None, expand=None, include_discussion_changes_only=None, max_page_size=None):
        """ReadReportingRevisionsGet.
        [Preview API] Get a batch of work item revisions with the option of including deleted items
        :param str project: Project ID or project name
        :param [str] fields: A list of fields to return in work item revisions. Omit this parameter to get all reportable fields.
        :param [str] types: A list of types to filter the results to specific work item types. Omit this parameter to get work item revisions of all work item types.
        :param str continuation_token: Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions.
        :param datetime start_date_time: Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter.
        :param bool include_identity_ref: Return an identity reference instead of a string value for identity fields.
        :param bool include_deleted: Specify if the deleted item should be returned.
        :param bool include_tag_ref: Specify if the tag objects should be returned for System.Tags field.
        :param bool include_latest_only: Return only the latest revisions of work items, skipping all historical revisions
        :param str expand: Return all the fields in work item revisions, including long text fields which are not returned by default
        :param bool include_discussion_changes_only: Return only the those revisions of work items, where only history field was changed
        :param int max_page_size: The maximum number of results to return in this batch
        :rtype: :class:`<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work-item-tracking.models.ReportingWorkItemRevisionsBatch>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if types is not None:
            types = ",".join(types)
            query_parameters['types'] = self._serialize.query('types', types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        if include_identity_ref is not None:
            query_parameters['includeIdentityRef'] = self._serialize.query('include_identity_ref', include_identity_ref, 'bool')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_tag_ref is not None:
            query_parameters['includeTagRef'] = self._serialize.query('include_tag_ref', include_tag_ref, 'bool')
        if include_latest_only is not None:
            query_parameters['includeLatestOnly'] = self._serialize.query('include_latest_only', include_latest_only, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if include_discussion_changes_only is not None:
            query_parameters['includeDiscussionChangesOnly'] = self._serialize.query('include_discussion_changes_only', include_discussion_changes_only, 'bool')
        if max_page_size is not None:
            query_parameters['$maxPageSize'] = self._serialize.query('max_page_size', max_page_size, 'int')
        response = self._send(http_method='GET',
                              location_id='f828fe59-dd87-495d-a17c-7a8d6211ca6c',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def read_reporting_revisions_post(self, filter, project=None, continuation_token=None, start_date_time=None, expand=None):
        """ReadReportingRevisionsPost.
        [Preview API] Get a batch of work item revisions. This request may be used if your list of fields is large enough that it may run the URL over the length limit.
        :param :class:`<ReportingWorkItemRevisionsFilter> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsFilter>` filter: An object that contains request settings: field filter, type filter, identity format
        :param str project: Project ID or project name
        :param str continuation_token: Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions.
        :param datetime start_date_time: Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter.
        :param str expand:
        :rtype: :class:`<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work-item-tracking.models.ReportingWorkItemRevisionsBatch>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(filter, 'ReportingWorkItemRevisionsFilter')
        response = self._send(http_method='POST',
                              location_id='f828fe59-dd87-495d-a17c-7a8d6211ca6c',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def read_reporting_discussions(self, project=None, continuation_token=None, max_page_size=None):
        """ReadReportingDiscussions.
        [Preview API]
        :param str project: Project ID or project name
        :param str continuation_token:
        :param int max_page_size:
        :rtype: :class:`<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work-item-tracking.models.ReportingWorkItemRevisionsBatch>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if max_page_size is not None:
            query_parameters['$maxPageSize'] = self._serialize.query('max_page_size', max_page_size, 'int')
        response = self._send(http_method='GET',
                              location_id='4a644469-90c5-4fcc-9a9f-be0827d369ec',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def create_work_item(self, document, project, type, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None):
        """CreateWorkItem.
        [Preview API] Creates a single work item.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v5_1.work_item_tracking.models.[JsonPatchOperation]>` document: The JSON Patch document representing the work item
        :param str project: Project ID or project name
        :param str type: The work item type of the work item to create
        :param bool validate_only: Indicate if you only want to validate the changes without saving the work item
        :param bool bypass_rules: Do not enforce the work item type rules on this update
        :param bool suppress_notifications: Do not fire any notifications for this change
        :param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.
        :rtype: :class:`<WorkItem> <azure.devops.v5_1.work-item-tracking.models.WorkItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if validate_only is not None:
            query_parameters['validateOnly'] = self._serialize.query('validate_only', validate_only, 'bool')
        if bypass_rules is not None:
            query_parameters['bypassRules'] = self._serialize.query('bypass_rules', bypass_rules, 'bool')
        if suppress_notifications is not None:
            query_parameters['suppressNotifications'] = self._serialize.query('suppress_notifications', suppress_notifications, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='POST',
                              location_id='62d3d110-0047-428c-ad3c-4fe872c91c74',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('WorkItem', response)

    def get_work_item_template(self, project, type, fields=None, as_of=None, expand=None):
        """GetWorkItemTemplate.
        [Preview API] Returns a single work item from a template.
        :param str project: Project ID or project name
        :param str type: The work item type name
        :param str fields: Comma-separated list of requested fields
        :param datetime as_of: AsOf UTC date time string
        :param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.
        :rtype: :class:`<WorkItem> <azure.devops.v5_1.work-item-tracking.models.WorkItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if fields is not None:
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='62d3d110-0047-428c-ad3c-4fe872c91c74',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def delete_work_item(self, id, project=None, destroy=None):
        """DeleteWorkItem.
        [Preview API] Deletes the specified work item and sends it to the Recycle Bin, so that it can be restored back, if required. Optionally, if the destroy parameter has been set to true, it destroys the work item permanently. WARNING: If the destroy parameter is set to true, work items deleted by this command will NOT go to recycle-bin and there is no way to restore/recover them after deletion. It is recommended NOT to use this parameter. If you do, please use this parameter with extreme caution.
        :param int id: ID of the work item to be deleted
        :param str project: Project ID or project name
        :param bool destroy: Optional parameter, if set to true, the work item is deleted permanently. Please note: the destroy action is PERMANENT and cannot be undone.
        :rtype: :class:`<WorkItemDelete> <azure.devops.v5_1.work-item-tracking.models.WorkItemDelete>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if destroy is not None:
            query_parameters['destroy'] = self._serialize.query('destroy', destroy, 'bool')
        response = self._send(http_method='DELETE',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemDelete', response)

    def get_work_item(self, id, project=None, fields=None, as_of=None, expand=None):
        """GetWorkItem.
        [Preview API] Returns a single work item.
        :param int id: The work item id
        :param str project: Project ID or project name
        :param [str] fields: Comma-separated list of requested fields
        :param datetime as_of: AsOf UTC date time string
        :param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.
        :rtype: :class:`<WorkItem> <azure.devops.v5_1.work-item-tracking.models.WorkItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def get_work_items(self, ids, project=None, fields=None, as_of=None, expand=None, error_policy=None):
        """GetWorkItems.
        [Preview API] Returns a list of work items (Maximum 200)
        :param [int] ids: The comma-separated list of requested work item ids. (Maximum 200 ids allowed).
        :param str project: Project ID or project name
        :param [str] fields: Comma-separated list of requested fields
        :param datetime as_of: AsOf UTC date time string
        :param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.
        :param str error_policy: The flag to control error policy in a bulk get work items request. Possible options are {Fail, Omit}.
        :rtype: [WorkItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if error_policy is not None:
            query_parameters['errorPolicy'] = self._serialize.query('error_policy', error_policy, 'str')
        response = self._send(http_method='GET',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def update_work_item(self, document, id, project=None, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None):
        """UpdateWorkItem.
        [Preview API] Updates a single work item.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v5_1.work_item_tracking.models.[JsonPatchOperation]>` document: The JSON Patch document representing the update
        :param int id: The id of the work item to update
        :param str project: Project ID or project name
        :param bool validate_only: Indicate if you only want to validate the changes without saving the work item
        :param bool bypass_rules: Do not enforce the work item type rules on this update
        :param bool suppress_notifications: Do not fire any notifications for this change
        :param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.
        :rtype: :class:`<WorkItem> <azure.devops.v5_1.work-item-tracking.models.WorkItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if validate_only is not None:
            query_parameters['validateOnly'] = self._serialize.query('validate_only', validate_only, 'bool')
        if bypass_rules is not None:
            query_parameters['bypassRules'] = self._serialize.query('bypass_rules', bypass_rules, 'bool')
        if suppress_notifications is not None:
            query_parameters['suppressNotifications'] = self._serialize.query('suppress_notifications', suppress_notifications, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('WorkItem', response)

    def get_work_items_batch(self, work_item_get_request, project=None):
        """GetWorkItemsBatch.
        [Preview API] Gets work items for a list of work item ids (Maximum 200)
        :param :class:`<WorkItemBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.WorkItemBatchGetRequest>` work_item_get_request:
        :param str project: Project ID or project name
        :rtype: [WorkItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_get_request, 'WorkItemBatchGetRequest')
        response = self._send(http_method='POST',
                              location_id='908509b6-4248-4475-a1cd-829139ba419f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def get_work_item_next_states_on_checkin_action(self, ids, action=None):
        """GetWorkItemNextStatesOnCheckinAction.
        [Preview API] Returns the next state on the given work item IDs.
        :param [int] ids: list of work item ids
        :param str action: possible actions. Currently only supports checkin
        :rtype: [WorkItemNextStateOnTransition]
        """
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if action is not None:
            query_parameters['action'] = self._serialize.query('action', action, 'str')
        response = self._send(http_method='GET',
                              location_id='afae844b-e2f6-44c2-8053-17b3bb936a40',
                              version='5.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemNextStateOnTransition]', self._unwrap_collection(response))

    def get_work_item_type_categories(self, project):
        """GetWorkItemTypeCategories.
        [Preview API] Get all work item type categories.
        :param str project: Project ID or project name
        :rtype: [WorkItemTypeCategory]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='9b9f5734-36c8-415e-ba67-f83b45c31408',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemTypeCategory]', self._unwrap_collection(response))

    def get_work_item_type_category(self, project, category):
        """GetWorkItemTypeCategory.
        [Preview API] Get specific work item type category by name.
        :param str project: Project ID or project name
        :param str category: The category name
        :rtype: :class:`<WorkItemTypeCategory> <azure.devops.v5_1.work-item-tracking.models.WorkItemTypeCategory>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if category is not None:
            route_values['category'] = self._serialize.url('category', category, 'str')
        response = self._send(http_method='GET',
                              location_id='9b9f5734-36c8-415e-ba67-f83b45c31408',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemTypeCategory', response)

    def get_work_item_type(self, project, type):
        """GetWorkItemType.
        [Preview API] Returns a work item type definition.
        :param str project: Project ID or project name
        :param str type: Work item type name
        :rtype: :class:`<WorkItemType> <azure.devops.v5_1.work-item-tracking.models.WorkItemType>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7c8d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemType', response)

    def get_work_item_types(self, project):
        """GetWorkItemTypes.
        [Preview API] Returns the list of work item types
        :param str project: Project ID or project name
        :rtype: [WorkItemType]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='7c8d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemType]', self._unwrap_collection(response))

    def get_work_item_type_fields_with_references(self, project, type, expand=None):
        """GetWorkItemTypeFieldsWithReferences.
        [Preview API] Get a list of fields for a work item type with detailed references.
        :param str project: Project ID or project name
        :param str type: Work item type.
        :param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.
        :rtype: [WorkItemTypeFieldWithReferences]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='bd293ce5-3d25-4192-8e67-e8092e879efb',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemTypeFieldWithReferences]', self._unwrap_collection(response))

    def get_work_item_type_field_with_references(self, project, type, field, expand=None):
        """GetWorkItemTypeFieldWithReferences.
        [Preview API] Get a field for a work item type with detailed references.
        :param str project: Project ID or project name
        :param str type: Work item type.
        :param str field:
        :param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.
        :rtype: :class:`<WorkItemTypeFieldWithReferences> <azure.devops.v5_1.work-item-tracking.models.WorkItemTypeFieldWithReferences>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if field is not None:
            route_values['field'] = self._serialize.url('field', field, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='bd293ce5-3d25-4192-8e67-e8092e879efb',
                              version='5.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemTypeFieldWithReferences', response)

    def get_work_item_type_states(self, project, type):
        """GetWorkItemTypeStates.
        [Preview API] Returns the state names and colors for a work item type.
        :param str project: Project ID or project name
        :param str type: The state name
        :rtype: [WorkItemStateColor]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7c9d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemStateColor]', self._unwrap_collection(response))

