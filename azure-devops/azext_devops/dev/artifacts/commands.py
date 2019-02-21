# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType

from azext_devops.dev.common.exception_handler import azure_devops_exception_handler

artifactOps = CliCommandType(
    operations_tmpl='azext_devops.dev.artifacts.universal#{}',
    exception_handler=azure_devops_exception_handler
)


def load_package_commands(self, _):
    with self.command_group('artifacts universal', command_type=artifactOps) as g:
        g.command('publish', 'publish_package')
        g.command('download', 'download_package')
