# Getting started
Now that you have successfully installed Azure CLI 2.0 and added the Azure DevOps extension, you are all set to get started!

## Log in to Azure DevOps
Before you can work with Azure DevOps, you need to log in to Azure CLI using the `az login` command.

If the CLI can open your default browser, it will do so and load a sign-in page.
Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after navigating to https://aka.ms/devicelogin in your browser. For more information, please refer [azure cli login page](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest).

## Configuring defaults
Although you can provide the organization and project for each command, we recommend you set these as defaults in configuration for seamless commanding. 

`az devops configure defaults --organization https://dev.azure.com/myorganization --project myproject`

## Example

Let us look at an example where the Azure DevOps extension can be used to view and trigger a build in Azure Pipelines.

1. Configure defaults
```
$az devops configure --defaults organization=https://dev.azure.com/contosoWebApp project=PaymentModule`
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
