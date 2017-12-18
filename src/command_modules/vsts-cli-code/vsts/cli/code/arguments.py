# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list, ArgumentsContext

# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_VOTE_VALUES = ['approve', 'approve-with-suggestions', 'reset', 'wait-for-author', 'reject']
_PR_STATUS_VALUES = ['all', 'active', 'completed', 'abandoned']


def load_code_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'code') as ac:
        ac.argument('open_browser', options_list='--open')
        ac.argument('project', options_list=('--project', '-p'))
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('reviewers', nargs='*')
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with ArgumentsContext(cli_command_loader, 'code pr') as ac:
        ac.argument('description', type=str, options_list=('--description', '-d'))
        ac.argument('pull_request_id', type=int, options_list='--id')
        ac.argument('repository', options_list=('--repository', '-r'))
        ac.argument('source_branch', options_list=('--source-branch', '-s'))
        ac.argument('target_branch', options_list=('--target-branch', '-t'))
        ac.argument('title', type=str)

    with ArgumentsContext(cli_command_loader, 'code pr create') as ac:
        ac.argument('work_items', nargs='*')

    with ArgumentsContext(cli_command_loader, 'code pr list') as ac:
        ac.argument('status', **enum_choice_list(_PR_STATUS_VALUES))

    with ArgumentsContext(cli_command_loader, 'code pr reviewers') as ac:
        ac.argument('reviewers', nargs='+')

    with ArgumentsContext(cli_command_loader, 'code pr work-items') as ac:
        ac.argument('work_items', nargs='+')

    with ArgumentsContext(cli_command_loader, 'code pr update') as ac:
        ac.argument('auto_complete', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        ac.argument('squash', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        ac.argument('delete_source_branch', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        ac.argument('bypass_policy', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with ArgumentsContext(cli_command_loader, 'code pr policies') as ac:
        ac.argument('evaluation_id', options_list=('--evaluation-id', '-e'))

    with ArgumentsContext(cli_command_loader, 'code pr set-vote') as ac:
        ac.argument('vote', **enum_choice_list(_VOTE_VALUES))

    with ArgumentsContext(cli_command_loader, 'code repo') as ac:
        ac.argument('repo_id', options_list='--id')

    with ArgumentsContext(cli_command_loader, 'code tag') as ac:
        ac.argument('repository', options_list=('--repository', '-r'))
        ac.argument('object-id', options_list=('--object-id'))

    with ArgumentsContext(cli_command_loader, 'code tag create') as ac:
        ac.argument('name', options_list=('--name', '-n'))
        ac.argument('message', options_list=('--message', '-m'))
