function createProject{
    param(
        [String]$org,
        [String]$projectName,
        [String]$process
    )

    
    Write-Host "`nCreating project with name $($projectName) . . . " 
    $project = az devops project create --org $org --name $projectName --process $process -o json | ConvertFrom-Json
    Write-Host "Created project with name $($project.name) and Id $($project.id)"
    return $project.id
}

function createRepo{
    param(
        [String]$org,
        [String]$projectID,
        [String]$repoName
    )

    Write-Host "`nCreating repository with name $($repoName) . . . " 
    $repo = az repos create --org $org -p $projectID --name $repoName -o json | ConvertFrom-Json
    Write-Host "Created repository with name $($repo.name) and Id $($repo.id)"
    return $repo.id
}

function importRepo{
    param(
        [String]$org,
        [String]$projectID,
        [String]$repoID,
        [String]$repoToImport,
        [String]$repoType
    )
    if($repoToImport -and ($repoType -eq 'Public')){
        Write-Host "`nImporting repository from url $($repoToImport)" 
        $importRepo = az repos import create --org $org -p $projectID -r $repoID --git-url $repoToImport -o json | ConvertFrom-Json
        Write-Host "Repo imported with Status $($importRepo.status)"
    }
    else {
        Write-Host "Private repo import wiki command goes here!"
    }
}

function publishCodeWiki{
    param(
        [String]$org,
        [String]$projectID,
        [String]$repo,
        [String]$wikiName,
        [String]$path,
        [String]$wikiType,
        [String]$branch
    )
    if ($wikiType -eq 'codewiki' -and $path -and $branch){
        $createCodeWiki = az devops wiki create --name $wikiName --type codewiki --version $branch --mapped-path $path -r $repo --org $org -p $projectID -o json | ConvertFrom-Json
        Write-Host "New code wiki published with ID : $($createCodeWiki.id)"
    }
    else {
        Write-Host "Project wiki creation command goes here!"
    }
    
}
