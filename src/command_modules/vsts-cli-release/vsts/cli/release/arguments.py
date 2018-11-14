# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_release_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'release') as ac:
        ac.argument('open_browser', options_list='--open')
        ac.argument('project', options_list=('--project', '-p'))
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with ArgumentsContext(cli_command_loader, 'release list') as ac:
        ac.argument('definition_id', nargs='*', type=int)

    with ArgumentsContext(cli_command_loader, 'release create') as ac:
        ac.argument('definition_id', type=int)
        ac.argument('artifact_metadata_list', nargs='*')

    with ArgumentsContext(cli_command_loader, 'release show') as ac:
        ac.argument('release_id', options_list='--id', type=int)

    with ArgumentsContext(cli_command_loader, 'release definition show') as ac:
        ac.argument('definition_id', options_list='--id', type=int)

    with ArgumentsContext(cli_command_loader, 'release definition update') as ac:
        ac.argument('filename', options_list=('--filename', '-f'))
