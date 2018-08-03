# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list, ArgumentsContext

_ORGANIZATION_LICENSE_TYPES_FOR_ADD = ['advanced', 'express', 'professional', 'stakeholder']
_LEVEL_FOR_BANNER = ['info', 'warning', 'error']


def load_admin_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'admin user') as ac:
        ac.argument('user_id', options_list='--id')
        ac.argument('access_level', **enum_choice_list(_ORGANIZATION_LICENSE_TYPES_FOR_ADD))
    with ArgumentsContext(cli_command_loader, 'admin banner') as ac:
        ac.argument('message', options_list=['-m', '--message'])
        ac.argument('message_id', options_list='--id')
        ac.argument('level', options_list=['-l', '--level'], **enum_choice_list(_LEVEL_FOR_BANNER))

