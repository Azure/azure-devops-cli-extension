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
                         help='Project-scoped GitHub service connection ID (GUID). '
                              'Optional if a connection was already attached via '
                              'migrations create --pipeline-service-connection-id or '
                              'pipelines update --service-connection-id.')

    with self.argument_context('devops migrations pipelines update') as context:
        context.argument('add_ids', options_list='--add-ids', nargs='+',
                         help='Pipeline IDs to add. Accepts space-separated or comma-separated values.')
        context.argument('remove_ids', options_list='--remove-ids', nargs='+',
                         help='Pipeline IDs to remove. Accepts space-separated or comma-separated values.')
        context.argument('retry_ids', options_list='--retry-ids', nargs='+',
                         help='Failed pipeline IDs to retry. Accepts space-separated or comma-separated values.')
        context.argument('service_connection_id', options_list='--service-connection-id',
                         help='Project-scoped GitHub service connection ID (GUID).')

    with self.argument_context('devops migrations pipelines retry') as context:
        context.argument('pipeline_ids', options_list='--pipeline-ids', nargs='+',
                         help='Pipeline definition IDs to retry. Accepts space-separated '
                              'or comma-separated values.')

    with self.argument_context('devops migrations pipelines delete') as context:
        context.argument('migration_id', options_list='--migration-id', type=int,
                         help='Migration ID used for pipeline rewiring cleanup.')
        context.argument('yes', options_list=['--yes', '-y'], action='store_true',
                         help='Do not prompt for confirmation.')

    with self.argument_context('devops migrations list') as context:
        context.argument('include_all', options_list='--include-all', action='store_true',
                         help='Return the full migration history (all records per repository). '
                              'By default only the latest migration per repository is returned, '
                              'regardless of its state.')
        context.argument('include_inactive', options_list='--include-inactive', action='store_true',
                         help='Deprecated. Use --include-all instead.',
                         deprecate_info=context.deprecate(redirect='--include-all',
                                                          target='--include-inactive', hide=False))
        context.argument('project', options_list='--project',
                         help='Optional project name or ID to filter migrations.')

    with self.argument_context('devops migrations create') as context:
        context.argument('target_repository', options_list='--target-repository',
                         help='Target repository URL (must start with http:// or https://).')
        context.argument('target_owner_user_id', options_list='--target-owner-user-id',
                         help='Target repository owner user ID. Deprecated and ignored when server-side '
                              'token-based owner resolution is enabled.')
        context.argument('github_token', options_list='--github-token',
                         help='GitHub user token used for user-identity verification on the target '
                              'host. Independent of --service-endpoint-id. If omitted and '
                              '--service-endpoint-id is not provided, the CLI checks ELM_GITHUB_TOKEN '
                              'and then runs GitHub device flow. When --service-endpoint-id is '
                              'provided, device flow is skipped; pass --github-token or set '
                              'ELM_GITHUB_TOKEN to supply the user token.')
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
                         help='Service endpoint ID (GUID) for the GitHub Enterprise Server connection '
                              'used to sync commits to the target. Independent of user-identity '
                              'verification: --github-token / ELM_GITHUB_TOKEN can be supplied '
                              'alongside this flag. Device flow is skipped when this flag is set.')
        context.argument('enable_boards_github_connection',
                         options_list='--enable-boards-github-connection', action='store_true',
                         help='Opt in to provisioning the Azure Boards GitHub connection at '
                              'cutover. Off by default. Requires the Azure Boards GitHub App '
                              'to be installed on the target GitHub Enterprise organization '
                              'before the migration runs.')
        context.argument('enable_auto_discover_pipelines',
                         options_list='--enable-auto-discover-pipelines', action='store_true',
                         help='Opt in to automatic pipeline discovery at cutover. Off by default. '
                              'When enabled, the ELM sync job walks the source repository and '
                              'creates clone definitions for every pipeline that references it. '
                              'Pipeline rewiring itself is always available via '
                              'az devops migrations pipelines submit / update.')
        context.argument('pipeline_service_connection_id',
                         options_list='--pipeline-service-connection-id',
                         help='Project-scoped GitHub service connection ID (GUID) attached at '
                              'create time for pipeline rewiring. Required for full auto-discovery '
                              'when combined with --enable-auto-discover-pipelines; optional in '
                              'manual mode (pre-attaches the connection so subsequent '
                              'pipelines submit calls only need --pipeline-ids).')

    with self.argument_context('devops migrations cutover set') as context:
        context.argument('cutover_date', options_list='--date',
                         type=convert_date_string_to_iso8601,
                         help='The date and time for cutover (ISO 8601).')

    with self.argument_context('devops migrations cutover approve') as context:
        context.argument('accept_failures', options_list='--accept-failures', type=int,
                         help='Number of unprocessed migration resources to accept before '
                              'proceeding with cutover.')
        context.argument('pipelines_verified', options_list='--pipelines-verified', action='store_true',
                         help='Acknowledge that all rewired pipelines have been verified. '
                              'Required when "cutover review" returns '
                              'requiresPipelineVerificationAcknowledgment: true. Can be combined '
                              'with --accept-failures in a single approve call.')

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
