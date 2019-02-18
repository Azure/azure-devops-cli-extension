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


def load_code_arguments(self, _):
    with self.argument_context('repos') as context:
        context.argument('project', options_list=('--project', '-p'))
        context.argument('organization', options_list=('--organization', '--org'))
        context.argument('repository', options_list=('--repository', '-r'))
        context.argument('reviewers', nargs='*')
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('repos policy') as context:
        context.argument('policy_configuration', options_list=('--policy-configuration', '--config'),
                         help='File path of file containing policy configuration to create in a serialized form. ' +
                         'please use / backslash when typing in directory path. '
                         +'Only --project and --organization param are needed when passing this.')
        context.argument('policy_id', options_list=('--policy-id', '--id'),
                         help='ID of the policy which needs to be updated')

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
