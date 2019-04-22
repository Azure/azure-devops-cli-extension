# Security Permissions Management

Security permissions for a User or Security group can be managed by running following group of commands:
`az devops security permission -h`

For more information on concepts related to Security permissions, kindly refer (REST API documentation)[https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.0]

## Finding the namespace

Typically, each family of resources (work items, Git repositories, etc.) is secured using a different namespace. Each security namespace contains zero or more access control lists. Each access control list contains a token, an inherit flag and a set of zero or more access control entries. Each access control entry contains an identity descriptor, an allowed permissions bitmask and an denied permissions bitmask.

### Listing all namespaces

To list all available namespace in an organization, run following command.
`az devops security permission namespace list`

### Getting namespace details

To get the details of a namespace, and check what are the permission types secured with that namespace, use `show` command.
`az devops security permission namespace show --namespace-id <NAMESPACE_ID>`


## Understanding security tokens

Tokens are arbitrary strings representing resources in VSTS and TFS. Token format differs per resource type, however hierarchy and separator characters are common between all tokens.


### Listing tokens for a namespace

Once you have figured the required namespace, you can list all the tokens available in namespace for a specific user or security group.
`az devops security permission list  --namespace-id <NAMESPACE_ID> --subject <USER_ID/GROUP_DESCRIPTOR> ` 

To get the required token for different namespaces, refer following [doc](security_tokens.md)

To list permissions for given token, for a group or user
`az devops security permission list  --namespace-id <NAMESPACE_ID> --subject <USER_ID/GROUP_DESCRIPTOR> --token <SECURITY_TOKEN>`

Check `resolve-json` command to interpret the json response and resolving it to corresponding permmission types.
`az devops security permission resolve-json --namespace-id <NAMESPACE_ID> --json-path listPermissionsJsonResponse.txt`

### Changing permissions

Here, permissions could be a single permission type or combination of multiple permission types
You will get the permission details available for any namespace with `az devops security permission namespace show --id` command.
You will have to pass this permission bits while assigning allow/deny permissions and removing permissions.

#### Add permissions

`az  devops security permission add  --namespace-id <NAMESPACE_ID> --subject <USER_ID/GROUP_DESCRIPTOR> --token <SECURITY_TOKEN> --allow-bit 4 deny-bit 1`

#### Reset permissions

`az  devops security permission reset  --namespace-id <NAMESPACE_ID> --subject <USER_ID/GROUP_DESCRIPTOR> --token <SECURITY_TOKEN> --permissions 5`

#### Reset all permissions 

You can clear all explicit permissions for given token , given user or group with following command.
`az devops security permission reset-all --namespace-id <NAMESPACE_ID> --subject <USER_ID/GROUP_DESCRIPTOR> --token <SECURITY_TOKEN>`


