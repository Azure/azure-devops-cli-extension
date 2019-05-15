# PR Review Reminder

## When to use

PRs where user is added as a reviewer and have not commented in last n days can be detected using this script.

## How to use

### Script Mode

1. Invoke the Script with required params-

```cmd
.\PRReviewReminder.ps1 -organization https://dev.azure.com/fabrikam -username user@fabrikam.com -notReviewedInLastNDays 1 -project fabrikamProject
```
