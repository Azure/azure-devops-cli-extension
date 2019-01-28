#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

param(
[string]$workitem_titles,
[string]$wit_template
)

Write-Host("Sample Usage -")
Write-Host("createWorkitemsinBulk.ps1 -workitem_titles ./my_wit_titles -wit_template ./my_wit_template")

<# 
Sample Wit Template :

organization=https://dev.azure.com/baggaatul24
project=testproject
workitem_type=Task
assignedto=
area=
iteration=
#>

if (!$wit_template)
{
    Write-Host("Template not provided will ask for default params interactively. Alternatively create a wit template and pass it to the script.")
    $organization = Read-host("Organization URL: ")
    $project = Read-host("Project Name: ")
    $workitem_type = Read-host("Workitem Type: ")
}
else{
    foreach($line in Get-Content $wit_template) {
    #    Write-Host($line)
        $arr = $line.split('=')
        $x = "$" + $arr[0]
        $y = """" + $arr[1] + """"
        if($y){
            Invoke-Expression("$x = $y")
        }
    }

    Write-Host("Creating a task with organization - " + $organization)
    Write-Host("Creating a task with project - " + $project)
    Write-Host("Creating a task with assigned to - " + $assignedto)
}

if (!$workitem_titles)
{
    Write-Host("No file for workitem titles. Will run in interactive mode to create workitems.")
    while(1) {
        $title = Read-Host("Enter workitem title: ")
        $command_string = "az boards work-item create --org $organization --project $project --title ""$title"" --type $workitem_type" # --assigned-to $assignedto #Doesnot seem to work
        Invoke-Expression($command_string) 
    }
}
else {
    foreach($line in Get-Content $workitem_titles) {
        $command_string = "az boards work-item create --org $organization --project $project --title ""$line"" --type $workitem_type" # --assigned-to $assignedto #Doesnot seem to work
        Invoke-Expression($command_string) 
    }
}