# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import argparse
import json
import re
import sys
import os

from knack import CLI
from vsts.cli.vsts_cli_help import VstsCLIHelp
from vsts.cli.vsts_commands_loader import VstsCommandsLoader

# ignore the params passed in now so they aren't used by the cli
sys.argv = sys.argv[:1]

cli_name = "vsts"
vstscli = CLI(cli_name=cli_name,
              config_dir=os.path.join('~', '.{}'.format(cli_name)),
              config_env_var_prefix=cli_name,
              commands_loader_cls=VstsCommandsLoader,
              help_cls=VstsCLIHelp)

loader = vstscli.commands_loader_cls()
loader.__init__(vstscli)
cmd_table = loader.load_command_table([])
for command in loader.command_table:
    loader.load_arguments(command)

vstsclihelp = vstscli.help_cls(cli_ctx=vstscli)

global_parser = vstscli.parser_cls.create_global_parser(cli_ctx=vstscli)
parser = vstscli.parser_cls(cli_ctx=vstscli, prog=vstscli.name, parents=[global_parser])
parser.load_command_table(cmd_table)

cmd_list = cmd_table.keys()

results = {}

for cmd_name in cmd_list:
    cmd_args = cmd_table[cmd_name].arguments
    args = []
    for arg in cmd_args:
        args.append(arg)
    results[cmd_name] = args

print(json.dumps(results, indent=1))

