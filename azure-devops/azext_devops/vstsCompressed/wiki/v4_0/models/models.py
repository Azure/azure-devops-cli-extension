# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class Change(Model):
    """Change.

    :param change_type:
    :type change_type: object
    :param item:
    :type item: :class:`GitItem <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitItem>`
    :param new_content:
    :type new_content: :class:`ItemContent <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.ItemContent>`
    :param source_server_item:
    :type source_server_item: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'item': {'key': 'item', 'type': 'GitItem'},
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



class GitCommitRef(Model):
    """GitCommitRef.

    :param _links:
    :type _links: ReferenceLinks
    :param author:
    :type author: :class:`GitUserDate <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitUserDate>`
    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.object>`
    :param comment:
    :type comment: str
    :param comment_truncated:
    :type comment_truncated: bool
    :param commit_id:
    :type commit_id: str
    :param committer:
    :type committer: :class:`GitUserDate <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitUserDate>`
    :param parents:
    :type parents: list of str
    :param remote_url:
    :type remote_url: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitStatus>`
    :param url:
    :type url: str
    :param work_items:
    :type work_items: list of ResourceRef
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
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, remote_url=None, statuses=None, url=None, work_items=None):
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
        self.remote_url = remote_url
        self.statuses = statuses
        self.url = url
        self.work_items = work_items



class GitPushRef(Model):
    """GitPushRef.

    :param _links:
    :type _links: ReferenceLinks
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: IdentityRef
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



class GitRepository(Model):
    """GitRepository.

    :param _links:
    :type _links: ReferenceLinks
    :param default_branch:
    :type default_branch: str
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitRepositoryRef>`
    :param project:
    :type project: TeamProjectReference
    :param remote_url:
    :type remote_url: str
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
        'url': {'key': 'url', 'type': 'str'},
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, url=None, valid_remote_urls=None):
        super(GitRepository, self).__init__()
        self._links = _links
        self.default_branch = default_branch
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.parent_repository = parent_repository
        self.project = project
        self.remote_url = remote_url
        self.url = url
        self.valid_remote_urls = valid_remote_urls



class GitRepositoryRef(Model):
    """GitRepositoryRef.

    :param collection: Team Project Collection where this Fork resides
    :type collection: TeamProjectCollectionReference
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param project:
    :type project: TeamProjectReference
    :param remote_url:
    :type remote_url: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, collection=None, id=None, name=None, project=None, remote_url=None, url=None):
        super(GitRepositoryRef, self).__init__()
        self.collection = collection
        self.id = id
        self.name = name
        self.project = project
        self.remote_url = remote_url
        self.url = url



class GitStatus(Model):
    """GitStatus.

    :param _links: Reference links.
    :type _links: ReferenceLinks
    :param context: Context of the status.
    :type context: :class:`GitStatusContext <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitStatusContext>`
    :param created_by: Identity that created the status.
    :type created_by: IdentityRef
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



class GitUserDate(Model):
    """GitUserDate.

    :param date:
    :type date: datetime
    :param email:
    :type email: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'email': {'key': 'email', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, date=None, email=None, name=None):
        super(GitUserDate, self).__init__()
        self.date = date
        self.email = email
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
    :type _links: ReferenceLinks
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.FileContentMetadata>`
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
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None):
        super(ItemModel, self).__init__()
        self._links = _links
        self.content_metadata = content_metadata
        self.is_folder = is_folder
        self.is_sym_link = is_sym_link
        self.path = path
        self.url = url



class WikiAttachment(Model):
    """WikiAttachment.

    :param name: Name of the wiki attachment file.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(WikiAttachment, self).__init__()
        self.name = name



class WikiAttachmentResponse(Model):
    """WikiAttachmentResponse.

    :param attachment: Defines properties for wiki attachment file.
    :type attachment: :class:`WikiAttachment <wiki.v4_0.models.WikiAttachment>`
    :param eTag: Contains the list of ETag values from the response header of the attachments API call. The first item in the list contains the head commit of wiki repository after the corresponding attachments API call.
    :type eTag: list of str
    """

    _attribute_map = {
        'attachment': {'key': 'attachment', 'type': 'WikiAttachment'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, attachment=None, eTag=None):
        super(WikiAttachmentResponse, self).__init__()
        self.attachment = attachment
        self.eTag = eTag



class WikiChange(Model):
    """WikiChange.

    :param change_type: ChangeType associated with the item in this change.
    :type change_type: object
    :param content: New content of the item.
    :type content: str
    :param item: Item that is subject to this change.
    :type item: object
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'content': {'key': 'content', 'type': 'str'},
        'item': {'key': 'item', 'type': 'object'}
    }

    def __init__(self, change_type=None, content=None, item=None):
        super(WikiChange, self).__init__()
        self.change_type = change_type
        self.content = content
        self.item = item



class WikiPage(Model):
    """WikiPage.

    :param depth: The depth in terms of level in the hierarchy.
    :type depth: int
    :param git_item_path: The path of the item corresponding to the wiki page stored in the backing Git repository. This is populated only in the response of the wiki pages GET API.
    :type git_item_path: str
    :param is_non_conformant: Flag to denote if a page is non-conforming, i.e. 1) if the name doesn't match our norms. 2) if the page does not have a valid entry in the appropriate order file.
    :type is_non_conformant: bool
    :param is_parent_page: Returns true if this page has child pages under its path.
    :type is_parent_page: bool
    :param order: Order associated with the page with respect to other pages in the same hierarchy level.
    :type order: int
    :param path: Path of the wiki page.
    :type path: str
    """

    _attribute_map = {
        'depth': {'key': 'depth', 'type': 'int'},
        'git_item_path': {'key': 'gitItemPath', 'type': 'str'},
        'is_non_conformant': {'key': 'isNonConformant', 'type': 'bool'},
        'is_parent_page': {'key': 'isParentPage', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, depth=None, git_item_path=None, is_non_conformant=None, is_parent_page=None, order=None, path=None):
        super(WikiPage, self).__init__()
        self.depth = depth
        self.git_item_path = git_item_path
        self.is_non_conformant = is_non_conformant
        self.is_parent_page = is_parent_page
        self.order = order
        self.path = path



class WikiPageChange(WikiChange):
    """WikiPageChange.

    :param original_order: Original order of the page to be provided in case of reorder or rename.
    :type original_order: int
    :param original_path: Original path of the page to be provided in case of rename.
    :type original_path: str
    """

    _attribute_map = {
        'original_order': {'key': 'originalOrder', 'type': 'int'},
        'original_path': {'key': 'originalPath', 'type': 'str'}
    }

    def __init__(self, original_order=None, original_path=None):
        super(WikiPageChange, self).__init__()
        self.original_order = original_order
        self.original_path = original_path



class WikiRepository(Model):
    """WikiRepository.

    :param head_commit: The head commit associated with the git repository backing up the wiki.
    :type head_commit: str
    :param id: The ID of the wiki which is same as the ID of the Git repository that it is backed by.
    :type id: str
    :param repository: The git repository that backs up the wiki.
    :type repository: :class:`GitRepository <wiki.v4_0.models.GitRepository>`
    """

    _attribute_map = {
        'head_commit': {'key': 'headCommit', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, head_commit=None, id=None, repository=None):
        super(WikiRepository, self).__init__()
        self.head_commit = head_commit
        self.id = id
        self.repository = repository



class WikiUpdate(Model):
    """WikiUpdate.

    :param associated_git_push: Git push object associated with this wiki update object. This is populated only in the response of the wiki updates POST API.
    :type associated_git_push: :class:`GitPush <wiki.v4_0.models.GitPush>`
    :param attachment_changes: List of attachment change objects that is to be associated with this update.
    :type attachment_changes: list of :class:`WikiAttachmentChange <wiki.v4_0.models.WikiAttachmentChange>`
    :param comment: Comment to be associated with this update.
    :type comment: str
    :param head_commit: Headcommit of the of the repository.
    :type head_commit: str
    :param page_change: Page change object associated with this update.
    :type page_change: :class:`WikiPageChange <wiki.v4_0.models.WikiPageChange>`
    """

    _attribute_map = {
        'associated_git_push': {'key': 'associatedGitPush', 'type': 'GitPush'},
        'attachment_changes': {'key': 'attachmentChanges', 'type': '[WikiAttachmentChange]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'head_commit': {'key': 'headCommit', 'type': 'str'},
        'page_change': {'key': 'pageChange', 'type': 'WikiPageChange'}
    }

    def __init__(self, associated_git_push=None, attachment_changes=None, comment=None, head_commit=None, page_change=None):
        super(WikiUpdate, self).__init__()
        self.associated_git_push = associated_git_push
        self.attachment_changes = attachment_changes
        self.comment = comment
        self.head_commit = head_commit
        self.page_change = page_change



class GitItem(ItemModel):
    """GitItem.

    :param _links:
    :type _links: ReferenceLinks
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.FileContentMetadata>`
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
    :type latest_processed_change: :class:`GitCommitRef <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitCommitRef>`
    :param object_id: Git object id
    :type object_id: str
    :param original_object_id: Git object id
    :type original_object_id: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
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

    def __init__(self, _links=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, commit_id=None, git_object_type=None, latest_processed_change=None, object_id=None, original_object_id=None):
        super(GitItem, self).__init__(_links=_links, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.commit_id = commit_id
        self.git_object_type = git_object_type
        self.latest_processed_change = latest_processed_change
        self.object_id = object_id
        self.original_object_id = original_object_id



class GitPush(GitPushRef):
    """GitPush.

    :param _links:
    :type _links: ReferenceLinks
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: IdentityRef
    :param push_id:
    :type push_id: int
    :param url:
    :type url: str
    :param commits:
    :type commits: list of :class:`GitCommitRef <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitCommitRef>`
    :param ref_updates:
    :type ref_updates: list of :class:`GitRefUpdate <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitRefUpdate>`
    :param repository:
    :type repository: :class:`GitRepository <microsoft.-team-foundation.-source-control.-web-api.v4_0.models.GitRepository>`
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



class WikiAttachmentChange(WikiChange):
    """WikiAttachmentChange.

    :param overwrite_content_if_existing: Defines whether the content of an existing attachment is to be overwriten or not. If true, the content of the attachment is overwritten on an existing attachment. If attachment non-existing, new attachment is created. If false, exception is thrown if an attachment with same name exists.
    :type overwrite_content_if_existing: bool
    """

    _attribute_map = {
        'overwrite_content_if_existing': {'key': 'overwriteContentIfExisting', 'type': 'bool'}
    }

    def __init__(self, overwrite_content_if_existing=None):
        super(WikiAttachmentChange, self).__init__()
        self.overwrite_content_if_existing = overwrite_content_if_existing
