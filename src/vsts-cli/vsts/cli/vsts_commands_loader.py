# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CLICommandsLoader
from azdos.cli.admin.commands import load_admin_commands
from azdos.cli.admin.arguments import load_admin_arguments
from azdos.cli.build.commands import load_build_commands
from azdos.cli.build.arguments import load_build_arguments
from azdos.cli.code.commands import load_code_commands
from azdos.cli.code.arguments import load_code_arguments
from azdos.cli.team.commands import load_team_commands
from azdos.cli.team.arguments import load_team_arguments
from azdos.cli.work.commands import load_work_commands
from azdos.cli.work.arguments import load_work_arguments
from azdos.cli.package.commands import load_package_commands
from azdos.cli.package.arguments import load_package_arguments


class AzdosCommandsLoader(CLICommandsLoader):
    def load_command_table(self, args):
        load_admin_commands(self)
        load_build_commands(self)
        load_code_commands(self)
        load_team_commands(self)
        load_work_commands(self)
        load_package_commands(self)
        return super(AzdosCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command):
        load_admin_arguments(self)
        load_build_arguments(self)
        load_code_arguments(self)
        load_team_arguments(self)
        load_work_arguments(self)
        load_package_arguments(self)
        super(AzdosCommandsLoader, self).load_arguments(command)
