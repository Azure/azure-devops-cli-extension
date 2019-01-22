[![Build Status](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_apis/build/status/YAML/Azure%20DevOps%20CLI%20-%20Merge%20GitHub%20YAML?branchName=azuredevopscli-dev)](https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_build/latest?definitionId=38?branchName=azuredevopscli-dev)

# Azure Devops

Azure Devops CLI is a new command line interface for [Azure Devops Service](https://azure.microsoft.com/en-in/services/devops/) 

> Azure Devops CLI is currently in preview but we encourage you to give it a try and provide feedback (or contribute). 

## Get started

Refer to the [install guide](https://aka.ms/azure-devops-cli-docs-install) for detailed install instructions for Windows, Mac, and Linux.

Also refer to the ["get started" guide](https://aka.ms/azure-devops-cli-docs-getstarted) for in-depth instructions including first-time setup steps.

For help, pass the `-h` or `--help` argument, for example:

```bash
az devops -h
az repos -h
```

### Commands

Use the Azure Devops CLI to work with and manage build, releases, code repositories, projects, work items, and more in your Azure Devops account or on-premises Team Foundation Server collection.

Here are just a few of the commands:

* az pipelines build queue
* az repos pr list
* az repos pr complete
* az repos pr reviewers add
* az repos pr work-items list
* az devops project create
* az boards work-item create
* az boards work-item update

See the full list of [available commands](https://aka.ms/azure-devops-cli-commands).

### Login (setup credentials)

Create a personal access token and provide to the Azure Devops CLI via the login command. You can follow any one of the below options for login:

1. All AAD or MSA users can run `az login` and they shall be able to run devops commands. 

2. Enter PAT token to be used against default URL
```bash
az devops login
```

3. Enter credential for particular account
```bash
az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
```

4. In non-interactive mode: Fetch the PAT from a file and pass it on to login command
```
cat my_pat_token.txt | az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
```

5. You can also store your PAT token in an environment variable called 'AZURE_DEVOPS_EXT_PAT' and skip 'az devops login' command for automation scenarios

### Using Azure Devops CLI Behind a Proxy

The Azure Devops CLI picks the network proxy configuration from the environment variables `HTTP_PROXY`, and `HTTPS_PROXY`. 

### Git aliases

You can also add aliases in Git for certain Azure Devops CLI commands. For example, `git pr list` will be an alias for `az repos pr list`.

### Querying and filtering output

You can use the `--query` parameter and the [JMESPath](http://jmespath.org/) query syntax to customize your output, for example:

```bash
Result
-------------------------------------------------------------
[Demos]\CLI Team
[Demos]\Demo Team
Fabrikam Fiber
```

### Examples and snippets

For more usage examples, see the official Azure Devops CLI [documentation](https://aka.ms/azure-devops-cli-docs-overview).

## Developer setup

To contribute or to just play with the CLI in your development environment, see [developer setup](./doc/dev_setup.md) 

## License

```
Azure Devops CLI

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

## Telemetry

Azure Devops CLI collects usage data and sends it to Microsoft to help improve our products and services. Read our [privacy statement](https://privacy.microsoft.com/en-us/privacystatement) to learn more. 

To disable telemetry use the `az configure` command.

## Feedback

If you have any issues, questions, comments, or feature requests regarding this tool, please file an issue within this github repo using our contribution guidelines. 

To find where to provide feedback from the CLI, run `az devops feedback`.

## Contribute

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

This project follows the same contribution guidelines outlined by the Azure CLI. If you would like to become an active contributor, please follow the instructions provided in [Microsoft Azure Projects Contribution Guidelines](http://azure.github.io/guidelines.html).
