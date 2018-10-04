# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.commands import CommandGroup
from knack.prompting import prompt_y_n
from ._format import (transform_work_item_table_output,
                      transform_work_item_query_result_table_output)

from .work_item import show_work_item, create_work_item, query_work_items, update_work_item, delete_work_item

def workitem_delete_confirmation(command_args):
    return bool(prompt_y_n('Are you sure you want to delete this work item?'))

def load_work_commands(self, _):
    with self.command_group('boards') as g:
        g.custom_command('show', 'dev.boards.work_item.show_work_item', table_transformer=transform_work_item_table_output)
        g.custom_command('create', 'dev.boards.work_item.create_work_item', table_transformer=transform_work_item_table_output)
        g.custom_command('query', 'dev.boards.work_item.query_work_items', table_transformer=transform_work_item_query_result_table_output)
        g.custom_command('update', 'dev.boards.work_item.update_work_item', table_transformer=transform_work_item_table_output)
        g.custom_command('delete', 'dev.boards.work_item.delete_work_item', confirmation=workitem_delete_confirmation )