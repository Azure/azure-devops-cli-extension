# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_migration_help():
    helps['devops migrations'] = """
    type: group
    short-summary: Manage enterprise live migrations.
    long-summary: 'This command group is a part of the azure-devops extension. For ELM migrations, --org should be the ELM service base URL (for example: https://elm.contoso.com/elmo1).'
    """

    helps['devops migrations list'] = """
    type: command
    short-summary: List migrations in an organization.
    examples:
      - name: List migrations.
        text: |
          az devops migrations list --org https://elm.contoso.com/elmo1
      - name: List all migrations including inactive ones.
        text: |
          az devops migrations list --org https://elm.contoso.com/elmo1 --include-inactive
    """

    helps['devops migrations status'] = """
    type: command
    short-summary: Get migration status for a repository.
    examples:
      - name: Get migration status by repository id.
        text: |
          az devops migrations status --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000
    """

    helps['devops migrations create'] = """
    type: command
    short-summary: Create a migration for a repository.
    examples:
      - name: Create a migration.
        text: |
          az devops migrations create --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --target-repository https://example.ghe.com/OrgName/RepoName --target-owner-user-id GeoffCoxMSFT --agent-pool MigrationPool
      - name: Create a validate-only migration.
        text: |
          az devops migrations create --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --target-repository https://example.ghe.com/OrgName/RepoName --target-owner-user-id GeoffCoxMSFT --agent-pool MigrationPool --validate-only --skip-validation ActivePullRequestCount,PullRequestDeltaSize
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
          az devops migrations resume --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000
      - name: Resume in validate-only mode.
        text: |
          az devops migrations resume --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --validate-only
      - name: Continue migration (clears validate-only mode).
        text: |
          az devops migrations resume --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --migration
    """

    helps['devops migrations abandon'] = """
    type: command
    short-summary: Abandon and delete a migration.
    """

    helps['devops migrations cutover'] = """
    type: group
    short-summary: Manage migration cutover.
    """

    helps['devops migrations cutover set'] = """
    type: command
    short-summary: Schedule cutover for a migration.
    examples:
      - name: Schedule cutover.
        text: |
          az devops migrations cutover set --org https://elm.contoso.com/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --date 2030-12-31T11:59:00Z
    """

    helps['devops migrations cutover cancel'] = """
    type: command
    short-summary: Cancel a scheduled cutover.
    """
