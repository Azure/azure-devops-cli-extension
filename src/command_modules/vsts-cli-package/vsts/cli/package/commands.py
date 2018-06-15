# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import platform

from knack.commands import CommandGroup

def load_package_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'package universal', 'vsts.cli.package.common.universal#{}') as g:
        g.command('publish', 'publish_package')
        g.command('download', 'download_package')