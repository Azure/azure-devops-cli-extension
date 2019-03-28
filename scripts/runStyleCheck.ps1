$failure = $false             

Write-Output "Installing pylint"
pip install pylint<2

Write-Output "Installing flake8"
pip install flake8

Write-Output "Running pylint on all source"
pylint --rcfile pylintrc ./azure-devops/azext_devops -f colorized

if ($LastExitCode -ne 0) {
    $failure = $true
    Write-Output "Pylint NOT OK!"
  } else {
    Write-Output "Pylint OK!"
  }

Write-Output "Running flake8 checks"
flake8 --config .flake8

if ($LastExitCode -ne 0) {
    $failure = $true
    Write-Output "flake8 NOT OK!"
  } else {
    Write-Output "flake8 OK!"
  }

if($failure -eq $true){
    exit 1
}