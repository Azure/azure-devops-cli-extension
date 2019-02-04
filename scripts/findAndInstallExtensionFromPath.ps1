param([string]$pathToProbe)

Write-host "we will be probing " $pathToProbe
$extensions = Get-ChildItem -Path $pathToProbe -Filter "*.whl" -Recurse | Select-Object FullName
Foreach ($extension in $extensions)
{
    az extension add --source $extension.FullName -y
}
Write-Host "done"