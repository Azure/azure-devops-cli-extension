# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list
from azure.cli.core.commands.parameters import get_enum_type
from azext_devops.dev.common.const import _TRUE_FALSE_SWITCH
from .const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                    SERVICE_ENDPOINT_TYPE_GITHUB,
                    SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                    SERVICE_ENDPOINT_TYPE_AZURE_RM)


# CUSTOM CHOICE LISTS
_YES_NO_SWITCH_VALUES = ['yes', 'no']
_SOURCE_CONTROL_VALUES = ['git', 'tfvc']
_WIKI_TYPE_VALUES = ['projectwiki', 'codewiki']
_PROJECT_VISIBILITY_VALUES = ['private', 'public']
_STATE_VALUES = ['invalid', 'unchanged', 'all', 'new', 'wellformed', 'deleting', 'createpending']
_SERVICE_ENDPOINT_TYPE = [SERVICE_ENDPOINT_TYPE_GITHUB, SERVICE_ENDPOINT_TYPE_AZURE_RM]
_SERVICE_ENDPOINT_AUTHORIZATION_SCHEME = [SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                                          SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL]

_HTTP_METHOD_VALUES = ['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS', 'PUT', 'HEAD']

_LICENSE_TYPES = ['advanced', 'earlyAdopter', 'express', 'none', 'professional', 'stakeholder']
_RELATIONSHIP_TYPES = ['members', 'memberof']


def load_global_args(context):
    context.argument('organization', options_list=('--organization', '--org'),
                     help='Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/')
    context.argument('detect', arg_type=get_enum_type(['on', 'off']),
                     help='Automatically detect organization. Default is "on".')
    context.argument('project', options_list=('--project', '-p'), help='Name or ID of the project.')


# pylint: disable=too-many-statements
def load_team_arguments(self, _):
    with self.argument_context('devops configure') as context:
        context.argument('defaults', options_list=('--defaults', '-d'), nargs='*')

    with self.argument_context('devops') as context:
        context.argument('repository', options_list=('--repository', '-r'))

    with self.argument_context('devops project') as context:
        context.argument('process', options_list=('--process', '-p'))
        context.argument('source_control', options_list=('--source-control', '-s'),
                         **enum_choice_list(_SOURCE_CONTROL_VALUES))
        context.argument('description', options_list=('--description', '-d'))
        context.argument('state', **enum_choice_list(_STATE_VALUES))
        context.argument('visibility', **enum_choice_list(_PROJECT_VISIBILITY_VALUES))

    with self.argument_context('devops service-endpoint create') as context:
        context.argument('service_endpoint_type', **enum_choice_list(_SERVICE_ENDPOINT_TYPE))
        context.argument('authorization_scheme', **enum_choice_list(_SERVICE_ENDPOINT_AUTHORIZATION_SCHEME))
    with self.argument_context('devops project delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')
    with self.argument_context('devops configure') as context:
        context.argument('use_git_aliases', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('list_config', options_list=('--list', '-l'))

    with self.argument_context('devops invoke') as context:
        context.argument('route_parameters', nargs='*',
                         help='Specifies the list of route parameters')
        context.argument('query_parameters', nargs='*',
                         help='Specifies the list of query parameters')
        context.argument('http_method', arg_type=get_enum_type(_HTTP_METHOD_VALUES),
                         help='Specifies the method used for the request.')
        context.argument('media_type',
                         help='Specifies the content type of the request.')
        context.argument('accept_media_type',
                         help='Specifies the content type of the response.')
        context.argument('in_file',
                         help='Path and file name to the file that contains the contents of the request.')
        context.argument('out_file',
                         help='Path and file name to the file  for which this function saves the response body.')
        context.argument('area',
                         help='The area to find the resource.')
        context.argument('resource',
                         help='The name of the resource to operate on.')
        context.argument('api_version',
                         help='The version of the API to target')

    with self.argument_context('devops user') as context:
        context.argument('license_type', arg_type=get_enum_type(_LICENSE_TYPES))
    with self.argument_context('devops user add') as context:
        context.argument('send_email_invite', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Whether to send email invite for new user or not.')

    with self.argument_context('devops security group membership') as context:
        context.argument('relationship', arg_type=get_enum_type(_RELATIONSHIP_TYPES),
                         help='Get member of/members for this group.')

    with self.argument_context('devops extension') as context:
        context.argument('include_built_in', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Include built in extensions.')
        context.argument('include_disabled', arg_type=get_enum_type(_TRUE_FALSE_SWITCH),
                         help='Include disabled extensions.')
        context.argument('publisher_id', help='Publisher ID')
        context.argument('extension_id', help='Extension ID')
        context.argument('search_query', options_list=('--search-query', '-q'), help='Search term')

    with self.argument_context('devops') as context:
        load_global_args(context)

    with self.argument_context('repos') as context:
        load_global_args(context)

    with self.argument_context('artifacts') as context:
        load_global_args(context)

    with self.argument_context('boards') as context:
        load_global_args(context)

    with self.argument_context('pipelines') as context:
        load_global_args(context)

    with self.argument_context('devops wiki') as context:
        context.argument('wiki_type', options_list=('--wiki-type', '--type'), **enum_choice_list(_WIKI_TYPE_VALUES))
        context.argument('version', options_list=('--version', '-v'))
