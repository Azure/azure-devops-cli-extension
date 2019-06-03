# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_work_item_table_output,
                      transform_work_item_query_result_table_output,
                      transform_work_item_relation_type_table_output,
                      transform_work_item_relations,
                      transform_work_item_team_iterations_table_output,
                      transform_work_item_team_iteration_table_output,
                      transform_work_item_project_classification_nodes_table_output,
                      transform_work_item_project_classification_node_table_output,
                      transform_work_item_team_areas_table_output,
                      transform_work_item_team_default_area_table_output)


workItemOps = CliCommandType(
    operations_tmpl='azext_devops.dev.boards.work_item#{}',
    exception_handler=azure_devops_exception_handler
)

relationsOps = CliCommandType(
    operations_tmpl='azext_devops.dev.boards.relations#{}',
    exception_handler=azure_devops_exception_handler
)

workProjectAndTeamIterationOps = CliCommandType(
    operations_tmpl='azext_devops.dev.boards.iteration#{}',
    exception_handler=azure_devops_exception_handler
)

workProjectAndTeamAreaOps = CliCommandType(
    operations_tmpl='azext_devops.dev.boards.area#{}',
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

    with self.command_group('boards work-item', command_type=relationsOps) as g:
        # relation commands
        g.command('relation list-type', 'get_relation_types_show',
                  table_transformer=transform_work_item_relation_type_table_output)
        g.command('relation add', 'add_relation', table_transformer=transform_work_item_relations)
        g.command('relation remove', 'remove_relation', table_transformer=transform_work_item_relations,
                  confirmation='Are you sure you want to remove this relation(s)?')
        g.command('relation show', 'show_work_item', table_transformer=transform_work_item_relations)

    with self.command_group('boards iteration team', command_type=workProjectAndTeamIterationOps) as g:
        # team iteration commands
        g.command('list', 'get_team_iterations', table_transformer=transform_work_item_team_iterations_table_output)
        g.command('show', 'get_team_iteration', table_transformer=transform_work_item_team_iteration_table_output)
        g.command('remove', 'delete_team_iteration', table_transformer=transform_work_item_team_iteration_table_output)
        g.command('add', 'post_team_iteration', table_transformer=transform_work_item_team_iteration_table_output)

    with self.command_group('boards iteration project', command_type=workProjectAndTeamIterationOps) as g:
        # team iteration commands
        g.command('list', 'get_project_iterations',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('update', 'update_project_iteration',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('delete', 'delete_project_iteration',
                  confirmation='Are you sure you want to delete this iteration?')
        g.command('show', 'get_project_iteration',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('create', 'create_project_iteration',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)

    with self.command_group('boards area project', command_type=workProjectAndTeamAreaOps) as g:
        # team iteration commands
        g.command('list', 'get_project_areas',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('delete', 'delete_project_area',
                  confirmation='Are you sure you want to delete this area?')
        g.command('create', 'create_project_area',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('update', 'update_project_area',
                  table_transformer=transform_work_item_project_classification_nodes_table_output)
        g.command('show', 'get_project_area',
                  table_transformer=transform_work_item_project_classification_node_table_output)

    with self.command_group('boards area team', command_type=workProjectAndTeamAreaOps) as g:
        # team iteration commands
        g.command('list', 'get_team_areas', table_transformer=transform_work_item_team_areas_table_output)
        g.command('add', 'add_team_area', table_transformer=transform_work_item_team_areas_table_output)
        g.command('remove', 'remove_team_area', table_transformer=transform_work_item_team_areas_table_output)
        g.command('configure-default', 'configure_team_area',
                  table_transformer=transform_work_item_team_default_area_table_output)
