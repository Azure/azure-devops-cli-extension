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

    with self.argument_context('devops migrations pipelines') as context:
        context.argument('repository_mapping', options_list='--repository-mapping', action='append',
                         help='Repository mapping in the format <sourceRepoId>=<targetOwner>/<targetRepo>. '
                              'Can be provided multiple times.')

    with self.argument_context('devops migrations pipelines submit') as context:
        context.argument('pipeline_ids', options_list='--pipeline-ids', nargs='+',
                         help='Pipeline definition IDs. Accepts space-separated values '
                              '(for example, 42 43 44) or comma-separated values '
                              '(for example, 42,43,44).')
        context.argument('service_connection_id', options_list='--service-connection-id',
                         help='Project-scoped GitHub service connection ID (GUID).')

    with self.argument_context('devops migrations pipelines update') as context:
        context.argument('add_ids', options_list='--add-ids', nargs='+',
                         help='Pipeline IDs to add. Accepts space-separated or comma-separated values.')
        context.argument('remove_ids', options_list='--remove-ids', nargs='+',
                         help='Pipeline IDs to remove. Accepts space-separated or comma-separated values.')
        context.argument('retry_ids', options_list='--retry-ids', nargs='+',
                         help='Failed pipeline IDs to retry. Accepts space-separated or comma-separated values.')
        context.argument('acknowledge_ids', options_list='--acknowledge-ids', nargs='+',
                         help='Pipeline IDs to acknowledge. Accepts space-separated or comma-separated values.')
        context.argument('service_connection_id', options_list='--service-connection-id',
                         help='Project-scoped GitHub service connection ID (GUID).')

    with self.argument_context('devops migrations pipelines retry') as context:
        context.argument('pipeline_ids', options_list='--pipeline-ids', nargs='+',
                         help='Pipeline definition IDs to retry. Accepts space-separated '
                              'or comma-separated values.')

    with self.argument_context('devops migrations pipelines acknowledge') as context:
        context.argument('pipeline_ids', options_list='--pipeline-ids', nargs='+',
                         help='Pipeline definition IDs to acknowledge. Accepts space-separated '
                              'or comma-separated values.')

    with self.argument_context('devops migrations pipelines delete') as context:
        context.argument('migration_id', options_list='--migration-id', type=int,
                         help='Migration ID used for pipeline rewiring cleanup.')
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')

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
                         help='GitHub token used for migration authorization. Ignored when '
                              '--service-endpoint-id is specified. If omitted, the CLI first '
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
                              'policy names (for example, AgentPoolExists,MaxFileSize) or a non-negative '
                              'integer bitmask.')
        context.argument('service_endpoint_id', options_list='--service-endpoint-id',
                         help='Service endpoint ID (GUID) for the GitHub Enterprise Server connection. '
                              'When specified, the server uses the service connection for GitHub '
                              'authentication and the CLI skips GitHub device flow. Mutually exclusive '
                              'with --github-token.')

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
