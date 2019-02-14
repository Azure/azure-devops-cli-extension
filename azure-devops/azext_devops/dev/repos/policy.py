# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# This file a lot of these are intentional because that makes grouping variables easy

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.policy.v4_0.models.models import PolicyConfiguration

from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.services import (get_policy_client, resolve_instance_and_project)
from azext_devops.dev.common.const import (APPROVER_COUNT_POLICY,
                                           APPROVER_COUNT_POLICY_ID,
                                           BUILD_POLICY,
                                           BUILD_POLICY_ID,
                                           COMMENT_REQUIREMENTS_POLICY,
                                           COMMENT_REQUIREMENTS_POLICY_ID,
                                           MERGE_STRATEGY_POLICY,
                                           MERGE_STRATEGY_POLICY_ID,
                                           FILE_SIZE_POLICY,
                                           FILE_SIZE_POLICY_ID,
                                           WORKITEM_LINKING_POLICY,
                                           WORKITEM_LINKING_POLICY_ID,
                                           REQUIRED_REVIEWER_POLICY,
                                           REQUIRED_REVIEWER_POLICY_ID)
from azext_devops.dev.common.identities import resolve_identity_as_id

logger = get_logger(__name__)


def list_policy(organization=None, project=None, repository_id=None, branch=None, detect=None):
    """List of policies.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param repository_id: Id (UUID) of the repository.
    :type repository_id: string
    :param branch: Branch. (--repository-id is required)
    :type branch: string
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: [PolicyConfiguration]
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)

        scope = None

        if branch is not None and repository_id is None:
            raise CLIError('--repository-id is required with --branch')

        if repository_id is not None:
            scope = repository_id
            if branch is not None:
                branch = resolve_git_ref_heads(branch)
                scope = scope + ':' + branch

        policy_client = get_policy_client(organization)
        return policy_client.get_policy_configurations(project=project, scope=scope)
    except VstsServiceError as ex:
        raise CLIError(ex)


def get_policy(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Show policy details.
    :param id: ID of the policy.
    :type id: int
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: :class:`<PolicyConfiguration> <policy.v4_0.models.PolicyConfiguration>`
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        return policy_client.get_policy_configuration(project=project, configuration_id=id)
    except VstsServiceError as ex:
        raise CLIError(ex)


def delete_policy(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a policy.
    :param id: ID of the policy.
    :type id: int
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        return policy_client.delete_policy_configuration(project=project, configuration_id=id)
    except VstsServiceError as ex:
        raise CLIError(ex)


# pylint: disable=too-many-locals
def create_policy(policy_configuration=None,
                  repository_id=None, branch=None,
                  is_blocking=None, is_enabled=None,
                  policy_type=None,
                  minimum_approver_count=None, creator_vote_counts=None, allow_downvotes=None, reset_on_source_push=None,
                  use_squash_merge=None,
                  build_definition_id=None, queue_on_source_update_only=None, manual_queue_only=None, display_name=None, valid_duration=None,
                  maximum_git_blob_size_in_bytes=None, use_uncompressed_size=None,
                  optional_reviewer_ids=None, required_reviewer_ids=None, message=None,
                  organization=None, project=None, detect=None):
    """Create a policy.
    :param policy_configuration: File path of file containing policy configuration to create in a serialized form.
                                 please use / backslash when typing in directory path.
                                 Only --project and --organization param are needed when passing this.
    :type policy_configuration: string

    :param repository_id: Id (UUID) of the repository on which to apply the policy
    :type repository_id: string
    :param branch: Branch on which this policy should be applied
    :type branch: string
    :param is_blocking: Whether the policy should be blocking or not.
    :type is_blocking: bool
    :param is_enabled: Whether the policy is enabled or not.
    :type is_enabled: bool
    :param policy_type: Type of policy you want to create
    :type policy_type: string

    :param optional_reviewer_ids: Optional Reviewers (List of email ids seperated with ';').
    :type optional_reviewer_ids: string
    :param required_reviewer_ids: Required Reviewers (List of email ids seperated with ';').
    :type required_reviewer_ids: string
    :param message: Message.
    :type message: string

    :param minimum_approver_count: Minimum approver count.
    :type minimum_approver_count: int
    :param creator_vote_counts: Whether the creator's vote count counts or not.
    :type creator_vote_counts: bool
    :param allow_downvotes: Whether to allow downvotes or not.
    :type allow_downvotes: bool
    :param reset_on_source_push: Whether to reset source on push.
    :type reset_on_source_push: bool

    :param build_definition_id: Build Definition Id
    :type build_definition_id: int
    :param queue_on_source_update_only: Queue Only on source update.
    :type queue_on_source_update_only: bool
    :param manual_queue_only : Whether to allow only manual queue of builds.
    :type manual_queue_only : bool
    :param display_name : Display Name.
    :type display_name : string
    :param valid_duration :  Policy validity duration (in hours).
    :type valid_duration : double

    :param use_squash_merge: Whether to squash merge always.
    :type use_squash_merge: bool

    :param maximum_git_blob_size_in_bytes: Maximum Git Blob Size In Bytes.
    :type maximum_git_blob_size_in_bytes: long
    :param use_uncompressed_size: Whether to use uncompressed size.
    :type use_uncompressed_size: bool

    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: :class:`<PolicyConfiguration> <policy.v4_0.models.PolicyConfiguration>`
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)

        policyConfigurationToCreate = generateConfigurationObject(
            policy_configuration,
            repository_id, branch,
            policy_type,
            is_blocking, is_enabled,
            minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push,
            use_squash_merge,
            build_definition_id, queue_on_source_update_only, manual_queue_only, display_name, valid_duration,
            maximum_git_blob_size_in_bytes, use_uncompressed_size,
            optional_reviewer_ids, required_reviewer_ids, message,
            organization)

        return policy_client.create_policy_configuration(configuration=policyConfigurationToCreate, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)


# pylint: disable=too-many-locals
def update_policy(policy_id,
                  policy_configuration=None,
                  repository_id=None, branch=None,
                  is_blocking=None, is_enabled=None,
                  policy_type=None,
                  minimum_approver_count=None, creator_vote_counts=None, allow_downvotes=None, reset_on_source_push=None,
                  use_squash_merge=None,
                  build_definition_id=None, queue_on_source_update_only=None, manual_queue_only=None, display_name=None, valid_duration=None,
                  maximum_git_blob_size_in_bytes=None, use_uncompressed_size=None,
                  optional_reviewer_ids=None, required_reviewer_ids=None, message=None,
                  organization=None, project=None, detect=None):
    """Update a policy.
    :param policy_configuration: File path of file containing policy configuration to create in a serialized form.
                                 please use / backslash when typing in directory path.
                                 Only --project and --organization param are needed when passing this.
    :type policy_configuration: string
    :param repository_id: Id (UUID) of the repository on which to apply the policy to.
    :type repository_id: string
    :param branch: Branch on which this policy should be applied
    :type branch: string
    :param policy_id: ID of the policy which needs to be updated
    :type policy_id: int
    :param isBlocking: Whether the policy should be blocking or not.
    :param is_blocking: Whether the policy should be blocking or not.
    :type is_blocking: bool
    :param is_enabled: Whether the policy is enabled or not.
    :type is_enabled: bool
    :param policy_type: Type of policy you want to create
    :type policy_type: string

    :param optional_reviewer_ids: Optional Reviewers (List of email ids seperated with ';').
    :type optional_reviewer_ids: string
    :param required_reviewer_ids: Required Reviewers (List of email ids seperated with ';').
    :type required_reviewer_ids: string
    :param message: Message.
    :type message: string

    :param minimum_approver_count: Minimum approver count.
    :type minimum_approver_count: int
    :param creator_vote_counts: Whether the creator's vote count counts or not.
    :type creator_vote_counts: bool
    :param allow_downvotes: Whether to allow downvotes or not.
    :type allow_downvotes: bool
    :param reset_on_source_push: Whether to reset source on push.
    :type reset_on_source_push: bool

    :param build_definition_id: Build Definition Id
    :type build_definition_id: int
    :param queue_on_source_update_only: Queue Only on source update.
    :type queue_on_source_update_only: bool
    :param manual_queue_only : Whether to allow only manual queue of builds.
    :type manual_queue_only : bool
    :param display_name : Display Name.
    :type display_name : string
    :param valid_duration :  Policy validity duration (in hours).
    :type valid_duration : double

    :param use_squash_merge: Whether to squash merge always.
    :type use_squash_merge: bool

    :param maximum_git_blob_size_in_bytes: Maximum Git Blob Size In Bytes.
    :type maximum_git_blob_size_in_bytes: long
    :param use_uncompressed_size: Whether to use uncompressed size.
    :type use_uncompressed_size: bool

    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: :class:`<PolicyConfiguration> <policy.v4_0.models.PolicyConfiguration>`
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)

        policyConfigurationToCreate = generateConfigurationObject(
            policy_configuration,
            repository_id, branch,
            policy_type,
            is_blocking, is_enabled,
            minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push,
            use_squash_merge,
            build_definition_id, queue_on_source_update_only, manual_queue_only, display_name, valid_duration,
            maximum_git_blob_size_in_bytes, use_uncompressed_size,
            optional_reviewer_ids, required_reviewer_ids, message,
            organization)

        return policy_client.update_policy_configuration(
            configuration=policyConfigurationToCreate,
            project=project,
            configuration_id=policy_id)
    except VstsServiceError as ex:
        raise CLIError(ex)


# pylint: disable=too-many-locals, too-many-statements
def generateConfigurationObject(policy_configuration=None,
                                repository_id=None, branch=None,
                                policy_type=None,
                                isBlocking=False, isEnabled=False,
                                minimumApproverCount=None, creatorVoteCounts=None, allowDownvotes=None, resetOnSourcePush=None,
                                useSquashMerge=None,
                                buildDefinitionId=None, queueOnSourceUpdateOnly=None, manualQueueOnly=None, displayName=None, validDuration=None,
                                maximumGitBlobSizeInBytes=None, useUncompressedSize=None,
                                optionalReviewerIds=None, requiredReviewerIds=None, message=None,
                                organization=None):
    if policy_configuration is None and policy_type is None:
        raise CLIError('Either --policy-configuration or --policy-type must be passed')

    if policy_configuration is not None:
        with open(policy_configuration) as f:
            import json
            return json.load(f)

    branch = resolve_git_ref_heads(branch)

    # these 2 will be filled by respective types
    paramNameArray = []
    paramArray = []
    policytypeId = ''

    if policy_type == APPROVER_COUNT_POLICY:
        policytypeId = APPROVER_COUNT_POLICY_ID
        paramArray = [minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush]
        paramNameArray = ['minimumApproverCount', 'creatorVoteCounts', 'allowDownvotes', 'resetOnSourcePush']
        argumentNameArray = ['minimum-approver-count', 'creator-vote-counts', 'allow-downvotes', 'reset-on-source-push']

    elif policy_type == BUILD_POLICY:
        policytypeId = BUILD_POLICY_ID
        paramArray = [buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration]
        paramNameArray = ['buildDefinitionId', 'queueOnSourceUpdateOnly', 'manualQueueOnly', 'displayName', 'validDuration']
        argumentNameArray = ['build-definition-id', 'queue-on-source-update-only', 'manual-queue_only', 'display-name', 'valid-duration']

    elif policy_type == COMMENT_REQUIREMENTS_POLICY:
        policytypeId = COMMENT_REQUIREMENTS_POLICY_ID
        # this particular policy does not need any other parameter

    elif policy_type == MERGE_STRATEGY_POLICY:
        policytypeId = MERGE_STRATEGY_POLICY_ID
        paramArray = [useSquashMerge]
        paramNameArray = ['useSquashMerge']
        argumentNameArray = ['use-squash-merge']

    elif policy_type == FILE_SIZE_POLICY:
        policytypeId = FILE_SIZE_POLICY_ID
        paramArray = [maximumGitBlobSizeInBytes, useUncompressedSize]
        paramNameArray = ['maximumGitBlobSizeInBytes', 'useUncompressedSize']
        argumentNameArray = ['maximum-git-blob-size-in-bytes', 'use-uncompressed-size']

    elif policy_type == WORKITEM_LINKING_POLICY:
        policytypeId = WORKITEM_LINKING_POLICY_ID
        # this particular policy does not need any other parameter

    elif policy_type == REQUIRED_REVIEWER_POLICY:
        policytypeId = REQUIRED_REVIEWER_POLICY_ID
        optionalReviewerIds = resolveIdentityMailsToIds(optionalReviewerIds, organization)
        requiredReviewerIds = resolveIdentityMailsToIds(requiredReviewerIds, organization)
        # special handling for this policy
        if optionalReviewerIds and (not requiredReviewerIds):
            requiredReviewerIds = []
        if requiredReviewerIds and (not optionalReviewerIds):
            optionalReviewerIds = []
        paramArray = [optionalReviewerIds, requiredReviewerIds, message]
        paramNameArray = ['optionalReviewerIds', 'requiredReviewerIds', 'message']
        argumentNameArray = ['optional-reviewer-ids', 'required-reviewer-ids', 'message']

    # check if we have value in all the required params or not
    raiseErrorIfRequiredParamMissing(paramArray, argumentNameArray, policy_type)

    policyConfiguration = PolicyConfiguration(is_blocking=_parseTrueFalse(isBlocking), is_enabled=_parseTrueFalse(isEnabled))
    scope = createScope(policy_type, repository_id, branch)

    policyConfiguration.settings = {
        'scope': scope
    }

    policyConfiguration.type = {
        'id': policytypeId
    }

    index = 0
    for param in paramNameArray:
        policyConfiguration.settings[param] = paramArray[index]
        index = index + 1

    return policyConfiguration


def createScope(policy_type, repository_id, branch):
    scope = [
        {
            'repositoryId': repository_id,
            'refName': branch,
            'matchKind': 'exact'
        }
    ]

    if policy_type == FILE_SIZE_POLICY:
        if branch is not None:
            raise CLIError('You can only use repository for this policy type not branch')
        scope = [
            {
                'repositoryId': repository_id
            }
        ]

    return scope


def resolveIdentityMailsToIds(mailList, organization):
    logger.debug('mail list %s ', mailList)
    if not mailList or (not mailList.strip()):
        return None

    idList = []
    for mail in mailList.split(';'):
        mailStripped = mail.strip()
        logger.debug('trying to resolve %s', mailStripped)
        identityId = resolve_identity_as_id(mailStripped, organization)
        logger.debug('got id as %s', identityId)
        idList.append(identityId)

    return idList


def raiseErrorIfRequiredParamMissing(paramArray, paramNameArray, policyName):
    if not paramNameArray:
        return
    if any(v is None for v in paramArray):
        raise CLIError('{} are required for {}'.format('--' + ', --'.join(paramNameArray), policyName))

def _parseTrueFalse(inputString):
    if inputString is not None and inputString.lower() == 'true' :
        return True
    
    return False
