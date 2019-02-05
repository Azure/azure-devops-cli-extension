# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_repos_help():
    helps['repos'] = """
    type: group
    short-summary: Manage Azure Repos.
    long-summary:
    """

    helps['repos pr'] = """
    type: group
    short-summary: Manage pull requests.
    long-summary:
    """

    helps['repos pr policy'] = """
    type: group
    short-summary: Manage pull request policy.
    long-summary:
    """

    helps['repos pr reviewers'] = """
    type: group
    short-summary: Manage pull request reviewers.
    long-summary:
    """

    helps['repos pr work-items'] = """
    type: group
    short-summary: Manage work items associated with pull requests.
    long-summary:
    """

    helps['repos import'] = """
    type: group
    short-summary: Manage Git repositories import
    long-summary:
    """

    helps['repos policy'] = """
    type: group
    short-summary: Manage branch policy.
    long-summary:
    """

    create_update_helptext = """
        - name: {0} a approver count policy
          text: |
            az repos policy {1} --branch "refs/heads/master" -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type ApproverCountPolicy --allowDownvotes False --creatorVoteCounts False --minimumApproverCount 2 --resetOnSourcePush True --isBlocking --isEnabled
    """

    helps['repos policy create'] = """
    type: command
    short-summary: Create a policy.
    long-summary: see https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies-overview?view=azure-devops for more details
    examples: 
        {}
    """.format(create_update_helptext.format('Create', 'create'))

    helps['repos policy update'] = """
    type: command
    short-summary: Update a policy.
    long-summary: see https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies-overview?view=azure-devops for more details
    examples: 
        {}
    """.format(create_update_helptext.format('Update', 'update --policy-id 1'))
