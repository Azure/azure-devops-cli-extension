# Set up credentials and connect to Azure Devops

Before you can run VSTS commands, you need to run the vsts login command to sign in or set up credentials. There are a few ways to establish credentials for use in the CLI.


## Option 1: Login with azure-cli credentials
All MSA and AAD backed accounts can directly run `az login` command to use azure devops resources.
```bash
az login
```
You will be prompted to go to a URL and supply the provided code.


## Option 2: Login using a personal acces token
 
First, create a personal access token if you don't have one. If you already have one, you can skip this step to the options below.

To make full use of the Azure devops cli, you should check the All scopes option when creating the token. If you only need to interact with a specific Azure devops organization, limit your token to just this organization.

Use `az devops login` command to store your PAT. The Azure devops CLI securely stores credentials in the Credential Manager (on Windows), Keychain (on macOS), or protected file (on Linux).

You can provide PAT in following ways.

1. Default login. 
```bash
az devops login
```
You will be prompted to enter PAT token. Let's say you run the command `az repos pr list --org https://dev.azure.com/MY-ORGANIZATION-NAME` , default PAT token would be used against this URL for this scenario. 

3. Enter credential for particular account.
```bash
az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
```
You will be prompted to enter PAT token for <MY-ORGANIZATION-NAME>. This would be also set to your default organization in config file. This means above organization URL would be assumed if you choose to skip providing `organization` argument for a command. Every `az devops login` command run with organization URL would update the default. You can list/change a default value by running: `az devops configure --defaults`.

4. In non-interactive mode: Fetch the PAT from a file and pass it on to login command
```bash
cat my_pat_token.txt | az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
```
Again, your default organization would be updated in this case.

5. You can also store your PAT token in an environment variable called 'AZURE_DEVOPS_CLI_PAT' and skip 'az devops login' command for automation scenarios.


# Logout


## Logout from azure-cli

```bash
az logout
```
If you have logged-in with `az login` , you can directly run `az logout` command.

## Logout from azure devops cli

You can run following commands to reset credentials for azure devops.

1. Clear the default credentials.
```bash
`az devops logout`
```
This will reset the default credentials.

2. Logout of a particular account.
```bash
`az devops logout --organization https://dev.azure.com/MY-ORGANIZATION-NAME/`
```
This will clear the credentials for a particular URL. If default organization is set to 'https://dev.azure.com/MY-ORGANIZATION-NAME/', then this command would reset the default organization as well.  

 


