
param(
    [String]$filePath
)
. (Join-Path $PSScriptRoot .\Boards\boardsettings.ps1)
. (Join-Path $PSScriptRoot .\Repos\setPolicies.ps1)
. (Join-Path $PSScriptRoot .\configureTeam.ps1)


#get input params

if (!$filePath) {
    Write-Host("`nFile input not provided so switching the script to interactive mode to ask default parameters.")
    $org = "https://dev.azure.com/CliDemo" # Read-host("`nOrganization URL ")
    $projectName = Read-host("Project Name ")
    $repoName = Read-host("Repo Name ")
    $repoToImport = Read-host("Repo Import URL ")
    
    $requiredReviewersInput = Read-host("Required reviewers(Comma separated EMail IDs) ")
    $requiredReviewers = if ($requiredReviewersInput) { $requiredReviewersInput.split(",") } 

    $optionalReviewersInput = Read-host("Optional reviewers(Comma separated EMail IDs) ")
    $optionalReviewers = if ($optionalReviewersInput) { $optionalReviewersInput.split(",") }

    $teamName = Read-host("Team Name ")

    $teamMembersInput = Read-host("Team Members(Comma separated EMail IDs) ")
    $teamMembers = if ($teamMembersInput) { $teamMembersInput.split(",") }
    
    $teamAdminMembersInput = Read-host("Team Admin Members(Comma separated EMail IDs) ")
    $teamAdminMembers = if ($teamAdminMembersInput) { $teamAdminMembersInput.split(",") }
    

    $childIterationNamesInput = Read-host("Child iterations list(Comma separated) ")
    $childIterationNamesList = if ($childIterationNamesInput) { $childIterationNamesInput.split(",") }

    Write-Host("`nThanks for providing all the required details. Now just sit back and relax, script is in action now . . . ")
}
else {
    $values = Get-Content $filePath | Out-String | ConvertFrom-StringData
    $org = $values.org
    $projectName = $values.projectName
    $repoName = $values.repoName
    $repoToImport = $values.repoToImport
    $teamName = $values.teamName
    $requiredReviewers = $values.requiredReviewers.split(",")
    $optionalReviewers = $values.optionalReviewers.split(",")
    $teamMembers = $values.teamMembers.split(",")
    $teamAdminMembers = $values.teamAdminMembers.split(",")
    $childIterationNamesList = $values.childIterationNamesList.split(",")
    $iterationsPermissionsBit = $values.iterationsPermissionsBit

    Write-Host("`nAll the required parameters are read from file at $($filePath)  Now just sit back and relax, script is in action now . . . ")
}

$invokeRequestsPath = . Join-Path $PSScriptRoot InvokeRequests\
If (!(test-path $invokeRequestsPath)) {
    New-Item -ItemType Directory -Force -Path $invokeRequestsPath
}

# scaffolding
Write-Host "`nCreating project with name $($projectName) . . . " 
$project = az devops project create --org $org --name $projectName --process Agile -o json | ConvertFrom-Json
Write-Host "Created project with name $($project.name) and Id $($project.id)" 


if ($repoName) { 
    Write-Host "`nCreating repository with name $($repoName) . . . " 
    $repo = az repos create --org $org -p $projectName --name $repoName -o json | ConvertFrom-Json
    Write-Host "Created repository with name $($repo.name) and Id $($repo.id)"

    if ($repoToImport) {
        Write-Host "`nImporting repository from url $($repoToImport)" 
        $importRepo = az repos import create --org $org -p $project.id -r $repo.id --git-url $repoToImport -o json | ConvertFrom-Json
        Write-Host "Repo imported with Status $($importRepo.status)"
        if ($requiredReviewers -or $optionalReviewers) {
            $policiesSet = set_policies -org $org -projectName $project.id -repoId $repo.id -branch 'master' -requiredApprovers $requiredReviewers -optionalApprovers $optionalReviewers
            Write-Host "`nBranch policies set for master"
        }
    }
}
else {
    Write-Host "`nSkipping repo creation as repo name is empty"
}

# team set up
$apiVersion = '5.0'
if ($teamName) {
    Write-Host "`nCreating team with name $($teamName) . . . " 
    $createTeam = az devops team create --name $teamName  --org $org -p $project.id -o json | ConvertFrom-Json
    Write-Host "Created team with name $($createTeam.name) and Id $($createTeam.id)"
    if ($teamMembers) {
        $listGroups = az devops security group list --org $org -p $project.id -o json | ConvertFrom-Json
        foreach ($grp in $listGroups.graphGroups) {
            if ($grp.displayName -eq $teamName) {
                # Add team members
                addTeamMembers -org $org -teamMembersList $teamMembers -teamDescriptor $grp.descriptor
                # create a team admin group and add it to this team
                $teamAdminGroupName = $teamName + ' Admins'
                $createTeamAdminsGroup = az devops security group create --org $org -p $project.id --name $teamAdminGroupName --groups $grp.descriptor -o json | ConvertFrom-Json 
                Write-Host "`nCreated new admin group with name $($teamAdminGroupName) and added to the newly created team $($createTeam.name)."

                if ($teamAdminMembers) {
                    addTeamMembers -org $org -teamMembersList $teamAdminMembers -teamDescriptor $createTeamAdminsGroup.descriptor
                }
                # add this newly created Admin group as Team Administrators
                addTeamAdmins -org $org -projectID $project.id -teamID $($createTeam.id) -adminGrpDescriptor $createTeamAdminsGroup.descriptor

                #create Area for this team
                createTeamArea -org $org -projectID $project.id -areaName $teamName

                # area path
                $areaPath = $projectName + '\' + $teamName
                configureDefaultArea -org $org -projectID $project.id -teamID $($createTeam.id) -defaultAreaPath $areaPath
                
                # Configure project level iterations with this group/team and grant permissions for admins group
                $projectIterationNameForThisTeam = $teamName + ' iteration' 
                $rootIterationId = projectLevelIterationsSettings -org $org -projectID $project.id -rootIterationName $projectIterationNameForThisTeam -subject $createTeamAdminsGroup.descriptor -allow $iterationsPermissionsBit -childIterationNamesList $childIterationNamesList
            
                #set backlog iteration ID
                $setBacklogIteration = az boards iteration team set-backlog-iteration --id $rootIterationId --team $createTeam.id --org $org -p $project.id -o json | ConvertFrom-Json 

                # Boards General settings
                setUpGeneralBoardSettings -org $org -projectID $project.id -teamID $($createTeam.id) -epics $true -stories $true -features $true 
                
                # Add child iterations of backlog iteration to the given team
                setUpTeamIterations -org $org -projectID $projectName -teamID $($createTeam.id)
            }
        }
    }
}

# clean up temp files for invoke requests
Remove-Item -path .\InvokeRequests\ -recurse