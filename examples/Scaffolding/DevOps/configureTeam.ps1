. (Join-Path $PSScriptRoot ..\Utils\permissionsHelper.ps1)
function addTeamAdmins{
    param (
        [String]$adminGrpDescriptor,
        [String]$org,
        [String]$projectID,
        [String]$teamID
    )
    
    $securityToken = $projectID + '\' + $teamID
    
    #display current permissions
    $showIdentityPermissions = az devops security permission show --org $org --id 5a27515b-ccd7-42c9-84f1-54c998f03866 --token $securityToken --subject $adminGrpDescriptor -o json | ConvertFrom-Json
    Write-Host "Current permissions for this group"
    displayPermissions -permissionsResponse $showIdentityPermissions

    #update permissions to manage : Adding team admins is equivalent to giving them manage permissions (i.e bit 31)
    $updateIdentityPermissions = az devops security permission update --allow-bit 31 --org $org --id 5a27515b-ccd7-42c9-84f1-54c998f03866 --token $securityToken --subject $adminGrpDescriptor -o json | ConvertFrom-Json
    Write-Host "`nGiving admins permissions to the requested group. Updated permissions:"

    $showIdentityPermissions = az devops security permission show --org $org --id 5a27515b-ccd7-42c9-84f1-54c998f03866 --token $securityToken --subject $adminGrpDescriptor -o json | ConvertFrom-Json
    displayPermissions -permissionsResponse $showIdentityPermissions

}

function addTeamMembers {
    param (
        [String[]]$teamMembersList,
        [String]$org,
        [String]$teamDescriptor
    )

    foreach($member in $teamMembersList)
    {
        $addMember = az devops security group membership add --group-id $teamDescriptor --member-id $member --org $org -o json | ConvertFrom-Json 
        Write-Host "Team member $($member) added"
    }
}

function createTeam {
    param (
        [string]$teamName,
        [string]$org,
        [string]$projectID
    )
    Write-Host "`nCreating team with name $($teamName) . . . " 
    $createTeam = az devops team create --name $teamName  --org $org -p $projectID -o json | ConvertFrom-Json
    Write-Host "Created team with name $($createTeam.name) and Id $($createTeam.id)"
    return $createTeam.id
}