# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import ArgumentsContext, enum_choice_list

# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_YES_NO_SWITCH_VALUES = ['yes', 'no']
_OUTPUT_VALUES = ['json', 'jsonc', 'table', 'tsv']
_SOURCE_CONTROL_VALUES = ['git', 'tfvc']
_STATE_VALUES = ['invalid', 'unchanged', 'all', 'new', 'wellformed', 'deleting', 'createpending']


def load_team_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'login') as ac:
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with ArgumentsContext(cli_command_loader, 'logout') as ac:
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with ArgumentsContext(cli_command_loader, 'configure') as ac:
        ac.argument('defaults', options_list=('--defaults', '-d'), nargs='*')
    with ArgumentsContext(cli_command_loader, 'project') as ac:
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('process', options_list=('--process', '-p'))
        ac.argument('source_control', options_list=('--source-control', '-s'),
                    **enum_choice_list(_SOURCE_CONTROL_VALUES))
        ac.argument('description', options_list=('--description', '-d'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        ac.argument('state', **enum_choice_list(_STATE_VALUES))
        ac.argument('project_id', options_list='--id')
    with ArgumentsContext(cli_command_loader, 'configure') as ac:
        ac.argument('collect_telemetry', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        ac.argument('enable_log_file', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        ac.argument('use_git_aliases', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        ac.argument('suppress_update_message', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        ac.argument('default_output', **enum_choice_list(_OUTPUT_VALUES))
        ac.argument('list_config', options_list=('--list', '-l'))
