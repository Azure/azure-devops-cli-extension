# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from argparse import ArgumentTypeError

def load_package_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'package upack') as ac:
        ac.argument('team_instance', options_list=('--instance'))
        ac.argument('feed', type=nonempty_str)
        ac.argument('name', type=nonempty_str)
        ac.argument('version', type=nonempty_str)
        ac.argument('path', type=nonempty_str)
        ac.argument('description')

def nonempty_str(s):
    if not s.strip():
        raise ArgumentTypeError("value must not be empty")
    return s
