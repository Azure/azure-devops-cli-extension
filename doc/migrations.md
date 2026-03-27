# Enterprise live migrations (ELM)

The `az devops migrations` command group manages enterprise live migrations for repositories.

## Prerequisites

- Azure DevOps CLI with the Azure DevOps extension installed.
- Sign in using `az login` or `az devops login`.
- Use `--org` to authenticate and resolve credentials. For ELM migrations, `--org` is the ELM service base URL.

## Required inputs

- `--repository-id` is the Azure Repos repository GUID.
- `--target-repository` is the target repository URL.
- `--target-owner-user-id` is required for create.
- `--agent-pool` is required for create.
- `--cutover-date` / `--date` must be ISO 8601, for example: `2030-12-31T11:59:00Z`.

## Command reference

- `list`: List migrations for the ELM org. Use `--include-inactive` to include completed/failed/suspended migrations.
- `status`: Show migration status for a repository GUID.
- `create`: Create a migration. Use `--validate-only` for pre-migration checks only.
- `pause`: Pause an active migration.
- `resume`: Resume a stopped (paused, failed) migration. Optional flags:
  - `--validate-only`: Resume in validate-only mode.
  - `--migration`: Continue the migration (clears validate-only mode).
  If a migration is active, pause it before resuming.
- `cutover set` / `cutover cancel`: Schedule or cancel cutover.
- `abandon`: Abandon and delete a migration.

## Common workflows

### List migrations

```bash
az devops migrations list --org https://elm.contoso.com/elmo1
```

### List all migrations including inactive

```bash
az devops migrations list --org https://elm.contoso.com/elmo1 --include-inactive
```

### Check migration status

```bash
az devops migrations status --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Create a migration

```bash
az devops migrations create --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
  --agent-pool MigrationPool
```

### Create a validate-only migration

```bash
az devops migrations create --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
  --agent-pool MigrationPool \
  --validate-only
```

### Pause and resume

```bash
az devops migrations pause --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations resume --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations resume --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 --validate-only

az devops migrations resume --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 --migration
```

### Schedule or cancel cutover

```bash
az devops migrations cutover set --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --date 2030-12-31T11:59:00Z

az devops migrations cutover cancel --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Abandon a migration

```bash
az devops migrations abandon --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```
