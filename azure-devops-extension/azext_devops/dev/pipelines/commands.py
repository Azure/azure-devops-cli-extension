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

from azure.cli.core.commands import CliCommandType

buildOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.build#{}'
)

buildDefOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.build_definition#{}'
)

buildTaskOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.task#{}'
)

def load_build_commands(self, _):
    with self.command_group('pipelines build', command_type=buildOps) as g:
        # basic vsts_cli_build commands
        g.command('list', 'build_list', table_transformer=transform_builds_table_output)
        g.command('queue', 'build_queue', table_transformer=transform_build_table_output)
        g.command('show', 'build_show', table_transformer=transform_build_table_output)

    with self.command_group('pipelines build definition', command_type=buildDefOps) as g:
        # basic vsts_cli_build definition commands
        g.command('list', 'build_definition_list', table_transformer=transform_definitions_table_output)
        g.command('show', 'build_definition_show', table_transformer=transform_definition_table_output)

    with self.command_group('pipelines build task', command_type=buildTaskOps) as g:
        # basic vsts_cli_build task commands
        g.command('list', 'task_list', table_transformer=transform_tasks_table_output)
        g.command('show', 'task_show', table_transformer=transform_task_table_output)
