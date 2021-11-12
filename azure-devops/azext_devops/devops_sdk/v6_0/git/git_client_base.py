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

    def create_annotated_tag(self, tag_object, project, repository_id):
        """CreateAnnotatedTag.
        [Preview API] Create an annotated tag.
        :param :class:`<GitAnnotatedTag> <azure.devops.v6_0.git.models.GitAnnotatedTag>` tag_object: Object containing details of tag to be created.
        :param str project: Project ID or project name
        :param str repository_id: ID or name of the repository.
        :rtype: :class:`<GitAnnotatedTag> <azure.devops.v6_0.git.models.GitAnnotatedTag>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(tag_object, 'GitAnnotatedTag')
        response = self._send(http_method='POST',
                              location_id='5e8a8081-3851-4626-b677-9891cc04102e',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitAnnotatedTag', response)

    def get_annotated_tag(self, project, repository_id, object_id):
        """GetAnnotatedTag.
        [Preview API] Get an annotated tag.
        :param str project: Project ID or project name
        :param str repository_id: ID or name of the repository.
        :param str object_id: ObjectId (Sha1Id) of tag to get.
        :rtype: :class:`<GitAnnotatedTag> <azure.devops.v6_0.git.models.GitAnnotatedTag>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if object_id is not None:
            route_values['objectId'] = self._serialize.url('object_id', object_id, 'str')
        response = self._send(http_method='GET',
                              location_id='5e8a8081-3851-4626-b677-9891cc04102e',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitAnnotatedTag', response)

    def get_blob(self, repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None):
        """GetBlob.
        [Preview API] Get a single blob.
        :param str repository_id: The name or ID of the repository.
        :param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.
        :param str project: Project ID or project name
        :param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip
        :param str file_name: Provide a fileName to use for a download.
        :param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types
        :rtype: :class:`<GitBlobRef> <azure.devops.v6_0.git.models.GitBlobRef>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitBlobRef', response)

    def get_blob_content(self, repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs):
        """GetBlobContent.
        [Preview API] Get a single blob.
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
                              version='6.0-preview.1',
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
        [Preview API] Gets one or more blobs in a zip file download.
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
                              version='6.0-preview.1',
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
        [Preview API] Get a single blob.
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
                              version='6.0-preview.1',
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
        [Preview API] Retrieve statistics about a single branch.
        :param str repository_id: The name or ID of the repository.
        :param str name: Name of the branch.
        :param str project: Project ID or project name
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` base_version_descriptor: Identifies the commit or branch to use as the base.
        :rtype: :class:`<GitBranchStats> <azure.devops.v6_0.git.models.GitBranchStats>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitBranchStats', response)

    def get_branches(self, repository_id, project=None, base_version_descriptor=None):
        """GetBranches.
        [Preview API] Retrieve statistics about all branches within a repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` base_version_descriptor: Identifies the commit or branch to use as the base.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitBranchStats]', self._unwrap_collection(response))

    def get_changes(self, commit_id, repository_id, project=None, top=None, skip=None):
        """GetChanges.
        [Preview API] Retrieve changes for a particular commit.
        :param str commit_id: The id of the commit.
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param str project: Project ID or project name
        :param int top: The maximum number of changes to return.
        :param int skip: The number of changes to skip.
        :rtype: :class:`<GitCommitChanges> <azure.devops.v6_0.git.models.GitCommitChanges>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommitChanges', response)

    def create_cherry_pick(self, cherry_pick_to_create, project, repository_id):
        """CreateCherryPick.
        [Preview API] Cherry pick a specific commit or commits that are associated to a pull request into a new branch.
        :param :class:`<GitAsyncRefOperationParameters> <azure.devops.v6_0.git.models.GitAsyncRefOperationParameters>` cherry_pick_to_create:
        :param str project: Project ID or project name
        :param str repository_id: ID of the repository.
        :rtype: :class:`<GitCherryPick> <azure.devops.v6_0.git.models.GitCherryPick>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(cherry_pick_to_create, 'GitAsyncRefOperationParameters')
        response = self._send(http_method='POST',
                              location_id='033bad68-9a14-43d1-90e0-59cb8856fef6',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitCherryPick', response)

    def get_cherry_pick(self, project, cherry_pick_id, repository_id):
        """GetCherryPick.
        [Preview API] Retrieve information about a cherry pick operation by cherry pick Id.
        :param str project: Project ID or project name
        :param int cherry_pick_id: ID of the cherry pick.
        :param str repository_id: ID of the repository.
        :rtype: :class:`<GitCherryPick> <azure.devops.v6_0.git.models.GitCherryPick>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if cherry_pick_id is not None:
            route_values['cherryPickId'] = self._serialize.url('cherry_pick_id', cherry_pick_id, 'int')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='033bad68-9a14-43d1-90e0-59cb8856fef6',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitCherryPick', response)

    def get_cherry_pick_for_ref_name(self, project, repository_id, ref_name):
        """GetCherryPickForRefName.
        [Preview API] Retrieve information about a cherry pick operation for a specific branch. This operation is expensive due to the underlying object structure, so this API only looks at the 1000 most recent cherry pick operations.
        :param str project: Project ID or project name
        :param str repository_id: ID of the repository.
        :param str ref_name: The GitAsyncRefOperationParameters generatedRefName used for the cherry pick operation.
        :rtype: :class:`<GitCherryPick> <azure.devops.v6_0.git.models.GitCherryPick>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if ref_name is not None:
            query_parameters['refName'] = self._serialize.query('ref_name', ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='033bad68-9a14-43d1-90e0-59cb8856fef6',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCherryPick', response)

    def get_commit_diffs(self, repository_id, project=None, diff_common_commit=None, top=None, skip=None, base_version_descriptor=None, target_version_descriptor=None):
        """GetCommitDiffs.
        [Preview API] Find the closest common commit (the merge base) between base and target commits, and get the diff between either the base and target commits or common and target commits.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param bool diff_common_commit: If true, diff between common and target commits. If false, diff between base and target commits.
        :param int top: Maximum number of changes to return. Defaults to 100.
        :param int skip: Number of changes to skip
        :param :class:`<GitBaseVersionDescriptor> <azure.devops.v6_0.git.models.GitBaseVersionDescriptor>` base_version_descriptor: Descriptor for base commit.
        :param :class:`<GitTargetVersionDescriptor> <azure.devops.v6_0.git.models.GitTargetVersionDescriptor>` target_version_descriptor: Descriptor for target commit.
        :rtype: :class:`<GitCommitDiffs> <azure.devops.v6_0.git.models.GitCommitDiffs>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommitDiffs', response)

    def get_commit(self, commit_id, repository_id, project=None, change_count=None):
        """GetCommit.
        [Preview API] Retrieve a particular commit.
        :param str commit_id: The id of the commit.
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param str project: Project ID or project name
        :param int change_count: The number of changes to include in the result.
        :rtype: :class:`<GitCommit> <azure.devops.v6_0.git.models.GitCommit>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitCommit', response)

    def get_commits(self, repository_id, search_criteria, project=None, skip=None, top=None):
        """GetCommits.
        [Preview API] Retrieve git commits for a project
        :param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.
        :param :class:`<GitQueryCommitsCriteria> <azure.devops.v6_0.git.models.GitQueryCommitsCriteria>` search_criteria:
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
            if search_criteria.show_oldest_commits_first is not None:
                query_parameters['searchCriteria.showOldestCommitsFirst'] = search_criteria.show_oldest_commits_first
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='c2570c3b-5b3f-41b8-98bf-5407bfde8d58',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_push_commits(self, repository_id, push_id, project=None, top=None, skip=None, include_links=None):
        """GetPushCommits.
        [Preview API] Retrieve a list of commits associated with a particular push.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_commits_batch(self, search_criteria, repository_id, project=None, skip=None, top=None, include_statuses=None):
        """GetCommitsBatch.
        [Preview API] Retrieve git commits for a project matching the search criteria
        :param :class:`<GitQueryCommitsCriteria> <azure.devops.v6_0.git.models.GitQueryCommitsCriteria>` search_criteria: Search options
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_deleted_repositories(self, project):
        """GetDeletedRepositories.
        [Preview API] Retrieve deleted git repositories.
        :param str project: Project ID or project name
        :rtype: [GitDeletedRepository]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='2b6869c4-cb25-42b5-b7a3-0d3e6be0a11a',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[GitDeletedRepository]', self._unwrap_collection(response))

    def get_forks(self, repository_name_or_id, collection_id, project=None, include_links=None):
        """GetForks.
        [Preview API] Retrieve all forks of a repository in the collection.
        :param str repository_name_or_id: The name or ID of the repository.
        :param str collection_id: Team project collection ID.
        :param str project: Project ID or project name
        :param bool include_links: True to include links.
        :rtype: [GitRepositoryRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        if collection_id is not None:
            route_values['collectionId'] = self._serialize.url('collection_id', collection_id, 'str')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='158c0340-bf6f-489c-9625-d572a1480d57',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitRepositoryRef]', self._unwrap_collection(response))

    def create_fork_sync_request(self, sync_params, repository_name_or_id, project=None, include_links=None):
        """CreateForkSyncRequest.
        [Preview API] Request that another repository's refs be fetched into this one. It syncs two existing forks. To create a fork, please see the <a href="https://docs.microsoft.com/en-us/rest/api/vsts/git/repositories/create?view=azure-devops-rest-5.1"> repositories endpoint</a>
        :param :class:`<GitForkSyncRequestParameters> <azure.devops.v6_0.git.models.GitForkSyncRequestParameters>` sync_params: Source repository and ref mapping.
        :param str repository_name_or_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param bool include_links: True to include links
        :rtype: :class:`<GitForkSyncRequest> <azure.devops.v6_0.git.models.GitForkSyncRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        content = self._serialize.body(sync_params, 'GitForkSyncRequestParameters')
        response = self._send(http_method='POST',
                              location_id='1703f858-b9d1-46af-ab62-483e9e1055b5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitForkSyncRequest', response)

    def get_fork_sync_request(self, repository_name_or_id, fork_sync_operation_id, project=None, include_links=None):
        """GetForkSyncRequest.
        [Preview API] Get a specific fork sync operation's details.
        :param str repository_name_or_id: The name or ID of the repository.
        :param int fork_sync_operation_id: OperationId of the sync request.
        :param str project: Project ID or project name
        :param bool include_links: True to include links.
        :rtype: :class:`<GitForkSyncRequest> <azure.devops.v6_0.git.models.GitForkSyncRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        if fork_sync_operation_id is not None:
            route_values['forkSyncOperationId'] = self._serialize.url('fork_sync_operation_id', fork_sync_operation_id, 'int')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='1703f858-b9d1-46af-ab62-483e9e1055b5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitForkSyncRequest', response)

    def get_fork_sync_requests(self, repository_name_or_id, project=None, include_abandoned=None, include_links=None):
        """GetForkSyncRequests.
        [Preview API] Retrieve all requested fork sync operations on this repository.
        :param str repository_name_or_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param bool include_abandoned: True to include abandoned requests.
        :param bool include_links: True to include links.
        :rtype: [GitForkSyncRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        query_parameters = {}
        if include_abandoned is not None:
            query_parameters['includeAbandoned'] = self._serialize.query('include_abandoned', include_abandoned, 'bool')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='1703f858-b9d1-46af-ab62-483e9e1055b5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitForkSyncRequest]', self._unwrap_collection(response))

    def create_import_request(self, import_request, project, repository_id):
        """CreateImportRequest.
        [Preview API] Create an import request.
        :param :class:`<GitImportRequest> <azure.devops.v6_0.git.models.GitImportRequest>` import_request: The import request to create.
        :param str project: Project ID or project name
        :param str repository_id: The name or ID of the repository.
        :rtype: :class:`<GitImportRequest> <azure.devops.v6_0.git.models.GitImportRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(import_request, 'GitImportRequest')
        response = self._send(http_method='POST',
                              location_id='01828ddc-3600-4a41-8633-99b3a73a0eb3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitImportRequest', response)

    def get_import_request(self, project, repository_id, import_request_id):
        """GetImportRequest.
        [Preview API] Retrieve a particular import request.
        :param str project: Project ID or project name
        :param str repository_id: The name or ID of the repository.
        :param int import_request_id: The unique identifier for the import request.
        :rtype: :class:`<GitImportRequest> <azure.devops.v6_0.git.models.GitImportRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if import_request_id is not None:
            route_values['importRequestId'] = self._serialize.url('import_request_id', import_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='01828ddc-3600-4a41-8633-99b3a73a0eb3',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitImportRequest', response)

    def query_import_requests(self, project, repository_id, include_abandoned=None):
        """QueryImportRequests.
        [Preview API] Retrieve import requests for a repository.
        :param str project: Project ID or project name
        :param str repository_id: The name or ID of the repository.
        :param bool include_abandoned: True to include abandoned import requests in the results.
        :rtype: [GitImportRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if include_abandoned is not None:
            query_parameters['includeAbandoned'] = self._serialize.query('include_abandoned', include_abandoned, 'bool')
        response = self._send(http_method='GET',
                              location_id='01828ddc-3600-4a41-8633-99b3a73a0eb3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitImportRequest]', self._unwrap_collection(response))

    def update_import_request(self, import_request_to_update, project, repository_id, import_request_id):
        """UpdateImportRequest.
        [Preview API] Retry or abandon a failed import request.
        :param :class:`<GitImportRequest> <azure.devops.v6_0.git.models.GitImportRequest>` import_request_to_update: The updated version of the import request. Currently, the only change allowed is setting the Status to Queued or Abandoned.
        :param str project: Project ID or project name
        :param str repository_id: The name or ID of the repository.
        :param int import_request_id: The unique identifier for the import request to update.
        :rtype: :class:`<GitImportRequest> <azure.devops.v6_0.git.models.GitImportRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if import_request_id is not None:
            route_values['importRequestId'] = self._serialize.url('import_request_id', import_request_id, 'int')
        content = self._serialize.body(import_request_to_update, 'GitImportRequest')
        response = self._send(http_method='PATCH',
                              location_id='01828ddc-3600-4a41-8633-99b3a73a0eb3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitImportRequest', response)

    def get_item(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, sanitize=None):
        """GetItem.
        [Preview API] Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :param bool sanitize: Set to true to sanitize an svg file and return it as image. Useful only if requested for svg file. Default is false.
        :rtype: :class:`<GitItem> <azure.devops.v6_0.git.models.GitItem>`
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
        if sanitize is not None:
            query_parameters['sanitize'] = self._serialize.query('sanitize', sanitize, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitItem', response)

    def get_item_content(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, sanitize=None, **kwargs):
        """GetItemContent.
        [Preview API] Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :param bool sanitize: Set to true to sanitize an svg file and return it as image. Useful only if requested for svg file. Default is false.
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
        if sanitize is not None:
            query_parameters['sanitize'] = self._serialize.query('sanitize', sanitize, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='6.0-preview.1',
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
        [Preview API] Get Item Metadata and/or Content for a collection of items. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param bool include_links: Set to true to include links to items.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitItem]', self._unwrap_collection(response))

    def get_item_text(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, sanitize=None, **kwargs):
        """GetItemText.
        [Preview API] Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :param bool sanitize: Set to true to sanitize an svg file and return it as image. Useful only if requested for svg file. Default is false.
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
        if sanitize is not None:
            query_parameters['sanitize'] = self._serialize.query('sanitize', sanitize, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_item_zip(self, repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, sanitize=None, **kwargs):
        """GetItemZip.
        [Preview API] Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
        :param str repository_id: The name or ID of the repository.
        :param str path: The item path.
        :param str project: Project ID or project name
        :param str scope_path: The path scope.  The default is null.
        :param str recursion_level: The recursion level of this request. The default is 'none', no recursion.
        :param bool include_content_metadata: Set to true to include content metadata.  Default is false.
        :param bool latest_processed_change: Set to true to include the latest changes.  Default is false.
        :param bool download: Set to true to download the response as a file.  Default is false.
        :param :class:`<GitVersionDescriptor> <azure.devops.v6_0.git.models.GitVersionDescriptor>` version_descriptor: Version descriptor.  Default is the default branch for the repository.
        :param bool include_content: Set to true to include item content when requesting json.  Default is false.
        :param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.
        :param bool sanitize: Set to true to sanitize an svg file and return it as image. Useful only if requested for svg file. Default is false.
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
        if sanitize is not None:
            query_parameters['sanitize'] = self._serialize.query('sanitize', sanitize, 'bool')
        response = self._send(http_method='GET',
                              location_id='fb93c0db-47ed-4a31-8c20-47552878fb44',
                              version='6.0-preview.1',
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
        [Preview API] Post for retrieving a creating a batch out of a set of items in a repo / project given a list of paths or a long path
        :param :class:`<GitItemRequestData> <azure.devops.v6_0.git.models.GitItemRequestData>` request_data: Request data attributes: ItemDescriptors, IncludeContentMetadata, LatestProcessedChange, IncludeLinks. ItemDescriptors: Collection of items to fetch, including path, version, and recursion level. IncludeContentMetadata: Whether to include metadata for all items LatestProcessedChange: Whether to include shallow ref to commit that last changed each item. IncludeLinks: Whether to include the _links field on the shallow references.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[[GitItem]]', self._unwrap_collection(response))

    def get_merge_bases(self, repository_name_or_id, commit_id, other_commit_id, project=None, other_collection_id=None, other_repository_id=None):
        """GetMergeBases.
        [Preview API] Find the merge bases of two commits, optionally across forks. If otherRepositoryId is not specified, the merge bases will only be calculated within the context of the local repositoryNameOrId.
        :param str repository_name_or_id: ID or name of the local repository.
        :param str commit_id: First commit, usually the tip of the target branch of the potential merge.
        :param str other_commit_id: Other commit, usually the tip of the source branch of the potential merge.
        :param str project: Project ID or project name
        :param str other_collection_id: The collection ID where otherCommitId lives.
        :param str other_repository_id: The repository ID where otherCommitId lives.
        :rtype: [GitCommitRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        if commit_id is not None:
            route_values['commitId'] = self._serialize.url('commit_id', commit_id, 'str')
        query_parameters = {}
        if other_commit_id is not None:
            query_parameters['otherCommitId'] = self._serialize.query('other_commit_id', other_commit_id, 'str')
        if other_collection_id is not None:
            query_parameters['otherCollectionId'] = self._serialize.query('other_collection_id', other_collection_id, 'str')
        if other_repository_id is not None:
            query_parameters['otherRepositoryId'] = self._serialize.query('other_repository_id', other_repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='7cf2abb6-c964-4f7e-9872-f78c66e72e9c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def create_merge_request(self, merge_parameters, project, repository_name_or_id, include_links=None):
        """CreateMergeRequest.
        [Preview API] Request a git merge operation. Currently we support merging only 2 commits.
        :param :class:`<GitMergeParameters> <azure.devops.v6_0.git.models.GitMergeParameters>` merge_parameters: Parents commitIds and merge commit messsage.
        :param str project: Project ID or project name
        :param str repository_name_or_id: The name or ID of the repository.
        :param bool include_links: True to include links
        :rtype: :class:`<GitMerge> <azure.devops.v6_0.git.models.GitMerge>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        content = self._serialize.body(merge_parameters, 'GitMergeParameters')
        response = self._send(http_method='POST',
                              location_id='985f7ae9-844f-4906-9897-7ef41516c0e2',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitMerge', response)

    def get_merge_request(self, project, repository_name_or_id, merge_operation_id, include_links=None):
        """GetMergeRequest.
        [Preview API] Get a specific merge operation's details.
        :param str project: Project ID or project name
        :param str repository_name_or_id: The name or ID of the repository.
        :param int merge_operation_id: OperationId of the merge request.
        :param bool include_links: True to include links
        :rtype: :class:`<GitMerge> <azure.devops.v6_0.git.models.GitMerge>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_name_or_id is not None:
            route_values['repositoryNameOrId'] = self._serialize.url('repository_name_or_id', repository_name_or_id, 'str')
        if merge_operation_id is not None:
            route_values['mergeOperationId'] = self._serialize.url('merge_operation_id', merge_operation_id, 'int')
        query_parameters = {}
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='985f7ae9-844f-4906-9897-7ef41516c0e2',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitMerge', response)

    def get_policy_configurations(self, project, repository_id=None, ref_name=None, policy_type=None, top=None, continuation_token=None):
        """GetPolicyConfigurations.
        [Preview API] Retrieve a list of policy configurations by a given set of scope/filtering criteria.
        :param str project: Project ID or project name
        :param str repository_id: The repository id.
        :param str ref_name: The fully-qualified Git ref name (e.g. refs/heads/master).
        :param str policy_type: The policy type filter.
        :param int top: Maximum number of policies to return.
        :param str continuation_token: Pass a policy configuration ID to fetch the next page of results, up to top number of results, for this endpoint.
        :rtype: :class:`<GitPolicyConfigurationResponse> <azure.devops.v6_0.git.models.GitPolicyConfigurationResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if ref_name is not None:
            query_parameters['refName'] = self._serialize.query('ref_name', ref_name, 'str')
        if policy_type is not None:
            query_parameters['policyType'] = self._serialize.query('policy_type', policy_type, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='2c420070-a0a2-49cc-9639-c9f271c5ff07',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.GitPolicyConfigurationResponse()
        response_object.policy_configurations = self._deserialize('[PolicyConfiguration]', self._unwrap_collection(response))
        response_object.continuation_token = response.headers.get('x-ms-continuationtoken')
        return response_object

    def create_attachment(self, upload_stream, file_name, repository_id, pull_request_id, project=None, **kwargs):
        """CreateAttachment.
        [Preview API] Attach a new file to a pull request.
        :param object upload_stream: Stream to upload
        :param str file_name: The name of the file.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<Attachment> <azure.devops.v6_0.git.models.Attachment>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='965d9361-878b-413b-a494-45d5b5fd8ab7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('Attachment', response)

    def delete_attachment(self, file_name, repository_id, pull_request_id, project=None):
        """DeleteAttachment.
        [Preview API] Delete a pull request attachment.
        :param str file_name: The name of the attachment to delete.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        self._send(http_method='DELETE',
                   location_id='965d9361-878b-413b-a494-45d5b5fd8ab7',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_attachment_content(self, file_name, repository_id, pull_request_id, project=None, **kwargs):
        """GetAttachmentContent.
        [Preview API] Get the file content of a pull request attachment.
        :param str file_name: The name of the attachment.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='965d9361-878b-413b-a494-45d5b5fd8ab7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachments(self, repository_id, pull_request_id, project=None):
        """GetAttachments.
        [Preview API] Get a list of files attached to a given pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: [Attachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='965d9361-878b-413b-a494-45d5b5fd8ab7',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[Attachment]', self._unwrap_collection(response))

    def get_attachment_zip(self, file_name, repository_id, pull_request_id, project=None, **kwargs):
        """GetAttachmentZip.
        [Preview API] Get the file content of a pull request attachment.
        :param str file_name: The name of the attachment.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='965d9361-878b-413b-a494-45d5b5fd8ab7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_like(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """CreateLike.
        [Preview API] Add a like on a comment.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: The ID of the thread that contains the comment.
        :param int comment_id: The ID of the comment.
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
        self._send(http_method='POST',
                   location_id='5f2e2851-1389-425b-a00b-fb2adb3ef31b',
                   version='6.0-preview.1',
                   route_values=route_values)

    def delete_like(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """DeleteLike.
        [Preview API] Delete a like on a comment.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: The ID of the thread that contains the comment.
        :param int comment_id: The ID of the comment.
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
                   location_id='5f2e2851-1389-425b-a00b-fb2adb3ef31b',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_likes(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """GetLikes.
        [Preview API] Get likes for a comment.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: The ID of the thread that contains the comment.
        :param int comment_id: The ID of the comment.
        :param str project: Project ID or project name
        :rtype: [IdentityRef]
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
                              location_id='5f2e2851-1389-425b-a00b-fb2adb3ef31b',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[IdentityRef]', self._unwrap_collection(response))

    def get_pull_request_iteration_commits(self, repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None):
        """GetPullRequestIterationCommits.
        [Preview API] Get the commits for the specified iteration of a pull request.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_pull_request_commits(self, repository_id, pull_request_id, project=None, top=None, continuation_token=None):
        """GetPullRequestCommits.
        [Preview API] Get the commits for the specified pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param int top: Maximum number of commits to return.
        :param str continuation_token: The continuation token used for pagination.
        :rtype: :class:`<[GitCommitRef]> <azure.devops.v6_0.git.models.[GitCommitRef]>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitCommitRef]', self._unwrap_collection(response))

    def get_pull_request_iteration_changes(self, repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None, compare_to=None):
        """GetPullRequestIterationChanges.
        [Preview API] Retrieve the changes made in a pull request between two iterations.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration. <br /> Iteration IDs are zero-based with zero indicating the common commit between the source and target branches. Iteration one is the head of the source branch at the time the pull request is created and subsequent iterations are created when there are pushes to the source branch.
        :param str project: Project ID or project name
        :param int top: Optional. The number of changes to retrieve.  The default value is 100 and the maximum value is 2000.
        :param int skip: Optional. The number of changes to ignore.  For example, to retrieve changes 101-150, set top 50 and skip to 100.
        :param int compare_to: ID of the pull request iteration to compare against.  The default value is zero which indicates the comparison is made against the common commit between the source and target branches
        :rtype: :class:`<GitPullRequestIterationChanges> <azure.devops.v6_0.git.models.GitPullRequestIterationChanges>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequestIterationChanges', response)

    def get_pull_request_iteration(self, repository_id, pull_request_id, iteration_id, project=None):
        """GetPullRequestIteration.
        [Preview API] Get the specified iteration for a pull request.
        :param str repository_id: ID or name of the repository.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration to return.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestIteration> <azure.devops.v6_0.git.models.GitPullRequestIteration>`
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequestIteration', response)

    def get_pull_request_iterations(self, repository_id, pull_request_id, project=None, include_commits=None):
        """GetPullRequestIterations.
        [Preview API] Get the list of iterations for the specified pull request.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequestIteration]', self._unwrap_collection(response))

    def create_pull_request_iteration_status(self, status, repository_id, pull_request_id, iteration_id, project=None):
        """CreatePullRequestIterationStatus.
        [Preview API] Create a pull request status on the iteration. This operation will have the same result as Create status on pull request with specified iteration ID in the request body.
        :param :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>` status: Pull request status to create.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>`
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
        content = self._serialize.body(status, 'GitPullRequestStatus')
        response = self._send(http_method='POST',
                              location_id='75cf11c5-979f-4038-a76e-058a06adf2bf',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestStatus', response)

    def delete_pull_request_iteration_status(self, repository_id, pull_request_id, iteration_id, status_id, project=None):
        """DeletePullRequestIterationStatus.
        [Preview API] Delete pull request iteration status.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration.
        :param int status_id: ID of the pull request status.
        :param str project: Project ID or project name
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
        if status_id is not None:
            route_values['statusId'] = self._serialize.url('status_id', status_id, 'int')
        self._send(http_method='DELETE',
                   location_id='75cf11c5-979f-4038-a76e-058a06adf2bf',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_pull_request_iteration_status(self, repository_id, pull_request_id, iteration_id, status_id, project=None):
        """GetPullRequestIterationStatus.
        [Preview API] Get the specific pull request iteration status by ID. The status ID is unique within the pull request across all iterations.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration.
        :param int status_id: ID of the pull request status.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>`
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
        if status_id is not None:
            route_values['statusId'] = self._serialize.url('status_id', status_id, 'int')
        response = self._send(http_method='GET',
                              location_id='75cf11c5-979f-4038-a76e-058a06adf2bf',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequestStatus', response)

    def get_pull_request_iteration_statuses(self, repository_id, pull_request_id, iteration_id, project=None):
        """GetPullRequestIterationStatuses.
        [Preview API] Get all the statuses associated with a pull request iteration.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration.
        :param str project: Project ID or project name
        :rtype: [GitPullRequestStatus]
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
                              location_id='75cf11c5-979f-4038-a76e-058a06adf2bf',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[GitPullRequestStatus]', self._unwrap_collection(response))

    def update_pull_request_iteration_statuses(self, patch_document, repository_id, pull_request_id, iteration_id, project=None):
        """UpdatePullRequestIterationStatuses.
        [Preview API] Update pull request iteration statuses collection. The only supported operation type is `remove`.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v6_0.git.models.[JsonPatchOperation]>` patch_document: Operations to apply to the pull request statuses in JSON Patch format.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int iteration_id: ID of the pull request iteration.
        :param str project: Project ID or project name
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
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        self._send(http_method='PATCH',
                   location_id='75cf11c5-979f-4038-a76e-058a06adf2bf',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content,
                   media_type='application/json-patch+json')

    def create_pull_request_label(self, label, repository_id, pull_request_id, project=None, project_id=None):
        """CreatePullRequestLabel.
        [Preview API] Create a label for a specified pull request. The only required field is the name of the new label.
        :param :class:`<WebApiCreateTagRequestData> <azure.devops.v6_0.git.models.WebApiCreateTagRequestData>` label: Label to assign to the pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param str project_id: Project ID or project name.
        :rtype: :class:`<WebApiTagDefinition> <azure.devops.v6_0.git.models.WebApiTagDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        content = self._serialize.body(label, 'WebApiCreateTagRequestData')
        response = self._send(http_method='POST',
                              location_id='f22387e3-984e-4c52-9c6d-fbb8f14c812d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('WebApiTagDefinition', response)

    def delete_pull_request_labels(self, repository_id, pull_request_id, label_id_or_name, project=None, project_id=None):
        """DeletePullRequestLabels.
        [Preview API] Removes a label from the set of those assigned to the pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str label_id_or_name: The name or ID of the label requested.
        :param str project: Project ID or project name
        :param str project_id: Project ID or project name.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if label_id_or_name is not None:
            route_values['labelIdOrName'] = self._serialize.url('label_id_or_name', label_id_or_name, 'str')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        self._send(http_method='DELETE',
                   location_id='f22387e3-984e-4c52-9c6d-fbb8f14c812d',
                   version='6.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_pull_request_label(self, repository_id, pull_request_id, label_id_or_name, project=None, project_id=None):
        """GetPullRequestLabel.
        [Preview API] Retrieves a single label that has been assigned to a pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str label_id_or_name: The name or ID of the label requested.
        :param str project: Project ID or project name
        :param str project_id: Project ID or project name.
        :rtype: :class:`<WebApiTagDefinition> <azure.devops.v6_0.git.models.WebApiTagDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if label_id_or_name is not None:
            route_values['labelIdOrName'] = self._serialize.url('label_id_or_name', label_id_or_name, 'str')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        response = self._send(http_method='GET',
                              location_id='f22387e3-984e-4c52-9c6d-fbb8f14c812d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WebApiTagDefinition', response)

    def get_pull_request_labels(self, repository_id, pull_request_id, project=None, project_id=None):
        """GetPullRequestLabels.
        [Preview API] Get all the labels assigned to a pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :param str project_id: Project ID or project name.
        :rtype: [WebApiTagDefinition]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        query_parameters = {}
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        response = self._send(http_method='GET',
                              location_id='f22387e3-984e-4c52-9c6d-fbb8f14c812d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WebApiTagDefinition]', self._unwrap_collection(response))

    def get_pull_request_properties(self, repository_id, pull_request_id, project=None):
        """GetPullRequestProperties.
        [Preview API] Get external properties of the pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<object> <azure.devops.v6_0.git.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='48a52185-5b9e-4736-9dc1-bb1e2feac80b',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('object', response)

    def update_pull_request_properties(self, patch_document, repository_id, pull_request_id, project=None):
        """UpdatePullRequestProperties.
        [Preview API] Create or update pull request external properties. The patch operation can be `add`, `replace` or `remove`. For `add` operation, the path can be empty. If the path is empty, the value must be a list of key value pairs. For `replace` operation, the path cannot be empty. If the path does not exist, the property will be added to the collection. For `remove` operation, the path cannot be empty. If the path does not exist, no action will be performed.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v6_0.git.models.[JsonPatchOperation]>` patch_document: Properties to add, replace or remove in JSON Patch format.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<object> <azure.devops.v6_0.git.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='48a52185-5b9e-4736-9dc1-bb1e2feac80b',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_pull_request_query(self, queries, repository_id, project=None):
        """GetPullRequestQuery.
        [Preview API] This API is used to find what pull requests are related to a given commit.  It can be used to either find the pull request that created a particular merge commit or it can be used to find all pull requests that have ever merged a particular commit.  The input is a list of queries which each contain a list of commits. For each commit that you search against, you will get back a dictionary of commit -> pull requests.
        :param :class:`<GitPullRequestQuery> <azure.devops.v6_0.git.models.GitPullRequestQuery>` queries: The list of queries to perform.
        :param str repository_id: ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestQuery> <azure.devops.v6_0.git.models.GitPullRequestQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(queries, 'GitPullRequestQuery')
        response = self._send(http_method='POST',
                              location_id='b3a6eebe-9cf0-49ea-b6cb-1a4c5f5007b0',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestQuery', response)

    def create_pull_request_reviewer(self, reviewer, repository_id, pull_request_id, reviewer_id, project=None):
        """CreatePullRequestReviewer.
        [Preview API] Add a reviewer to a pull request or cast a vote.
        :param :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>` reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br />Reviewers can set their own vote with this method.  When adding other reviewers, vote must be set to zero.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('IdentityRefWithVote', response)

    def create_pull_request_reviewers(self, reviewers, repository_id, pull_request_id, project=None):
        """CreatePullRequestReviewers.
        [Preview API] Add reviewers to a pull request.
        :param [IdentityRef] reviewers: Reviewers to add to the pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[IdentityRefWithVote]', self._unwrap_collection(response))

    def create_unmaterialized_pull_request_reviewer(self, reviewer, repository_id, pull_request_id, project=None):
        """CreateUnmaterializedPullRequestReviewer.
        [Preview API] Add an unmaterialized identity to the reviewers of a pull request.
        :param :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>` reviewer: Reviewer to add to the pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(reviewer, 'IdentityRefWithVote')
        response = self._send(http_method='PUT',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('IdentityRefWithVote', response)

    def delete_pull_request_reviewer(self, repository_id, pull_request_id, reviewer_id, project=None):
        """DeletePullRequestReviewer.
        [Preview API] Remove a reviewer from a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
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
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_pull_request_reviewer(self, repository_id, pull_request_id, reviewer_id, project=None):
        """GetPullRequestReviewer.
        [Preview API] Retrieve information about a particular reviewer on a pull request
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>`
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('IdentityRefWithVote', response)

    def get_pull_request_reviewers(self, repository_id, pull_request_id, project=None):
        """GetPullRequestReviewers.
        [Preview API] Retrieve the reviewers for a pull request
        :param str repository_id: The repository ID of the pull request's target branch.
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[IdentityRefWithVote]', self._unwrap_collection(response))

    def update_pull_request_reviewer(self, reviewer, repository_id, pull_request_id, reviewer_id, project=None):
        """UpdatePullRequestReviewer.
        [Preview API] Edit a reviewer entry. These fields are patchable: isFlagged, hasDeclined
        :param :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>` reviewer: Reviewer data.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str reviewer_id: ID of the reviewer.
        :param str project: Project ID or project name
        :rtype: :class:`<IdentityRefWithVote> <azure.devops.v6_0.git.models.IdentityRefWithVote>`
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
        response = self._send(http_method='PATCH',
                              location_id='4b6702c7-aa35-4b89-9c96-b9abf6d3e540',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('IdentityRefWithVote', response)

    def update_pull_request_reviewers(self, patch_votes, repository_id, pull_request_id, project=None):
        """UpdatePullRequestReviewers.
        [Preview API] Reset the votes of multiple reviewers on a pull request.  NOTE: This endpoint only supports updating votes, but does not support updating required reviewers (use policy) or display names.
        :param [IdentityRefWithVote] patch_votes: IDs of the reviewers whose votes will be reset to zero
        :param str repository_id: The repository ID of the pull request's target branch.
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
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_pull_request_by_id(self, pull_request_id, project=None):
        """GetPullRequestById.
        [Preview API] Retrieve a pull request.
        :param int pull_request_id: The ID of the pull request to retrieve.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='01a46dea-7d46-4d40-bc84-319e7c260d99',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequest', response)

    def get_pull_requests_by_project(self, project, search_criteria, max_comment_length=None, skip=None, top=None):
        """GetPullRequestsByProject.
        [Preview API] Retrieve all pull requests matching a specified criteria.
        :param str project: Project ID or project name
        :param :class:`<GitPullRequestSearchCriteria> <azure.devops.v6_0.git.models.GitPullRequestSearchCriteria>` search_criteria: Pull requests will be returned that match this search criteria.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequest]', self._unwrap_collection(response))

    def create_pull_request(self, git_pull_request_to_create, repository_id, project=None, supports_iterations=None):
        """CreatePullRequest.
        [Preview API] Create a pull request.
        :param :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>` git_pull_request_to_create: The pull request to create.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param str project: Project ID or project name
        :param bool supports_iterations: If true, subsequent pushes to the pull request will be individually reviewable. Set this to false for large pull requests for performance reasons if this functionality is not needed.
        :rtype: :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitPullRequest', response)

    def get_pull_request(self, repository_id, pull_request_id, project=None, max_comment_length=None, skip=None, top=None, include_commits=None, include_work_item_refs=None):
        """GetPullRequest.
        [Preview API] Retrieve a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: The ID of the pull request to retrieve.
        :param str project: Project ID or project name
        :param int max_comment_length: Not used.
        :param int skip: Not used.
        :param int top: Not used.
        :param bool include_commits: If true, the pull request will be returned with the associated commits.
        :param bool include_work_item_refs: If true, the pull request will be returned with the associated work item references.
        :rtype: :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequest', response)

    def get_pull_requests(self, repository_id, search_criteria, project=None, max_comment_length=None, skip=None, top=None):
        """GetPullRequests.
        [Preview API] Retrieve all pull requests matching a specified criteria.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param :class:`<GitPullRequestSearchCriteria> <azure.devops.v6_0.git.models.GitPullRequestSearchCriteria>` search_criteria: Pull requests will be returned that match this search criteria.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequest]', self._unwrap_collection(response))

    def update_pull_request(self, git_pull_request_to_update, repository_id, pull_request_id, project=None):
        """UpdatePullRequest.
        [Preview API] Update a pull request
        :param :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>` git_pull_request_to_update: The pull request content that should be updated.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request to update.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequest> <azure.devops.v6_0.git.models.GitPullRequest>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequest', response)

    def share_pull_request(self, user_message, repository_id, pull_request_id, project=None):
        """SharePullRequest.
        [Preview API] Sends an e-mail notification about a specific pull request to a set of recipients
        :param :class:`<ShareNotificationContext> <azure.devops.v6_0.git.models.ShareNotificationContext>` user_message:
        :param str repository_id: ID of the git repository.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(user_message, 'ShareNotificationContext')
        self._send(http_method='POST',
                   location_id='696f3a82-47c9-487f-9117-b9d00972ca84',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def create_pull_request_status(self, status, repository_id, pull_request_id, project=None):
        """CreatePullRequestStatus.
        [Preview API] Create a pull request status.
        :param :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>` status: Pull request status to create.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(status, 'GitPullRequestStatus')
        response = self._send(http_method='POST',
                              location_id='b5f6bb4f-8d1e-4d79-8d11-4c9172c99c35',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestStatus', response)

    def delete_pull_request_status(self, repository_id, pull_request_id, status_id, project=None):
        """DeletePullRequestStatus.
        [Preview API] Delete pull request status.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int status_id: ID of the pull request status.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if status_id is not None:
            route_values['statusId'] = self._serialize.url('status_id', status_id, 'int')
        self._send(http_method='DELETE',
                   location_id='b5f6bb4f-8d1e-4d79-8d11-4c9172c99c35',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_pull_request_status(self, repository_id, pull_request_id, status_id, project=None):
        """GetPullRequestStatus.
        [Preview API] Get the specific pull request status by ID. The status ID is unique within the pull request across all iterations.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param int status_id: ID of the pull request status.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestStatus> <azure.devops.v6_0.git.models.GitPullRequestStatus>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        if status_id is not None:
            route_values['statusId'] = self._serialize.url('status_id', status_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5f6bb4f-8d1e-4d79-8d11-4c9172c99c35',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitPullRequestStatus', response)

    def get_pull_request_statuses(self, repository_id, pull_request_id, project=None):
        """GetPullRequestStatuses.
        [Preview API] Get all the statuses associated with a pull request.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: [GitPullRequestStatus]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5f6bb4f-8d1e-4d79-8d11-4c9172c99c35',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[GitPullRequestStatus]', self._unwrap_collection(response))

    def update_pull_request_statuses(self, patch_document, repository_id, pull_request_id, project=None):
        """UpdatePullRequestStatuses.
        [Preview API] Update pull request statuses collection. The only supported operation type is `remove`.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v6_0.git.models.[JsonPatchOperation]>` patch_document: Operations to apply to the pull request statuses in JSON Patch format.
        :param str repository_id: The repository ID of the pull request’s target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'int')
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        self._send(http_method='PATCH',
                   location_id='b5f6bb4f-8d1e-4d79-8d11-4c9172c99c35',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content,
                   media_type='application/json-patch+json')

    def create_comment(self, comment, repository_id, pull_request_id, thread_id, project=None):
        """CreateComment.
        [Preview API] Create a comment on a specific thread in a pull request (up to 500 comments can be created per thread).
        :param :class:`<Comment> <azure.devops.v6_0.git.models.Comment>` comment: The comment to create. Comments can be up to 150,000 characters.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v6_0.git.models.Comment>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def delete_comment(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """DeleteComment.
        [Preview API] Delete a comment associated with a specific thread in a pull request.
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
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_comment(self, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """GetComment.
        [Preview API] Retrieve a comment associated with a specific thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param int comment_id: ID of the comment.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v6_0.git.models.Comment>`
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Comment', response)

    def get_comments(self, repository_id, pull_request_id, thread_id, project=None):
        """GetComments.
        [Preview API] Retrieve all comments associated with a specific thread in a pull request.
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[Comment]', self._unwrap_collection(response))

    def update_comment(self, comment, repository_id, pull_request_id, thread_id, comment_id, project=None):
        """UpdateComment.
        [Preview API] Update a comment associated with a specific thread in a pull request.
        :param :class:`<Comment> <azure.devops.v6_0.git.models.Comment>` comment: The comment content that should be updated. Comments can be up to 150,000 characters.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread that the desired comment is in.
        :param int comment_id: ID of the comment to update.
        :param str project: Project ID or project name
        :rtype: :class:`<Comment> <azure.devops.v6_0.git.models.Comment>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def create_thread(self, comment_thread, repository_id, pull_request_id, project=None):
        """CreateThread.
        [Preview API] Create a thread in a pull request.
        :param :class:`<GitPullRequestCommentThread> <azure.devops.v6_0.git.models.GitPullRequestCommentThread>` comment_thread: The thread to create. Thread must contain at least one comment.
        :param str repository_id: Repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v6_0.git.models.GitPullRequestCommentThread>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_pull_request_thread(self, repository_id, pull_request_id, thread_id, project=None, iteration=None, base_iteration=None):
        """GetPullRequestThread.
        [Preview API] Retrieve a thread in a pull request.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread.
        :param str project: Project ID or project name
        :param int iteration: If specified, thread position will be tracked using this iteration as the right side of the diff.
        :param int base_iteration: If specified, thread position will be tracked using this iteration as the left side of the diff.
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v6_0.git.models.GitPullRequestCommentThread>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_threads(self, repository_id, pull_request_id, project=None, iteration=None, base_iteration=None):
        """GetThreads.
        [Preview API] Retrieve all threads in a pull request.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPullRequestCommentThread]', self._unwrap_collection(response))

    def update_thread(self, comment_thread, repository_id, pull_request_id, thread_id, project=None):
        """UpdateThread.
        [Preview API] Update a thread in a pull request.
        :param :class:`<GitPullRequestCommentThread> <azure.devops.v6_0.git.models.GitPullRequestCommentThread>` comment_thread: The thread content that should be updated.
        :param str repository_id: The repository ID of the pull request's target branch.
        :param int pull_request_id: ID of the pull request.
        :param int thread_id: ID of the thread to update.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPullRequestCommentThread> <azure.devops.v6_0.git.models.GitPullRequestCommentThread>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPullRequestCommentThread', response)

    def get_pull_request_work_item_refs(self, repository_id, pull_request_id, project=None):
        """GetPullRequestWorkItemRefs.
        [Preview API] Retrieve a list of work items associated with a pull request.
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
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def create_push(self, push, repository_id, project=None):
        """CreatePush.
        [Preview API] Push changes to the repository.
        :param :class:`<GitPush> <azure.devops.v6_0.git.models.GitPush>` push:
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitPush> <azure.devops.v6_0.git.models.GitPush>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(push, 'GitPush')
        response = self._send(http_method='POST',
                              location_id='ea98d07b-3c87-4971-8ede-a613694ffb55',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitPush', response)

    def get_push(self, repository_id, push_id, project=None, include_commits=None, include_ref_updates=None):
        """GetPush.
        [Preview API] Retrieves a particular push.
        :param str repository_id: The name or ID of the repository.
        :param int push_id: ID of the push.
        :param str project: Project ID or project name
        :param int include_commits: The number of commits to include in the result.
        :param bool include_ref_updates: If true, include the list of refs that were updated by the push.
        :rtype: :class:`<GitPush> <azure.devops.v6_0.git.models.GitPush>`
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
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitPush', response)

    def get_pushes(self, repository_id, project=None, skip=None, top=None, search_criteria=None):
        """GetPushes.
        [Preview API] Retrieves pushes associated with the specified repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :param int skip: Number of pushes to skip.
        :param int top: Number of pushes to return.
        :param :class:`<GitPushSearchCriteria> <azure.devops.v6_0.git.models.GitPushSearchCriteria>` search_criteria: Search criteria attributes: fromDate, toDate, pusherId, refName, includeRefUpdates or includeLinks. fromDate: Start date to search from. toDate: End date to search to. pusherId: Identity of the person who submitted the push. refName: Branch name to consider. includeRefUpdates: If true, include the list of refs that were updated by the push. includeLinks: Whether to include the _links field on the shallow references.
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
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitPush]', self._unwrap_collection(response))

    def delete_repository_from_recycle_bin(self, project, repository_id):
        """DeleteRepositoryFromRecycleBin.
        [Preview API] Destroy (hard delete) a soft-deleted Git repository.
        :param str project: Project ID or project name
        :param str repository_id: The ID of the repository.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        self._send(http_method='DELETE',
                   location_id='a663da97-81db-4eb3-8b83-287670f63073',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_recycle_bin_repositories(self, project):
        """GetRecycleBinRepositories.
        [Preview API] Retrieve soft-deleted git repositories from the recycle bin.
        :param str project: Project ID or project name
        :rtype: [GitDeletedRepository]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='a663da97-81db-4eb3-8b83-287670f63073',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[GitDeletedRepository]', self._unwrap_collection(response))

    def restore_repository_from_recycle_bin(self, repository_details, project, repository_id):
        """RestoreRepositoryFromRecycleBin.
        [Preview API] Recover a soft-deleted Git repository. Recently deleted repositories go into a soft-delete state for a period of time before they are hard deleted and become unrecoverable.
        :param :class:`<GitRecycleBinRepositoryDetails> <azure.devops.v6_0.git.models.GitRecycleBinRepositoryDetails>` repository_details:
        :param str project: Project ID or project name
        :param str repository_id: The ID of the repository.
        :rtype: :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(repository_details, 'GitRecycleBinRepositoryDetails')
        response = self._send(http_method='PATCH',
                              location_id='a663da97-81db-4eb3-8b83-287670f63073',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitRepository', response)

    def get_refs(self, repository_id, project=None, filter=None, include_links=None, include_statuses=None, include_my_branches=None, latest_statuses_only=None, peel_tags=None, filter_contains=None, top=None, continuation_token=None):
        """GetRefs.
        [Preview API] Queries the provided repository for its refs and returns them.
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
        :rtype: :class:`<[GitRef]> <azure.devops.v6_0.git.models.[GitRef]>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitRef]', self._unwrap_collection(response))

    def update_ref(self, new_ref_info, repository_id, filter, project=None, project_id=None):
        """UpdateRef.
        [Preview API] Lock or Unlock a branch.
        :param :class:`<GitRefUpdate> <azure.devops.v6_0.git.models.GitRefUpdate>` new_ref_info: The ref update action (lock/unlock) to perform
        :param str repository_id: The name or ID of the repository.
        :param str filter: The name of the branch to lock/unlock
        :param str project: Project ID or project name
        :param str project_id: ID or name of the team project. Optional if specifying an ID for repository.
        :rtype: :class:`<GitRef> <azure.devops.v6_0.git.models.GitRef>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitRef', response)

    def update_refs(self, ref_updates, repository_id, project=None, project_id=None):
        """UpdateRefs.
        [Preview API] Creating, updating, or deleting refs(branches).
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[GitRefUpdateResult]', self._unwrap_collection(response))

    def create_favorite(self, favorite, project):
        """CreateFavorite.
        [Preview API] Creates a ref favorite
        :param :class:`<GitRefFavorite> <azure.devops.v6_0.git.models.GitRefFavorite>` favorite: The ref favorite to create.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRefFavorite> <azure.devops.v6_0.git.models.GitRefFavorite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(favorite, 'GitRefFavorite')
        response = self._send(http_method='POST',
                              location_id='876f70af-5792-485a-a1c7-d0a7b2f42bbb',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitRefFavorite', response)

    def delete_ref_favorite(self, project, favorite_id):
        """DeleteRefFavorite.
        [Preview API] Deletes the refs favorite specified
        :param str project: Project ID or project name
        :param int favorite_id: The Id of the ref favorite to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if favorite_id is not None:
            route_values['favoriteId'] = self._serialize.url('favorite_id', favorite_id, 'int')
        self._send(http_method='DELETE',
                   location_id='876f70af-5792-485a-a1c7-d0a7b2f42bbb',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_ref_favorite(self, project, favorite_id):
        """GetRefFavorite.
        [Preview API] Gets the refs favorite for a favorite Id.
        :param str project: Project ID or project name
        :param int favorite_id: The Id of the requested ref favorite.
        :rtype: :class:`<GitRefFavorite> <azure.devops.v6_0.git.models.GitRefFavorite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if favorite_id is not None:
            route_values['favoriteId'] = self._serialize.url('favorite_id', favorite_id, 'int')
        response = self._send(http_method='GET',
                              location_id='876f70af-5792-485a-a1c7-d0a7b2f42bbb',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitRefFavorite', response)

    def get_ref_favorites(self, project, repository_id=None, identity_id=None):
        """GetRefFavorites.
        [Preview API] Gets the refs favorites for a repo and an identity.
        :param str project: Project ID or project name
        :param str repository_id: The id of the repository.
        :param str identity_id: The id of the identity whose favorites are to be retrieved. If null, the requesting identity is used.
        :rtype: [GitRefFavorite]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if identity_id is not None:
            query_parameters['identityId'] = self._serialize.query('identity_id', identity_id, 'str')
        response = self._send(http_method='GET',
                              location_id='876f70af-5792-485a-a1c7-d0a7b2f42bbb',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitRefFavorite]', self._unwrap_collection(response))

    def create_repository(self, git_repository_to_create, project=None, source_ref=None):
        """CreateRepository.
        [Preview API] Create a git repository in a team project.
        :param :class:`<GitRepositoryCreateOptions> <azure.devops.v6_0.git.models.GitRepositoryCreateOptions>` git_repository_to_create: Specify the repo name, team project and/or parent repository. Team project information can be omitted from gitRepositoryToCreate if the request is project-scoped (i.e., includes project Id).
        :param str project: Project ID or project name
        :param str source_ref: [optional] Specify the source refs to use while creating a fork repo
        :rtype: :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('GitRepository', response)

    def delete_repository(self, repository_id, project=None):
        """DeleteRepository.
        [Preview API] Delete a git repository
        :param str repository_id: The ID of the repository.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        self._send(http_method='DELETE',
                   location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_repositories(self, project=None, include_links=None, include_all_urls=None, include_hidden=None):
        """GetRepositories.
        [Preview API] Retrieve git repositories.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitRepository]', self._unwrap_collection(response))

    def get_repository(self, repository_id, project=None):
        """GetRepository.
        [Preview API] Retrieve a git repository.
        :param str repository_id: The name or ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitRepository', response)

    def get_repository_with_parent(self, repository_id, include_parent, project=None):
        """GetRepositoryWithParent.
        [Preview API] Retrieve a git repository.
        :param str repository_id: The name or ID of the repository.
        :param bool include_parent: True to include parent repository. Only available in authenticated calls.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitRepository', response)

    def update_repository(self, new_repository_info, repository_id, project=None):
        """UpdateRepository.
        [Preview API] Updates the Git repository with either a new repo name or a new default branch.
        :param :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>` new_repository_info: Specify a new repo name or a new default branch of the repository
        :param str repository_id: The ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitRepository> <azure.devops.v6_0.git.models.GitRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(new_repository_info, 'GitRepository')
        response = self._send(http_method='PATCH',
                              location_id='225f7195-f9c7-4d14-ab28-a83f7ff77e1f',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitRepository', response)

    def get_stats(self, project, repository_id):
        """GetStats.
        [Preview API] Retrieves statistics of a repository.
        :param str project: Project ID or project name
        :param str repository_id: Friendly name or guid of repository.
        :rtype: :class:`<GitRepositoryStats> <azure.devops.v6_0.git.models.GitRepositoryStats>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='616a5255-74b3-40f5-ae1d-bbae2eec8db5',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitRepositoryStats', response)

    def create_revert(self, revert_to_create, project, repository_id):
        """CreateRevert.
        [Preview API] Starts the operation to create a new branch which reverts changes introduced by either a specific commit or commits that are associated to a pull request.
        :param :class:`<GitAsyncRefOperationParameters> <azure.devops.v6_0.git.models.GitAsyncRefOperationParameters>` revert_to_create:
        :param str project: Project ID or project name
        :param str repository_id: ID of the repository.
        :rtype: :class:`<GitRevert> <azure.devops.v6_0.git.models.GitRevert>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        content = self._serialize.body(revert_to_create, 'GitAsyncRefOperationParameters')
        response = self._send(http_method='POST',
                              location_id='bc866058-5449-4715-9cf1-a510b6ff193c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitRevert', response)

    def get_revert(self, project, revert_id, repository_id):
        """GetRevert.
        [Preview API] Retrieve information about a revert operation by revert Id.
        :param str project: Project ID or project name
        :param int revert_id: ID of the revert operation.
        :param str repository_id: ID of the repository.
        :rtype: :class:`<GitRevert> <azure.devops.v6_0.git.models.GitRevert>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if revert_id is not None:
            route_values['revertId'] = self._serialize.url('revert_id', revert_id, 'int')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='bc866058-5449-4715-9cf1-a510b6ff193c',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('GitRevert', response)

    def get_revert_for_ref_name(self, project, repository_id, ref_name):
        """GetRevertForRefName.
        [Preview API] Retrieve information about a revert operation for a specific branch.
        :param str project: Project ID or project name
        :param str repository_id: ID of the repository.
        :param str ref_name: The GitAsyncRefOperationParameters generatedRefName used for the revert operation.
        :rtype: :class:`<GitRevert> <azure.devops.v6_0.git.models.GitRevert>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        query_parameters = {}
        if ref_name is not None:
            query_parameters['refName'] = self._serialize.query('ref_name', ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc866058-5449-4715-9cf1-a510b6ff193c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitRevert', response)

    def create_commit_status(self, git_commit_status_to_create, commit_id, repository_id, project=None):
        """CreateCommitStatus.
        [Preview API] Create Git commit status.
        :param :class:`<GitStatus> <azure.devops.v6_0.git.models.GitStatus>` git_commit_status_to_create: Git commit status object to create.
        :param str commit_id: ID of the Git commit.
        :param str repository_id: ID of the repository.
        :param str project: Project ID or project name
        :rtype: :class:`<GitStatus> <azure.devops.v6_0.git.models.GitStatus>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('GitStatus', response)

    def get_statuses(self, commit_id, repository_id, project=None, top=None, skip=None, latest_only=None):
        """GetStatuses.
        [Preview API] Get statuses associated with the Git commit.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[GitStatus]', self._unwrap_collection(response))

    def get_suggestions(self, repository_id, project=None):
        """GetSuggestions.
        [Preview API] Retrieve a pull request suggestion for a particular repository or team project.
        :param str repository_id: ID of the git repository.
        :param str project: Project ID or project name
        :rtype: [GitSuggestion]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if repository_id is not None:
            route_values['repositoryId'] = self._serialize.url('repository_id', repository_id, 'str')
        response = self._send(http_method='GET',
                              location_id='9393b4fb-4445-4919-972b-9ad16f442d83',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[GitSuggestion]', self._unwrap_collection(response))

    def get_tree(self, repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None):
        """GetTree.
        [Preview API] The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
        :param str repository_id: Repository Id.
        :param str sha1: SHA1 hash of the tree object.
        :param str project: Project ID or project name
        :param str project_id: Project Id.
        :param bool recursive: Search recursively. Include trees underneath this tree. Default is false.
        :param str file_name: Name to use if a .zip file is returned. Default is the object ID.
        :rtype: :class:`<GitTreeRef> <azure.devops.v6_0.git.models.GitTreeRef>`
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('GitTreeRef', response)

    def get_tree_zip(self, repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None, **kwargs):
        """GetTreeZip.
        [Preview API] The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
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
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

