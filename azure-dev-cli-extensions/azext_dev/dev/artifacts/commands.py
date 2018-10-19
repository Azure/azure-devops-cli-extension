# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .universal import (publish_package, 
                        download_package)

def load_package_commands(self, _):
    with self.command_group('artifacts universal') as g:
        g.custom_command('publish', 'dev.artifacts.universal.publish_package')
        g.custom_command('download', 'dev.artifacts.universal.download_package')