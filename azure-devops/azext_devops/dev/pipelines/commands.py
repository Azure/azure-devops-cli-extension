# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_build_table_output,
                      transform_builds_table_output,
                      transform_pipeline_run_table_output,
                      transform_pipeline_runs_table_output,
                      transform_pipeline_table_output,
                      transform_pipelines_table_output,
                      transform_build_tags_output,
                      transform_definition_table_output,
                      transform_definitions_table_output,
                      transform_releases_table_output,
                      transform_release_table_output,
                      transform_release_definitions_table_output,
                      transform_release_definition_table_output,
                      transform_runs_artifact_table_output,
                      transform_pipelines_pools_table_output,
                      transform_pipelines_pool_table_output,
                      transform_pipelines_agents_table_output,
                      transform_pipelines_agent_table_output,
                      transform_pipelines_queues_table_output,
                      transform_pipelines_queue_table_output,
                      transform_pipelines_variable_groups_table_output,
                      transform_pipelines_variable_group_table_output)

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

pipelinesOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.pipeline#{}',
    exception_handler=azure_devops_exception_handler
)

pipelineCreateOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.pipeline_create#{}',
    exception_handler=azure_devops_exception_handler
)

pipelinesRunOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.pipeline_run#{}',
    exception_handler=azure_devops_exception_handler
)

pipelineRunArtifactsOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.runs_artifacts#{}',
    exception_handler=azure_devops_exception_handler
)

pipelineAgentPoolQueueOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.agent_pool_queue#{}',
    exception_handler=azure_devops_exception_handler
)

pipelineVariableGroupOps = CliCommandType(
    operations_tmpl='azext_devops.dev.pipelines.variable_group#{}',
    exception_handler=azure_devops_exception_handler
)

def load_build_commands(self, _):
    with self.command_group('pipelines', command_type=pipelineCreateOps) as g:
        g.command('create', 'pipeline_create', table_transformer=transform_pipeline_run_table_output)
        g.command('update', 'pipeline_update', table_transformer=transform_pipeline_table_output)

    with self.command_group('pipelines', command_type=pipelinesOps) as g:
        g.command('list', 'pipeline_list', table_transformer=transform_pipelines_table_output)
        g.command('show', 'pipeline_show', table_transformer=transform_pipeline_table_output)
        g.command('delete', 'pipeline_delete', confirmation='Are you sure you want to delete this pipeline?')
        g.command('run', 'pipeline_run', table_transformer=transform_pipeline_run_table_output)

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

    with self.command_group('pipelines release', command_type=releaseOps) as g:
        # basic release commands
        g.command('list', 'release_list', table_transformer=transform_releases_table_output)
        g.command('create', 'release_create', table_transformer=transform_release_table_output)
        g.command('show', 'release_show', table_transformer=transform_release_table_output)

    with self.command_group('pipelines release definition', command_type=releaseDefinitionOps) as g:
        # basic release commands
        g.command('list', 'release_definition_list', table_transformer=transform_release_definitions_table_output)
        g.command('show', 'release_definition_show', table_transformer=transform_release_definition_table_output)

    with self.command_group('pipelines runs artifact', command_type=pipelineRunArtifactsOps) as g:
        g.command('download', 'run_artifact_download')
        g.command('list', 'run_artifact_list', table_transformer=transform_runs_artifact_table_output)
        g.command('upload', 'run_artifact_upload')

    with self.command_group('pipelines runs tag', command_type=pipelinesRunOps) as g:
        g.command('add', 'pipeline_run_add_tag', table_transformer=transform_build_tags_output)
        g.command('list', 'pipeline_run_get_tags', table_transformer=transform_build_tags_output)
        g.command('delete', 'pipeline_run_delete_tag', table_transformer=transform_build_tags_output)

    with self.command_group('pipelines runs', command_type=pipelinesRunOps) as g:
        g.command('list', 'pipeline_run_list', table_transformer=transform_pipeline_runs_table_output)
        g.command('show', 'pipeline_run_show', table_transformer=transform_pipeline_run_table_output)

    with self.command_group('pipelines pool', command_type=pipelineAgentPoolQueueOps) as g:
        g.command('list', 'list_pools', table_transformer=transform_pipelines_pools_table_output)
        g.command('show', 'show_pool', table_transformer=transform_pipelines_pool_table_output)

    with self.command_group('pipelines agent', command_type=pipelineAgentPoolQueueOps) as g:
        g.command('list', 'list_agents', table_transformer=transform_pipelines_agents_table_output)
        g.command('show', 'show_agent', table_transformer=transform_pipelines_agent_table_output)

    with self.command_group('pipelines queue', command_type=pipelineAgentPoolQueueOps) as g:
        g.command('list', 'list_queues', table_transformer=transform_pipelines_queues_table_output)
        g.command('show', 'show_queue', table_transformer=transform_pipelines_queue_table_output)

    with self.command_group('pipelines variable-group', command_type=pipelineVariableGroupOps) as g:
        g.command('create', 'variable_group_create', table_transformer=transform_pipelines_variable_group_table_output)
        g.command('show', 'variable_group_show', table_transformer=transform_pipelines_variable_group_table_output)
        g.command('list', 'variable_group_list', table_transformer=transform_pipelines_variable_groups_table_output)
        g.command('update', 'variable_group_update', table_transformer=transform_pipelines_variable_group_table_output)
        g.command('delete', 'variable_group_delete',
                  confirmation='Are you sure you want to delete this variable group?')

    with self.command_group('pipelines variable-group variable', command_type=pipelineVariableGroupOps) as g:
        g.command('add', 'variable_group_variable_add')
        g.command('list', 'variable_group_variable_list')
        g.command('delete', 'variable_group_variable_delete',
                  confirmation='Are you sure you want to delete this variable?')
