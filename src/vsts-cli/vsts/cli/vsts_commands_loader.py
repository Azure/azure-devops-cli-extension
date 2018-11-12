# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CLICommandsLoader
from vsts.cli.admin.commands import load_admin_commands
from vsts.cli.admin.arguments import load_admin_arguments
from vsts.cli.build.commands import load_build_commands
from vsts.cli.build.arguments import load_build_arguments
from vsts.cli.vrelease.commands import load_release_commands
from vsts.cli.vrelease.arguments import load_release_arguments
from vsts.cli.code.commands import load_code_commands
from vsts.cli.code.arguments import load_code_arguments
from vsts.cli.team.commands import load_team_commands
from vsts.cli.team.arguments import load_team_arguments
from vsts.cli.work.commands import load_work_commands
from vsts.cli.work.arguments import load_work_arguments
from vsts.cli.package.commands import load_package_commands
from vsts.cli.package.arguments import load_package_arguments


class VstsCommandsLoader(CLICommandsLoader):
    def load_command_table(self, args):
        load_admin_commands(self)
        load_build_commands(self)
        load_release_commands(self)
        load_code_commands(self)
        load_team_commands(self)
        load_work_commands(self)
        load_package_commands(self)
        return super(VstsCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command):
        load_admin_arguments(self)
        load_build_arguments(self)
        load_release_arguments(self)
        load_code_arguments(self)
        load_team_arguments(self)
        load_work_arguments(self)
        load_package_arguments(self)
        super(VstsCommandsLoader, self).load_arguments(command)
