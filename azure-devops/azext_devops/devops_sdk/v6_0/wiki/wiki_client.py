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


class WikiClient(Client):
    """Wiki
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WikiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bf7d82a0-8aa5-4613-94ef-6172a5ea01f3'

    def create_attachment(self, upload_stream, project, wiki_identifier, name, version_descriptor=None, **kwargs):
        """CreateAttachment.
        [Preview API] Creates an attachment in the wiki.
        :param object upload_stream: Stream to upload
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str name: Wiki attachment name.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).
        :rtype: :class:`<WikiAttachmentResponse> <azure.devops.v6_0.wiki.models.WikiAttachmentResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='c4382d8d-fefc-40e0-92c5-49852e9e17c0',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        response_object = models.WikiAttachmentResponse()
        response_object.attachment = self._deserialize('WikiAttachment', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def create_page_move(self, page_move_parameters, project, wiki_identifier, comment=None, version_descriptor=None):
        """CreatePageMove.
        [Preview API] Creates a page move operation that updates the path and order of the page as provided in the parameters.
        :param :class:`<WikiPageMoveParameters> <azure.devops.v6_0.wiki.models.WikiPageMoveParameters>` page_move_parameters: Page more operation parameters.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str comment: Comment that is to be associated with this page move.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).
        :rtype: :class:`<WikiPageMoveResponse> <azure.devops.v6_0.wiki.models.WikiPageMoveResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        content = self._serialize.body(page_move_parameters, 'WikiPageMoveParameters')
        response = self._send(http_method='POST',
                              location_id='e37bbe71-cbae-49e5-9a4e-949143b9d910',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        response_object = models.WikiPageMoveResponse()
        response_object.page_move = self._deserialize('WikiPageMove', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def create_or_update_page(self, parameters, project, wiki_identifier, path, version, comment=None, version_descriptor=None):
        """CreateOrUpdatePage.
        [Preview API] Creates or edits a wiki page.
        :param :class:`<WikiPageCreateOrUpdateParameters> <azure.devops.v6_0.wiki.models.WikiPageCreateOrUpdateParameters>` parameters: Wiki create or update operation parameters.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str path: Wiki page path.
        :param String version: Version of the page on which the change is to be made. Mandatory for `Edit` scenario. To be populated in the If-Match header of the request.
        :param str comment: Comment to be associated with the page operation.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        additional_headers = {}
        if version is not None:
            additional_headers['If-Match'] = version
        content = self._serialize.body(parameters, 'WikiPageCreateOrUpdateParameters')
        response = self._send(http_method='PUT',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def delete_page(self, project, wiki_identifier, path, comment=None, version_descriptor=None):
        """DeletePage.
        [Preview API] Deletes a wiki page.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str path: Wiki page path.
        :param str comment: Comment to be associated with this page delete.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        response = self._send(http_method='DELETE',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None):
        """GetPage.
        [Preview API] Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str path: Wiki page path.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page_text(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        """GetPageText.
        [Preview API] Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str path: Wiki page path.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_page_zip(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        """GetPageZip.
        [Preview API] Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str path: Wiki page path.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def delete_page_by_id(self, project, wiki_identifier, id, comment=None):
        """DeletePageById.
        [Preview API] Deletes a wiki page.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param int id: Wiki page ID.
        :param str comment: Comment to be associated with this page delete.
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        response = self._send(http_method='DELETE',
                              location_id='ceddcf75-1068-452d-8b13-2d4d76e1f970',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page_by_id(self, project, wiki_identifier, id, recursion_level=None, include_content=None):
        """GetPageById.
        [Preview API] Gets metadata or content of the wiki page for the provided page id. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name..
        :param int id: Wiki page ID.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ceddcf75-1068-452d-8b13-2d4d76e1f970',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page_by_id_text(self, project, wiki_identifier, id, recursion_level=None, include_content=None, **kwargs):
        """GetPageByIdText.
        [Preview API] Gets metadata or content of the wiki page for the provided page id. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name..
        :param int id: Wiki page ID.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ceddcf75-1068-452d-8b13-2d4d76e1f970',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_page_by_id_zip(self, project, wiki_identifier, id, recursion_level=None, include_content=None, **kwargs):
        """GetPageByIdZip.
        [Preview API] Gets metadata or content of the wiki page for the provided page id. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name..
        :param int id: Wiki page ID.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ceddcf75-1068-452d-8b13-2d4d76e1f970',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_page_by_id(self, parameters, project, wiki_identifier, id, version, comment=None):
        """UpdatePageById.
        [Preview API] Edits a wiki page.
        :param :class:`<WikiPageCreateOrUpdateParameters> <azure.devops.v6_0.wiki.models.WikiPageCreateOrUpdateParameters>` parameters: Wiki update operation parameters.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param int id: Wiki page ID.
        :param String version: Version of the page on which the change is to be made. Mandatory for `Edit` scenario. To be populated in the If-Match header of the request.
        :param str comment: Comment to be associated with the page operation.
        :rtype: :class:`<WikiPageResponse> <azure.devops.v6_0.wiki.models.WikiPageResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        additional_headers = {}
        if version is not None:
            additional_headers['If-Match'] = version
        content = self._serialize.body(parameters, 'WikiPageCreateOrUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='ceddcf75-1068-452d-8b13-2d4d76e1f970',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_pages_batch(self, pages_batch_request, project, wiki_identifier, version_descriptor=None):
        """GetPagesBatch.
        [Preview API] Returns pageable list of Wiki Pages
        :param :class:`<WikiPagesBatchRequest> <azure.devops.v6_0.wiki.models.WikiPagesBatchRequest>` pages_batch_request: Wiki batch page request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.wiki.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).
        :rtype: :class:`<[WikiPageDetail]> <azure.devops.v6_0.wiki.models.[WikiPageDetail]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        content = self._serialize.body(pages_batch_request, 'WikiPagesBatchRequest')
        response = self._send(http_method='POST',
                              location_id='71323c46-2592-4398-8771-ced73dd87207',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[WikiPageDetail]', self._unwrap_collection(response))

    def get_page_data(self, project, wiki_identifier, page_id, page_views_for_days=None):
        """GetPageData.
        [Preview API] Returns page detail corresponding to Page ID.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki ID or wiki name.
        :param int page_id: Wiki page ID.
        :param int page_views_for_days: last N days from the current day for which page views is to be returned. It's inclusive of current day.
        :rtype: :class:`<WikiPageDetail> <azure.devops.v6_0.wiki.models.WikiPageDetail>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'int')
        query_parameters = {}
        if page_views_for_days is not None:
            query_parameters['pageViewsForDays'] = self._serialize.query('page_views_for_days', page_views_for_days, 'int')
        response = self._send(http_method='GET',
                              location_id='81c4e0fe-7663-4d62-ad46-6ab78459f274',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WikiPageDetail', response)

    def create_wiki(self, wiki_create_params, project=None):
        """CreateWiki.
        [Preview API] Creates the wiki resource.
        :param :class:`<WikiCreateParametersV2> <azure.devops.v6_0.wiki.models.WikiCreateParametersV2>` wiki_create_params: Parameters for the wiki creation.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <azure.devops.v6_0.wiki.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(wiki_create_params, 'WikiCreateParametersV2')
        response = self._send(http_method='POST',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

    def delete_wiki(self, wiki_identifier, project=None):
        """DeleteWiki.
        [Preview API] Deletes the wiki corresponding to the wiki ID or wiki name provided.
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <azure.devops.v6_0.wiki.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='DELETE',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def get_all_wikis(self, project=None):
        """GetAllWikis.
        [Preview API] Gets all wikis in a project or collection.
        :param str project: Project ID or project name
        :rtype: [WikiV2]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('[WikiV2]', self._unwrap_collection(response))

    def get_wiki(self, wiki_identifier, project=None):
        """GetWiki.
        [Preview API] Gets the wiki corresponding to the wiki ID or wiki name provided.
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <azure.devops.v6_0.wiki.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def update_wiki(self, update_parameters, wiki_identifier, project=None):
        """UpdateWiki.
        [Preview API] Updates the wiki corresponding to the wiki ID or wiki name provided using the update parameters.
        :param :class:`<WikiUpdateParameters> <azure.devops.v6_0.wiki.models.WikiUpdateParameters>` update_parameters: Update parameters.
        :param str wiki_identifier: Wiki ID or wiki name.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <azure.devops.v6_0.wiki.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        content = self._serialize.body(update_parameters, 'WikiUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

