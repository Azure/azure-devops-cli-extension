# Azure DevOps Extension for Azure CLI

[![Build Status](https://dev.azure.com/ms/azure-devops-cli-extension/_apis/build/status/Azure%20DevOps%20CLI%20-%20Merge%20GitHub?branchName=master)](https://dev.azure.com/ms/azure-devops-cli-extension/_build/latest?definitionId=39&branchName=master)

The Azure DevOps Extension for Azure CLI adds Pipelines, Boards, Repos, Artifacts and DevOps commands to the Azure CLI 2.0.

>The Azure CLI with the Azure DevOps Extension has replaced the VSTS CLI. The VSTS CLI has been deprecated and will no longer be receiving new features. We recommend that users of the VSTS CLI switch to the Azure CLI and add the Azure DevOps extension. See the [Command Mapping](/doc/command_mapping.md) section to view the mapping between VSTS CLI and Azure DevOps Extension commands.

## Quick start

1. [Install the Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli). You must have at least `v2.0.69`, which you can verify with `az --version` command.

1. Add the Azure DevOps Extension `az extension add --name azure-devops`

1. Run the `az login` command.

    If the CLI can open your default browser, it will do so and load a sign-in page. Otherwise, you need to open a
    browser page and follow the instructions on the command line to enter an authorization code after navigating to
    [https://aka.ms/devicelogin](https://aka.ms/devicelogin) in your browser. For more information, see the
    [Azure CLI login page](https://docs.microsoft.com/cli/azure/authenticate-azure-cli).

See the [Get started guide](https://docs.microsoft.com/azure/devops/cli/get-started?view=azure-devops) for detailed setup instructions.

## Usage

```bash
$az [group] [subgroup] [command] {parameters}
```

Adding the Azure DevOps Extension adds `devops`, `pipelines`, `artifacts`, `boards` and `repos` groups.
For usage and help content for any command, pass in the -h parameter, for example:

```bash
$ az devops -h

Group
    az devops : Manage Azure DevOps organization level operations.
        Related Groups
        az pipelines: Manage Azure Pipelines
        az boards: Manage Azure Boards
        az repos: Manage Azure Repos
        az artifacts: Manage Azure Artifacts.

Subgroups:
    admin            : Manage administration operations.
    extension        : Manage extensions.
    project          : Manage team projects.
    security         : Manage security related operations.
    service-endpoint : Manage service endpoints/service connections.
    team             : Manage teams.
    user             : Manage users.
    wiki             : Manage wikis.

Commands:
    configure        : Configure the Azure DevOps CLI or view your configuration.
    feedback         : Displays information on how to provide feedback to the Azure DevOps CLI team.
    invoke           : This command will invoke request for any DevOps area and resource. Please use
                       only json output as the response of this command is not fixed. Helpful docs -
                       https://docs.microsoft.com/en-us/rest/api/azure/devops/.
    login            : Set the credential (PAT) to use for a particular organization.
    logout           : Clear the credential for all or a particular organization.
```

- Checkout the CLI docs at [docs.microsoft.com - Azure DevOps CLI](https://docs.microsoft.com/azure/devops/cli/).
- Check out other examples in the [How-to guides](https://docs.microsoft.com/azure/devops/cli/?view=azure-devops#how-to-guides) section.
- You can view the various commands and its usage here - [docs.microsoft.com - Azure DevOps Extension Reference](https://docs.microsoft.com/cli/azure/ext/azure-devops)

## Contribute

See our [contribution guidelines](CONTRIBUTING.md) to learn how you can contribute to this project.

TLDR of [contribution guidelines](CONTRIBUTING.md) <br/>

Questions : [Stack Overflow](https://stackoverflow.com/questions/tagged/azure-devops) <br/>
Bug reports : [Developer Community](https://developercommunity.visualstudio.com/spaces/21/index.html) <br/>
New Feature request : [Azure DevOps repo](https://github.com/Microsoft/azure-devops-cli-extension/issues/new/choose) <br/>

## License

[MIT License](LICENSE)
