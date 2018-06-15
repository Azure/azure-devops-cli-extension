# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import platform

from knack.commands import CommandGroup

def load_package_commands(cli_command_loader):
    if platform.system().lower() == "windows": # UPack is currently only supported on Windows
        with CommandGroup(cli_command_loader, 'package upack', 'vsts.cli.package.common.upack#{}') as g:
            g.command('publish', 'publish_package')
            g.command('download', 'download_package')