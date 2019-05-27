$org = 'https://dev.azure.com/ishitamehta'
$listProjects = az devops project list --org $org -o json | ConvertFrom-Json
foreach($proj in $listProjects){
    if ($proj.name -match '0905'){
        $deleteProject = az devops project delete --id $proj.id --org $org -y -o json
        Write-Host "$deleteProject"
    }
}
