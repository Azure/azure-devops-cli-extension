param([Boolean]$outputTestResultAsJunit=$false)

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

$testFailureFound = $false

if($outputTestResultAsJunit -eq $true)
{
    pytest 'azure-devops/' --junitxml "TEST-UT-results.xml" --cov=azext_devops --cov-report=xml --cov-report=html
}
else{
    pytest 'azure-devops/'
}

if ($LastExitCode -ne 0) {
    $testFailureFound = $true
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

if($testFailureFound -eq $true){
    exit 1
}