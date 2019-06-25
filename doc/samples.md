# Table of Contents

1. [Log in via Azure DevOps Personal Access Token (PAT)](samples.md#log-in-via-azure-devops-personal-access-token-pat)
1. [Auto detect and git aliases](samples.md#auto-detect-and-git-aliases)
1. [Configure output formats](samples.md#configure-output-formats)
1. [Query ouput](samples.md#query-output)
1. [Open items in browser](samples.md#open-items-in-browser)
1. [Use the Azure DevOps Extension in a release pipeline](samples.md#use-the-azure-devops-extension-in-a-release-pipeline)
1. [Use the Azure DevOps Extension with YAML](samples.md#use-the-azure-devops-extension-with-yaml)
1. [Use policy configuration file to configure policies](samples.md#use-policy-configuration-file-to-configure-policies)

## Log in via Azure DevOps Personal Access Token (PAT)

You can log in using an Azure DevOps Personal Access Token. See the [create personal access token guide](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts#create-personal-access-tokens-to-authenticate-access) to create one.

Once you have the PAT Token, run the `az devops login` command. You will be prompted to enter PAT token.

```bash
$az devops login --organization https://dev.azure.com/contoso
Token:
```

Once successfully logged in, this would also set your default organization to Contoso, provided there is no default organization configured.

In the above experience, you need to manually enter the token when prompted. However, you might want to login in a non-interactive manner, especially when running automation scripts. For this, you can use one of the following methods:

- Use environment variables.

There are cases where persisting a personal access token on the machine where the Azure CLI is running is not technically possible or is not secure. In these cases you can get a token from an environment variable.
To use a personal access token, set the `AZURE_DEVOPS_EXT_PAT` environment variable:

Windows:

```powershell
  set AZURE_DEVOPS_EXT_PAT=xxxxxxxxxx
```

Linux or macOS:

```bash
export AZURE_DEVOPS_EXT_PAT=xxxxxxxxxx
```

Replace *xxxxxxxxxx* with the your PAT.

Now run any command without having to login explicitly. Each command will try to use the PAT in the environment variable for authentication.

```bash
cat my_pat_token.txt | az devops login --organization https://dev.azure.com/contoso/
```

## Auto detect and git aliases

The Azure DevOps Extension has been optimized for Azure Repos to work well with git workflows.

The Azure DevOps Extension evaluates if your current working directory is an Azure Repos git repository to auto detect configuration setting - organization, project and repository. This is achieved using the `detect` flag which is ON by default.

If you are working in a local check out of a repository, you can simply run `az repos pr list` from the local directory to view all PRs.

You can also configure the Azure Devops Extension to add git aliases for common git-based Azure Repos commands like creating or adding reviewers to pull requests. This can be enabled by running the following command:

```bash
az devops configure --use-git-alias true
```

This will alias all `az repos` commands to `git repo` and all `az repos pr` commands to `git pr`.
So `az repos list` becomes `git repo list` and `az repo pr list` becomes `git pr list`

For example, a pull request can now be created using the following command:

```bash
git pr create --target-branch {branch\_name}
```

## Configure output formats

The output formats are inherited from Azure CLI. The Azure CLI uses JSON as its default output option, but offers various ways for you to format the output of any command.  Refer [Set the default output format](https://docs.microsoft.com/cli/azure/format-output-azure-cli?view=azure-cli-latest#set-the-default-output-format) guide to update default output format.

## Query output

You can use the --query parameter and the JMESPath query syntax to customize your output.

```bash
az devops project list --query "[?visibility=='private'].{ProjectName: name, ProjectDescription: description}"
```

```bash
ProjectName                                 ProjectDescription
--------------------------------            -------------------------------------------------
Foobar                                      Sample Foobar project
Fabrikam                                    Sample Fabrikam Project
```

## Open items in browser

You can use --open switch to open any artifact in Azure DevOps portal in your default browser.

For example :

```bash
az pipelines build show --id 1 --open
```

This will show the details of build with id 1 on command-line and also open it in the default browser.

## Use the Azure DevOps Extension in a release pipeline

To use the Azure DevOps Extension in a hosted agent using a Release Pipeline, execute the following steps:

- Create a New Release Pipeline

![new release pipeline](/doc/images/New%20Pipeline.PNG)

- Select an empty job

![select template](/doc/images/SelectTemplate.PNG)

- Click Stage 1 to configure the Stage.

![Stage 1](/doc/images/Stage.PNG)

- Configure the job to use Hosted Mac OS in Agent Pools

![Agent Job Configuration](/doc/images/JobConfig.PNG)

- Click on the + button to add a task and add PowerShell task

![PowerShell](/doc/images/PowerShell.PNG)

- Add the script - either via file or inline. For the example, the script has been included inline.

![PowerShell](/doc/images/Script.PNG)

Including the inline script for reference

```powershell
$extensions = az extension list -o json | ConvertFrom-Json

$devopsFound = $False
foreach($extension in $extensions)
{
    if($extension.name -eq 'azure-devops'){
        $devopsFound = $True
    }
}

if ($devopsFound -eq $False){
    az extension add -n azure-devops
}
```

### Use the Azure DevOps Extension with YAML

If you prefer to use YAML to provide your release pipeline configuration, you can use the following example to understand how YAML can be used to install Azure CLI and add the Azure DevOps extension.

In the example, you will learn how to add the Azure DevOps extension to Azure CLI and run the build and PR list commands on Linux, Mac OS and Windows hosted agents

- Create the azure-pipelines-steps.yml file and include the content below.

For Mac OS: azure-pipelines-steps-mac.yml

```yaml
steps:
- script: az extension add -n azure-devops
  displayName: 'Install Azure DevOps Extension'


- script: az devops configure --defaults organization=$(System.TeamFoundationCollectionUri) project=$(System.TeamProject) --use-git-aliases
  displayName: 'Set default Azure DevOps organization and project'

- script: |
    az pipelines build list
    git pr list
  env:
    AZURE_DEVOPS_EXT_PAT: $(System.AccessToken)
  displayName: 'Show build list and PRs'   
```

For Linux: azure-pipelines-steps-linux.yml

```yaml
steps:
  # Updating the python version available on the linux agent
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.x'
      architecture: 'x64'

  # Updating pip to latest
  - script: python -m pip install --upgrade pip
    displayName: 'Upgrade pip'

  # Updating to latest Azure CLI version.
  - script: pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge
    displayName: 'upgrade azure cli'

  - script: az --version
    displayName: 'Show Azure CLI version'

  - script: az extension add -n azure-devops
    displayName: 'Install Azure DevOps Extension'

  - script: az devops configure --defaults organization=$(System.TeamFoundationCollectionUri) project=$(System.TeamProject) --use-git-aliases
    displayName: 'Set default Azure DevOps organization and project'

  - script: |
      az pipelines build list
      git pr list
    env:
      AZURE_DEVOPS_EXT_PAT: $(System.AccessToken)
    displayName: 'Show build list and PRs'
```

For Windows: azure-pipelines-steps-win.yml

```yaml
steps:
  # Updating the python version available on the linux agent
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.x'
      architecture: 'x64'

  # Updating pip to latest which is required by the Azure DevOps extension
  - script: python -m pip install --upgrade pip
    displayName: 'Upgrade pip'

  # Upgrading Azure CLI from 2.0.46 to latest; min version required for Azure DevOps is 2.0.49
  - script: pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge
    displayName: 'upgrade azure cli'

  - script: az --version
    displayName: 'Show Azure CLI version'

  - script: az extension add -n azure-devops
    displayName: 'Install Azure DevOps Extension'

  - script: az devops configure --defaults organization=$(System.TeamFoundationCollectionUri) project=$(System.TeamProject) --use-git-aliases
    displayName: 'Set default Azure DevOps organization and project' 

  - script: |
      az pipelines build list
      git pr list
    env:
      AZURE_DEVOPS_EXT_PAT: $(System.AccessToken)
    displayName: 'Show build list and PRs'
```

- Create the azure-pipelines.yml and include the content below.

```yaml
jobs:
# Running Azure DevOps extension commands on a hosted Mac agent
- job:
  displayName: 'macOS'
  pool:
    vmImage: 'macOS-10.13'
  steps:
  - template: azure-pipelines-steps-mac.yml

# Running Azure DevOps extension commands on a hosted Linux agent
- job:
  displayName: 'Linux'
  pool:
    vmImage: 'ubuntu-16.04'
  steps:
  - template: azure-pipelines-steps-linux.yml

# Runnig Azure DevOps extension commands on a hosted Windows agent
- job:
  displayName: 'Windows'
  pool:
    vmImage: 'vs2017-win2016'
  steps:
  - template: azure-pipelines-steps-win.yml
```

## Use policy configuration file to configure policies

You can easily configure branch policies for your repository using the various policy commands. However, the policy commands accept a single scope, i.e., single combination of repository, branch and match type. If you want to apply the same policy across various scopes, you can do that using a policy configuration file.

Say you want to create a manual queue build policy across all branch folders that start with "release" and also on the branch. To achieve this, execute the following steps:

- Create a policy configuration file for build polcy, including the multiple application scopes:

```json
{
"isBlocking": true,
"isDeleted": false,
"isEnabled": true,
"revision": 1,
"settings": {
  "buildDefinitionId": 22,
  "displayName": "Manual Queue Policy",
  "manualQueueOnly": true,
  "queueOnSourceUpdateOnly": false,
  "scope": [
  {
    "matchKind": "Prefix",
    "refName": "refs/heads/release",
    "repositoryId": "e646f204-53c9-4153-9ab9-fd41a11e3564"
  },
  {
    "matchKind": "Exact",
    "refName": "refs/heads/master",
    "repositoryId": "e646f204-53c9-4153-9ab9-fd41a11e1234"
  }
  ],
  "validDuration": 0
},
"type": {
  "displayName": "Build",
  "id": "0609b952-1397-4640-95ec-e00a01b2f659"
}
}
```

Refer the [Policy create](https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.0#examples) documentation to know more about the structure for various policy types.

- Save the file and run the create policy command

`az repos policy create C:\policyConfiguration.txt`

*Note that the path is provided using '\\' backslash.

## Create an Azure DevOps YAML based multi stage pipeline

You can create and manage YAML based multi stage Azure Pipelines using the `az pipelines` commands.

### Prerequisites

- A Github account, where you can create a repository. If you don't have one, you can [create one for free](https://github.com/)

- An Azure Devops organization. If you don't have one, you can [create one for free](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-sign-up?view=azure-devops). If your team already has one, then make sure you're an administrator of the Azure DevOps project that you want to use.

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) along with the [azure-devops extension](../getting_started.md) added.

- You can use Azure Pipelines to build an app written in any language. For this quickstart, we will use Java. To get started, fork the following repository into your GitHub account.

```BASH
https://github.com/MicrosoftDocs/pipelines-java
```

To create the pipeline, execute the following steps:

1. Sign in to Azure CLI using your crendentials.

1. Configure your defaults to include the Azure DevOps organization and project
   `az devops configure --defaults organization=https://dev.azure.com/contosoWebApp project=PaymentModule`

1. Clone your GitHub repository and navigate to the source code directory

1. Run `az pipelines create` command
   `az pipelines create --name "Contoso.CI"`

1. You will be asked for a service connection which enables Azure DevOps to communicate to GitHub. If you don't have one, you can create one and provide your GitHub credentials.

1. Select the Maven pipeline template from the list of recommended templates.

1. The pipeline YAML is generated. You can open the YAML in your default editor to view and make changes.

1. Select option to commit changes to master. A new run is started. Wait for the run to finish.

## Manage permissions with Azure DevOps CLI

You can update/reset/list permissions for an user or group with the help of security commands.

Refer [Permissions Documentation](permissions.md) for more details on how to get security tokens and manage permissions for a Azure DevOps resource.
