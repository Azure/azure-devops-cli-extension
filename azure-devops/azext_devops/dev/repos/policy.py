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


def create_policy_configuration_file(policy_configuration, organization=None, project=None, detect=None):
    """Create a policy using configuration provided through configuration file
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
        with open(policy_configuration) as f:
            import json
            configuration = json.load(f)
            return policy_client.create_policy_configuration(configuration=configuration, project=project)
    except VstsServiceError as ex:
        raise CLIError(ex)

def update_policy_configuration_file(policy_id, policy_configuration, organization=None, project=None, detect=None):
    """Updates a policy using configuration provided through configuration file
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
        with open(policy_configuration) as f:
            import json
            configuration = json.load(f)
            return policy_client.update_policy_configuration(
                configuration=configuration,
                project=project,
                configuration_id=policy_id)
    except VstsServiceError as ex:
        raise CLIError(ex) 