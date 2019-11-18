# Instructions to release a new version of Azure DevOps CLI extension

The creation of a new release involves:

1. Creating a new wheel from existing code and hosting it.
1. Updating index file in Azure CLI extensions repository.
1. Updating Azure DevOps CLI extension version in repository and releases

## Creating a new wheel from existing code and hosting it

To do this trigger a [Azure DevOps CLI - Create Releases - YAML](https://dev.azure.com/ms/azure-devops-cli-extension/_build?definitionId=38) build

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

## Create a new release branch and push to the repo 
Create a new branch (release-0.x.0) from  master with the changes which have been released and push this new branch to the repo.

## Updating Azure DevOps CLI extension version in repository and releases

Once relase is done make sure to update the version for Azure-DevOps CLI in [version.py](https://github.com/Microsoft/azure-devops-cli-extension/blob/master/azure-devops/azext_devops/version.py)
Also update build pipelines YAMLS
[Release Pipeline](./../.azure-pipelines/azure-pipelines-create-release.yml)
[Merge Pipeline](./../.azure-pipelines/azure-pipelines-merge.yml)

### Update Azure DevOps CLI-Released Version pipeline definition

Update the [definition](https://dev.azure.com/ms/azure-devops-cli-extension/_build?definitionId=36&_a=summary) to run from the latest release branch as pushed above.

This release runs periodically and makes sure the released build works. Main validation here is dependency validation.
