# Enterprise live migrations (ELM)

The `az devops migrations` command group manages enterprise live migrations for repositories.

## Prerequisites

- Azure DevOps CLI with the Azure DevOps extension installed.
- Sign in using `az login` or `az devops login`.
- Use `--org` to authenticate and resolve credentials. For ELM migrations, `--org` is the ELM service base URL.

## Required inputs

- `--repository-id` is the Azure Repos repository GUID.
- `--target-repository` must be a GitHub URL in this format:
  `https://github.com/OrgName/RepoName` or `https://example.ghe.com/OrgName/RepoName`
- `--target-owner-user-id` is required for create.
- `--scheduled-cutover-date` must be ISO 8601, for example: `2030-12-31T11:59:00Z`.

## Command reference

- `list`: List migrations for the ELM org.
- `status`: Show migration status for a repository GUID.
- `create`: Create a validation-only migration. `--validate-only false` is not supported.
  Use `resume --migrate` to move from validation to migration.
- `pause`: Pause an active migration.
- `resume`: Resume a non-active migration. Optional flags:
  - `--validate-only`: Resume and force validate-only.
  - `--migrate`: Resume and start migration.
  If a migration is active, pause it before resuming.
- `cutover set` / `cutover cancel`: Schedule or cancel cutover.
- `abandon`: Abandon and delete a migration.

## Common workflows

### List migrations

```bash
az devops migrations list --org https://elm.contoso.com/elmo1
```

### Check migration status

```bash
az devops migrations status --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Create a validation-only migration

```bash
az devops migrations create --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://github.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
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
  --repository-id 00000000-0000-0000-0000-000000000000 --migrate
```

### Schedule or cancel cutover

```bash
az devops migrations cutover set --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --scheduled-cutover-date 2030-12-31T11:59:00Z

az devops migrations cutover cancel --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Abandon a migration

```bash
az devops migrations abandon --org https://elm.contoso.com/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```
