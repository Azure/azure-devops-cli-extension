# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
 
from knack.help_files import helps

from azure.cli.core import AzCommandsLoader

helps['hello world'] = """
    type: command
    short-summary: Say hello world.
"""


class DevCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_dev#{}')
        super(DevCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        from azext_dev.dev.admin.commands import load_admin_commands
        load_admin_commands(self, args)
        from azext_dev.dev.boards.commands import load_work_commands
        load_work_commands(self, args)
        from azext_dev.dev.pipelines.commands import load_build_commands
        load_build_commands(self, args)
        from azext_dev.dev.repos.commands import load_code_commands
        load_code_commands(self, args)
        from azext_dev.dev.team.commands import load_team_commands
        load_team_commands(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_dev.dev.admin.arguments import load_admin_arguments
        load_admin_arguments(self, command)
        from azext_dev.dev.boards.arguments import load_work_arguments
        load_work_arguments(self, command)
        from azext_dev.dev.pipelines.arguments import load_build_arguments
        load_build_arguments(self, command)
        from azext_dev.dev.repos.arguments import load_code_arguments
        load_code_arguments(self, command)
        from azext_dev.dev.team.arguments import load_team_arguments
        load_team_arguments(self, command)

COMMAND_LOADER_CLS = DevCommandsLoader