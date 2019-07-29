
param(
    [String]$filePath
)
. (Join-Path $PSScriptRoot .\Boards\boardsettings.ps1)
. (Join-Path $PSScriptRoot .\Repos\setPolicies.ps1)
. (Join-Path $PSScriptRoot .\DevOps\projectSetUp.ps1)
. (Join-Path $PSScriptRoot .\DevOps\configureTeam.ps1)


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
    $requiredReviewers = if ($values.requiredReviewers) { $values.requiredReviewers.split(",") }
    $optionalReviewers = if ($values.optionalReviewers) { $values.optionalReviewers.split(",") }
    $teamMembers = if ($values.teamMembers) { $values.teamMembers.split(",") }
    $teamAdminMembers = if ($values.teamAdminMembers) { $values.teamAdminMembers.split(",") }
    $childIterationNamesList = if ($values.childIterationNamesList) { $values.childIterationNamesList.split(",") }
    $iterationsPermissionsBit = $values.iterationsPermissionsBit

    Write-Host("`nAll the required parameters are read from file at $($filePath)  Now just sit back and relax, script is in action now . . . ")
}

$invokeRequestsPath = . Join-Path $PSScriptRoot InvokeRequests\
If (!(test-path $invokeRequestsPath)) {
    New-Item -ItemType Directory -Force -Path $invokeRequestsPath
}

# scaffolding
$projectID = createProject -org $org -projectName $projectName -process 'Agile' -sourceControl 'git' -visibility 'private'

if ($repoName) {

    $repoID = createRepo  -repoName $repoName -org $org -projectID $projectID
    if ($repoToImport) {
        importRepo -repoID $repoID -repoToImport $repoToImport -repoType 'Public' -org $org -projectID $projectID
        if ($requiredReviewers -or $optionalReviewers) {
            $policiesSet = set_policies -org $org -projectName $projectID -repoId $repoID -branch 'master' -requiredApprovers $requiredReviewers -optionalApprovers $optionalReviewers
            Write-Host "`nBranch policies set for master"
        }
    }
}
else {
    Write-Host "`nSkipping repo creation as repo name is empty"
}

# team set up
if ($teamName) {
    $teamID = createTeam -org $org -teamName $teamName -projectID $projectID
    if ($teamMembers) {
        $listGroups = az devops security group list --org $org -p $projectID -o json | ConvertFrom-Json
        foreach ($grp in $listGroups.graphGroups) {
            if ($grp.displayName -eq $teamName) {
                # Add team members
                addTeamMembers -org $org -teamMembersList $teamMembers -teamDescriptor $grp.descriptor
                # create a team admin group and add it to this team
                $teamAdminGroupName = $teamName + ' Admins'
                $createTeamAdminsGroup = az devops security group create --org $org -p $projectID --name $teamAdminGroupName --groups $grp.descriptor -o json | ConvertFrom-Json 
                Write-Host "`nCreated new admin group with name $($teamAdminGroupName) and added to the newly created team $teamName."

                if ($teamAdminMembers) {
                    addTeamMembers -org $org -teamMembersList $teamAdminMembers -teamDescriptor $createTeamAdminsGroup.descriptor
                }
                # add this newly created Admin group as Team Administrators
                addTeamAdmins -org $org -projectID $projectID -teamID $teamID -adminGrpDescriptor $createTeamAdminsGroup.descriptor

                #create Area for this team
                createTeamArea -org $org -projectID $projectID -areaName $teamName

                # area path
                $areaPath = $projectName + '\' + $teamName
                configureDefaultArea -org $org -projectID $projectID -teamID $teamID -defaultAreaPath $areaPath
                
                # Configure project level iterations with this group/team and grant permissions for admins group
                $projectIterationNameForThisTeam = $teamName + ' iteration' 
                $rootIterationId = projectLevelIterationsSettings -org $org -projectID $projectID -rootIterationName $projectIterationNameForThisTeam -subject $createTeamAdminsGroup.descriptor -allow $iterationsPermissionsBit -childIterationNamesList $childIterationNamesList
            
                if ($rootIterationId)
                {
                    #set backlog iteration ID
                    $setBacklogIteration = az boards iteration team set-backlog-iteration --id $rootIterationId --team $teamID --org $org -p $projectID -o json | ConvertFrom-Json 
                    Write-Host "`nSetting backlog iteration to : $($setBacklogIteration.backlogIteration.path)"
                    # Boards General settings
                    setUpGeneralBoardSettings -org $org -projectID $projectID -teamID $teamID -epics $true -stories $true -features $true 
                    
                    # Add child iterations of backlog iteration to the given team
                    setUpTeamIterations -org $org -projectName $projectName -teamID $teamID
                }
            }
        }
    }
}

# clean up temp files for invoke requests
Remove-Item -path .\InvokeRequests\ -recurse