# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import ArgumentsContext, enum_choice_list

# CUSTOM CHOICE LISTS
_on_off_switch_values = ['on', 'off']


def load_team_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'team') as ac:
        ac.argument('team_instance', options_list=('--team-instance', '-i'))
        ac.argument('detect', **enum_choice_list(_on_off_switch_values))
