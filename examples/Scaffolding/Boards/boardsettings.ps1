. "$PSScriptRoot\permissions.ps1"
$invokeRequestsPath = Join-Path $PSScriptRoot ..\InvokeRequests\
$apiVersion = '5.0'
function setUpGeneralBoardSettings {
    param(
        [String]$org,
        [String]$projectID,
        [String]$teamID,
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

    if ($epics -or $stories -or $features) {
        [void]$contentToStoreInFile.Append(  "`"backlogVisibilities`" : { " )
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
    $listAreasForTeam = az boards area team add --path $defaultAreaPath --set-as-default --team $teamID --org $org --project $projectName -o json | ConvertFrom-Json
    Write-Host "Default area changed to: $defaultAreaPath"
}

function createTeamArea {
    param(
        [String]$org,
        [String]$projectID,
        [String]$areaName
    )
    
    $createAreasForTeam = az boards area project create --name $areaName --org $org --project $projectID -o json | ConvertFrom-Json
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

    $projectRootIterationList = az boards iteration project list --org $org --project $projectID -o json | ConvertFrom-Json
    $iterationsNodeID = $projectRootIterationList.identifier
    
    $projectRootIterationCreate = az boards iteration project create --name $rootIterationName --org $org --project $projectID -o json | ConvertFrom-Json
    if ($projectRootIterationCreate) {
        Write-Host "`nRoot Iteration created with name: $($projectRootIterationCreate.name)"
        foreach ($entry in $childIterationNamesList) {
            $childIterationName = $rootIterationName + ' ' + $entry.ToString()
            #$projectRootIterationCreate
            $projectChildIterationCreate = az boards iteration project create --name $childIterationName --path $projectRootIterationCreate.path --org $org --project $projectID -o json | ConvertFrom-Json
            Write-Host "Child Iteration created with name: $($projectChildIterationCreate.name)"
        }

        # Add permissions at root iterations
        $rootIterationToken = get_token -iterationsNodeID $iterationsNodeID -rootIterationID  $($projectRootIterationCreate.identifier)
        $updatePermissions = setPermissions -org $org -tokenStr $rootIterationToken -subject $subject -allowBit $allow -denyBit $deny
    }
    return $projectRootIterationCreate.identifier
}


function setUpTeamIterations {
    param(
        [String]$org,
        [String]$projectName,
        [String]$teamID
    )

    # show backlog iteration command
    $backlogIterationDetails = az boards iteration team show-backlog-iteration --team $teamID --org $org --project $projectName -o json| ConvertFrom-Json
    
    $depthParam = '1'
    $backlogIterationPath = $backlogIterationDetails.backlogIteration.path
    Write-Host "`nTeam Iterations Configuration"
    # Format iteration path to include project name and structure type
    $backlogIterationPath = '\' + $projectName + '\Iteration\' + $backlogIterationPath 
    $rootIteration = az boards iteration project list --path $backlogIterationPath --project $projectName --org $org --depth $depthParam -o json | ConvertFrom-Json
    if ($rootIteration.hasChildren -eq $True) {
        foreach ($child in $rootIteration.children) {
            $getProjectTeamIterationID = $child.identifier
            # add this child iteration to the given team
            $addTeamIteration = az boards iteration team add --team $teamID --id $getProjectTeamIterationID  --project $projectName --org $org -o json | ConvertFrom-Json
            Write-Host "Team iteration added with ID : $($addTeamIteration.id) and name:$($child.name)"
        }
    }
    
}