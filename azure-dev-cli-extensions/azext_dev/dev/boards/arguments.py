# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_work_arguments(self, _):
    with self.argument_context('boards') as context:
        context.argument('open_browser', options_list='--open')
        context.argument('project', options_list=('--project', '-p'))
        context.argument('team_instance', options_list=('--instance', '-i'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('boards item') as context:
        context.argument('work_item_id', type=int, options_list='--id')
        context.argument('work_item_type', type=str, options_list='--type')
        context.argument('fields', nargs='*', options_list=('--fields', '-f'))
        context.argument('description', options_list=('--description', '-d'))

    with self.argument_context('boards item query') as context:
        context.argument('query_id', type=str, options_list='--id')
