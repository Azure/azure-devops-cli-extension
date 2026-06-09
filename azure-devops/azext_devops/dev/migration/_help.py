# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_migration_help():
    helps['devops migrations'] = """
    type: group
    short-summary: Manage enterprise live migrations.
    long-summary: 'This command group is a part of the azure-devops extension and is in preview. Availability may be limited (for example, to 1P/allowlisted users). For ELM migrations, --org should be your Azure DevOps organization URL (for example: https://dev.azure.com/myorg).'
    """

    helps['devops migrations list'] = """
    type: command
    short-summary: List migrations in an organization.
    long-summary: 'By default the latest migration per repository is returned, regardless of state. Use --include-all to return the full migration history.'
    examples:
      - name: List the latest migration per repository.
        text: |
          az devops migrations list --org https://dev.azure.com/myorg
      - name: List the full migration history for every repository.
        text: |
          az devops migrations list --org https://dev.azure.com/myorg --include-all
    """

    helps['devops migrations status'] = """
    type: command
    short-summary: Get migration status for a repository.
    examples:
      - name: Get migration status by repository id.
        text: |
          az devops migrations status --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000
    """

    helps['devops migrations create'] = """
    type: command
    short-summary: Create a migration for a repository.
    long-summary: 'If --github-token is not provided, the CLI checks ELM_GITHUB_TOKEN and then runs GitHub device flow to acquire a token.'
    examples:
      - name: Create a migration.
        text: |
          az devops migrations create --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --target-repository https://github.com/OrgName/RepoName --agent-pool <your-agent-pool>
      - name: Create a validate-only migration.
        text: |
          az devops migrations create --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --target-repository https://github.com/OrgName/RepoName --agent-pool <your-agent-pool> --validate-only --skip-validation ActivePullRequestCount,PullRequestDeltaSize
      - name: Create using a pre-generated GitHub token or PAT.
        text: |
          az devops migrations create --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --target-repository https://github.com/OrgName/RepoName --github-token <token>
    """

    helps['devops migrations pause'] = """
    type: command
    short-summary: Pause an active migration.
    """

    helps['devops migrations resume'] = """
    type: command
    short-summary: Resume a stopped (paused, failed) migration.
    examples:
      - name: Resume using the current mode.
        text: |
          az devops migrations resume --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000
      - name: Resume in validate-only mode.
        text: |
          az devops migrations resume --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --validate-only
      - name: Continue migration (clears validate-only mode).
        text: |
          az devops migrations resume --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --migration
    """

    helps['devops migrations abandon'] = """
    type: command
    short-summary: Abandon a migration.
    long-summary: 'Moves the migration to an abandoned/failed state; the migration record is not purged. Pipeline rewiring data is left intact so a subsequent migration can reuse it.'
    examples:
      - name: Abandon and keep repository read-only (default).
        text: |
          az devops migrations abandon --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000
      - name: Abandon and set repository back to read-write.
        text: |
          az devops migrations abandon --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --remove-read-only
    """

    helps['devops migrations cutover'] = """
    type: group
    short-summary: Manage migration cutover.
    """

    helps['devops migrations cutover review'] = """
    type: command
    short-summary: Review unprocessed migration items before cutover.
    long-summary: 'The response includes requiresPipelineVerificationAcknowledgment. When true, cutover approve must be re-run with --pipelines-verified before the migration can proceed.'
    examples:
      - name: Review failures before approving cutover.
        text: |
          az devops migrations cutover review --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000
    """

    helps['devops migrations cutover approve'] = """
    type: command
    short-summary: Approve cutover by accepting unprocessed items and/or verifying rewired pipelines.
    long-summary: 'Provide --accept-failures when cutover review surfaces unprocessed items, and/or --pipelines-verified when cutover review reports requiresPipelineVerificationAcknowledgment: true. At least one of the two must be supplied; both may be sent together in a single call.'
    examples:
      - name: Approve cutover after reviewing failures.
        text: |
          az devops migrations cutover approve --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --accept-failures 3
      - name: Acknowledge pipeline verification only (no unprocessed items).
        text: |
          az devops migrations cutover approve --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --pipelines-verified
      - name: Combine failure acceptance and pipeline verification in one call.
        text: |
          az devops migrations cutover approve --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --accept-failures 3 --pipelines-verified
    """

    helps['devops migrations cutover set'] = """
    type: command
    short-summary: Schedule cutover for a migration.
    examples:
      - name: Schedule cutover.
        text: |
          az devops migrations cutover set --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --date 2030-12-31T11:59:00Z
    """

    helps['devops migrations cutover cancel'] = """
    type: command
    short-summary: Cancel a scheduled cutover.
    """

    helps['devops migrations pipelines'] = """
    type: group
    short-summary: Manage pipeline rewiring for migrations. (Preview)
    """

    helps['devops migrations pipelines list'] = """
    type: command
    short-summary: List pipeline rewiring configuration and per-pipeline status.
    examples:
      - name: List pipeline rewiring status.
        text: |
          az devops migrations pipelines list --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000
    """

    helps['devops migrations pipelines submit'] = """
    type: command
    short-summary: Submit pipelines for rewiring. (Preview)
    examples:
      - name: Submit pipelines with service connection and repository mappings.
        text: |
          az devops migrations pipelines submit --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --pipeline-ids 42 43 44 --service-connection-id 11111111-1111-1111-1111-111111111111 --repository-mapping aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa=myorg/shared-templates
    """

    helps['devops migrations pipelines update'] = """
    type: command
    short-summary: Bulk update pipeline rewiring configuration. (Preview)
    examples:
      - name: Add, remove, and update service connection.
        text: |
          az devops migrations pipelines update --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --add-ids 50 51 --remove-ids 42 --service-connection-id 22222222-2222-2222-2222-222222222222
    """

    helps['devops migrations pipelines retry'] = """
    type: command
    short-summary: Retry failed pipeline rewiring entries. (Preview)
    examples:
      - name: Retry specific failed pipelines.
        text: |
          az devops migrations pipelines retry --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --pipeline-ids 42 43
    """

    helps['devops migrations pipelines delete'] = """
    type: command
    short-summary: Delete pipeline rewiring data for a migration. (Preview)
    examples:
      - name: Delete rewiring config and cloned definitions.
        text: |
          az devops migrations pipelines delete --org https://dev.azure.com/myorg --repository-id 00000000-0000-0000-0000-000000000000 --migration-id 7 --yes
    """
