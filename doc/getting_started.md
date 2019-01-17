# Getting started
Now that you have successfully installed Azure CLI and added the Azure DevOps extension, you are all set to get started!

## Log in to Azure DevOps
Before you can work with Azure DevOps, you need to log in to Azure CLI using the `az login` command.

If the CLI can open your default browser, it will do so and load a sign-in page.
Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after navigating to https://aka.ms/devicelogin in your browser. For more information, please refer [azure cli login page](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest).

You can also login using an Azure DevOps Personal Access Token. Refer [Connecting to Azure DevOps using PAT token]().

## Configuring defaults
Although you can provide the organization and project for each command, we recommend you set these as defaults in configuration for seamless commanding. 

`az devops configure defaults --organization https://dev.azure.com/myorganization --project myproject`

## Example

Let us look at an example where the Azure DevOps extension can be used to view and trigger a build in Azure Pipelines.

1. Configure defaults
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
3. Queue a build pipeline
```
$az pipelines build queue --definition-name Contoso.CI -o table
ID   Number      Status      Result     Definition ID   Definition Name           Source Branch    Queued Time                 Reason  
---  ----------  ---------   ---------  -------------   -----------------------   --------------   --------------------------  -------
1    20190116.2  completed   succeeded  1               Contoso.CI                master           2019-01-16 17:29:07.497795  manual
```

