# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import (transform_pull_request_table_output,
                      transform_pull_requests_table_output,
                      transform_refs_table_output,
                      transform_ref_table_output,
                      transform_repo_table_output,
                      transform_repos_table_output,
                      transform_reviewers_table_output,
                      transform_reviewer_table_output,
                      transform_policies_table_output,
                      transform_policy_table_output,
                      transform_work_items_table_output)


def load_code_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'code', 'vsts.cli.code.common.{}') as g:
        # basic pr commands
        g.command('pr create', 'pull_request#create_pull_request',
                  table_transformer=transform_pull_request_table_output)
        g.command('pr update', 'pull_request#update_pull_request',
                  table_transformer=transform_pull_request_table_output)
        g.command('pr show', 'pull_request#show_pull_request',
                  table_transformer=transform_pull_request_table_output)
        g.command('pr list', 'pull_request#list_pull_requests',
                  table_transformer=transform_pull_requests_table_output)

        # pr status update commands
        g.command('pr complete', 'pull_request#complete_pull_request',
                  table_transformer=transform_pull_request_table_output)
        g.command('pr abandon', 'pull_request#abandon_pull_request',
                  table_transformer=transform_pull_request_table_output)
        g.command('pr reactivate', 'pull_request#reactivate_pull_request',
                  table_transformer=transform_pull_request_table_output)

        # pr reviewer commands
        g.command('pr reviewers add', 'pull_request#create_pull_request_reviewers',
                  table_transformer=transform_reviewers_table_output)
        g.command('pr reviewers list', 'pull_request#list_pull_request_reviewers',
                  table_transformer=transform_reviewers_table_output)
        g.command('pr reviewers remove', 'pull_request#delete_pull_request_reviewers',
                  table_transformer=transform_reviewers_table_output)

        # pr work item commands
        g.command('pr work-items add', 'pull_request#add_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)
        g.command('pr work-items list', 'pull_request#list_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)
        g.command('pr work-items remove', 'pull_request#remove_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)

        # pr set-vote commands
        g.command('pr set-vote', 'pull_request#vote_pull_request', table_transformer=transform_reviewer_table_output)

        # pr policy commands
        g.command('pr policies list', 'pull_request#list_pr_policies', table_transformer=transform_policies_table_output)
        g.command('pr policies queue', 'pull_request#queue_pr_policy', table_transformer=transform_policy_table_output)

        # refs commands
        g.command('ref create', 'ref#create_ref', table_transformer=transform_ref_table_output)
        g.command('ref delete', 'ref#delete_ref', table_transformer=transform_ref_table_output)
        g.command('ref list', 'ref#list_refs', table_transformer=transform_refs_table_output)
        g.command('ref update', 'ref#update_ref', table_transformer=transform_ref_table_output)

        # repository commands
        g.command('repo create', 'repository#create_repo', table_transformer=transform_repo_table_output)
        g.command('repo list', 'repository#list_repos', table_transformer=transform_repos_table_output)
        g.command('repo show', 'repository#show_repo', table_transformer=transform_repo_table_output)
