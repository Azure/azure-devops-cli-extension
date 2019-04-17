# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_work_arguments(self, _):
    with self.argument_context('boards') as context:
        context.argument('project', options_list=('--project', '-p'))

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

    with self.argument_context('boards work-item relation') as context:
        context.argument('id', help='The ID of the work item')
        context.argument('relation_type', help='Relation type to create. example: parent, child ')
        context.argument('target_ids', help='ID(s) of work-items to create relation with. \
                         Multiple values can be passed , seperated. Example: 1,2 ')
