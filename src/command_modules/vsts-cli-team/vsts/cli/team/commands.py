# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_project_table_output


def load_team_commands(cli_command_loader):
    cli_command_loader.command_table['login'] = \
        cli_command_loader.create_command(module_name='team', name='login',
                                          operation='vsts.cli.team.common.custom#credential_set')

    cli_command_loader.command_table['logout'] = \
        cli_command_loader.create_command(module_name='team', name='logout',
                                          operation='vsts.cli.team.common.custom#credential_clear')

    cli_command_loader.command_table['feedback'] = \
        cli_command_loader.create_command(module_name='team', name='feedback',
                                          operation='vsts.cli.team.common.custom#feedback')

    cli_command_loader.command_table['configure'] = \
        cli_command_loader.create_command(module_name='team', name='configure',
                                          operation='vsts.cli.team.common.custom#configure')

    cli_command_loader.command_table['project create'] = \
        cli_command_loader.create_command(module_name='team', name='project create',
                                          operation='vsts.cli.team.common.project#create_project',
                                          table_transformer=transform_project_table_output)
