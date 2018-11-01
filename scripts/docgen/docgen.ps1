$DocGenBase = $PSScriptRoot
$DocGenOutput = "$DocGenBase\_output"
$DocGenTools = "$DocGenBase\_tools"
$CliSourceRepoUrl = "https://github.com/Microsoft/azdos-cli"
$CliSourceRepoBranch = "master"
$RepoRoot = "$DocGenBase\..\.."

function Write-CommitMap {
    $docSourceRaw = Get-Content -Raw -Path "$DocGenBase\doc_source_map.json" | ConvertFrom-Json

    $docFiles = $docSourceRaw | Get-Member -type NoteProperty | %{ $docSourceRaw."$($_.Name)" }
    $docFiles = $docFiles | select -Unique
    $fileCommitMap = @{}

    Push-Location -Path $RepoRoot

    foreach($file in $docFiles)
    {
        $commitId = (git rev-list -1 HEAD $file)
        if($commitId -match '^[0-9a-f]{40}$')
        {
            $date = Get-Date -Date (git log --pretty=format:%cd -n 1 --date=iso $file)
            $date = $date.ToUniversalTime()
            $date = Get-Date $date -format G
            $fileCommitMap[$file] = @{}
            $fileCommitMap[$file]["commit"] = $commitId
            $fileCommitMap[$file]["date"] = $date
        }
        else
        {
            Write-Host -ForegroundColor Red "Failed to get commit id for $file"
            $host.SetShouldExit(-1)
        }
    }

    Pop-Location

    $fileCommitMap | ConvertTo-Json | Out-File "$DocGenOutput\doc_commit_map.json"

    
}

# Run Sphinx to generate XML for VSTS CLI commands
function Invoke-PyToXml {   
    Push-Location $DocGenBase
    Invoke-Expression "python -m sphinx.__init__ -E -b xml -d $DocGenOutput/doctrees . $DocGenOutput/xml/latest"
    Pop-Location
}

# Run XML to YAML conversion
function Invoke-XmlToYml {
    if(!(test-path $DocGenTools))
    {
        New-Item -ItemType Directory -Force -Path $DocGenTools
    }

    $DocGenToolsZipFile = "$DocGenTools/azure.cli.doc.xml2yml.zip"
    Invoke-WebRequest -Uri "https://ci.appveyor.com/nuget/azure-docs-cli-pre-process/api/v2/package/azure.cli.doc.xml2yml/1.0.1" -OutFile $DocGenToolsZipFile
    Expand-Archive -Path $DocGenToolsZipFile -DestinationPath "$DocGenTools/azure.cli.doc.xml2yml" -Force

    Push-Location -Path "$DocGenTools/azure.cli.doc.xml2yml/tools"
    #Install-Package -Name azure.cli.doc.xml2yml -Source https://ci.appveyor.com/nuget/azure-docs-cli-pre-process -
    Invoke-Expression ".\AzCliDocPreprocessor.exe -s $DocGenOutput\xml\latest -d $DocGenOutput\yml\latest -r $CliSourceRepoUrl -b $CliSourceRepoBranch -c $DocGenOutput\doc_commit_map.json -g ""azdos"" -v 1"
    Pop-Location
}

# Install docgen Python dependences
function Install-PreReqs {
    python -m pip install sphinx==1.5.6
}

function Main {
    # Create output directory
    if(!(test-path $DocGenOutput))
    {
        New-Item -ItemType Directory -Force -Path $DocGenOutput
    }

    # Run tasks
    Install-PreReqs
    Write-CommitMap
    Invoke-PyToXml
    Invoke-XmlToYml
}

Main

