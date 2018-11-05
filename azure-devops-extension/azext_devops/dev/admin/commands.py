# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import transform_banner_table_output

from .banner import banner_list, banner_show, banner_add, banner_remove, banner_update

def load_admin_commands(self, _):
    with self.command_group('devops admin banner') as g:
        g.custom_command('list', 'dev.admin.banner.banner_list', table_transformer=transform_banner_table_output)
        g.custom_command('show', 'dev.admin.banner.banner_show', table_transformer=transform_banner_table_output)
        g.custom_command('add', 'dev.admin.banner.banner_add', table_transformer=transform_banner_table_output)
        g.custom_command('remove', 'dev.admin.banner.banner_remove')
        g.custom_command('update', 'dev.admin.banner.banner_update', table_transformer=transform_banner_table_output)

