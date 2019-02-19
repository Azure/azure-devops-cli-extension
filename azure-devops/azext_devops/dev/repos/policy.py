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
    :param repository_id: Id (UUID) of the repository.
    :type repository_id: string
    :param branch: Branch. (--repository-id is required)
    :type branch: string
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
                                 minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push,
                                 organization=None, project=None, detect=None):
    """Create approver count policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        param_name_array = ['minimumApproverCount', 'creatorVoteCounts', 'allowDownvotes', 'resetOnSourcePush']
        param_value_array = [minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push]
        configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                        'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd',
                        param_name_array, param_value_array)

        return policy_client.create_policy_configuration(configuration=configuration, project=project)

    except VstsServiceError as ex:
        raise CLIError(ex)

def update_policy_approver_count(policy_id,
                                 repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                 minimum_approver_count=None, creator_vote_counts=None, allow_downvotes=None, reset_on_source_push=None,
                                 organization=None, project=None, detect=None):
    """Update approver count policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
        param_name_array = ['minimumApproverCount', 'creatorVoteCounts', 'allowDownvotes', 'resetOnSourcePush']
        
        current_setting = current_policy.settings
        current_scope = current_policy.settings['scope'][0]

        param_value_array = [
           minimum_approver_count or current_setting.get('minimumApproverCount', None),
           creator_vote_counts or current_setting.get('creatorVoteCounts', None),
           allow_downvotes or current_setting.get('allowDownvotes', None),
           reset_on_source_push or current_setting.get('resetOnSourcePush', None)
        ]

        updated_configuration = create_configuration_object(
            repository_id or current_scope['repositoryId'],
            branch or current_scope['refName'],
            is_blocking or str(current_policy.is_blocking),
            is_enabled or str(current_policy.is_enabled),
            'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd',
            param_name_array,
            param_value_array
        )

        return policy_client.update_policy_configuration(
            configuration=updated_configuration,
            project=project,
            configuration_id=policy_id
        )

    except VstsServiceError as ex:
        raise CLIError(ex)


def create_policy_merge_strategy(repository_id, branch, is_blocking, is_enabled,
                                 use_squash_merge,
                                 organization=None, project=None, detect=None):
    """Create merge strategy policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        param_name_array = ['useSquashMerge']
        param_value_array = [use_squash_merge]
        configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                        'fa4e907d-c16b-4a4c-9dfa-4916e5d171ab',
                        param_name_array, param_value_array)

        return policy_client.create_policy_configuration(configuration=configuration, project=project)

    except VstsServiceError as ex:
        raise CLIError(ex)

def update_policy_merge_strategy(policy_id,
                                 repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                 use_squash_merge=None,
                                 organization=None, project=None, detect=None):
    """Update merge strategy policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
        param_name_array = ['useSquashMerge']
        
        current_setting = current_policy.settings
        current_scope = current_policy.settings['scope'][0]

        param_value_array = [
           use_squash_merge or current_setting.get('useSquashMerge', None)
        ]

        updated_configuration = create_configuration_object(
            repository_id or current_scope['repositoryId'],
            branch or current_scope['refName'],
            is_blocking or str(current_policy.is_blocking),
            is_enabled or str(current_policy.is_enabled),
            'fa4e907d-c16b-4a4c-9dfa-4916e5d171ab',
            param_name_array,
            param_value_array
        )

        return policy_client.update_policy_configuration(
            configuration=updated_configuration,
            project=project,
            configuration_id=policy_id
        )

    except VstsServiceError as ex:
        raise CLIError(ex)

def create_policy_build(repository_id, branch, is_blocking, is_enabled,
                        build_definition_id, queue_on_source_update_only, manual_queue_only, display_name, valid_duration,
                        organization=None, project=None, detect=None):
    """Create build policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        param_name_array = ['buildDefinitionId', 'queueOnSourceUpdateOnly', 'manualQueueOnly', 'displayName', 'validDuration']
        param_value_array = [build_definition_id, queue_on_source_update_only, manual_queue_only, display_name, valid_duration]
        configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                        '0609b952-1397-4640-95ec-e00a01b2c241',
                        param_name_array, param_value_array)

        return policy_client.create_policy_configuration(configuration=configuration, project=project)

    except VstsServiceError as ex:
        raise CLIError(ex)
        
def update_policy_build(policy_id,
                        repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                        build_definition_id=None, queue_on_source_update_only=None, manual_queue_only=None, display_name=None, valid_duration=None,
                        organization=None, project=None, detect=None):
    """Update build policy
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        policy_client = get_policy_client(organization)
        current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
        param_name_array = ['buildDefinitionId', 'queueOnSourceUpdateOnly', 'manualQueueOnly', 'displayName', 'validDuration']
        
        current_setting = current_policy.settings
        current_scope = current_policy.settings['scope'][0]

        param_value_array = [
           build_definition_id or current_setting.get('buildDefinitionId', None),
           queue_on_source_update_only or current_setting.get('queueOnSourceUpdateOnly', None),
           manual_queue_only or current_setting.get('manualQueueOnly', None),
           display_name or current_setting.get('displayName', None),
           valid_duration or current_setting.get('validDuration', None)
        ]

        updated_configuration = create_configuration_object(
            repository_id or current_scope['repositoryId'],
            branch or current_scope['refName'],
            is_blocking or str(current_policy.is_blocking),
            is_enabled or str(current_policy.is_enabled),
            '0609b952-1397-4640-95ec-e00a01b2c241',
            param_name_array,
            param_value_array
        )

        return policy_client.update_policy_configuration(
            configuration=updated_configuration,
            project=project,
            configuration_id=policy_id
        )

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