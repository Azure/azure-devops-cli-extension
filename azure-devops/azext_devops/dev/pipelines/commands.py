# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_build_table_output,
                      transform_builds_table_output,
                      transform_build_tags_output,
                      transform_definition_table_output,
                      transform_definitions_table_output,
                      transform_tasks_table_output,
                      transform_task_table_output,
                      transform_releases_table_output,
                      transform_release_table_output,
                      transform_release_definitions_table_output,
                      transform_release_definition_table_output,
                      transform_runs_artifact_table_output)

buildOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.build#{}',
    exception_handler=azure_devops_exception_handler
)

buildDefOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.build_definition#{}',
    exception_handler=azure_devops_exception_handler
)

buildTaskOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.task#{}',
    exception_handler=azure_devops_exception_handler
)

releaseOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.release#{}',
    exception_handler=azure_devops_exception_handler
)

releaseDefinitionOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.release_definition#{}',
    exception_handler=azure_devops_exception_handler
)

runOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.runs#{}'
)


def load_build_commands(self, _):
    with self.command_group('pipelines build', command_type=buildOps) as g:
        # basic build commands
        g.command('list', 'build_list', table_transformer=transform_builds_table_output)
        g.command('queue', 'build_queue', table_transformer=transform_build_table_output)
        g.command('show', 'build_show', table_transformer=transform_build_table_output)

    with self.command_group('pipelines build tag', command_type=buildOps) as g:
        # basic build tag commands
        g.command('list', 'get_build_tags', table_transformer=transform_build_tags_output)
        g.command('add', 'add_build_tags', table_transformer=transform_build_tags_output)
        g.command('delete', 'delete_build_tag', table_transformer=transform_build_tags_output)

    with self.command_group('pipelines build definition', command_type=buildDefOps) as g:
        # basic build definition commands
        g.command('list', 'build_definition_list', table_transformer=transform_definitions_table_output)
        g.command('show', 'build_definition_show', table_transformer=transform_definition_table_output)

    with self.command_group('pipelines build task', command_type=buildTaskOps) as g:
        # basic build task commands
        g.command('list', 'task_list', table_transformer=transform_tasks_table_output)
        g.command('show', 'task_show', table_transformer=transform_task_table_output)

    with self.command_group('pipelines release', command_type=releaseOps) as g:
        # basic release commands
        g.command('list', 'release_list', table_transformer=transform_releases_table_output)
        g.command('create', 'release_create', table_transformer=transform_release_table_output)
        g.command('show', 'release_show', table_transformer=transform_release_table_output)

    with self.command_group('pipelines release definition', command_type=releaseDefinitionOps) as g:
        # basic release commands
        g.command('list', 'release_definition_list', table_transformer=transform_release_definitions_table_output)
        g.command('show', 'release_definition_show', table_transformer=transform_release_definition_table_output)

    with self.command_group('pipelines runs artifact', command_type=runOps) as g:
        g.command('download', 'run_artifact_download')
        g.command('list', 'run_artifact_list', table_transformer=transform_runs_artifact_table_output)
        g.command('upload', 'run_artifact_upload')