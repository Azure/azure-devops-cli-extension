# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_build_arguments(self, _):
    with self.argument_context('pipelines build') as context:
        context.argument('open_browser', options_list='--open')
        context.argument('project', options_list=('--project', '-p'))
        context.argument('team_instance', options_list=('--instance', '-i'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('pipelines build list') as context:
        context.argument('definition_ids', nargs='*', type=int)
        context.argument('tags', nargs='*')

    with self.argument_context('pipelines build queue') as context:
        context.argument('definition_id', type=int)
        context.argument('variables', nargs='*')

    with self.argument_context('build show') as context:
        context.argument('build_id', options_list='--id', type=int)

    with self.argument_context('build definition show') as context:
        context.argument('definition_id', options_list='--id', type=int)

    with self.argument_context('build task') as context:
        context.argument('task_id', options_list='--id', type=str)
