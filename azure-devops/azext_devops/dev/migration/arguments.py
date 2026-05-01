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
                         help='ID of the Azure Repos repository (GUID).')

    with self.argument_context('devops migrations list') as context:
        context.argument('include_inactive', options_list='--include-inactive', action='store_true',
                         help='Include inactive (completed, abandoned, failed) migrations in the results.')
        context.argument('project', options_list='--project',
                         help='Optional project name or ID to filter migrations.')

    with self.argument_context('devops migrations create') as context:
        context.argument('target_repository', options_list='--target-repository',
                         help='Target repository URL (must start with http:// or https://).')
        context.argument('target_owner_user_id', options_list='--target-owner-user-id',
                         help='Target repository owner user ID. Deprecated and ignored when server-side '
                              'token-based owner resolution is enabled.')
        context.argument('github_token', options_list='--github-token',
                         help='GitHub token used for migration authorization. If omitted, the CLI first '
                              'checks ELM_GITHUB_TOKEN and then runs GitHub device flow.')
        context.argument('validate_only', options_list='--validate-only', action='store_true',
                         help='Create in validate-only mode (pre-migration checks only).')
        context.argument('cutover_date', options_list='--cutover-date',
                         type=convert_date_string_to_iso8601,
                         help='Scheduled cutover date/time (ISO 8601).')
        context.argument('agent_pool', options_list='--agent-pool',
                         help='Agent pool name to use for migration work.')
        context.argument('skip_validation', options_list='--skip-validation',
                         help='Validation policies to skip. Accepts either a comma-separated list of '
                              'policy names (for example, AgentPoolExists,MaxRepoSize) or a non-negative '
                              'integer bitmask.')
        context.argument('service_endpoint_id', options_list='--service-endpoint-id',
                         help='Service endpoint ID (GUID) for GitHub Enterprise Server connection.')

    with self.argument_context('devops migrations cutover set') as context:
        context.argument('cutover_date', options_list='--date',
                         type=convert_date_string_to_iso8601,
                         help='The date and time for cutover (ISO 8601).')

    with self.argument_context('devops migrations cutover approve') as context:
        context.argument('accept_failures', options_list='--accept-failures', type=int,
                         help='Number of unprocessed migration resources to accept before '
                              'proceeding with cutover.')

    with self.argument_context('devops migrations resume') as context:
        context.argument('validate_only', options_list='--validate-only', action='store_true',
                         help='Resume in validate-only mode.')
        context.argument('migration', options_list='--migration', action='store_true',
                         help='Promote a succeeded validate-only migration to a full migration '
                              '(sets validateOnly=false and statusRequested=active).')

    with self.argument_context('devops migrations abandon') as context:
        context.argument('remove_read_only', options_list='--remove-read-only', action='store_true',
                         help='Also set the Azure Repos repository back to read-write state by '
                              'sending removeReadOnly=true.')
