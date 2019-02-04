Write-Output "upgrading pip"
python -m pip install --upgrade pip
Write-Output "done"
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

# Install CLI & CLI testsdk
Write-Output "installing azure-cli-testsdk and azure-cli..."
pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge
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