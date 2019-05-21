#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$organization,
    [String]$project,
    [String]$username,
    [int]$notReviewedInLastNDays
)

$prlist = az repos pr list --reviewer $username --org $organization -p $project -o json | ConvertFrom-Json
$prReminderList = @()
$lastNDays = -1 * $notReviewedInLastNDays

foreach ($pr in $prlist) {
    $repositoryId = $pr.repository.id
    $pullrequestId = $pr.pullRequestId
    $nDaysBefore = (Get-Date).ToUniversalTime().AddDays($lastNDays)
    $lastUpdatedDate = $nDaysBefore
    $threads = az devops invoke --area git --resource pullRequestThreads --org $organization --route-parameters repositoryId=$repositoryId pullRequestId=$pullrequestId --http-method GET --api-version 5.1-preview -o json | ConvertFrom-Json

    foreach($thread in $threads.value) {
        $comments = $thread.comments

        foreach($comment in $comments) {
            $commentDate = ([datetime]$comment.lastUpdatedDate).ToUniversalTime()
            if($comment.author.uniqueName -eq $username -and $commentDate -gt $lastUpdatedDate) {
                $lastUpdatedDate = $commentDate
            }
        }
    }

    if($lastUpdatedDate -eq $nDaysBefore) {
        $prReminderList += ($pr)
    }
}

if($prReminderList.Length -eq 0) {
    Write-Host "No pull requests pending to be reviewed at this moment.."
} elseif($prReminderList.Length -gt 0) {
    Write-Host "Pull requests not reviewed/updated in last "$notReviewedInLastNDays" days:"
}

foreach($pr in $prReminderList) {
    Write-Host $pr.pullRequestId $pr.title
}
