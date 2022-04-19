# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BoardResult(Model):
    """
    Defines the Board result that matched a Board search request.

    :param boardtype: Board Type of the board document.
    :type boardtype: str
    :param collection: Collection details of the baord document.
    :type collection: :class:`Collection <azure.devops.v6_0.search.models.Collection>`
    :param project: Project details of the board document.
    :type project: :class:`Project <azure.devops.v6_0.search.models.Project>`
    :param team: Team details of the board document.
    :type team: :class:`Team <azure.devops.v6_0.search.models.Team>`
    """

    _attribute_map = {
        'boardtype': {'key': 'boardtype', 'type': 'str'},
        'collection': {'key': 'collection', 'type': 'Collection'},
        'project': {'key': 'project', 'type': 'Project'},
        'team': {'key': 'team', 'type': 'Team'}
    }

    def __init__(self, boardtype=None, collection=None, project=None, team=None):
        super(BoardResult, self).__init__()
        self.boardtype = boardtype
        self.collection = collection
        self.project = project
        self.team = team


class BranchInfo(Model):
    """
    Information about the configured branch.

    :param last_indexed_change_id: The commit Id of the last Git commit indexed in this branch
    :type last_indexed_change_id: str
    :param last_processed_time: The last time this branch was processed by the Search service
    :type last_processed_time: datetime
    :param name: Name of the indexed branch
    :type name: str
    """

    _attribute_map = {
        'last_indexed_change_id': {'key': 'lastIndexedChangeId', 'type': 'str'},
        'last_processed_time': {'key': 'lastProcessedTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, last_indexed_change_id=None, last_processed_time=None, name=None):
        super(BranchInfo, self).__init__()
        self.last_indexed_change_id = last_indexed_change_id
        self.last_processed_time = last_processed_time
        self.name = name


class CodeResult(Model):
    """
    Defines the code result containing information of the searched files and its metadata.

    :param collection: Collection of the result file.
    :type collection: :class:`Collection <azure.devops.v6_0.search.models.Collection>`
    :param content_id: ContentId of the result file.
    :type content_id: str
    :param file_name: Name of the result file.
    :type file_name: str
    :param matches: Dictionary of field to hit offsets in the result file. Key identifies the area in which hits were found, for ex: file content/file name etc.
    :type matches: dict
    :param path: Path at which result file is present.
    :type path: str
    :param project: Project of the result file.
    :type project: :class:`Project <azure.devops.v6_0.search.models.Project>`
    :param repository: Repository of the result file.
    :type repository: :class:`Repository <azure.devops.v6_0.search.models.Repository>`
    :param versions: Versions of the result file.
    :type versions: list of :class:`Version <azure.devops.v6_0.search.models.Version>`
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'Collection'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'matches': {'key': 'matches', 'type': '{[Hit]}'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'Project'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'versions': {'key': 'versions', 'type': '[Version]'}
    }

    def __init__(self, collection=None, content_id=None, file_name=None, matches=None, path=None, project=None, repository=None, versions=None):
        super(CodeResult, self).__init__()
        self.collection = collection
        self.content_id = content_id
        self.file_name = file_name
        self.matches = matches
        self.path = path
        self.project = project
        self.repository = repository
        self.versions = versions


class Collection(Model):
    """
    Defines the details of the collection.

    :param name: Name of the collection.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(Collection, self).__init__()
        self.name = name


class CustomRepositoryStatusResponse(Model):
    """
    Defines the custom repository status.

    :param id: Repository Id.
    :type id: str
    :param indexed_top_level_folders: List of indexed top level folders info.
    :type indexed_top_level_folders: list of :class:`DepotInfo <azure.devops.v6_0.search.models.DepotInfo>`
    :param name: Repository Name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'indexed_top_level_folders': {'key': 'indexedTopLevelFolders', 'type': '[DepotInfo]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, indexed_top_level_folders=None, name=None):
        super(CustomRepositoryStatusResponse, self).__init__()
        self.id = id
        self.indexed_top_level_folders = indexed_top_level_folders
        self.name = name


class DepotInfo(Model):
    """
    Information about the custom repository indexing freshness for configured branches and depots.

    :param indexed_branches: List of Indexed branches info.
    :type indexed_branches: list of :class:`BranchInfo <azure.devops.v6_0.search.models.BranchInfo>`
    :param name: Name of the indexed top level folder (depot).
    :type name: str
    """

    _attribute_map = {
        'indexed_branches': {'key': 'indexedBranches', 'type': '[BranchInfo]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, indexed_branches=None, name=None):
        super(DepotInfo, self).__init__()
        self.indexed_branches = indexed_branches
        self.name = name


class EntitySearchRequestBase(Model):
    """
    Base class for search request types.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'}
    }

    def __init__(self, filters=None, search_text=None):
        super(EntitySearchRequestBase, self).__init__()
        self.filters = filters
        self.search_text = search_text


class EntitySearchResponse(Model):
    """
    Defines the base contract for search response.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'}
    }

    def __init__(self, facets=None, info_code=None):
        super(EntitySearchResponse, self).__init__()
        self.facets = facets
        self.info_code = info_code


class FeedInfo(Model):
    """
    Defines the details of a feed.

    :param collection_id: Id of the collection.
    :type collection_id: str
    :param collection_name: Name of the collection.
    :type collection_name: str
    :param feed_id: Id of the feed.
    :type feed_id: str
    :param feed_name: Name of the feed.
    :type feed_name: str
    :param latest_matched_version: Latest matched version of package in this Feed.
    :type latest_matched_version: str
    :param latest_version: Latest version of package in this Feed.
    :type latest_version: str
    :param package_url: Url of package in this Feed.
    :type package_url: str
    :param views: List of views which contain the matched package.
    :type views: list of str
    """

    _attribute_map = {
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'collection_name': {'key': 'collectionName', 'type': 'str'},
        'feed_id': {'key': 'feedId', 'type': 'str'},
        'feed_name': {'key': 'feedName', 'type': 'str'},
        'latest_matched_version': {'key': 'latestMatchedVersion', 'type': 'str'},
        'latest_version': {'key': 'latestVersion', 'type': 'str'},
        'package_url': {'key': 'packageUrl', 'type': 'str'},
        'views': {'key': 'views', 'type': '[str]'}
    }

    def __init__(self, collection_id=None, collection_name=None, feed_id=None, feed_name=None, latest_matched_version=None, latest_version=None, package_url=None, views=None):
        super(FeedInfo, self).__init__()
        self.collection_id = collection_id
        self.collection_name = collection_name
        self.feed_id = feed_id
        self.feed_name = feed_name
        self.latest_matched_version = latest_matched_version
        self.latest_version = latest_version
        self.package_url = package_url
        self.views = views


class Filter(Model):
    """
    Describes a filter bucket item representing the total matches of search result, name and id.

    :param id: Id of the filter bucket.
    :type id: str
    :param name: Name of the filter bucket.
    :type name: str
    :param result_count: Count of matches in the filter bucket.
    :type result_count: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'result_count': {'key': 'resultCount', 'type': 'int'}
    }

    def __init__(self, id=None, name=None, result_count=None):
        super(Filter, self).__init__()
        self.id = id
        self.name = name
        self.result_count = result_count


class Hit(Model):
    """
    Describes the position of a piece of text in a document.

    :param char_offset: Gets or sets the start character offset of a piece of text.
    :type char_offset: int
    :param code_snippet: Gets or sets an extract of code where the match appears. Usually it is the line where there is the match.
    :type code_snippet: str
    :param column: Gets or sets the column number where the match appears in the line.
    :type column: int
    :param length: Gets or sets the length of a piece of text.
    :type length: int
    :param line: Gets or sets the line number where the match appears in the file.
    :type line: int
    :param type: Gets or sets the name of type of a piece of text.
    :type type: str
    """

    _attribute_map = {
        'char_offset': {'key': 'charOffset', 'type': 'int'},
        'code_snippet': {'key': 'codeSnippet', 'type': 'str'},
        'column': {'key': 'column', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
        'line': {'key': 'line', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, char_offset=None, code_snippet=None, column=None, length=None, line=None, type=None):
        super(Hit, self).__init__()
        self.char_offset = char_offset
        self.code_snippet = code_snippet
        self.column = column
        self.length = length
        self.line = line
        self.type = type


class PackageHit(Model):
    """
    Defines the matched terms in the field of the package result.

    :param field_reference_name: Reference name of the highlighted field.
    :type field_reference_name: str
    :param highlights: Matched/highlighted snippets of the field.
    :type highlights: list of str
    """

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(PackageHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class PackageResult(Model):
    """
    Defines the package result that matched a package search request.

    :param description: Description of the package.
    :type description: str
    :param feeds: List of feeds which contain the matching package.
    :type feeds: list of :class:`FeedInfo <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.FeedInfo>`
    :param hits: List of highlighted fields for the match.
    :type hits: list of :class:`PackageHit <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.PackageHit>`
    :param id: Id of the package.
    :type id: str
    :param name: Name of the package.
    :type name: str
    :param protocol_type: Type of the package.
    :type protocol_type: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'feeds': {'key': 'feeds', 'type': '[FeedInfo]'},
        'hits': {'key': 'hits', 'type': '[PackageHit]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'}
    }

    def __init__(self, description=None, feeds=None, hits=None, id=None, name=None, protocol_type=None):
        super(PackageResult, self).__init__()
        self.description = description
        self.feeds = feeds
        self.hits = hits
        self.id = id
        self.name = name
        self.protocol_type = protocol_type


class PackageSearchResponse(Model):
    """
    :param activity_id:
    :type activity_id: list of str
    :param content:
    :type content: :class:`PackageSearchResponseContent <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.PackageSearchResponseContent>`
    """

    _attribute_map = {
        'activity_id': {'key': 'activityId', 'type': '[str]'},
        'content': {'key': 'content', 'type': 'PackageSearchResponseContent'}
    }

    def __init__(self, activity_id=None, content=None):
        super(PackageSearchResponse, self).__init__()
        self.activity_id = activity_id
        self.content = content


class PackageSearchResponseContent(EntitySearchResponse):
    """
    Defines a response item that is returned for a package search request.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched packages.
    :type count: int
    :param results: List of matched packages.
    :type results: list of :class:`PackageResult <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.PackageResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[PackageResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(PackageSearchResponseContent, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class Project(Model):
    """
    Defines the details of the project.

    :param id: Id of the project.
    :type id: str
    :param name: Name of the project.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(Project, self).__init__()
        self.id = id
        self.name = name


class ProjectReference(Model):
    """
    Defines the details of the project.

    :param id: ID of the project.
    :type id: str
    :param name: Name of the project.
    :type name: str
    :param visibility: Visibility of the project.
    :type visibility: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, visibility=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name
        self.visibility = visibility


class Repository(Model):
    """
    Defines the details of the repository.

    :param id: Id of the repository.
    :type id: str
    :param name: Name of the repository.
    :type name: str
    :param type: Version control type of the result file.
    :type type: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(Repository, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class RepositoryStatusResponse(Model):
    """
    Defines the repository status.

    :param id: Repository Id.
    :type id: str
    :param indexed_branches: List of Indexed branches info.
    :type indexed_branches: list of :class:`BranchInfo <azure.devops.v6_0.search.models.BranchInfo>`
    :param name: Repository Name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'indexed_branches': {'key': 'indexedBranches', 'type': '[BranchInfo]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, indexed_branches=None, name=None):
        super(RepositoryStatusResponse, self).__init__()
        self.id = id
        self.indexed_branches = indexed_branches
        self.name = name


class ScrollSearchRequest(EntitySearchRequestBase):
    """
    Defines a scroll code search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param scroll_id: Scroll Id for scroll search query.
    :type scroll_id: str
    :param scroll_size: Size of data to return for scroll search query. Min value is 201.
    :type scroll_size: int
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'scroll_id': {'key': '$scrollId', 'type': 'str'},
        'scroll_size': {'key': '$scrollSize', 'type': 'int'}
    }

    def __init__(self, filters=None, search_text=None, scroll_id=None, scroll_size=None):
        super(ScrollSearchRequest, self).__init__(filters=filters, search_text=search_text)
        self.scroll_id = scroll_id
        self.scroll_size = scroll_size


class SettingResult(Model):
    """
    Defines the setting result that matched a setting search request

    :param description: Description of the settings page
    :type description: str
    :param icon: Icon name of the settings page
    :type icon: str
    :param route_id: Contribution url route id of the corresponding settings page
    :type route_id: str
    :param route_parameter_mapping: Contribution url route parameter of the corresponding settings page
    :type route_parameter_mapping: dict
    :param scope: Scope of the settings page, either organization, project or user
    :type scope: object
    :param title: Title of the settings page
    :type title: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'icon': {'key': 'icon', 'type': 'str'},
        'route_id': {'key': 'routeId', 'type': 'str'},
        'route_parameter_mapping': {'key': 'routeParameterMapping', 'type': '{str}'},
        'scope': {'key': 'scope', 'type': 'object'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, description=None, icon=None, route_id=None, route_parameter_mapping=None, scope=None, title=None):
        super(SettingResult, self).__init__()
        self.description = description
        self.icon = icon
        self.route_id = route_id
        self.route_parameter_mapping = route_parameter_mapping
        self.scope = scope
        self.title = title


class SettingSearchResponse(EntitySearchResponse):
    """
    Defines a setting search response item

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched setting documents.
    :type count: int
    :param results: List of top matched setting documents.
    :type results: list of :class:`SettingResult <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.SettingResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[SettingResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(SettingSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class SortOption(Model):
    """
    Defines how to sort the result.

    :param field: Field name on which sorting should be done.
    :type field: str
    :param sort_order: Order (ASC/DESC) in which the results should be sorted.
    :type sort_order: str
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'}
    }

    def __init__(self, field=None, sort_order=None):
        super(SortOption, self).__init__()
        self.field = field
        self.sort_order = sort_order


class Team(Model):
    """
    Defines the details of the team.

    :param id: Id of the team.
    :type id: str
    :param name: Name of the Team.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(Team, self).__init__()
        self.id = id
        self.name = name


class TfvcRepositoryStatusResponse(Model):
    """
    Defines the TFVC repository status.

    :param id: Repository Id.
    :type id: str
    :param indexing_information: List of Indexing Information for TFVC repository
    :type indexing_information: list of :class:`BranchInfo <azure.devops.v6_0.search.models.BranchInfo>`
    :param name: Repository Name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'indexing_information': {'key': 'indexingInformation', 'type': '[BranchInfo]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, indexing_information=None, name=None):
        super(TfvcRepositoryStatusResponse, self).__init__()
        self.id = id
        self.indexing_information = indexing_information
        self.name = name


class Version(Model):
    """
    Describes the details pertaining to a version of the result file.

    :param branch_name: Name of the branch.
    :type branch_name: str
    :param change_id: ChangeId in the given branch associated with this match.
    :type change_id: str
    """

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'change_id': {'key': 'changeId', 'type': 'str'}
    }

    def __init__(self, branch_name=None, change_id=None):
        super(Version, self).__init__()
        self.branch_name = branch_name
        self.change_id = change_id


class Wiki(Model):
    """
    Defines the details of wiki.

    :param id: Id of the wiki.
    :type id: str
    :param mapped_path: Mapped path for the wiki.
    :type mapped_path: str
    :param name: Name of the wiki.
    :type name: str
    :param version: Version for wiki.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'mapped_path': {'key': 'mappedPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, mapped_path=None, name=None, version=None):
        super(Wiki, self).__init__()
        self.id = id
        self.mapped_path = mapped_path
        self.name = name
        self.version = version


class WikiHit(Model):
    """
    Defines the matched terms in the field of the wiki result.

    :param field_reference_name: Reference name of the highlighted field.
    :type field_reference_name: str
    :param highlights: Matched/highlighted snippets of the field.
    :type highlights: list of str
    """

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(WikiHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class WikiResult(Model):
    """
    Defines the wiki result that matched a wiki search request.

    :param collection: Collection of the result file.
    :type collection: :class:`Collection <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.Collection>`
    :param content_id: ContentId of the result file.
    :type content_id: str
    :param file_name: Name of the result file.
    :type file_name: str
    :param hits: Highlighted snippets of fields that match the search request. The list is sorted by relevance of the snippets.
    :type hits: list of :class:`WikiHit <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.WikiHit>`
    :param path: Path at which result file is present.
    :type path: str
    :param project: Project details of the wiki document.
    :type project: :class:`ProjectReference <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.ProjectReference>`
    :param wiki: Wiki information for the result.
    :type wiki: :class:`Wiki <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.Wiki>`
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'Collection'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'hits': {'key': 'hits', 'type': '[WikiHit]'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'wiki': {'key': 'wiki', 'type': 'Wiki'}
    }

    def __init__(self, collection=None, content_id=None, file_name=None, hits=None, path=None, project=None, wiki=None):
        super(WikiResult, self).__init__()
        self.collection = collection
        self.content_id = content_id
        self.file_name = file_name
        self.hits = hits
        self.path = path
        self.project = project
        self.wiki = wiki


class WikiSearchResponse(EntitySearchResponse):
    """
    Defines a wiki search response item.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched wiki documents.
    :type count: int
    :param results: List of top matched wiki documents.
    :type results: list of :class:`WikiResult <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.WikiResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[WikiResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(WikiSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class WorkItemHit(Model):
    """
    Defines the matched terms in the field of the work item result.

    :param field_reference_name: Reference name of the highlighted field.
    :type field_reference_name: str
    :param highlights: Matched/highlighted snippets of the field.
    :type highlights: list of str
    """

    _attribute_map = {
        'field_reference_name': {'key': 'fieldReferenceName', 'type': 'str'},
        'highlights': {'key': 'highlights', 'type': '[str]'}
    }

    def __init__(self, field_reference_name=None, highlights=None):
        super(WorkItemHit, self).__init__()
        self.field_reference_name = field_reference_name
        self.highlights = highlights


class WorkItemResult(Model):
    """
    Defines the work item result that matched a work item search request.

    :param fields: A standard set of work item fields and their values.
    :type fields: dict
    :param hits: Highlighted snippets of fields that match the search request. The list is sorted by relevance of the snippets.
    :type hits: list of :class:`WorkItemHit <azure.devops.v6_0.search.models.WorkItemHit>`
    :param project: Project details of the work item.
    :type project: :class:`Project <azure.devops.v6_0.search.models.Project>`
    :param url: Reference to the work item.
    :type url: str
    """

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '{str}'},
        'hits': {'key': 'hits', 'type': '[WorkItemHit]'},
        'project': {'key': 'project', 'type': 'Project'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, fields=None, hits=None, project=None, url=None):
        super(WorkItemResult, self).__init__()
        self.fields = fields
        self.hits = hits
        self.project = project
        self.url = url


class WorkItemSearchResponse(EntitySearchResponse):
    """
    Defines a response item that is returned for a work item search request.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched work items.
    :type count: int
    :param results: List of top matched work items.
    :type results: list of :class:`WorkItemResult <azure.devops.v6_0.search.models.WorkItemResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[WorkItemResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(WorkItemSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class BoardSearchResponse(EntitySearchResponse):
    """
    Defines a Board search response item.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched Board documents.
    :type count: int
    :param results: List of top matched Board documents.
    :type results: list of :class:`BoardResult <azure.devops.v6_0.search.models.BoardResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[BoardResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(BoardSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class CodeSearchResponse(EntitySearchResponse):
    """
    Defines a code search response item.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched files.
    :type count: int
    :param results: List of matched files.
    :type results: list of :class:`CodeResult <azure.devops.v6_0.search.models.CodeResult>`
    """

    _attribute_map = {
        'facets': {'key': 'facets', 'type': '{[Filter]}'},
        'info_code': {'key': 'infoCode', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'results': {'key': 'results', 'type': '[CodeResult]'}
    }

    def __init__(self, facets=None, info_code=None, count=None, results=None):
        super(CodeSearchResponse, self).__init__(facets=facets, info_code=info_code)
        self.count = count
        self.results = results


class EntitySearchRequest(EntitySearchRequestBase):
    """
    Base contract for search request types without scroll support.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'}
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(EntitySearchRequest, self).__init__(filters=filters, search_text=search_text)
        self.order_by = order_by
        self.skip = skip
        self.top = top
        self.include_facets = include_facets


class PackageSearchRequest(EntitySearchRequest):
    """
    Defines a package search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(PackageSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class SettingSearchRequest(EntitySearchRequest):
    """
    Defines a setting search request

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(SettingSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class WikiSearchRequest(EntitySearchRequest):
    """
    Defines a wiki search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(WikiSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class WorkItemSearchRequest(EntitySearchRequest):
    """
    Defines a work item search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.search.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(WorkItemSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class BoardSearchRequest(EntitySearchRequest):
    """
    Defines a Board search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.search.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None):
        super(BoardSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


class CodeSearchRequest(EntitySearchRequest):
    """
    Defines a code search request.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v6_0.search.models.SortOption>`
    :param skip: Number of results to be skipped.
    :type skip: int
    :param top: Number of results to be returned.
    :type top: int
    :param include_facets: Flag to opt for faceting in the result. Default behavior is false.
    :type include_facets: bool
    :param include_snippet: Flag to opt for including matched code snippet in the result. Default behavior is false.
    :type include_snippet: bool
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '{[str]}'},
        'search_text': {'key': 'searchText', 'type': 'str'},
        'order_by': {'key': '$orderBy', 'type': '[SortOption]'},
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'include_facets': {'key': 'includeFacets', 'type': 'bool'},
        'include_snippet': {'key': 'includeSnippet', 'type': 'bool'}
    }

    def __init__(self, filters=None, search_text=None, order_by=None, skip=None, top=None, include_facets=None, include_snippet=None):
        super(CodeSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)
        self.include_snippet = include_snippet


__all__ = [
    'BoardResult',
    'BranchInfo',
    'CodeResult',
    'Collection',
    'CustomRepositoryStatusResponse',
    'DepotInfo',
    'EntitySearchRequestBase',
    'EntitySearchResponse',
    'FeedInfo',
    'Filter',
    'Hit',
    'PackageHit',
    'PackageResult',
    'PackageSearchResponse',
    'PackageSearchResponseContent',
    'Project',
    'ProjectReference',
    'Repository',
    'RepositoryStatusResponse',
    'ScrollSearchRequest',
    'SettingResult',
    'SettingSearchResponse',
    'SortOption',
    'Team',
    'TfvcRepositoryStatusResponse',
    'Version',
    'Wiki',
    'WikiHit',
    'WikiResult',
    'WikiSearchResponse',
    'WorkItemHit',
    'WorkItemResult',
    'WorkItemSearchResponse',
    'BoardSearchResponse',
    'CodeSearchResponse',
    'EntitySearchRequest',
    'PackageSearchRequest',
    'SettingSearchRequest',
    'WikiSearchRequest',
    'WorkItemSearchRequest',
    'BoardSearchRequest',
    'CodeSearchRequest',
]
