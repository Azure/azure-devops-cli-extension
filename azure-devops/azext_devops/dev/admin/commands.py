# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import transform_banner_table_output


bannerops = CliCommandType(
    operations_tmpl='azext_devops.dev.admin.banner#{}',
    exception_handler=azure_devops_exception_handler
)


def load_admin_commands(self, _):
    with self.command_group('devops admin banner', command_type=bannerops) as g:
        g.command('list', 'banner_list', table_transformer=transform_banner_table_output)
        g.show_command('show', 'banner_show', table_transformer=transform_banner_table_output)
        g.command('add', 'banner_add', table_transformer=transform_banner_table_output)
        g.command('remove', 'banner_remove')
        g.command('update', 'banner_update', table_transformer=transform_banner_table_output)
