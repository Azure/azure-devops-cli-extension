# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import (transform_build_table_output,
                      transform_builds_table_output,
                      transform_definition_table_output,
                      transform_definitions_table_output,
                      transform_tasks_table_output,
                      transform_task_table_output)
from knack.commands import CommandGroup


def load_build_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'build', 'vsts.cli.build.common.{}') as g:
        # basic vsts_cli_build commands
        g.command('list', 'build#build_list',
                  table_transformer=transform_builds_table_output)
        g.command('queue', 'build#build_queue',
                  table_transformer=transform_build_table_output)
        g.command('show', 'build#build_show',
                  table_transformer=transform_build_table_output)

        # basic vsts_cli_build definition commands
        g.command('definition list', 'build_definition#build_definition_list',
                  table_transformer=transform_definitions_table_output)
        g.command('definition show', 'build_definition#build_definition_show',
                  table_transformer=transform_definition_table_output)

        # basic vsts_cli_build task commands
        g.command('task list', 'task#task_list', table_transformer=transform_tasks_table_output)
        g.command('task show', 'task#task_show', table_transformer=transform_task_table_output)
