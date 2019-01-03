## Set up defaults and using git defaults

Azure Devops CLI supports setting up defaults like organization and project for ease of use. e.g.

```
az devops configure --defaults organization=https://dev.azure.com/myorganization  project=myproject
```

Default args will be used in any commands where these args are inputs but are not provided with the command.

Default values can be also detected from the git remote url. If you are running a command from inside a git repository folder, organization, project and repository name will be auto-detected from the git remote url.

## Listing the defaults

You can list the defaults by running below command.
```
az devops configure --list
```

## Using git-aliases


For more information on configurations check help for configure command.

```
az devops configure -h
```
