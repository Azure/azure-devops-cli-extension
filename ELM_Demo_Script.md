# Enterprise Live Migration (ELM) Demo Script
## 3-Minute Happy Path: Azure DevOps → GitHub Proxima

**Last Updated:** May 6, 2026  
**Duration:** ~3 minutes  
**Audience:** Enterprise developers, decision-makers  
**Tools:** Azure DevOps CLI extension v1.0.4+ (elm-migrations-preview-1p branch)

---

## Pre-Demo Checklist

- [x] Azure DevOps CLI authenticated
- [x] Source repo ID: `1c01b5a0-9479-4d6a-8317-1307181cf524`
- [x] Target repo: `https://msft.ghe.com/1ES/ELMProximaValidation`
- [x] Terminal ready

---

## Opening Remarks (0:00–0:30)

**Say (read naturally, set the stage):**

> Hi everyone. Today I want to show you Enterprise Live Migration—we call it ELM.
>
> ELM moves Azure DevOps repositories to GitHub Proxima with zero downtime. Here's what makes it different: the migration is *live*.
>
> What does that mean? Your source repository stays active. Your teams keep working while we continuously sync changes to GitHub in real-time. Then at a time you choose, we execute cutover—the source becomes read-only, GitHub becomes the source of truth.
>
> We migrate everything with full fidelity: all git history, branches, tags, pull requests, comments, reviews. No data loss whatsoever.
>
> Let me show you the happy path in about three minutes. We'll validate, promote, schedule, and execute. Let's go to the terminal.

---

## Live Demo (0:30–2:50)

### Step 1: Create & Validate Migration (0:30–1:15)

**What to say BEFORE running the command:**

> So let's start. First step is validation. I'm going to create a migration, but in validate-only mode. This means we run all pre-flight checks without actually moving data yet. We check things like: does the target repository already exist? Is the agent pool configured? Are there too many active pull requests? It's a safety net.
>
> Here's the command:

**Run this command:**
```bash
az devops migrations create \
  --org https://dev.azure.com/mseng \
  --repository-id 1c01b5a0-9479-4d6a-8317-1307181cf524 \
  --target-repository https://msft.ghe.com/1ES/ELMProximaValidation \
  --validate-only
```

**What to say WHILE waiting for output:**

> This creates the migration request. Notice three things: we pass the organization, the source repository ID, the target GitHub URL, and the `--validate-only` flag. That flag is important—it tells ELM "don't move data yet, just check if this repository is safe to migrate."

**After the command completes, immediately run the status check:**
```bash
az devops migrations status \
  --org https://dev.azure.com/mseng \
  --repository-id 1c01b5a0-9479-4d6a-8317-1307181cf524
```

**What to say AFTER seeing the status output:**

> Perfect! Look at the output. The stage is now `Synchronization` and status is `Succeeded`. That means:
> - All pre-flight checks passed ✓
> - Code has already synced to the target ✓
> - Pull requests are synced ✓
>
> Now we know this repository is safe to migrate. The validation phase is complete. Ready to move to the next step?

---

### Step 2: Promote & Schedule Cutover (1:15–2:00)

**What to say BEFORE running these commands:**

> Great! Validation passed. Now step two: I'm going to do two things at once.
>
> First, I promote this from validate-only mode to a *real* migration. That means we start continuous synchronization—any new commits, PRs, or changes in the source will continuously sync to GitHub until we tell it to stop.
>
> Second, I schedule the cutover time. This is when the switch happens—source becomes read-only, GitHub becomes the active repository.

**Run the promote command:**
```bash
az devops migrations resume \
  --org https://dev.azure.com/mseng \
  --repository-id 1c01b5a0-9479-4d6a-8317-1307181cf524 \
  --migration
```

**What to say WHILE the first command runs:**

> This command promotes the migration from validate-only to full. Notice the `--migration` flag—that tells ELM "take this validated setup and start the real migration."

**Now run the cutover schedule command:**
```bash
az devops migrations cutover set \
  --org https://dev.azure.com/mseng \
  --repository-id 1c01b5a0-9479-4d6a-8317-1307181cf524 \
  --date 2026-05-06T21:05:00Z
```

**What to say AFTER both commands complete:**

> Excellent. What just happened:
> - The migration is now LIVE—we're syncing everything continuously
> - Cutover is scheduled for 21:05:00 UTC
> - At that time, the cutover will execute automatically
>
> The system is now doing continuous sync in the background. All new code, PRs, everything flows to GitHub in real-time. Teams can still work in Azure DevOps—they won't be interrupted until cutover actually executes.

---

### Step 3: Complete & Verify (2:00–2:50)

**What to say BEFORE this final check:**

> Now we wait for cutover to complete. In a real migration, you might wait hours or days. But in this demo, we scheduled it for just a few moments from now. Let me check the current status to see if we've reached the finish line.

**Run the final status check:**
```bash
az devops migrations status \
  --org https://dev.azure.com/mseng \
  --repository-id 1c01b5a0-9479-4d6a-8317-1307181cf524 \
  --query "{Stage:stage, Status:status, CodeSync:codeSyncDate, LastUpdate:changedDate}"
```

**What to say AFTER seeing the output:**

> There it is. Stage is `Migrated`. Status is `Succeeded`. Here's what this means:
>
> ✅ All code migrated successfully  
> ✅ All pull requests migrated successfully  
> ✅ All git history preserved  
> ✅ Source repository is now read-only  
> ✅ GitHub is now the authoritative repository  
>
> The cutover is done. The repository has moved from Azure DevOps to GitHub Proxima. Teams will now switch to working in GitHub. No data loss, no downtime.
>
> That's the happy path—validate, promote, schedule, execute, done. Questions?



---

## Closing (2:50–3:00)

**What to say to wrap up:**

> So that's Enterprise Live Migration in action. Four commands, about three minutes, and the repository is safely moved from Azure DevOps to GitHub.
>
> The key points:
> - **Validation first** catches problems before you migrate data
> - **Live sync** means your teams aren't blocked
> - **You control the timing** of cutover
> - **Full data fidelity**—nothing is lost
>
> If you need to migrate repositories, ELM handles it safely and efficiently. Thanks for watching!

---

## Key Talking Points (Reference)

Use these if questions come up:

**Q: What if validation fails?**  
> You fix the blocker and try again. It's just validation—no data moved, no harm done.

**Q: Can teams still work during the sync phase?**  
> Yes. That's the whole point of "live migration." The source stays active. Teams work normally until cutover.

**Q: What happens at cutover?**  
> The source becomes read-only, GitHub becomes writable, and sync stops. Usually takes a few seconds to a few minutes.

**Q: Is there data loss?**  
> No. We migrate everything with full fidelity: full git history, all PRs with comments, reviews, everything.

**Q: How long does validation take?**  
> Typically 30 seconds to a few minutes depending on repo size and complexity.

**Q: Can I cancel a migration?**  
> Yes, use `az devops migrations abandon`. The source stays active.

---

## Quick Reference

**All commands in one block:**
```bash
ORG="https://dev.azure.com/mseng"
REPO="1c01b5a0-9479-4d6a-8317-1307181cf524"
TARGET="https://msft.ghe.com/1ES/ELMProximaValidation"

# 1. Validate
az devops migrations create --org $ORG --repository-id $REPO --target-repository $TARGET --validate-only

# 2. Check status
az devops migrations status --org $ORG --repository-id $REPO

# 3. Promote & schedule cutover
az devops migrations resume --org $ORG --repository-id $REPO --migration
az devops migrations cutover set --org $ORG --repository-id $REPO --date 2026-05-06T21:05:00Z

# 4. Verify completion
az devops migrations status --org $ORG --repository-id $REPO
```

---

## Troubleshooting (If Needed)

If cutover has failures:
```bash
# See what failed
az devops migrations cutover review --org $ORG --repository-id $REPO

# Approve and proceed
az devops migrations cutover approve --org $ORG --repository-id $REPO --accept-failures 1
```

# Schedule cutover
az devops migrations cutover set --org https://dev.azure.com/ORG --repository-id SOURCE_REPO_GUID --date 2026-05-04T20:00:00Z -o json

# Check final status
az devops migrations status --org https://dev.azure.com/ORG --repository-id SOURCE_REPO_GUID -o json
```

---

## Troubleshooting (If Demo Breaks)

### Scenario: Validation is stuck or takes too long
**What to say:**
> Validation typically completes in seconds to minutes. In real scenarios, it depends on repo size and complexity. (Pause a moment.) Let me check the detailed error output.

**What to run:**
```powershell
az devops migrations status --org https://dev.azure.com/ORG --repository-id SOURCE_REPO_GUID -o json
```

**Look for:** `statusDetails` or `failureReason` fields.

---

### Scenario: Create fails with "repo not found"
**What to say:**
> If the source repo is not found, it could be disabled or you may lack permissions. Let me quickly verify repo access.

**What to run:**
```powershell
az repos show --org https://dev.azure.com/ORG --project PROJECT_NAME --repository SOURCE_REPO_GUID
```

**Expected:** Repo metadata with `isDisabled: false`.  
**If failed:** Check repo is enabled and accessible in ADO UI.

---

### Scenario: Create fails with "403 / Manage enterprise live migrations permission"
**What to say:**
> This is a permissions issue. The caller needs the "Manage enterprise live migrations" permission on that repository. That's a granular permission we grant at the repo level for safety.

**Resolution:** Grant permission in ADO > Project Settings > Repositories > [Repo] > Security.

---

### Scenario: Cutover set fails with "Invalid date format"
**What to say:**
> Cutover date must be ISO 8601 format.

**Example valid dates:**
- `2026-05-04T20:00:00Z` (UTC)
- `2026-05-04T20:00:00-07:00` (with timezone offset)

---

## Demo Success Criteria

- [ ] Validation completes successfully
- [ ] Promotion to full migration succeeds (validateOnly → false)
- [ ] Cutover date is set
- [ ] Final status shows Migrated stage (or will after real cutover)
- [ ] ADO repo read-only banner is visible
- [ ] Proxima repo shows all branches/PRs/history

---

## References

- **Full TSG:** `doc/elm_migrations_tsg.md`
- **CLI Help:** `az devops migrations --help`
- **API Version:** 7.2-preview (`/_apis/elm/migrations`)

---

## Notes for Presenter

- **If validation is slow:** Say: "In production this typically runs in seconds to minutes. Let me show you the current state."
- **Close with:** "And that's ELM. Orchestrated, controlled, full-fidelity migration with zero disruption until you schedule cutover. Enterprise-grade migration."

---

**Good luck with your demo!**
