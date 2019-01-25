# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from knack.util import CLIError
from vsts.exceptions import VstsClientRequestError, VstsServiceError
from vsts.policy.v4_0.models.policy_configuration import PolicyConfiguration

from azext_devops.dev.common.services import (get_policy_client, resolve_instance_and_project)
from azext_devops.dev.common.const import *


def list_policy(organization=None, project=None, detect=None):
    """
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: [PolicyConfiguration]
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        return policy_client.get_policy_configurations(project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

def get_policy(id, organization=None, project=None, detect=None):
    """
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

def delete_policy(id, organization=None, project=None, detect=None):
    """
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

def create_policy(repository_id, branch,
                  isBlocking=False, isEnabled=False,
                  policy_type=None,
                  minimumApproverCount=None, creatorVoteCounts=None, allowDownvotes=None, resetOnSourcePush=None,
                  useSquashMerge=None,
                  buildDefinitionId=None, queueOnSourceUpdateOnly=None, manualQueueOnly=None, displayName=None, validDuration=None,
                  maximumGitBlobSizeInBytes=None, useUncompressedSize=None,
                  organization=None, project=None, detect=None):
    """
    :param repository_id: Id (UUID) of the repository on which to apply the policy
    :type repository_id: string
    :param branch: Branch on which this policy should be applied
    :type branch: string
    :param isBlocking: Tells if the policy should be blocking or not
    :type isBlocking: bool
    :param isEnabled: Tells if the policy is enabled or not
    :type isEnabled: bool
    :param policy_type: Type of policy you want to create
    :type policy_type: string

    :param minimumApproverCount: Minimum approver count. Required if policy type is ApproverCountPolicy.
    :type minimumApproverCount: int
    :param creatorVoteCounts: Creator vote counts or not. Required if policy type is ApproverCountPolicy
    :type creatorVoteCounts: bool
    :param allowDownvotes: Allow Downvotes. Required if policy type is ApproverCountPolicy.
    :type allowDownvotes: bool
    :param resetOnSourcePush: Reset on Source Push. Required if policy type is ApproverCountPolicy.
    :type resetOnSourcePush: bool

    :param buildDefinitionId: Build Definition Id. Required if policy type is Buildpolicy.
    :type buildDefinitionId: int
    :param queueOnSourceUpdateOnly: Queue Only on source update. Required if policy type is Buildpolicy.
    :type queueOnSourceUpdateOnly: bool
    :param manualQueueOnly : Manual Queue Only. Required if policy type is Buildpolicy.
    :type manualQueueOnly : bool
    :param displayName : Display Name. Required if policy type is Buildpolicy.
    :type displayName : string
    :param validDuration : Valid duration. Required if policy type is Buildpolicy.
    :type validDuration : double

    :param useSquashMerge: Use Squash Merge. Required if policy type is MergeStrategyPolicy
    :type useSquashMerge: bool

    :param maximumGitBlobSizeInBytes: Maximum Git Blob Size In Bytes. Required if policy type is FileSizePolicy
    :type maximumGitBlobSizeInBytes: long
    :param useUncompressedSize: Use uncompressed size. Required if policy type is FileSizePolicy
    :type useUncompressedSize: bool

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

        # these 2 will be filled by respective types
        paramNameArray = []
        paramArray = []
        policytypeId = ''

        if(policy_type == APPROVER_COUNT_POLICY):
            policytypeId = APPROVER_COUNT_POLICY_ID
            paramArray = [minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush]
            paramNameArray = nameOfArray([minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush])

        elif(policy_type == BUILD_POLICY):
            policytypeId = BUILD_POLICY_ID
            paramArray = [buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration]
            paramNameArray = nameOfArray([buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration])

        elif(policy_type == COMMENT_REQUIREMENTS_POLICY):
            policytypeId = COMMENT_REQUIREMENTS_POLICY_ID
            # this particular policy does not need any other parameter

        elif(policy_type == MERGE_STRATEGY_POLICY):
            policytypeId = MERGE_STRATEGY_POLICY_ID
            paramArray = [useSquashMerge]
            paramNameArray = nameOfArray([useSquashMerge])

        elif(policy_type == FILE_SIZE_POLICY):
            policytypeId = FILE_SIZE_POLICY_ID
            paramArray = [maximumGitBlobSizeInBytes, useUncompressedSize]
            paramNameArray = nameOfArray([maximumGitBlobSizeInBytes, useUncompressedSize])

        elif(policy_type == WORKITEM_LINKING_POLICY):
            policytypeId = WORKITEM_LINKING_POLICY_ID
            # this particular policy does not need any other parameter

        

        # check if we have value in all the required params or not
        raiseErrorIfRequiredParamMissing(paramArray, paramNameArray, policy_type)

        policyConfigurationToCreate = PolicyConfiguration(is_blocking=isBlocking, is_enabled=isEnabled)
        scope = [
            {
                'repositoryId': repository_id,
                'refName': branch,
                'matchKind': 'exact'
            }
        ]
        policyConfigurationToCreate.settings = {
            'scope': scope
            }

        policyConfigurationToCreate.type = {
            'id' : policytypeId
        }

        index = 0
        for param in paramNameArray:
            policyConfigurationToCreate.settings[param] = paramArray[index]
            index = index + 1

        return policy_client.create_policy_configuration(configuration=policyConfigurationToCreate, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)
    

def raiseErrorIfRequiredParamMissing(paramArray, paramNameArray, policyName):
    if not paramNameArray:
        return
    if any(v is None for v in paramArray):
        raise CLIError('{} are required for {}'.format('--' + ' --'.join(paramNameArray), policyName))


def nameOfArray(exp):
    frame = sys._getframe(1)
    fname = frame.f_code.co_filename
    line = frame.f_lineno
    with open(fname) as f:
        line = f.read().split('\n')[line - 1]
    start = line.find('nameOfArray([') + 13
    end = line.find('])', start)
    linePassedToFunction = line[start:end]
    return [x.strip() for x in linePassedToFunction.split(',')]
