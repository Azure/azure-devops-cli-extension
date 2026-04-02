# ELM Migrations — End-to-End Guide & Troubleshooting (TSG)

Migrate Git repositories from Azure DevOps to GitHub using the `az devops migrations` CLI commands.

> **Shell note:** Examples use `\` for line continuation (bash/zsh). In PowerShell, use backtick `` ` `` instead, or put the entire command on one line.

---

## 1. Prerequisites & Setup

### 1.1 Install Azure CLI (if not already installed)

Follow [Install the Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

Verify it's installed:

```powershell
az --version
```

### 1.2 Install the ELM extension from the wheel file

You'll receive a `.whl` file (e.g., `azure_devops-1.0.3-py2.py3-none-any.whl`). This is the Azure DevOps CLI extension package that contains the migration commands.

```powershell
# Remove any existing version first (ignore errors if not installed)
az extension remove -n azure-devops

# Install from the wheel file (use the actual path to your .whl file)
az extension add --source ./azure_devops-1.0.3-py2.py3-none-any.whl -y

# Verify installation — you should see name: "azure-devops" and a version
az extension show -n azure-devops --query "{name:name,version:version}" -o json
```

### 1.3 Sign in

```powershell
# Option A: Azure AD / Entra ID (recommended)
az login

# Option B: Personal Access Token (needs "Full access" or at minimum Code Read/Write scope)
az devops login
```

### 1.4 Set your default ELM org (recommended)

This saves you from typing `--org` on every single command:

```powershell
az devops configure -d organization=https://<elm-base>/elmo1
```

> **Important:** `--org` is the **ELM service base URL** (e.g., `https://elm.contoso.com/elmo1`).
> This is **NOT** your Azure DevOps org URL (`https://dev.azure.com/myorg`).
> Ask your ELM service owner for the correct URL if you don't have it.

### 1.5 Verify your config

```powershell
az devops configure -l
```

You should see your ELM URL under `organization`. If you see a wrong URL (e.g., `codedev.ms` or `dev.azure.com`), re-run step 1.4 with the correct URL.

---

## 2. Understand the Migration Lifecycle

A migration moves through these **stages**:

```
Queued → Validation → Synchronization → Cutover → Migrated
```

And has one of these **statuses**:

| Status | Meaning |
|---|---|
| `Active` | Migration is running (in one of the stages above) |
| `Succeeded` | Migration completed successfully |
| `Failed` | Migration encountered an error (can be resumed) |
| `Suspended` | Migration was paused by the user (can be resumed) |

### Recommended workflow

The safest approach is **validate first, then migrate**:

```
Create (validate-only) → Check status → Pause → Resume (--migration) → Monitor → Schedule cutover → Done
```

---

## 3. End-to-End Walkthrough

### What you'll need before starting

| Item | Example | How to get it |
|---|---|---|
| ELM service URL | `https://elm.contoso.com/elmo1` | Ask your ELM service owner |
| Azure DevOps org URL | `https://dev.azure.com/myorg` | Your ADO org (only needed for step 3.1) |
| ADO project name | `MyProject` | The project containing the source repo |
| ADO repo name | `my-repo` | The repo you want to migrate |
| Target repo URL | `https://example.ghe.com/OrgName/RepoName` | Create the empty target repo in GitHub **before** starting |
| Target owner user ID | `GeoffCoxMSFT` | The GitHub user ID who owns the target repo |
| Agent pool name | `MigrationPool` | Ask your ELM service owner |

### 3.1 Get the source repository GUID from Azure DevOps

Every migration command uses a repository GUID (not the repo name). Get it from your ADO org:

```powershell
az repos show --org https://dev.azure.com/myorg/ --project MyProject --repository my-repo --query id -o tsv
```

Example output:
```
b3e18946-5b39-40ca-8e2f-d0eb683d8a85
```

Save this GUID — you'll use it in every command below.

### 3.2 (Optional) Check for existing migrations

See if any migrations already exist for your org:

```powershell
# Active migrations only
az devops migrations list --detect false

# All migrations including completed/failed/suspended
az devops migrations list --detect false --include-inactive
```

### 3.3 Create a validate-only migration

Start with validation to catch any issues **before** moving data. This runs pre-migration checks without transferring any code or PRs:

```powershell
az devops migrations create --detect false \
  --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85 \
  --target-repository https://example.ghe.com/OrgName/RepoName \
  --target-owner-user-id GeoffCoxMSFT \
  --agent-pool MigrationPool \
  --validate-only
```

The command returns the migration details as JSON. The migration begins immediately in the background.

> **Tip:** If you're confident and want to start a full migration right away (skip validate-only), omit the `--validate-only` flag.

**Optional parameters you can add at creation time:**

| Parameter | What it does | Example |
|---|---|---|
| `--cutover-date` | Pre-schedule the final cutover date | `--cutover-date 2030-12-31T11:59:00Z` |
| `--skip-validation` | Skip specific validation checks | `--skip-validation ActivePullRequestCount,PullRequestDeltaSize` |

### 3.4 Monitor migration status

Check status anytime — run this as often as you need:

```powershell
az devops migrations status --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85
```

For the full JSON response (useful for debugging):

```powershell
az devops migrations status --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85 -o json
```

**How to read the output:**

| You see this | It means | What to do next |
|---|---|---|
| `status: Active`, `stage: Validation` | Validation is in progress | Wait, check again later |
| `status: Active`, `stage: Synchronization` | Code/PRs are syncing | Wait, check again later |
| `status: Succeeded` | Current phase completed | If validate-only: go to step 3.5. If migration: go to step 3.6 |
| `status: Failed` | Something went wrong | Check the error in `-o json` output, fix the issue, then resume (step 4) |
| `status: Suspended` | You paused it | Resume when ready (step 3.5) |

### 3.5 Promote from validate-only to full migration

**When to do this:** After step 3.4 shows `status: Succeeded` (validation passed).

You need to pause first (because the migration may still be active), then resume in migration mode:

```powershell
# Step A: Pause the current migration
az devops migrations pause --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85

# Step B: Resume as a full migration (this starts data movement)
az devops migrations resume --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85 --migration
```

> **If you get:** `Migration is active (status: ..., stage: ...). Pause it before resuming or changing mode.`
> Run the pause command first (Step A), then retry Step B.

After this, monitor with step 3.4 until `stage: Synchronization` is running.

### 3.6 Schedule cutover

Once synchronization is running and you're ready to finalize the migration:

```powershell
az devops migrations cutover set --detect false \
  --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85 --date 2030-12-31T11:59:00Z
```

> **Date format:** Must be ISO 8601. Examples: `2030-12-31T11:59:00Z`, `2030-06-15T08:00:00-07:00`

Changed your mind? Cancel the scheduled cutover:

```powershell
az devops migrations cutover cancel --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85
```

### 3.7 Verify completion

After cutover completes, confirm the migration finished:

```powershell
az devops migrations status --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85
```

**Success looks like:** `status: Succeeded`, `stage: Migrated`.

At this point your repository has been fully migrated from Azure DevOps to GitHub. Verify the target repo in GitHub has all your code, branches, and pull requests.

### 3.8 (If needed) Abandon a migration

If something went wrong and you want to delete the migration entirely and start over:

```powershell
az devops migrations abandon --detect false --repository-id b3e18946-5b39-40ca-8e2f-d0eb683d8a85
```

> **Warning:** This permanently deletes the migration record. You will be prompted to confirm. After abandoning, you can create a new migration for the same repository.

---

## 4. Other Scenarios

### Pause and resume without changing mode

If you need to temporarily stop a migration and restart it in the same mode:

```powershell
# Pause
az devops migrations pause --detect false --repository-id <GUID>

# Resume (keeps whatever mode — validate-only or full migration — it was in)
az devops migrations resume --detect false --repository-id <GUID>
```

### Switch back to validate-only after starting full migration

Changed your mind after promoting to full migration? You can go back:

```powershell
az devops migrations pause --detect false --repository-id <GUID>
az devops migrations resume --detect false --repository-id <GUID> --validate-only
```

### Resume a failed migration

If a migration fails (you'll see `status: Failed` in the status output), you can resume it directly — no pause needed since it's already stopped:

```powershell
# Resume in the same mode
az devops migrations resume --detect false --repository-id <GUID>

# Or resume and switch mode at the same time
az devops migrations resume --detect false --repository-id <GUID> --migration
az devops migrations resume --detect false --repository-id <GUID> --validate-only
```

---

## 5. Complete Command & Parameter Reference

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

### 5.1 Parameter Details

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

## 6. Common Pitfalls

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

## 7. Common Errors and Fixes

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

## 8. Useful Commands

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

## 9. Output Formats

| Flag | Format | Best for |
|---|---|---|
| (default / `--output table`) | Table with key columns | Quick overview |
| `--output json` | Full JSON response from API | Scripting, debugging, seeing all fields |
| `--output tsv` | Tab-separated values | Piping to other commands |
| `--query <JMESPath>` | Filtered output | Extracting specific fields (e.g., `--query status`) |
