# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import (transform_work_item_table_output,
                      transform_work_item_query_result_table_output)


def load_work_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'work', 'vsts.cli.work.common.custom#{}') as g:
        g.command('item show', 'show_work_item',
                  table_transformer=transform_work_item_table_output)
        g.command('item create', 'create_work_item',
                  table_transformer=transform_work_item_table_output)
        g.command('item query', 'query_work_items',
                  table_transformer=transform_work_item_query_result_table_output)
        g.command('item update', 'update_work_item',
                  table_transformer=transform_work_item_table_output)
