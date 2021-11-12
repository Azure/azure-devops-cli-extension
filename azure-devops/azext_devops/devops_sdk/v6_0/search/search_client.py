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


class SearchClient(Client):
    """Search
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(SearchClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'ea48a0a1-269c-42d8-b8ad-ddc8fcdcf578'

    def fetch_scroll_code_search_results(self, request, project=None):
        """FetchScrollCodeSearchResults.
        [Preview API] Provides a set of results for the search text.
        :param :class:`<ScrollSearchRequest> <azure.devops.v6_0.search.models.ScrollSearchRequest>` request: The Code Search Request.
        :param str project: Project ID or project name
        :rtype: :class:`<CodeSearchResponse> <azure.devops.v6_0.search.models.CodeSearchResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'ScrollSearchRequest')
        response = self._send(http_method='POST',
                              location_id='852dac94-e8f7-45a2-9910-927ae35766a2',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CodeSearchResponse', response)

    def fetch_code_search_results(self, request, project=None):
        """FetchCodeSearchResults.
        [Preview API] Provides a set of results for the search text.
        :param :class:`<CodeSearchRequest> <azure.devops.v6_0.search.models.CodeSearchRequest>` request: The Code Search Request.
        :param str project: Project ID or project name
        :rtype: :class:`<CodeSearchResponse> <azure.devops.v6_0.search.models.CodeSearchResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'CodeSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e7f29993-5b82-4fca-9386-f5cfe683d524',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CodeSearchResponse', response)

    def fetch_package_search_results(self, request):
        """FetchPackageSearchResults.
        [Preview API] Provides a set of results for the search text.
        :param :class:`<PackageSearchRequest> <azure.devops.v6_0.search.models.PackageSearchRequest>` request: The Package Search Request.
        :rtype: :class:`<PackageSearchResponse> <azure.devops.v6_0.search.models.PackageSearchResponse>`
        """
        content = self._serialize.body(request, 'PackageSearchRequest')
        response = self._send(http_method='POST',
                              location_id='f62ada48-eedc-4c8e-93f0-de870e4ecce0',
                              version='6.0-preview.1',
                              content=content)
        response_object = models.PackageSearchResponse()
        response_object.content = self._deserialize('PackageSearchResponseContent', response)
        response_object.activity_id = response.headers.get('ActivityId')
        return response_object

    def get_repository_status(self, project, repository):
        """GetRepositoryStatus.
        [Preview API] Provides status of Repository.
        :param str project: Project ID or project name
        :param str repository: Repository ID or repository name.
        :rtype: :class:`<RepositoryStatusResponse> <azure.devops.v6_0.search.models.RepositoryStatusResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository is not None:
            route_values['repository'] = self._serialize.url('repository', repository, 'str')
        response = self._send(http_method='GET',
                              location_id='1f60303c-7261-4387-80f1-742a2ecf2964',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('RepositoryStatusResponse', response)

    def get_tfvc_repository_status(self, project):
        """GetTfvcRepositoryStatus.
        [Preview API] Provides status of TFVC Repository.
        :param str project: Project ID or project name
        :rtype: :class:`<TfvcRepositoryStatusResponse> <azure.devops.v6_0.search.models.TfvcRepositoryStatusResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='d5bf4e52-e0af-4626-8c50-8a80b18fa69f',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('TfvcRepositoryStatusResponse', response)

    def fetch_wiki_search_results(self, request, project=None):
        """FetchWikiSearchResults.
        [Preview API] Provides a set of results for the search request.
        :param :class:`<WikiSearchRequest> <azure.devops.v6_0.search.models.WikiSearchRequest>` request: The Wiki Search Request.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiSearchResponse> <azure.devops.v6_0.search.models.WikiSearchResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WikiSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e90e7664-7049-4100-9a86-66b161d81080',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiSearchResponse', response)

    def fetch_work_item_search_results(self, request, project=None):
        """FetchWorkItemSearchResults.
        [Preview API] Provides a set of results for the search text.
        :param :class:`<WorkItemSearchRequest> <azure.devops.v6_0.search.models.WorkItemSearchRequest>` request: The Work Item Search Request.
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemSearchResponse> <azure.devops.v6_0.search.models.WorkItemSearchResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WorkItemSearchRequest')
        response = self._send(http_method='POST',
                              location_id='73b2c9e2-ff9e-4447-8cda-5f5b21ff7cae',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemSearchResponse', response)

