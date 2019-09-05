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

$bypassPRsInfo = ''

while($continueFetching)
{ 
    $prs = az repos pr list --org $org -p $project --skip $skip --top 100 --status completed -o json | ConvertFrom-Json
    $skip = $skip + 100
    foreach($pr in $prs)
    {
        $prClosedDateInString = $pr | Select-Object -ExpandProperty closedDate
        Write-Host -NoNewline "."
        $prClosedData = [datetime]::ParseExact($prClosedDateInString.SubString(0,10),'yyyy-MM-dd', $null)
        $prId = $pr | Select-Object -ExpandProperty pullRequestId        

        $prDetails = az repos pr show --org $org --id $prId -o json | ConvertFrom-Json

        if($prDetails.completionOptions.bypassPolicy)
        {
            $bypassPRsInfo = $bypassPRsInfo + "$($prId) is bypassed.
            Bypass reason : $($prDetails.completionOptions.bypassReason).
            Author : $($prDetails.closedBy.uniqueName).
            Closed Date: $($prClosedDateInString). `n"
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
Write-Host "ByPassed PR details"
Write-Host $bypassPRsInfo
