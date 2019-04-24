# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


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
    :type parent_repository: :class:`GitRepositoryRef <azure.devops.v5_1.microsoft._team_foundation._source_control._web_api.models.GitRepositoryRef>`
    :param project:
    :type project: TeamProjectReference
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
    """GitRepositoryRef.

    :param collection: Team Project Collection where this Fork resides
    :type collection: TeamProjectCollectionReference
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param project:
    :type project: TeamProjectReference
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


class WikiAttachment(Model):
    """WikiAttachment.

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
    """WikiAttachmentResponse.

    :param attachment: Defines properties for wiki attachment file.
    :type attachment: :class:`WikiAttachment <azure.devops.v5_1.wiki.models.WikiAttachment>`
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
    """WikiCreateBaseParameters.

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
    """WikiCreateParametersV2.

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
    :type version: :class:`GitVersionDescriptor <azure.devops.v5_1.wiki.models.GitVersionDescriptor>`
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
    """WikiPageCreateOrUpdateParameters.

    :param content: Content of the wiki page.
    :type content: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'}
    }

    def __init__(self, content=None):
        super(WikiPageCreateOrUpdateParameters, self).__init__()
        self.content = content


class WikiPageMoveParameters(Model):
    """WikiPageMoveParameters.

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
    """WikiPageMoveResponse.

    :param eTag: Contains the list of ETag values from the response header of the page move API call. The first item in the list contains the version of the wiki page subject to page move.
    :type eTag: list of str
    :param page_move: Defines properties for wiki page move.
    :type page_move: :class:`WikiPageMove <azure.devops.v5_1.wiki.models.WikiPageMove>`
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
    """WikiPageResponse.

    :param eTag: Contains the list of ETag values from the response header of the pages API call. The first item in the list contains the version of the wiki page.
    :type eTag: list of str
    :param page: Defines properties for wiki page.
    :type page: :class:`WikiPage <azure.devops.v5_1.wiki.models.WikiPage>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'page': {'key': 'page', 'type': 'WikiPage'}
    }

    def __init__(self, eTag=None, page=None):
        super(WikiPageResponse, self).__init__()
        self.eTag = eTag
        self.page = page


class WikiPageViewStats(Model):
    """WikiPageViewStats.

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
    """WikiUpdateParameters.

    :param name: Name for wiki.
    :type name: str
    :param versions: Versions of the wiki.
    :type versions: list of :class:`GitVersionDescriptor <azure.devops.v5_1.wiki.models.GitVersionDescriptor>`
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
    """WikiV2.

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
    :type versions: list of :class:`GitVersionDescriptor <azure.devops.v5_1.wiki.models.GitVersionDescriptor>`
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


class WikiPage(WikiPageCreateOrUpdateParameters):
    """WikiPage.

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
    :type sub_pages: list of :class:`WikiPage <azure.devops.v5_1.wiki.models.WikiPage>`
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
    """WikiPageMove.

    :param new_order: New order of the wiki page.
    :type new_order: int
    :param new_path: New path of the wiki page.
    :type new_path: str
    :param path: Current path of the wiki page.
    :type path: str
    :param page: Resultant page of this page move operation.
    :type page: :class:`WikiPage <azure.devops.v5_1.wiki.models.WikiPage>`
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
    'GitRepository',
    'GitRepositoryRef',
    'GitVersionDescriptor',
    'WikiAttachment',
    'WikiAttachmentResponse',
    'WikiCreateBaseParameters',
    'WikiCreateParametersV2',
    'WikiPageCreateOrUpdateParameters',
    'WikiPageMoveParameters',
    'WikiPageMoveResponse',
    'WikiPageResponse',
    'WikiPageViewStats',
    'WikiUpdateParameters',
    'WikiV2',
    'WikiPage',
    'WikiPageMove',
]
