# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys

from .vsts_cli_help import VstsCLIHelp
from .vsts_commands_loader import VstsCommandsLoader
from knack import CLI
from vsts.cli.common.vsts import set_tracking_data


try:
    cli_name = "vsts"
    vstscli = CLI(cli_name=cli_name,
                  config_dir=os.path.join('~', '.{}'.format(cli_name)),
                  config_env_var_prefix=cli_name,
                  commands_loader_cls=VstsCommandsLoader,
                  help_cls=VstsCLIHelp)
    set_tracking_data(sys.argv[1:])
    exit_code = vstscli.invoke(sys.argv[1:])
    sys.exit(exit_code)
except KeyboardInterrupt:
    sys.exit(1)
