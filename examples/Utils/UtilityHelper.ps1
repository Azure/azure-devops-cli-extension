#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

function GetWorkItems {
    param(
        [string]$wiqlQuery, 
        [string]$organization
    )
    $workItems = az.cmd boards query --wiql $wiqlQuery --org $organization -o json | ConvertFrom-Json
    return $workItems
}


function HTMLContentWitsWithChangedDate {
    param (
        $witsParam,
        [string]$trackingData = ""
    )

    $sb = [System.Text.StringBuilder]::new()
    
    if ($witsParam) {
        [void]$sb.AppendLine( "<html><head><style>table, th, td {border: 1px solid black; font-family:verdana;font-size:12;}</style></head><body  style=`"font-family:verdana;font-size:11`">" )
        $ageColumnName = "Days Inactive"
        [void]$sb.AppendLine( "<table><tr><th>ID</th><th>Work Item Type</th><th>Title</th><th>State</th><th>$($ageColumnName)</th></tr>" )

        foreach ($wit in $witsParam) {
            [String]$witId = $wit.fields | Select-Object -ExpandProperty System.Id
            [String]$witType = $wit.fields | Select-Object -ExpandProperty System.WorkItemType
            [String]$witTitle = $wit.fields | Select-Object -ExpandProperty System.Title
            [String]$witState = $wit.fields | Select-Object -ExpandProperty System.State
            [String]$witChangedDate = $wit.fields | Select-Object -ExpandProperty System.ChangedDate

            $howOld = GetAge $witChangedDate
            
            [String]$witUrl = $wit.url.Replace("_apis/wit/workItems", "_workitems/edit")
            [string]$finalUrl = $witUrl + $trackingData
            [void]$sb.AppendLine( "<tr><td><a href=$finalUrl>$witId</a></td><td>$witType</td><td>$witTitle</td><td>$witState</td><td align=`"right`">$howOld</td></tr>" )
        }

        [void]$sb.AppendLine( "</table>" );
        [void]$sb.AppendLine( "</body></html>" )
    }
    
    return $sb.ToString()
}