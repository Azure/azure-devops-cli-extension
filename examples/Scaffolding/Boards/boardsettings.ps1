. "$PSScriptRoot\permissions.ps1"
$invokeRequestsPath = Join-Path $PSScriptRoot ..\InvokeRequests\
$apiVersion = '5.0'
function setUpGeneralBoardSettings {
    param(
        [String]$org,
        [String]$projectID,
        [String]$teamID,
        [String]$backlogIterationId,
        [Bool]$epics,
        [Bool]$stories,
        [Bool]$features
    )

    # Team boards settings
    $currentBoardsTeamSettings = az devops invoke --org $org --area work --resource teamsettings --api-version $apiVersion --http-method GET --route-parameters project=$projectID team=$teamID  -o json | ConvertFrom-Json
    
    Write-Host "`nCurrent general team configurations"
    "Current backlog navigation levels"
    printBacklogLevels -boardsTeamSettings $currentBoardsTeamSettings

    #update these settings
    $contentFileName = $invokeRequestsPath + 'updateTeamConfig.txt'
    $contentToStoreInFile = [System.Text.StringBuilder]::new()
    [void]$contentToStoreInFile.Append( "{")
    [void]$contentToStoreInFile.Append( "`"backlogIteration`" : " )
    [void]$contentToStoreInFile.Append( ($backlogIterationId.ToString() | ConvertTo-Json) )

    if ($epics -or $stories -or $features) {
        [void]$contentToStoreInFile.Append(  ",`"backlogVisibilities`" : { " )
        if ($epics -eq $True) {
            [void]$contentToStoreInFile.Append(  "`"Microsoft.EpicCategory`" : true " )
        }
        else {
            [void]$contentToStoreInFile.Append(  "`"Microsoft.EpicCategory`" : false " )
        }

        if ($features -eq $True) {
            [void]$contentToStoreInFile.Append(  ",`"Microsoft.FeatureCategory`" : true " )
        }
        else {
            [void]$contentToStoreInFile.Append(  ",`"Microsoft.FeatureCategory`" : false " )
        }
        
        if ($stories -eq $True) {
            [void]$contentToStoreInFile.Append(  ",`"Microsoft.RequirementCategory`" : true " )
        }
        else {
            [void]$contentToStoreInFile.Append(  ",`"Microsoft.RequirementCategory`" : false " )
        }

        [void]$contentToStoreInFile.Append( "}" ) 
    }
    [void]$contentToStoreInFile.Append( "}" )
    Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()
    
    $updatedBoardsTeamSettings = az devops invoke --org $org --area work --resource teamsettings --api-version $apiVersion --http-method PATCH --route-parameters project=$projectID team=$teamID --in-file $contentFileName -o json | ConvertFrom-Json
    "Updated backlog navigation levels"
    printBacklogLevels -boardsTeamSettings $updatedBoardsTeamSettings
}

function configureDefaultArea {
    param(
        [String]$org,
        [String]$projectID,
        [String]$teamID,
        [String]$defaultAreaPath
    )
    $listAreasForTeam = az devops invoke --org $org --area work --resource teamfieldvalues --api-version $apiVersion --http-method GET --route-parameters project=$projectID  team=$teamID -o json | ConvertFrom-Json
    #$defaultTeamArea = $listAreasForTeam.defaultValue

    $contentFileName = $invokeRequestsPath + 'updateDefaultAreaRequest.txt'
    $contentToStoreInFile = [System.Text.StringBuilder]::new()
    [void]$contentToStoreInFile.Append( "{`"defaultValue`" : " )
    [void]$contentToStoreInFile.Append( ($defaultAreaPath.ToString() | ConvertTo-Json) )
    $teamAreaValues = $listAreasForTeam.values
    if ($teamAreaValues) {
        $areaValues = $teamAreaValues | ConvertTo-Json
        [void]$contentToStoreInFile.Append(  ",`"values`" : " )
        [void]$contentToStoreInFile.Append( $areaValues.ToString())
    }
    else {
        [void]$contentToStoreInFile.Append(  ",`"values`" : " )
        [void]$contentToStoreInFile.Append( "[ {`"value`" : " )
        [void]$contentToStoreInFile.Append( ($defaultAreaPath.ToString() | ConvertTo-Json) )
        [void]$contentToStoreInFile.Append(  ",`"includeChildren`" : true" )
        [void]$contentToStoreInFile.Append( " } ]" )
    }
    [void]$contentToStoreInFile.Append( "}" )
    Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()

    $updateDefaultAreaForTeam = az devops invoke --org $org --area work --resource teamfieldvalues --api-version $apiVersion --http-method PATCH --route-parameters project=$projectID  team=$teamID --in-file $contentFileName -o json | ConvertFrom-Json
    Write-Host "Default area is now: $($updateDefaultAreaForTeam.defaultValue)"
}

function createTeamArea {
    param(
        [String]$org,
        [String]$projectID,
        [String]$areaName
    )
    
    $contentFileName = $invokeRequestsPath + 'createTeamAreaRequest.txt'
    $contentToStoreInFile = [System.Text.StringBuilder]::new()
    [void]$contentToStoreInFile.Append( "{`"name`" : " )
    [void]$contentToStoreInFile.Append( ($areaName.ToString() | ConvertTo-Json) )
    [void]$contentToStoreInFile.Append( "}" )
    Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()

    $createAreasForTeam = az devops invoke --org $org --area wit --resource classificationnodes --api-version $apiVersion --http-method POST --route-parameters project=$projectID  --query-parameters structureGroup=Areas --in-file $contentFileName  -o json | ConvertFrom-Json
    #$defaultTeamArea = $createAreasForTeam.defaultValue
    
    Write-Host "`nNew area created : $($createAreasForTeam.name) with id : $($createAreasForTeam.id)"
}

function printBacklogLevels([object]$boardsTeamSettings) {
    if ($boardsTeamSettings) {
        $epics = SelectObject -inputObject $boardsTeamSettings.backlogVisibilities -propertyName Microsoft.EpicCategory
        Write-Host "Epics: $epics"
        
        $features = SelectObject -inputObject $boardsTeamSettings.backlogVisibilities -propertyName Microsoft.FeatureCategory
        Write-Host "Features: $features"
        
        $requirements = SelectObject -inputObject $boardsTeamSettings.backlogVisibilities -propertyName Microsoft.RequirementCategory
        Write-Host "Stories: $requirements"
        
        $days = $boardsTeamSettings.workingDays
        Write-Host "Working days : $days"
    }
}

function SelectObject([object]$inputObject, [string]$propertyName) {
    $objectExists = Get-Member -InputObject $inputObject -Name $propertyName

    if ($objectExists) {
        return $inputObject | Select-Object -ExpandProperty $propertyName
    }
    return $null  
}

function projectLevelIterationsSettings {
    param(
        [String]$org,
        [String]$projectID,
        [String]$rootIterationName,
        [String]$subject,
        [Int]$allow,
        [Int]$deny,
        [String[]]$childIterationNamesList
    )
    # Project level iterations
    $apiVersion = '5.0'
    $depthParam = "`$depth=1"

    $projectRootIterationList = az devops invoke --org $org --api-version $apiVersion --area wit --resource classificationnodes --route-parameters project=$projectID structureGroup=iterations --query-parameters $depthParam -o json | ConvertFrom-Json
    $iterationsNodeID = $projectRootIterationList.identifier
    
    $contentFileName = $invokeRequestsPath + 'createIterationRequest.txt'
    $contentToStoreInFile = [System.Text.StringBuilder]::new()
    [void]$contentToStoreInFile.Append( "{`"name`" : " )
    [void]$contentToStoreInFile.Append( ($rootIterationName.ToString() | ConvertTo-Json) )
    [void]$contentToStoreInFile.Append( "}" )
    Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()

    $projectRootIterationCreate = az devops invoke --org $org --api-version 5.0 --area wit --resource classificationnodes --route-parameters project=$projectID structureGroup=iterations --http-method POST --in-file $contentFileName -o json | ConvertFrom-Json

    if ($projectRootIterationCreate) {
        Write-Host "`nRoot Iteration created with name: $($projectRootIterationCreate.name)"
        foreach ($entry in $childIterationNamesList) {
            $childIterationName = $rootIterationName + ' ' + $entry.ToString()
            $contentToStoreInFile = [System.Text.StringBuilder]::new()
            [void]$contentToStoreInFile.Append( "{`"name`" : " )
            [void]$contentToStoreInFile.Append( ($childIterationName | ConvertTo-Json) )
            [void]$contentToStoreInFile.Append( "}" )
            Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()
            $projectChildIterationCreate = az devops invoke --org $org --api-version 5.0 --area wit --resource classificationnodes --route-parameters project=$projectID structureGroup=iterations --query-parameters path=$rootIterationName  --http-method POST --in-file $contentFileName -o json | ConvertFrom-Json
            Write-Host "Child Iteration created with name: $($projectChildIterationCreate.name)"
        }

        # Add permissions at root iterations
        $rootIterationToken = get_token -iterationsNodeID $iterationsNodeID -rootIterationID  $($projectRootIterationCreate.identifier)
        $updatePermissions = setPermissions -org $org -tokenStr $rootIterationToken -subject $subject -allowBit $allow -denyBit $deny
    }
    $projectRootIterationCreate.identifier
}


function setUpTeamIterations {
    param(
        [String]$org,
        [String]$projectID,
        [String]$teamID,
        [String]$backlogIterationName
    )

    #get iteration id from name
    $getBacklogIteration = az devops invoke --org $org --api-version $apiVersion --area wit --resource classificationnodes --route-parameters project=$projectID structureGroup=iterations --query-parameters  path=$backlogIterationName -o json | ConvertFrom-Json
    $getBacklogIterationID = $getBacklogIteration.id
    
    $depthParam = "`$depth=1"
    $listChildIterations = az devops invoke --org $org --api-version $apiVersion --area wit --resource classificationnodes --route-parameters project=$projectID  --query-parameters ids=$getBacklogIterationID $depthParam -o json | ConvertFrom-Json 
    if ($listChildIterations.count -eq 1) {
        $rootIteration = $listChildIterations.value[0]
        if ($rootIteration.hasChildren -eq $True) {
            foreach ($child in $rootIteration.children) {
                $getProjectTeamIterationID = $child.identifier
                
                # add this child iteration to the given team
                $contentFileName = $invokeRequestsPath + 'setUpTeamIterations.txt'
                $contentToStoreInFile = [System.Text.StringBuilder]::new()
                [void]$contentToStoreInFile.Append( "{")
                [void]$contentToStoreInFile.Append( "`"id`" : " )
                [void]$contentToStoreInFile.Append( ($getProjectTeamIterationID | ConvertTo-Json) )
                [void]$contentToStoreInFile.Append( "}" )
                Set-Content -Path $contentFileName -Value $contentToStoreInFile.ToString()

                $addTeamIteration = az devops invoke --org $org  --area work --resource iterations --api-version $apiVersion --http-method POST --route-parameters project=$projectID team=$teamID --in-file $contentFileName -o json | ConvertFrom-Json
            }
        }
    }
}