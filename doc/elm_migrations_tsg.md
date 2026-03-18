# ELM migrations troubleshooting guide (TSG)

## Scope
- Applies to `az devops migrations` commands in the azure-devops CLI extension.
- Migration direction: Azure DevOps (source) to GitHub (target) via the ELM service.

## Key concepts
- `--org` for migrations is the ELM service base URL, not the ADO org.
- The ADO org is only used to look up the source repo GUID (`az repos show`).
- `--detect` defaults to true. If you run commands inside an ADO git repo, auto-detect can override `--org`.
  Use `--detect false` or run from a directory that is not inside an ADO repo.

## Quick start
1) Get source repo GUID from ADO:
```powershell
az repos show --org https://dev.azure.com/<ado-org>/ --project <ProjectName> --repository <RepoName> --query id -o tsv
```

2) Create a validation-only migration (default is validate-only):
```powershell
az devops migrations create --org https://<elm-base>/elm --detect false \
  --repository-id <GUID_FROM_STEP_1> \
  --target-repository https://<ghe-host>/<Org>/<Repo> \
  --target-owner-user-id <GHE_UserId>
```

3) Check status:
```powershell
az devops migrations status --org https://<elm-base>/elm --detect false --repository-id <GUID_FROM_STEP_1>
```

4) Start full migration after validation passes:
```powershell
az devops migrations resume --org https://<elm-base>/elm --detect false --repository-id <GUID_FROM_STEP_1> --migrate
```

5) Re-run validation (optional):
```powershell
az devops migrations resume --org https://<elm-base>/elm --detect false --repository-id <GUID_FROM_STEP_1> --validate-only
```
6) Optional cutover:
```powershell
az devops migrations cutover set --org https://<elm-base>/elm --detect false \
  --repository-id <GUID_FROM_STEP_1> --scheduled-cutover-date 2030-12-31T11:59:00Z
```

## Common pitfalls
- **Auto-detect override**: If you are inside an ADO repo, `--detect` may override your ELM base URL.
  Use `--detect false`.
- **Wrong org for migrations**: Using `https://dev.azure.com/...` with `az devops migrations` will hit ADO
  instead of ELM and fail.
- **Too many parallel migrations**: Run one migration at a time unless your service owner says otherwise.
- **Resume fails while active**: `resume` is meant for non-active states (succeeded, failed, suspended). Pause first if needed.

## Common errors and fixes
- **401/403 Unauthorized**: You are not logged in or the token lacks permission.
  Run `az devops login` (PAT) or `az login` (AAD) as required by your environment.
- **404 Not Found**: The ELM base URL or repo GUID is incorrect.
- **406 Not Acceptable**: The ELM service rejected the request. Verify the ELM base URL includes `/elm`,
  confirm you are using the latest extension, and contact the service owner if it persists.
- **Warning: Azure DevOps Server not supported**: This can appear when using non-dev.azure.com URLs.
  It is expected for ELM and can usually be ignored.
- **Target repo validation error**: The CLI validates that the target host is `github.com` or `*.ghe.com`.
  If you see an error like `--target-repository must be a https://github.com/OrgName/RepoName or https://<org>.ghe.com/OrgName/RepoName URL`,
  verify the target URL host or update the validation rule for your environment.

## Useful commands
```powershell
# Check extension version
az extension show -n azure-devops --query "{name:name,version:version}" -o json

# Set default org to the ELM base
az devops configure -d organization=https://<elm-base>/elm
```
