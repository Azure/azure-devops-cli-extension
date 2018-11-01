# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_project_table_output, transform_projects_table_output


def load_team_commands(cli_command_loader):
    cli_command_loader.command_table['login'] = \
        cli_command_loader.create_command(module_name='team', name='login',
                                          operation='azdos.cli.team.common.credentials#credential_set')

    cli_command_loader.command_table['logout'] = \
        cli_command_loader.create_command(module_name='team', name='logout',
                                          operation='azdos.cli.team.common.credentials#credential_clear')

    cli_command_loader.command_table['feedback'] = \
        cli_command_loader.create_command(module_name='team', name='feedback',
                                          operation='azdos.cli.team.common.feedback#feedback')

    cli_command_loader.command_table['configure'] = \
        cli_command_loader.create_command(module_name='team', name='configure',
                                          operation='azdos.cli.team.common.configure#configure')

    cli_command_loader.command_table['project create'] = \
        cli_command_loader.create_command(module_name='team', name='project create',
                                          operation='azdos.cli.team.common.project#create_project',
                                          table_transformer=transform_project_table_output)
    cli_command_loader.command_table['project show'] = \
        cli_command_loader.create_command(module_name='team', name='project show',
                                          operation='azdos.cli.team.common.project#show_project',
                                          table_transformer=transform_project_table_output)
    cli_command_loader.command_table['project list'] = \
        cli_command_loader.create_command(module_name='team', name='project list',
                                          operation='azdos.cli.team.common.project#list_projects',
                                          table_transformer=transform_projects_table_output)
