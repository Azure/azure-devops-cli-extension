# Mark Work Items as stale

## When to use

Work Items which are untouched for a very long time can be marked as stale using this script.

## How to use

### Script Mode

1. Invoke the Script with required params-

This command will add {Probot: Stale} tag to all the work itmes assigned to user "user@fabrikam.com" in <https://dev.azure.com/fabrikam> organization which are not changed in last 30 days

```cmd
.\markStaleWorkItem.ps1 -organization https://dev.azure.com/fabrikam -assignedTo user@fabrikam.com -daysUntilStale 30 -daysUntilClose 60
```
