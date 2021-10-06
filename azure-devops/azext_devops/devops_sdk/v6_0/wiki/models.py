# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CommentCreateParameters(Model):
    """
    Represents a request to create a work item comment.

    :param parent_id: Optional CommentId of the parent in order to add a reply for an existing comment
    :type parent_id: int
    :param text:
    :type text: str
    """

    _attribute_map = {
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, parent_id=None, text=None):
        super(CommentCreateParameters, self).__init__()
        self.parent_id = parent_id
        self.text = text


class CommentResourceReference(Model):
    """
    Base class for comment resource references

    :param url:
    :type url: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, url=None):
        super(CommentResourceReference, self).__init__()
        self.url = url


class CommentUpdateParameters(Model):
    """
    Represents a request to update a comment.

    :param state: Set the current state of the comment
    :type state: object
    :param text: The updated text of the comment
    :type text: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'}
    }

    def __init__(self, state=None, text=None):
        super(CommentUpdateParameters, self).__init__()
        self.state = state
        self.text = text


class GitRepository(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._team_foundation._source_control._web_api.models.ReferenceLinks>`
    :param default_branch:
    :type default_branch: str
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <azure.devops.v6_0.microsoft._team_foundation._source_control._web_api.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v6_0.microsoft._team_foundation._source_control._web_api.models.TeamProjectReference>`
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
    :param web_url:
    :type web_url: str
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
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, size=None, ssh_url=None, url=None, valid_remote_urls=None, web_url=None):
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
        self.web_url = web_url


class GitRepositoryRef(Model):
    """
    :param collection: Team Project Collection where this Fork resides
    :type collection: :class:`TeamProjectCollectionReference <azure.devops.v6_0.microsoft._team_foundation._source_control._web_api.models.TeamProjectCollectionReference>`
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <azure.devops.v6_0.microsoft._team_foundation._source_control._web_api.models.TeamProjectReference>`
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


class GitVersionDescriptor(Model):
    """
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


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class TeamProjectCollectionReference(Model):
    """
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param url:
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
    """
    :param abbreviation:
    :type abbreviation: str
    :param default_team_image_url:
    :type default_team_image_url: str
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param last_update_time:
    :type last_update_time: datetime
    :param name:
    :type name: str
    :param revision:
    :type revision: long
    :param state:
    :type state: object
    :param url:
    :type url: str
    :param visibility:
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


class WikiAttachment(Model):
    """
    Defines properties for wiki attachment file.

    :param name: Name of the wiki attachment file.
    :type name: str
    :param path: Path of the wiki attachment file.
    :type path: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, name=None, path=None):
        super(WikiAttachment, self).__init__()
        self.name = name
        self.path = path


class WikiAttachmentResponse(Model):
    """
    Response contract for the Wiki Attachments API

    :param attachment: Defines properties for wiki attachment file.
    :type attachment: :class:`WikiAttachment <azure.devops.v6_0.wiki.models.WikiAttachment>`
    :param eTag: Contains the list of ETag values from the response header of the attachments API call. The first item in the list contains the version of the wiki attachment.
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


class WikiCreateBaseParameters(Model):
    """
    Base wiki creation parameters.

    :param mapped_path: Folder path inside repository which is shown as Wiki. Not required for ProjectWiki type.
    :type mapped_path: str
    :param name: Wiki name.
    :type name: str
    :param project_id: ID of the project in which the wiki is to be created.
    :type project_id: str
    :param repository_id: ID of the git repository that backs up the wiki. Not required for ProjectWiki type.
    :type repository_id: str
    :param type: Type of the wiki.
    :type type: object
    """

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None):
        super(WikiCreateBaseParameters, self).__init__()
        self.mapped_path = mapped_path
        self.name = name
        self.project_id = project_id
        self.repository_id = repository_id
        self.type = type


class WikiCreateParametersV2(WikiCreateBaseParameters):
    """
    Wiki creation parameters.

    :param mapped_path: Folder path inside repository which is shown as Wiki. Not required for ProjectWiki type.
    :type mapped_path: str
    :param name: Wiki name.
    :type name: str
    :param project_id: ID of the project in which the wiki is to be created.
    :type project_id: str
    :param repository_id: ID of the git repository that backs up the wiki. Not required for ProjectWiki type.
    :type repository_id: str
    :param type: Type of the wiki.
    :type type: object
    :param version: Version of the wiki. Not required for ProjectWiki type.
    :type version: :class:`GitVersionDescriptor <azure.devops.v6_0.wiki.models.GitVersionDescriptor>`
    """

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'version': {'key': 'version', 'type': 'GitVersionDescriptor'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None, version=None):
        super(WikiCreateParametersV2, self).__init__(mapped_path=mapped_path, name=name, project_id=project_id, repository_id=repository_id, type=type)
        self.version = version


class WikiPageCreateOrUpdateParameters(Model):
    """
    Contract encapsulating parameters for the page create or update operations.

    :param content: Content of the wiki page.
    :type content: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'}
    }

    def __init__(self, content=None):
        super(WikiPageCreateOrUpdateParameters, self).__init__()
        self.content = content


class WikiPageDetail(Model):
    """
    Defines a page with its metedata in a wiki.

    :param id: When present, permanent identifier for the wiki page
    :type id: int
    :param path: Path of the wiki page.
    :type path: str
    :param view_stats: Path of the wiki page.
    :type view_stats: list of :class:`WikiPageStat <azure.devops.v6_0.wiki.models.WikiPageStat>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'view_stats': {'key': 'viewStats', 'type': '[WikiPageStat]'}
    }

    def __init__(self, id=None, path=None, view_stats=None):
        super(WikiPageDetail, self).__init__()
        self.id = id
        self.path = path
        self.view_stats = view_stats


class WikiPageMoveParameters(Model):
    """
    Contract encapsulating parameters for the page move operation.

    :param new_order: New order of the wiki page.
    :type new_order: int
    :param new_path: New path of the wiki page.
    :type new_path: str
    :param path: Current path of the wiki page.
    :type path: str
    """

    _attribute_map = {
        'new_order': {'key': 'newOrder', 'type': 'int'},
        'new_path': {'key': 'newPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, new_order=None, new_path=None, path=None):
        super(WikiPageMoveParameters, self).__init__()
        self.new_order = new_order
        self.new_path = new_path
        self.path = path


class WikiPageMoveResponse(Model):
    """
    Response contract for the Wiki Page Move API.

    :param eTag: Contains the list of ETag values from the response header of the page move API call. The first item in the list contains the version of the wiki page subject to page move.
    :type eTag: list of str
    :param page_move: Defines properties for wiki page move.
    :type page_move: :class:`WikiPageMove <azure.devops.v6_0.wiki.models.WikiPageMove>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'page_move': {'key': 'pageMove', 'type': 'WikiPageMove'}
    }

    def __init__(self, eTag=None, page_move=None):
        super(WikiPageMoveResponse, self).__init__()
        self.eTag = eTag
        self.page_move = page_move


class WikiPageResponse(Model):
    """
    Response contract for the Wiki Pages PUT, PATCH and DELETE APIs.

    :param eTag: Contains the list of ETag values from the response header of the pages API call. The first item in the list contains the version of the wiki page.
    :type eTag: list of str
    :param page: Defines properties for wiki page.
    :type page: :class:`WikiPage <azure.devops.v6_0.wiki.models.WikiPage>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'page': {'key': 'page', 'type': 'WikiPage'}
    }

    def __init__(self, eTag=None, page=None):
        super(WikiPageResponse, self).__init__()
        self.eTag = eTag
        self.page = page


class WikiPagesBatchRequest(Model):
    """
    Contract encapsulating parameters for the pages batch.

    :param continuation_token: If the list of page data returned is not complete, a continuation token to query next batch of pages is included in the response header as "x-ms-continuationtoken". Omit this parameter to get the first batch of Wiki Page Data.
    :type continuation_token: str
    :param page_views_for_days: last N days from the current day for which page views is to be returned. It's inclusive of current day.
    :type page_views_for_days: int
    :param top: Total count of pages on a wiki to return.
    :type top: int
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'page_views_for_days': {'key': 'pageViewsForDays', 'type': 'int'},
        'top': {'key': 'top', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, page_views_for_days=None, top=None):
        super(WikiPagesBatchRequest, self).__init__()
        self.continuation_token = continuation_token
        self.page_views_for_days = page_views_for_days
        self.top = top


class WikiPageStat(Model):
    """
    Defines properties for wiki page stat.

    :param count: the count of the stat for the Day
    :type count: int
    :param day: Day of the stat
    :type day: datetime
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'day': {'key': 'day', 'type': 'iso-8601'}
    }

    def __init__(self, count=None, day=None):
        super(WikiPageStat, self).__init__()
        self.count = count
        self.day = day


class WikiPageViewStats(Model):
    """
    Defines properties for wiki page view stats.

    :param count: Wiki page view count.
    :type count: int
    :param last_viewed_time: Wiki page last viewed time.
    :type last_viewed_time: datetime
    :param path: Wiki page path.
    :type path: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'last_viewed_time': {'key': 'lastViewedTime', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, count=None, last_viewed_time=None, path=None):
        super(WikiPageViewStats, self).__init__()
        self.count = count
        self.last_viewed_time = last_viewed_time
        self.path = path


class WikiUpdateParameters(Model):
    """
    Wiki update parameters.

    :param name: Name for wiki.
    :type name: str
    :param versions: Versions of the wiki.
    :type versions: list of :class:`GitVersionDescriptor <azure.devops.v6_0.wiki.models.GitVersionDescriptor>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, name=None, versions=None):
        super(WikiUpdateParameters, self).__init__()
        self.name = name
        self.versions = versions


class WikiV2(WikiCreateBaseParameters):
    """
    Defines a wiki resource.

    :param mapped_path: Folder path inside repository which is shown as Wiki. Not required for ProjectWiki type.
    :type mapped_path: str
    :param name: Wiki name.
    :type name: str
    :param project_id: ID of the project in which the wiki is to be created.
    :type project_id: str
    :param repository_id: ID of the git repository that backs up the wiki. Not required for ProjectWiki type.
    :type repository_id: str
    :param type: Type of the wiki.
    :type type: object
    :param id: ID of the wiki.
    :type id: str
    :param properties: Properties of the wiki.
    :type properties: dict
    :param remote_url: Remote web url to the wiki.
    :type remote_url: str
    :param url: REST url for this wiki.
    :type url: str
    :param versions: Versions of the wiki.
    :type versions: list of :class:`GitVersionDescriptor <azure.devops.v6_0.wiki.models.GitVersionDescriptor>`
    """

    _attribute_map = {
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, mapped_path=None, name=None, project_id=None, repository_id=None, type=None, id=None, properties=None, remote_url=None, url=None, versions=None):
        super(WikiV2, self).__init__(mapped_path=mapped_path, name=name, project_id=project_id, repository_id=repository_id, type=type)
        self.id = id
        self.properties = properties
        self.remote_url = remote_url
        self.url = url
        self.versions = versions


class Comment(CommentResourceReference):
    """
    Comment on an artifact like Work Item or Wiki, etc.

    :param url:
    :type url: str
    :param artifact_id: The id of the artifact this comment belongs to
    :type artifact_id: str
    :param created_by: IdentityRef of the creator of the comment.
    :type created_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.IdentityRef>`
    :param created_date: The creation date of the comment.
    :type created_date: datetime
    :param id: The id assigned to the comment.
    :type id: int
    :param is_deleted: Indicates if the comment has been deleted.
    :type is_deleted: bool
    :param mentions: The mentions of the comment.
    :type mentions: list of :class:`CommentMention <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.CommentMention>`
    :param modified_by: IdentityRef of the user who last modified the comment.
    :type modified_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.IdentityRef>`
    :param modified_date: The last modification date of the comment.
    :type modified_date: datetime
    :param parent_id: The comment id of the parent comment, if any
    :type parent_id: int
    :param reactions: The reactions on the comment.
    :type reactions: list of :class:`CommentReaction <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.CommentReaction>`
    :param rendered_text: The rendered text of the comment
    :type rendered_text: str
    :param replies: Replies for this comment
    :type replies: :class:`CommentList <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.CommentList>`
    :param state: Indicates the current state of the comment
    :type state: object
    :param text: The plaintext/markdown version of the comment
    :type text: str
    :param version: The current version of the comment
    :type version: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'mentions': {'key': 'mentions', 'type': '[CommentMention]'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'reactions': {'key': 'reactions', 'type': '[CommentReaction]'},
        'rendered_text': {'key': 'renderedText', 'type': 'str'},
        'replies': {'key': 'replies', 'type': 'CommentList'},
        'state': {'key': 'state', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, url=None, artifact_id=None, created_by=None, created_date=None, id=None, is_deleted=None, mentions=None, modified_by=None, modified_date=None, parent_id=None, reactions=None, rendered_text=None, replies=None, state=None, text=None, version=None):
        super(Comment, self).__init__(url=url)
        self.artifact_id = artifact_id
        self.created_by = created_by
        self.created_date = created_date
        self.id = id
        self.is_deleted = is_deleted
        self.mentions = mentions
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.parent_id = parent_id
        self.reactions = reactions
        self.rendered_text = rendered_text
        self.replies = replies
        self.state = state
        self.text = text
        self.version = version


class CommentAttachment(CommentResourceReference):
    """
    Represents an attachment to a comment.

    :param url:
    :type url: str
    :param created_by: IdentityRef of the creator of the attachment.
    :type created_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.IdentityRef>`
    :param created_date: The creation date of the attachment.
    :type created_date: datetime
    :param id: Unique Id of the attachment.
    :type id: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, url=None, created_by=None, created_date=None, id=None):
        super(CommentAttachment, self).__init__(url=url)
        self.created_by = created_by
        self.created_date = created_date
        self.id = id


class CommentList(CommentResourceReference):
    """
    Represents a list of comments.

    :param url:
    :type url: str
    :param comments: List of comments in the current batch.
    :type comments: list of :class:`Comment <azure.devops.v6_0.microsoft._azure._dev_ops._comments._web_api.models.Comment>`
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
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'next_page': {'key': 'nextPage', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, url=None, comments=None, continuation_token=None, count=None, next_page=None, total_count=None):
        super(CommentList, self).__init__(url=url)
        self.comments = comments
        self.continuation_token = continuation_token
        self.count = count
        self.next_page = next_page
        self.total_count = total_count


class CommentMention(CommentResourceReference):
    """
    Contains information about various artifacts mentioned in the comment

    :param url:
    :type url: str
    :param artifact_id: Id of the artifact this mention belongs to
    :type artifact_id: str
    :param comment_id: Id of the comment associated with this mention. Nullable to support legacy mentions which can potentially have null commentId
    :type comment_id: int
    :param mentioned_artifact: Value of the mentioned artifact. Expected Value varies by CommentMentionType: Person:         VSID associated with the identity Work Item:      ID of the work item Pull Request:   ID of the Pull Request
    :type mentioned_artifact: str
    :param type: The context which represent where this mentioned was parsed from
    :type type: object
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'mentioned_artifact': {'key': 'mentionedArtifact', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, artifact_id=None, comment_id=None, mentioned_artifact=None, type=None):
        super(CommentMention, self).__init__(url=url)
        self.artifact_id = artifact_id
        self.comment_id = comment_id
        self.mentioned_artifact = mentioned_artifact
        self.type = type


class CommentReaction(CommentResourceReference):
    """
    Contains information about comment reaction for a particular reaction type.

    :param url:
    :type url: str
    :param comment_id: The id of the comment this reaction belongs to.
    :type comment_id: int
    :param count: Total number of reactions for the CommentReactionType.
    :type count: int
    :param is_current_user_engaged: Flag to indicate if the current user has engaged on this particular EngagementType (e.g. if they liked the associated comment).
    :type is_current_user_engaged: bool
    :param type: Type of the reaction.
    :type type: object
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'comment_id': {'key': 'commentId', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'is_current_user_engaged': {'key': 'isCurrentUserEngaged', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, url=None, comment_id=None, count=None, is_current_user_engaged=None, type=None):
        super(CommentReaction, self).__init__(url=url)
        self.comment_id = comment_id
        self.count = count
        self.is_current_user_engaged = is_current_user_engaged
        self.type = type


class WikiPage(WikiPageCreateOrUpdateParameters):
    """
    Defines a page in a wiki.

    :param content: Content of the wiki page.
    :type content: str
    :param git_item_path: Path of the git item corresponding to the wiki page stored in the backing Git repository.
    :type git_item_path: str
    :param id: When present, permanent identifier for the wiki page
    :type id: int
    :param is_non_conformant: True if a page is non-conforming, i.e. 1) if the name doesn't match page naming standards. 2) if the page does not have a valid entry in the appropriate order file.
    :type is_non_conformant: bool
    :param is_parent_page: True if this page has subpages under its path.
    :type is_parent_page: bool
    :param order: Order of the wiki page, relative to other pages in the same hierarchy level.
    :type order: int
    :param path: Path of the wiki page.
    :type path: str
    :param remote_url: Remote web url to the wiki page.
    :type remote_url: str
    :param sub_pages: List of subpages of the current page.
    :type sub_pages: list of :class:`WikiPage <azure.devops.v6_0.wiki.models.WikiPage>`
    :param url: REST url for this wiki page.
    :type url: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'git_item_path': {'key': 'gitItemPath', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_non_conformant': {'key': 'isNonConformant', 'type': 'bool'},
        'is_parent_page': {'key': 'isParentPage', 'type': 'bool'},
        'order': {'key': 'order', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'sub_pages': {'key': 'subPages', 'type': '[WikiPage]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, content=None, git_item_path=None, id=None, is_non_conformant=None, is_parent_page=None, order=None, path=None, remote_url=None, sub_pages=None, url=None):
        super(WikiPage, self).__init__(content=content)
        self.git_item_path = git_item_path
        self.id = id
        self.is_non_conformant = is_non_conformant
        self.is_parent_page = is_parent_page
        self.order = order
        self.path = path
        self.remote_url = remote_url
        self.sub_pages = sub_pages
        self.url = url


class WikiPageMove(WikiPageMoveParameters):
    """
    Request contract for Wiki Page Move.

    :param new_order: New order of the wiki page.
    :type new_order: int
    :param new_path: New path of the wiki page.
    :type new_path: str
    :param path: Current path of the wiki page.
    :type path: str
    :param page: Resultant page of this page move operation.
    :type page: :class:`WikiPage <azure.devops.v6_0.wiki.models.WikiPage>`
    """

    _attribute_map = {
        'new_order': {'key': 'newOrder', 'type': 'int'},
        'new_path': {'key': 'newPath', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'page': {'key': 'page', 'type': 'WikiPage'}
    }

    def __init__(self, new_order=None, new_path=None, path=None, page=None):
        super(WikiPageMove, self).__init__(new_order=new_order, new_path=new_path, path=path)
        self.page = page


__all__ = [
    'CommentCreateParameters',
    'CommentResourceReference',
    'CommentUpdateParameters',
    'GitRepository',
    'GitRepositoryRef',
    'GitVersionDescriptor',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'WikiAttachment',
    'WikiAttachmentResponse',
    'WikiCreateBaseParameters',
    'WikiCreateParametersV2',
    'WikiPageCreateOrUpdateParameters',
    'WikiPageDetail',
    'WikiPageMoveParameters',
    'WikiPageMoveResponse',
    'WikiPageResponse',
    'WikiPagesBatchRequest',
    'WikiPageStat',
    'WikiPageViewStats',
    'WikiUpdateParameters',
    'WikiV2',
    'Comment',
    'CommentAttachment',
    'CommentList',
    'CommentMention',
    'CommentReaction',
    'WikiPage',
    'WikiPageMove',
]
