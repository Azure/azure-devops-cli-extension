param([string]$pathToProbe)

Write-host "we will be probing " $pathToProbe
$extensions = Get-ChildItem -Path $pathToProbe -Filter "*.whl" -Recurse | Select-Object FullName
Foreach ($extension in $extensions)
{
    pip install $extension.FullName
}
Write-Host "done"