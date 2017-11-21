# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import (transform_build_table_output,
                      transform_builds_table_output,
                      transform_definition_table_output,
                      transform_definitions_table_output)
from knack.commands import CommandGroup


def load_build_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'build', 'vsts.cli.build.common.custom#{}') as g:
        # basic vsts_cli_build commands
        g.command('list', 'build_list',
                  table_transformer=transform_builds_table_output)
        g.command('queue', 'build_queue',
                  table_transformer=transform_build_table_output)
        g.command('show', 'build_show',
                  table_transformer=transform_build_table_output)

        # basic vsts_cli_build definition commands
        g.command('definition list', 'build_definition_list',
                  table_transformer=transform_definitions_table_output)
        g.command('definition show', 'build_definition_show',
                  table_transformer=transform_definition_table_output)
