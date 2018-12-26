# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType

artifactOps = CliCommandType(
    operations_tmpl='azext_devops.dev.artifacts.universal#{}'
)

def load_package_commands(self, _):
    with self.command_group('artifacts universal', command_type=artifactOps) as g:
        g.command('publish', 'publish_package')
        g.command('download', 'download_package')
        