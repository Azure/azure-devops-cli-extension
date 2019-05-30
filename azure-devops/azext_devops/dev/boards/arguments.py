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

    with self.argument_context('boards work-item relation add') as context:
        context.argument('relation_type', help='Relation type to create. Example: parent, child ')
        context.argument('target_id', help='ID(s) of work-items to create relation with. \
                         Multiple values can be passed comma separated. Example: 1,2 ')

    with self.argument_context('boards work-item relation remove') as context:
        context.argument('relation_type', help='Relation type to remove. Example: parent, child ')
        context.argument('target_id', help='ID(s) of work-items to remove relation from. \
                         Multiple values can be passed comma separated. Example: 1,2 ')

    with self.argument_context('boards iteration project') as context:
        context.argument('path',  help='Iteration path.')

    with self.argument_context('boards iteration project show') as context:
        context.argument('id', type=int)

    with self.argument_context('boards iteration project create') as context:
        context.argument('path',  help='Iteration path. Creates an iteration at root level if --path is not specified.')

    with self.argument_context('boards area') as context:
        context.argument('path',  help='Area path.')

    with self.argument_context('boards area project create') as context:
        context.argument('path',  help='Area path. Creates an area at root level if --path is not specified.')

    with self.argument_context('boards area team') as context:
        context.argument('team',  help='The name or id of the team.')

