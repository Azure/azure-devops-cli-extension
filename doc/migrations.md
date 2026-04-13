# Enterprise live migrations (ELM)

The `az devops migrations` command group manages enterprise live migrations for repositories.

## Prerequisites

- Azure DevOps CLI with the Azure DevOps extension installed.
- Sign in using `az login` or `az devops login`.
- Configure a default org once to avoid repeating `--org`:

```bash
az devops configure --defaults organization=https://dev.azure.com/myorg
```

- You can still override per command with `--org`.

## Required inputs

- `--repository-id` is the Azure Repos repository GUID.
- `--target-repository` is the target repository URL.
- `--target-owner-user-id` is required for create.
- `--agent-pool` is optional for create.
- `--cutover-date` / `--date` must be ISO 8601, for example: `2030-12-31T11:59:00Z`.

### How to find `--repository-id`

```bash
az repos show --repository MyRepo --project MyProject --query id -o tsv
```

## Command reference

- `list`: List migrations for the org. Use `--include-inactive` to include completed/failed/suspended migrations.
- `status`: Show migration status for a repository GUID.
- `create`: Create a migration. Use `--validate-only` for pre-migration checks only.
- `pause`: Pause an active migration.
- `resume`: Resume a stopped (paused, failed) migration. Optional flags:
  - `--validate-only`: Resume in validate-only mode.
  - `--migration`: Promote a succeeded validate-only migration to full migration.
    This updates the existing migration by setting `validateOnly=false` and `statusRequested=active`.
  If a migration is active, pause it before resuming.
- `cutover set` / `cutover cancel`: Schedule or cancel cutover.
- `abandon`: Abandon and delete a migration.

## Status fields

- `statusRequested`: Desired state requested by client.
- `status`: Current overall status reported by service.
- `stage`: Current active stage (for example, validation, synchronization, cutover).

If a command is blocked, inspect all three fields from `status` output to understand whether the migration is active, terminal, or promotable.

## Common workflows

### List migrations

```bash
az devops migrations list --org https://dev.azure.com/myorg
```

### List all migrations including inactive

```bash
az devops migrations list --org https://dev.azure.com/myorg --include-inactive
```

### Check migration status

```bash
az devops migrations status --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Create a migration

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
  --agent-pool MigrationPool
```

### Create a validate-only migration

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
  --agent-pool MigrationPool \
  --validate-only
```

### Pause and resume

```bash
az devops migrations pause --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations resume --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations resume --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 --validate-only

az devops migrations resume --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 --migration
```

### Promote a succeeded validate-only migration

After validation succeeds, run:

```bash
az devops migrations resume --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 --migration
```

This promotes the same migration record (no new migration is created).

### Schedule or cancel cutover

```bash
az devops migrations cutover set --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --date 2030-12-31T11:59:00Z

az devops migrations cutover cancel --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Abandon a migration

```bash
az devops migrations abandon --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000
```

## Troubleshooting

- Error: migration is active.
  Pause first, then retry resume or mode changes.

```bash
az devops migrations pause --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000
```

- Error: validation already succeeded.
  Use `resume --migration` to promote instead of re-running validate-only.

- Error: `--target-repository` must be valid.
  Ensure it is a fully qualified URL starting with `http://` or `https://`.
