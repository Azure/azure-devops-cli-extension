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
Write-Output "installing keyring"
pip install keyring
Write-Output "done"
# only needed for running tests in environment with python version less that 3.3
Write-Output "installing mock"
pip install mock
Write-Output "done"

Write-Output "Install azure-cli-testsdk"
pip install "git+https://github.com/Azure/azure-cli@master#egg=azure-cli-testsdk&subdirectory=src/azure-cli-testsdk" -q
Write-Output "done"

az --h --debug

try{
    $logoutCommand = "az devops logout **2>&1 | Write-Host**"
    Invoke-Expression $logoutCommand
    Write-Host "logout done"
}
catch{
    Write-Host "no credentials were stored"
}