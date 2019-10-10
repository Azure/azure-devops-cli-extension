# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list
from azure.cli.core.commands.parameters import get_enum_type, get_three_state_flag
from azext_devops.dev.common.utils import FILE_ENCODING_TYPES


# CUSTOM CHOICE LISTS
_SOURCE_CONTROL_VALUES = ['git', 'tfvc']
_WIKI_TYPE_VALUES = ['projectwiki', 'codewiki']
_SCOPE_VALUES = ['project', 'organization']
_PROJECT_VISIBILITY_VALUES = ['private', 'public']
_STATE_VALUES = ['invalid', 'unchanged', 'all', 'new', 'wellformed', 'deleting', 'createpending']
_PROJECT_GET_STATE_VALUE_FILTER = ['all', 'createPending', 'deleted', 'deleting', 'new', 'unchanged', 'wellFormed']

_HTTP_METHOD_VALUES = ['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS', 'PUT', 'HEAD']

_LICENSE_TYPES = ['advanced', 'earlyAdopter', 'express', 'professional', 'stakeholder']
_RELATIONSHIP_TYPES = ['members', 'memberof']
_FILE_ENCODING_TYPE_VALUES = FILE_ENCODING_TYPES


def load_global_args(context):
    context.argument('organization', options_list=('--organization', '--org'),
                     help='Azure DevOps organization URL. You can configure the default organization using '
                     'az devops configure -d organization=ORG_URL. Required if not configured as '
                     'default or picked up via git config. Example: https://dev.azure.com/MyOrganizationName/')
    context.argument('detect', arg_type=get_three_state_flag(),
                     help='Automatically detect organization.')
    context.argument('project', options_list=('--project', '-p'),
                     help='Name or ID of the project. You can configure the default project using '
                     'az devops configure -d project=NAME_OR_ID. Required if not configured as '
                     'default or picked up via git config.')


# pylint: disable=too-many-statements
def load_team_arguments(self, _):
    with self.argument_context('devops login') as context:
        context.argument('organization',
                         help='Azure DevOps organization URL. Example: https://dev.azure.com/MyOrganizationName')

    with self.argument_context('devops logout') as context:
        context.argument('organization',
                         help='Azure DevOps organization URL. Example: https://dev.azure.com/MyOrganizationName/. '
                         'If no organization is specified, all organizations will be logged out.')

    with self.argument_context('devops configure') as context:
        context.argument('defaults', options_list=('--defaults', '-d'), nargs='*')
        context.argument('use_git_aliases', arg_type=get_three_state_flag())
        context.argument('list_config', options_list=('--list', '-l'))

    with self.argument_context('devops') as context:
        context.argument('repository', options_list=('--repository', '-r'))

    with self.argument_context('devops project') as context:
        context.argument('process', options_list=('--process', '-p'))
        context.argument('source_control', options_list=('--source-control', '-s'),
                         **enum_choice_list(_SOURCE_CONTROL_VALUES))
        context.argument('description', options_list=('--description', '-d'))
        context.argument('state', **enum_choice_list(_STATE_VALUES))
        context.argument('visibility', **enum_choice_list(_PROJECT_VISIBILITY_VALUES))

    with self.argument_context('devops project delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')

    with self.argument_context('devops project list') as context:
        context.argument('state_filter', arg_type=get_enum_type(_PROJECT_GET_STATE_VALUE_FILTER),
                         help='State filter.')
        context.argument('continuation_token',
                         help='Continuation token.')
        context.argument('get_default_team_image_url', arg_type=get_three_state_flag(),
                         help='Whether to get default team image url or not.')

    with self.argument_context('devops service-endpoint create') as context:
        context.argument('encoding',
                         help='Encoding of the input file.',
                         **enum_choice_list(_FILE_ENCODING_TYPE_VALUES))

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
        context.argument('encoding',
                         help='Encoding of the input file. Used in conjunction with --in-file.',
                         **enum_choice_list(_FILE_ENCODING_TYPE_VALUES))
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
        context.argument('send_email_invite', arg_type=get_three_state_flag(),
                         help='Whether to send email invite for new user or not.')

    with self.argument_context('devops security group create') as context:
        context.argument('project',
                         help='Name or ID of the project in which Azure DevOps group should be created.')
        context.argument('scope', **enum_choice_list(_SCOPE_VALUES))

    with self.argument_context('devops security group list') as context:
        context.argument('project',
                         help='List groups for a particular project')
        context.argument('scope', **enum_choice_list(_SCOPE_VALUES))

    with self.argument_context('devops security group membership') as context:
        context.argument('relationship', arg_type=get_enum_type(_RELATIONSHIP_TYPES),
                         help='Get member of/members for this group.')

    with self.argument_context('devops security permission') as context:
        context.argument('namespace_id', options_list=('--namespace-id', '--id'),
                         help='ID of security namespace')
        context.argument('token',
                         help='Security token.')
        context.argument('subject',
                         help='User Email ID or Group descriptor')

    with self.argument_context('devops security permission update') as context:
        context.argument('merge', arg_type=get_three_state_flag(),
                         help='If set, the existing ACE has its allow and deny merged with \
                         the incoming ACE\'s allow and deny. If unset, the existing ACE is displaced.')
        context.argument('allow_bit', type=int,
                         help='Allow bit or addition of bits. Required if --deny-bit is missing.')
        context.argument('deny_bit', type=int,
                         help='Deny bit or addition of bits. Required if --allow-bit is missing.')

    with self.argument_context('devops security permission reset') as context:
        context.argument('permission_bit', type=int,
                         help='Permission bit or addition of permission bits which needs to be reset\
                         for given user/group and token.')

    with self.argument_context('devops extension') as context:
        context.argument('include_built_in', arg_type=get_three_state_flag(),
                         help='Include built in extensions.')
        context.argument('include_disabled', arg_type=get_three_state_flag(),
                         help='Include disabled extensions.')
        context.argument('publisher_name', help='Publisher Name')
        context.argument('extension_name', help='Extension Name')
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
        context.argument('encoding', **enum_choice_list(_FILE_ENCODING_TYPE_VALUES))

    with self.argument_context('devops wiki list') as context:
        context.argument('scope', **enum_choice_list(_SCOPE_VALUES))
