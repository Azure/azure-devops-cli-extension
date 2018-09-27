$rootPath = Get-Location
$extensionDirectory = Join-Path -Path $rootPath -ChildPath "azure-dev-cli-extensions"

Set-Location $extensionDirectory
Write-Host "installing azure dev cli extension"
pip install --upgrade .
Write-Host "done"
Write-Host "creating wheel"
python setup.py bdist_wheel
Write-Host "done"
Set-Location $rootPath

$ErrorActionPreference = "Continue"
try {
    $uninstallCommand = "az extension remove -n azure-cli-dev **2>&1 | Write-Host**"
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

az dev -h

$testDirectory = Join-Path -Path $rootPath -ChildPath "tests"

$basicPrTests = Join-Path -Path $testDirectory -ChildPath "basicPrTest.py"
pytest $basicPrTests