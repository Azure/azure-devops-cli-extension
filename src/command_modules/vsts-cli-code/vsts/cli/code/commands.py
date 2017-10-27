# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandSuperGroup
from ._format import (transform_pull_request_table_output,
                      transform_pull_requests_table_output,
                      transform_reviewers_table_output,
                      transform_reviewer_table_output,
                      transform_policies_table_output,
                      transform_policy_table_output,
                      transform_work_items_table_output)


def load_code_commands(cli_command_loader):
    with CommandSuperGroup(__name__, cli_command_loader, 'vsts.cli.code.common.custom#{}') as sg:
        with sg.group('code') as g:
            # basic pr commands
            g.command('pr create', 'create_pull_request',
                      table_transformer=transform_pull_request_table_output)
            g.command('pr update', 'update_pull_request',
                      table_transformer=transform_pull_request_table_output)
            g.command('pr show', 'show_pull_request',
                      table_transformer=transform_pull_request_table_output)
            g.command('pr list', 'list_pull_requests',
                      table_transformer=transform_pull_requests_table_output)

            # pr status update commands
            g.command('pr complete', 'complete_pull_request',
                      table_transformer=transform_pull_request_table_output)
            g.command('pr abandon', 'abandon_pull_request',
                      table_transformer=transform_pull_request_table_output)
            g.command('pr reactivate', 'reactivate_pull_request',
                      table_transformer=transform_pull_request_table_output)

            # pr reviewer commands
            g.command('pr reviewers add', 'create_pull_request_reviewers',
                      table_transformer=transform_reviewers_table_output)
            g.command('pr reviewers list', 'list_pull_request_reviewers',
                      table_transformer=transform_reviewers_table_output)
            g.command('pr reviewers remove', 'delete_pull_request_reviewers',
                      table_transformer=transform_reviewers_table_output)

            # pr work item commands
            g.command('pr work-items add', 'add_pull_request_work_items',
                      table_transformer=transform_work_items_table_output)
            g.command('pr work-items list', 'list_pull_request_work_items',
                      table_transformer=transform_work_items_table_output)
            g.command('pr work-items remove', 'remove_pull_request_work_items',
                      table_transformer=transform_work_items_table_output)

            # pr set-vote commands
            g.command('pr set-vote', 'vote_pull_request', table_transformer=transform_reviewer_table_output)

            # pr policy commands
            g.command('pr policies list', 'list_pr_policies', table_transformer=transform_policies_table_output)
            g.command('pr policies queue', 'queue_pr_policy', table_transformer=transform_policy_table_output)

            # git alias commands
            g.command('setup-git-aliases', 'setup_git_aliases')
