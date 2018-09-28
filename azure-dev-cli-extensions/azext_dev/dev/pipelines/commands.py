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

from .build import build_list, build_queue, build_show
from .build_definition import build_definition_list, build_definition_show
from .task import task_list, task_show

def load_build_commands(self, _):
    with self.command_group('pipelines') as g:
        # basic vsts_cli_build commands
        g.custom_command('build list', 'dev.pipelines.build.build_list', table_transformer=transform_builds_table_output)
        g.custom_command('build queue', 'dev.pipelines.build.build_queue', table_transformer=transform_build_table_output)
        g.custom_command('build show', 'dev.pipelines.build.build_show', table_transformer=transform_build_table_output)

        # basic vsts_cli_build definition commands
        g.custom_command('build definition list', 'dev.pipelines.build_definition.build_definition_list', table_transformer=transform_definitions_table_output)
        g.custom_command('build definition show', 'dev.pipelines.build_definition.build_definition_show', table_transformer=transform_definition_table_output)

        # basic vsts_cli_build task commands
        g.custom_command('build task list', 'dev.pipelines.task.task_list', table_transformer=transform_tasks_table_output)
        g.custom_command('build task show', 'dev.pipelines.task.task_show', table_transformer=transform_task_table_output)
