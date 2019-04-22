# Security tokens for Permissions management

Tokens are arbitrary strings representing resources in VSTS and TFS. Token format differs per resource type, however hierarchy and separator characters are common between all tokens.

### Hierarchy

A security namespace can be either hierarchical or flat.
Tokens in a hierarchical namespace exist in a hierarchy with effective permissions being inherited from parent tokens to child tokens.
Tokens in a flat namespace have no concept of a parent-child relationship between any two tokens.

### Separator character

Tokens in a hierarchical namespace either have a fixed length for each path part, or variable length.
If the tokens have variable-length path parts, then a separator character is used to distinguish where one path part ends and another begins.

### Project namespace

Get/Form tokens for project namespace [Namespace ID:52d39943-cb85-4d7f-8fa8-c6baac873819]

Basically tokens in this namespace are of the following format
 Root token : '$PROJECT'

 Token to secure permissions for each project in your organization
 '$PROJECT:vstfs:///Classification/TeamProject/PROJECT_ID'

 So, let's assume you have a project named 'Test Project 1'.
 You can get the project ID for this project by referring project show command
 `az devops project show --project "Test Project 1"`

 Above command would return a project-id (say xxxxxxxx-a1de-4bc8-b751-188eea17c3ba)

 Thus, the token to secure project related permissions for 'Test Project 1' would be
  '$PROJECT:vstfs:///Classification/TeamProject/xxxxxxxx-a1de-4bc8-b751-188eea17c3ba'