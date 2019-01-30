#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$org,
    [String]$projectName,
    [String]$repoName,
    [String]$repoToImport
)

if([string]::IsNullOrWhiteSpace($org))
{
    $org = Read-Host 'What is your organization? (ex: https://contoso.visualstudio.com/)'
}

if([string]::IsNullOrWhiteSpace($projectName))
{
    $projectName = Read-Host 'Please enter name of project to be used for bugbash'
}

$project = az devops project create --org $org --name $projectName -o json | ConvertFrom-Json
Write-Host "Created new project with Id $($project.id)" 

if([string]::IsNullOrWhiteSpace($repoName))
{
    $repoName = Read-Host "Please enter name of repo to be used for bugbash"
}

$repo = az repos create --org $org -p $project.id --name $repoName -o json | ConvertFrom-Json
Write-Host "Create repo with Id $($repo.id)"


if([string]::IsNullOrWhiteSpace($repoToImport))
{
    $repoToImport = Read-Host "Please give source of repo to import"
}

az repos import create --org $org -p $project.id -r $repo.id --git-url $repoToImport 
