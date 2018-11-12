# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help import CLIHelp
from vsts.cli.common.version import VERSION


class VstsCLIHelp(CLIHelp):
    def __init__(self, cli_ctx=None):
        # import command group help
        import vsts.cli.admin._help
        import vsts.cli.build._help
        import vsts.cli.code._help
        import vsts.cli.team._help
        import vsts.cli.work._help
        import vsts.cli.package._help
        import vsts.cli.vrelease._help
        super(VstsCLIHelp, self).__init__(cli_ctx=cli_ctx,
                                          privacy_statement=PRIVACY_STATEMENT,
                                          welcome_message=WELCOME_MESSAGE)


PRIVACY_STATEMENT = """Visual Studio Team Services CLI {}

Telemetry
---------
The VSTS CLI collects usage data in order to improve your experience.
The data is anonymous and does not include commandline argument values.
The data is collected by Microsoft.

You can change your telemetry settings with `vsts configure`.
""".format(VERSION)

WELCOME_MESSAGE = """Visual Studio Team Services CLI {}

Use `vsts -h` to see available commands or go to https://aka.ms/vsts-cli.

Available commands:""".format(VERSION)
