# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
from azext_devops.dev.team.arguments import load_global_args


# pylint: disable=too-many-statements
def load_migration_arguments(self, _):
    with self.argument_context('devops migrations') as context:
        load_global_args(context)
        context.argument('repository_id', options_list='--repository-id',
                         help='ID of the repository (GUID).')

    with self.argument_context('devops migrations list') as context:
        context.argument('include_inactive', options_list='--include-inactive', action='store_true',
                         help='Include inactive (completed, abandoned, failed) migrations in the results.')

    with self.argument_context('devops migrations create') as context:
        context.argument('target_repository', options_list='--target-repository',
                         help='Target repository URL.')
        context.argument('target_owner_user_id', options_list='--target-owner-user-id',
                         help='Target repository owner user ID.')
        context.argument('validate_only', options_list='--validate-only', action='store_true',
                         help='Create in validate-only mode (pre-migration checks only).')
        context.argument('cutover_date', options_list='--cutover-date',
                         type=convert_date_string_to_iso8601,
                         help='Scheduled cutover date/time (ISO 8601).')
        context.argument('agent_pool', options_list='--agent-pool',
                         help='Agent pool name to use for migration work.')
        context.argument('skip_validation', options_list='--skip-validation',
                         help='Comma-separated list of validation policies to skip (e.g. MaxFileSize,ActivePullRequestCount).')

    with self.argument_context('devops migrations cutover set') as context:
        context.argument('cutover_date', options_list='--date',
                         type=convert_date_string_to_iso8601,
                         help='The date and time for cutover (ISO 8601).')

    with self.argument_context('devops migrations resume') as context:
        context.argument('validate_only', options_list='--validate-only', action='store_true',
                         help='Resume in validate-only mode.')
        context.argument('migration', options_list='--migration', action='store_true',
                         help='Continue the migration (clears any validate-only mode).')
