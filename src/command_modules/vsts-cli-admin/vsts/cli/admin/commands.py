# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import transform_banner_table_output


def load_admin_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'admin', 'azdos.cli.admin.common.banner#{}') as g:
        g.command('banner list', 'banner_list', table_transformer=transform_banner_table_output)
        g.command('banner show', 'banner_show', table_transformer=transform_banner_table_output)
        g.command('banner add', 'banner_add', table_transformer=transform_banner_table_output)
        g.command('banner remove', 'banner_remove')
        g.command('banner update', 'banner_update', table_transformer=transform_banner_table_output)

