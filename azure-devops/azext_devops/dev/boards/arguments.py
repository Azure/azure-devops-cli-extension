# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_work_arguments(self, _):
    with self.argument_context('boards') as context:
        context.argument('project', options_list=('--project', '-p'))
        context.argument('organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('boards work-item create') as context:
        context.argument('work_item_type', type=str, options_list='--type')
        context.argument('fields', nargs='*', options_list=('--fields', '-f'))
        context.argument('description', options_list=('--description', '-d'))

    with self.argument_context('boards work-item update') as context:
        context.argument('fields', nargs='*', options_list=('--fields', '-f'))
        context.argument('description', options_list=('--description', '-d'))

    with self.argument_context('boards work-item delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')
