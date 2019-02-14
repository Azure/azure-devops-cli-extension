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

    helps['repos pr reviewer'] = """
    type: group
    short-summary: Manage pull request reviewers.
    long-summary:
    """

    helps['repos pr work-item'] = """
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
        - name: {0} an approver count policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type ApproverCountPolicy --allow-downvotes False --creator-vote-counts False --minimum-approver-count 2 --reset-on-source-push True --is-blocking True --is-enabled True

        - name: {0} a build policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type BuildPolicy --build-definition-id 72 --display-name Build-Required --manual-queue-only False --queue-on-source-update-only True --valid-duration 12 --is-blocking True --is-enabled True

        - name: {0} a file size policy
          text: |
            az repos policy {1} -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type FileSizePolicy --maximum-git-blob-size-in-bytes 5012 --use-uncompressed-size True --is-blocking True --is-enabled True

        - name: {0} a merge strategy policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type MergeStrategyPolicy --use-squash-merge True --is-blocking True --is-enabled True

        - name: {0} a comment requirement policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type CommentRequirementsPolicy --is-blocking True --is-enabled True

        - name: {0} a work item linking policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type WorkItemLinkingPolicy --is-blocking True --is-enabled True

        - name: {0} a required reviewer policy
          text: |
            az repos policy {1} --branch master -r ac6b3157-6af1-4afa-b9d5-80d9ed3afd72 --policy-type RequiredReviewersPolicy --message this-is-policy-message --required-reviewer-ids gsaral@microsoft.com;atbagga@microsoft.com --is-blocking True --is-enabled True
    """

    helps['repos policy create'] = """
    type: command
    short-summary: Create a policy.
    long-summary:
    examples:
        {}
    """.format(create_update_helptext.format('Create', 'create'))

    helps['repos policy update'] = """
    type: command
    short-summary: Update a policy.
    long-summary:
    examples:
        {}
    """.format(create_update_helptext.format('Update', 'update --policy-id 1'))
