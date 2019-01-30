## Table of Contents
1. [Log in via Azure DevOps Personal Access Token (PAT)](samples.md#log-in-via-azure-devops-personal-access-token-pat)
2. [Auto detect and git aliases](samples.md#auto-detect-and-git-aliases)
3. [Configure output formats](samples.md#configure-output-formats)
4. [Query ouput](samples.md#query-output)
4. [Open items in browser](samples.md#open-items-in-browser)
5. [Use the Azure DevOps Extension in a release pipeline](samples.md#use-the-azure-devops-extension-in-a-release-pipeline)
6. [Use the Azure DevOps Extension with YAML](samples.md#use-the-azure-devops-extension-with-yaml)

## Log in via Azure DevOps Personal Access Token (PAT)
You can log in using an Azure DevOps Personal Access Token. See the [create personal access token guide](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts#create-personal-access-tokens-to-authenticate-access) to create one. 

Once you have the PAT Token, run the `az devops login` command. You will be prompted to enter PAT token.
```
$az devops login --organization https://dev.azure.com/contoso
Token:
```
Once successfully logged in, this would also set your default organization to Contoso, provided there is no default organization configured. 

In the above experience, you need to manually enter the token when prompted. However, you might want to login in a non-interactive manner, especially when running automation scripts. For this, you can use one of the following methods:

1. Fetch PAT from a file and pass it to login command.
    ```
    cat my_pat_token.txt | az devops login --organization https://dev.azure.com/contoso/
    ```
2. Use environment variables.  
There are cases where persisting a personal access token on the machine where the Azure CLI is running is not technically possible or is not secure. In these cases you can get a token from an environment variable.
To use a personal access token, set the `AZURE_DEVOPS_EXT_PAT` environment variable:

    Windows:
    ```
      set AZURE_DEVOPS_EXT_PAT=xxxxxxxxxx
    ```
    Linux or macOS:
    ```
      export AZURE_DEVOPS_EXT_PAT=xxxxxxxxxx
    ```
    Replace *xxxxxxxxxx* with the your PAT.

    Now run
    ```bash
    $az devops login --organization https://dev.azure.com/contoso
    ```
## Auto detect and git aliases
The Azure DevOps Extension has been optimized for Azure Repos to work well with git workflows. 

The Azure DevOps Extension evaluates if your current working directory is an Azure Repos git repository to auto detect configuration setting - organization, project and repository. This is achieved using the `detect` flag which is ON by default. 

If you are working in a local check out of a repository, you can simply run `az repos pr list` from the local directory to view all PRs.

You can also configure the Azure Devops Extension to add git aliases for common git-based Azure Repos commands like creating or adding reviewers to pull requests. This can be enabled by running the following command:

```
$ az devops configure --use-git-aliases yes
```
This will alias all `az repos` commands to `git` and all `az repos pr` commands to `git pr`.

For example, a pull request can now be created using the following command:
```
$ git pr create --target-branch {branch\_name}
```

## Configure output formats

The output formats are inherited from Azure CLI. The Azure CLI uses JSON as its default output option, but offers various ways for you to format the output of any command.  Refer [Set the default output format](https://docs.microsoft.com/cli/azure/format-output-azure-cli?view=azure-cli-latest#set-the-default-output-format) guide to update default output format.

## Query output
You can use the --query parameter and the JMESPath query syntax to customize your output.

```

$ az devops project list --query "[?visibility=='private'].{ProjectName: name, ProjectDescription: description}"
```
```
ProjectName                                 ProjectDescription
--------------------------------            -------------------------------------------------
Foobar                                      Sample Foobar project
Fabrikam                                    Sample Fabrikam Project
```

## Open items in browser

You can use --open switch to open any artifact in Azure DevOps portal in your default browser.

For example :
```
$az pipelines build show --build-id 1 --open 
```
This will show the details of build with id 1 on command-line and also open it in the default browser.

## Use the Azure DevOps Extension in a release pipeline
To use the Azure DevOps Extension in a hosted agent using a Release Pipeline, execute the following steps:
1. Create a New Release Pipeline
![new release pipeline](/doc/images/New%20Pipeline.PNG)
2. Select an empty job
![select template](/doc/images/SelectTemplate.PNG)
3. Click Stage 1 to configure the Stage.
![Stage 1](/doc/images/Stage.PNG)
4. Configure the job to use Hosted Mac OS in Agent Pools
![Agent Job Configuration](/doc/images/JobConfig.PNG)
5. Click on the + button to add a task and add PowerShell task
![PowerShell](/doc/images/PowerShell.PNG)
6. Add the script - either via file or inline. For the example, the script has been included inline. 
![PowerShell](/doc/images/Script.PNG)

Including the inline script for reference
```bash
pip install --pre azure-cli==2.0.55 --extra-index-url https://azurecliprod.blob.core.windows.net/edgeaz --h
az --version
az extension add --name azure-devops
az devops -h
```

The first line of the script installs the Azure CLI. 

# Use the Azure DevOps Extension with YAML
If you prefer to use YAML to provide your release pipeline configuration, you can use the following example to understand how YAML can be used to install Azure CLI and add the Azure DevOps extension.

In the example, you will learn how to add the Azure DevOps extension to Azure CLI and run the build and PR list commands on Linux, Mac OS and Windows hosted agents

1. Create the azure-pipelines-steps.yml file and include the content below.

For Mac OS: azure-pipelines-steps-mac.yml
```
steps:
- script: az extension add -n azure-devops
  displayName: 'Install Azure DevOps Extension'

- script: echo ${AZURE_DEVOPS_CLI_PAT} | az devops login
  env:
    AZURE_DEVOPS_CLI_PAT: $(System.AccessToken)
  displayName: 'Login Azure DevOps Extension'

- script: az devops configure --defaults organization=$(System.TeamFoundationCollectionUri) project=$(System.TeamProject) --use-git-aliases yes
  displayName: 'Set default Azure DevOps organization and project'

- script: |
    az pipelines build list
    git pr list
  displayName: 'Show build list and PRs'
```
For Linux: azure-pipelines-steps-linux.yml
```
steps:
  # Updating the python version available on the linux agent
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.7.0'
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

  - script: echo ${AZURE_DEVOPS_CLI_PAT} | az devops login
    env:
      AZURE_DEVOPS_CLI_PAT: $(System.AccessToken)
    displayName: 'Login Azure DevOps Extension'  

  - script: az devops configure --defaults organization=https://georgeverghese.visualstudio.com project="Movie Search Web App" --use-git-aliases yes
    displayName: 'Set default Azure DevOps organization and project'
    
  - script: |
      az pipelines build list
      git pr list
    displayName: 'Show build list and PRs'
```

For Windows: azure-pipelines-steps-win.yml

```
steps:
  # Updating the python version available on the linux agent
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.7.0'
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
    
  - script: echo $(System.AccessToken) | az devops login
    env:
      AZURE_DEVOPS_CLI_PAT: $(System.AccessToken)
    displayName: 'Login Azure DevOps Extension'
  
  - script: az devops configure --defaults organization=https://georgeverghese.visualstudio.com project="Movie Search Web App" --use-git-aliases yes
    displayName: 'Set default Azure DevOps organization and project'

  - script: |
      az pipelines build list
      git pr list
    displayName: 'Show build list and PRs'
```
2. Create the azure-pipelines.yml and include the content below.
```
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