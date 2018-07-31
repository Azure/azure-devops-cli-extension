# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext

def load_package_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'package universal') as ac:
        ac.argument('team_instance', options_list=('--instance', '-i'))