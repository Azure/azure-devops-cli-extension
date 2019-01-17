# Auto-detect repository

By default, detect flag is 'on' for every command.
So, if your current working directory is a git repository, Azure devops CLI would try to auto detect organization, project and repository.

If you want to run any command for a particular orgainzation or project, you can explicity give it as an argument. 
```
az boards work-item show --id 1 --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
```