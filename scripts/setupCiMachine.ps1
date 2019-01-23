Write-Output "installing wheel"
pip install wheel
Write-Output "done"
Write-Output "installing pytest"
pip install pytest
Write-Output "done"
Write-Output "installing coverage"
pip install coverage
Write-Output "done"
Write-Output "installing pytest-cov"
pip install pytest-cov
Write-Output "done"
Write-Output "installing keyring"
pip install keyring
Write-Output "done"

# Install CLI & CLI testsdk
Write-Output "installing azure-cli-testsdk and azure-cli..."
pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge
# Update the git commit or branch when we need a new version of azure-cli-testsdk
pip install "git+https://github.com/Azure/azure-cli@master#egg=azure-cli-testsdk&subdirectory=src/azure-cli-testsdk" -q
Write-Output "done"

az --h

try{
    $logoutCommand = "az devops logout **2>&1 | Write-Host**"
    Invoke-Expression $logoutCommand
    Write-Host "logout done"
}
catch{
    Write-Host "no credentials were stored"
}