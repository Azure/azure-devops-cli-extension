# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_repos_help():
    helps['repos'] = """
    type: group
    short-summary: Manage Azure Repos.
    long-summary: This command group is a part of the azure-devops extension.
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
    long-summary: This command imports the public repo fabrikam-open-source to the empty Git repo fabrikam-open-source for the default configuration
                  az devops configure --defaults organization=https://dev.azure.com/fabrikamprime project="Fabrikam Fiber".
    examples:
          - name: Manage Git repositories import.
            text: |
                az repos import create --git-source-url https://github.com/fabrikamprime/fabrikam-open-source --repository fabrikam-open-source
    """

    helps['repos policy'] = """
    type: group
    short-summary: Manage branch policy.
    long-summary:
    """

    helps['repos policy approver-count'] = """
    type: group
    short-summary: Manage approver count policy.
    long-summary:
    """

    helps['repos policy build'] = """
    type: group
    short-summary: Manage build policy.
    long-summary:
    """

    helps['repos policy comment-required'] = """
    type: group
    short-summary: Manage comment required policy.
    long-summary:
    """

    helps['repos policy file-size'] = """
    type: group
    short-summary: Manage file size policy.
    long-summary:
    """

    helps['repos policy merge-strategy'] = """
    type: group
    short-summary: Manage merge strategy policy.
    long-summary:
    """

    helps['repos policy required-reviewer'] = """
    type: group
    short-summary: Manage required reviewer policy.
    long-summary:
    """

    helps['repos policy work-item-linking'] = """
    type: group
    short-summary: Manage work item linking policy.
    long-summary:
    """

    helps['repos policy case-enforcement'] = """
    type: group
    short-summary: Manage case enforcement policy.
    long-summary:
    """

    helps['repos ref'] = """
    type: group
    short-summary: Manage Git references.
    long-summary:
    """
