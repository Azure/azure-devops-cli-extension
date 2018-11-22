# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_build_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'build') as ac:
        ac.argument('open_browser', options_list='--open')
        ac.argument('project', options_list=('--project', '-p'))
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))

    with ArgumentsContext(cli_command_loader, 'build list') as ac:
        ac.argument('definition_ids', nargs='*', type=int)
        ac.argument('tags', nargs='*')

    with ArgumentsContext(cli_command_loader, 'build queue') as ac:
        ac.argument('definition_id', type=int)
        ac.argument('variables', nargs='*')

    with ArgumentsContext(cli_command_loader, 'build show') as ac:
        ac.argument('build_id', options_list='--id', type=int)

    with ArgumentsContext(cli_command_loader, 'build definition show') as ac:
        ac.argument('definition_id', options_list='--id', type=int)

    with ArgumentsContext(cli_command_loader, 'build definition list') as ac:
        ac.argument('repository_type', choices=['TfsVersionControl', 'TfsGit', 'Git', 'GitHub', 'GitHubEnterprise', 'Bitbucket', 'Svn'])

    with ArgumentsContext(cli_command_loader, 'build task') as ac:
        ac.argument('task_id', options_list='--id', type=str)
