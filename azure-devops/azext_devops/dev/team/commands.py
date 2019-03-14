# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_project_table_output,
                      transform_projects_table_output,
                      transform_service_endpoints_table_output,
                      transform_team_table_output,
                      transform_teams_table_output,
                      transform_team_members_table_output,
                      transform_users_table_output,
                      transform_user_table_output,
                      transform_extension_table_output,
                      transform_extensions_table_output)


projectOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.project#{}',
    exception_handler=azure_devops_exception_handler
)

configureOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.configure#{}',
    exception_handler=azure_devops_exception_handler
)

feedbackOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.feedback#{}',
    exception_handler=azure_devops_exception_handler
)

credentialsOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.credentials#{}',
    exception_handler=azure_devops_exception_handler
)

service_endpointOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.service_endpoint#{}',
    exception_handler=azure_devops_exception_handler
)

teamOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.team#{}',
    exception_handler=azure_devops_exception_handler
)

userOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.user#{}',
    exception_handler=azure_devops_exception_handler
)

extensionOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.extension#{}',
    exception_handler=azure_devops_exception_handler
)


def load_team_commands(self, _):
    with self.command_group('devops', command_type=credentialsOps) as g:
        g.command('login', 'credential_set')
        g.command('logout', 'credential_clear')

    with self.command_group('devops', command_type=feedbackOps) as g:
        g.command('feedback', 'feedback')

    with self.command_group('devops', command_type=configureOps) as g:
        g.command('configure', 'configure')

    with self.command_group('devops project', command_type=projectOps) as g:
        g.command('create', 'create_project', table_transformer=transform_project_table_output)
        g.command('delete', 'delete_project', confirmation='Are you sure you want to delete this project?')
        g.command('show', 'show_project', table_transformer=transform_project_table_output)
        g.command('list', 'list_projects', table_transformer=transform_projects_table_output)

    with self.command_group('devops service-endpoint', command_type=service_endpointOps) as g:
        g.command('list', 'list_service_endpoints', table_transformer=transform_service_endpoints_table_output)
        g.command('show', 'show_service_endpoint')  # no table transform because type is not well defined
        g.command('create', 'create_service_endpoint')

    with self.command_group('devops team', command_type=teamOps) as g:
        g.command('create', 'create_team', table_transformer=transform_team_table_output)
        g.command('delete', 'delete_team', confirmation='Are you sure you want to delete this team?')
        g.command('show', 'get_team', table_transformer=transform_team_table_output)
        g.command('list', 'get_teams', table_transformer=transform_teams_table_output)
        g.command('list-member', 'get_team_members', table_transformer=transform_team_members_table_output)
        g.command('update', 'update_team', table_transformer=transform_team_table_output)

    with self.command_group('devops user', command_type=userOps) as g:
        g.command('list', 'get_user_entitlements', table_transformer=transform_users_table_output)
        g.command('show', 'get_user_entitlement', table_transformer=transform_user_table_output)
        g.command('remove', 'delete_user_entitlement', confirmation='Are you sure you want to remove this user?')
        g.command('update', 'update_user_entitlement', table_transformer=transform_user_table_output)
        g.command('add', 'add_user_entitlement', table_transformer=transform_user_table_output)

    with self.command_group('devops extension', command_type=extensionOps) as g:
        g.command('list', 'list_extensions', table_transformer=transform_extensions_table_output)
        g.command('uninstall', 'uninstall_extension', confirmation='Are you sure you want to uninstall this extension?')
        g.command('install', 'install_extension', table_transformer=transform_extension_table_output)
        g.command('show', 'get_extension', table_transformer=transform_extension_table_output)
        g.command('enable', 'enable_extension', table_transformer=transform_extension_table_output)
        g.command('disable', 'disable_extension', table_transformer=transform_extension_table_output)
