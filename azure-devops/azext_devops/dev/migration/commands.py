# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import transform_migrations_table_output, transform_migration_table_output, transform_message_output


migrationOps = CliCommandType(
    operations_tmpl='azext_devops.dev.migration.migration#{}',
    exception_handler=azure_devops_exception_handler
)


def load_migration_commands(self, _):
    with self.command_group('devops migrations', command_type=migrationOps, is_preview=True) as g:
        g.command('list', 'list_migrations', table_transformer=transform_migrations_table_output)
        g.command('status', 'get_migration', table_transformer=transform_migration_table_output)
        g.command('create', 'create_migration', table_transformer=transform_migration_table_output)
        g.command('pause', 'pause_migration', table_transformer=transform_message_output)
        g.command('resume', 'resume_migration', table_transformer=transform_migration_table_output)
        g.command('abandon', 'delete_migration',
                  confirmation='Are you sure you want to abandon this migration?',
                  table_transformer=transform_message_output)

    with self.command_group('devops migrations cutover', command_type=migrationOps, is_preview=True) as g:
        g.command('set', 'schedule_cutover', table_transformer=transform_migration_table_output)
        g.command('cancel', 'cancel_cutover', table_transformer=transform_message_output)
