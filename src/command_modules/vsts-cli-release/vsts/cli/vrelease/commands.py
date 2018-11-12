# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import (transform_release_table_output,
                      transform_releases_table_output,
                      transform_release_definition_table_output,
                      transform_release_definitions_table_output)
from knack.commands import CommandGroup


def load_release_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'release', 'vsts.cli.vrelease.common.{}') as g:
        # basic vsts_cli_release commands
        g.command('list', 'release#release_list',
                  table_transformer=transform_releases_table_output)
        g.command('create', 'release#release_create',
                  table_transformer=transform_release_table_output)
        g.command('show', 'release#release_show',
                  table_transformer=transform_release_table_output)

        # basic vsts_cli_release definition commands
        g.command('definition list', 'release_definition#release_definition_list',
                  table_transformer=transform_release_definitions_table_output)
        g.command('definition show', 'release_definition#release_definition_show',
                  table_transformer=transform_release_definition_table_output)
