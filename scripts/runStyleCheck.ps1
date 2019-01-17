scripts/setupCiMachine.ps1

Write-Output "Installing azure devops python sdk"
pip install vsts                     

Write-Output "Installing pylint"
pip install pylint<2

Write-Output "Installing flake8"
pip install flake8

Write-Output "Running pylint on all source"
pylint --rcfile pylintrc ./azure-devops/azext_devops -f colorized
Write-Output "Pylint OK!"

Write-Output "Running flake8 checks"
flake8 --config .flake8
Write-Output "Flake8 OK!"

