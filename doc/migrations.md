# Enterprise live migrations (ELM)

The `az devops migrations` command group manages enterprise live migrations for repositories.

## Prerequisites

- Azure DevOps CLI with the Azure DevOps extension installed.
- Sign in using `az login` or `az devops login`.
- Use `--org` to authenticate and resolve credentials.

## Required inputs

- `--repository-id` is the Azure Repos repository GUID.
- `--target-repository` must be a GitHub Enterprise Server URL in this format:
  `https://microsoft.ghe.com/OrgName/RepoName`
- `--target-owner-user-id` is required for create.
- `--scheduled-cutover-date` must be ISO 8601, for example: `2030-12-31T11:59:00Z`.

## Common workflows

### List migrations

```bash
az devops migrations list --org https://codedev.ms/elmo1
```

### Check migration status

```bash
az devops migrations status --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Create a validation-only migration

```bash
az devops migrations create --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --target-repository https://microsoft.ghe.com/OrgName/RepoName \
  --target-owner-user-id OwnerId \
  --validate-only
```

### Turn validate-only off

```bash
az devops migrations set-validate-only --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 --off
```

### Start full migration

```bash
az devops migrations migrate --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Pause and resume

```bash
az devops migrations pause --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000

az devops migrations resume --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Schedule or cancel cutover

```bash
az devops migrations cutover set --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000 \
  --scheduled-cutover-date 2030-12-31T11:59:00Z

az devops migrations cutover cancel --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```

### Abandon a migration

```bash
az devops migrations abandon --org https://codedev.ms/elmo1 \
  --repository-id 00000000-0000-0000-0000-000000000000
```
