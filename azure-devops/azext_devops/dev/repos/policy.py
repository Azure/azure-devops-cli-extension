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


def create_policy_configuration_file(policy_configuration, organization=None, project=None, detect=None):
    """Create a policy using configuration provided through configuration file
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        with open(policy_configuration) as f:
            import json
            configuration = json.load(f)
            return policy_client.create_policy_configuration(configuration=configuration, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

def update_policy_configuration_file(policy_id, policy_configuration, organization=None, project=None, detect=None):
    """Updates a policy using configuration provided through configuration file
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        with open(policy_configuration) as f:
            import json
            configuration = json.load(f)
            return policy_client.update_policy_configuration(
                configuration=configuration,
                project=project,
                configuration_id=policy_id)
    except VstsServiceError as ex:
        raise CLIError(ex)

def create_policy_approver_count(repository_id, branch, is_blocking, is_enabled,
                                 minimum_approver_count, creator_vote_count, allow_downvotes, reset_on_source_push,
                                 organization=None, project=None, detect=None):
    """Create a approver count policy
    :param minimum_approver_count: Minimum approver count.
    :type minimum_approver_count: int
    :param creator_vote_counts: Whether the creator's vote count counts or not.
    :type creator_vote_counts: bool
    :param allow_downvotes: Whether to allow downvotes or not.
    :type allow_downvotes: bool
    :param reset_on_source_push: Whether to reset source on push.
    :type reset_on_source_push: bool
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        param_name_array = ['minimumApproverCount', 'creatorVoteCounts', 'allowDownvotes', 'resetOnSourcePush']
        param_value_array = [minimum_approver_count, creator_vote_count, allow_downvotes, reset_on_source_push]
        configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                        'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd',
                        param_name_array, param_value_array)

        return policy_client.create_policy_configuration(configuration=configuration, project=project)

    except VstsServiceError as ex:
        raise CLIError(ex)

def create_configuration_object(repository_id, branch, is_blocking, is_enabled, policy_type_id, param_name_array, param_value_array):
    branch = resolve_git_ref_heads(branch)
    policyConfiguration = PolicyConfiguration(is_blocking=parseTrueFalse(is_blocking), is_enabled=parseTrueFalse(is_enabled))
    scope = createScope(repository_id, branch)
    policyConfiguration.settings = {
        'scope': scope
    }
    policyConfiguration.type = {
        'id': policy_type_id
    }

    index = 0
    for param in param_name_array:
        policyConfiguration.settings[param] = param_value_array[index]
        index = index + 1

    return policyConfiguration

def createScope(repository_id, branch):
    scope = [
        {
            'repositoryId': repository_id,
            'refName': branch,
            'matchKind': 'exact'
        }
    ]

    if branch is None:
        scope = [
            {
                'repositoryId': repository_id,                
            }
        ]

    return scope

def parseTrueFalse(inputString):
    if inputString is not None and inputString.lower() == 'true':
        return True

    return False