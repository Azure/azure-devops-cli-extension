# Getting started
Now that you have successfully installed the Azure CLI and added the Azure DevOps Extension, you are all set to get started!

## Log in via Azure CLI
Before you can work with Azure DevOps, you need to log in using the `az login` command. 

If the CLI can open your default browser, it will do so and load a sign-in page.
Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after navigating to https://aka.ms/devicelogin in your browser. For more information, please refer the [Azure CLI login page](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest).

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
    
## Configuring defaults
Although you can provide the organization and project for each command, we recommend you set these as defaults in configuration for seamless commanding. 

`az devops configure defaults --organization https://dev.azure.com/contoso --project PaymentModule`

This ensures that the "contoso" and "PaymentModule" are configured as defaults for organization and project parameters. They will be used in any command that accepts organization or project as inputs.

You can view the defaults configured by running the following command:
```
$az devops configure --list

[defaults]
organization=https://dev.azure.com/contoso
project=PaymentModule

Use git alias = No
```
Configuration values used are evaluated in the following precedence, with items higher on the list taking priority.
1. Command-line parameters
2. Environment variables
3. Values configured with `az devops configure`

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

## Example

Let us look at an example where the Azure DevOps Extension can be used to view and trigger a build in Azure Pipelines using the concepts explained above.

1. Log in to Azure CLI
```
$az login
Note, we have launched a browser for you to login. For old experience with device code, use "az login --use-device-code"
You have logged in. Now let us find all the subscriptions to which you have access...
```
2. Configure defaults
```
$az devops configure --defaults organization=https://dev.azure.com/contosoWebApp project=PaymentModule`
```
If you want to explore the help document for any command, use the help switch (--help/-h) to see the corresponding documentation.

For example, in the above scenario, to see the help documentation, run the following command:
```
$ az devops configure -h
Command
  az devops configure: Configure the Azure DevOps CLI or view your configuration.
  
 Arguments
  --defaults -d     : Space separated 'name=value' pairs for common arguments defaults, e.g. '--
                      defaults project=my-project-name organization=https://dev.azure.com/organizationName arg=value' Use '' to 
                      clear the defaults, e.g. --defaults project=''.
  -- list    -l     : Lists the contents of the config file.
  --use-git-aliases : Set to 'yes' to configure Git aliiases global git config file (to enable 
                      commands like "git pr list"). Set to 'no' to remove any aliases set by the
                      tool. Allowed values: no, yes.

Global Arguments
  --debug           : Increase logging verbosity to show all debug logs
  --help -h         : Show this help message and exit.
  --output -o       : Output format. Allowed values: json, jsonc, table, tsv, yaml. Default: json.
  --query           : JMESPath query string. See http://jmespath.org/ for more information and examples.
  --subscription    : Name or ID of subscription. You can configure the default subscription using 'az account set -s NAME_OR_ID'
  --verbose         : Increase logging verbosity. Use --debug for full debug logs.
 
```

2. List all build pipelines
```
$az pipelines build list -o table
ID   Number      Status      Result     Definition ID   Definition Name           Source Branch    Queued Time                 Reason  
---  ----------  ---------   ---------  -------------   -----------------------   --------------   --------------------------  -------
1    20190116.2  completed   succeeded  1               Contoso.CI                master           2019-01-16 17:29:07.497795  manual
```

You can also view the build pipeline details on the portal by running the following command:
```
$az pipeline build show --build-id 1 --open-browser
```

3. Queue a build pipeline
```
$az pipelines build queue --definition-name Contoso.CI -o table
ID   Number      Status      Result     Definition ID   Definition Name           Source Branch    Queued Time                 Reason  
---  ----------  ---------   ---------  -------------   -----------------------   --------------   --------------------------  -------
1    20190116.2  completed   succeeded  1               Contoso.CI                master           2019-01-16 17:29:07.497795  manual
```



