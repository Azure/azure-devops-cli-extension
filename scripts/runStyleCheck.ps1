scripts/setupCiMachine.ps1

$failure = $false

Write-Output "Installing azure devops python sdk"
pip install vsts                     

Write-Output "Installing pylint"
pip install pylint<2

Write-Output "Installing flake8"
pip install flake8

Write-Output "Running pylint on all source"
pylint --rcfile pylintrc ./azure-devops/azext_devops -f colorized

if ($LastExitCode -ne 0) {
    $failure = $true
  }

Write-Output "Pylint OK!"

Write-Output "Running flake8 checks"
flake8 --config .flake8

if ($LastExitCode -ne 0) {
    $failure = $true
  }

Write-Output "Flake8 OK!"

if($failure -eq $true){
    exit 1
}