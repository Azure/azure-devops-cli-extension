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
                  buildDefinitionId=None, queueOnSourceUpdateOnly=None, manualQueueOnly=None, displayName=None, validDuration=None,
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
        typeId = ''

        if(policy_type == APPROVER_COUNT_POLICY):
            if any(v is None for v in [minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush]):
                paramNameArray = nameOfArray([minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush])
                raise CLIError('{} are required for ApproverCountPolicy'.format('--' + ' --'.join(paramNameArray)))

            typeId = APPROVER_COUNT_POLICY_ID
            paramNameArray = nameOfArray([minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush])
            paramArray = [minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush]

        elif(policy_type == BUILD_POLICY):
            if any(v is None for v in [buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration]):
                paramNameArray = nameOfArray([buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration])
                raise CLIError('{} are required for ApproverCountPolicy'.format('--' + ' --'.join(paramNameArray)))

            typeId = BUILD_POLICY_ID
            paramNameArray = nameOfArray([buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration])
            paramArray = [buildDefinitionId, queueOnSourceUpdateOnly, manualQueueOnly, displayName, validDuration]

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
            'id' : typeId
        }

        index = 0
        for param in paramNameArray:
            policyConfigurationToCreate.settings[param] = paramArray[index]
            index = index + 1

        return policy_client.create_policy_configuration(configuration=policyConfigurationToCreate, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)
    

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
