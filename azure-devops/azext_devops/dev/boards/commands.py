# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_work_item_table_output,
                      transform_work_item_query_result_table_output)


workItemOps = CliCommandType(
    operations_tmpl='azext_devops.dev.boards.work_item#{}',
    exception_handler=azure_devops_exception_handler
)


def load_work_commands(self, _):
    with self.command_group('boards', command_type=workItemOps) as g:
        # basic work item commands
        g.command('work-item show', 'show_work_item', table_transformer=transform_work_item_table_output)
        g.command('work-item create', 'create_work_item', table_transformer=transform_work_item_table_output)
        g.command('work-item update', 'update_work_item', table_transformer=transform_work_item_table_output)
        g.command('work-item delete', 'delete_work_item',
                  confirmation='Are you sure you want to delete this work item?')

        # query commands
        g.command('query', 'query_work_items', table_transformer=transform_work_item_query_result_table_output)
