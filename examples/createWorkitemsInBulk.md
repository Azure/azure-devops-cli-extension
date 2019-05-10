# Creating work items in bulk

## When to use

You can create large number of workitems through a text file input or interactively. Common use case is when planning a project or bug bash. 

## How to use

### Interactive Mode

Just invoke the script and answer the questions to use the default organization, project and workitem type.

```
> .\createWorkitemsInBulk.ps1

Sample Usage -
createWorkitemsinBulk.ps1 -workitem_titles ./my_wit_titles -wit_template ./my_wit_template

Template not provided will ask for default params interactively. Alternatively create a wit template and pass it to the script.

Organization URL: : https://dev.azure.com/baggaatul24
Project Name: : deletetest
Workitem Type: : Task
```

You will be prompted for workitem titles and keep creating new items as you press enter. Press Ctrl+C to break.

```
No file for workitem titles. Will run in interactive mode to create workitems.

Enter workitem title: : Test issue 1 - XYZ not working
ID    Type    Title                           Assigned To    State
----  ------  ------------------------------  -------------  -------
106   Task    Test issue 1 - XYZ not working                 New

Enter workitem title: :
```

### Script Mode

1. Create a file with workitem titles in different lines e.g. my_wit_title.txt has content-

```
XYZ is not working
Service enhancement - add caching logic 
Fix the issue in caching
```

1. Create a file with template for default organization and project to be used when creating workitems. e.g. my_wit_template.txt has content-

```
organization=https://dev.azure.com/ContosoOrg
project=ContosoProject
workitem_type=Bug
```

Invoke the Script with the template and titles files as follows-

```
.\createWorkitemsInBulk.ps1 -workitem_titles .\my_wit_titles.txt -wit_template .\my_wit_template.txt
```






