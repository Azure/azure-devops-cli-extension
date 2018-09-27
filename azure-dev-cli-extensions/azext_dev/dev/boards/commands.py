# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import (transform_work_item_table_output,
                      transform_work_item_query_result_table_output)

from .work_item import show_work_item, create_work_item, query_work_items, update_work_item

def load_work_commands(self, _):
    with self.command_group('dev work item') as g:
        g.custom_command('show', 'dev.boards.work_item.show_work_item', table_transformer=transform_work_item_table_output)
        g.custom_command('create', 'dev.boards.work_item.create_work_item', table_transformer=transform_work_item_table_output)
        g.custom_command('query', 'dev.boards.work_item.query_work_items', table_transformer=transform_work_item_query_result_table_output)
        g.custom_command('update', 'dev.boards.work_item.update_work_item', table_transformer=transform_work_item_table_output)