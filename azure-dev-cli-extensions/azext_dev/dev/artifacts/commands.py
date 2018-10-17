# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def load_package_commands(cli_command_loader):
    with self.command_group('artifacts universal') as g:
        g.custom_command('publish', 'artifacts.universal.publish_package')
        g.custom_command('download', 'artifacts.universal.download_package')