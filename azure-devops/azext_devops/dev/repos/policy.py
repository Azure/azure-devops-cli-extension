# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# This file a lot of these are intentional because that makes grouping variables easy

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.vstsCompressed.policy.v4_0.models.models import PolicyConfiguration

from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.services import (get_policy_client, resolve_instance_and_project)
from azext_devops.dev.common.identities import resolve_identity_as_id

logger = get_logger(__name__)


def list_policy(organization=None, project=None, repository_id=None, branch=None, detect=None):
    """List all branch policies in a project.
    :param repository_id: Id (UUID) of the repository.
    :type repository_id: string
    :param branch: Branch. (--repository-id is required)
    :type branch: string
    :rtype: [PolicyConfiguration]
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)

        if branch is not None and repository_id is None:
            raise CLIError('--repository-id is required with --branch')

        scope = None

        if repository_id is not None:
            repository_id = repository_id.replace('-', '')
            scope = repository_id
            if branch is not None:
                branch = resolve_git_ref_heads(branch)
                scope = scope + ':' + branch

    policy_client = get_policy_client(organization)
    return policy_client.get_policy_configurations(project=project, scope=scope)


def get_policy(policy_id, organization=None, project=None, detect=None):
    """Show policy details.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    return policy_client.get_policy_configuration(project=project, configuration_id=policy_id)


def delete_policy(policy_id, organization=None, project=None, detect=None):
    """Delete a policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    return policy_client.delete_policy_configuration(project=project, configuration_id=policy_id)


def create_policy_configuration_file(policy_configuration, organization=None, project=None, detect=None):
    '''Create a policy using a configuration file.
    Recommended when creating policies using multiple scopes for a policy.
    See https://aka.ms/azure-devops-cli-docs for more information.
    '''
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    with open(policy_configuration) as f:
        import json
        configuration = json.load(f)
        return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_configuration_file(policy_id, policy_configuration, organization=None, project=None, detect=None):
    """Update a policy using a configuration file.
    Recommended when creating policies using multiple scopes for a policy.
    See https://aka.ms/azure-devops-cli-docs for more information.
    """
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


def create_policy_approver_count(repository_id, branch, is_blocking, is_enabled,
                                 minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push,
                                 organization=None, project=None, detect=None):
    """Create approver count policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    param_name_array = ['minimumApproverCount', 'creatorVoteCounts', 'allowDownvotes', 'resetOnSourcePush']
    param_value_array = [minimum_approver_count, creator_vote_counts, allow_downvotes, reset_on_source_push]
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                'fa4e907d-c16b-4a4c-9dfa-4906e5d171dd',
                                                param_name_array, param_value_array)

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_approver_count(policy_id,
                                 repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                 minimum_approver_count=None, creator_vote_counts=None, allow_downvotes=None, reset_on_source_push=None,
                                 organization=None, project=None, detect=None):
    """Update approver count policy
    """
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


def create_policy_required_reviewer(repository_id, branch, branch_match_type, is_blocking, is_enabled,
                                    message, required_reviewer_ids,
                                    path_filter=None,
                                    organization=None, project=None, detect=None):
    """Create required reviewer policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    requiredReviewerIds = resolveIdentityMailsToIds(required_reviewer_ids, organization)
    policy_client = get_policy_client(organization)
    param_name_array = ['requiredReviewerIds', 'message', 'filenamePatterns']
    param_value_array = [requiredReviewerIds, message, createFileNamePatterns(path_filter)]
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                'fd2167ab-b0be-447a-8ec8-39368250530e',
                                                param_name_array, param_value_array,
                                                branch_match_type)

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_required_reviewer(policy_id,
                                    repository_id=None, branch=None, branch_match_type=None, is_blocking=None, is_enabled=None,
                                    message=None, required_reviewer_ids=None,
                                    path_filter=None,
                                    organization=None, project=None, detect=None):
    """Update required reviewer policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
    param_name_array = ['requiredReviewerIds', 'message', 'filenamePatterns']
    requiredReviewerIds = resolveIdentityMailsToIds(required_reviewer_ids, organization)

    current_setting = current_policy.settings
    current_scope = current_policy.settings['scope'][0]

    param_value_array = [
        requiredReviewerIds or current_setting.get('requiredReviewerIds', None),
        message or current_setting.get('message', None),
        createFileNamePatterns(path_filter) or current_setting.get('filenamePatterns', None)
    ]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        branch or current_scope['refName'],
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        'fd2167ab-b0be-447a-8ec8-39368250530e',
        param_name_array,
        param_value_array,
        branch_match_type or current_scope['matchKind']
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_policy_merge_strategy(repository_id, branch, is_blocking, is_enabled,
                                 use_squash_merge,
                                 organization=None, project=None, detect=None):
    """Create merge strategy policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    param_name_array = ['useSquashMerge']
    param_value_array = [use_squash_merge]
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                'fa4e907d-c16b-4a4c-9dfa-4916e5d171ab',
                                                param_name_array, param_value_array)

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_merge_strategy(policy_id,
                                 repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                 use_squash_merge=None,
                                 organization=None, project=None, detect=None):
    """Update merge strategy policy
    """
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


def create_policy_build(repository_id, branch, branch_match_type, is_blocking, is_enabled,
                        build_definition_id, queue_on_source_update_only, manual_queue_only, display_name, valid_duration,
                        path_filter=None,
                        organization=None, project=None, detect=None):
    """Create build policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    param_name_array = [
        'buildDefinitionId',
        'queueOnSourceUpdateOnly',
        'manualQueueOnly',
        'displayName',
        'validDuration',
        'filenamePatterns']
    param_value_array = [
        build_definition_id,
        queue_on_source_update_only,
        manual_queue_only,
        display_name,
        valid_duration,
        createFileNamePatterns(path_filter)]
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                '0609b952-1397-4640-95ec-e00a01b2c241',
                                                param_name_array, param_value_array,
                                                branch_match_type)

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_build(policy_id,
                        repository_id=None, branch=None, branch_match_type=None, is_blocking=None, is_enabled=None,
                        build_definition_id=None, queue_on_source_update_only=None, manual_queue_only=None, display_name=None, valid_duration=None,
                        path_filter=None,
                        organization=None, project=None, detect=None):
    """Update build policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
    param_name_array = [
        'buildDefinitionId',
        'queueOnSourceUpdateOnly',
        'manualQueueOnly',
        'displayName',
        'validDuration',
        'filenamePatterns']

    current_setting = current_policy.settings
    current_scope = current_policy.settings['scope'][0]

    param_value_array = [
        build_definition_id or current_setting.get('buildDefinitionId', None),
        queue_on_source_update_only or current_setting.get('queueOnSourceUpdateOnly', None),
        manual_queue_only or current_setting.get('manualQueueOnly', None),
        display_name or current_setting.get('displayName', None),
        valid_duration or current_setting.get('validDuration', None),
        createFileNamePatterns(path_filter) or current_setting.get('filenamePatterns', None)
    ]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        branch or current_scope['refName'],
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        '0609b952-1397-4640-95ec-e00a01b2c241',
        param_name_array,
        param_value_array,
        branch_match_type or current_scope['matchKind']
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_policy_file_size(repository_id, is_blocking, is_enabled,
                            maximum_git_blob_size, use_uncompressed_size,
                            organization=None, project=None, detect=None):
    """Create file size policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    param_name_array = ['maximumGitBlobSizeInBytes', 'useUncompressedSize']
    param_value_array = [maximum_git_blob_size, use_uncompressed_size]
    configuration = create_configuration_object(repository_id, None, is_blocking, is_enabled,
                                                '2e26e725-8201-4edd-8bf5-978563c34a80',
                                                param_name_array, param_value_array)

    return policy_client.create_policy_configuration(configuration=configuration, project=project)

def update_policy_file_size(policy_id,
                            repository_id=None, is_blocking=None, is_enabled=None,
                            maximum_git_blob_size=None, use_uncompressed_size=None,
                            organization=None, project=None, detect=None):
    """Update file size policy
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)
    param_name_array = ['maximumGitBlobSizeInBytes', 'useUncompressedSize']

    current_setting = current_policy.settings
    current_scope = current_policy.settings['scope'][0]

    param_value_array = [
        maximum_git_blob_size or current_setting.get('maximumGitBlobSizeInBytes', None),
        use_uncompressed_size or current_setting.get('useUncompressedSize', None)
    ]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        None,
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        '2e26e725-8201-4edd-8bf5-978563c34a80',
        param_name_array,
        param_value_array
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_policy_comment_required(repository_id, branch, is_blocking, is_enabled,
                                   organization=None, project=None, detect=None):
    """Create comment resolution required policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                'c6a1889d-b943-4856-b76f-9e46bb6b0df2', [], [])

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_comment_required(policy_id,
                                   repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                   organization=None, project=None, detect=None):
    """Update comment resolution required policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)

    current_scope = current_policy.settings['scope'][0]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        branch or current_scope['refName'],
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        'c6a1889d-b943-4856-b76f-9e46bb6b0df2',
        [],
        []
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_policy_work_item_linking(repository_id, branch, is_blocking, is_enabled,
                                    organization=None, project=None, detect=None):
    """Create work item linking policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    configuration = create_configuration_object(repository_id, branch, is_blocking, is_enabled,
                                                '40e92b44-2fe1-4dd6-b3d8-74a9c21d0c6e', [], [])

    return policy_client.create_policy_configuration(configuration=configuration, project=project)


def update_policy_work_item_linking(policy_id,
                                    repository_id=None, branch=None, is_blocking=None, is_enabled=None,
                                    organization=None, project=None, detect=None):
    """Update work item linking policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)

    current_scope = current_policy.settings['scope'][0]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        branch or current_scope['refName'],
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        '40e92b44-2fe1-4dd6-b3d8-74a9c21d0c6e',
        [],
        []
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_policy_case_enforcement(repository_id, is_blocking, is_enabled,
                                   organization=None, project=None, detect=None):
    """Create case enforcement policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    configuration = create_configuration_object(repository_id, None, is_blocking, is_enabled,
                                                '40e92b44-2fe1-4dd6-b3d8-74a9c21d0c6e',
                                                ['enforceConsistentCase'],
                                                ['true'])

    return policy_client.create_policy_configuration(configuration=configuration, project=project)

def update_policy_case_enforcement(policy_id,
                                   repository_id=None, is_blocking=None, is_enabled=None,
                                   organization=None, project=None, detect=None):
    """Update case enforcement policy.
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    policy_client = get_policy_client(organization)
    current_policy = policy_client.get_policy_configuration(project=project, configuration_id=policy_id)

    current_scope = current_policy.settings['scope'][0]

    updated_configuration = create_configuration_object(
        repository_id or current_scope['repositoryId'],
        None,
        is_blocking or str(current_policy.is_blocking),
        is_enabled or str(current_policy.is_enabled),
        '40e92b44-2fe1-4dd6-b3d8-74a9c21d0c6e',
        ['enforceConsistentCase'],
        ['true']
    )

    return policy_client.update_policy_configuration(
        configuration=updated_configuration,
        project=project,
        configuration_id=policy_id
    )


def create_configuration_object(repository_id,
                                branch,
                                is_blocking,
                                is_enabled,
                                policy_type_id,
                                param_name_array,
                                param_value_array,
                                branch_match_type='exact'):
    branch = resolve_git_ref_heads(branch)
    policyConfiguration = PolicyConfiguration(is_blocking=parseTrueFalse(is_blocking), is_enabled=parseTrueFalse(is_enabled))
    scope = createScope(repository_id, branch, branch_match_type)
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


def createFileNamePatterns(filePatterns):
    if filePatterns is None:
        return []

    return filePatterns.split(';')


def createScope(repository_id, branch, branch_match_type):
    scope = [
        {
            'repositoryId': repository_id,
            'refName': branch,
            'matchKind': branch_match_type
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


def resolveIdentityMailsToIds(mailList, organization):
    if mailList is None:
        return []

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
