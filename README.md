[![Build Status](https://dev.azure.com/ms/azure-devops-cli-extension/_apis/build/status/Azure%20DevOps%20CLI%20-%20Merge%20GitHub?branchName=master)](https://dev.azure.com/ms/azure-devops-cli-extension/_build/latest?definitionId=39&branchName=master)

# Azure DevOps Extension for Azure CLI

The Azure DevOps Extension for Azure CLI adds Pipelines, Boards, Repos, Artifacts and DevOps commands to the Azure CLI 2.0.

> The Azure DevOps Extension is currently in preview but we encourage you to give it a try and provide feedback (or contribute).
>
>The Azure CLI with the Azure DevOps Extension has replaced the VSTS CLI. The VSTS CLI has been deprecated and will no longer be receiving new features. We recommend that users of the VSTS CLI switch to the Azure CLI and add the Azure DevOps extension. See the [Command Mapping](/doc/command_mapping.md) section to view the mapping between VSTS CLI and Azure DevOps Extension commands.

## Quick start

1. [Install the Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli). You must have at least `v2.0.49`, which you can verify with `az --version` command.

1. Add the Azure DevOps Extension `az extension add --name azure-devops`

1. Run the `az login` command.

    If the CLI can open your default browser, it will do so and load a sign-in page. Otherwise, you need to open a
    browser page and follow the instructions on the command line to enter an authorization code after navigating to
    [https://aka.ms/devicelogin](https://aka.ms/devicelogin) in your browser. For more information, see the
    [Azure CLI login page](https://docs.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest).

See the [Get started guide](/doc/getting_started.md) for detailed setup instructions.

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
    project          : Manage team projects.
    service-endpoint : Manage service endpoints/service connections.
    team             : Manage teams.

Commands:
    configure        : Configure the Azure DevOps CLI or view your configuration.
    feedback         : Displays information on how to provide feedback to the Azure DevOps CLI team.
    login            : Set the credential (PAT) to use for a particular organization.
    logout           : Clear the credential for all or a particular organization.
```

- Documentation for all the commands is available at [Microsoft Azure CLI Docs - Azure DevOps](https://docs.microsoft.com/cli/azure/ext/azure-devops/?view=azure-cli-latest).
- Check out other examples in the [samples](/doc/samples.md) section.

## Contribute

See our [contribution guidelines](CONTRIBUTING.md) to learn how you can contribute to this project.

## License

[MIT License](LICENSE)
