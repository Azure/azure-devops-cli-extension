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
                      transform_extensions_table_output,
                      transform_extension_search_results_table_output,
                      transform_wiki_table_output,
                      transform_wikis_table_output,
                      transform_wiki_page_table_output)


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

invokeOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.invoke#{}',
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

security_groupOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.security_group#{}',
    exception_handler=azure_devops_exception_handler
)


wikiOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.wiki#{}',
    exception_handler=azure_devops_exception_handler
)


# pylint: disable=too-many-statements
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

    with self.command_group('devops', command_type=invokeOps) as g:
        g.command('invoke', 'invoke')

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
        g.command('search', 'search_extensions', table_transformer=transform_extension_search_results_table_output)

    # with self.command_group('devops security group', command_type=security_groupOps) as g:
    #     g.command('list', 'list_groups', table_transformer=transform_groups_table_output)
    #     g.command('show', 'get_group', table_transformer=transform_group_table_output)
    #     g.command('update', 'update_group', table_transformer=transform_group_table_output)
    #     g.command('create', 'create_group', table_transformer=transform_group_table_output)
    #     g.command('delete', 'delete_group', confirmation='Are you sure you want to delete this group?')

    # with self.command_group('devops security group membership', command_type=security_groupOps) as g:
    #     g.command('list', 'list_memberships', table_transformer=transform_memberships_table_output)
    #     g.command('add', 'add_membership', table_transformer=transform_membership_table_output)
    #     g.command('remove', 'remove_membership', confirmation='Are you sure you want to delete this relationship?')

    with self.command_group('devops wiki', command_type=wikiOps) as g:
        g.command('create', 'create_wiki', table_transformer=transform_wiki_table_output)
        g.command('list', 'list_wiki', table_transformer=transform_wikis_table_output)
        g.command('show', 'show_wiki', table_transformer=transform_wiki_table_output)
        g.command('delete', 'delete_wiki', table_transformer=transform_wiki_table_output,
                  confirmation='Are you sure you want to delete this wiki?')

    with self.command_group('devops wiki page', command_type=wikiOps) as g:
        g.command('create', 'add_page', table_transformer=transform_wiki_page_table_output)
        g.command('update', 'update_page', table_transformer=transform_wiki_page_table_output)
        g.command('show', 'get_page', table_transformer=transform_wiki_page_table_output)
        g.command('delete', 'delete_page',
                  confirmation='Are you sure you want to delete this wiki page?')
