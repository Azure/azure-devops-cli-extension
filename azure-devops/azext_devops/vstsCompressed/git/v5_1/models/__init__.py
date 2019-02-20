# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .models import Attachment
from .models import Change
from .models import Comment
from .models import CommentIterationContext
from .models import CommentPosition
from .models import CommentThread
from .models import CommentThreadContext
from .models import CommentTrackingCriteria
from .models import FileContentMetadata
from .models import FileDiff
from .models import FileDiffParams
from .models import FileDiffsCriteria
from .models import GitAnnotatedTag
from .models import GitAsyncRefOperation
from .models import GitAsyncRefOperationDetail
from .models import GitAsyncRefOperationParameters
from .models import GitAsyncRefOperationSource
from .models import GitBaseVersionDescriptor
from .models import GitBlobRef
from .models import GitBranchStats
from .models import GitCherryPick
from .models import GitCommit
from .models import GitCommitChanges
from .models import GitCommitDiffs
from .models import GitCommitRef
from .models import GitConflict
from .models import GitConflictUpdateResult
from .models import GitDeletedRepository
from .models import GitFilePathsCollection
from .models import GitForkOperationStatusDetail
from .models import GitForkRef
from .models import GitForkSyncRequest
from .models import GitForkSyncRequestParameters
from .models import_git_source import GitImportGitSource
from .models import_request import GitImportRequest
from .models import_request_parameters import GitImportRequestParameters
from .models import_status_detail import GitImportStatusDetail
from .models import_tfvc_source import GitImportTfvcSource
from .models import GitItem
from .models import GitItemDescriptor
from .models import GitItemRequestData
from .models import GitMerge
from .models import GitMergeOperationStatusDetail
from .models import GitMergeOriginRef
from .models import GitMergeParameters
from .models import GitObject
from .models import GitPolicyConfigurationResponse
from .models import GitPullRequest
from .models import GitPullRequestChange
from .models import GitPullRequestCommentThread
from .models import GitPullRequestCommentThreadContext
from .models import GitPullRequestCompletionOptions
from .models import GitPullRequestIteration
from .models import GitPullRequestIterationChanges
from .models import GitPullRequestMergeOptions
from .models import GitPullRequestQuery
from .models import GitPullRequestQueryInput
from .models import GitPullRequestSearchCriteria
from .models import GitPullRequestStatus
from .models import GitPush
from .models import GitPushRef
from .models import GitPushSearchCriteria
from .models import GitQueryBranchStatsCriteria
from .models import GitQueryCommitsCriteria
from .models import GitRecycleBinRepositoryDetails
from .models import GitRef
from .models import GitRefFavorite
from .models import GitRefUpdate
from .models import GitRefUpdateResult
from .models import GitRepository
from .models import GitRepositoryCreateOptions
from .models import GitRepositoryRef
from .models import GitRepositoryStats
from .models import GitRevert
from .models import GitStatus
from .models import GitStatusContext
from .models import GitSuggestion
from .models import GitTargetVersionDescriptor
from .models import GitTemplate
from .models import GitTreeDiff
from .models import GitTreeDiffEntry
from .models import GitTreeDiffResponse
from .models import GitTreeEntryRef
from .models import GitTreeRef
from .models import GitUserDate
from .models import GitVersionDescriptor
from .models import GlobalGitRepositoryKey
from .models import GraphSubjectBase
from .models import IdentityRef
from .models import IdentityRefWithVote
from .models import_repository_validation import ImportRepositoryValidation
from .models import ItemContent
from .models import ItemModel
from .models import JsonPatchOperation
from .models import LineDiffBlock
from .models import PolicyConfiguration
from .models import PolicyConfigurationRef
from .models import PolicyTypeRef
from .models import ReferenceLinks
from .models import ResourceRef
from .models import ShareNotificationContext
from .models import SourceToTargetRef
from .models import TeamProjectCollectionReference
from .models import TeamProjectReference
from .models import VersionedPolicyConfigurationRef
from .models import VstsInfo
from .models import WebApiCreateTagRequestData
from .models import WebApiTagDefinition

__all__ = [
    'Attachment',
    'Change',
    'Comment',
    'CommentIterationContext',
    'CommentPosition',
    'CommentThread',
    'CommentThreadContext',
    'CommentTrackingCriteria',
    'FileContentMetadata',
    'FileDiff',
    'FileDiffParams',
    'FileDiffsCriteria',
    'GitAnnotatedTag',
    'GitAsyncRefOperation',
    'GitAsyncRefOperationDetail',
    'GitAsyncRefOperationParameters',
    'GitAsyncRefOperationSource',
    'GitBaseVersionDescriptor',
    'GitBlobRef',
    'GitBranchStats',
    'GitCherryPick',
    'GitCommit',
    'GitCommitChanges',
    'GitCommitDiffs',
    'GitCommitRef',
    'GitConflict',
    'GitConflictUpdateResult',
    'GitDeletedRepository',
    'GitFilePathsCollection',
    'GitForkOperationStatusDetail',
    'GitForkRef',
    'GitForkSyncRequest',
    'GitForkSyncRequestParameters',
    'GitImportGitSource',
    'GitImportRequest',
    'GitImportRequestParameters',
    'GitImportStatusDetail',
    'GitImportTfvcSource',
    'GitItem',
    'GitItemDescriptor',
    'GitItemRequestData',
    'GitMerge',
    'GitMergeOperationStatusDetail',
    'GitMergeOriginRef',
    'GitMergeParameters',
    'GitObject',
    'GitPolicyConfigurationResponse',
    'GitPullRequest',
    'GitPullRequestChange',
    'GitPullRequestCommentThread',
    'GitPullRequestCommentThreadContext',
    'GitPullRequestCompletionOptions',
    'GitPullRequestIteration',
    'GitPullRequestIterationChanges',
    'GitPullRequestMergeOptions',
    'GitPullRequestQuery',
    'GitPullRequestQueryInput',
    'GitPullRequestSearchCriteria',
    'GitPullRequestStatus',
    'GitPush',
    'GitPushRef',
    'GitPushSearchCriteria',
    'GitQueryBranchStatsCriteria',
    'GitQueryCommitsCriteria',
    'GitRecycleBinRepositoryDetails',
    'GitRef',
    'GitRefFavorite',
    'GitRefUpdate',
    'GitRefUpdateResult',
    'GitRepository',
    'GitRepositoryCreateOptions',
    'GitRepositoryRef',
    'GitRepositoryStats',
    'GitRevert',
    'GitStatus',
    'GitStatusContext',
    'GitSuggestion',
    'GitTargetVersionDescriptor',
    'GitTemplate',
    'GitTreeDiff',
    'GitTreeDiffEntry',
    'GitTreeDiffResponse',
    'GitTreeEntryRef',
    'GitTreeRef',
    'GitUserDate',
    'GitVersionDescriptor',
    'GlobalGitRepositoryKey',
    'GraphSubjectBase',
    'IdentityRef',
    'IdentityRefWithVote',
    'ImportRepositoryValidation',
    'ItemContent',
    'ItemModel',
    'JsonPatchOperation',
    'LineDiffBlock',
    'PolicyConfiguration',
    'PolicyConfigurationRef',
    'PolicyTypeRef',
    'ReferenceLinks',
    'ResourceRef',
    'ShareNotificationContext',
    'SourceToTargetRef',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'VersionedPolicyConfigurationRef',
    'VstsInfo',
    'WebApiCreateTagRequestData',
    'WebApiTagDefinition',
]
