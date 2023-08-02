# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list
from azure.cli.core.commands.parameters import get_enum_type, get_three_state_flag

# CUSTOM CHOICE LISTS
_BRANCH_MATCH_KIND_VALUES = ['prefix', 'exact']
_VOTE_VALUES = ['approve', 'approve-with-suggestions', 'reset', 'wait-for-author', 'reject']
_PR_STATUS_VALUES = ['all', 'active', 'completed', 'abandoned']
_PR_TARGET_STATUS_VALUES = ['active', 'completed', 'abandoned']


# pylint: disable=too-many-statements
def load_code_arguments(self, _):
    with self.argument_context('repos') as context:
        context.argument('repository', options_list=('--repository', '-r'))
        context.argument('reviewers', nargs='*')

    with self.argument_context('repos policy') as context:
        context.argument('policy_configuration', options_list=('--policy-configuration', '--config'),
                         help='Local file path for configuration file. ' +
                         'Please use \\backslash when typing in directory path.')
        context.argument('policy_id', options_list=('--policy-id', '--id'),
                         help='ID of the policy.')
        context.argument('repository_id', help='Id of the repository on which to apply the policy')
        context.argument('branch', help='Branch on which this policy should be applied. For example: master')
        context.argument('branch_match_type', arg_type=get_enum_type(_BRANCH_MATCH_KIND_VALUES),
                         help='Determines how the branch argument is used to apply a policy. ' +
                         'If value is \'exact\', the policy will be applied on a branch which has an ' +
                         'exact match on the --branch argument. ' +
                         'If value is \'prefix\' the policy is applied across all branch folders that ' +
                         'match the prefix provided by the --branch argument.')
        context.argument('blocking', arg_type=get_three_state_flag(),
                         help='Whether the policy should be blocking or not')
        context.argument('enabled', arg_type=get_three_state_flag(),
                         help='Whether the policy is enabled or not')
        context.argument('path_filter',
                         help='Filter path(s) on which the policy is applied. ' +
                         'Supports absolute paths, wildcards and multiple paths separated by \';\'. ' +
                         'Example: /WebApp/Models/Data.cs, /WebApp/* or *.cs,' +
                         '/WebApp/Models/Data.cs;ClientApp/Models/Data.cs')

    with self.argument_context('repos policy list') as context:
        context.argument('branch',
                         help='Branch name to filter results by exact match of branch name. ' +
                         'The --repository-id parameter is required to use the branch filter. ' +
                         'For example: --branch master')
        context.argument('repository_id',
                         help='ID of the repository to filter results by exact match of the repository ID. ' +
                         'For example --repository-ID e556f204-53c9-4153-9cd9-ef41a11e3345')

    with self.argument_context('repos policy approver-count') as context:
        context.argument('minimum_approver_count',
                         help='Minimum number of approvers required. For example: 2')
        context.argument('creator_vote_counts', arg_type=get_three_state_flag(),
                         help='Whether the creator\'s vote counts or not.')
        context.argument('allow_downvotes', arg_type=get_three_state_flag(),
                         help='Whether to allow downvotes or not.')
        context.argument('reset_on_source_push', arg_type=get_three_state_flag(),
                         help='Whether to reset source on push.')

    with self.argument_context('repos policy merge-strategy') as context:
        context.argument('use_squash_merge', arg_type=get_three_state_flag(),
                         help='Whether to squash merge always. '
                         'This option does not work for allowing other merge types.',
                         deprecate_info=context.deprecate(redirect='--allow-squash', target='--use-squash-merge',
                                                          hide=True))
        context.argument('allow_squash', arg_type=get_three_state_flag(),
                         help='Squash merge - Creates a linear history by condensing the source branch commits '
                         'into a single new commit on the target branch.')
        context.argument('allow_rebase', arg_type=get_three_state_flag(),
                         help='Rebase and fast-forward - Creates a linear history by replaying the source branch '
                         'commits onto the target without a merge commit.')
        context.argument('allow_no_fast_forward', arg_type=get_three_state_flag(),
                         help='Basic merge (no fast-forward) - Preserves nonlinear history exactly as it happened '
                         'during development.')
        context.argument('allow_rebase_merge', arg_type=get_three_state_flag(),
                         help='Rebase with merge commit - Creates a semi-linear history by replaying the source '
                         'branch commits onto the target and then creating a merge commit.')

    with self.argument_context('repos policy build') as context:
        context.argument('build_definition_id', help='Build Definition Id.')
        context.argument('queue_on_source_update_only', arg_type=get_three_state_flag(),
                         help='Queue Only on source update.')
        context.argument('manual_queue_only', arg_type=get_three_state_flag(),
                         help='Whether to allow only manual queue of builds.')
        context.argument('display_name',
                         help='Display name for this build policy to identify the policy. ' +
                         'For example: \'Manual queue policy\'')
        context.argument('valid_duration', help='Policy validity duration (in minutes).')

    with self.argument_context('repos policy file-size') as context:
        context.argument('maximum_git_blob_size',
                         help='Maximum git blob size in bytes. ' +
                         'For example, to specify a 10byte limit, --maximum-git-blob-size 10.')
        context.argument('use_uncompressed_size', arg_type=get_three_state_flag(),
                         help='Whether to use uncompressed size.')

    with self.argument_context('repos policy required-reviewer') as context:
        context.argument('required_reviewer_ids',
                         help='Required reviewers email addresses separated by \';\'. ' +
                         'For example: john@contoso.com;alice@contoso.com')
        context.argument('message', help='Message.')

    with self.argument_context('repos pr') as context:
        context.argument('description', type=str, options_list=('--description', '-d'), nargs='*')
        context.argument('source_branch', options_list=('--source-branch', '-s'))
        context.argument('target_branch', options_list=('--target-branch', '-t'))
        context.argument('title', type=str)

    with self.argument_context('repos pr create') as context:
        context.argument('work_items', nargs='*')
        context.argument('draft', arg_type=get_three_state_flag())
        context.argument('auto_complete', arg_type=get_three_state_flag())
        context.argument('squash', arg_type=get_three_state_flag())
        context.argument('delete_source_branch', arg_type=get_three_state_flag())
        context.argument('bypass_policy', arg_type=get_three_state_flag())
        context.argument('transition_work_items', arg_type=get_three_state_flag())
        context.argument('optional_reviewers', options_list=('--reviewers', '--optional-reviewers'))


    with self.argument_context('repos pr list') as context:
        context.argument('status', **enum_choice_list(_PR_STATUS_VALUES))

    with self.argument_context('repos pr reviewer') as context:
        context.argument('reviewers', nargs='+')

    with self.argument_context('repos pr work-item') as context:
        context.argument('work_items', nargs='+')

    with self.argument_context('repos pr update') as context:
        context.argument('auto_complete', arg_type=get_three_state_flag())
        context.argument('squash', arg_type=get_three_state_flag())
        context.argument('delete_source_branch', arg_type=get_three_state_flag())
        context.argument('bypass_policy', arg_type=get_three_state_flag())
        context.argument('transition_work_items', arg_type=get_three_state_flag())
        context.argument('draft', arg_type=get_three_state_flag())
        context.argument('status', **enum_choice_list(_PR_TARGET_STATUS_VALUES))

    with self.argument_context('repos pr policy') as context:
        context.argument('evaluation_id', options_list=('--evaluation-id', '-e'))

    with self.argument_context('repos pr set-vote') as context:
        context.argument('vote', **enum_choice_list(_VOTE_VALUES))

    with self.argument_context('repos delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')

    with self.argument_context('repos import create') as context:
        context.argument('git_source_url', options_list=('--git-source-url', '--git-url'))

    with self.argument_context('repos ref') as context:
        context.argument('repository', options_list=('--repository', '-r'))
        context.argument('object_id', options_list=('--object-id'))
