[![Build Status](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_apis/build/status/YAML/Azure%20DevOps%20CLI%20-%20Merge%20GitHub%20YAML?branchName=azuredevopscli-dev)](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build/latest?definitionId=38?branchName=azuredevopscli-dev)


# Azure DevOps Extension for Azure CLI


The Azure DevOps Extension for Azure CLI adds Pipelines, Boards, Repos, Artifacts and DevOps commands to the Azure CLI 2.0. 


> The Azure DevOps Extension is currently in preview but we encourage you to give it a try and provide feedback (or contribute).
With the release of the Azure DevOps Extension, we will be retiring the preview version of the VSTS CLI. The Azure DevOps Extension has functional parity with the VSTS CLI and we aim to deprecate VSTS CLI by April, 2019. 


# Quick start

1. [Install Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli). 
You must have at least `v2.0.49`, which you can verify with `az --version` command.
2. Add the Azure DevOps Extension
`az extension add --name azure-devops`
3. Run the `az login` command. 

    If the CLI can open your default browser, it will do so and load a sign-in page.
    Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after       navigating to https://aka.ms/devicelogin in your browser. For more information, see the [Azure CLI login page](https://docs.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest). 

See the [Get started guide](/doc/getting_started.md) for detailed setup instructions. 

# Usage
```
$az [group] [subgroup] [command] {parameters}
```
Adding the Azure DevOps Extension adds `devops`, `pipelines`, `artifacts`, `boards` and `repos` groups.
For usage and help content for any command, pass in the -h parameter, for example:
```
$az devops -h
```
- Documentation for all the commands is available at [Microsoft Azure CLI Docs - Azure DevOps](https://docs.microsoft.com/cli/azure/ext/azure-devops/?view=azure-cli-latest). 
- Check out other examples in the [samples](/doc/samples.md) section.

# Contribute

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

See our [contribution guidelines](/doc/contributing.md) to learn how you can contribute to this project.

[MIT License](LICENSE)
