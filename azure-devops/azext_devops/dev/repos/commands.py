# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azext_devops.dev.common.exception_handler import azure_devops_exception_handler
from ._format import (transform_pull_request_table_output,
                      transform_pull_requests_table_output,
                      transform_repo_table_output,
                      transform_repos_table_output,
                      transform_ref_table_output,
                      transform_refs_table_output,
                      transform_reviewers_table_output,
                      transform_reviewer_table_output,
                      transform_policies_table_output,
                      transform_policy_table_output,
                      transform_work_items_table_output,
                      transform_repo_import_table_output,
                      transform_repo_policy_table_output,
                      transform_repo_policies_table_output)


reposPullRequestOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.pull_request#{}',
    exception_handler=azure_devops_exception_handler
)

reposRefOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.ref#{}',
    exception_handler=azure_devops_exception_handler
)

reposRepositoryOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.repository#{}',
    exception_handler=azure_devops_exception_handler
)

reposImportOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.import_request#{}',
    exception_handler=azure_devops_exception_handler
)

policyOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.policy#{}',
    exception_handler=azure_devops_exception_handler
)


def load_code_commands(self, _):  # pylint: disable=too-many-statements
    with self.command_group('repos', command_type=reposRepositoryOps) as g:
        # repository commands
        g.command('create', 'create_repo', table_transformer=transform_repo_table_output)
        g.command('delete', 'delete_repo', confirmation='Are you sure you want to delete this repository?')
        g.command('list', 'list_repos', table_transformer=transform_repos_table_output)
        g.command('show', 'show_repo', table_transformer=transform_repo_table_output)
        g.command('update', 'update_repo', table_transformer=transform_repo_table_output)

    with self.command_group('repos policy', command_type=policyOps) as g:
        # repository/ branch policies
        g.command('list', 'list_policy', table_transformer=transform_repo_policies_table_output)
        g.command('show', 'get_policy', table_transformer=transform_repo_policy_table_output)
        g.command('delete', 'delete_policy', confirmation='Are you sure you want to delete this policy?')
        g.command('create', 'create_policy_configuration_file', table_transformer=transform_repo_policy_table_output)
        g.command('update', 'update_policy_configuration_file', table_transformer=transform_repo_policy_table_output)
        g.command('approver-count create', 'create_policy_approver_count',
                  table_transformer=transform_repo_policy_table_output)
        g.command('approver-count update', 'update_policy_approver_count',
                  table_transformer=transform_repo_policy_table_output)
        g.command('merge-strategy create', 'create_policy_merge_strategy',
                  table_transformer=transform_repo_policy_table_output)
        g.command('merge-strategy update', 'update_policy_merge_strategy',
                  table_transformer=transform_repo_policy_table_output)
        g.command('build create', 'create_policy_build',
                  table_transformer=transform_repo_policy_table_output)
        g.command('build update', 'update_policy_build',
                  table_transformer=transform_repo_policy_table_output)
        g.command('comment-required create', 'create_policy_comment_required',
                  table_transformer=transform_repo_policy_table_output)
        g.command('comment-required update', 'update_policy_comment_required',
                  table_transformer=transform_repo_policy_table_output)
        g.command('work-item-linking create', 'create_policy_work_item_linking',
                  table_transformer=transform_repo_policy_table_output)
        g.command('work-item-linking update', 'update_policy_work_item_linking',
                  table_transformer=transform_repo_policy_table_output)
        g.command('file-size create', 'create_policy_file_size',
                  table_transformer=transform_repo_policy_table_output)
        g.command('file-size update', 'update_policy_file_size',
                  table_transformer=transform_repo_policy_table_output)
        g.command('required-reviewer create', 'create_policy_required_reviewer',
                  table_transformer=transform_repo_policy_table_output)
        g.command('required-reviewer update', 'update_policy_required_reviewer',
                  table_transformer=transform_repo_policy_table_output)
        g.command('case-enforcement create', 'create_policy_case_enforcement',
                  table_transformer=transform_repo_policy_table_output)
        g.command('case-enforcement update', 'update_policy_case_enforcement',
                  table_transformer=transform_repo_policy_table_output)

    with self.command_group('repos pr', command_type=reposPullRequestOps) as g:
        # basic pr commands
        g.command('create', 'create_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('update', 'update_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('show', 'show_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('list', 'list_pull_requests', table_transformer=transform_pull_requests_table_output)
        g.command('checkout', 'checkout')

        # pr reviewer commands
        g.command('reviewer add', 'create_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.command('reviewer list', 'list_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.command('reviewer remove', 'delete_pull_request_reviewers',
                  table_transformer=transform_reviewers_table_output)

        # pr work item commands
        g.command('work-item add', 'add_pull_request_work_items', table_transformer=transform_work_items_table_output)
        g.command('work-item list', 'list_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)
        g.command('work-item remove', 'remove_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)

        # pr set-vote commands
        g.command('set-vote', 'vote_pull_request', table_transformer=transform_reviewer_table_output)

        # pr policy commands
        g.command('policy list', 'list_pr_policies', table_transformer=transform_policies_table_output)
        g.command('policy queue', 'queue_pr_policy', table_transformer=transform_policy_table_output)

    with self.command_group('repos import', command_type=reposImportOps) as g:
        # import request
        g.command('create', 'create_import_request', table_transformer=transform_repo_import_table_output)

    with self.command_group('repos ref', command_type=reposRefOps) as g:
        # refs commands
        g.command('create', 'create_ref', table_transformer=transform_ref_table_output)
        g.command('delete', 'delete_ref', table_transformer=transform_ref_table_output)
        g.command('list', 'list_refs', table_transformer=transform_refs_table_output)
        g.command('lock', 'lock_ref', table_transformer=transform_ref_table_output)
        g.command('unlock', 'unlock_ref', table_transformer=transform_ref_table_output)
