# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import get_three_state_flag
from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
from azext_devops.dev.team.arguments import load_global_args


# pylint: disable=too-many-statements
def load_migration_arguments(self, _):
    with self.argument_context('devops migrations') as context:
        load_global_args(context)
        context.argument('repository_id', options_list='--repository-id',
                         help='ID of the repository (GUID).')

    with self.argument_context('devops migrations create') as context:
        context.argument('target_repository', options_list='--target-repository',
                         help='Target GitHub repository URL. Example: https://microsoft.ghe.com/OrgName/RepoName')
        context.argument('target_owner_user_id', options_list='--target-owner-user-id',
                         help='Target repository owner user ID.')
        context.argument('validate_only', options_list='--validate-only',
                         help='Validate only (true/false). Defaults to true.',
                         arg_type=get_three_state_flag())
        context.argument('scheduled_cutover_date', options_list='--scheduled-cutover-date',
                         type=convert_date_string_to_iso8601,
                         help='Scheduled cutover date/time (ISO 8601).')
        context.argument('agent_pool_name', options_list='--agent-pool-name',
                         help='Agent pool name for migration validation.')
        context.argument('skip_validation', options_list='--skip-validation',
                         help='Comma-separated list of validation checks to skip. '
                              'Values: None, ActivePullRequestCount, PullRequestDeltaSize, '
                              'TargetRepoMigration, All.')

    with self.argument_context('devops migrations cutover set') as context:
        context.argument('scheduled_cutover_date', options_list='--scheduled-cutover-date',
                         type=convert_date_string_to_iso8601,
                         help='Scheduled cutover date/time (ISO 8601).')

    with self.argument_context('devops migrations set-validate-only') as context:
        context.argument('on', options_list='--on', action='store_true',
                         help='Set validate-only to true.')
        context.argument('off', options_list='--off', action='store_true',
                         help='Set validate-only to false.')
