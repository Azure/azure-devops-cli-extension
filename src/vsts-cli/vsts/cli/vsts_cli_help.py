# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help import CLIHelp
from azdos.cli.common.version import VERSION


class AzdosCLIHelp(CLIHelp):
    def __init__(self, cli_ctx=None):
        # import command group help
        import azdos.cli.admin._help
        import azdos.cli.build._help
        import azdos.cli.code._help
        import azdos.cli.team._help
        import azdos.cli.work._help
        import azdos.cli.package._help
        super(AzdosCLIHelp, self).__init__(cli_ctx=cli_ctx,
                                          privacy_statement=PRIVACY_STATEMENT,
                                          welcome_message=WELCOME_MESSAGE)


PRIVACY_STATEMENT = """Azure DevOps Services CLI {}

Telemetry
---------
The ADS CLI collects usage data in order to improve your experience.
The data is anonymous and does not include commandline argument values.
The data is collected by Microsoft.

You can change your telemetry settings with `azdos configure`.
""".format(VERSION)

WELCOME_MESSAGE = """Azure DevOps Services CLI {}

Use `azdos -h` to see available commands or go to https://aka.ms/azdos-cli.

Available commands:""".format(VERSION)
