# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list
from azure.cli.core.commands.parameters import get_enum_type

# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_TRUE_FALSE_SWITCH = ['true', 'false']
_VOTE_VALUES = ['approve', 'approve-with-suggestions', 'reset', 'wait-for-author', 'reject']
_PR_STATUS_VALUES = ['all', 'active', 'completed', 'abandoned']


def load_code_arguments(self, _):
    with self.argument_context('repos') as context:
        context.argument('project', options_list=('--project', '-p'))
        context.argument('organization', options_list=('--organization', '--org'))
        context.argument('repository', options_list=('--repository', '-r'))
        context.argument('reviewers', nargs='*')
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('repos policy') as context:
        context.argument('organization', options_list=('--organization', '--org'),
                         help='Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/')
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES),
                         help='Automatically detect organization. Default is "on".')
        context.argument('project', options_list=('--project', '-p'),
                         help='Name or ID of the project.')
        context.argument('policy_configuration', options_list=('--policy-configuration', '--config'),
                         help='File path of file containing policy configuration to create in a serialized form. '
                         +'please use / backslash when typing in directory path. '
                         +'Only --project and --organization param are needed when passing this.')
        context.argument('policy_id', options_list=('--policy-id', '--id'),
                         help='ID of the policy which needs to be updated')
        context.argument('repository_id', help='Id (UUID) of the repository on which to apply the policy')
        context.argument('branch', help='Branch on which this policy should be applied')
        context.argument('is_blocking', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether the policy should be blocking or not')
        context.argument('is_enabled', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether the policy is enabled or not')

    with self.argument_context('repos policy approver-count') as context:
        context.argument('minimum_approver_count',
                         help='Minimum approver count.')
        context.argument('creator_vote_counts', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether the creator\'s vote count counts or not.')
        context.argument('allow_downvotes', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether to allow downvotes or not.')
        context.argument('reset_on_source_push', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether to reset source on push.')

    with self.argument_context('repos policy merge-strategy') as context:
        context.argument('use_squash_merge', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether to squash merge always.')

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
