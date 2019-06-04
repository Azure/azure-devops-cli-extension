# Automating Team Project set up

In any team, project, or an organization there is a need to templatize and automate processes associated with a project. E.g.
You may want to templatize the project creation  process.

**Scaffolding.ps1** is a powershell script which helps users of an organization to have a standard getting started experience.

## Sample command to invoke the script –

.\scaffolding.ps1 -filePath .\org_details.txt

## Input parameters expected

You can either interactively provide inputs or pass a file instead. The contents of file would look something like this:

    org=https://dev.azure.com/contoso

    projectName=cliDemoScaffolding

    repoName=cli_repo

    repoToImport = https://github.com/ishitam8/snake.git

    teamName=Protocol CLI team

    optionalReviewers=user1@contoso.com,user2@contoso.com

    requiredReviewers=user3@contoso.com,user4@contoso.com

    teamMembers=user1@contoso.com,user2@contoso.com,user3@contoso.com

    teamAdminMembers=admin1@contoso.com,admin2@contoso.com

    childIterationNamesList=Sprint 1,Sprint 2,Sprint 3

    iterationsPermissionsBit=7

## What does this script do

1. Takes Your organization URL
   `[org=https://dev.azure.com/contoso]`
1. Creates a new project under this organization
   `[projectName=cliDemoScaffolding]`
1. Creates a new Repository
   `[repoName=cli_repo]`
1. Repository URL to be imported in the newly created repo
   `[repoToImport = https://github.com/ishitam8/snake.git]`
   Accepts only public repo URL.
1. List of required reviewers for configuring branch policies
   `[requiredReviewers=user1@contoso.com,user2@contoso.com]`
   Currently, these branch policies are applied on master.
1. List of required reviewers for configuring branch policies
   `[optionalReviewers=user3@contoso.com,user4@contoso.com]`
   Currently, these branch policies are applied on master.
1. Creates a team
   `[teamName=Protocol CLI team]`
1. Adds the list of team members to the new team
   `[teamMembers=user1@contoso.com,user2@contoso.com,user3@contoso.com]`
1. Creates a corresponding admins group which would be used to manage this team.
   Add this admins group as `Team administrator` of this team.
1. Adds the list of admin members to the team admin group
   `[teamAdminMembers=admin1@contoso.com,admin2@contoso.com]`
1. Boards settings for this team
    Setting up area
    - Creates a new area for this team and sets it to default area for this team.
    Iterations related settings
    - Creates a root iteration by the same name as team [i.e teamName].
    - Creates child iterations which will be added this root iteration
      `[childIterationNamesList=Sprint1,Sprint2,Sprint3]`.
    - Configure/add these root and child iterations to the newly created team.
    - Give iterations related permissions to the admins group
      `[iterationsPermissionsBit=7]`
      The permission bit 7 denotes the addition of required permission bits to be allowed to this admins group.
      Which shall be as follows
      View permissions for this node = 1
      Edit this node = 2
      Create child nodes = 4
    General settings
    - Configure backlog navigation settings [Currently assumed as epics: true, features: true, stories: true]
    - Configure working days [Currently assumed as Monday to Friday]
