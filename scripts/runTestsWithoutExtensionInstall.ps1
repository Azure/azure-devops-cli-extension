$rootPath = Get-Location
$testFiles = @()
$testDirectory = Join-Path -Path $rootPath -ChildPath "tests"
$testFiles = Get-ChildItem -path $testDirectory -Recurse -Depth 0 -file -filter *Test.py | Select -ExpandProperty FullName

foreach($testFile in $testFiles){
    
   $leafFile = Split-Path $testFile -leaf
   $testResultFile = "TEST-" + $leafFile + ".xml"
    Write-Host "test result output at " $testResultFile
    pytest $testFile --junitxml $testResultFile
    
    if ($LastExitCode -ne 0) {
        $testFailureFound = $true
      }
}

if($testFailureFound -eq $true){
    exit 1
}