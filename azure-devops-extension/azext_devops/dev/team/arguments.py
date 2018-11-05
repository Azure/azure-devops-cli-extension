# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import ArgumentsContext, enum_choice_list

# CUSTOM CHOICE LISTS
_ON_OFF_SWITCH_VALUES = ['on', 'off']
_YES_NO_SWITCH_VALUES = ['yes', 'no']
_OUTPUT_VALUES = ['json', 'jsonc', 'table', 'tsv']
_SOURCE_CONTROL_VALUES = ['git', 'tfvc']
_PROJECT_VISIBILITY_VALUES = ['private', 'public']
_STATE_VALUES = ['invalid', 'unchanged', 'all', 'new', 'wellformed', 'deleting', 'createpending']


def load_team_arguments(self, _):
    with self.argument_context('devops login') as context:
        context.argument('team_instance', options_list=('--instance', '-i'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with self.argument_context('devops logout') as context:
        context.argument('team_instance', options_list=('--instance', '-i'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
    with self.argument_context('devops configure') as context:
        context.argument('defaults', options_list=('--defaults', '-d'), nargs='*')
    with self.argument_context('devops project') as context:
        context.argument('team_instance', options_list=('--instance', '-i'))
        context.argument('process', options_list=('--process', '-p'))
        context.argument('source_control', options_list=('--source-control', '-s'),
                    **enum_choice_list(_SOURCE_CONTROL_VALUES))
        context.argument('description', options_list=('--description', '-d'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('state', **enum_choice_list(_STATE_VALUES))
        context.argument('project_id', options_list='--id')
        context.argument('visibility',**enum_choice_list(_PROJECT_VISIBILITY_VALUES))
    with self.argument_context('devops project delete') as context:
        context.argument('yes', options_list=['--yes', '-y'], action='store_true', help='Do not prompt for confirmation.')
    with self.argument_context('devops configure') as context:
        context.argument('collect_telemetry', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('enable_log_file', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('use_git_aliases', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('suppress_update_message', **enum_choice_list(_YES_NO_SWITCH_VALUES))
        context.argument('default_output', **enum_choice_list(_OUTPUT_VALUES))
        context.argument('list_config', options_list=('--list', '-l'))
