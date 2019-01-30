#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$org,
    [String]$project,
    [Int]$daysToLookBack
)

$continueFetching = $true

$skip = 0
$lookBackDate = (Get-Date).AddDays(-1 * $daysToLookBack)
Write-Host "we will look back till $($lookBackDate)"

$bypassedCount = 0
$nonByPassedCount = 0

while($continueFetching)
{ 
    $prs = az repos pr list --org $org -p $project --skip $skip --top 100 --status completed -o json | ConvertFrom-Json
    $skip = $skip + 100
    foreach($pr in $prs)
    {
        $prClosedDateInString = $pr | Select-Object -ExpandProperty closedDate
        Write-Host -NoNewline "."
        $prClosedData = [datetime]::ParseExact($prClosedDateInString.SubString(0,10),'yyyy-mm-dd', $null)
        $prId = $pr | Select-Object -ExpandProperty pullRequestId        

        $bypassed = $false

        $evaluationResults = az repos pr policies list --org $org --id $prId -o json| ConvertFrom-Json

        foreach($evaluationResult in $evaluationResults)
        {
            $completedDate = $evaluationResult.completedDate
            if($completedDate -eq $null)
            {
                $isBlockingText = $evaluationResult.configuration | Select-Object -ExpandProperty isBlocking
                $isBlocking = [System.Convert]::ToBoolean($isBlockingText) 

                if($isBlocking)
                {
                    $bypassed = $true
                }
            }
        }

        if($bypassed)
        {
            Write-Host "."
            Write-Host "Bypassed PR is $($prId)"
            $bypassedCount = $bypassedCount + 1
        }
        Else
        {
            $nonByPassedCount = $nonByPassedCount + 1
        }

        if($prClosedData -lt $lookBackDate)
        {
            $continueFetching = $false
        }
    }

    if($prs.Length -lt 100)
    {
        $continueFetching = $false
    }
}

Write-Host "."
Write-Host "ByPassed PR count $($bypassedCount)"
Write-Host "Non ByPassed PR count $($nonByPassedCount)"