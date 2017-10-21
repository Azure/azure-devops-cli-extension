# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list, ArgumentsContext

# CUSTOM CHOICE LISTS
_on_off_switch_values = ['on', 'off']
_vote_values = ['approve', 'approve-with-suggestions', 'reset', 'wait-for-author', 'reject']
_pr_status_values = ['all', 'active', 'completed', 'abandoned']


def load_code_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'code') as ac:
        ac.argument('open_browser', options_list='--open')
        ac.argument('project', options_list=('--team-project', '-p'))
        ac.argument('team_instance', options_list=('--team-instance', '-i'))
        ac.argument('reviewers', nargs='*')
        ac.argument('detect', **enum_choice_list(_on_off_switch_values))

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
        ac.argument('status', **enum_choice_list(_pr_status_values))

    with ArgumentsContext(cli_command_loader, 'code pr reviewers') as ac:
        ac.argument('reviewers', nargs='+')

    with ArgumentsContext(cli_command_loader, 'code pr work-items') as ac:
        ac.argument('work_items', nargs='+')
        
    with ArgumentsContext(cli_command_loader, 'code pr update') as ac:
        ac.argument('auto_complete', **enum_choice_list(_on_off_switch_values))
        ac.argument('squash', **enum_choice_list(_on_off_switch_values))
        ac.argument('delete_source_branch', **enum_choice_list(_on_off_switch_values))
        ac.argument('bypass_policy', **enum_choice_list(_on_off_switch_values))

    with ArgumentsContext(cli_command_loader, 'code pr policies') as ac:
        ac.argument('evaluation_id', options_list=('--evaluation-id', '-e'))

    with ArgumentsContext(cli_command_loader, 'code pr set-vote') as ac:
        ac.argument('vote', **enum_choice_list(_vote_values))
