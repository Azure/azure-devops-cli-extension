# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CodeResult(Model):
    """CodeResult.

    :param collection: Collection of the result file.
    :type collection: :class:`Collection <azure.devops.v5_0.search.models.Collection>`
    :param content_id: ContentId of the result file.
    :type content_id: str
    :param file_name: Name of the result file.
    :type file_name: str
    :param matches: Dictionary of field to hit offsets in the result file. Key identifies the area in which hits were found, for ex: file content/file name etc.
    :type matches: dict
    :param path: Path at which result file is present.
    :type path: str
    :param project: Project of the result file.
    :type project: :class:`Project <azure.devops.v5_0.search.models.Project>`
    :param repository: Repository of the result file.
    :type repository: :class:`Repository <azure.devops.v5_0.search.models.Repository>`
    :param versions: Versions of the result file.
    :type versions: list of :class:`str <azure.devops.v5_0.search.models.str>`
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'Collection'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'matches': {'key': 'matches', 'type': '{[Hit]}'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'Project'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'versions': {'key': 'versions', 'type': '[str]'}
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
    """Collection.

    :param name: Name of the collection.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(Collection, self).__init__()
        self.name = name


class EntitySearchRequestBase(Model):
    """EntitySearchRequestBase.

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
    """EntitySearchResponse.

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


class Filter(Model):
    """Filter.

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
    """Hit.

    :param char_offset: Gets or sets the start character offset of a piece of text.
    :type char_offset: int
    :param length: Gets or sets the length of a piece of text.
    :type length: int
    """

    _attribute_map = {
        'char_offset': {'key': 'charOffset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'}
    }

    def __init__(self, char_offset=None, length=None):
        super(Hit, self).__init__()
        self.char_offset = char_offset
        self.length = length


class Project(Model):
    """Project.

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
    """ProjectReference.

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
    """Repository.

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


class SortOption(Model):
    """SortOption.

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


class Wiki(Model):
    """Wiki.

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
    """WikiHit.

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
    """WikiResult.

    :param collection: Collection of the result file.
    :type collection: :class:`Collection <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.Collection>`
    :param content_id: ContentId of the result file.
    :type content_id: str
    :param file_name: Name of the result file.
    :type file_name: str
    :param hits: Highlighted snippets of fields that match the search request. The list is sorted by relevance of the snippets.
    :type hits: list of :class:`WikiHit <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.WikiHit>`
    :param path: Path at which result file is present.
    :type path: str
    :param project: Project details of the wiki document.
    :type project: :class:`ProjectReference <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.ProjectReference>`
    :param wiki: Wiki information for the result.
    :type wiki: :class:`Wiki <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.Wiki>`
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
    """WikiSearchResponse.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched wiki documents.
    :type count: int
    :param results: List of top matched wiki documents.
    :type results: list of :class:`WikiResult <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.WikiResult>`
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
    """WorkItemHit.

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
    """WorkItemResult.

    :param fields: A standard set of work item fields and their values.
    :type fields: dict
    :param hits: Highlighted snippets of fields that match the search request. The list is sorted by relevance of the snippets.
    :type hits: list of :class:`WorkItemHit <azure.devops.v5_0.search.models.WorkItemHit>`
    :param project: Project details of the work item.
    :type project: :class:`Project <azure.devops.v5_0.search.models.Project>`
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
    """WorkItemSearchResponse.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched work items.
    :type count: int
    :param results: List of top matched work items.
    :type results: list of :class:`WorkItemResult <azure.devops.v5_0.search.models.WorkItemResult>`
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


class CodeSearchResponse(EntitySearchResponse):
    """CodeSearchResponse.

    :param facets: A dictionary storing an array of <code>Filter</code> object against each facet.
    :type facets: dict
    :param info_code: Numeric code indicating any additional information: 0 - Ok, 1 - Account is being reindexed, 2 - Account indexing has not started, 3 - Invalid Request, 4 - Prefix wildcard query not supported, 5 - MultiWords with code facet not supported, 6 - Account is being onboarded, 7 - Account is being onboarded or reindexed, 8 - Top value trimmed to maxresult allowed 9 - Branches are being indexed, 10 - Faceting not enabled, 11 - Work items not accessible, 19 - Phrase queries with code type filters not supported, 20 - Wildcard queries with code type filters not supported. Any other info code is used for internal purpose.
    :type info_code: int
    :param count: Total number of matched files.
    :type count: int
    :param results: List of matched files.
    :type results: list of :class:`CodeResult <azure.devops.v5_0.search.models.CodeResult>`
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
    """EntitySearchRequest.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
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


class WikiSearchRequest(EntitySearchRequest):
    """WikiSearchRequest.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v5_0.microsoft._visual_studio._services._search._shared._web_api.models.SortOption>`
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
    """WorkItemSearchRequest.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v5_0.search.models.SortOption>`
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


class CodeSearchRequest(EntitySearchRequest):
    """CodeSearchRequest.

    :param filters: Filters to be applied. Set it to null if there are no filters to be applied.
    :type filters: dict
    :param search_text: The search text.
    :type search_text: str
    :param order_by: Options for sorting search results. If set to null, the results will be returned sorted by relevance. If more than one sort option is provided, the results are sorted in the order specified in the OrderBy.
    :type order_by: list of :class:`SortOption <azure.devops.v5_0.search.models.SortOption>`
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
        super(CodeSearchRequest, self).__init__(filters=filters, search_text=search_text, order_by=order_by, skip=skip, top=top, include_facets=include_facets)


__all__ = [
    'CodeResult',
    'Collection',
    'EntitySearchRequestBase',
    'EntitySearchResponse',
    'Filter',
    'Hit',
    'Project',
    'ProjectReference',
    'Repository',
    'SortOption',
    'Wiki',
    'WikiHit',
    'WikiResult',
    'WikiSearchResponse',
    'WorkItemHit',
    'WorkItemResult',
    'WorkItemSearchResponse',
    'CodeSearchResponse',
    'EntitySearchRequest',
    'WikiSearchRequest',
    'WorkItemSearchRequest',
    'CodeSearchRequest',
]
