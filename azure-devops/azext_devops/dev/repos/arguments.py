# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list
from azext_devops.dev.common.const import REPO_POLICY_TYPE

# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_TRUE_FALSE_SWITCH = ['true', 'false']
_VOTE_VALUES = ['approve', 'approve-with-suggestions', 'reset', 'wait-for-author', 'reject']
_PR_STATUS_VALUES = ['all', 'active', 'completed', 'abandoned']


def repo_policy_create_udpate_common_arguments(context):
    context.argument('is_blocking', **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('is_enabled', **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('policy_type', **enum_choice_list(REPO_POLICY_TYPE))
    context.argument('repository_id', options_list=('--repository-id', '-r'))
    APPROVER_COUNT_POLICY_ARGUMENT_GROUP = 'Approver Count Policy'
    context.argument('minimum_approver_count', arg_group=APPROVER_COUNT_POLICY_ARGUMENT_GROUP)
    context.argument('creator_vote_counts', arg_group=APPROVER_COUNT_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('allow_downvotes', arg_group=APPROVER_COUNT_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('reset_on_source_push', arg_group=APPROVER_COUNT_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    MERGE_STRATEGY_POLICY_ARGUMENT_GROUP = 'Merge Strategy Policy'
    context.argument('use_squash_merge', arg_group=MERGE_STRATEGY_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    BUILD_POLICY_ARGUMENT_GROUP = 'Build Policy'
    context.argument('build_definition_id', arg_group=BUILD_POLICY_ARGUMENT_GROUP)
    context.argument('queue_on_source_update_only', arg_group=BUILD_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('manual_queue_only', arg_group=BUILD_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    context.argument('display_name', arg_group=BUILD_POLICY_ARGUMENT_GROUP)
    context.argument('valid_duration', arg_group=BUILD_POLICY_ARGUMENT_GROUP)
    FILE_SIZE_POLICY_ARGUMENT_GROUP = 'File Size Policy'
    context.argument('maximum_git_blob_size_in_bytes', arg_group=FILE_SIZE_POLICY_ARGUMENT_GROUP)
    context.argument('use_uncompressed_size', arg_group=FILE_SIZE_POLICY_ARGUMENT_GROUP,
                     **enum_choice_list(_TRUE_FALSE_SWITCH))
    REQUIRED_REVIEWER_POLICY_GROUP = 'Required Reviewer Policy'
    context.argument('optional_reviewer_ids', arg_group=REQUIRED_REVIEWER_POLICY_GROUP)
    context.argument('required_reviewer_ids', arg_group=REQUIRED_REVIEWER_POLICY_GROUP)
    context.argument('message', arg_group=REQUIRED_REVIEWER_POLICY_GROUP)


def load_code_arguments(self, _):
    with self.argument_context('repos') as context:
        context.argument('project', options_list=('--project', '-p'))
        context.argument('organization', options_list=('--organization', '--org'))
        context.argument('repository', options_list=('--repository', '-r'))
        context.argument('reviewers', nargs='*')
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('repos policy create') as context:
        repo_policy_create_udpate_common_arguments(context)

    with self.argument_context('repos policy update') as context:
        repo_policy_create_udpate_common_arguments(context)
        context.argument('policy_id', options_list=('--policy-id', '--id'))

    with self.argument_context('repos pr') as context:
        context.argument('description', type=str, options_list=('--description', '-d'), nargs='*')
        context.argument('source_branch', options_list=('--source-branch', '-s'))
        context.argument('target_branch', options_list=('--target-branch', '-t'))
        context.argument('title', type=str)

    with self.argument_context('repos pr create') as context:
        context.argument('work_items', nargs='*')

    with self.argument_context('repos pr list') as context:
        context.argument('status', **enum_choice_list(_PR_STATUS_VALUES))

    with self.argument_context('repos pr reviewer') as context:
        context.argument('reviewers', nargs='+')

    with self.argument_context('repos pr work-item') as context:
        context.argument('work_items', nargs='+')

    with self.argument_context('repos pr update') as context:
        context.argument('auto_complete', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('squash', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('delete_source_branch', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('bypass_policy', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('transition_work_items', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('repos pr policy') as context:
        context.argument('evaluation_id', options_list=('--evaluation-id', '-e'))

    with self.argument_context('repos pr set-vote') as context:
        context.argument('vote', **enum_choice_list(_VOTE_VALUES))

    with self.argument_context('repos delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')

    with self.argument_context('repos import create') as context:
        context.argument('git_source_url', options_list=('--git-source-url', '--git-url'))
