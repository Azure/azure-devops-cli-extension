# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext

def load_package_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'package upack') as ac:
        ac.argument('team_instance', options_list=('--instance'))
        ac.argument('feed', options_list=('--feed'))
        ac.argument('package_name', options_list=('--package-name'))
        ac.argument('package_version', options_list=('--package-version'))
        ac.argument('description', options_list=('--description'))