# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AssociatedWorkItem(Model):
    """AssociatedWorkItem.

    :param assigned_to:
    :type assigned_to: str
    :param id: Id of associated the work item.
    :type id: int
    :param state:
    :type state: str
    :param title:
    :type title: str
    :param url: REST Url of the work item.
    :type url: str
    :param web_url:
    :type web_url: str
    :param work_item_type:
    :type work_item_type: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, state=None, title=None, url=None, web_url=None, work_item_type=None):
        super(AssociatedWorkItem, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.state = state
        self.title = title
        self.url = url
        self.web_url = web_url
        self.work_item_type = work_item_type


class Change(Model):
    """Change.

    :param change_type: The type of change that was made to the item.
    :type change_type: object
    :param item: Current version.
    :type item: object
    :param new_content: Content of the item after the change.
    :type new_content: :class:`ItemContent <azure.devops.v5_0.tfvc.models.ItemContent>`
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


class CheckinNote(Model):
    """CheckinNote.

    :param name:
    :type name: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(CheckinNote, self).__init__()
        self.name = name
        self.value = value


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


class GitRepository(Model):
    """GitRepository.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param default_branch:
    :type default_branch: str
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <azure.devops.v5_0.tfvc.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_0.tfvc.models.TeamProjectReference>`
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


class GitRepositoryRef(Model):
    """GitRepositoryRef.

    :param collection: Team Project Collection where this Fork resides
    :type collection: :class:`TeamProjectCollectionReference <azure.devops.v5_0.tfvc.models.TeamProjectCollectionReference>`
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_0.tfvc.models.TeamProjectReference>`
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


class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias:
    :type directory_alias: str
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
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
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
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param content:
    :type content: str
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <azure.devops.v5_0.tfvc.models.FileContentMetadata>`
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
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class TfvcBranchMapping(Model):
    """TfvcBranchMapping.

    :param depth: Depth of the branch.
    :type depth: str
    :param server_item: Server item for the branch.
    :type server_item: str
    :param type: Type of the branch.
    :type type: str
    """

    _attribute_map = {
        'depth': {'key': 'depth', 'type': 'str'},
        'server_item': {'key': 'serverItem', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, depth=None, server_item=None, type=None):
        super(TfvcBranchMapping, self).__init__()
        self.depth = depth
        self.server_item = server_item
        self.type = type


class TfvcChange(Change):
    """TfvcChange.

    :param merge_sources: List of merge sources in case of rename or branch creation.
    :type merge_sources: list of :class:`TfvcMergeSource <azure.devops.v5_0.tfvc.models.TfvcMergeSource>`
    :param pending_version: Version at which a (shelved) change was pended against
    :type pending_version: int
    """

    _attribute_map = {
        'merge_sources': {'key': 'mergeSources', 'type': '[TfvcMergeSource]'},
        'pending_version': {'key': 'pendingVersion', 'type': 'int'}
    }

    def __init__(self, merge_sources=None, pending_version=None):
        super(TfvcChange, self).__init__()
        self.merge_sources = merge_sources
        self.pending_version = pending_version


class TfvcChangesetRef(Model):
    """TfvcChangesetRef.

    :param _links: A collection of REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param author: Alias or display name of user
    :type author: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param changeset_id: Id of the changeset.
    :type changeset_id: int
    :param checked_in_by: Alias or display name of user
    :type checked_in_by: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param comment: Comment for the changeset.
    :type comment: str
    :param comment_truncated: Was the Comment result truncated?
    :type comment_truncated: bool
    :param created_date: Creation date of the changeset.
    :type created_date: datetime
    :param url: URL to retrieve the item.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'checked_in_by': {'key': 'checkedInBy', 'type': 'IdentityRef'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, changeset_id=None, checked_in_by=None, comment=None, comment_truncated=None, created_date=None, url=None):
        super(TfvcChangesetRef, self).__init__()
        self._links = _links
        self.author = author
        self.changeset_id = changeset_id
        self.checked_in_by = checked_in_by
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.created_date = created_date
        self.url = url


class TfvcChangesetSearchCriteria(Model):
    """TfvcChangesetSearchCriteria.

    :param author: Alias or display name of user who made the changes
    :type author: str
    :param follow_renames: Whether or not to follow renames for the given item being queried
    :type follow_renames: bool
    :param from_date: If provided, only include changesets created after this date (string) Think of a better name for this.
    :type from_date: str
    :param from_id: If provided, only include changesets after this changesetID
    :type from_id: int
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param item_path: Path of item to search under
    :type item_path: str
    :param mappings:
    :type mappings: list of :class:`TfvcMappingFilter <azure.devops.v5_0.tfvc.models.TfvcMappingFilter>`
    :param to_date: If provided, only include changesets created before this date (string) Think of a better name for this.
    :type to_date: str
    :param to_id: If provided, a version descriptor for the latest change list to include
    :type to_id: int
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'str'},
        'follow_renames': {'key': 'followRenames', 'type': 'bool'},
        'from_date': {'key': 'fromDate', 'type': 'str'},
        'from_id': {'key': 'fromId', 'type': 'int'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_path': {'key': 'itemPath', 'type': 'str'},
        'mappings': {'key': 'mappings', 'type': '[TfvcMappingFilter]'},
        'to_date': {'key': 'toDate', 'type': 'str'},
        'to_id': {'key': 'toId', 'type': 'int'}
    }

    def __init__(self, author=None, follow_renames=None, from_date=None, from_id=None, include_links=None, item_path=None, mappings=None, to_date=None, to_id=None):
        super(TfvcChangesetSearchCriteria, self).__init__()
        self.author = author
        self.follow_renames = follow_renames
        self.from_date = from_date
        self.from_id = from_id
        self.include_links = include_links
        self.item_path = item_path
        self.mappings = mappings
        self.to_date = to_date
        self.to_id = to_id


class TfvcChangesetsRequestData(Model):
    """TfvcChangesetsRequestData.

    :param changeset_ids: List of changeset Ids.
    :type changeset_ids: list of int
    :param comment_length: Length of the comment.
    :type comment_length: int
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    """

    _attribute_map = {
        'changeset_ids': {'key': 'changesetIds', 'type': '[int]'},
        'comment_length': {'key': 'commentLength', 'type': 'int'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'}
    }

    def __init__(self, changeset_ids=None, comment_length=None, include_links=None):
        super(TfvcChangesetsRequestData, self).__init__()
        self.changeset_ids = changeset_ids
        self.comment_length = comment_length
        self.include_links = include_links


class TfvcItem(ItemModel):
    """TfvcItem.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param content:
    :type content: str
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <azure.devops.v5_0.tfvc.models.FileContentMetadata>`
    :param is_folder:
    :type is_folder: bool
    :param is_sym_link:
    :type is_sym_link: bool
    :param path:
    :type path: str
    :param url:
    :type url: str
    :param change_date:
    :type change_date: datetime
    :param deletion_id:
    :type deletion_id: int
    :param encoding: File encoding from database, -1 represents binary.
    :type encoding: int
    :param hash_value: MD5 hash as a base 64 string, applies to files only.
    :type hash_value: str
    :param is_branch:
    :type is_branch: bool
    :param is_pending_change:
    :type is_pending_change: bool
    :param size: The size of the file, if applicable.
    :type size: long
    :param version:
    :type version: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content': {'key': 'content', 'type': 'str'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'change_date': {'key': 'changeDate', 'type': 'iso-8601'},
        'deletion_id': {'key': 'deletionId', 'type': 'int'},
        'encoding': {'key': 'encoding', 'type': 'int'},
        'hash_value': {'key': 'hashValue', 'type': 'str'},
        'is_branch': {'key': 'isBranch', 'type': 'bool'},
        'is_pending_change': {'key': 'isPendingChange', 'type': 'bool'},
        'size': {'key': 'size', 'type': 'long'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, _links=None, content=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, change_date=None, deletion_id=None, encoding=None, hash_value=None, is_branch=None, is_pending_change=None, size=None, version=None):
        super(TfvcItem, self).__init__(_links=_links, content=content, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.change_date = change_date
        self.deletion_id = deletion_id
        self.encoding = encoding
        self.hash_value = hash_value
        self.is_branch = is_branch
        self.is_pending_change = is_pending_change
        self.size = size
        self.version = version


class TfvcItemDescriptor(Model):
    """TfvcItemDescriptor.

    :param path:
    :type path: str
    :param recursion_level:
    :type recursion_level: object
    :param version:
    :type version: str
    :param version_option:
    :type version_option: object
    :param version_type:
    :type version_type: object
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'recursion_level': {'key': 'recursionLevel', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'version_option': {'key': 'versionOption', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, path=None, recursion_level=None, version=None, version_option=None, version_type=None):
        super(TfvcItemDescriptor, self).__init__()
        self.path = path
        self.recursion_level = recursion_level
        self.version = version
        self.version_option = version_option
        self.version_type = version_type


class TfvcItemRequestData(Model):
    """TfvcItemRequestData.

    :param include_content_metadata: If true, include metadata about the file type
    :type include_content_metadata: bool
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param item_descriptors:
    :type item_descriptors: list of :class:`TfvcItemDescriptor <azure.devops.v5_0.tfvc.models.TfvcItemDescriptor>`
    """

    _attribute_map = {
        'include_content_metadata': {'key': 'includeContentMetadata', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_descriptors': {'key': 'itemDescriptors', 'type': '[TfvcItemDescriptor]'}
    }

    def __init__(self, include_content_metadata=None, include_links=None, item_descriptors=None):
        super(TfvcItemRequestData, self).__init__()
        self.include_content_metadata = include_content_metadata
        self.include_links = include_links
        self.item_descriptors = item_descriptors


class TfvcLabelRef(Model):
    """TfvcLabelRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param id:
    :type id: int
    :param label_scope:
    :type label_scope: str
    :param modified_date:
    :type modified_date: datetime
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, description=None, id=None, label_scope=None, modified_date=None, name=None, owner=None, url=None):
        super(TfvcLabelRef, self).__init__()
        self._links = _links
        self.description = description
        self.id = id
        self.label_scope = label_scope
        self.modified_date = modified_date
        self.name = name
        self.owner = owner
        self.url = url


class TfvcLabelRequestData(Model):
    """TfvcLabelRequestData.

    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param item_label_filter:
    :type item_label_filter: str
    :param label_scope:
    :type label_scope: str
    :param max_item_count:
    :type max_item_count: int
    :param name:
    :type name: str
    :param owner:
    :type owner: str
    """

    _attribute_map = {
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_label_filter': {'key': 'itemLabelFilter', 'type': 'str'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'max_item_count': {'key': 'maxItemCount', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'}
    }

    def __init__(self, include_links=None, item_label_filter=None, label_scope=None, max_item_count=None, name=None, owner=None):
        super(TfvcLabelRequestData, self).__init__()
        self.include_links = include_links
        self.item_label_filter = item_label_filter
        self.label_scope = label_scope
        self.max_item_count = max_item_count
        self.name = name
        self.owner = owner


class TfvcMappingFilter(Model):
    """TfvcMappingFilter.

    :param exclude:
    :type exclude: bool
    :param server_path:
    :type server_path: str
    """

    _attribute_map = {
        'exclude': {'key': 'exclude', 'type': 'bool'},
        'server_path': {'key': 'serverPath', 'type': 'str'}
    }

    def __init__(self, exclude=None, server_path=None):
        super(TfvcMappingFilter, self).__init__()
        self.exclude = exclude
        self.server_path = server_path


class TfvcMergeSource(Model):
    """TfvcMergeSource.

    :param is_rename: Indicates if this a rename source. If false, it is a merge source.
    :type is_rename: bool
    :param server_item: The server item of the merge source
    :type server_item: str
    :param version_from: Start of the version range
    :type version_from: int
    :param version_to: End of the version range
    :type version_to: int
    """

    _attribute_map = {
        'is_rename': {'key': 'isRename', 'type': 'bool'},
        'server_item': {'key': 'serverItem', 'type': 'str'},
        'version_from': {'key': 'versionFrom', 'type': 'int'},
        'version_to': {'key': 'versionTo', 'type': 'int'}
    }

    def __init__(self, is_rename=None, server_item=None, version_from=None, version_to=None):
        super(TfvcMergeSource, self).__init__()
        self.is_rename = is_rename
        self.server_item = server_item
        self.version_from = version_from
        self.version_to = version_to


class TfvcPolicyFailureInfo(Model):
    """TfvcPolicyFailureInfo.

    :param message:
    :type message: str
    :param policy_name:
    :type policy_name: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'}
    }

    def __init__(self, message=None, policy_name=None):
        super(TfvcPolicyFailureInfo, self).__init__()
        self.message = message
        self.policy_name = policy_name


class TfvcPolicyOverrideInfo(Model):
    """TfvcPolicyOverrideInfo.

    :param comment:
    :type comment: str
    :param policy_failures:
    :type policy_failures: list of :class:`TfvcPolicyFailureInfo <azure.devops.v5_0.tfvc.models.TfvcPolicyFailureInfo>`
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'policy_failures': {'key': 'policyFailures', 'type': '[TfvcPolicyFailureInfo]'}
    }

    def __init__(self, comment=None, policy_failures=None):
        super(TfvcPolicyOverrideInfo, self).__init__()
        self.comment = comment
        self.policy_failures = policy_failures


class TfvcShallowBranchRef(Model):
    """TfvcShallowBranchRef.

    :param path: Path for the branch.
    :type path: str
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, path=None):
        super(TfvcShallowBranchRef, self).__init__()
        self.path = path


class TfvcShelvesetRef(Model):
    """TfvcShelvesetRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param comment:
    :type comment: str
    :param comment_truncated:
    :type comment_truncated: bool
    :param created_date:
    :type created_date: datetime
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, comment=None, comment_truncated=None, created_date=None, id=None, name=None, owner=None, url=None):
        super(TfvcShelvesetRef, self).__init__()
        self._links = _links
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.created_date = created_date
        self.id = id
        self.name = name
        self.owner = owner
        self.url = url


class TfvcShelvesetRequestData(Model):
    """TfvcShelvesetRequestData.

    :param include_details: Whether to include policyOverride and notes Only applies when requesting a single deep shelveset
    :type include_details: bool
    :param include_links: Whether to include the _links field on the shallow references. Does not apply when requesting a single deep shelveset object. Links will always be included in the deep shelveset.
    :type include_links: bool
    :param include_work_items: Whether to include workItems
    :type include_work_items: bool
    :param max_change_count: Max number of changes to include
    :type max_change_count: int
    :param max_comment_length: Max length of comment
    :type max_comment_length: int
    :param name: Shelveset's name
    :type name: str
    :param owner: Owner's ID. Could be a name or a guid.
    :type owner: str
    """

    _attribute_map = {
        'include_details': {'key': 'includeDetails', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_work_items': {'key': 'includeWorkItems', 'type': 'bool'},
        'max_change_count': {'key': 'maxChangeCount', 'type': 'int'},
        'max_comment_length': {'key': 'maxCommentLength', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'}
    }

    def __init__(self, include_details=None, include_links=None, include_work_items=None, max_change_count=None, max_comment_length=None, name=None, owner=None):
        super(TfvcShelvesetRequestData, self).__init__()
        self.include_details = include_details
        self.include_links = include_links
        self.include_work_items = include_work_items
        self.max_change_count = max_change_count
        self.max_comment_length = max_comment_length
        self.name = name
        self.owner = owner


class TfvcStatistics(Model):
    """TfvcStatistics.

    :param changeset_id: Id of the last changeset the stats are based on.
    :type changeset_id: int
    :param file_count_total: Count of files at the requested scope.
    :type file_count_total: long
    """

    _attribute_map = {
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'file_count_total': {'key': 'fileCountTotal', 'type': 'long'}
    }

    def __init__(self, changeset_id=None, file_count_total=None):
        super(TfvcStatistics, self).__init__()
        self.changeset_id = changeset_id
        self.file_count_total = file_count_total


class TfvcVersionDescriptor(Model):
    """TfvcVersionDescriptor.

    :param version:
    :type version: str
    :param version_option:
    :type version_option: object
    :param version_type:
    :type version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_option': {'key': 'versionOption', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_option=None, version_type=None):
        super(TfvcVersionDescriptor, self).__init__()
        self.version = version
        self.version_option = version_option
        self.version_type = version_type


class VersionControlProjectInfo(Model):
    """VersionControlProjectInfo.

    :param default_source_control_type:
    :type default_source_control_type: object
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v5_0.tfvc.models.TeamProjectReference>`
    :param supports_git:
    :type supports_git: bool
    :param supports_tFVC:
    :type supports_tFVC: bool
    """

    _attribute_map = {
        'default_source_control_type': {'key': 'defaultSourceControlType', 'type': 'object'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'supports_git': {'key': 'supportsGit', 'type': 'bool'},
        'supports_tFVC': {'key': 'supportsTFVC', 'type': 'bool'}
    }

    def __init__(self, default_source_control_type=None, project=None, supports_git=None, supports_tFVC=None):
        super(VersionControlProjectInfo, self).__init__()
        self.default_source_control_type = default_source_control_type
        self.project = project
        self.supports_git = supports_git
        self.supports_tFVC = supports_tFVC


class VstsInfo(Model):
    """VstsInfo.

    :param collection:
    :type collection: :class:`TeamProjectCollectionReference <azure.devops.v5_0.tfvc.models.TeamProjectCollectionReference>`
    :param repository:
    :type repository: :class:`GitRepository <azure.devops.v5_0.tfvc.models.GitRepository>`
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


class TfvcBranchRef(TfvcShallowBranchRef):
    """TfvcBranchRef.

    :param path: Path for the branch.
    :type path: str
    :param _links: A collection of REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param created_date: Creation date of the branch.
    :type created_date: datetime
    :param description: Description of the branch.
    :type description: str
    :param is_deleted: Is the branch deleted?
    :type is_deleted: bool
    :param owner: Alias or display name of user
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url: URL to retrieve the item.
    :type url: str
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, path=None, _links=None, created_date=None, description=None, is_deleted=None, owner=None, url=None):
        super(TfvcBranchRef, self).__init__(path=path)
        self._links = _links
        self.created_date = created_date
        self.description = description
        self.is_deleted = is_deleted
        self.owner = owner
        self.url = url


class TfvcChangeset(TfvcChangesetRef):
    """TfvcChangeset.

    :param _links: A collection of REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param author: Alias or display name of user
    :type author: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param changeset_id: Id of the changeset.
    :type changeset_id: int
    :param checked_in_by: Alias or display name of user
    :type checked_in_by: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param comment: Comment for the changeset.
    :type comment: str
    :param comment_truncated: Was the Comment result truncated?
    :type comment_truncated: bool
    :param created_date: Creation date of the changeset.
    :type created_date: datetime
    :param url: URL to retrieve the item.
    :type url: str
    :param account_id: Account Id of the changeset.
    :type account_id: str
    :param changes: List of associated changes.
    :type changes: list of :class:`TfvcChange <azure.devops.v5_0.tfvc.models.TfvcChange>`
    :param checkin_notes: Checkin Notes for the changeset.
    :type checkin_notes: list of :class:`CheckinNote <azure.devops.v5_0.tfvc.models.CheckinNote>`
    :param collection_id: Collection Id of the changeset.
    :type collection_id: str
    :param has_more_changes: Are more changes available.
    :type has_more_changes: bool
    :param policy_override: Policy Override for the changeset.
    :type policy_override: :class:`TfvcPolicyOverrideInfo <azure.devops.v5_0.tfvc.models.TfvcPolicyOverrideInfo>`
    :param team_project_ids: Team Project Ids for the changeset.
    :type team_project_ids: list of str
    :param work_items: List of work items associated with the changeset.
    :type work_items: list of :class:`AssociatedWorkItem <azure.devops.v5_0.tfvc.models.AssociatedWorkItem>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'changeset_id': {'key': 'changesetId', 'type': 'int'},
        'checked_in_by': {'key': 'checkedInBy', 'type': 'IdentityRef'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'changes': {'key': 'changes', 'type': '[TfvcChange]'},
        'checkin_notes': {'key': 'checkinNotes', 'type': '[CheckinNote]'},
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'has_more_changes': {'key': 'hasMoreChanges', 'type': 'bool'},
        'policy_override': {'key': 'policyOverride', 'type': 'TfvcPolicyOverrideInfo'},
        'team_project_ids': {'key': 'teamProjectIds', 'type': '[str]'},
        'work_items': {'key': 'workItems', 'type': '[AssociatedWorkItem]'}
    }

    def __init__(self, _links=None, author=None, changeset_id=None, checked_in_by=None, comment=None, comment_truncated=None, created_date=None, url=None, account_id=None, changes=None, checkin_notes=None, collection_id=None, has_more_changes=None, policy_override=None, team_project_ids=None, work_items=None):
        super(TfvcChangeset, self).__init__(_links=_links, author=author, changeset_id=changeset_id, checked_in_by=checked_in_by, comment=comment, comment_truncated=comment_truncated, created_date=created_date, url=url)
        self.account_id = account_id
        self.changes = changes
        self.checkin_notes = checkin_notes
        self.collection_id = collection_id
        self.has_more_changes = has_more_changes
        self.policy_override = policy_override
        self.team_project_ids = team_project_ids
        self.work_items = work_items


class TfvcLabel(TfvcLabelRef):
    """TfvcLabel.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param id:
    :type id: int
    :param label_scope:
    :type label_scope: str
    :param modified_date:
    :type modified_date: datetime
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url:
    :type url: str
    :param items:
    :type items: list of :class:`TfvcItem <azure.devops.v5_0.tfvc.models.TfvcItem>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'label_scope': {'key': 'labelScope', 'type': 'str'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'items': {'key': 'items', 'type': '[TfvcItem]'}
    }

    def __init__(self, _links=None, description=None, id=None, label_scope=None, modified_date=None, name=None, owner=None, url=None, items=None):
        super(TfvcLabel, self).__init__(_links=_links, description=description, id=id, label_scope=label_scope, modified_date=modified_date, name=name, owner=owner, url=url)
        self.items = items


class TfvcShelveset(TfvcShelvesetRef):
    """TfvcShelveset.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param comment:
    :type comment: str
    :param comment_truncated:
    :type comment_truncated: bool
    :param created_date:
    :type created_date: datetime
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url:
    :type url: str
    :param changes:
    :type changes: list of :class:`TfvcChange <azure.devops.v5_0.tfvc.models.TfvcChange>`
    :param notes:
    :type notes: list of :class:`CheckinNote <azure.devops.v5_0.tfvc.models.CheckinNote>`
    :param policy_override:
    :type policy_override: :class:`TfvcPolicyOverrideInfo <azure.devops.v5_0.tfvc.models.TfvcPolicyOverrideInfo>`
    :param work_items:
    :type work_items: list of :class:`AssociatedWorkItem <azure.devops.v5_0.tfvc.models.AssociatedWorkItem>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'changes': {'key': 'changes', 'type': '[TfvcChange]'},
        'notes': {'key': 'notes', 'type': '[CheckinNote]'},
        'policy_override': {'key': 'policyOverride', 'type': 'TfvcPolicyOverrideInfo'},
        'work_items': {'key': 'workItems', 'type': '[AssociatedWorkItem]'}
    }

    def __init__(self, _links=None, comment=None, comment_truncated=None, created_date=None, id=None, name=None, owner=None, url=None, changes=None, notes=None, policy_override=None, work_items=None):
        super(TfvcShelveset, self).__init__(_links=_links, comment=comment, comment_truncated=comment_truncated, created_date=created_date, id=id, name=name, owner=owner, url=url)
        self.changes = changes
        self.notes = notes
        self.policy_override = policy_override
        self.work_items = work_items


class TfvcBranch(TfvcBranchRef):
    """TfvcBranch.

    :param path: Path for the branch.
    :type path: str
    :param _links: A collection of REST reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.tfvc.models.ReferenceLinks>`
    :param created_date: Creation date of the branch.
    :type created_date: datetime
    :param description: Description of the branch.
    :type description: str
    :param is_deleted: Is the branch deleted?
    :type is_deleted: bool
    :param owner: Alias or display name of user
    :type owner: :class:`IdentityRef <azure.devops.v5_0.tfvc.models.IdentityRef>`
    :param url: URL to retrieve the item.
    :type url: str
    :param children: List of children for the branch.
    :type children: list of :class:`TfvcBranch <azure.devops.v5_0.tfvc.models.TfvcBranch>`
    :param mappings: List of branch mappings.
    :type mappings: list of :class:`TfvcBranchMapping <azure.devops.v5_0.tfvc.models.TfvcBranchMapping>`
    :param parent: Path of the branch's parent.
    :type parent: :class:`TfvcShallowBranchRef <azure.devops.v5_0.tfvc.models.TfvcShallowBranchRef>`
    :param related_branches: List of paths of the related branches.
    :type related_branches: list of :class:`TfvcShallowBranchRef <azure.devops.v5_0.tfvc.models.TfvcShallowBranchRef>`
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'children': {'key': 'children', 'type': '[TfvcBranch]'},
        'mappings': {'key': 'mappings', 'type': '[TfvcBranchMapping]'},
        'parent': {'key': 'parent', 'type': 'TfvcShallowBranchRef'},
        'related_branches': {'key': 'relatedBranches', 'type': '[TfvcShallowBranchRef]'}
    }

    def __init__(self, path=None, _links=None, created_date=None, description=None, is_deleted=None, owner=None, url=None, children=None, mappings=None, parent=None, related_branches=None):
        super(TfvcBranch, self).__init__(path=path, _links=_links, created_date=created_date, description=description, is_deleted=is_deleted, owner=owner, url=url)
        self.children = children
        self.mappings = mappings
        self.parent = parent
        self.related_branches = related_branches


__all__ = [
    'AssociatedWorkItem',
    'Change',
    'CheckinNote',
    'FileContentMetadata',
    'GitRepository',
    'GitRepositoryRef',
    'GraphSubjectBase',
    'IdentityRef',
    'ItemContent',
    'ItemModel',
    'ReferenceLinks',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'TfvcBranchMapping',
    'TfvcChange',
    'TfvcChangesetRef',
    'TfvcChangesetSearchCriteria',
    'TfvcChangesetsRequestData',
    'TfvcItem',
    'TfvcItemDescriptor',
    'TfvcItemRequestData',
    'TfvcLabelRef',
    'TfvcLabelRequestData',
    'TfvcMappingFilter',
    'TfvcMergeSource',
    'TfvcPolicyFailureInfo',
    'TfvcPolicyOverrideInfo',
    'TfvcShallowBranchRef',
    'TfvcShelvesetRef',
    'TfvcShelvesetRequestData',
    'TfvcStatistics',
    'TfvcVersionDescriptor',
    'VersionControlProjectInfo',
    'VstsInfo',
    'TfvcBranchRef',
    'TfvcChangeset',
    'TfvcLabel',
    'TfvcShelveset',
    'TfvcBranch',
]
