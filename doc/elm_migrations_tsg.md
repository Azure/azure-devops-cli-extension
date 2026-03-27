# ELM Migrations Troubleshooting Guide (TSG)

## Scope

- Applies to `az devops migrations` commands in the azure-devops CLI extension.
- Migration direction: Azure DevOps (source) to GitHub (target) via the ELM service.

## Key Concepts

| Concept | Details |
|---|---|
| `--org` | The **ELM service base URL** (e.g., `https://elm.contoso.com/elmo1`). This is NOT your ADO org URL. |
| `--repository-id` | The Azure Repos repository **GUID**. Get it from `az repos show --query id`. |
| `--detect` | Defaults to `true`. Auto-detects org from git remote. Use `--detect false` if outside an ADO repo or to avoid override. |
| Default org | Set with `az devops configure -d organization=<ELM URL>` so you can omit `--org` on every call. |
| `--validate-only` | Runs pre-migration checks only (no data movement). Default is `false` — omit the flag for a full migration. |

## Quick Start

### Step 1: Get source repo GUID from ADO

```powershell
az repos show --org https://dev.azure.com/<ado-org>/ --project <ProjectName> --repository <RepoName> --query id -o tsv
```

### Step 2: List existing migrations

```powershell
# List active migrations
az devops migrations list --org https://<elm-base>/elmo1 --detect false

# List all migrations (including completed, failed, suspended)
az devops migrations list --org https://<elm-base>/elmo1 --detect false --include-inactive
```

### Step 3: Create a migration

**Minimum required:**

```powershell
az devops migrations create --org https://<elm-base>/elmo1 --detect false \
  --repository-id <GUID_FROM_STEP_1> \
  --target-repository https://<target-host>/<Org>/<Repo> \
  --target-owner-user-id <OwnerUserId> \
  --agent-pool <PoolName>
```

**With validate-only mode** (pre-migration checks, no data movement):

```powershell
az devops migrations create --org https://<elm-base>/elmo1 --detect false \
  --repository-id <GUID_FROM_STEP_1> \
  --target-repository https://<target-host>/<Org>/<Repo> \
  --target-owner-user-id <OwnerUserId> \
  --agent-pool <PoolName> \
  --validate-only
```

**With all optional parameters:**

```powershell
az devops migrations create --org https://<elm-base>/elmo1 --detect false \
  --repository-id <GUID_FROM_STEP_1> \
  --target-repository https://<target-host>/<Org>/<Repo> \
  --target-owner-user-id <OwnerUserId> \
  --agent-pool <PoolName> \
  --validate-only \
  --cutover-date 2030-12-31T11:59:00Z \
  --skip-validation ActivePullRequestCount,PullRequestDeltaSize
```

### Step 4: Check status

```powershell
az devops migrations status --org https://<elm-base>/elmo1 --detect false --repository-id <GUID_FROM_STEP_1>
```

### Step 5: Pause, resume, or change mode

```powershell
# Pause an active migration
az devops migrations pause --org https://<elm-base>/elmo1 --detect false --repository-id <GUID>

# Resume (keeps current mode)
az devops migrations resume --org https://<elm-base>/elmo1 --detect false --repository-id <GUID>

# Resume and switch to validate-only mode
az devops migrations resume --org https://<elm-base>/elmo1 --detect false --repository-id <GUID> --validate-only

# Resume and switch to full migration mode
az devops migrations resume --org https://<elm-base>/elmo1 --detect false --repository-id <GUID> --migration
```

> **Note:** You must pause an active migration before resuming with a different mode.

### Step 6: Schedule or cancel cutover

```powershell
# Schedule a cutover date
az devops migrations cutover set --org https://<elm-base>/elmo1 --detect false \
  --repository-id <GUID> --date 2030-12-31T11:59:00Z

# Cancel a scheduled cutover
az devops migrations cutover cancel --org https://<elm-base>/elmo1 --detect false \
  --repository-id <GUID>
```

### Step 7: Abandon a migration

```powershell
az devops migrations abandon --org https://<elm-base>/elmo1 --detect false --repository-id <GUID>
```

> **Warning:** This permanently deletes the migration. You will be prompted to confirm.

## Complete Command & Parameter Reference

| Command | Required Params | Optional Params | HTTP | Description |
|---|---|---|---|---|
| `list` | `--org` | `--include-inactive`, `--detect` | GET | List migrations. By default only active ones. |
| `status` | `--org`, `--repository-id` | `--detect` | GET | Get detailed status for one migration. |
| `create` | `--org`, `--repository-id`, `--target-repository`, `--target-owner-user-id`, `--agent-pool` | `--validate-only`, `--cutover-date`, `--skip-validation`, `--detect` | POST | Create a new migration. |
| `pause` | `--org`, `--repository-id` | `--detect` | PUT | Pause an active migration. |
| `resume` | `--org`, `--repository-id` | `--validate-only`, `--migration`, `--detect` | PUT | Resume a stopped migration. |
| `cutover set` | `--org`, `--repository-id`, `--date` | `--detect` | PUT | Schedule a cutover date/time. |
| `cutover cancel` | `--org`, `--repository-id` | `--detect` | PUT | Cancel a scheduled cutover. |
| `abandon` | `--org`, `--repository-id` | `--detect` | DELETE | Permanently delete a migration (prompts for confirmation). |

### Parameter Details

| Parameter | Type | Used By | Description |
|---|---|---|---|
| `--org` | URL | All | ELM service base URL (e.g., `https://elm.contoso.com/elmo1`). Can be set as default. |
| `--repository-id` | GUID | All except `list` | Azure Repos repository GUID. Get from `az repos show --query id`. |
| `--target-repository` | URL | `create` | Target repository URL (e.g., `https://example.ghe.com/OrgName/RepoName`). Validated by the server. |
| `--target-owner-user-id` | string | `create` | Target repository owner user ID. |
| `--agent-pool` | string | `create` | Agent pool name for migration work. Required. |
| `--validate-only` | flag | `create`, `resume` | On `create`: run pre-migration checks only. On `resume`: switch to validate-only mode. |
| `--migration` | flag | `resume` | Switch to full migration mode (clears validate-only). Mutually exclusive with `--validate-only`. |
| `--cutover-date` | ISO 8601 | `create` | Pre-schedule cutover at creation time. E.g., `2030-12-31T11:59:00Z`. |
| `--date` | ISO 8601 | `cutover set` | Schedule cutover date/time. E.g., `2030-12-31T11:59:00Z`. |
| `--skip-validation` | string | `create` | Comma-separated list of validation policies to skip. |
| `--include-inactive` | flag | `list` | Include completed, failed, and suspended migrations. |
| `--detect` | flag | All | Auto-detect org from git remote (default: `true`). Use `--detect false` to disable. |

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| **Using ADO org URL instead of ELM URL** | 404 or unexpected errors | Use the ELM service base URL for `--org`, not `https://dev.azure.com/...` |
| **Auto-detect overrides `--org`** | Requests go to wrong host (e.g., `codedev.ms`) | Add `--detect false` or run from a non-ADO-repo directory |
| **Stale default org in config** | Requests go to old/dev URL (e.g., `codedev.ms`) | Run `az devops configure -d organization=<correct ELM URL>` to update |
| **Resume on an active migration** | Error: "Migration is active..." | Pause first with `az devops migrations pause`, then resume |
| **Both `--validate-only` and `--migration` on resume** | Error: "Please specify only one..." | Use only one flag at a time |
| **Missing `--agent-pool` on create** | Error: "--agent-pool must be specified." | Always provide `--agent-pool <PoolName>` |
| **Invalid `--repository-id`** | Error: "--repository-id must be a valid GUID." | Use `az repos show --query id` to get the correct GUID |
| **Bad date format** | Error: "must be a valid date or datetime string" | Use ISO 8601 format, e.g., `2030-12-31T11:59:00Z` |

## Common Errors and Fixes

### Authentication Errors (401 / 403)

**Symptom:** `Request failed with status 401` or `403`.

**Fix:**
1. Run `az login` (AAD) or `az devops login` (PAT).
2. Ensure the token/account has permission to the ELM service.
3. Verify `--org` points to the correct ELM URL.

### 404 Not Found

**Symptom:** `Request failed with status 404`.

**Fix:**
1. Verify the ELM base URL is correct (e.g., `https://elm.contoso.com/elmo1`).
2. Verify the `--repository-id` is a valid GUID that exists in the ELM service.

### 400 Bad Request

**Symptom:** `Request failed with status 400` or `JsonReaderException`.

**Fix:**
1. Check date values are valid ISO 8601 strings (e.g., `2030-12-31T11:59:00Z`).
2. Ensure `--target-repository` is a valid URL.
3. Ensure `--agent-pool` matches a pool name the service recognizes.

### 406 Not Acceptable

**Symptom:** `Request failed with status 406`.

**Fix:**
1. Verify the ELM base URL is correct.
2. Confirm you are using the latest CLI extension version.
3. Contact the service owner if it persists.

### 500 Internal Server Error / Retries Exhausted

**Symptom:** `Max retries exceeded with url: ... (Caused by ResponseError('too many 500 error responses'))`.

**Fix:**
1. Check if the requests are going to the **wrong host** (e.g., `codedev.ms` instead of your ELM URL).
   - Run `az devops configure -l` to check your default org.
   - Fix with `az devops configure -d organization=<correct ELM URL>`.
   - Or pass `--org <correct URL> --detect false` explicitly.
2. If the correct host is being used, the ELM service may be down — retry later or contact the service owner.

### "Warning: Azure DevOps Server not supported"

**Symptom:** Warning message appears but command may still work.

**Fix:** This warning is expected when using non-`dev.azure.com` URLs (like ELM URLs). It can be safely ignored.

## Useful Commands

```powershell
# Check extension version
az extension show -n azure-devops --query "{name:name,version:version}" -o json

# Set default org to the ELM base (so you can omit --org)
az devops configure -d organization=https://<elm-base>/elmo1

# View current defaults
az devops configure -l

# Install/update the extension from a wheel file
az extension add --source ./azure_devops-1.0.3-py2.py3-none-any.whl -y

# Uninstall the extension
az extension remove -n azure-devops

# Get repo GUID from ADO
az repos show --org https://dev.azure.com/<ado-org>/ --project <ProjectName> --repository <RepoName> --query id -o tsv

# List all migrations (including inactive)
az devops migrations list --include-inactive

# Get full JSON output (instead of table)
az devops migrations status --repository-id <GUID> -o json
```

## Output Formats

| Flag | Format | Best for |
|---|---|---|
| (default / `--output table`) | Table with key columns | Quick overview |
| `--output json` | Full JSON response from API | Scripting, debugging, seeing all fields |
| `--output tsv` | Tab-separated values | Piping to other commands |
| `--query <JMESPath>` | Filtered output | Extracting specific fields (e.g., `--query status`) |
