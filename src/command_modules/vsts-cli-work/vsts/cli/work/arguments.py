# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_work_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'work') as ac:
        ac.argument('open_browser', options_list='--open')
        ac.argument('project', options_list=('--project', '-p'))
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with ArgumentsContext(cli_command_loader, 'work item') as ac:
        ac.argument('work_item_id', type=int, options_list='--id')
        ac.argument('work_item_type', type=str, options_list='--type')
        ac.argument('fields', nargs='*', options_list=('--fields', '-f'))

    with ArgumentsContext(cli_command_loader, 'work item query') as ac:
        ac.argument('query_id', type=str, options_list='--id')

    with ArgumentsContext(cli_command_loader, 'work item relation') as ac:
        ac.argument('work_item_id', type=int, options_list='--id')

    with ArgumentsContext(cli_command_loader, 'work item relation add') as ac:
        ac.argument('relations', nargs='*', options_list=('--relations', '-r'))

    with ArgumentsContext(cli_command_loader, 'work item relation remove') as ac:
        ac.argument('indexes', type=str, options_list=('--indexes'))
