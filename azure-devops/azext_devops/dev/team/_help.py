# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_team_help():
    helps['devops'] = """
    type: group
    short-summary: Manage Azure DevOps organization level operations.
    long-summary: |
        Related Groups
        az pipelines: Manage Azure Pipelines
        az boards: Manage Azure Boards
        az repos: Manage Azure Repos
        az artifacts: Manage Azure Artifacts
        """

    helps['devops project'] = """
    type: group
    short-summary: Manage team projects.
    """

    helps['devops service-endpoint'] = """
    type: group
    short-summary: Manage service endpoints/service connections
    """

    helps['devops security'] = """
    type: group
    short-summary: Manage security related operations
    """

    helps['devops security group'] = """
    type: group
    short-summary: Manage security groups
    """

    helps['devops security group create'] = """
    type: command
    short-summary: Create a new Azure DevOps group.
    long-summary:
    examples:
          - name: Create an Azure DevOps Group with name and description
            text: |
              az devops security group create --name 'Some group name'
              --description 'Something to describe this group'
          - name: Add an existing AAD group to an Azure DevOps group
            text: |
              Get object ID of an existing AAD group
              az ad group show -g '{Group Name}'
              az devops security group create --origin-id '{Object ID}' --groups 'vssgp.someDescriptorForGroup'
          - name: Add an existing AAD group to an Azure DevOps group with AAD group Email ID
            text: |
              az devops security group create --email-id '{Email ID of AAD group}'
              --groups 'vssgp.someDescriptorForGroup'
          - name: Create a new Azure DevOps group and add it to existing Azure DevOps groups.
            text: |
              az devops security group create --name 'Some group name'
              --groups 'vssgp.someDescriptorForGroupOne,vssgp.someDescriptorForGroupTwo'
    """

    helps['devops security group membership'] = """
    type: group
    short-summary: Manage memberships for security groups
    """

    helps['devops team'] = """
    type: group
    short-summary: Manage teams
    """

    helps['devops user'] = """
    type: group
    short-summary: Manage users
    """

    helps['devops extension'] = """
    type: group
    short-summary: Manage extensions
    """

    helps['devops invoke'] = """
    type: command
    short-summary: This command will invoke request for any DevOps area and resource.
                   Please use only json output as the response of this command is not fixed.
                   Helpful docs -
                   https://docs.microsoft.com/en-us/rest/api/azure/devops/
    long-summary:
    examples:
        - name: Discover areas related to 'Wiki'
          text: |
            az devops invoke --query "[?contains(area,'wiki')]"

        - name: Get all wikis in a project
          text: |
            az devops invoke --area wiki --resource wikis --route-parameters project={Project Name} -o json
            az devops invoke --area wiki --resource wikis --route-parameters project=WikiIssue -o json

        - name: Add page to a wiki
          text: |
            az devops invoke --area wiki --resource pages --route-parameters project={Project Name}
            wikiIdentifier={Wiki Id} --in-file {Full File Path containing text to add to wiki}
            --query-parameters path={Page Path In Wiki} --http-method PUT --api-version 5.1-preview -o json
            az devops invoke --area wiki --resource pages --route-parameters project=WikiIssue
            wikiIdentifier=e479f402-2be8-4953-bb0b-3a0209cbc2d2 --in-file D:/temp/createWikiRequestBody.txt
            --query-parameters path=sample738 --http-method PUT --api-version 5.1-preview -o json
    """

    helps['devops wiki'] = """
    type: group
    short-summary: Manage wikis
    """

    helps['devops wiki page'] = """
    type: group
    short-summary: Manage wiki pages
    """
