$ErrorActionPreference = "Stop"

$build_confirmation = Read-Host "Do you want to build/rebuild the packages? [Yes/No]"
if($build_confirmation -like "yes"){
    Write-Host "Creating wheels"
    python create_wheels.py
    Write-Host "done creating wheels"

    Write-Host "creating sdist"
    python sdist.py
    Write-Host "done creating sdist"
}

$install_confirmation = Read-Host "Do you want to upload the packages to PyPi? [Yes/No]"
if($install_confirmation -like "yes"){
    Write-Host "Upgrade pip"
    python -m pip install --upgrade pip
    Write-Host "done - Upgrade pip"
    
    Write-Host "Install twine"
    python -m pip install --user --upgrade twine    
    Write-Host "done - install twine"

    Write-Host "Publishing will start now - Your credentials can be read from Environment Variables (TWINE_USERNAME, TWINE_PASSWORD) or through user input."

    $pypi_username = $env:TWINE_USERNAME
    $pypi_password = $env:TWINE_PASSWORD

    if ($pypi_username -like ''){
        $pypi_username = Read-Host "Enter your PyPi username"
    }

    Write-Host "Using Pypi username:"  $pypi_username

    if ($pypi_password -like ''){
        $pypi_password = Read-Host "Enter your PyPi password" #-AsSecureString #There is some issue in auth when using the secure string password so disabling for now. 
    }
    
    $scriptPath = Get-Location
    $parentPath = Split-Path -parent $scriptPath
    $srcDirectory = Join-Path -Path $parentPath -ChildPath "src"
    $setupFiles = Get-ChildItem -path $srcDirectory -Recurse -Depth 2 -file -filter setup.py

    foreach($setupFile in $setupFiles){
        Write-Host "Publishing package for " $setupFile.Directory.Name
        $setup_location = $setupFile.Directory
        Set-Location $setup_location
        python -m twine upload dist/* -u $pypi_username -p $pypi_password
    }
}
else {
    Write-Host "Exit without publish."
}

