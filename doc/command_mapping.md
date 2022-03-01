# Command Mapping

> Updated till azure-devops extension version 0.13.0. This file is no longer maintained. Please check latest azure-devops [command reference](/cli/azure/ext/azure-devops) for command availability.

The following table provides the mapping of commands from VSTS CLI to Azure DevOps Extension.

|VSTS CLI|Azure DevOps Extension|
|---|---|
|`vsts configure`|`az devops configure`|
|`vsts feedback`|`az feedback`|
|`vsts login`|`az login` <br> `az devops login` (for PAT)|
|`vsts logout`|`az logout` <br> `az devops logout` (for PAT)|
|`vsts admin banner add`|`az devops admin banner add`|
|`vsts admin banner list`|`az devops admin banner list`|
|`vsts admin banner remove`|`az devops admin banner remove`|
|`vsts admin banner show`|`az devops admin banner show`|
|`vsts admin banner update`|`az devops admin banner update`|
|`vsts build list`|`az pipelines build list`|
|`vsts build queue`|`az pipelines build queue`|
|`vsts build show`|`az pipelines build show`|
|`vsts build definition list`|`az pipelines build definition list`|
|`vsts build definition show`|`az pipelines build definition show`|
|`vsts build task list`|`az pipelines build task list`|
|`vsts build task show`|`az pipelines build task show`|
|`vsts code pr abandon`|`az repos pr update --status abandoned`|
|`vsts code pr complete`|`az repos pr update --status completed`|
|`vsts code pr create`|`az repos pr create`|
|`vsts code pr list`|`az repos pr list`|
|`vsts code pr reactivate`|`az repos pr update --status active`|
|`vsts code pr set-vote`|`az repos pr set-vote`|
|`vsts code pr show`|`az repos pr show`|
|`vsts code pr update`|`az repos pr update`|
|`vsts code pr policies list`|`az repos pr policy list`|
|`vsts code pr policies queue`|`az repos pr policy queue`|
|`vsts code pr reviewers add`|`az repos pr reviewer add`|
|`vsts code pr reviewers list`|`az repos pr reviewer list`|
|`vsts code pr reviewers remove`|`az repos pr reviewer remove`|
|`vsts code pr work-items add`|`az repos pr work-item add`|
|`vsts code pr work-items list`|`az repos pr work-item list`|
|`vsts code pr work-items remove`|`az repos pr work-item remove`|
|`vsts code repo create`|`az repos create`|
|`vsts code repo list`|`az repos list`|
|`vsts code repo show`|`az repos show`|
|`vsts package universal download`|`az artifacts universal download`|
|`vsts package universal publish`|`az artifacts universal publish`|
|`vsts project create`|`az devops project create`|
|`vsts project list`|`az devops project list`|
|`vsts project show`|`az devops project show`|
|`vsts release list`|`az pipelines release list`|
|`vsts release create`|`az pipelines release create`|
|`vsts release show`|`az pipelines release show`|
|`vsts release definition list`|`az pipelines release definition list`|
|`vsts release definition show`|`az pipelines release definition show`|
|`vsts work item create`|`az boards work-item create`|
|`vsts work item show`|`az boards work-item show`|
|`vsts work item update`|`az boards work-item update`|
|`vsts work item query`|`az boards query`|
