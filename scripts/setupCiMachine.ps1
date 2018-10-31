Write-Output "upgrading pip"
python -m pip install --upgrade pip
Write-Output "done"
Write-Output "installing wheel"
pip install wheel
Write-Output "done"
Write-Output "installing pytest"
pip install pytest
Write-Output "done"

pip install keyring
pip install keyrings.alt

# Install CLI & CLI testsdk
Write-Output "Installing azure-cli-testsdk and azure-cli..."

# Update the git commit or branch when we need a new version of azure-cli-testsdk
pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge
pip install "git+https://github.com/Azure/azure-cli@master#egg=azure-cli-testsdk&subdirectory=src/azure-cli-testsdk" -q

Write-Output "Installed."
az --h

try{
    $logoutCommand = "az devops logout **2>&1 | Write-Host**"
    Invoke-Expression $logoutCommand
    Write-Host "logout done"
}
catch{
    Write-Host "no credentials were stored"
}