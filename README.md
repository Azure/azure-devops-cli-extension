[![Build Status](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_apis/build/status/YAML/Azure%20DevOps%20CLI%20-%20Merge%20GitHub%20YAML?branchName=azuredevopscli-dev)](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build/latest?definitionId=38?branchName=azuredevopscli-dev)


# Azure DevOps Extension for Azure CLI


The Azure DevOps Extension for Azure CLI adds Pipelines, Boards, Repos, Artifacts and DevOps commands to the Azure CLI 2.0. 


> Azure DevOps extension is currently in preview but we encourage you to give it a try and provide feedback (or contribute).
With the release of Azure DevOps extension, we will be retiring the preview version of VSTS CLI. The Azure DevOps extension has functional parity with the VSTS CLI and we aim to deprecate the preview version of VSTS CLI by April, 2019. 


# Installation

1. [Install Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli). 
You must have at least `v2.0.49`, which you can verify with `az --version` command.
2. Add Azure DevOps extension
`az extension add --name azure-devops`

# Usage
```
$az [group] [subgroup] [command] {parameters}
```
Adding the Azure DevOps extension adds `devops`, `pipelines`, `artifacts`, `boards` and `repos` groups.
For usage and help content for any command, pass in the -h parameter, for example:
```
$az devops -h
```
- Documentation for all the commands is available at [Microsoft Azure CLI Docs - Azure DevOps](https://docs.microsoft.com/cli/azure/ext/azure-devops/?view=azure-cli-latest). 
- Please refer the [Getting Started guide]() for detailed setup instructions. 
- Check out other examples in the [samples](/doc/samples.md) section.

# Contribute

## Code of Conduct
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Contribution Guidelines
Refer our [contribution guidelines](/doc/contributing.md) to learn how you can contribute to this project.


# License

```
Azure DevOps Extension

MIT License

    Copyright (c) Microsoft Corporation. All rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE
```
