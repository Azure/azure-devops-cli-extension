# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Attachment(Model):
    """Attachment.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param author: The person that uploaded this attachment.
    :type author: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param content_hash: Content hash of on-disk representation of file content. Its calculated by the server by using SHA1 hash function.
    :type content_hash: str
    :param created_date: The time the attachment was uploaded.
    :type created_date: datetime
    :param description: The description of the attachment.
    :type description: str
    :param display_name: The display name of the attachment. Can't be null or empty.
    :type display_name: str
    :param id: Id of the attachment.
    :type id: int
    :param properties: Extended properties.
    :type properties: :class:`object <azure.devops.v5_1.git.models.object>`
    :param url: The url to download the content of the attachment.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'content_hash': {'key': 'contentHash', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, content_hash=None, created_date=None, description=None, display_name=None, id=None, properties=None, url=None):
        super(Attachment, self).__init__()
        self._links = _links
        self.author = author
        self.content_hash = content_hash
        self.created_date = created_date
        self.description = description
        self.display_name = display_name
        self.id = id
        self.properties = properties
        self.url = url


class Change(Model):
    """Change.

    :param change_type: The type of change that was made to the item.
    :type change_type: object
    :param item: Current version.
    :type item: object
    :param new_content: Content of the item after the change.
    :type new_content: :class:`ItemContent <azure.devops.v5_1.git.models.ItemContent>`
    :param source_server_item: Path of the item on the server.
    :type source_server_item: str
    :param url: URL to retrieve the item.
    :type url: str
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'item': {'key': 'item', 'type': 'object'},
        'new_content': {'key': 'newContent', 'type': 'ItemContent'},
        'source_server_item': {'key': 'sourceServerItem', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, change_type=None, item=None, new_content=None, source_server_item=None, url=None):
        super(Change, self).__init__()
        self.change_type = change_type
        self.item = item
        self.new_content = new_content
        self.source_server_item = source_server_item
        self.url = url


class Comment(Model):
    """Comment.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param author: The author of the comment.
    :type author: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param comment_type: The comment type at the time of creation.
    :type comment_type: object
    :param content: The comment content.
    :type content: str
    :param id: The comment ID. IDs start at 1 and are unique to a pull request.
    :type id: int
    :param is_deleted: Whether or not this comment was soft-deleted.
    :type is_deleted: bool
    :param last_content_updated_date: The date the comment's content was last updated.
    :type last_content_updated_date: datetime
    :param last_updated_date: The date the comment was last updated.
    :type last_updated_date: datetime
    :param parent_comment_id: The ID of the parent comment. This is used for replies.
    :type parent_comment_id: int
    :param published_date: The date the comment was first published.
    :type published_date: datetime
    :param users_liked: A list of the users who have liked this comment.
    :type users_liked: list of :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'comment_type': {'key': 'commentType', 'type': 'object'},
        'content': {'key': 'content', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_content_updated_date': {'key': 'lastContentUpdatedDate', 'type': 'iso-8601'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'parent_comment_id': {'key': 'parentCommentId', 'type': 'int'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'users_liked': {'key': 'usersLiked', 'type': '[IdentityRef]'}
    }

    def __init__(self, _links=None, author=None, comment_type=None, content=None, id=None, is_deleted=None, last_content_updated_date=None, last_updated_date=None, parent_comment_id=None, published_date=None, users_liked=None):
        super(Comment, self).__init__()
        self._links = _links
        self.author = author
        self.comment_type = comment_type
        self.content = content
        self.id = id
        self.is_deleted = is_deleted
        self.last_content_updated_date = last_content_updated_date
        self.last_updated_date = last_updated_date
        self.parent_comment_id = parent_comment_id
        self.published_date = published_date
        self.users_liked = users_liked


class CommentIterationContext(Model):
    """CommentIterationContext.

    :param first_comparing_iteration: The iteration of the file on the left side of the diff when the thread was created. If this value is equal to SecondComparingIteration, then this version is the common commit between the source and target branches of the pull request.
    :type first_comparing_iteration: int
    :param second_comparing_iteration: The iteration of the file on the right side of the diff when the thread was created.
    :type second_comparing_iteration: int
    """

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, second_comparing_iteration=None):
        super(CommentIterationContext, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.second_comparing_iteration = second_comparing_iteration


class CommentPosition(Model):
    """CommentPosition.

    :param line: The line number of a thread's position. Starts at 1.
    :type line: int
    :param offset: The character offset of a thread's position inside of a line. Starts at 0.
    :type offset: int
    """

    _attribute_map = {
        'line': {'key': 'line', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'}
    }

    def __init__(self, line=None, offset=None):
        super(CommentPosition, self).__init__()
        self.line = line
        self.offset = offset


class CommentThread(Model):
    """CommentThread.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param comments: A list of the comments.
    :type comments: list of :class:`Comment <azure.devops.v5_1.git.models.Comment>`
    :param id: The comment thread id.
    :type id: int
    :param identities: Set of identities related to this thread
    :type identities: dict
    :param is_deleted: Specify if the thread is deleted which happens when all comments are deleted.
    :type is_deleted: bool
    :param last_updated_date: The time this thread was last updated.
    :type last_updated_date: datetime
    :param properties: Optional properties associated with the thread as a collection of key-value pairs.
    :type properties: :class:`object <azure.devops.v5_1.git.models.object>`
    :param published_date: The time this thread was published.
    :type published_date: datetime
    :param status: The status of the comment thread.
    :type status: object
    :param thread_context: Specify thread context such as position in left/right file.
    :type thread_context: :class:`CommentThreadContext <azure.devops.v5_1.git.models.CommentThreadContext>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'identities': {'key': 'identities', 'type': '{IdentityRef}'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, identities=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None):
        super(CommentThread, self).__init__()
        self._links = _links
        self.comments = comments
        self.id = id
        self.identities = identities
        self.is_deleted = is_deleted
        self.last_updated_date = last_updated_date
        self.properties = properties
        self.published_date = published_date
        self.status = status
        self.thread_context = thread_context


class CommentThreadContext(Model):
    """CommentThreadContext.

    :param file_path: File path relative to the root of the repository. It's up to the client to use any path format.
    :type file_path: str
    :param left_file_end: Position of last character of the thread's span in left file.
    :type left_file_end: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param left_file_start: Position of first character of the thread's span in left file.
    :type left_file_start: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param right_file_end: Position of last character of the thread's span in right file.
    :type right_file_end: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param right_file_start: Position of first character of the thread's span in right file.
    :type right_file_start: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    """

    _attribute_map = {
        'file_path': {'key': 'filePath', 'type': 'str'},
        'left_file_end': {'key': 'leftFileEnd', 'type': 'CommentPosition'},
        'left_file_start': {'key': 'leftFileStart', 'type': 'CommentPosition'},
        'right_file_end': {'key': 'rightFileEnd', 'type': 'CommentPosition'},
        'right_file_start': {'key': 'rightFileStart', 'type': 'CommentPosition'}
    }

    def __init__(self, file_path=None, left_file_end=None, left_file_start=None, right_file_end=None, right_file_start=None):
        super(CommentThreadContext, self).__init__()
        self.file_path = file_path
        self.left_file_end = left_file_end
        self.left_file_start = left_file_start
        self.right_file_end = right_file_end
        self.right_file_start = right_file_start


class CommentTrackingCriteria(Model):
    """CommentTrackingCriteria.

    :param first_comparing_iteration: The iteration of the file on the left side of the diff that the thread will be tracked to. Threads were tracked if this is greater than 0.
    :type first_comparing_iteration: int
    :param orig_file_path: Original filepath the thread was created on before tracking. This will be different than the current thread filepath if the file in question was renamed in a later iteration.
    :type orig_file_path: str
    :param orig_left_file_end: Original position of last character of the thread's span in left file.
    :type orig_left_file_end: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param orig_left_file_start: Original position of first character of the thread's span in left file.
    :type orig_left_file_start: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param orig_right_file_end: Original position of last character of the thread's span in right file.
    :type orig_right_file_end: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param orig_right_file_start: Original position of first character of the thread's span in right file.
    :type orig_right_file_start: :class:`CommentPosition <azure.devops.v5_1.git.models.CommentPosition>`
    :param second_comparing_iteration: The iteration of the file on the right side of the diff that the thread will be tracked to. Threads were tracked if this is greater than 0.
    :type second_comparing_iteration: int
    """

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'orig_file_path': {'key': 'origFilePath', 'type': 'str'},
        'orig_left_file_end': {'key': 'origLeftFileEnd', 'type': 'CommentPosition'},
        'orig_left_file_start': {'key': 'origLeftFileStart', 'type': 'CommentPosition'},
        'orig_right_file_end': {'key': 'origRightFileEnd', 'type': 'CommentPosition'},
        'orig_right_file_start': {'key': 'origRightFileStart', 'type': 'CommentPosition'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, orig_file_path=None, orig_left_file_end=None, orig_left_file_start=None, orig_right_file_end=None, orig_right_file_start=None, second_comparing_iteration=None):
        super(CommentTrackingCriteria, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.orig_file_path = orig_file_path
        self.orig_left_file_end = orig_left_file_end
        self.orig_left_file_start = orig_left_file_start
        self.orig_right_file_end = orig_right_file_end
        self.orig_right_file_start = orig_right_file_start
        self.second_comparing_iteration = second_comparing_iteration


class FileContentMetadata(Model):
    """FileContentMetadata.

    :param content_type:
    :type content_type: str
    :param encoding:
    :type encoding: int
    :param extension:
    :type extension: str
    :param file_name:
    :type file_name: str
    :param is_binary:
    :type is_binary: bool
    :param is_image:
    :type is_image: bool
    :param vs_link:
    :type vs_link: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'encoding': {'key': 'encoding', 'type': 'int'},
        'extension': {'key': 'extension', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'is_binary': {'key': 'isBinary', 'type': 'bool'},
        'is_image': {'key': 'isImage', 'type': 'bool'},
        'vs_link': {'key': 'vsLink', 'type': 'str'}
    }

    def __init__(self, content_type=None, encoding=None, extension=None, file_name=None, is_binary=None, is_image=None, vs_link=None):
        super(FileContentMetadata, self).__init__()
        self.content_type = content_type
        self.encoding = encoding
        self.extension = extension
        self.file_name = file_name
        self.is_binary = is_binary
        self.is_image = is_image
        self.vs_link = vs_link


class FileDiff(Model):
    """FileDiff.

    :param line_diff_blocks: The collection of line diff blocks
    :type line_diff_blocks: list of :class:`LineDiffBlock <azure.devops.v5_1.git.models.LineDiffBlock>`
    :param original_path: Original path of item if different from current path.
    :type original_path: str
    :param path: Current path of item
    :type path: str
    """

    _attribute_map = {
        'line_diff_blocks': {'key': 'lineDiffBlocks', 'type': '[LineDiffBlock]'},
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, line_diff_blocks=None, original_path=None, path=None):
        super(FileDiff, self).__init__()
        self.line_diff_blocks = line_diff_blocks
        self.original_path = original_path
        self.path = path


class FileDiffParams(Model):
    """FileDiffParams.

    :param original_path: Original path of the file
    :type original_path: str
    :param path: Current path of the file
    :type path: str
    """

    _attribute_map = {
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, original_path=None, path=None):
        super(FileDiffParams, self).__init__()
        self.original_path = original_path
        self.path = path


class FileDiffsCriteria(Model):
    """FileDiffsCriteria.

    :param base_version_commit: Commit ID of the base version
    :type base_version_commit: str
    :param file_diff_params: List of parameters for each of the files for which we need to get the file diff
    :type file_diff_params: list of :class:`FileDiffParams <azure.devops.v5_1.git.models.FileDiffParams>`
    :param target_version_commit: Commit ID of the target version
    :type target_version_commit: str
    """

    _attribute_map = {
        'base_version_commit': {'key': 'baseVersionCommit', 'type': 'str'},
        'file_diff_params': {'key': 'fileDiffParams', 'type': '[FileDiffParams]'},
        'target_version_commit': {'key': 'targetVersionCommit', 'type': 'str'}
    }

    def __init__(self, base_version_commit=None, file_diff_params=None, target_version_commit=None):
        super(FileDiffsCriteria, self).__init__()
        self.base_version_commit = base_version_commit
        self.file_diff_params = file_diff_params
        self.target_version_commit = target_version_commit


class GitAnnotatedTag(Model):
    """GitAnnotatedTag.

    :param message: The tagging Message
    :type message: str
    :param name: The name of the annotated tag.
    :type name: str
    :param object_id: The objectId (Sha1Id) of the tag.
    :type object_id: str
    :param tagged_by: User info and date of tagging.
    :type tagged_by: :class:`GitUserDate <azure.devops.v5_1.git.models.GitUserDate>`
    :param tagged_object: Tagged git object.
    :type tagged_object: :class:`GitObject <azure.devops.v5_1.git.models.GitObject>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'tagged_by': {'key': 'taggedBy', 'type': 'GitUserDate'},
        'tagged_object': {'key': 'taggedObject', 'type': 'GitObject'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, message=None, name=None, object_id=None, tagged_by=None, tagged_object=None, url=None):
        super(GitAnnotatedTag, self).__init__()
        self.message = message
        self.name = name
        self.object_id = object_id
        self.tagged_by = tagged_by
        self.tagged_object = tagged_object
        self.url = url


class GitAsyncRefOperation(Model):
    """GitAsyncRefOperation.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <azure.devops.v5_1.git.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <azure.devops.v5_1.git.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url: A URL that can be used to make further requests for status about the operation
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None):
        super(GitAsyncRefOperation, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.parameters = parameters
        self.status = status
        self.url = url


class GitAsyncRefOperationDetail(Model):
    """GitAsyncRefOperationDetail.

    :param conflict: Indicates if there was a conflict generated when trying to cherry pick or revert the changes.
    :type conflict: bool
    :param current_commit_id: The current commit from the list of commits that are being cherry picked or reverted.
    :type current_commit_id: str
    :param failure_message: Detailed information about why the cherry pick or revert failed to complete.
    :type failure_message: str
    :param progress: A number between 0 and 1 indicating the percent complete of the operation.
    :type progress: float
    :param status: Provides a status code that indicates the reason the cherry pick or revert failed.
    :type status: object
    :param timedout: Indicates if the operation went beyond the maximum time allowed for a cherry pick or revert operation.
    :type timedout: bool
    """

    _attribute_map = {
        'conflict': {'key': 'conflict', 'type': 'bool'},
        'current_commit_id': {'key': 'currentCommitId', 'type': 'str'},
        'failure_message': {'key': 'failureMessage', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'float'},
        'status': {'key': 'status', 'type': 'object'},
        'timedout': {'key': 'timedout', 'type': 'bool'}
    }

    def __init__(self, conflict=None, current_commit_id=None, failure_message=None, progress=None, status=None, timedout=None):
        super(GitAsyncRefOperationDetail, self).__init__()
        self.conflict = conflict
        self.current_commit_id = current_commit_id
        self.failure_message = failure_message
        self.progress = progress
        self.status = status
        self.timedout = timedout


class GitAsyncRefOperationParameters(Model):
    """GitAsyncRefOperationParameters.

    :param generated_ref_name: Proposed target branch name for the cherry pick or revert operation.
    :type generated_ref_name: str
    :param onto_ref_name: The target branch for the cherry pick or revert operation.
    :type onto_ref_name: str
    :param repository: The git repository for the cherry pick or revert operation.
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    :param source: Details about the source of the cherry pick or revert operation (e.g. A pull request or a specific commit).
    :type source: :class:`GitAsyncRefOperationSource <azure.devops.v5_1.git.models.GitAsyncRefOperationSource>`
    """

    _attribute_map = {
        'generated_ref_name': {'key': 'generatedRefName', 'type': 'str'},
        'onto_ref_name': {'key': 'ontoRefName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'source': {'key': 'source', 'type': 'GitAsyncRefOperationSource'}
    }

    def __init__(self, generated_ref_name=None, onto_ref_name=None, repository=None, source=None):
        super(GitAsyncRefOperationParameters, self).__init__()
        self.generated_ref_name = generated_ref_name
        self.onto_ref_name = onto_ref_name
        self.repository = repository
        self.source = source


class GitAsyncRefOperationSource(Model):
    """GitAsyncRefOperationSource.

    :param commit_list: A list of commits to cherry pick or revert
    :type commit_list: list of :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param pull_request_id: Id of the pull request to cherry pick or revert
    :type pull_request_id: int
    """

    _attribute_map = {
        'commit_list': {'key': 'commitList', 'type': '[GitCommitRef]'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, commit_list=None, pull_request_id=None):
        super(GitAsyncRefOperationSource, self).__init__()
        self.commit_list = commit_list
        self.pull_request_id = pull_request_id


class GitBlobRef(Model):
    """GitBlobRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param size: Size of blob content (in bytes)
    :type size: long
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, url=None):
        super(GitBlobRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.url = url


class GitBranchStats(Model):
    """GitBranchStats.

    :param ahead_count: Number of commits ahead.
    :type ahead_count: int
    :param behind_count: Number of commits behind.
    :type behind_count: int
    :param commit: Current commit.
    :type commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param is_base_version: True if this is the result for the base version.
    :type is_base_version: bool
    :param name: Name of the ref.
    :type name: str
    """

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'commit': {'key': 'commit', 'type': 'GitCommitRef'},
        'is_base_version': {'key': 'isBaseVersion', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, behind_count=None, commit=None, is_base_version=None, name=None):
        super(GitBranchStats, self).__init__()
        self.ahead_count = ahead_count
        self.behind_count = behind_count
        self.commit = commit
        self.is_base_version = is_base_version
        self.name = name


class GitCherryPick(GitAsyncRefOperation):
    """GitCherryPick.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <azure.devops.v5_1.git.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <azure.devops.v5_1.git.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url: A URL that can be used to make further requests for status about the operation
    :type url: str
    :param cherry_pick_id:
    :type cherry_pick_id: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'cherry_pick_id': {'key': 'cherryPickId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, cherry_pick_id=None):
        super(GitCherryPick, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.cherry_pick_id = cherry_pick_id


class GitCommitChanges(Model):
    """GitCommitChanges.

    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <azure.devops.v5_1.git.models.object>`
    """

    _attribute_map = {
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'}
    }

    def __init__(self, change_counts=None, changes=None):
        super(GitCommitChanges, self).__init__()
        self.change_counts = change_counts
        self.changes = changes


class GitCommitDiffs(Model):
    """GitCommitDiffs.

    :param ahead_count:
    :type ahead_count: int
    :param all_changes_included:
    :type all_changes_included: bool
    :param base_commit:
    :type base_commit: str
    :param behind_count:
    :type behind_count: int
    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <azure.devops.v5_1.git.models.object>`
    :param common_commit:
    :type common_commit: str
    :param target_commit:
    :type target_commit: str
    """

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'all_changes_included': {'key': 'allChangesIncluded', 'type': 'bool'},
        'base_commit': {'key': 'baseCommit', 'type': 'str'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'common_commit': {'key': 'commonCommit', 'type': 'str'},
        'target_commit': {'key': 'targetCommit', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, all_changes_included=None, base_commit=None, behind_count=None, change_counts=None, changes=None, common_commit=None, target_commit=None):
        super(GitCommitDiffs, self).__init__()
        self.ahead_count = ahead_count
        self.all_changes_included = all_changes_included
        self.base_commit = base_commit
        self.behind_count = behind_count
        self.change_counts = change_counts
        self.changes = changes
        self.common_commit = common_commit
        self.target_commit = target_commit


class GitCommitRef(Model):
    """GitCommitRef.

    :param _links: A collection of related REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param author: Author of the commit.
    :type author: :class:`GitUserDate <azure.devops.v5_1.git.models.GitUserDate>`
    :param change_counts: Counts of the types of changes (edits, deletes, etc.) included with the commit.
    :type change_counts: dict
    :param changes: An enumeration of the changes included with the commit.
    :type changes: list of :class:`object <azure.devops.v5_1.git.models.object>`
    :param comment: Comment or message of the commit.
    :type comment: str
    :param comment_truncated: Indicates if the comment is truncated from the full Git commit comment message.
    :type comment_truncated: bool
    :param commit_id: ID (SHA-1) of the commit.
    :type commit_id: str
    :param committer: Committer of the commit.
    :type committer: :class:`GitUserDate <azure.devops.v5_1.git.models.GitUserDate>`
    :param parents: An enumeration of the parent commit IDs for this commit.
    :type parents: list of str
    :param push: The push associated with this commit.
    :type push: :class:`GitPushRef <azure.devops.v5_1.git.models.GitPushRef>`
    :param remote_url: Remote URL path to the commit.
    :type remote_url: str
    :param statuses: A list of status metadata from services and extensions that may associate additional information to the commit.
    :type statuses: list of :class:`GitStatus <azure.devops.v5_1.git.models.GitStatus>`
    :param url: REST URL for this resource.
    :type url: str
    :param work_items: A list of workitems associated with this commit.
    :type work_items: list of :class:`ResourceRef <azure.devops.v5_1.git.models.ResourceRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, push=None, remote_url=None, statuses=None, url=None, work_items=None):
        super(GitCommitRef, self).__init__()
        self._links = _links
        self.author = author
        self.change_counts = change_counts
        self.changes = changes
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.commit_id = commit_id
        self.committer = committer
        self.parents = parents
        self.push = push
        self.remote_url = remote_url
        self.statuses = statuses
        self.url = url
        self.work_items = work_items


class GitConflict(Model):
    """GitConflict.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param conflict_id:
    :type conflict_id: int
    :param conflict_path:
    :type conflict_path: str
    :param conflict_type:
    :type conflict_type: object
    :param merge_base_commit:
    :type merge_base_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param merge_origin:
    :type merge_origin: :class:`GitMergeOriginRef <azure.devops.v5_1.git.models.GitMergeOriginRef>`
    :param merge_source_commit:
    :type merge_source_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param merge_target_commit:
    :type merge_target_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param resolution_error:
    :type resolution_error: object
    :param resolution_status:
    :type resolution_status: object
    :param resolved_by:
    :type resolved_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param resolved_date:
    :type resolved_date: datetime
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'conflict_id': {'key': 'conflictId', 'type': 'int'},
        'conflict_path': {'key': 'conflictPath', 'type': 'str'},
        'conflict_type': {'key': 'conflictType', 'type': 'object'},
        'merge_base_commit': {'key': 'mergeBaseCommit', 'type': 'GitCommitRef'},
        'merge_origin': {'key': 'mergeOrigin', 'type': 'GitMergeOriginRef'},
        'merge_source_commit': {'key': 'mergeSourceCommit', 'type': 'GitCommitRef'},
        'merge_target_commit': {'key': 'mergeTargetCommit', 'type': 'GitCommitRef'},
        'resolution_error': {'key': 'resolutionError', 'type': 'object'},
        'resolution_status': {'key': 'resolutionStatus', 'type': 'object'},
        'resolved_by': {'key': 'resolvedBy', 'type': 'IdentityRef'},
        'resolved_date': {'key': 'resolvedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, conflict_id=None, conflict_path=None, conflict_type=None, merge_base_commit=None, merge_origin=None, merge_source_commit=None, merge_target_commit=None, resolution_error=None, resolution_status=None, resolved_by=None, resolved_date=None, url=None):
        super(GitConflict, self).__init__()
        self._links = _links
        self.conflict_id = conflict_id
        self.conflict_path = conflict_path
        self.conflict_type = conflict_type
        self.merge_base_commit = merge_base_commit
        self.merge_origin = merge_origin
        self.merge_source_commit = merge_source_commit
        self.merge_target_commit = merge_target_commit
        self.resolution_error = resolution_error
        self.resolution_status = resolution_status
        self.resolved_by = resolved_by
        self.resolved_date = resolved_date
        self.url = url


class GitConflictUpdateResult(Model):
    """GitConflictUpdateResult.

    :param conflict_id: Conflict ID that was provided by input
    :type conflict_id: int
    :param custom_message: Reason for failing
    :type custom_message: str
    :param updated_conflict: New state of the conflict after updating
    :type updated_conflict: :class:`GitConflict <azure.devops.v5_1.git.models.GitConflict>`
    :param update_status: Status of the update on the server
    :type update_status: object
    """

    _attribute_map = {
        'conflict_id': {'key': 'conflictId', 'type': 'int'},
        'custom_message': {'key': 'customMessage', 'type': 'str'},
        'updated_conflict': {'key': 'updatedConflict', 'type': 'GitConflict'},
        'update_status': {'key': 'updateStatus', 'type': 'object'}
    }

    def __init__(self, conflict_id=None, custom_message=None, updated_conflict=None, update_status=None):
        super(GitConflictUpdateResult, self).__init__()
        self.conflict_id = conflict_id
        self.custom_message = custom_message
        self.updated_conflict = updated_conflict
        self.update_status = update_status


class GitDeletedRepository(Model):
    """GitDeletedRepository.

    :param created_date:
    :type created_date: datetime
    :param deleted_by:
    :type deleted_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param deleted_date:
    :type deleted_date: datetime
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.git.models.TeamProjectReference>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, created_date=None, deleted_by=None, deleted_date=None, id=None, name=None, project=None):
        super(GitDeletedRepository, self).__init__()
        self.created_date = created_date
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.project = project


class GitFilePathsCollection(Model):
    """GitFilePathsCollection.

    :param commit_id:
    :type commit_id: str
    :param paths:
    :type paths: list of str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, commit_id=None, paths=None, url=None):
        super(GitFilePathsCollection, self).__init__()
        self.commit_id = commit_id
        self.paths = paths
        self.url = url


class GitForkOperationStatusDetail(Model):
    """GitForkOperationStatusDetail.

    :param all_steps: All valid steps for the forking process
    :type all_steps: list of str
    :param current_step: Index into AllSteps for the current step
    :type current_step: int
    :param error_message: Error message if the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitForkOperationStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message


class GitForkSyncRequest(Model):
    """GitForkSyncRequest.

    :param _links: Collection of related links
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitForkOperationStatusDetail <azure.devops.v5_1.git.models.GitForkOperationStatusDetail>`
    :param operation_id: Unique identifier for the operation.
    :type operation_id: int
    :param source: Fully-qualified identifier for the source repository.
    :type source: :class:`GlobalGitRepositoryKey <azure.devops.v5_1.git.models.GlobalGitRepositoryKey>`
    :param source_to_target_refs: If supplied, the set of ref mappings to use when performing a "sync" or create. If missing, all refs will be synchronized.
    :type source_to_target_refs: list of :class:`SourceToTargetRef <azure.devops.v5_1.git.models.SourceToTargetRef>`
    :param status:
    :type status: object
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitForkOperationStatusDetail'},
        'operation_id': {'key': 'operationId', 'type': 'int'},
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, _links=None, detailed_status=None, operation_id=None, source=None, source_to_target_refs=None, status=None):
        super(GitForkSyncRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.operation_id = operation_id
        self.source = source
        self.source_to_target_refs = source_to_target_refs
        self.status = status


class GitForkSyncRequestParameters(Model):
    """GitForkSyncRequestParameters.

    :param source: Fully-qualified identifier for the source repository.
    :type source: :class:`GlobalGitRepositoryKey <azure.devops.v5_1.git.models.GlobalGitRepositoryKey>`
    :param source_to_target_refs: If supplied, the set of ref mappings to use when performing a "sync" or create. If missing, all refs will be synchronized.
    :type source_to_target_refs: list of :class:`SourceToTargetRef <azure.devops.v5_1.git.models.SourceToTargetRef>`
    """

    _attribute_map = {
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'}
    }

    def __init__(self, source=None, source_to_target_refs=None):
        super(GitForkSyncRequestParameters, self).__init__()
        self.source = source
        self.source_to_target_refs = source_to_target_refs


class GitImportGitSource(Model):
    """GitImportGitSource.

    :param overwrite: Tells if this is a sync request or not
    :type overwrite: bool
    :param url: Url for the source repo
    :type url: str
    """

    _attribute_map = {
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, overwrite=None, url=None):
        super(GitImportGitSource, self).__init__()
        self.overwrite = overwrite
        self.url = url


class GitImportRequest(Model):
    """GitImportRequest.

    :param _links: Links to related resources.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status: Detailed status of the import, including the current step and an error message, if applicable.
    :type detailed_status: :class:`GitImportStatusDetail <azure.devops.v5_1.git.models.GitImportStatusDetail>`
    :param import_request_id: The unique identifier for this import request.
    :type import_request_id: int
    :param parameters: Parameters for creating the import request.
    :type parameters: :class:`GitImportRequestParameters <azure.devops.v5_1.git.models.GitImportRequestParameters>`
    :param repository: The target repository for this import.
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    :param status: Current status of the import.
    :type status: object
    :param url: A link back to this import request resource.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitImportStatusDetail'},
        'import_request_id': {'key': 'importRequestId', 'type': 'int'},
        'parameters': {'key': 'parameters', 'type': 'GitImportRequestParameters'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, import_request_id=None, parameters=None, repository=None, status=None, url=None):
        super(GitImportRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.import_request_id = import_request_id
        self.parameters = parameters
        self.repository = repository
        self.status = status
        self.url = url


class GitImportRequestParameters(Model):
    """GitImportRequestParameters.

    :param delete_service_endpoint_after_import_is_done: Option to delete service endpoint when import is done
    :type delete_service_endpoint_after_import_is_done: bool
    :param git_source: Source for importing git repository
    :type git_source: :class:`GitImportGitSource <azure.devops.v5_1.git.models.GitImportGitSource>`
    :param service_endpoint_id: Service Endpoint for connection to external endpoint
    :type service_endpoint_id: str
    :param tfvc_source: Source for importing tfvc repository
    :type tfvc_source: :class:`GitImportTfvcSource <azure.devops.v5_1.git.models.GitImportTfvcSource>`
    """

    _attribute_map = {
        'delete_service_endpoint_after_import_is_done': {'key': 'deleteServiceEndpointAfterImportIsDone', 'type': 'bool'},
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'}
    }

    def __init__(self, delete_service_endpoint_after_import_is_done=None, git_source=None, service_endpoint_id=None, tfvc_source=None):
        super(GitImportRequestParameters, self).__init__()
        self.delete_service_endpoint_after_import_is_done = delete_service_endpoint_after_import_is_done
        self.git_source = git_source
        self.service_endpoint_id = service_endpoint_id
        self.tfvc_source = tfvc_source


class GitImportStatusDetail(Model):
    """GitImportStatusDetail.

    :param all_steps: All valid steps for the import process
    :type all_steps: list of str
    :param current_step: Index into AllSteps for the current step
    :type current_step: int
    :param error_message: Error message if the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitImportStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message


class GitImportTfvcSource(Model):
    """GitImportTfvcSource.

    :param import_history: Set true to import History, false otherwise
    :type import_history: bool
    :param import_history_duration_in_days: Get history for last n days (max allowed value is 180 days)
    :type import_history_duration_in_days: int
    :param path: Path which we want to import (this can be copied from Path Control in Explorer)
    :type path: str
    """

    _attribute_map = {
        'import_history': {'key': 'importHistory', 'type': 'bool'},
        'import_history_duration_in_days': {'key': 'importHistoryDurationInDays', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, import_history=None, import_history_duration_in_days=None, path=None):
        super(GitImportTfvcSource, self).__init__()
        self.import_history = import_history
        self.import_history_duration_in_days = import_history_duration_in_days
        self.path = path


class GitItemDescriptor(Model):
    """GitItemDescriptor.

    :param path: Path to item
    :type path: str
    :param recursion_level: Specifies whether to include children (OneLevel), all descendants (Full), or None
    :type recursion_level: object
    :param version: Version string (interpretation based on VersionType defined in subclass
    :type version: str
    :param version_options: Version modifiers (e.g. previous)
    :type version_options: object
    :param version_type: How to interpret version (branch,tag,commit)
    :type version_type: object
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'recursion_level': {'key': 'recursionLevel', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, path=None, recursion_level=None, version=None, version_options=None, version_type=None):
        super(GitItemDescriptor, self).__init__()
        self.path = path
        self.recursion_level = recursion_level
        self.version = version
        self.version_options = version_options
        self.version_type = version_type


class GitItemRequestData(Model):
    """GitItemRequestData.

    :param include_content_metadata: Whether to include metadata for all items
    :type include_content_metadata: bool
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param item_descriptors: Collection of items to fetch, including path, version, and recursion level
    :type item_descriptors: list of :class:`GitItemDescriptor <azure.devops.v5_1.git.models.GitItemDescriptor>`
    :param latest_processed_change: Whether to include shallow ref to commit that last changed each item
    :type latest_processed_change: bool
    """

    _attribute_map = {
        'include_content_metadata': {'key': 'includeContentMetadata', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_descriptors': {'key': 'itemDescriptors', 'type': '[GitItemDescriptor]'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'bool'}
    }

    def __init__(self, include_content_metadata=None, include_links=None, item_descriptors=None, latest_processed_change=None):
        super(GitItemRequestData, self).__init__()
        self.include_content_metadata = include_content_metadata
        self.include_links = include_links
        self.item_descriptors = item_descriptors
        self.latest_processed_change = latest_processed_change


class GitMergeOperationStatusDetail(Model):
    """GitMergeOperationStatusDetail.

    :param failure_message: Error message if the operation failed.
    :type failure_message: str
    :param merge_commit_id: The commitId of the resultant merge commit.
    :type merge_commit_id: str
    """

    _attribute_map = {
        'failure_message': {'key': 'failureMessage', 'type': 'str'},
        'merge_commit_id': {'key': 'mergeCommitId', 'type': 'str'}
    }

    def __init__(self, failure_message=None, merge_commit_id=None):
        super(GitMergeOperationStatusDetail, self).__init__()
        self.failure_message = failure_message
        self.merge_commit_id = merge_commit_id


class GitMergeOriginRef(Model):
    """GitMergeOriginRef.

    :param pull_request_id:
    :type pull_request_id: int
    """

    _attribute_map = {
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, pull_request_id=None):
        super(GitMergeOriginRef, self).__init__()
        self.pull_request_id = pull_request_id


class GitMergeParameters(Model):
    """GitMergeParameters.

    :param comment: Comment or message of the commit.
    :type comment: str
    :param parents: An enumeration of the parent commit IDs for the merge  commit.
    :type parents: list of str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parents': {'key': 'parents', 'type': '[str]'}
    }

    def __init__(self, comment=None, parents=None):
        super(GitMergeParameters, self).__init__()
        self.comment = comment
        self.parents = parents


class GitObject(Model):
    """GitObject.

    :param object_id: Object Id (Sha1Id).
    :type object_id: str
    :param object_type: Type of object (Commit, Tree, Blob, Tag)
    :type object_type: object
    """

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'object'}
    }

    def __init__(self, object_id=None, object_type=None):
        super(GitObject, self).__init__()
        self.object_id = object_id
        self.object_type = object_type


class GitPolicyConfigurationResponse(Model):
    """GitPolicyConfigurationResponse.

    :param continuation_token: The HTTP client methods find the continuation token header in the response and populate this field.
    :type continuation_token: str
    :param policy_configurations:
    :type policy_configurations: list of :class:`PolicyConfiguration <azure.devops.v5_1.git.models.PolicyConfiguration>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'policy_configurations': {'key': 'policyConfigurations', 'type': '[PolicyConfiguration]'}
    }

    def __init__(self, continuation_token=None, policy_configurations=None):
        super(GitPolicyConfigurationResponse, self).__init__()
        self.continuation_token = continuation_token
        self.policy_configurations = policy_configurations


class GitPullRequest(Model):
    """GitPullRequest.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param artifact_id: A string which uniquely identifies this pull request. To generate an artifact ID for a pull request, use this template: ```vstfs:///Git/PullRequestId/{projectId}/{repositoryId}/{pullRequestId}```
    :type artifact_id: str
    :param auto_complete_set_by: If set, auto-complete is enabled for this pull request and this is the identity that enabled it.
    :type auto_complete_set_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param closed_by: The user who closed the pull request.
    :type closed_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param closed_date: The date when the pull request was closed (completed, abandoned, or merged externally).
    :type closed_date: datetime
    :param code_review_id: The code review ID of the pull request. Used internally.
    :type code_review_id: int
    :param commits: The commits contained in the pull request.
    :type commits: list of :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param completion_options: Options which affect how the pull request will be merged when it is completed.
    :type completion_options: :class:`GitPullRequestCompletionOptions <azure.devops.v5_1.git.models.GitPullRequestCompletionOptions>`
    :param completion_queue_time: The most recent date at which the pull request entered the queue to be completed. Used internally.
    :type completion_queue_time: datetime
    :param created_by: The identity of the user who created the pull request.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param creation_date: The date when the pull request was created.
    :type creation_date: datetime
    :param description: The description of the pull request.
    :type description: str
    :param fork_source: If this is a PR from a fork this will contain information about its source.
    :type fork_source: :class:`GitForkRef <azure.devops.v5_1.git.models.GitForkRef>`
    :param is_draft: Draft / WIP pull request.
    :type is_draft: bool
    :param labels: The labels associated with the pull request.
    :type labels: list of :class:`WebApiTagDefinition <azure.devops.v5_1.git.models.WebApiTagDefinition>`
    :param last_merge_commit: The commit of the most recent pull request merge. If empty, the most recent merge is in progress or was unsuccessful.
    :type last_merge_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param last_merge_source_commit: The commit at the head of the source branch at the time of the last pull request merge.
    :type last_merge_source_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param last_merge_target_commit: The commit at the head of the target branch at the time of the last pull request merge.
    :type last_merge_target_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param merge_failure_message: If set, pull request merge failed for this reason.
    :type merge_failure_message: str
    :param merge_failure_type: The type of failure (if any) of the pull request merge.
    :type merge_failure_type: object
    :param merge_id: The ID of the job used to run the pull request merge. Used internally.
    :type merge_id: str
    :param merge_options: Options used when the pull request merge runs. These are separate from completion options since completion happens only once and a new merge will run every time the source branch of the pull request changes.
    :type merge_options: :class:`GitPullRequestMergeOptions <azure.devops.v5_1.git.models.GitPullRequestMergeOptions>`
    :param merge_status: The current status of the pull request merge.
    :type merge_status: object
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param remote_url: Used internally.
    :type remote_url: str
    :param repository: The repository containing the target branch of the pull request.
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    :param reviewers: A list of reviewers on the pull request along with the state of their votes.
    :type reviewers: list of :class:`IdentityRefWithVote <azure.devops.v5_1.git.models.IdentityRefWithVote>`
    :param source_ref_name: The name of the source branch of the pull request.
    :type source_ref_name: str
    :param status: The status of the pull request.
    :type status: object
    :param supports_iterations: If true, this pull request supports multiple iterations. Iteration support means individual pushes to the source branch of the pull request can be reviewed and comments left in one iteration will be tracked across future iterations.
    :type supports_iterations: bool
    :param target_ref_name: The name of the target branch of the pull request.
    :type target_ref_name: str
    :param title: The title of the pull request.
    :type title: str
    :param url: Used internally.
    :type url: str
    :param work_item_refs: Any work item references associated with this pull request.
    :type work_item_refs: list of :class:`ResourceRef <azure.devops.v5_1.git.models.ResourceRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'auto_complete_set_by': {'key': 'autoCompleteSetBy', 'type': 'IdentityRef'},
        'closed_by': {'key': 'closedBy', 'type': 'IdentityRef'},
        'closed_date': {'key': 'closedDate', 'type': 'iso-8601'},
        'code_review_id': {'key': 'codeReviewId', 'type': 'int'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'completion_options': {'key': 'completionOptions', 'type': 'GitPullRequestCompletionOptions'},
        'completion_queue_time': {'key': 'completionQueueTime', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'fork_source': {'key': 'forkSource', 'type': 'GitForkRef'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'labels': {'key': 'labels', 'type': '[WebApiTagDefinition]'},
        'last_merge_commit': {'key': 'lastMergeCommit', 'type': 'GitCommitRef'},
        'last_merge_source_commit': {'key': 'lastMergeSourceCommit', 'type': 'GitCommitRef'},
        'last_merge_target_commit': {'key': 'lastMergeTargetCommit', 'type': 'GitCommitRef'},
        'merge_failure_message': {'key': 'mergeFailureMessage', 'type': 'str'},
        'merge_failure_type': {'key': 'mergeFailureType', 'type': 'object'},
        'merge_id': {'key': 'mergeId', 'type': 'str'},
        'merge_options': {'key': 'mergeOptions', 'type': 'GitPullRequestMergeOptions'},
        'merge_status': {'key': 'mergeStatus', 'type': 'object'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'reviewers': {'key': 'reviewers', 'type': '[IdentityRefWithVote]'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'supports_iterations': {'key': 'supportsIterations', 'type': 'bool'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_refs': {'key': 'workItemRefs', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, artifact_id=None, auto_complete_set_by=None, closed_by=None, closed_date=None, code_review_id=None, commits=None, completion_options=None, completion_queue_time=None, created_by=None, creation_date=None, description=None, fork_source=None, is_draft=None, labels=None, last_merge_commit=None, last_merge_source_commit=None, last_merge_target_commit=None, merge_failure_message=None, merge_failure_type=None, merge_id=None, merge_options=None, merge_status=None, pull_request_id=None, remote_url=None, repository=None, reviewers=None, source_ref_name=None, status=None, supports_iterations=None, target_ref_name=None, title=None, url=None, work_item_refs=None):
        super(GitPullRequest, self).__init__()
        self._links = _links
        self.artifact_id = artifact_id
        self.auto_complete_set_by = auto_complete_set_by
        self.closed_by = closed_by
        self.closed_date = closed_date
        self.code_review_id = code_review_id
        self.commits = commits
        self.completion_options = completion_options
        self.completion_queue_time = completion_queue_time
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.fork_source = fork_source
        self.is_draft = is_draft
        self.labels = labels
        self.last_merge_commit = last_merge_commit
        self.last_merge_source_commit = last_merge_source_commit
        self.last_merge_target_commit = last_merge_target_commit
        self.merge_failure_message = merge_failure_message
        self.merge_failure_type = merge_failure_type
        self.merge_id = merge_id
        self.merge_options = merge_options
        self.merge_status = merge_status
        self.pull_request_id = pull_request_id
        self.remote_url = remote_url
        self.repository = repository
        self.reviewers = reviewers
        self.source_ref_name = source_ref_name
        self.status = status
        self.supports_iterations = supports_iterations
        self.target_ref_name = target_ref_name
        self.title = title
        self.url = url
        self.work_item_refs = work_item_refs


class GitPullRequestChange(Model):
    """GitPullRequestChange.

    :param change_tracking_id: ID used to track files through multiple changes.
    :type change_tracking_id: int
    """

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'}
    }

    def __init__(self, change_tracking_id=None):
        super(GitPullRequestChange, self).__init__()
        self.change_tracking_id = change_tracking_id


class GitPullRequestCommentThread(CommentThread):
    """GitPullRequestCommentThread.

    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param comments: A list of the comments.
    :type comments: list of :class:`Comment <azure.devops.v5_1.git.models.Comment>`
    :param id: The comment thread id.
    :type id: int
    :param identities: Set of identities related to this thread
    :type identities: dict
    :param is_deleted: Specify if the thread is deleted which happens when all comments are deleted.
    :type is_deleted: bool
    :param last_updated_date: The time this thread was last updated.
    :type last_updated_date: datetime
    :param properties: Optional properties associated with the thread as a collection of key-value pairs.
    :type properties: :class:`object <azure.devops.v5_1.git.models.object>`
    :param published_date: The time this thread was published.
    :type published_date: datetime
    :param status: The status of the comment thread.
    :type status: object
    :param thread_context: Specify thread context such as position in left/right file.
    :type thread_context: :class:`CommentThreadContext <azure.devops.v5_1.git.models.CommentThreadContext>`
    :param pull_request_thread_context: Extended context information unique to pull requests
    :type pull_request_thread_context: :class:`GitPullRequestCommentThreadContext <azure.devops.v5_1.git.models.GitPullRequestCommentThreadContext>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'identities': {'key': 'identities', 'type': '{IdentityRef}'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'},
        'pull_request_thread_context': {'key': 'pullRequestThreadContext', 'type': 'GitPullRequestCommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, identities=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None, pull_request_thread_context=None):
        super(GitPullRequestCommentThread, self).__init__(_links=_links, comments=comments, id=id, identities=identities, is_deleted=is_deleted, last_updated_date=last_updated_date, properties=properties, published_date=published_date, status=status, thread_context=thread_context)
        self.pull_request_thread_context = pull_request_thread_context


class GitPullRequestCommentThreadContext(Model):
    """GitPullRequestCommentThreadContext.

    :param change_tracking_id: Used to track a comment across iterations. This value can be found by looking at the iteration's changes list. Must be set for pull requests with iteration support. Otherwise, it's not required for 'legacy' pull requests.
    :type change_tracking_id: int
    :param iteration_context: The iteration context being viewed when the thread was created.
    :type iteration_context: :class:`CommentIterationContext <azure.devops.v5_1.git.models.CommentIterationContext>`
    :param tracking_criteria: The criteria used to track this thread. If this property is filled out when the thread is returned, then the thread has been tracked from its original location using the given criteria.
    :type tracking_criteria: :class:`CommentTrackingCriteria <azure.devops.v5_1.git.models.CommentTrackingCriteria>`
    """

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'},
        'iteration_context': {'key': 'iterationContext', 'type': 'CommentIterationContext'},
        'tracking_criteria': {'key': 'trackingCriteria', 'type': 'CommentTrackingCriteria'}
    }

    def __init__(self, change_tracking_id=None, iteration_context=None, tracking_criteria=None):
        super(GitPullRequestCommentThreadContext, self).__init__()
        self.change_tracking_id = change_tracking_id
        self.iteration_context = iteration_context
        self.tracking_criteria = tracking_criteria


class GitPullRequestCompletionOptions(Model):
    """GitPullRequestCompletionOptions.

    :param bypass_policy: If true, policies will be explicitly bypassed while the pull request is completed.
    :type bypass_policy: bool
    :param bypass_reason: If policies are bypassed, this reason is stored as to why bypass was used.
    :type bypass_reason: str
    :param delete_source_branch: If true, the source branch of the pull request will be deleted after completion.
    :type delete_source_branch: bool
    :param merge_commit_message: If set, this will be used as the commit message of the merge commit.
    :type merge_commit_message: str
    :param merge_strategy: Specify the strategy used to merge the pull request during completion. If MergeStrategy is not set to any value, a no-FF merge will be created if SquashMerge == false. If MergeStrategy is not set to any value, the pull request commits will be squash if SquashMerge == true. The SquashMerge member is deprecated. It is recommended that you explicitly set MergeStrategy in all cases. If an explicit value is provided for MergeStrategy, the SquashMerge member will be ignored.
    :type merge_strategy: object
    :param squash_merge: SquashMerge is deprecated. You should explicity set the value of MergeStrategy. If MergeStrategy is set to any value, the SquashMerge value will be ignored. If MergeStrategy is not set, the merge strategy will be no-fast-forward if this flag is false, or squash if true.
    :type squash_merge: bool
    :param transition_work_items: If true, we will attempt to transition any work items linked to the pull request into the next logical state (i.e. Active -> Resolved)
    :type transition_work_items: bool
    :param triggered_by_auto_complete: If true, the current completion attempt was triggered via auto-complete. Used internally.
    :type triggered_by_auto_complete: bool
    """

    _attribute_map = {
        'bypass_policy': {'key': 'bypassPolicy', 'type': 'bool'},
        'bypass_reason': {'key': 'bypassReason', 'type': 'str'},
        'delete_source_branch': {'key': 'deleteSourceBranch', 'type': 'bool'},
        'merge_commit_message': {'key': 'mergeCommitMessage', 'type': 'str'},
        'merge_strategy': {'key': 'mergeStrategy', 'type': 'object'},
        'squash_merge': {'key': 'squashMerge', 'type': 'bool'},
        'transition_work_items': {'key': 'transitionWorkItems', 'type': 'bool'},
        'triggered_by_auto_complete': {'key': 'triggeredByAutoComplete', 'type': 'bool'}
    }

    def __init__(self, bypass_policy=None, bypass_reason=None, delete_source_branch=None, merge_commit_message=None, merge_strategy=None, squash_merge=None, transition_work_items=None, triggered_by_auto_complete=None):
        super(GitPullRequestCompletionOptions, self).__init__()
        self.bypass_policy = bypass_policy
        self.bypass_reason = bypass_reason
        self.delete_source_branch = delete_source_branch
        self.merge_commit_message = merge_commit_message
        self.merge_strategy = merge_strategy
        self.squash_merge = squash_merge
        self.transition_work_items = transition_work_items
        self.triggered_by_auto_complete = triggered_by_auto_complete


class GitPullRequestIteration(Model):
    """GitPullRequestIteration.

    :param _links: A collection of related REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param author: Author of the pull request iteration.
    :type author: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param change_list: Changes included with the pull request iteration.
    :type change_list: list of :class:`GitPullRequestChange <azure.devops.v5_1.git.models.GitPullRequestChange>`
    :param commits: The commits included with the pull request iteration.
    :type commits: list of :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param common_ref_commit: The first common Git commit of the source and target refs.
    :type common_ref_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param created_date: The creation date of the pull request iteration.
    :type created_date: datetime
    :param description: Description of the pull request iteration.
    :type description: str
    :param has_more_commits: Indicates if the Commits property contains a truncated list of commits in this pull request iteration.
    :type has_more_commits: bool
    :param id: ID of the pull request iteration. Iterations are created as a result of creating and pushing updates to a pull request.
    :type id: int
    :param new_target_ref_name: If the iteration reason is Retarget, this is the refName of the new target
    :type new_target_ref_name: str
    :param old_target_ref_name: If the iteration reason is Retarget, this is the original target refName
    :type old_target_ref_name: str
    :param push: The Git push information associated with this pull request iteration.
    :type push: :class:`GitPushRef <azure.devops.v5_1.git.models.GitPushRef>`
    :param reason: The reason for which the pull request iteration was created.
    :type reason: object
    :param source_ref_commit: The source Git commit of this iteration.
    :type source_ref_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param target_ref_commit: The target Git commit of this iteration.
    :type target_ref_commit: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param updated_date: The updated date of the pull request iteration.
    :type updated_date: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'change_list': {'key': 'changeList', 'type': '[GitPullRequestChange]'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'common_ref_commit': {'key': 'commonRefCommit', 'type': 'GitCommitRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'has_more_commits': {'key': 'hasMoreCommits', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'new_target_ref_name': {'key': 'newTargetRefName', 'type': 'str'},
        'old_target_ref_name': {'key': 'oldTargetRefName', 'type': 'str'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'reason': {'key': 'reason', 'type': 'object'},
        'source_ref_commit': {'key': 'sourceRefCommit', 'type': 'GitCommitRef'},
        'target_ref_commit': {'key': 'targetRefCommit', 'type': 'GitCommitRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, author=None, change_list=None, commits=None, common_ref_commit=None, created_date=None, description=None, has_more_commits=None, id=None, new_target_ref_name=None, old_target_ref_name=None, push=None, reason=None, source_ref_commit=None, target_ref_commit=None, updated_date=None):
        super(GitPullRequestIteration, self).__init__()
        self._links = _links
        self.author = author
        self.change_list = change_list
        self.commits = commits
        self.common_ref_commit = common_ref_commit
        self.created_date = created_date
        self.description = description
        self.has_more_commits = has_more_commits
        self.id = id
        self.new_target_ref_name = new_target_ref_name
        self.old_target_ref_name = old_target_ref_name
        self.push = push
        self.reason = reason
        self.source_ref_commit = source_ref_commit
        self.target_ref_commit = target_ref_commit
        self.updated_date = updated_date


class GitPullRequestIterationChanges(Model):
    """GitPullRequestIterationChanges.

    :param change_entries: Changes made in the iteration.
    :type change_entries: list of :class:`GitPullRequestChange <azure.devops.v5_1.git.models.GitPullRequestChange>`
    :param next_skip: Value to specify as skip to get the next page of changes.  This will be zero if there are no more changes.
    :type next_skip: int
    :param next_top: Value to specify as top to get the next page of changes.  This will be zero if there are no more changes.
    :type next_top: int
    """

    _attribute_map = {
        'change_entries': {'key': 'changeEntries', 'type': '[GitPullRequestChange]'},
        'next_skip': {'key': 'nextSkip', 'type': 'int'},
        'next_top': {'key': 'nextTop', 'type': 'int'}
    }

    def __init__(self, change_entries=None, next_skip=None, next_top=None):
        super(GitPullRequestIterationChanges, self).__init__()
        self.change_entries = change_entries
        self.next_skip = next_skip
        self.next_top = next_top


class GitPullRequestMergeOptions(Model):
    """GitPullRequestMergeOptions.

    :param detect_rename_false_positives:
    :type detect_rename_false_positives: bool
    :param disable_renames: If true, rename detection will not be performed during the merge.
    :type disable_renames: bool
    """

    _attribute_map = {
        'detect_rename_false_positives': {'key': 'detectRenameFalsePositives', 'type': 'bool'},
        'disable_renames': {'key': 'disableRenames', 'type': 'bool'}
    }

    def __init__(self, detect_rename_false_positives=None, disable_renames=None):
        super(GitPullRequestMergeOptions, self).__init__()
        self.detect_rename_false_positives = detect_rename_false_positives
        self.disable_renames = disable_renames


class GitPullRequestQuery(Model):
    """GitPullRequestQuery.

    :param queries: The queries to perform.
    :type queries: list of :class:`GitPullRequestQueryInput <azure.devops.v5_1.git.models.GitPullRequestQueryInput>`
    :param results: The results of the queries. This matches the QueryInputs list so Results[n] are the results of QueryInputs[n]. Each entry in the list is a dictionary of commit->pull requests.
    :type results: list of {[GitPullRequest]}
    """

    _attribute_map = {
        'queries': {'key': 'queries', 'type': '[GitPullRequestQueryInput]'},
        'results': {'key': 'results', 'type': '[{[GitPullRequest]}]'}
    }

    def __init__(self, queries=None, results=None):
        super(GitPullRequestQuery, self).__init__()
        self.queries = queries
        self.results = results


class GitPullRequestQueryInput(Model):
    """GitPullRequestQueryInput.

    :param items: The list of commit IDs to search for.
    :type items: list of str
    :param type: The type of query to perform.
    :type type: object
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, items=None, type=None):
        super(GitPullRequestQueryInput, self).__init__()
        self.items = items
        self.type = type


class GitPullRequestSearchCriteria(Model):
    """GitPullRequestSearchCriteria.

    :param creator_id: If set, search for pull requests that were created by this identity.
    :type creator_id: str
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param repository_id: If set, search for pull requests whose target branch is in this repository.
    :type repository_id: str
    :param reviewer_id: If set, search for pull requests that have this identity as a reviewer.
    :type reviewer_id: str
    :param source_ref_name: If set, search for pull requests from this branch.
    :type source_ref_name: str
    :param source_repository_id: If set, search for pull requests whose source branch is in this repository.
    :type source_repository_id: str
    :param status: If set, search for pull requests that are in this state. Defaults to Active if unset.
    :type status: object
    :param target_ref_name: If set, search for pull requests into this branch.
    :type target_ref_name: str
    """

    _attribute_map = {
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'reviewer_id': {'key': 'reviewerId', 'type': 'str'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'}
    }

    def __init__(self, creator_id=None, include_links=None, repository_id=None, reviewer_id=None, source_ref_name=None, source_repository_id=None, status=None, target_ref_name=None):
        super(GitPullRequestSearchCriteria, self).__init__()
        self.creator_id = creator_id
        self.include_links = include_links
        self.repository_id = repository_id
        self.reviewer_id = reviewer_id
        self.source_ref_name = source_ref_name
        self.source_repository_id = source_repository_id
        self.status = status
        self.target_ref_name = target_ref_name


class GitPushRef(Model):
    """GitPushRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param push_id:
    :type push_id: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None):
        super(GitPushRef, self).__init__()
        self._links = _links
        self.date = date
        self.push_correlation_id = push_correlation_id
        self.pushed_by = pushed_by
        self.push_id = push_id
        self.url = url


class GitPushSearchCriteria(Model):
    """GitPushSearchCriteria.

    :param from_date:
    :type from_date: datetime
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param include_ref_updates:
    :type include_ref_updates: bool
    :param pusher_id:
    :type pusher_id: str
    :param ref_name:
    :type ref_name: str
    :param to_date:
    :type to_date: datetime
    """

    _attribute_map = {
        'from_date': {'key': 'fromDate', 'type': 'iso-8601'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_ref_updates': {'key': 'includeRefUpdates', 'type': 'bool'},
        'pusher_id': {'key': 'pusherId', 'type': 'str'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'iso-8601'}
    }

    def __init__(self, from_date=None, include_links=None, include_ref_updates=None, pusher_id=None, ref_name=None, to_date=None):
        super(GitPushSearchCriteria, self).__init__()
        self.from_date = from_date
        self.include_links = include_links
        self.include_ref_updates = include_ref_updates
        self.pusher_id = pusher_id
        self.ref_name = ref_name
        self.to_date = to_date


class GitQueryBranchStatsCriteria(Model):
    """GitQueryBranchStatsCriteria.

    :param base_commit:
    :type base_commit: :class:`GitVersionDescriptor <azure.devops.v5_1.git.models.GitVersionDescriptor>`
    :param target_commits:
    :type target_commits: list of :class:`GitVersionDescriptor <azure.devops.v5_1.git.models.GitVersionDescriptor>`
    """

    _attribute_map = {
        'base_commit': {'key': 'baseCommit', 'type': 'GitVersionDescriptor'},
        'target_commits': {'key': 'targetCommits', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, base_commit=None, target_commits=None):
        super(GitQueryBranchStatsCriteria, self).__init__()
        self.base_commit = base_commit
        self.target_commits = target_commits


class GitQueryCommitsCriteria(Model):
    """GitQueryCommitsCriteria.

    :param skip: Number of entries to skip
    :type skip: int
    :param top: Maximum number of entries to retrieve
    :type top: int
    :param author: Alias or display name of the author
    :type author: str
    :param compare_version: Only applicable when ItemVersion specified. If provided, start walking history starting at this commit.
    :type compare_version: :class:`GitVersionDescriptor <azure.devops.v5_1.git.models.GitVersionDescriptor>`
    :param exclude_deletes: Only applies when an itemPath is specified. This determines whether to exclude delete entries of the specified path.
    :type exclude_deletes: bool
    :param from_commit_id: If provided, a lower bound for filtering commits alphabetically
    :type from_commit_id: str
    :param from_date: If provided, only include history entries created after this date (string)
    :type from_date: str
    :param history_mode: What Git history mode should be used. This only applies to the search criteria when Ids = null and an itemPath is specified.
    :type history_mode: object
    :param ids: If provided, specifies the exact commit ids of the commits to fetch. May not be combined with other parameters.
    :type ids: list of str
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param include_push_data: Whether to include the push information
    :type include_push_data: bool
    :param include_user_image_url: Whether to include the image Url for committers and authors
    :type include_user_image_url: bool
    :param include_work_items: Whether to include linked work items
    :type include_work_items: bool
    :param item_path: Path of item to search under
    :type item_path: str
    :param item_version: If provided, identifies the commit or branch to search
    :type item_version: :class:`GitVersionDescriptor <azure.devops.v5_1.git.models.GitVersionDescriptor>`
    :param to_commit_id: If provided, an upper bound for filtering commits alphabetically
    :type to_commit_id: str
    :param to_date: If provided, only include history entries created before this date (string)
    :type to_date: str
    :param user: Alias or display name of the committer
    :type user: str
    """

    _attribute_map = {
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'author': {'key': 'author', 'type': 'str'},
        'compare_version': {'key': 'compareVersion', 'type': 'GitVersionDescriptor'},
        'exclude_deletes': {'key': 'excludeDeletes', 'type': 'bool'},
        'from_commit_id': {'key': 'fromCommitId', 'type': 'str'},
        'from_date': {'key': 'fromDate', 'type': 'str'},
        'history_mode': {'key': 'historyMode', 'type': 'object'},
        'ids': {'key': 'ids', 'type': '[str]'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_push_data': {'key': 'includePushData', 'type': 'bool'},
        'include_user_image_url': {'key': 'includeUserImageUrl', 'type': 'bool'},
        'include_work_items': {'key': 'includeWorkItems', 'type': 'bool'},
        'item_path': {'key': 'itemPath', 'type': 'str'},
        'item_version': {'key': 'itemVersion', 'type': 'GitVersionDescriptor'},
        'to_commit_id': {'key': 'toCommitId', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'str'},
        'user': {'key': 'user', 'type': 'str'}
    }

    def __init__(self, skip=None, top=None, author=None, compare_version=None, exclude_deletes=None, from_commit_id=None, from_date=None, history_mode=None, ids=None, include_links=None, include_push_data=None, include_user_image_url=None, include_work_items=None, item_path=None, item_version=None, to_commit_id=None, to_date=None, user=None):
        super(GitQueryCommitsCriteria, self).__init__()
        self.skip = skip
        self.top = top
        self.author = author
        self.compare_version = compare_version
        self.exclude_deletes = exclude_deletes
        self.from_commit_id = from_commit_id
        self.from_date = from_date
        self.history_mode = history_mode
        self.ids = ids
        self.include_links = include_links
        self.include_push_data = include_push_data
        self.include_user_image_url = include_user_image_url
        self.include_work_items = include_work_items
        self.item_path = item_path
        self.item_version = item_version
        self.to_commit_id = to_commit_id
        self.to_date = to_date
        self.user = user


class GitRecycleBinRepositoryDetails(Model):
    """GitRecycleBinRepositoryDetails.

    :param deleted: Setting to false will undo earlier deletion and restore the repository.
    :type deleted: bool
    """

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(GitRecycleBinRepositoryDetails, self).__init__()
        self.deleted = deleted


class GitRef(Model):
    """GitRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param creator:
    :type creator: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param is_locked:
    :type is_locked: bool
    :param is_locked_by:
    :type is_locked_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param name:
    :type name: str
    :param object_id:
    :type object_id: str
    :param peeled_object_id:
    :type peeled_object_id: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <azure.devops.v5_1.git.models.GitStatus>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'creator': {'key': 'creator', 'type': 'IdentityRef'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, creator=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None):
        super(GitRef, self).__init__()
        self._links = _links
        self.creator = creator
        self.is_locked = is_locked
        self.is_locked_by = is_locked_by
        self.name = name
        self.object_id = object_id
        self.peeled_object_id = peeled_object_id
        self.statuses = statuses
        self.url = url


class GitRefFavorite(Model):
    """GitRefFavorite.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param id:
    :type id: int
    :param identity_id:
    :type identity_id: str
    :param name:
    :type name: str
    :param repository_id:
    :type repository_id: str
    :param type:
    :type type: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, identity_id=None, name=None, repository_id=None, type=None, url=None):
        super(GitRefFavorite, self).__init__()
        self._links = _links
        self.id = id
        self.identity_id = identity_id
        self.name = name
        self.repository_id = repository_id
        self.type = type
        self.url = url


class GitRefUpdate(Model):
    """GitRefUpdate.

    :param is_locked:
    :type is_locked: bool
    :param name:
    :type name: str
    :param new_object_id:
    :type new_object_id: str
    :param old_object_id:
    :type old_object_id: str
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, is_locked=None, name=None, new_object_id=None, old_object_id=None, repository_id=None):
        super(GitRefUpdate, self).__init__()
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.repository_id = repository_id


class GitRefUpdateResult(Model):
    """GitRefUpdateResult.

    :param custom_message: Custom message for the result object For instance, Reason for failing.
    :type custom_message: str
    :param is_locked: Whether the ref is locked or not
    :type is_locked: bool
    :param name: Ref name
    :type name: str
    :param new_object_id: New object ID
    :type new_object_id: str
    :param old_object_id: Old object ID
    :type old_object_id: str
    :param rejected_by: Name of the plugin that rejected the updated.
    :type rejected_by: str
    :param repository_id: Repository ID
    :type repository_id: str
    :param success: True if the ref update succeeded, false otherwise
    :type success: bool
    :param update_status: Status of the update from the TFS server.
    :type update_status: object
    """

    _attribute_map = {
        'custom_message': {'key': 'customMessage', 'type': 'str'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'rejected_by': {'key': 'rejectedBy', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'update_status': {'key': 'updateStatus', 'type': 'object'}
    }

    def __init__(self, custom_message=None, is_locked=None, name=None, new_object_id=None, old_object_id=None, rejected_by=None, repository_id=None, success=None, update_status=None):
        super(GitRefUpdateResult, self).__init__()
        self.custom_message = custom_message
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.rejected_by = rejected_by
        self.repository_id = repository_id
        self.success = success
        self.update_status = update_status


class GitRepository(Model):
    """GitRepository.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param default_branch:
    :type default_branch: str
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <azure.devops.v5_1.git.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.git.models.TeamProjectReference>`
    :param remote_url:
    :type remote_url: str
    :param size: Compressed size (bytes) of the repository.
    :type size: long
    :param ssh_url:
    :type ssh_url: str
    :param url:
    :type url: str
    :param valid_remote_urls:
    :type valid_remote_urls: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'ssh_url': {'key': 'sshUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, size=None, ssh_url=None, url=None, valid_remote_urls=None):
        super(GitRepository, self).__init__()
        self._links = _links
        self.default_branch = default_branch
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.parent_repository = parent_repository
        self.project = project
        self.remote_url = remote_url
        self.size = size
        self.ssh_url = ssh_url
        self.url = url
        self.valid_remote_urls = valid_remote_urls


class GitRepositoryCreateOptions(Model):
    """GitRepositoryCreateOptions.

    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <azure.devops.v5_1.git.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.git.models.TeamProjectReference>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, name=None, parent_repository=None, project=None):
        super(GitRepositoryCreateOptions, self).__init__()
        self.name = name
        self.parent_repository = parent_repository
        self.project = project


class GitRepositoryRef(Model):
    """GitRepositoryRef.

    :param collection: Team Project Collection where this Fork resides
    :type collection: :class:`TeamProjectCollectionReference <azure.devops.v5_1.git.models.TeamProjectCollectionReference>`
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.git.models.TeamProjectReference>`
    :param remote_url:
    :type remote_url: str
    :param ssh_url:
    :type ssh_url: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'ssh_url': {'key': 'sshUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, collection=None, id=None, is_fork=None, name=None, project=None, remote_url=None, ssh_url=None, url=None):
        super(GitRepositoryRef, self).__init__()
        self.collection = collection
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.project = project
        self.remote_url = remote_url
        self.ssh_url = ssh_url
        self.url = url


class GitRepositoryStats(Model):
    """GitRepositoryStats.

    :param active_pull_requests_count:
    :type active_pull_requests_count: int
    :param branches_count:
    :type branches_count: int
    :param commits_count:
    :type commits_count: int
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'active_pull_requests_count': {'key': 'activePullRequestsCount', 'type': 'int'},
        'branches_count': {'key': 'branchesCount', 'type': 'int'},
        'commits_count': {'key': 'commitsCount', 'type': 'int'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, active_pull_requests_count=None, branches_count=None, commits_count=None, repository_id=None):
        super(GitRepositoryStats, self).__init__()
        self.active_pull_requests_count = active_pull_requests_count
        self.branches_count = branches_count
        self.commits_count = commits_count
        self.repository_id = repository_id


class GitRevert(GitAsyncRefOperation):
    """GitRevert.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <azure.devops.v5_1.git.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <azure.devops.v5_1.git.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url: A URL that can be used to make further requests for status about the operation
    :type url: str
    :param revert_id:
    :type revert_id: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'revert_id': {'key': 'revertId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, revert_id=None):
        super(GitRevert, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.revert_id = revert_id


class GitStatus(Model):
    """GitStatus.

    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param context: Context of the status.
    :type context: :class:`GitStatusContext <azure.devops.v5_1.git.models.GitStatusContext>`
    :param created_by: Identity that created the status.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param creation_date: Creation date and time of the status.
    :type creation_date: datetime
    :param description: Status description. Typically describes current state of the status.
    :type description: str
    :param id: Status identifier.
    :type id: int
    :param state: State of the status.
    :type state: object
    :param target_url: URL with status details.
    :type target_url: str
    :param updated_date: Last update date and time of the status.
    :type updated_date: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None):
        super(GitStatus, self).__init__()
        self._links = _links
        self.context = context
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.id = id
        self.state = state
        self.target_url = target_url
        self.updated_date = updated_date


class GitStatusContext(Model):
    """GitStatusContext.

    :param genre: Genre of the status. Typically name of the service/tool generating the status, can be empty.
    :type genre: str
    :param name: Name identifier of the status, cannot be null or empty.
    :type name: str
    """

    _attribute_map = {
        'genre': {'key': 'genre', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, genre=None, name=None):
        super(GitStatusContext, self).__init__()
        self.genre = genre
        self.name = name


class GitSuggestion(Model):
    """GitSuggestion.

    :param properties: Specific properties describing the suggestion.
    :type properties: dict
    :param type: The type of suggestion (e.g. pull request).
    :type type: str
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, properties=None, type=None):
        super(GitSuggestion, self).__init__()
        self.properties = properties
        self.type = type


class GitTemplate(Model):
    """GitTemplate.

    :param name: Name of the Template
    :type name: str
    :param type: Type of the Template
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, name=None, type=None):
        super(GitTemplate, self).__init__()
        self.name = name
        self.type = type


class GitTreeDiff(Model):
    """GitTreeDiff.

    :param base_tree_id: ObjectId of the base tree of this diff.
    :type base_tree_id: str
    :param diff_entries: List of tree entries that differ between the base and target tree.  Renames and object type changes are returned as a delete for the old object and add for the new object.  If a continuation token is returned in the response header, some tree entries are yet to be processed and may yeild more diff entries. If the continuation token is not returned all the diff entries have been included in this response.
    :type diff_entries: list of :class:`GitTreeDiffEntry <azure.devops.v5_1.git.models.GitTreeDiffEntry>`
    :param target_tree_id: ObjectId of the target tree of this diff.
    :type target_tree_id: str
    :param url: REST Url to this resource.
    :type url: str
    """

    _attribute_map = {
        'base_tree_id': {'key': 'baseTreeId', 'type': 'str'},
        'diff_entries': {'key': 'diffEntries', 'type': '[GitTreeDiffEntry]'},
        'target_tree_id': {'key': 'targetTreeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, base_tree_id=None, diff_entries=None, target_tree_id=None, url=None):
        super(GitTreeDiff, self).__init__()
        self.base_tree_id = base_tree_id
        self.diff_entries = diff_entries
        self.target_tree_id = target_tree_id
        self.url = url


class GitTreeDiffEntry(Model):
    """GitTreeDiffEntry.

    :param base_object_id: SHA1 hash of the object in the base tree, if it exists. Will be null in case of adds.
    :type base_object_id: str
    :param change_type: Type of change that affected this entry.
    :type change_type: object
    :param object_type: Object type of the tree entry. Blob, Tree or Commit("submodule")
    :type object_type: object
    :param path: Relative path in base and target trees.
    :type path: str
    :param target_object_id: SHA1 hash of the object in the target tree, if it exists. Will be null in case of deletes.
    :type target_object_id: str
    """

    _attribute_map = {
        'base_object_id': {'key': 'baseObjectId', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'object_type': {'key': 'objectType', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'target_object_id': {'key': 'targetObjectId', 'type': 'str'}
    }

    def __init__(self, base_object_id=None, change_type=None, object_type=None, path=None, target_object_id=None):
        super(GitTreeDiffEntry, self).__init__()
        self.base_object_id = base_object_id
        self.change_type = change_type
        self.object_type = object_type
        self.path = path
        self.target_object_id = target_object_id


class GitTreeDiffResponse(Model):
    """GitTreeDiffResponse.

    :param continuation_token: The HTTP client methods find the continuation token header in the response and populate this field.
    :type continuation_token: list of str
    :param tree_diff:
    :type tree_diff: :class:`GitTreeDiff <azure.devops.v5_1.git.models.GitTreeDiff>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'tree_diff': {'key': 'treeDiff', 'type': 'GitTreeDiff'}
    }

    def __init__(self, continuation_token=None, tree_diff=None):
        super(GitTreeDiffResponse, self).__init__()
        self.continuation_token = continuation_token
        self.tree_diff = tree_diff


class GitTreeEntryRef(Model):
    """GitTreeEntryRef.

    :param git_object_type: Blob or tree
    :type git_object_type: object
    :param mode: Mode represented as octal string
    :type mode: str
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param relative_path: Path relative to parent tree object
    :type relative_path: str
    :param size: Size of content
    :type size: long
    :param url: url to retrieve tree or blob
    :type url: str
    """

    _attribute_map = {
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'mode': {'key': 'mode', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, git_object_type=None, mode=None, object_id=None, relative_path=None, size=None, url=None):
        super(GitTreeEntryRef, self).__init__()
        self.git_object_type = git_object_type
        self.mode = mode
        self.object_id = object_id
        self.relative_path = relative_path
        self.size = size
        self.url = url


class GitTreeRef(Model):
    """GitTreeRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param size: Sum of sizes of all children
    :type size: long
    :param tree_entries: Blobs and trees under this tree
    :type tree_entries: list of :class:`GitTreeEntryRef <azure.devops.v5_1.git.models.GitTreeEntryRef>`
    :param url: Url to tree
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'tree_entries': {'key': 'treeEntries', 'type': '[GitTreeEntryRef]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, tree_entries=None, url=None):
        super(GitTreeRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.tree_entries = tree_entries
        self.url = url


class GitUserDate(Model):
    """GitUserDate.

    :param date: Date of the Git operation.
    :type date: datetime
    :param email: Email address of the user performing the Git operation.
    :type email: str
    :param image_url: Url for the user's avatar.
    :type image_url: str
    :param name: Name of the user performing the Git operation.
    :type name: str
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'email': {'key': 'email', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, date=None, email=None, image_url=None, name=None):
        super(GitUserDate, self).__init__()
        self.date = date
        self.email = email
        self.image_url = image_url
        self.name = name


class GitVersionDescriptor(Model):
    """GitVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None):
        super(GitVersionDescriptor, self).__init__()
        self.version = version
        self.version_options = version_options
        self.version_type = version_type


class GlobalGitRepositoryKey(Model):
    """GlobalGitRepositoryKey.

    :param collection_id: Team Project Collection ID of the collection for the repository.
    :type collection_id: str
    :param project_id: Team Project ID of the project for the repository.
    :type project_id: str
    :param repository_id: ID of the repository.
    :type repository_id: str
    """

    _attribute_map = {
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, collection_id=None, project_id=None, repository_id=None):
        super(GlobalGitRepositoryKey, self).__init__()
        self.collection_id = collection_id
        self.project_id = project_id
        self.repository_id = repository_id


class GraphSubjectBase(Model):
    """GraphSubjectBase.

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
    """IdentityRef.

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


class IdentityRefWithVote(IdentityRef):
    """IdentityRefWithVote.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
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
    :param is_required: Indicates if this is a required reviewer for this pull request. <br /> Branches can have policies that require particular reviewers are required for pull requests.
    :type is_required: bool
    :param reviewer_url: URL to retrieve information about this identity
    :type reviewer_url: str
    :param vote: Vote on a pull request:<br /> 10 - approved 5 - approved with suggestions 0 - no vote -5 - waiting for author -10 - rejected
    :type vote: int
    :param voted_for: Groups or teams that that this reviewer contributed to. <br /> Groups and teams can be reviewers on pull requests but can not vote directly.  When a member of the group or team votes, that vote is rolled up into the group or team vote.  VotedFor is a list of such votes.
    :type voted_for: list of :class:`IdentityRefWithVote <azure.devops.v5_1.git.models.IdentityRefWithVote>`
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
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'reviewer_url': {'key': 'reviewerUrl', 'type': 'str'},
        'vote': {'key': 'vote', 'type': 'int'},
        'voted_for': {'key': 'votedFor', 'type': '[IdentityRefWithVote]'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None, is_required=None, reviewer_url=None, vote=None, voted_for=None):
        super(IdentityRefWithVote, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, directory_alias=directory_alias, id=id, image_url=image_url, inactive=inactive, is_aad_identity=is_aad_identity, is_container=is_container, is_deleted_in_origin=is_deleted_in_origin, profile_url=profile_url, unique_name=unique_name)
        self.is_required = is_required
        self.reviewer_url = reviewer_url
        self.vote = vote
        self.voted_for = voted_for


class ImportRepositoryValidation(Model):
    """ImportRepositoryValidation.

    :param git_source:
    :type git_source: :class:`GitImportGitSource <azure.devops.v5_1.git.models.GitImportGitSource>`
    :param password:
    :type password: str
    :param tfvc_source:
    :type tfvc_source: :class:`GitImportTfvcSource <azure.devops.v5_1.git.models.GitImportTfvcSource>`
    :param username:
    :type username: str
    """

    _attribute_map = {
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'password': {'key': 'password', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'},
        'username': {'key': 'username', 'type': 'str'}
    }

    def __init__(self, git_source=None, password=None, tfvc_source=None, username=None):
        super(ImportRepositoryValidation, self).__init__()
        self.git_source = git_source
        self.password = password
        self.tfvc_source = tfvc_source
        self.username = username


class ItemContent(Model):
    """ItemContent.

    :param content:
    :type content: str
    :param content_type:
    :type content_type: object
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'object'}
    }

    def __init__(self, content=None, content_type=None):
        super(ItemContent, self).__init__()
        self.content = content
        self.content_type = content_type


class ItemModel(Model):
    """ItemModel.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param content:
    :type content: str
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <azure.devops.v5_1.git.models.FileContentMetadata>`
    :param is_folder:
    :type is_folder: bool
    :param is_sym_link:
    :type is_sym_link: bool
    :param path:
    :type path: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None):
        super(ItemModel, self).__init__()
        self._links = _links
        self.content = content
        self.content_metadata = content_metadata
        self.is_folder = is_folder
        self.is_sym_link = is_sym_link
        self.path = path
        self.url = url


class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation. In the case of an array, a zero based index can be used to specify the position in the array (e.g. /biscuits/0/name). The "-" character can be used instead of an index to insert at the end of the array (e.g. /biscuits/-).
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


class LineDiffBlock(Model):
    """LineDiffBlock.

    :param change_type: Type of change that was made to the block.
    :type change_type: object
    :param modified_line_number_start: Line number where this block starts in modified file.
    :type modified_line_number_start: int
    :param modified_lines_count: Count of lines in this block in modified file.
    :type modified_lines_count: int
    :param original_line_number_start: Line number where this block starts in original file.
    :type original_line_number_start: int
    :param original_lines_count: Count of lines in this block in original file.
    :type original_lines_count: int
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'modified_line_number_start': {'key': 'modifiedLineNumberStart', 'type': 'int'},
        'modified_lines_count': {'key': 'modifiedLinesCount', 'type': 'int'},
        'original_line_number_start': {'key': 'originalLineNumberStart', 'type': 'int'},
        'original_lines_count': {'key': 'originalLinesCount', 'type': 'int'}
    }

    def __init__(self, change_type=None, modified_line_number_start=None, modified_lines_count=None, original_line_number_start=None, original_lines_count=None):
        super(LineDiffBlock, self).__init__()
        self.change_type = change_type
        self.modified_line_number_start = modified_line_number_start
        self.modified_lines_count = modified_lines_count
        self.original_line_number_start = original_line_number_start
        self.original_lines_count = original_lines_count


class PolicyConfigurationRef(Model):
    """PolicyConfigurationRef.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.microsoft._team_foundation._policy._web_api.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, type=None, url=None):
        super(PolicyConfigurationRef, self).__init__()
        self.id = id
        self.type = type
        self.url = url


class PolicyTypeRef(Model):
    """PolicyTypeRef.

    :param display_name: Display name of the policy type.
    :type display_name: str
    :param id: The policy type ID.
    :type id: str
    :param url: The URL where the policy type can be retrieved.
    :type url: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None):
        super(PolicyTypeRef, self).__init__()
        self.display_name = display_name
        self.id = id
        self.url = url


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


class ResourceRef(Model):
    """ResourceRef.

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
        super(ResourceRef, self).__init__()
        self.id = id
        self.url = url


class ShareNotificationContext(Model):
    """ShareNotificationContext.

    :param message: Optional user note or message.
    :type message: str
    :param receivers: Identities of users who will receive a share notification.
    :type receivers: list of :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'receivers': {'key': 'receivers', 'type': '[IdentityRef]'}
    }

    def __init__(self, message=None, receivers=None):
        super(ShareNotificationContext, self).__init__()
        self.message = message
        self.receivers = receivers


class SourceToTargetRef(Model):
    """SourceToTargetRef.

    :param source_ref: The source ref to copy. For example, refs/heads/master.
    :type source_ref: str
    :param target_ref: The target ref to update. For example, refs/heads/master.
    :type target_ref: str
    """

    _attribute_map = {
        'source_ref': {'key': 'sourceRef', 'type': 'str'},
        'target_ref': {'key': 'targetRef', 'type': 'str'}
    }

    def __init__(self, source_ref=None, target_ref=None):
        super(SourceToTargetRef, self).__init__()
        self.source_ref = source_ref
        self.target_ref = target_ref


class TeamProjectCollectionReference(Model):
    """TeamProjectCollectionReference.

    :param id: Collection Id.
    :type id: str
    :param name: Collection Name.
    :type name: str
    :param url: Collection REST Url.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(TeamProjectCollectionReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class TeamProjectReference(Model):
    """TeamProjectReference.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class VersionedPolicyConfigurationRef(PolicyConfigurationRef):
    """VersionedPolicyConfigurationRef.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.microsoft._team_foundation._policy._web_api.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    :param revision: The policy configuration revision ID.
    :type revision: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None):
        super(VersionedPolicyConfigurationRef, self).__init__(id=id, type=type, url=url)
        self.revision = revision


class VstsInfo(Model):
    """VstsInfo.

    :param collection:
    :type collection: :class:`TeamProjectCollectionReference <azure.devops.v5_1.git.models.TeamProjectCollectionReference>`
    :param repository:
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    :param server_url:
    :type server_url: str
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'server_url': {'key': 'serverUrl', 'type': 'str'}
    }

    def __init__(self, collection=None, repository=None, server_url=None):
        super(VstsInfo, self).__init__()
        self.collection = collection
        self.repository = repository
        self.server_url = server_url


class WebApiCreateTagRequestData(Model):
    """WebApiCreateTagRequestData.

    :param name: Name of the tag definition that will be created.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(WebApiCreateTagRequestData, self).__init__()
        self.name = name


class WebApiTagDefinition(Model):
    """WebApiTagDefinition.

    :param active: Whether or not the tag definition is active.
    :type active: bool
    :param id: ID of the tag definition.
    :type id: str
    :param name: The name of the tag definition.
    :type name: str
    :param url: Resource URL for the Tag Definition.
    :type url: str
    """

    _attribute_map = {
        'active': {'key': 'active', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, active=None, id=None, name=None, url=None):
        super(WebApiTagDefinition, self).__init__()
        self.active = active
        self.id = id
        self.name = name
        self.url = url


class GitBaseVersionDescriptor(GitVersionDescriptor):
    """GitBaseVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    :param base_version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type base_version: str
    :param base_version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type base_version_options: object
    :param base_version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type base_version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'base_version': {'key': 'baseVersion', 'type': 'str'},
        'base_version_options': {'key': 'baseVersionOptions', 'type': 'object'},
        'base_version_type': {'key': 'baseVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, base_version=None, base_version_options=None, base_version_type=None):
        super(GitBaseVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.base_version = base_version
        self.base_version_options = base_version_options
        self.base_version_type = base_version_type


class GitCommit(GitCommitRef):
    """GitCommit.

    :param _links: A collection of related REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param author: Author of the commit.
    :type author: :class:`GitUserDate <azure.devops.v5_1.git.models.GitUserDate>`
    :param change_counts: Counts of the types of changes (edits, deletes, etc.) included with the commit.
    :type change_counts: dict
    :param changes: An enumeration of the changes included with the commit.
    :type changes: list of :class:`object <azure.devops.v5_1.git.models.object>`
    :param comment: Comment or message of the commit.
    :type comment: str
    :param comment_truncated: Indicates if the comment is truncated from the full Git commit comment message.
    :type comment_truncated: bool
    :param commit_id: ID (SHA-1) of the commit.
    :type commit_id: str
    :param committer: Committer of the commit.
    :type committer: :class:`GitUserDate <azure.devops.v5_1.git.models.GitUserDate>`
    :param parents: An enumeration of the parent commit IDs for this commit.
    :type parents: list of str
    :param push: The push associated with this commit.
    :type push: :class:`GitPushRef <azure.devops.v5_1.git.models.GitPushRef>`
    :param remote_url: Remote URL path to the commit.
    :type remote_url: str
    :param statuses: A list of status metadata from services and extensions that may associate additional information to the commit.
    :type statuses: list of :class:`GitStatus <azure.devops.v5_1.git.models.GitStatus>`
    :param url: REST URL for this resource.
    :type url: str
    :param work_items: A list of workitems associated with this commit.
    :type work_items: list of :class:`ResourceRef <azure.devops.v5_1.git.models.ResourceRef>`
    :param tree_id:
    :type tree_id: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'},
        'tree_id': {'key': 'treeId', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, push=None, remote_url=None, statuses=None, url=None, work_items=None, tree_id=None):
        super(GitCommit, self).__init__(_links=_links, author=author, change_counts=change_counts, changes=changes, comment=comment, comment_truncated=comment_truncated, commit_id=commit_id, committer=committer, parents=parents, push=push, remote_url=remote_url, statuses=statuses, url=url, work_items=work_items)
        self.tree_id = tree_id


class GitForkRef(GitRef):
    """GitForkRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param creator:
    :type creator: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param is_locked:
    :type is_locked: bool
    :param is_locked_by:
    :type is_locked_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param name:
    :type name: str
    :param object_id:
    :type object_id: str
    :param peeled_object_id:
    :type peeled_object_id: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <azure.devops.v5_1.git.models.GitStatus>`
    :param url:
    :type url: str
    :param repository: The repository ID of the fork.
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'creator': {'key': 'creator', 'type': 'IdentityRef'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, creator=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None, repository=None):
        super(GitForkRef, self).__init__(_links=_links, creator=creator, is_locked=is_locked, is_locked_by=is_locked_by, name=name, object_id=object_id, peeled_object_id=peeled_object_id, statuses=statuses, url=url)
        self.repository = repository


class GitItem(ItemModel):
    """GitItem.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param content:
    :type content: str
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <azure.devops.v5_1.git.models.FileContentMetadata>`
    :param is_folder:
    :type is_folder: bool
    :param is_sym_link:
    :type is_sym_link: bool
    :param path:
    :type path: str
    :param url:
    :type url: str
    :param commit_id: SHA1 of commit item was fetched at
    :type commit_id: str
    :param git_object_type: Type of object (Commit, Tree, Blob, Tag, ...)
    :type git_object_type: object
    :param latest_processed_change: Shallow ref to commit that last changed this item Only populated if latestProcessedChange is requested May not be accurate if latest change is not yet cached
    :type latest_processed_change: :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param object_id: Git object id
    :type object_id: str
    :param original_object_id: Git object id
    :type original_object_id: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'GitCommitRef'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'original_object_id': {'key': 'originalObjectId', 'type': 'str'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, commit_id=None, git_object_type=None, latest_processed_change=None, object_id=None, original_object_id=None):
        super(GitItem, self).__init__(_links=_links, content=content, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.commit_id = commit_id
        self.git_object_type = git_object_type
        self.latest_processed_change = latest_processed_change
        self.object_id = object_id
        self.original_object_id = original_object_id


class GitMerge(GitMergeParameters):
    """GitMerge.

    :param comment: Comment or message of the commit.
    :type comment: str
    :param parents: An enumeration of the parent commit IDs for the merge  commit.
    :type parents: list of str
    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param detailed_status: Detailed status of the merge operation.
    :type detailed_status: :class:`GitMergeOperationStatusDetail <azure.devops.v5_1.git.models.GitMergeOperationStatusDetail>`
    :param merge_operation_id: Unique identifier for the merge operation.
    :type merge_operation_id: int
    :param status: Status of the merge operation.
    :type status: object
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'parents': {'key': 'parents', 'type': '[str]'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitMergeOperationStatusDetail'},
        'merge_operation_id': {'key': 'mergeOperationId', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, parents=None, _links=None, detailed_status=None, merge_operation_id=None, status=None):
        super(GitMerge, self).__init__(comment=comment, parents=parents)
        self._links = _links
        self.detailed_status = detailed_status
        self.merge_operation_id = merge_operation_id
        self.status = status


class GitPullRequestStatus(GitStatus):
    """GitPullRequestStatus.

    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param context: Context of the status.
    :type context: :class:`GitStatusContext <azure.devops.v5_1.git.models.GitStatusContext>`
    :param created_by: Identity that created the status.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param creation_date: Creation date and time of the status.
    :type creation_date: datetime
    :param description: Status description. Typically describes current state of the status.
    :type description: str
    :param id: Status identifier.
    :type id: int
    :param state: State of the status.
    :type state: object
    :param target_url: URL with status details.
    :type target_url: str
    :param updated_date: Last update date and time of the status.
    :type updated_date: datetime
    :param iteration_id: ID of the iteration to associate status with. Minimum value is 1.
    :type iteration_id: int
    :param properties: Custom properties of the status.
    :type properties: :class:`object <azure.devops.v5_1.git.models.object>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None, iteration_id=None, properties=None):
        super(GitPullRequestStatus, self).__init__(_links=_links, context=context, created_by=created_by, creation_date=creation_date, description=description, id=id, state=state, target_url=target_url, updated_date=updated_date)
        self.iteration_id = iteration_id
        self.properties = properties


class GitPush(GitPushRef):
    """GitPush.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.git.models.ReferenceLinks>`
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: :class:`IdentityRef <azure.devops.v5_1.git.models.IdentityRef>`
    :param push_id:
    :type push_id: int
    :param url:
    :type url: str
    :param commits:
    :type commits: list of :class:`GitCommitRef <azure.devops.v5_1.git.models.GitCommitRef>`
    :param ref_updates:
    :type ref_updates: list of :class:`GitRefUpdate <azure.devops.v5_1.git.models.GitRefUpdate>`
    :param repository:
    :type repository: :class:`GitRepository <azure.devops.v5_1.git.models.GitRepository>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'ref_updates': {'key': 'refUpdates', 'type': '[GitRefUpdate]'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None, commits=None, ref_updates=None, repository=None):
        super(GitPush, self).__init__(_links=_links, date=date, push_correlation_id=push_correlation_id, pushed_by=pushed_by, push_id=push_id, url=url)
        self.commits = commits
        self.ref_updates = ref_updates
        self.repository = repository


class GitTargetVersionDescriptor(GitVersionDescriptor):
    """GitTargetVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    :param target_version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type target_version: str
    :param target_version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type target_version_options: object
    :param target_version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type target_version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'target_version': {'key': 'targetVersion', 'type': 'str'},
        'target_version_options': {'key': 'targetVersionOptions', 'type': 'object'},
        'target_version_type': {'key': 'targetVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, target_version=None, target_version_options=None, target_version_type=None):
        super(GitTargetVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.target_version = target_version
        self.target_version_options = target_version_options
        self.target_version_type = target_version_type


class PolicyConfiguration(VersionedPolicyConfigurationRef):
    """PolicyConfiguration.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.microsoft._team_foundation._policy._web_api.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    :param revision: The policy configuration revision ID.
    :type revision: int
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._team_foundation._policy._web_api.models.ReferenceLinks>`
    :param created_by: A reference to the identity that created the policy.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.microsoft._team_foundation._policy._web_api.models.IdentityRef>`
    :param created_date: The date and time when the policy was created.
    :type created_date: datetime
    :param is_blocking: Indicates whether the policy is blocking.
    :type is_blocking: bool
    :param is_deleted: Indicates whether the policy has been (soft) deleted.
    :type is_deleted: bool
    :param is_enabled: Indicates whether the policy is enabled.
    :type is_enabled: bool
    :param settings: The policy configuration settings.
    :type settings: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'is_blocking': {'key': 'isBlocking', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'settings': {'key': 'settings', 'type': 'object'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None, _links=None, created_by=None, created_date=None, is_blocking=None, is_deleted=None, is_enabled=None, settings=None):
        super(PolicyConfiguration, self).__init__(id=id, type=type, url=url, revision=revision)
        self._links = _links
        self.created_by = created_by
        self.created_date = created_date
        self.is_blocking = is_blocking
        self.is_deleted = is_deleted
        self.is_enabled = is_enabled
        self.settings = settings


__all__ = [
    'Attachment',
    'Change',
    'Comment',
    'CommentIterationContext',
    'CommentPosition',
    'CommentThread',
    'CommentThreadContext',
    'CommentTrackingCriteria',
    'FileContentMetadata',
    'FileDiff',
    'FileDiffParams',
    'FileDiffsCriteria',
    'GitAnnotatedTag',
    'GitAsyncRefOperation',
    'GitAsyncRefOperationDetail',
    'GitAsyncRefOperationParameters',
    'GitAsyncRefOperationSource',
    'GitBlobRef',
    'GitBranchStats',
    'GitCherryPick',
    'GitCommitChanges',
    'GitCommitDiffs',
    'GitCommitRef',
    'GitConflict',
    'GitConflictUpdateResult',
    'GitDeletedRepository',
    'GitFilePathsCollection',
    'GitForkOperationStatusDetail',
    'GitForkSyncRequest',
    'GitForkSyncRequestParameters',
    'GitImportGitSource',
    'GitImportRequest',
    'GitImportRequestParameters',
    'GitImportStatusDetail',
    'GitImportTfvcSource',
    'GitItemDescriptor',
    'GitItemRequestData',
    'GitMergeOperationStatusDetail',
    'GitMergeOriginRef',
    'GitMergeParameters',
    'GitObject',
    'GitPolicyConfigurationResponse',
    'GitPullRequest',
    'GitPullRequestChange',
    'GitPullRequestCommentThread',
    'GitPullRequestCommentThreadContext',
    'GitPullRequestCompletionOptions',
    'GitPullRequestIteration',
    'GitPullRequestIterationChanges',
    'GitPullRequestMergeOptions',
    'GitPullRequestQuery',
    'GitPullRequestQueryInput',
    'GitPullRequestSearchCriteria',
    'GitPushRef',
    'GitPushSearchCriteria',
    'GitQueryBranchStatsCriteria',
    'GitQueryCommitsCriteria',
    'GitRecycleBinRepositoryDetails',
    'GitRef',
    'GitRefFavorite',
    'GitRefUpdate',
    'GitRefUpdateResult',
    'GitRepository',
    'GitRepositoryCreateOptions',
    'GitRepositoryRef',
    'GitRepositoryStats',
    'GitRevert',
    'GitStatus',
    'GitStatusContext',
    'GitSuggestion',
    'GitTemplate',
    'GitTreeDiff',
    'GitTreeDiffEntry',
    'GitTreeDiffResponse',
    'GitTreeEntryRef',
    'GitTreeRef',
    'GitUserDate',
    'GitVersionDescriptor',
    'GlobalGitRepositoryKey',
    'GraphSubjectBase',
    'IdentityRef',
    'IdentityRefWithVote',
    'ImportRepositoryValidation',
    'ItemContent',
    'ItemModel',
    'JsonPatchOperation',
    'LineDiffBlock',
    'PolicyConfigurationRef',
    'PolicyTypeRef',
    'ReferenceLinks',
    'ResourceRef',
    'ShareNotificationContext',
    'SourceToTargetRef',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'VersionedPolicyConfigurationRef',
    'VstsInfo',
    'WebApiCreateTagRequestData',
    'WebApiTagDefinition',
    'GitBaseVersionDescriptor',
    'GitCommit',
    'GitForkRef',
    'GitItem',
    'GitMerge',
    'GitPullRequestStatus',
    'GitPush',
    'GitTargetVersionDescriptor',
    'PolicyConfiguration',
]
