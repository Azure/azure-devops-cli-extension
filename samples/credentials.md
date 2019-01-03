# Set up credentials and connect to Azure Devops

Before you can run Azure devops commands, you need to run login command to sign in or set up credentials. There are a few ways to establish credentials for use in the CLI.


## Option 1: Login with Azure CLI credentials
All MSA and AAD backed accounts can directly run `az login` command to use azure devops resources.
```bash
az login
```
If the CLI can open your default browser, it will do so and load a sign-in page.

Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after navigating to [https://aka.ms/devicelogin](https://aka.ms/devicelogin) in your browser.
For more information, please refer [azure cli login page](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest).


## Option 2: Login using a personal acces token
 
First, create a [personal access token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts) if you don't have one. 

To make full use of the Azure Devops CLI, you should check the All scopes option when creating the token. If you only need to interact with a specific Azure devops organization, limit your token to just this organization.

Use `az devops login` command to store your PAT. The Azure devops CLI securely stores credentials in the Credential Manager (on Windows), Keychain (on macOS), or user protected file (on Linux).

You can provide PAT in following ways.

1. Login without providing any organization URL. 
    ```bash
    az devops login
    ```
    You will be prompted to enter PAT token. A separate `organization` URL argument needs to be passed in expected commands unless it is explicitly configured in defaults. 
    Let's say you run following command, default PAT token given with earlier command would be used against this URL. 
    ```
    az repos pr list --org https://dev.azure.com/MY-ORGANIZATION-NAME --project MY-PROJECT-NAME
    ```

2. Enter credential for a particular account.
    ```bash
    az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
    ```
    You will be prompted to enter PAT token for MY-ORGANIZATION-NAME. This would be also set to your default organization in config file. This means above organization URL would be assumed if you choose to skip `organization` argument for a command.
    Every time `az devops login` command is run with organization URL, it would update the default organization. You can list/update a default value by running `az devops configure --defaults` command.

3. In non-interactive mode: Fetch the PAT from a file and pass it on to login command.
    ```bash
    cat my_pat_token.txt | az devops login --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
    ```
    Again, your default organization would be updated in this case.

4. There are cases where persisting a personal access token on the machine where Azure devops CLI is running is not technically possible or is not secure. In these cases you can get a token from an environment variable.

    To use a personal access token, set the `AZURE_DEVOPS_CLI_PAT` environment variable:

    Windows:
    ```
    set AZURE_DEVOPS_CLI_PAT=xxxxxxxxxx
    ```

    Linux or macOS:
    ```
    export AZURE_DEVOPS_CLI_PAT=xxxxxxxxxx
    ```

    Replace *xxxxxxxxxx* with the PAT you created.

    > Important: If the `AZURE_DEVOPS_CLI_PAT` environment variable is set, the Azure Devops CLI will not attempt to use credentials established using the `az devops login` command.


# Logout


## Logout from Azure CLI

If you have logged-in with `az login` , you can directly run `az logout` command.
```bash
az logout
```

## Logout from Azure Devops CLI

You can run following commands to reset credentials for azure devops.

1. Clear the default credentials.
    ```bash
    az devops logout
    ```
    This will reset the default credentials.

2. Logout of a particular account.
    ```bash
    az devops logout --organization https://dev.azure.com/MY-ORGANIZATION-NAME/
    ```
    This will clear the credentials for a particular URL. If default organization is set to 'https://dev.azure.com/MY-ORGANIZATION-NAME/', then this command would reset the default organization as well.  

 


