# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help import CLIHelp


class VstsCLIHelp(CLIHelp):
    def __init__(self, cli_ctx=None):
        # import command group help
        import vsts.cli.build._help
        import vsts.cli.code._help
        import vsts.cli.team._help
        import vsts.cli.work._help
        super(VstsCLIHelp, self).__init__(cli_ctx=cli_ctx)
