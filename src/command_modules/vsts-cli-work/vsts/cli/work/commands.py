# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_work_item_table_output
from knack.commands import CommandSuperGroup


def load_work_commands(cli_command_loader):
    with CommandSuperGroup(__name__, cli_command_loader, 'vsts.cli.work.common.custom#{}') as sg:
        with sg.group('work') as g:
            g.command('item show', 'show_work_item',
                      table_transformer=transform_work_item_table_output)
            g.command('item create', 'create_work_item',
                      table_transformer=transform_work_item_table_output)
            g.command('item update', 'update_work_item',
                      table_transformer=transform_work_item_table_output)
            g.command('setup-git-aliases', 'setup_git_aliases')
