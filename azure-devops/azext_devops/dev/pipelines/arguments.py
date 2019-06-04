# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list

_BUILD_REASON_VALUES = ['all', 'batchedCI', 'buildCompletion', 'checkInShelveset',
                        'individualCI', 'manual', 'pullRequest', 'schedule',
                        'triggered', 'userCreated', 'validateShelveset']

_BUILD_RESULT_VALUES = ['canceled', 'failed', 'none', 'partiallySucceeded', 'succeeded']

_BUILD_STATUS_VALUES = ['all', 'cancelling', 'completed', 'inProgress', 'none', 'notStarted', 'postponed']

_PIPELINES_QUERY_ORDER = ['NameAsc', 'NameDesc', 'ModifiedAsc', 'ModifiedDesc', 'None']

_PIPELINES_RUNS_QUERY_ORDER = ['FinishTimeAsc', 'FinishTimeDesc', 'StartTimeAsc', 'StartTimeDesc',
                               'QueueTimeAsc', 'QueueTimeDesc']

_AGENT_POOL_TYPES = ['automation', 'deployment']

_AGENT_ACTION_FILTER_TYPES = ['use', 'manage', 'none']

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

    with self.argument_context('pipelines pool') as context:
        context.argument('action', **enum_choice_list(_AGENT_ACTION_FILTER_TYPES))
        context.argument('pool_type', **enum_choice_list(_AGENT_POOL_TYPES))
