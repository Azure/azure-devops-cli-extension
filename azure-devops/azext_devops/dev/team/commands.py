# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.prompting import prompt_y_n
from azure.cli.core.commands import CliCommandType
from ._format import (transform_project_table_output, transform_projects_table_output,
                      transform_service_endpoints_table_output)


projectOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.project#{}'
)

configureOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.configure#{}'
)

feedbackOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.feedback#{}'
)

credentialsOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.credentials#{}'
)

service_endpointOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.service_endpoint#{}'
)

teamOps = CliCommandType(
    operations_tmpl='azext_devops.dev.team.team#{}'
)

def project_delete_confirmation():
    return bool(prompt_y_n('Are you sure you want to delete this project?'))


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
        g.command('delete', 'delete_project', confirmation=project_delete_confirmation)
        g.command('show', 'show_project', table_transformer=transform_project_table_output)
        g.command('list', 'list_projects', table_transformer=transform_projects_table_output)

    with self.command_group('devops service-endpoint', command_type=service_endpointOps) as g:
        g.command('list', 'list_service_endpoints', table_transformer=transform_service_endpoints_table_output)
        g.command('show', 'show_service_endpoint')  # no table transform because type is not well defined
        g.command('create', 'create_service_endpoint')
    
    with self.command_group('devops team', command_type=teamOps) as g:
        g.command('create', 'create_team')
