#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$org,
    [String]$bugbashProjectName,
    [String]$bugbashRepoName,
    [String]$repoToImport
)

if([string]::IsNullOrWhiteSpace($org))
{
    $org = Read-Host 'What is your organization? (ex: https://contoso.visualstudio.com/)'
}

if([string]::IsNullOrWhiteSpace($bugbashProjectName))
{
    $bugbashProjectName = Read-Host 'Please enter name of project to be used for bugbash'
}

$bugbashProject = az devops project create --org $org --name $bugbashProjectName -o json | ConvertFrom-Json
Write-Host "Created new project with Id $($bugbashProject.id)" 

if([string]::IsNullOrWhiteSpace($bugbashProjectName))
{
    $bugbashRepoName = Read-Host "Please enter name of repo to be used for bugbash"
}

$bugbashRepo = az repos create --org $org -p $bugbashProject.id --name $bugbashRepoName -o json | ConvertFrom-Json
Write-Host "Create repo with Id $($bugbashRepo.id)"


if([string]::IsNullOrWhiteSpace($repoToImport))
{
    $repoToImport = Read-Host "Please give source of repo to import"
}

az repos import create --org $org -p $bugbashProject.id -r $bugbashRepo.id --git-url $repoToImport 
