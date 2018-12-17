# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']

_BUILD_REASON_VALUES = ['all', 'batchedCI', 'buildCompletion', 'checkInShelveset', 
    'individualCI', 'manual', 'pullRequest', 'schedule', 
    'triggered', 'userCreated', 'validateShelveset']	

_BUILD_RESULT_VALUES = ['canceled', 'failed', 'none', 'partiallySucceeded',	'succeeded']

_BUILD_STATUS_VALUES = [ 'all','cancelling', 'completed', 'inProgress', 'none', 'notStarted', 'postponed']

def load_build_arguments(self, _):
    with self.argument_context('pipelines build') as context:
        context.argument('open_browser', options_list='--open')
        context.argument('project', options_list=('--project', '-p'))
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('pipelines build list') as context:
        context.argument('definition_ids', nargs='*', type=int)
        context.argument('tags', nargs='*')
        context.argument('reason', **enum_choice_list(_BUILD_REASON_VALUES))
        context.argument('result', **enum_choice_list(_BUILD_RESULT_VALUES))
        context.argument('status', **enum_choice_list(_BUILD_STATUS_VALUES))

    with self.argument_context('pipelines build queue') as context:
        context.argument('definition_id', type=int)
        context.argument('variables', nargs='*')

    with self.argument_context('pipelines build show') as context:
        context.argument('build_id', options_list='--id', type=int)

    with self.argument_context('pipelines build definition show') as context:
        context.argument('definition_id', options_list=('--definition-id', '--id'), type=int)

    with self.argument_context('pipelines build definition list') as context:
        context.argument('repository_type', choices=['tfsversioncontrol', 'tfsgit', 'git', 'github', 'githubenterprise', 'bitbucket', 'svn'],
        type=str.lower)

    with self.argument_context('pipelines build task') as context:
        context.argument('task_id', options_list='--id', type=str)

    with self.argument_context('pipelines release') as context:
        context.argument('open_browser', options_list='--open')
        context.argument('project', options_list=('--project', '-p'))
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with self.argument_context('pipelines release list') as context:
        context.argument('definition_id', type=int)

    with self.argument_context('pipelines release create') as context:
        context.argument('definition_id', type=int)
        context.argument('artifact_metadata_list', nargs='*')

    with self.argument_context('pipelines release show') as context:
        context.argument('release_id', options_list='--id', type=int)

    with self.argument_context('pipelines release definition show') as context:
        context.argument('definition_id', options_list='--id', type=int)

    with self.argument_context('pipelines release definition list') as context:
        context.argument('artifact_type', choices=['build', 'jenkins', 'github', 'externaltfsbuild', 'git', 'tfvc'], type=str.lower)
