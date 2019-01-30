# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [Boolean]$outputTestResultAsJunit=$false,
    [Boolean]$run_UT=$true,
    [Boolean]$run_VCR=$true,
    [string]$pat
)

$rootPath = Get-Location
$extensionDirectory = Join-Path -Path $rootPath -ChildPath "azure-devops"

Set-Location $extensionDirectory
Write-Host "installing azure dev cli extension"
pip install --upgrade .
Write-Host "done"
Write-Host "creating wheel"
python setup.py sdist bdist_wheel
Write-Host "done"
Set-Location $rootPath

# only needed for running tests in environment with python version less that 3.3
pip install mock

$ErrorActionPreference = "Continue"
try {
    Write-Host "trying to uninstall extension of az devops extension was installed"
    $uninstallCommand = "az extension remove -n azure-devops **2>&1 | Write-Host**"
    Invoke-Expression $uninstallCommand
    Write-Host "extension was installed and it was removed"
}
catch {
    Write-Host "extension was not installed"
}

$ErrorActionPreference = "Stop"

Write-Host "installing azure dev cli extension"
$extensions = Get-ChildItem -Path $sourceDir -Filter "*.whl" -Recurse | Select-Object FullName
az extension add --source $extensions[0].FullName -y
Write-Host "done"

# Install this extension just so that we can compare the load time
az extension add -n azure-cli-iot-ext

az --version
az -h
az devops -h --debug

$testFailureFound = $false

if($run_UT -eq $true)
{
    if($outputTestResultAsJunit -eq $true) {
        pytest 'azure-devops/' --junitxml "TEST-UT-results.xml" --cov=azext_devops --cov-report=xml --cov-report=html
    }
    else {
        pytest 'azure-devops/'
    }

    if ($LastExitCode -ne 0) {
       $testFailureFound = $true
    }
}

if($run_VCR -eq $true) {
    $env_pat_token_name = "AZURE_DEVOPS_EXT_PAT"
    if (Test-Path env:$env_pat_token_name) { 
        $env_pat_token = (get-item env:$env_pat_token_name).Value
        if($env_pat_token) {
            Write-Host('Trying devops login with token in environment.')
            Write-Host("echo '" + $env_pat_token + "' | az devops login --org https://dev.azure.com/azuredevopsclitest")
            Invoke-Expression("echo '" + $env_pat_token + "' | az devops login --org https://dev.azure.com/azuredevopsclitest")
            Write-Host ($env_pat_token)
        }
        if($pat) {
            Write-Host('Trying devops login with token in environment.')
            Write-Host("echo '" + $pat + "' | az devops login --org https://dev.azure.com/azuredevopsclitest")
            Invoke-Expression("echo '" + $pat + "' | az devops login --org https://dev.azure.com/azuredevopsclitest")
            Write-Host ($pat)
        }
    }

    if($outputTestResultAsJunit -eq $true)
    {
        pytest 'tests/' --junitxml "TEST-recordings-results.xml" --cov=azext_devops --cov-report=xml --cov-report=html
    }
    else{
        pytest 'tests/'
    }

    if ($LastExitCode -ne 0) {
        $testFailureFound = $true
    }
}

if($testFailureFound -eq $true){
    exit 1
}