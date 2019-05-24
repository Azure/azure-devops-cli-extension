. (Join-Path $PSScriptRoot ..\Utils\permissionsHelper.ps1)

function get_token{
    param(
        [String]$iterationsNodeID,
        [String]$rootIterationID,
        [String]$childIterationID
    )
    $rootStr = 'vstfs:///Classification/Node/'
    $tokenStr = ''
    if($iterationsNodeID)
    {
        $tokenStr = $rootStr + $iterationsNodeID
        if($rootIterationID)
        {
            $tokenStr = $tokenStr + ':' + $rootStr + $rootIterationID
            if($childIterationID)
            {
                $tokenStr = $tokenStr + ':' + $rootStr + $childIterationID
            }
            return $tokenStr
        }
    }
    else {
        return $null
    }
}

function setPermissions{
    param(
        [String]$org,
        [String]$subject,
        [String]$tokenStr,
        [Int]$allowBit,
        [Int]$denyBit
    )
    # boards iterations namespace id
    $namespaceId = 'bf7bfa03-b2b7-47db-8113-fa2e002cc5b1'
    
    $aclList = az devops security permission list --org $org --subject $subject --id $namespaceId -o json | ConvertFrom-Json
    foreach($acl in $aclList){
        if ($($acl.token) -contains $tokenStr)
        {
            # Show permissions
            $displayPermissions = az devops security permission show --org $org --id $namespaceId --subject $subject --token $tokenStr -o json | ConvertFrom-Json
            Write-Host "`nCurrent iterations related permissions for admin group :"
            displayPermissions -permissionsResponse $displayPermissions

            # Update permissions
            if($allowBit)
            {
                $updatePermissions = az devops security permission update --org $org --id $namespaceId --subject $subject --token $tokenStr --allow-bit $allowBit -o json | ConvertFrom-Json    
            }

            if($denyBit)
            {
                $updatePermissions = az devops security permission update --org $org --id $namespaceId --subject $subject --token $tokenStr --deny-bit $denyBit -o json | ConvertFrom-Json    
            }
            
            $displayPermissions = az devops security permission show --org $org --id $namespaceId --subject $subject --token $tokenStr -o json | ConvertFrom-Json
            Write-Host "Updated iterations related permissions for admin group :"
            displayPermissions -permissionsResponse $displayPermissions
        }
    }
}

