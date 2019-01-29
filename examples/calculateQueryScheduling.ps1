#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$org,
    [String]$project,
    [String]$queryId
)

if([string]::IsNullOrEmpty($org))
{
    $org = Read-Host 'What is your organization? (ex: https://contoso.visualstudio.com/)'
}

if([string]::IsNullOrEmpty($project))
{
    $project = Read-Host 'what is your project?'
}

if([string]::IsNullOrEmpty($queryId))
{
    $queryId = Read-Host 'what is the work item query id?'
}

$totalEstimatedTime = 0
$totalWorkDone = 0
$itemsMissed = 0

$workItems = az boards query --id $queryId -p $project --org $org -o json | ConvertFrom-Json

foreach($workItem in $workItems)
{
    try
    {
        $workItemWithDetail = az boards work-item show --id $workItem.id --org $org -o json | ConvertFrom-Json
        $timeRemaining = $workItemWithDetail.fields | Select-Object -ExpandProperty Microsoft.VSTS.Scheduling.OriginalEstimate
        $timeDone = $workItemWithDetail.fields | Select-Object -ExpandProperty Microsoft.VSTS.Scheduling.CompletedWork
        $totalEstimatedTime = $totalEstimatedTime + $timeRemaining
        $totalWorkDone = $totalWorkDone + $timeDone
    }
    catch
    {
        $itemsMissed = $itemsMissed + 1
    }
}

Write-Host "Total Work Time Estimated as part of this $($totalEstimatedTime)"
$totalWorkDonePercentage = [math]::Round(($totalWorkDone / $totalEstimatedTime) * 100.0,1)
Write-Host "Total Work Time Done for items in this query $($totalWorkDone) $($totalWorkDonePercentage)%"
if($itemsMissed -gt 0)
{
    Write-Host "$($itemsMissed) does not have sufficient information"
}