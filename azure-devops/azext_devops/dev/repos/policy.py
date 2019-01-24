# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

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
                  isBlocking=True, isEnabled=False,
                  policy_type=None,
                  minimumApproverCount=None, creatorVoteCounts=None, allowDownvotes=None, resetOnSourcePush=None,
                  organization=None, project=None, detect=None):
    """
    :param policy_type: Type of policy you want to create
    :type policy_type: string
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

        if(policy_type == APPROVER_COUNT_POLICY):
            if any(v is None for v in [minimumApproverCount, creatorVoteCounts, allowDownvotes, resetOnSourcePush]):
                raise CLIError('--minimumApproverCount, --creatorVoteCounts, --allowDownvotes, --resetOnSourcePush are required for ApproverCountPolicy')

        policyConfigurationToCreate = PolicyConfiguration(is_blocking=isBlocking, is_enabled=isEnabled)

        if(policy_type == APPROVER_COUNT_POLICY):
            policyConfigurationToCreate.type = {
                'id' : APPROVER_COUNT_POLICY_ID
            }

            policyConfigurationToCreate.settings = {
                'minimumApproverCount' : minimumApproverCount,
                'creatorVoteCounts' : creatorVoteCounts,
                'allowDownvotes' : allowDownvotes,
                'resetOnSourcePush' : resetOnSourcePush,
                'scope': [
                    {
                        'repositoryId': repository_id,
                        'refName': branch,
                        'matchKind': 'exact'
                        }]}

        return policy_client.create_policy_configuration(configuration=policyConfigurationToCreate, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)
    
