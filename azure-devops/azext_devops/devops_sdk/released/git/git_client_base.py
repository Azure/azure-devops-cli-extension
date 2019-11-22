# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.git import models


class GitClientBase(Client):
    """Git
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(GitClientBase, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '4e080c62-fa21-4fbc-8fef-2a10a2b38049'

    def get_blob(self, repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None):
        """GetBlob.
        Get a single blob.
        :param str repository_id: The name or ID of the repository.
        :param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.
        :param str project: Project ID or project name
        :param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip
        :param str file_name: Provide a fileName to use for a download.
        :param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types
        :rtype: :class:`<GitBlobRef> <azure.devops.v5_1.git.models.GitBlobRef>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if sha1 is not None:
            route_values['sha1'] = self._serialize.url('sha1', sha1, 'str')
        query_parameters = {}
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='7b28e929-2c99-405d-9c5c-6167a06e6816',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitBlobRef', response)

    def get_blob_content(self, repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs):
        """GetBlobContent.
        Get a single blob.
        :param str repository_id: The name or ID of the repository.
        :param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.
        :param str project: Project ID or project name
        :param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip
        :param str file_name: Provide a fileName to use for a download.
        :param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if sha1 is not None:
            route_values['sha1'] = self._serialize.url('sha1', sha1, 'str')
        query_parameters = {}
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='7b28e929-2c99-405d-9c5c-6167a06e6816',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_blobs_zip(self, blob_ids, repository_id, project=None, filename=None, **kwargs):
        """GetBlobsZip.
        Gets one or more blobs in a zip file download.
        :param [str] blob_ids: Blob IDs (SHA1 hashes) to be returned in the zip file.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param str filename:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if filename is not None:
            query_parameters['filename'] = self._serialize.query('filename', filename, 'str')
        content = self._serialize.body(blob_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='7b28e929-2c99-405d-9c5c-6167a06e6816',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_blob_zip(self, repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs):
        """GetBlobZip.
        Get a single blob.
        :param str repository_id: The name or ID of the repository.
        :param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.
        :param str project: Project ID or project name
        :param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip
        :param str file_name: Provide a fileName to use for a download.
        :param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if sha1 is not None:
            route_values['sha1'] = self._serialize.url('sha1', sha1, 'str')
        query_parameters = {}
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='7b28e929-2c99-405d-9c5c-6167a06e6816',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_branch(self, repository_id, name, project=None, base_version_descriptor=None):
        """GetBranch.
        Retrieve statistics about a single branch.
        :param str repository_id: The name or ID of the repository.
        :param str name: Name of the branch.
        :param str project: Project ID or project name
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` base_version_descriptor: Identifies the commit or branch to use as the base.
        :rtype: :class:`<GitBranchStats> <azure.devops.v5_1.git.models.GitBranchStats>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if base_version_descriptor is not None:
            if base_version_descriptor.version_type is not None:
                query_parameters['baseVersionDescriptor.versionType'] = base_version_descriptor.version_type
            if base_version_descriptor.version is not None:
                query_parameters['baseVersionDescriptor.version'] = base_version_descriptor.version
            if base_version_descriptor.version_options is not None:
                query_parameters['baseVersionDescriptor.versionOptions'] = base_version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='d5b216de-d8d5-4d32-ae76-51df755b16d3',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitBranchStats', response)

    def get_branches(self, repository_id, project=None, base_version_descriptor=None):
        """GetBranches.
        Retrieve statistics about all branches within a repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` base_version_descriptor: Identifies the commit or branch to use as the base.
        :rtype: [GitBranchStats]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if base_version_descriptor is not None:
            if base_version_descriptor.version_type is not None:
                query_parameters['baseVersionDescriptor.versionType'] = base_version_descriptor.version_type
            if base_version_descriptor.version is not None:
                query_parameters['baseVersionDescriptor.version'] = base_version_descriptor.version
            if base_version_descriptor.version_options is not None:
                query_parameters['baseVersionDescriptor.versionOptions'] = base_version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='d5b216de-d8d5-4d32-ae76-51df755b16d3',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitBranchStats]', self._unwrap_collection(response))

    def get_changes(self, commit_id, repository_id, project=None, top=None, skip=None):
        """GetChanges.
        Retrieve changes for a particular commit.
        :param str commit_id: The id of the commit.
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param str project: Project ID or project name
        :param int top: The maximum number of changes to return.
        :param int skip: The number of changes to skip.
        :rtype: :class:`<GitCommitChanges> <azure.devops.v5_1.git.models.GitCommitChanges>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if commit_id is not None:
            route_values['commitId'] = self._serialize.url('commit_id', commit_id, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='5bf884f5-3e07-42e9-afb8-1b872267bf16',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommitChanges', response)

    def get_commit_diffs(self, repository_id, project=None, diff_common_commit=None, top=None, skip=None, base_version_descriptor=None, target_version_descriptor=None):
        """GetCommitDiffs.
        Find the closest common commit (the merge base) between base and target commits, and get the diff between either the base and target commits or common and target commits.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param bool diff_common_commit: If true, diff between common and target commits. If false, diff between base and target commits.
        :param int top: Maximum number of changes to return. Defaults to 100.
        :param int skip: Number of changes to skip
        :param :class:`<GitBaseVersionDescriptor> <azure.devops.v5_1.git.models.GitBaseVersionDescriptor>` base_version_descriptor: Descriptor for base commit.
        :param :class:`<GitTargetVersionDescriptor> <azure.devops.v5_1.git.models.GitTargetVersionDescriptor>` target_version_descriptor: Descriptor for target commit.
        :rtype: :class:`<GitCommitDiffs> <azure.devops.v5_1.git.models.GitCommitDiffs>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if diff_common_commit is not None:
            query_parameters['diffCommonCommit'] = self._serialize.query('diff_common_commit', diff_common_commit, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if base_version_descriptor is not None:
            if base_version_descriptor.base_version_type is not None:
                query_parameters['baseVersionType'] = base_version_descriptor.base_version_type
            if base_version_descriptor.base_version is not None:
                query_parameters['baseVersion'] = base_version_descriptor.base_version
            if base_version_descriptor.base_version_options is not None:
                query_parameters['baseVersionOptions'] = base_version_descriptor.base_version_options
        if target_version_descriptor is not None:
            if target_version_descriptor.target_version_type is not None:
                query_parameters['targetVersionType'] = target_version_descriptor.target_version_type
            if target_version_descriptor.target_version is not None:
                query_parameters['targetVersion'] = target_version_descriptor.target_version
            if target_version_descriptor.target_version_options is not None:
                query_parameters['targetVersionOptions'] = target_version_descriptor.target_version_options
        response = self._send(http_method='GET',
                              location_id='615588d5-c0c7-4b88-88f8-e625306446e8',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommitDiffs', response)

    def get_commit(self, commit_id, repository_id, project=None, change_count=None):
        """GetCommit.
        Retrieve a particular commit.
        :param str commit_id: The id of the commit.
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param str project: Project ID or project name
        :param int change_count: The number of changes to include in the result.
        :rtype: :class:`<GitCommit> <azure.devops.v5_1.git.models.GitCommit>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if commit_id is not None:
            route_values['commitId'] = self._serialize.url('commit_id', commit_id, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if change_count is not None:
            query_parameters['changeCount'] = self._serialize.query('change_count', change_count, 'int')
        response = self._send(http_method='GET',
                              location_id='c2570c3b-5b3f-41b8-98bf-5407bfde8d58',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommit', response)

    def get_commits(self, repository_id, search_criteria, project=None, skip=None, top=None):
        """GetCommits.
        Retrieve git commits for a project
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param :class:`<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria>` search_criteria:
        :param str project: Project ID or project name
        :param int skip:
        :param int top:
        :rtype: [GitCommitRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if search_criteria is not None:
            if search_criteria.ids is not None:
                query_parameters['searchCriteria.ids'] = search_criteria.ids
            if search_criteria.from_date is not None:
                query_parameters['searchCriteria.fromDate'] = search_criteria.from_date
            if search_criteria.to_date is not None:
                query_parameters['searchCriteria.toDate'] = search_criteria.to_date
            if search_criteria.item_version is not None:
                if search_criteria.item_version.version_type is not None:
                    query_parameters['searchCriteria.itemVersion.versionType'] = search_criteria.item_version.version_type
                if search_criteria.item_version.version is not None:
                    query_parameters['searchCriteria.itemVersion.version'] = search_criteria.item_version.version
                if search_criteria.item_version.version_options is not None:
                    query_parameters['searchCriteria.itemVersion.versionOptions'] = search_criteria.item_version.version_options
            if search_criteria.compare_version is not None:
                if search_criteria.compare_version.version_type is not None:
                    query_parameters['searchCriteria.compareVersion.versionType'] = search_criteria.compare_version.version_type
                if search_criteria.compare_version.version is not None:
                    query_parameters['searchCriteria.compareVersion.version'] = search_criteria.compare_version.version
                if search_criteria.compare_version.version_options is not None:
                    query_parameters['searchCriteria.compareVersion.versionOptions'] = search_criteria.compare_version.version_options
            if search_criteria.from_commit_id is not None:
                query_parameters['searchCriteria.fromCommitId'] = search_criteria.from_commit_id
            if search_criteria.to_commit_id is not None:
                query_parameters['searchCriteria.toCommitId'] = search_criteria.to_commit_id
            if search_criteria.user is not None:
                query_parameters['searchCriteria.user'] = search_criteria.user
            if search_criteria.author is not None:
                query_parameters['searchCriteria.author'] = search_criteria.author
            if search_criteria.item_path is not None:
                query_parameters['searchCriteria.itemPath'] = search_criteria.item_path
            if search_criteria.exclude_deletes is not None:
                query_parameters['searchCriteria.excludeDeletes'] = search_criteria.exclude_deletes
            if search_criteria.skip is not None:
                query_parameters['searchCriteria.$skip'] = search_criteria.skip
            if search_criteria.top is not None:
                query_parameters['searchCriteria.$top'] = search_criteria.top
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
            if search_criteria.include_work_items is not None:
                query_parameters['searchCriteria.includeWorkItems'] = search_criteria.include_work_items
            if search_criteria.include_user_image_url is not None:
                query_parameters['searchCriteria.includeUserImageUrl'] = search_criteria.include_user_image_url
            if search_criteria.include_push_data is not None:
                query_parameters['searchCriteria.includePushData'] = search_criteria.include_push_data
            if search_criteria.history_mode is not None:
                query_parameters['searchCriteria.historyMode'] = search_criteria.history_mode
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='c2570c3b-5b3f-41b8-98bf-5407bfde8d58',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_push_commits(self, repository_id, push_id, project=None, top=None, skip=None, include_links=None):
        """GetPushCommits.
        Retrieve a list of commits associated with a particular push.
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param int push_id: The id of the push.
        :param str project: Project ID or project name
        :param int top: The maximum number of commits to return ("get the top x commits").
        :param int skip: The number of commits to skip.
        :param bool include_links: Set to false to avoid including REST Url links for resources. Defaults to true.
        :rtype: [GitCommitRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if push_id is not None:
            query_parameters['pushId'] = self._serialize.query('push_id', push_id, 'int')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['skip'] = self._serialize.query('skip', skip, 'int')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='c2570c3b-5b3f-41b8-98bf-5407bfde8d58',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_commits_batch(self, search_criteria, repository_id, project=None, skip=None, top=None, include_statuses=None):
        """GetCommitsBatch.
        Retrieve git commits for a project matching the search criteria
        :param :class:`<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria>` search_criteria: Search options
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param int skip: Number of commits to skip.
        :param int top: Maximum number of commits to return.
        :param bool include_statuses: True to include additional commit status information.
        :rtype: [GitCommitRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_statuses is not None:
            query_parameters['includeStatuses'] = self._serialize.query('include_statuses', include_statuses, 'bool')
        content = self._serialize.body(search_criteria, 'GitQueryCommitsCriteria')
        response = self._send(http_method='POST',
                              location_id='6400dfb2-0bcb-462b-b992-5a57f8f1416c',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_item(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None):
        """GetItem.
        Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :rtype: :class:`<GitItem> <azure.devops.v5_1.git.models.GitItem>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content_metadata is not None:
            query_parameters['includeContentMetadata'] = self._serialize.query('include_content_metadata', include_content_metadata, 'bool')
        if latest_processed_change is not None:
            query_parameters['latestProcessedChange'] = self._serialize.query('latest_processed_change', latest_processed_change, 'bool')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitItem', response)

    def get_item_content(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs):
        """GetItemContent.
        Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content_metadata is not None:
            query_parameters['includeContentMetadata'] = self._serialize.query('include_content_metadata', include_content_metadata, 'bool')
        if latest_processed_change is not None:
            query_parameters['latestProcessedChange'] = self._serialize.query('latest_processed_change', latest_processed_change, 'bool')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_items(self, repository_id, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, include_links=None, version_descriptor=None):
        """GetItems.
        Get Item Metadata and/or Content for a collection of items. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param bool include_links: Set to true to include links to items.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :rtype: [GitItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content_metadata is not None:
            query_parameters['includeContentMetadata'] = self._serialize.query('include_content_metadata', include_content_metadata, 'bool')
        if latest_processed_change is not None:
            query_parameters['latestProcessedChange'] = self._serialize.query('latest_processed_change', latest_processed_change, 'bool')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitItem]', self._unwrap_collection(response))

    def get_item_text(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs):
        """GetItemText.
        Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content_metadata is not None:
            query_parameters['includeContentMetadata'] = self._serialize.query('include_content_metadata', include_content_metadata, 'bool')
        if latest_processed_change is not None:
            query_parameters['latestProcessedChange'] = self._serialize.query('latest_processed_change', latest_processed_change, 'bool')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_item_zip(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs):
        """GetItemZip.
        Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_content_metadata is not None:
            query_parameters['includeContentMetadata'] = self._serialize.query('include_content_metadata', include_content_metadata, 'bool')
        if latest_processed_change is not None:
            query_parameters['latestProcessedChange'] = self._serialize.query('latest_processed_change', latest_processed_change, 'bool')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        if resolve_lfs is not None:
            query_parameters['resolveLfs'] = self._serialize.query('resolve_lfs', resolve_lfs, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_items_batch(self, request_data, repository_id, project=None):
        """GetItemsBatch.
        Post for retrieving a creating a batch out of a set of items in a repo / project given a list of paths or a long path
        :param :class:`<GitItemRequestData> <azure.devops.v5_1.git.models.GitItemRequestData>` request_data: Request data attributes: ItemDescriptors, IncludeContentMetadata, LatestProcessedChange, IncludeLinks. ItemDescriptors: Collection of items to fetch, including path, version, and recursion level. IncludeContentMetadata: Whether to include metadata for all items LatestProcessedChange: Whether to include shallow ref to commit that last changed each item. IncludeLinks: Whether to include the _links field on the shallow references.
        :param str repository_id: The name or ID of the repository
        :param str project: Project ID or project name
        :rtype: [[GitItem]]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(request_data, 'GitItemRequestData')
        response = self._send(http_method='POST',
                              location_id='630fd2e4-fb88-4f85-ad21-13f3fd1fbca9',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[[GitItem]]', self._unwrap_collection(response))

    def get_pull_request_iteration_commits(self, repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None):
        """GetPullRequestIterationCommits.
        Get the commits for the specified iteration of a pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the iteration from which to get the commits.
        :param str project: Project ID or project name
        :param int top: Maximum number of commits to return. The maximum number of commits that can be returned per batch is 500.
        :param int skip: Number of commits to skip.
        :rtype: [GitCommitRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='e7ea0883-095f-4926-b5fb-f24691c26fb9',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_pull_request_commits(self, repository_id, pull_request_id, project=None, top=None, continuation_token=None):
        """GetPullRequestCommits.
        Get the commits for the specified pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param int top: Maximum number of commits to return.
        :param str continuation_token: The continuation token used for pagination.
        :rtype: :class:`<GetPullRequestCommitsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='52823034-34a8-4576-922c-8d8b77e9e4c4',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[GitCommitRef]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetPullRequestCommitsResponseValue(response_value, continuation_token)

    class GetPullRequestCommitsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_pull_request_commits method

            :param value:
            :type value: :class:`<[GitCommitRef]> <azure.devops.v5_1.git.models.[GitCommitRef]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def get_pull_request_iteration_changes(self, repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None, compare_to=None):
        """GetPullRequestIterationChanges.
        Retrieve the changes made in a pull request between two iterations.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration. <br /> Iteration IDs are zero-based with zero indicating the common commit between the source and target branches. Iteration one is the head of the source branch at the time the pull request is created and subsequent iterations are created when there are pushes to the source branch.
        :param str project: Project ID or project name
        :param int top: Optional. The number of changes to retrieve.  The default value is 100 and the maximum value is 2000.
        :param int skip: Optional. The number of changes to ignore.  For example, to retrieve changes 101-150, set top 50 and skip to 100.
        :param int compare_to: ID of the pull request iteration to compare against.  The default value is zero which indicates the comparison is made against the common commit between the source and target branches
        :rtype: :class:`<GitPullRequestIterationChanges> <azure.devops.v5_1.git.models.GitPullRequestIterationChanges>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if compare_to is not None:
            query_parameters['$compareTo'] = self._serialize.query('compare_to', compare_to, 'int')
        response = self._send(http_method='GET',
                              location_id='4216bdcf-b6b1-4d59-8b82-c34cc183fc8b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequestIterationChanges', response)

    def get_pull_request_iteration(self, repository_id, pull_request_id, iteration_id, project=None):
        """GetPullRequestIteration.
        Get the specified iteration for a pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration to return.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestIteration> <azure.devops.v5_1.git.models.GitPullRequestIteration>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='d43911ee-6958-46b0-a42b-8445b8a0d004',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequestIteration', response)

    def get_pull_request_iterations(self, repository_id, pull_request_id, project=None, include_commits=None):
        """GetPullRequestIterations.
        Get the list of iterations for the specified pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param bool include_commits: If true, include the commits associated with each iteration in the response.
        :rtype: [GitPullRequestIteration]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if include_commits is not None:
            query_parameters['includeCommits'] = self._serialize.query('include_commits', include_commits, 'bool')
        response = self._send(http_method='GET',
                              location_id='d43911ee-6958-46b0-a42b-8445b8a0d004',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequestIteration]', self._unwrap_collection(response))

    def get_pull_request_query(self, queries, repository_id, project=None):
        """GetPullRequestQuery.
        This API is used to find what pull requests are related to a given commit.  It can be used to either find the pull request that created a particular merge commit or it can be used to find all pull requests that have ever merged a particular commit.  The input is a list of queries which each contain a list of commits. For each commit that you search against, you will get back a dictionary of commit -> pull requests.
        :param :class:`<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery>` queries: The list of queries to perform.
        :param str repository_id: ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(queries, 'GitPullRequestQuery')
        response = self._send(http_method='POST',
                              location_id='b3a6eebe-9cf0-49ea-b6cb-1a4c5f5007b0',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestQuery', response)

    def create_pull_request_reviewer(self, reviewer, repository_id, pull_request_id, reviewer_id, project=None):
        """CreatePullRequestReviewer.
        Add a reviewer to a pull request or cast a vote.
        :param :class:`<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>` reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br />Reviewers can set their own vote with this method.  When adding other reviewers, vote must be set to zero.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if reviewer_id is not None:
            route_values['reviewerId'] = self._serialize.url('reviewer_id', reviewer_id, 'str')
        content = self._serialize.body(reviewer, 'IdentityRefWithVote')
        response = self._send(http_method='PUT',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('IdentityRefWithVote', response)

    def create_pull_request_reviewers(self, reviewers, repository_id, pull_request_id, project=None):
        """CreatePullRequestReviewers.
        Add reviewers to a pull request.
        :param [IdentityRef] reviewers: Reviewers to add to the pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: [IdentityRefWithVote]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(reviewers, '[IdentityRef]')
        response = self._send(http_method='POST',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[IdentityRefWithVote]', self._unwrap_collection(response))

    def delete_pull_request_reviewer(self, repository_id, pull_request_id, reviewer_id, project=None):
        """DeletePullRequestReviewer.
        Remove a reviewer from a pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer to remove.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if reviewer_id is not None:
            route_values['reviewerId'] = self._serialize.url('reviewer_id', reviewer_id, 'str')
        self._send(http_method='DELETE',
                   location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                   version='5.1',
                   route_values=route_values)

    def get_pull_request_reviewer(self, repository_id, pull_request_id, reviewer_id, project=None):
        """GetPullRequestReviewer.
        Retrieve information about a particular reviewer on a pull request
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if reviewer_id is not None:
            route_values['reviewerId'] = self._serialize.url('reviewer_id', reviewer_id, 'str')
        response = self._send(http_method='GET',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('IdentityRefWithVote', response)

    def get_pull_request_reviewers(self, repository_id, pull_request_id, project=None):
        """GetPullRequestReviewers.
        Retrieve the reviewers for a pull request
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: [IdentityRefWithVote]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[IdentityRefWithVote]', self._unwrap_collection(response))

    def update_pull_request_reviewers(self, patch_votes, repository_id, pull_request_id, project=None):
        """UpdatePullRequestReviewers.
        Reset the votes of multiple reviewers on a pull request.  NOTE: This endpoint only supports updating votes, but does not support updating required reviewers (use policy) or display names.
        :param [IdentityRefWithVote] patch_votes: IDs of the reviewers whose votes will be reset to zero
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(patch_votes, '[IdentityRefWithVote]')
        self._send(http_method='PATCH',
                   location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                   version='5.1',
                   route_values=route_values,
                   content=content)

    def get_pull_request_by_id(self, pull_request_id, project=None):
        """GetPullRequestById.
        Retrieve a pull request.
        :param int pull_request_id: The ID of the pull request to retrieve.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='01a46dea-7d46-4d40-bc84-319e7c260d99',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequest', response)

    def get_pull_requests_by_project(self, project, search_criteria, max_comment_length=None, skip=None, top=None):
        """GetPullRequestsByProject.
        Retrieve all pull requests matching a specified criteria.
        :param str project: Project ID or project name
        :param :class:`<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria>` search_criteria: Pull requests will be returned that match this search criteria.
        :param int max_comment_length: Not used.
        :param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.
        :param int top: The number of pull requests to retrieve.
        :rtype: [GitPullRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if search_criteria is not None:
            if search_criteria.repository_id is not None:
                query_parameters['searchCriteria.repositoryId'] = search_criteria.repository_id
            if search_criteria.creator_id is not None:
                query_parameters['searchCriteria.creatorId'] = search_criteria.creator_id
            if search_criteria.reviewer_id is not None:
                query_parameters['searchCriteria.reviewerId'] = search_criteria.reviewer_id
            if search_criteria.status is not None:
                query_parameters['searchCriteria.status'] = search_criteria.status
            if search_criteria.target_ref_name is not None:
                query_parameters['searchCriteria.targetRefName'] = search_criteria.target_ref_name
            if search_criteria.source_repository_id is not None:
                query_parameters['searchCriteria.sourceRepositoryId'] = search_criteria.source_repository_id
            if search_criteria.source_ref_name is not None:
                query_parameters['searchCriteria.sourceRefName'] = search_criteria.source_ref_name
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
        if max_comment_length is not None:
            query_parameters['maxCommentLength'] = self._serialize.query('max_comment_length', max_comment_length, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='a5d28130-9cd2-40fa-9f08-902e7daa9efb',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequest]', self._unwrap_collection(response))

    def create_pull_request(self, git_pull_request_to_create, repository_id, project=None, supports_iterations=None):
        """CreatePullRequest.
        Create a pull request.
        :param :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>` git_pull_request_to_create: The pull request to create.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param str project: Project ID or project name
        :param bool supports_iterations: If true, subsequent pushes to the pull request will be individually reviewable. Set this to false for large pull requests for performance reasons if this functionality is not needed.
        :rtype: :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if supports_iterations is not None:
            query_parameters['supportsIterations'] = self._serialize.query('supports_iterations', supports_iterations, 'bool')
        content = self._serialize.body(git_pull_request_to_create, 'GitPullRequest')
        response = self._send(http_method='POST',
                              location_id='9946fd70-0d40-406e-b686-b4744cbbcc37',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitPullRequest', response)

    def get_pull_request(self, repository_id, pull_request_id, project=None, max_comment_length=None, skip=None, top=None, include_commits=None, include_work_item_refs=None):
        """GetPullRequest.
        Retrieve a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: The ID of the pull request to retrieve.
        :param str project: Project ID or project name
        :param int max_comment_length: Not used.
        :param int skip: Not used.
        :param int top: Not used.
        :param bool include_commits: If true, the pull request will be returned with the associated commits.
        :param bool include_work_item_refs: If true, the pull request will be returned with the associated work item references.
        :rtype: :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if max_comment_length is not None:
            query_parameters['maxCommentLength'] = self._serialize.query('max_comment_length', max_comment_length, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_commits is not None:
            query_parameters['includeCommits'] = self._serialize.query('include_commits', include_commits, 'bool')
        if include_work_item_refs is not None:
            query_parameters['includeWorkItemRefs'] = self._serialize.query('include_work_item_refs', include_work_item_refs, 'bool')
        response = self._send(http_method='GET',
                              location_id='9946fd70-0d40-406e-b686-b4744cbbcc37',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequest', response)

    def get_pull_requests(self, repository_id, search_criteria, project=None, max_comment_length=None, skip=None, top=None):
        """GetPullRequests.
        Retrieve all pull requests matching a specified criteria.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param :class:`<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria>` search_criteria: Pull requests will be returned that match this search criteria.
        :param str project: Project ID or project name
        :param int max_comment_length: Not used.
        :param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.
        :param int top: The number of pull requests to retrieve.
        :rtype: [GitPullRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if search_criteria is not None:
            if search_criteria.repository_id is not None:
                query_parameters['searchCriteria.repositoryId'] = search_criteria.repository_id
            if search_criteria.creator_id is not None:
                query_parameters['searchCriteria.creatorId'] = search_criteria.creator_id
            if search_criteria.reviewer_id is not None:
                query_parameters['searchCriteria.reviewerId'] = search_criteria.reviewer_id
            if search_criteria.status is not None:
                query_parameters['searchCriteria.status'] = search_criteria.status
            if search_criteria.target_ref_name is not None:
                query_parameters['searchCriteria.targetRefName'] = search_criteria.target_ref_name
            if search_criteria.source_repository_id is not None:
                query_parameters['searchCriteria.sourceRepositoryId'] = search_criteria.source_repository_id
            if search_criteria.source_ref_name is not None:
                query_parameters['searchCriteria.sourceRefName'] = search_criteria.source_ref_name
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
        if max_comment_length is not None:
            query_parameters['maxCommentLength'] = self._serialize.query('max_comment_length', max_comment_length, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='9946fd70-0d40-406e-b686-b4744cbbcc37',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequest]', self._unwrap_collection(response))

    def update_pull_request(self, git_pull_request_to_update, repository_id, pull_request_id, project=None):
        """UpdatePullRequest.
        Update a pull request
        :param :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>` git_pull_request_to_update: The pull request content that should be updated.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request to update.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(git_pull_request_to_update, 'GitPullRequest')
        response = self._send(http_method='PATCH',
                              location_id='9946fd70-0d40-406e-b686-b4744cbbcc37',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequest', response)

    def create_comment(self, comment, repository_id, pull_request_id, thread_id, project=None):
        """CreateComment.
        Create a comment on a specific thread in a pull request (up to 500 comments can be created per thread).
        :param :class:`<Comment> <azure.devops.v5_1.git.models.Comment>` comment: The comment to create. Comments can be up to 150,000 characters.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v5_1.git.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        content = self._serialize.body(comment, 'Comment')
        response = self._send(http_method='POST',
                              location_id='965a3ec7-5ed8-455a-bdcb-835a5ea7fe7b',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def delete_comment(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """DeleteComment.
        Delete a comment associated with a specific thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param int comment_id: ID of the comment.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='965a3ec7-5ed8-455a-bdcb-835a5ea7fe7b',
                   version='5.1',
                   route_values=route_values)

    def get_comment(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """GetComment.
        Retrieve a comment associated with a specific thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param int comment_id: ID of the comment.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v5_1.git.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='965a3ec7-5ed8-455a-bdcb-835a5ea7fe7b',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('Comment', response)

    def get_comments(self, repository_id, pull_request_id, thread_id, project=None):
        """GetComments.
        Retrieve all comments associated with a specific thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread.
        :param str project: Project ID or project name
        :rtype: [Comment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        response = self._send(http_method='GET',
                              location_id='965a3ec7-5ed8-455a-bdcb-835a5ea7fe7b',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[Comment]', self._unwrap_collection(response))

    def update_comment(self, comment, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """UpdateComment.
        Update a comment associated with a specific thread in a pull request.
        :param :class:`<Comment> <azure.devops.v5_1.git.models.Comment>` comment: The comment content that should be updated. Comments can be up to 150,000 characters.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param int comment_id: ID of the comment to update.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v5_1.git.models.Comment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        content = self._serialize.body(comment, 'Comment')
        response = self._send(http_method='PATCH',
                              location_id='965a3ec7-5ed8-455a-bdcb-835a5ea7fe7b',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def create_thread(self, comment_thread, repository_id, pull_request_id, project=None):
        """CreateThread.
        Create a thread in a pull request.
        :param :class:`<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>` comment_thread: The thread to create. Thread must contain at least one comment.
        :param str repository_id: Repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(comment_thread, 'GitPullRequestCommentThread')
        response = self._send(http_method='POST',
                              location_id='ab6e2e5d-a0b7-4153-b64a-a4efe0d49449',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_pull_request_thread(self, repository_id, pull_request_id, thread_id, project=None, iteration=None, base_iteration=None):
        """GetPullRequestThread.
        Retrieve a thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread.
        :param str project: Project ID or project name
        :param int iteration: If specified, thread position will be tracked using this iteration as the right side of the diff.
        :param int base_iteration: If specified, thread position will be tracked using this iteration as the left side of the diff.
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        query_parameters = {}
        if iteration is not None:
            query_parameters['$iteration'] = self._serialize.query('iteration', iteration, 'int')
        if base_iteration is not None:
            query_parameters['$baseIteration'] = self._serialize.query('base_iteration', base_iteration, 'int')
        response = self._send(http_method='GET',
                              location_id='ab6e2e5d-a0b7-4153-b64a-a4efe0d49449',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_threads(self, repository_id, pull_request_id, project=None, iteration=None, base_iteration=None):
        """GetThreads.
        Retrieve all threads in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param int iteration: If specified, thread positions will be tracked using this iteration as the right side of the diff.
        :param int base_iteration: If specified, thread positions will be tracked using this iteration as the left side of the diff.
        :rtype: [GitPullRequestCommentThread]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if iteration is not None:
            query_parameters['$iteration'] = self._serialize.query('iteration', iteration, 'int')
        if base_iteration is not None:
            query_parameters['$baseIteration'] = self._serialize.query('base_iteration', base_iteration, 'int')
        response = self._send(http_method='GET',
                              location_id='ab6e2e5d-a0b7-4153-b64a-a4efe0d49449',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequestCommentThread]', self._unwrap_collection(response))

    def update_thread(self, comment_thread, repository_id, pull_request_id, thread_id, project=None):
        """UpdateThread.
        Update a thread in a pull request.
        :param :class:`<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>` comment_thread: The thread content that should be updated.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread to update.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if thread_id is not None:
            route_values['threadId'] = self._serialize.url('thread_id', thread_id, 'int')
        content = self._serialize.body(comment_thread, 'GitPullRequestCommentThread')
        response = self._send(http_method='PATCH',
                              location_id='ab6e2e5d-a0b7-4153-b64a-a4efe0d49449',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_pull_request_work_item_refs(self, repository_id, pull_request_id, project=None):
        """GetPullRequestWorkItemRefs.
        Retrieve a list of work items associated with a pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0a637fcc-5370-4ce8-b0e8-98091f5f9482',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def create_push(self, push, repository_id, project=None):
        """CreatePush.
        Push changes to the repository.
        :param :class:`<GitPush> <azure.devops.v5_1.git.models.GitPush>` push:
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPush> <azure.devops.v5_1.git.models.GitPush>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(push, 'GitPush')
        response = self._send(http_method='POST',
                              location_id='ea98d07b-3c87-4971-8ede-a613694ffb55',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPush', response)

    def get_push(self, repository_id, push_id, project=None, include_commits=None, include_ref_updates=None):
        """GetPush.
        Retrieves a particular push.
        :param str repository_id: The name or ID of the repository.
        :param int push_id: ID of the push.
        :param str project: Project ID or project name
        :param int include_commits: The number of commits to include in the result.
        :param bool include_ref_updates: If true, include the list of refs that were updated by the push.
        :rtype: :class:`<GitPush> <azure.devops.v5_1.git.models.GitPush>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if push_id is not None:
            route_values['pushId'] = self._serialize.url('push_id', push_id, 'int')
        query_parameters = {}
        if include_commits is not None:
            query_parameters['includeCommits'] = self._serialize.query('include_commits', include_commits, 'int')
        if include_ref_updates is not None:
            query_parameters['includeRefUpdates'] = self._serialize.query('include_ref_updates', include_ref_updates, 'bool')
        response = self._send(http_method='GET',
                              location_id='ea98d07b-3c87-4971-8ede-a613694ffb55',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPush', response)

    def get_pushes(self, repository_id, project=None, skip=None, top=None, search_criteria=None):
        """GetPushes.
        Retrieves pushes associated with the specified repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param int skip: Number of pushes to skip.
        :param int top: Number of pushes to return.
        :param :class:`<GitPushSearchCriteria> <azure.devops.v5_1.git.models.GitPushSearchCriteria>` search_criteria: Search criteria attributes: fromDate, toDate, pusherId, refName, includeRefUpdates or includeLinks. fromDate: Start date to search from. toDate: End date to search to. pusherId: Identity of the person who submitted the push. refName: Branch name to consider. includeRefUpdates: If true, include the list of refs that were updated by the push. includeLinks: Whether to include the _links field on the shallow references.
        :rtype: [GitPush]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if search_criteria is not None:
            if search_criteria.from_date is not None:
                query_parameters['searchCriteria.fromDate'] = search_criteria.from_date
            if search_criteria.to_date is not None:
                query_parameters['searchCriteria.toDate'] = search_criteria.to_date
            if search_criteria.pusher_id is not None:
                query_parameters['searchCriteria.pusherId'] = search_criteria.pusher_id
            if search_criteria.ref_name is not None:
                query_parameters['searchCriteria.refName'] = search_criteria.ref_name
            if search_criteria.include_ref_updates is not None:
                query_parameters['searchCriteria.includeRefUpdates'] = search_criteria.include_ref_updates
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
        response = self._send(http_method='GET',
                              location_id='ea98d07b-3c87-4971-8ede-a613694ffb55',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPush]', self._unwrap_collection(response))

    def get_refs(self, repository_id, project=None, filter=None, include_links=None, include_statuses=None, include_my_branches=None, latest_statuses_only=None, peel_tags=None, filter_contains=None, top=None, continuation_token=None):
        """GetRefs.
        Queries the provided repository for its refs and returns them.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param str filter: [optional] A filter to apply to the refs (starts with).
        :param bool include_links: [optional] Specifies if referenceLinks should be included in the result. default is false.
        :param bool include_statuses: [optional] Includes up to the first 1000 commit statuses for each ref. The default value is false.
        :param bool include_my_branches: [optional] Includes only branches that the user owns, the branches the user favorites, and the default branch. The default value is false. Cannot be combined with the filter parameter.
        :param bool latest_statuses_only: [optional] True to include only the tip commit status for each ref. This option requires `includeStatuses` to be true. The default value is false.
        :param bool peel_tags: [optional] Annotated tags will populate the PeeledObjectId property. default is false.
        :param str filter_contains: [optional] A filter to apply to the refs (contains).
        :param int top: [optional] Maximum number of refs to return. It cannot be bigger than 1000. If it is not provided but continuationToken is, top will default to 100.
        :param str continuation_token: The continuation token used for pagination.
        :rtype: :class:`<GetRefsResponseValue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if filter is not None:
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        if include_statuses is not None:
            query_parameters['includeStatuses'] = self._serialize.query('include_statuses', include_statuses, 'bool')
        if include_my_branches is not None:
            query_parameters['includeMyBranches'] = self._serialize.query('include_my_branches', include_my_branches, 'bool')
        if latest_statuses_only is not None:
            query_parameters['latestStatusesOnly'] = self._serialize.query('latest_statuses_only', latest_statuses_only, 'bool')
        if peel_tags is not None:
            query_parameters['peelTags'] = self._serialize.query('peel_tags', peel_tags, 'bool')
        if filter_contains is not None:
            query_parameters['filterContains'] = self._serialize.query('filter_contains', filter_contains, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='2d874a60-a811-4f62-9c9f-963a6ea0a55b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[GitRef]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetRefsResponseValue(response_value, continuation_token)

    class GetRefsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_refs method

            :param value:
            :type value: :class:`<[GitRef]> <azure.devops.v5_1.git.models.[GitRef]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def update_ref(self, new_ref_info, repository_id, filter, project=None, project_id=None):
        """UpdateRef.
        Lock or Unlock a branch.
        :param :class:`<GitRefUpdate> <azure.devops.v5_1.git.models.GitRefUpdate>` new_ref_info: The ref update action (lock/unlock) to perform
        :param str repository_id: The name or ID of the repository.
        :param str filter: The name of the branch to lock/unlock
        :param str project: Project ID or project name
        :param str project_id: ID or name of the team project. Optional if specifying an ID for repository.
        :rtype: :class:`<GitRef> <azure.devops.v5_1.git.models.GitRef>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if filter is not None:
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        content = self._serialize.body(new_ref_info, 'GitRefUpdate')
        response = self._send(http_method='PATCH',
                              location_id='2d874a60-a811-4f62-9c9f-963a6ea0a55b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitRef', response)

    def update_refs(self, ref_updates, repository_id, project=None, project_id=None):
        """UpdateRefs.
        Creating, updating, or deleting refs(branches).
        :param [GitRefUpdate] ref_updates: List of ref updates to attempt to perform
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param str project_id: ID or name of the team project. Optional if specifying an ID for repository.
        :rtype: [GitRefUpdateResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        content = self._serialize.body(ref_updates, '[GitRefUpdate]')
        response = self._send(http_method='POST',
                              location_id='2d874a60-a811-4f62-9c9f-963a6ea0a55b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[GitRefUpdateResult]', self._unwrap_collection(response))

    def create_repository(self, git_repository_to_create, project=None, source_ref=None):
        """CreateRepository.
        Create a git repository in a team project.
        :param :class:`<GitRepositoryCreateOptions> <azure.devops.v5_1.git.models.GitRepositoryCreateOptions>` git_repository_to_create: Specify the repo name, team project and/or parent repository. Team project information can be omitted from gitRepositoryToCreate if the request is project-scoped (i.e., includes project Id).
        :param str project: Project ID or project name
        :param str source_ref: [optional] Specify the source refs to use while creating a fork repo
        :rtype: :class:`<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if source_ref is not None:
            query_parameters['sourceRef'] = self._serialize.query('source_ref', source_ref, 'str')
        content = self._serialize.body(git_repository_to_create, 'GitRepositoryCreateOptions')
        response = self._send(http_method='POST',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitRepository', response)

    def delete_repository(self, repository_id, project=None):
        """DeleteRepository.
        Delete a git repository
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        self._send(http_method='DELETE',
                   location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                   version='5.1',
                   route_values=route_values)

    def get_repositories(self, project=None, include_links=None, include_all_urls=None, include_hidden=None):
        """GetRepositories.
        Retrieve git repositories.
        :param str project: Project ID or project name
        :param bool include_links: [optional] True to include reference links. The default value is false.
        :param bool include_all_urls: [optional] True to include all remote URLs. The default value is false.
        :param bool include_hidden: [optional] True to include hidden repositories. The default value is false.
        :rtype: [GitRepository]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        if include_all_urls is not None:
            query_parameters['includeAllUrls'] = self._serialize.query('include_all_urls', include_all_urls, 'bool')
        if include_hidden is not None:
            query_parameters['includeHidden'] = self._serialize.query('include_hidden', include_hidden, 'bool')
        response = self._send(http_method='GET',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitRepository]', self._unwrap_collection(response))

    def get_repository(self, repository_id, project=None):
        """GetRepository.
        Retrieve a git repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('GitRepository', response)

    def get_repository_with_parent(self, repository_id, include_parent, project=None):
        """GetRepositoryWithParent.
        Retrieve a git repository.
        :param str repository_id: The name or ID of the repository.
        :param bool include_parent: True to include parent repository. Only available in authenticated calls.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if include_parent is not None:
            query_parameters['includeParent'] = self._serialize.query('include_parent', include_parent, 'bool')
        response = self._send(http_method='GET',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitRepository', response)

    def update_repository(self, new_repository_info, repository_id, project=None):
        """UpdateRepository.
        Updates the Git repository with either a new repo name or a new default branch.
        :param :class:`<GitRepository> <azure.devops.v5_1.git.models.GitRepository>` new_repository_info: Specify a new repo name or a new default branch of the repository
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(new_repository_info, 'GitRepository')
        response = self._send(http_method='PATCH',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitRepository', response)

    def create_commit_status(self, git_commit_status_to_create, commit_id, repository_id, project=None):
        """CreateCommitStatus.
        Create Git commit status.
        :param :class:`<GitStatus> <azure.devops.v5_1.git.models.GitStatus>` git_commit_status_to_create: Git commit status object to create.
        :param str commit_id: ID of the Git commit.
        :param str repository_id: ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitStatus> <azure.devops.v5_1.git.models.GitStatus>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if commit_id is not None:
            route_values['commitId'] = self._serialize.url('commit_id', commit_id, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(git_commit_status_to_create, 'GitStatus')
        response = self._send(http_method='POST',
                              location_id='428dd4fb-fda5-4722-af02-9313b80305da',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitStatus', response)

    def get_statuses(self, commit_id, repository_id, project=None, top=None, skip=None, latest_only=None):
        """GetStatuses.
        Get statuses associated with the Git commit.
        :param str commit_id: ID of the Git commit.
        :param str repository_id: ID of the repository.
        :param str project: Project ID or project name
        :param int top: Optional. The number of statuses to retrieve. Default is 1000.
        :param int skip: Optional. The number of statuses to ignore. Default is 0. For example, to retrieve results 101-150, set top to 50 and skip to 100.
        :param bool latest_only: The flag indicates whether to get only latest statuses grouped by `Context.Name` and `Context.Genre`.
        :rtype: [GitStatus]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if commit_id is not None:
            route_values['commitId'] = self._serialize.url('commit_id', commit_id, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['skip'] = self._serialize.query('skip', skip, 'int')
        if latest_only is not None:
            query_parameters['latestOnly'] = self._serialize.query('latest_only', latest_only, 'bool')
        response = self._send(http_method='GET',
                              location_id='428dd4fb-fda5-4722-af02-9313b80305da',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitStatus]', self._unwrap_collection(response))

    def get_tree(self, repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None):
        """GetTree.
        The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
        :param str repository_id: Repository Id.
        :param str sha1: SHA1 hash of the tree object.
        :param str project: Project ID or project name
        :param str project_id: Project Id.
        :param bool recursive: Search recursively. Include trees underneath this tree. Default is false.
        :param str file_name: Name to use if a .zip file is returned. Default is the object ID.
        :rtype: :class:`<GitTreeRef> <azure.devops.v5_1.git.models.GitTreeRef>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if sha1 is not None:
            route_values['sha1'] = self._serialize.url('sha1', sha1, 'str')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        if recursive is not None:
            query_parameters['recursive'] = self._serialize.query('recursive', recursive, 'bool')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='729f6437-6f92-44ec-8bee-273a7111063c',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitTreeRef', response)

    def get_tree_zip(self, repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None, **kwargs):
        """GetTreeZip.
        The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
        :param str repository_id: Repository Id.
        :param str sha1: SHA1 hash of the tree object.
        :param str project: Project ID or project name
        :param str project_id: Project Id.
        :param bool recursive: Search recursively. Include trees underneath this tree. Default is false.
        :param str file_name: Name to use if a .zip file is returned. Default is the object ID.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if sha1 is not None:
            route_values['sha1'] = self._serialize.url('sha1', sha1, 'str')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        if recursive is not None:
            query_parameters['recursive'] = self._serialize.query('recursive', recursive, 'bool')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='729f6437-6f92-44ec-8bee-273a7111063c',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

