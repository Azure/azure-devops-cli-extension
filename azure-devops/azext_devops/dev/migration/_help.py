# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_migration_help():
    helps['devops migrations'] = """
    type: group
    short-summary: Manage enterprise live migrations.
    long-summary: This command group is a part of the azure-devops extension.
    """

    helps['devops migrations list'] = """
    type: command
    short-summary: List migrations in an organization.
    examples:
      - name: List migrations.
        text: |
          az devops migrations list --org https://codedev.ms/elmo1
    """

    helps['devops migrations status'] = """
    type: command
    short-summary: Get migration status for a repository.
    examples:
      - name: Get migration status by repository id.
        text: |
          az devops migrations status --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000
    """

    helps['devops migrations create'] = """
    type: command
    short-summary: Create a migration for a repository.
    examples:
      - name: Create a validation-only migration.
        text: |
          az devops migrations create --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 \
            --target-repository https://microsoft.ghe.com/1ES/Gardener --target-owner-user-id GeoffCoxMSFT --validate-only
      - name: Create a migration with optional validation settings.
        text: |
          az devops migrations create --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 \
            --target-repository https://microsoft.ghe.com/1ES/Gardener --target-owner-user-id GeoffCoxMSFT \
            --agent-pool-name MigrationPool --skip-validation ActivePullRequestCount,PullRequestDeltaSize
    """

    helps['devops migrations pause'] = """
    type: command
    short-summary: Pause an active migration.
    """

    helps['devops migrations resume'] = """
    type: command
    short-summary: Resume a paused migration.
    """

    helps['devops migrations abandon'] = """
    type: command
    short-summary: Abandon and delete a migration.
    """

    helps['devops migrations set-validate-only'] = """
    type: command
    short-summary: Set validate-only mode on or off.
    examples:
      - name: Turn validate-only on.
        text: |
          az devops migrations set-validate-only --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --on
      - name: Turn validate-only off.
        text: |
          az devops migrations set-validate-only --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 --off
    """

    helps['devops migrations migrate'] = """
    type: command
    short-summary: Start full migration after validation.
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
          az devops migrations cutover set --org https://codedev.ms/elmo1 --repository-id 00000000-0000-0000-0000-000000000000 \
            --scheduled-cutover-date 2030-12-31T11:59:00Z
    """

    helps['devops migrations cutover cancel'] = """
    type: command
    short-summary: Cancel a scheduled cutover.
    """
