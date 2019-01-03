# Opening an artifact in browser

You can use --open switch to open any artifact in your default browser.

For example :
```
bash
az boards work-item show --id 1 --open 
```
This will show the details of work item with id 1 and also open it in the default browser.

# Auto-detect repository

By default, detect flag is on for every command.
So, if your current working directory is a git repository, Azure devops CLI would try to auto detect organization, project and repository.

If you want to run any command for a particular orgainzation/project, you can give argument
