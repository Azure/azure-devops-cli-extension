#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
    [String]$organization,
    [String]$assignedTo,
    [int]$daysUntilStale,
    [int]$daysUntilClose
)

. (Join-Path $PSScriptRoot .\Utils\UtilityHelper.ps1)

function MarkWitAsStale {
    param (
        $organization,
        $staleWits,
        $exemptTags,
        $staleTagText,
        $staleCommentText
    )
    $updatedStaleWits = @()
    foreach ($staleWit in $staleWits) {
        # get current tags in staleWit
        [String]$staleWitId = $staleWit.fields | Select-Object -ExpandProperty System.Id
        [String]$staleWitTags = ""

        # check to verify if System.Tags is present in the staleWit.fields
        if ([bool]($staleWit.fields.PSobject.Properties.name -match "System.Tags")) {
            [String]$staleWitTags = $staleWit.fields | Select-Object -ExpandProperty System.Tags
            $staleWitTags += "; "
        }

        # We do not update a staleWit if it contains any of the exempted tags
        $exemptTagFlag = $false;
        foreach ($exemptTag in $exemptTags) {
            if ($staleWitTags -like "*$($exemptTag)*") {
                $exemptTagFlag = $true
                break;
            }
        }

        if ($exemptTagFlag) {
            continue;
        }

        # Add staleTagText if staleWitTags doesn't already contain the staleTag
        if (-Not ($staleWitTags -like "*$($staleTagText)*" )) {
            $staleWitTags += "$($staleTagText)"
            # update WIT with new tags and comment
            $ignoreOutput = az boards work-item update --id $staleWitId --fields -f System.Tags=$staleWitTags --discussion $staleCommentText --org $organization
            $updatedStaleWits += $staleWit
        }
    }

    return $updatedStaleWits
}

### main start
 
## configuration settings
$exemptTags = @('security', 'pinned')
$staleTagText = "ProAct : stale"
$staleCommentText = "This work item has been automatically marked as stale (tag => $staleTagText) because there has been no activity in last $daysUntilStale days. This work item will be closed if tag => $staleTagText is not removed within $daysUntilClose days."
$witTypeSupported = "('Feature','Task','User Story')"
##

## get active wit assigned to user
$activeWitWiqlQuery = "select [System.Id], [System.WorkItemType], [System.Title], [System.AssignedTo], [System.ChangedDate], [System.State], [System.Tags] from WorkItems where [System.WorkItemType] IN $($witTypeSupported) and not [System.State] in ('Closed', 'Resolved', 'Completed', 'Cut') AND [System.Tags] NOT CONTAINS '$staleTagText' AND [System.ChangedDate] < @today - $daysUntilStale AND [System.AssignedTo] = '$($assignedTo)' ORDER BY [System.ChangedDate] ASC"
$inactiveWits = GetWorkItems $activeWitWiqlQuery $organization 

<# mark all the filtered wits as stale by 
 1. add stale tag to wit
 2. add stale comment to wit
 #>
$updatedStaleWits = MarkWitAsStale $organization $inactiveWits $exemptTags $staleTagText $staleCommentText

HTMLContentWitsWithChangedDate $updatedStaleWits
