# Enterprise live migrations (ELM)

The `az devops migrations` command group (Preview) manages enterprise live migrations for repositories.
Availability may be limited (for example, to 1P/allowlisted users).

## Prerequisites

- Azure DevOps CLI with the Azure DevOps extension installed.
- Sign in using `az login` or `az devops login`.
- Configure a default org once to avoid repeating `--org`:

```bash
az devops configure --defaults organization=https://dev.azure.com/myorg
```

- You can still override per command with `--org`.
- If your current git remote points to another org, add `--detect false` to avoid auto-detect choosing the wrong organization.

## Migration lifecycle model

Typical active stages:

`queued -> validation -> synchronization -> cutover`

Key fields in `status` output:

- `statusRequested`: Desired state requested by the CLI (for example, `active`, `suspended`).
- `status`: Service-reported status (for example, `succeeded`, `failed`).
- `stage`: Current running stage while active.

Use all three fields together when troubleshooting state transitions.

## Required inputs

- `--repository-id` is the Azure Repos repository GUID.
- `--target-repository` is the target repository URL.
- `--github-token` is optional for create. If not provided, the CLI checks `ELM_GITHUB_TOKEN` and then runs GitHub device flow.
- `--target-owner-user-id` is deprecated and ignored when server-side token ownership resolution is enabled.
- `--agent-pool` is optional for create.
- `--cutover-date` / `--date` must be ISO 8601, for example: `2030-12-31T11:59:00Z`.
- `--skip-validation` accepts either comma-separated policy names or a non-negative integer bitmask.

Validation enforced by the CLI:

- `--target-repository` must start with `http://` or `https://`.
- `--repository-id` must be a valid GUID.
- `--skip-validation` policy names must be recognized values.

### How to find `--repository-id`

```bash
az repos show --repository MyRepo --project MyProject --query id -o tsv
```

## Command reference

- `list`: List migrations for the org. Use `--include-inactive` to include completed/failed/suspended migrations. Use `--project` to filter by project name or ID.
- `status`: Show migration status for a repository GUID.
- `create`: Create a migration. Use `--validate-only` for pre-migration checks only.
- `pause`: Pause an active migration.
- `resume`: Resume a stopped (paused, failed) migration. Optional flags are `--validate-only` (resume in validate-only mode) and `--migration` (promote a succeeded validate-only migration to full migration by setting `validateOnly=false` and `statusRequested=active`). If a migration is currently active, pause it before resuming or switching mode.
- `cutover set` / `cutover cancel`: Schedule or cancel cutover.
- `abandon`: Abandon and delete a migration.

## Status fields

- `statusRequested`: Desired state requested by client.
- `status`: Current overall status reported by service.
- `stage`: Current active stage (for example, validation, synchronization, cutover).

If a command is blocked, inspect all three fields from `status` output to understand whether the migration is active, terminal, or promotable.

## Promotion semantics

When validation succeeds in validate-only mode, promotion does not create a new migration.

Promotion command:

```bash
az devops migrations resume --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 --migration
```

What this does:

- Sends an update (PUT) to the existing migration.
- Sets `validateOnly=false`.
- Sets `statusRequested=active`.

## Common workflows

### List migrations

```bash
az devops migrations list --org https://dev.azure.com/myorg
```

### List migrations for a project

```bash
az devops migrations list --org https://dev.azure.com/myorg --project MyProject
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
  --agent-pool MigrationPool
```

### Create a validate-only migration

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --agent-pool MigrationPool \
  --validate-only
```

### Create a migration using explicit token or PAT

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --github-token <token>
```

### Create a migration with skip-validation

Recommended form using policy names:

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --skip-validation AgentPoolExists,MaxRepoSize
```

Advanced form using integer bitmask:

```bash
az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --skip-validation 132
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

If you receive an active-state error, pause first and retry:

```bash
az devops migrations pause --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000
```

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

- Error: missing GitHub token or device-flow setup.
  Pass `--github-token`, set `ELM_GITHUB_TOKEN`, or complete the interactive GitHub device-flow prompt shown by CLI.

- Error: `--skip-validation` contains unsupported policy names.
  Use supported names such as `AgentPoolExists`, `MaxRepoSize`, or pass a non-negative integer bitmask.

- Error: requests are sent to the wrong org.
  Use `--org <url> --detect false`, and verify defaults via `az devops configure -l`.

- Error: migration already succeeded.
  Use `abandon` to reset before creating a new migration.

- Error: active migration already exists for repository.
  The create command returns: `"An active migration already exists for repository <GUID>. Delete (abandon) the existing migration before creating a new one."` This means a non-terminal migration already exists for that repository GUID. Abandon it first, then retry create.

```bash
az devops migrations abandon --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations create --org https://dev.azure.com/myorg \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://example.ghe.com/OrgName/RepoName
```
