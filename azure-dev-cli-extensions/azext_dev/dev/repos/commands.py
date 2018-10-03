# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from knack.prompting import prompt_y_n
from ._format import (transform_pull_request_table_output,
                      transform_pull_requests_table_output,
                      transform_repo_table_output,
                      transform_repos_table_output,
                      transform_reviewers_table_output,
                      transform_reviewer_table_output,
                      transform_policies_table_output,
                      transform_policy_table_output,
                      transform_work_items_table_output)

from .pull_request import (create_pull_request,
                           update_pull_request,
                           show_pull_request, 
                           list_pull_requests,
                           complete_pull_request,
                           abandon_pull_request,
                           reactivate_pull_request,
                           create_pull_request_reviewers,
                           list_pull_request_reviewers,
                           delete_pull_request_reviewers,
                           add_pull_request_work_items,
                           list_pull_request_work_items,
                           remove_pull_request_work_items,
                           vote_pull_request,
                           list_pr_policies,
                           queue_pr_policy)

from .repository import create_repo, list_repos, show_repo, delete_repo

def repo_delete_confirmation(command_args):
    return bool(prompt_y_n('Are you sure you want to delete this repository?'))

def load_code_commands(self, _):
    with self.command_group('repos') as g:
        # basic pr commands
        g.custom_command('pr create', 'dev.repos.pull_request.create_pull_request', table_transformer=transform_pull_request_table_output)
        g.custom_command('pr update', 'dev.repos.pull_request.update_pull_request', table_transformer=transform_pull_request_table_output)
        g.custom_command('pr show', 'dev.repos.pull_request.show_pull_request', table_transformer=transform_pull_request_table_output)
        g.custom_command('pr list', 'dev.repos.pull_request.list_pull_requests', table_transformer=transform_pull_requests_table_output)

        # pr status update commands
        g.custom_command('pr complete', 'dev.repos.pull_request.complete_pull_request', table_transformer=transform_pull_request_table_output)
        g.custom_command('pr abandon', 'dev.repos.pull_request.abandon_pull_request', table_transformer=transform_pull_request_table_output)
        g.custom_command('pr reactivate', 'dev.repos.pull_request.reactivate_pull_request', table_transformer=transform_pull_request_table_output)

        # pr reviewer commands
        g.custom_command('pr reviewers add', 'dev.repos.pull_request.create_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.custom_command('pr reviewers list', 'dev.repos.pull_request.list_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.custom_command('pr reviewers remove', 'dev.repos.pull_request.delete_pull_request_reviewers', table_transformer=transform_reviewers_table_output)

        # pr work item commands
        g.custom_command('pr work-items add', 'dev.repos.pull_request.add_pull_request_work_items', table_transformer=transform_work_items_table_output)
        g.custom_command('pr work-items list', 'dev.repos.pull_request.list_pull_request_work_items', table_transformer=transform_work_items_table_output)
        g.custom_command('pr work-items remove', 'dev.repos.pull_request.remove_pull_request_work_items', table_transformer=transform_work_items_table_output)

        # pr set-vote commands
        g.custom_command('pr set-vote', 'dev.repos.pull_request.vote_pull_request', table_transformer=transform_reviewer_table_output)

        # pr policy commands
        g.custom_command('pr policies list', 'dev.repos.pull_request.list_pr_policies', table_transformer=transform_policies_table_output)
        g.custom_command('pr policies queue', 'dev.repos.pull_request.queue_pr_policy', table_transformer=transform_policies_table_output)

        # repository commands
        g.custom_command('repo create', 'dev.repos.repository.create_repo', table_transformer=transform_repo_table_output)
        g.custom_command('repo delete', 'dev.repos.repository.delete_repo', confirmation=repo_delete_confirmation)
        g.custom_command('repo list', 'dev.repos.repository.list_repos', table_transformer=transform_repo_table_output)
        g.custom_command('repo show', 'dev.repos.repository.show_repo', table_transformer=transform_repo_table_output)