## Table of Contents
1. [Log in via Azure DevOps Personal Access Token (PAT)](samples.md#log-in-via-azure-devops-personal-access-token-pat)
2. [Auto Detect and Git Aliases](samples.md#auto-detect-and-git-aliases)
3. [Configuring output formats](samples.md#configuring-output-formats)
4. [Query ouput](samples.md#query-output)
4. [Opening items in browser](samples.md#opening-items-in-browser)

## Log in via Azure DevOps Personal Access Token (PAT)
You can also log in using an Azure DevOps Personal Access Token. Refer [create personal access token guide](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts#create-personal-access-tokens-to-authenticate-access) to create one. 

Once you have the PAT Token, run the `az devops login` command. You will be prompted to enter PAT token.
```
$az devops login --organization https://dev.azure.com/contoso
Token:
```
Once successfully logged in, this would also set your default organization to Contoso, provided there is no default organization configured. 

In the above experience, you need to manually enter the token when prompted. However, you might want to login in a non-interactive manner, especially when running automation scripts. For this, you can use one of the following methods:

1. Fetch PAT from a file and pass it to login command.
    ```
    cat my_pat_token.txt | az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
    ```
2. Use environment variables.  
There are cases where persisting a personal access token on the machine where Azure CLI is running is not technically possible or is not secure. In these cases you can get a token from an environment variable.
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
## Auto Detect and Git Aliases
The Azure DevOps Extension has been optimized for Azure Repos to work well with git workflows. 

The Azure DevOps Extension evaluates if your current working directory is a git repository to auto detect configuration setting - organization, project and repository. This is achieved using the `detect` flag which is ON by default. 

If you are working in a local check out of an Azure Repos repository, you can simply run `az repos pr list` from the local directory to view all PRs.

You can also configure the Azure Devops Extension to add git aliases for common git-based Azure Repos commands like creating or adding reviewers to pull requests. This can be enabled by running the following command:

```
$ az devops configure --use-git-aliases yes
```
This will alias all `az repos` commands to `git` and all `az repos pr` commands to `git pr`.

For example, a pull request can now be created using the following command:
```
$ git pr create --target-branch {branch\_name}
```

## Configuring output formats

The output formats are inherited from Azure CLI. You can set the default output format value by running following command.
```
$az configure
```

The Azure CLI uses JSON as its default output option, but offers various ways for you to format the output of any command.  You can find more information about Azure CLI configuration and supported output formats [here](https://docs.microsoft.com/en-us/cli/azure/format-output-azure-cli?view=azure-cli-latest)

## Query output
You can use the --query parameter and the JMESPath query syntax to customize your output.

```

$ az devops project list --query "[?visibility=='private'].{ProjectName: name, ProjectDescription: description}"

ProjectName                                 ProjectDescription
--------------------------------            -------------------------------------------------
Foobar                                      Sample Foobar project
Fabrikam                                    Sample Fabrikam Project
```

## Opening items in browser

You can use --open switch to open any artifact in Azure DevOps portal in your default browser.

For example :
```
bash
az pipelines build show --build-id 1 --open-browser 
```
This will show the details of build with id 1 on command-line and also open it in the default browser.
