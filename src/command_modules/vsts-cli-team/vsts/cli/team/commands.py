# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandSuperGroup


def load_team_commands(cli_command_loader):
    with CommandSuperGroup(__name__, cli_command_loader, 'vsts.cli.team.common.custom#{}') as sg:
        with sg.group('team') as g:
            # credential commands
            g.command('credential set', 'credential_set')
            g.command('credential clear', 'credential_clear')

            # git alias commands
            g.command('setup-git-aliases', 'setup_git_aliases')
