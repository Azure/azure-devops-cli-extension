# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list
from .const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                    SERVICE_ENDPOINT_TYPE_GITHUB,
                    SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                    SERVICE_ENDPOINT_TYPE_AZURE_RM)


# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_YES_NO_SWITCH_VALUES = ['yes', 'no']
_SOURCE_CONTROL_VALUES = ['git', 'tfvc']
_PROJECT_VISIBILITY_VALUES = ['private', 'public']
_STATE_VALUES = ['invalid', 'unchanged', 'all', 'new', 'wellformed', 'deleting', 'createpending']
_SERVICE_ENDPOINT_TYPE = [SERVICE_ENDPOINT_TYPE_GITHUB, SERVICE_ENDPOINT_TYPE_AZURE_RM]
_SERVICE_ENDPOINT_AUTHORIZATION_SCHEME = [SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                                          SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL]


def load_team_arguments(self, _):
    with self.argument_context('devops login') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with self.argument_context('devops logout') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with self.argument_context('devops configure') as context:
        context.argument('defaults', options_list=('--defaults', '-d'), nargs='*')
    with self.argument_context('devops project') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('open_browser', options_list='--open')
        context.argument('process', options_list=('--process', '-p'))
        context.argument('source_control', options_list=('--source-control', '-s'),
                         **enum_choice_list(_SOURCE_CONTROL_VALUES))
        context.argument('description', options_list=('--description', '-d'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('state', **enum_choice_list(_STATE_VALUES))
        context.argument('visibility', **enum_choice_list(_PROJECT_VISIBILITY_VALUES))
    with self.argument_context('devops service-endpoint') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with self.argument_context('devops service-endpoint get') as context:
        context.argument('service_endpoint_id', options_list='--id')
    with self.argument_context('devops service-endpoint create') as context:
        context.argument('service_endpoint_type', **enum_choice_list(_SERVICE_ENDPOINT_TYPE))
        context.argument('authorization_scheme', **enum_choice_list(_SERVICE_ENDPOINT_AUTHORIZATION_SCHEME))
    with self.argument_context('devops project delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')
    with self.argument_context('devops configure') as context:
        context.argument('use_git_aliases', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('list_config', options_list=('--list', '-l'))
    with self.argument_context('devops team') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('project', options_list=('--project', '-p'))
