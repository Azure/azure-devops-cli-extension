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
from azdos.cli.azdos_cli_help import AzdosCLIHelp
from azdos.cli.azdos_commands_loader import AzdosCommandsLoader

# ignore the params passed in now so they aren't used by the cli
sys.argv = sys.argv[:1]

cli_name = "azdos"
azdoscli = CLI(cli_name=cli_name,
              config_dir=os.path.join('~', '.{}'.format(cli_name)),
              config_env_var_prefix=cli_name,
              commands_loader_cls=AzdosCommandsLoader,
              help_cls=AzdosCLIHelp)

loader = azdoscli.commands_loader_cls()
loader.__init__(azdoscli)
cmd_table = loader.load_command_table([])
for command in loader.command_table:
    loader.load_arguments(command)

azdosclihelp = azdoscli.help_cls(cli_ctx=azdoscli)

global_parser = azdoscli.parser_cls.create_global_parser(cli_ctx=azdoscli)
parser = azdoscli.parser_cls(cli_ctx=azdoscli, prog=azdoscli.name, parents=[global_parser])
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

