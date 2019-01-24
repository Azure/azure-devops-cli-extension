param([string]$pathToProbe)

Write-host "we will be probing " $pathToProbe
Write-Host "installing azure dev cli extension"
$extensions = Get-ChildItem -Path $pathToProbe -Filter "*.whl" -Recurse | Select-Object FullName
az extension add --source $extensions[0].FullName -y
Write-Host "done"