# Instructions to release a new version of Azure DevOps CLI extension

The creation of a new release involves:

1. Creating a new wheel from existing code and hosting it.
1. Updating index file in Azure CLI extensions repository.
1. Updating Azure DevOps CLI extension version in repository and releases

## Creating a new wheel from existing code and hosting it

To do this trigger a [Azure DevOps CLI - Create Releases - YAML](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=40&_a=summary) build

This build will:

* create and upload wheel with the latest code (which can be downloaded from artifacts)
* this will also create a draft release in GitHub Repository
* calculate sha256 for the wheel (which can be found in logs)

### Manual Steps

* Publish the draft release in GitHub after making required changes in release notes

## Updating index file in Azure CLI extensions repository

Index file is present [here](https://github.com/Azure/azure-cli-extensions/blob/master/src/index.json) which needs to be updated so that new wheel is available for consumption in azure CLI
Find 'DevOps' to see where is the entry for 'DevOps' extension
Create a PR for updating, fiels in index json are self explanatory

## Updating Azure DevOps CLI extension version in repository and releases

once relase is done make sure to update the version for Azure-DevOps CLI in [version.py](https://github.com/Microsoft/azure-devops-cli-extension/blob/master/azure-devops/azext_devops/version.py)
Also update build pipelines YAMLS
[Release Pipeline](./../.azure-pipelines/azure-pipelines-create-release.yml)
[Merge Pipeline](./../.azure-pipelines/azure-pipelines-merge.yml)

### Update AzureDevOpsCli-Released-Version-Check

Update [AzureDevOpsCli-Released-Version-Check](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build?definitionId=34) to run from the commit which was used to do the release.
This release runs periodically and makes sure the released build works. Main validation here is dependency validation.
Update Job 'Run_Test_From_Old_Release' in YAML to pick up the new released branch to run tests.
