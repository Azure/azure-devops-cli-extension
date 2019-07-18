# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list
from azure.cli.core.commands.parameters import get_three_state_flag

_BUILD_REASON_VALUES = ['all', 'batchedCI', 'buildCompletion', 'checkInShelveset',
                        'individualCI', 'manual', 'pullRequest', 'schedule',
                        'triggered', 'userCreated', 'validateShelveset']

_BUILD_RESULT_VALUES = ['canceled', 'failed', 'none', 'partiallySucceeded', 'succeeded']

_BUILD_STATUS_VALUES = ['all', 'cancelling', 'completed', 'inProgress', 'none', 'notStarted', 'postponed']

_PIPELINES_QUERY_ORDER = ['NameAsc', 'NameDesc', 'ModifiedAsc', 'ModifiedDesc', 'None']

_PIPELINES_RUNS_QUERY_ORDER = ['FinishTimeAsc', 'FinishTimeDesc', 'StartTimeAsc', 'StartTimeDesc',
                               'QueueTimeAsc', 'QueueTimeDesc']

_AGENT_POOL_TYPES = ['automation', 'deployment']

_ACTION_FILTER_TYPES = ['use', 'manage', 'none']

_VAR_GROUPS_QUERY_ORDER = ['Asc', 'Desc']


# pylint: disable=too-many-statements
def load_build_arguments(self, _):
    with self.argument_context('pipelines build list') as context:
        context.argument('definition_ids', nargs='*', type=int)
        context.argument('tags', nargs='*')
        context.argument('reason', **enum_choice_list(_BUILD_REASON_VALUES))
        context.argument('result', **enum_choice_list(_BUILD_RESULT_VALUES))
        context.argument('status', **enum_choice_list(_BUILD_STATUS_VALUES))

    with self.argument_context('pipelines build queue') as context:
        context.argument('definition_id', type=int)
        context.argument('variables', nargs='*')

    with self.argument_context('pipelines build definition list') as context:
        context.argument(
            'repository_type',
            choices=['tfsversioncontrol', 'tfsgit', 'git', 'github', 'githubenterprise', 'bitbucket', 'svn'],
            type=str.lower)

    with self.argument_context('pipelines release list') as context:
        context.argument('definition_id', type=int)

    with self.argument_context('pipelines release create') as context:
        context.argument('definition_id', type=int)
        context.argument('artifact_metadata_list', nargs='*')

    with self.argument_context('pipelines release definition list') as context:
        context.argument('artifact_type', choices=['build', 'jenkins', 'github', 'externaltfsbuild', 'git', 'tfvc'],
                         type=str.lower)

    with self.argument_context('pipelines runs list') as context:
        context.argument('pipeline_ids', nargs='*', type=int)
        context.argument('tags', nargs='*')
        context.argument('reason', **enum_choice_list(_BUILD_REASON_VALUES))
        context.argument('result', **enum_choice_list(_BUILD_RESULT_VALUES))
        context.argument('status', **enum_choice_list(_BUILD_STATUS_VALUES))
        context.argument('query_order', **enum_choice_list(_PIPELINES_RUNS_QUERY_ORDER))

    with self.argument_context('pipelines run') as context:
        context.argument('id', type=int)
        context.argument('variables', nargs='*')

    with self.argument_context('pipelines list') as context:
        context.argument('query_order', **enum_choice_list(_PIPELINES_QUERY_ORDER))
        context.argument(
            'repository_type',
            choices=['tfsversioncontrol', 'tfsgit', 'git', 'github', 'githubenterprise', 'bitbucket', 'svn'],
            type=str.lower)

    with self.argument_context('pipelines create') as context:
        context.argument('repository_type', choices=['tfsgit', 'github'], type=str.lower)
        context.argument('yml_path', options_list=('--yml-path', '--yaml-path'))

    with self.argument_context('pipelines update') as context:
        context.argument('yml_path', options_list=('--yml-path', '--yaml-path'))

    with self.argument_context('pipelines pool') as context:
        context.argument('pool_id', options_list=('--pool-id', '--id'))
        context.argument('action', **enum_choice_list(_ACTION_FILTER_TYPES))
        context.argument('pool_type', **enum_choice_list(_AGENT_POOL_TYPES))

    with self.argument_context('pipelines agent') as context:
        context.argument('agent_id', options_list=('--agent-id', '--id'))
        context.argument('include_capabilities', arg_type=get_three_state_flag())
        context.argument('include_assigned_request', arg_type=get_three_state_flag())
        context.argument('include_last_completed_request', arg_type=get_three_state_flag())

    with self.argument_context('pipelines queue') as context:
        context.argument('queue_id', options_list=('--queue-id', '--id'))
        context.argument('action', **enum_choice_list(_ACTION_FILTER_TYPES))

    with self.argument_context('pipelines variable-group') as context:
        context.argument('group_id', options_list=('--group-id', '--id'))
        context.argument('variables', nargs='*')
        context.argument('query_order', **enum_choice_list(_VAR_GROUPS_QUERY_ORDER))
        context.argument('action_filter', options_list=('--action-filter', '--action'),
                         **enum_choice_list(_ACTION_FILTER_TYPES))
        context.argument('secret', arg_type=get_three_state_flag())
        context.argument('authorize', arg_type=get_three_state_flag())
        context.argument('prompt_value', arg_type=get_three_state_flag())

    with self.argument_context('pipelines variable') as context:
        context.argument('secret', arg_type=get_three_state_flag())
        context.argument('prompt_value', arg_type=get_three_state_flag())
        context.argument('allow_override', arg_type=get_three_state_flag())
