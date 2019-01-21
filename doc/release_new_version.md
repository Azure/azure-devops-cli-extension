# Instructions to release a new version of Azure DevOps CLI extension

## This involves 3 broad steps
(1) Creating a new wheel from existing code and hosting it.  
(2) Updating index file in Azure CLI extensions repository.  
(3) Updating Azure DevOps CLI extension version in repository and releases  

## Details:
## Creating a new wheel from existing code and hosting it.
To do this trigger a [Azure DevOps CLI - Create Releases - YAML](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=40&_a=summary) build
### This build will 
 - create and upload wheel with the latest code (which can be downloaded from artifacts)
 - calculate sha256 for the wheel (which can be found in logs)

### Manual Steps
- Create a new release in GitHub
- Download wheel from build artifacts and put the same in GitHub releases
 
## Updating index file in Azure CLI extensions repository
Index file is present [here](https://github.com/Azure/azure-cli-extensions/blob/master/src/index.json) which needs to be updated so that new wheel is available for consumption in azure CLI  
Find 'DevOps' to see where is the entry for 'DevOps' extension  
Create a PR for updating, fiels in index json are self explanatory 

## Updating Azure DevOps CLI extension version in repository and releases
once relase is done make sure to update the version for Azure-DevOps CLI in [version.py](https://github.com/Microsoft/vsts-cli/blob/azuredevopscli-dev/azure-devops/azext_devops/version.py)  
Also update build pipelines   
[Azure DevOps CLI - Merge GitHub](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=25)  
[AzureDevOpsCli-Release](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=29)  

### Update AzureDevOpsCli-Released-Version-Check
Update [AzureDevOpsCli-Released-Version-Check](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=34) to run from the commit which was used to do the release.
This release runs periodically and makes sure the released build works. Main validation here is dependency validation.
