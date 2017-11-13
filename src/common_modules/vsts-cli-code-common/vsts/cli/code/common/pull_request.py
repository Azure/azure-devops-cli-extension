# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import webbrowser

from knack.util import CLIError
from vsts.exceptions import VstsClientRequestError
from vsts.git.v4_0.models.git_pull_request import GitPullRequest
from vsts.git.v4_0.models.git_pull_request_completion_options import GitPullRequestCompletionOptions
from vsts.git.v4_0.models.git_pull_request_search_criteria import GitPullRequestSearchCriteria
from vsts.git.v4_0.models.identity_ref import IdentityRef
from vsts.git.v4_0.models.identity_ref_with_vote import IdentityRefWithVote
from vsts.git.v4_0.models.resource_ref import ResourceRef
from vsts.work_item_tracking.v4_0.models.json_patch_operation import JsonPatchOperation
from vsts.work_item_tracking.v4_0.models.work_item_relation import WorkItemRelation
from vsts.cli.common.arguments import resolve_on_off_switch, should_detect
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.git import get_current_branch_name, resolve_git_ref_heads, setup_git_alias
from vsts.cli.common.identities import ME, resolve_identity_as_id
from vsts.cli.common.uri import uri_quote
from vsts.cli.common.uuid import EMPTY_UUID
from vsts.cli.common.services import (get_git_client,
                                      get_policy_client,
                                      get_work_item_tracking_client,
                                      resolve_instance,
                                      resolve_instance_project_and_repo)


def show_pull_request(pull_request_id, open_browser=False, team_instance=None, detect=None):
    """Show details for a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param open_browser: Open the pull request in the default web browser.
    :type open_browser: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        pr = client.get_pull_request(project=pr.repository.project.id,
                                     repository_id=pr.repository.id,
                                     pull_request_id=pull_request_id,
                                     include_commits=False,
                                     include_work_item_refs=True)
        if open_browser:
            _open_pull_request(pr, team_instance)
        return pr
    except Exception as ex:
        handle_command_exception(ex)


def list_pull_requests(repository=None, creator=None, include_links=False, reviewer=None,
                       source_branch=None, status=None, target_branch=None, project=None,
                       skip=None, top=None, team_instance=None, detect=None):
    """List pull requests.
    :param repository: Name or ID of the repository.
    :type repository: str
    :param creator: Limit results to pull requests created by this user.
    :type creator: str
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param reviewer: Limit results to pull requests where this user is a reviewer.
    :type reviewer: str
    :param source_branch: Limit results to pull requests originating from this source branch.
    :type source_branch: str
    :param status: Limit results to pull requests with this status.
    :type status: str
    :param target_branch: Limit results to pull requests that target this branch.
    :type target_branch: str
    :param project: Name or ID of the project.
    :type project: str
    :param skip: Number of results to skip.
    :type skip: int
    :param top: Maximum number of results to list.
    :type top: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`VssJsonCollectionWrapper <git.v4_0.models.VssJsonCollectionWrapper>`
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                               team_instance=team_instance,
                                                                               project=project,
                                                                               repo=repository)
        search_criteria = GitPullRequestSearchCriteria(creator_id=resolve_identity_as_id(creator, team_instance),
                                                       include_links=include_links,
                                                       reviewer_id=resolve_identity_as_id(reviewer, team_instance),
                                                       source_ref_name=resolve_git_ref_heads(source_branch),
                                                       status=status,
                                                       target_ref_name=resolve_git_ref_heads(target_branch))
        client = get_git_client(team_instance)
        if repository is None:
            pr_list = client.get_pull_requests_by_project(project=project, search_criteria=search_criteria,
                                                          skip=skip, top=top)
        else:
            pr_list = client.get_pull_requests(project=project, repository_id=repository,
                                               search_criteria=search_criteria,
                                               skip=skip, top=top)
    except Exception as ex:
        handle_command_exception(ex)
    return pr_list


def create_pull_request(project=None, repository=None, source_branch=None, target_branch=None,
                        title=None, description=None, auto_complete=False, squash=False,
                        delete_source_branch=False, bypass_policy=False, bypass_policy_reason=None,
                        merge_commit_message=None, reviewers=None, work_items=None,
                        open_browser=False, team_instance=None, detect=None):
    """Create a new pull request.
    :param project: Name or ID of the team project.
    :type project: str
    :param repository: Name or ID of the repository to create the pull request in.
    :type repository: str
    :param source_branch: Name of the source branch.
    :type source_branch: str
    :param target_branch: Name of the target branch. Defaults to the default branch of the target
                          repository if not specified.
    :type target_branch: str
    :param title: Short title for the new pull request.
    :type title: str
    :param description: Longer description for the new pull request. Can include markdown.
    :type description: str
    :param auto_complete: Set the pull request to complete automatically when all policies have passed and
                          the source branch can be merged into the target branch.
    :type auto_complete: bool
    :param squash: Squash the commits in the source branch when merging into the target branch.
    :type squash: bool
    :param delete_source_branch: Delete the source branch after the pull request has been completed
                                 and merged into the target branch.
    :type delete_source_branch: bool
    :param bypass_policy: Bypass required policies (if any) and completes the pull request once it
                          can be merged.
    :type bypass_policy: bool
    :param bypass_policy_reason: Justification for bypassing the required policies.
    :type bypass_policy_reason: str
    :param merge_commit_message: Message displayed when commits are merged.
    :type merge_commit_message: str
    :param reviewers: Additional users or groups to include as reviewers for the new pull request.
                      Space separated.
    :type reviewers: list of str
    :param work_items: Work items to link to the new pull request.
    :type work_items: list of str
    :param open_browser: Open the pull request in the default web browser after it has been created.
    :type open_browser: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                               team_instance=team_instance,
                                                                               project=project,
                                                                               repo=repository)
        if should_detect(detect):
            if source_branch is None:
                source_branch = get_current_branch_name()
                if source_branch is None:
                    raise ValueError('The source branch could not be detected, please '
                                     + 'provide the --source-branch argument.')
            if target_branch is None:
                if project is not None:
                    target_branch = _get_default_branch(team_instance, project, repository)
                if target_branch is None:
                    raise ValueError('The target branch could not be detected, please '
                                     + 'provide the --target-branch argument.')
        else:
            if source_branch is None:
                raise ValueError('--source-branch is a required argument.')
            if target_branch is None:
                raise ValueError('--target-branch is a required argument.')
        client = get_git_client(team_instance)
        pr = GitPullRequest(description=description, source_ref_name=source_branch,
                            target_ref_name=target_branch)
        if title is not None:
            pr.title = title
        else:
            pr.title = 'Merge ' + source_branch + ' to ' + target_branch
        pr.source_ref_name = resolve_git_ref_heads(source_branch)
        pr.target_ref_name = resolve_git_ref_heads(target_branch)
        if pr.source_ref_name == pr.target_ref_name:
            raise CLIError('The source branch, "{}", can not be the same as the target branch.'.format
                           (pr.source_ref_name))
        pr.reviewers = _resolve_reviewers_as_refs(reviewers, team_instance)
        if work_items is not None and len(work_items) > 0:
            resolved_work_items = []
            for work_item in work_items:
                resolved_work_items.append(ResourceRef(id=work_item))
            pr.work_item_refs = resolved_work_items
        pr = client.create_pull_request(git_pull_request_to_create=pr, project=project,
                                        repository_id=repository)
        title_from_commit = None
        if title is None:
            # if title wasn't specified and only one commit, we will set the PR title to the comment of that commit
            commits = client.get_pull_request_commits(repository_id=repository, pull_request_id=pr.pull_request_id,
                                                      project=project)
            if len(commits) == 1:
                title_from_commit = commits[0].comment
        set_completion_options = (bypass_policy is not None or bypass_policy_reason is not None
                                  or bypass_policy or squash or merge_commit_message is not None
                                  or delete_source_branch)
        if auto_complete or set_completion_options or title_from_commit is not None:
            pr_for_update = GitPullRequest()
            if auto_complete:
                # auto-complete will not get set on create, so a subsequent update is required.
                pr_for_update.auto_complete_set_by = IdentityRef(id=resolve_identity_as_id(ME, team_instance))
            if set_completion_options:
                completion_options = GitPullRequestCompletionOptions()
                completion_options.bypass_policy = bypass_policy
                completion_options.bypass_reason = bypass_policy_reason
                completion_options.delete_source_branch = delete_source_branch
                completion_options.squash_merge = squash
                completion_options.merge_commit_message = merge_commit_message
                pr_for_update.completion_options = completion_options
            if title_from_commit is not None:
                pr_for_update.title = title_from_commit
            pr = client.update_pull_request(git_pull_request_to_update=pr_for_update,
                                            project=pr.repository.project.id,
                                            repository_id=pr.repository.id,
                                            pull_request_id=pr.pull_request_id)
        if open_browser:
            _open_pull_request(pr, team_instance)
    except Exception as ex:
        handle_command_exception(ex)
    return pr


def update_pull_request(pull_request_id, title=None, description=None, auto_complete=None,
                        squash=None, delete_source_branch=None, bypass_policy=None,
                        bypass_policy_reason=None, merge_commit_message=None, team_instance=None, detect=None):
    """Update a pull request.
    :param pull_request_id: The ID of the pull request to update
    :type pull_request_id: int
    :param title: New title for the pull request.
    :type title: str
    :param description: New description for the pull request.
    :type description: str
    :param auto_complete: Set the pull request to complete automatically when all policies have passed and
                          the source branch can be merged into the target branch.
    :type auto_complete: str
    :param squash: Squash the commits in the source branch when merging into the target branch.
    :type squash: str
    :param delete_source_branch: Delete the source branch after the pull request has been completed
                                 and merged into the target branch.
    :type delete_source_branch: str
    :param bypass_policy: Bypass required policies (if any) and completes the pull request once it
                          can be merged.
    :type bypass_policy: str
    :param bypass_policy_reason: Justification for bypassing the required policies.
    :type bypass_policy_reason: str
    :param merge_commit_message: Message displayed when commits are merged.
    :type merge_commit_message: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        existing_pr = client.get_pull_request_by_id(pull_request_id)
        pr = GitPullRequest(title=title, description=description)
        if (bypass_policy is not None or bypass_policy_reason is not None or
            bypass_policy is not None or squash is not None or merge_commit_message
                is not None or delete_source_branch is not None):
            completion_options = existing_pr.completion_options
            if completion_options is None:
                completion_options = GitPullRequestCompletionOptions()
            if bypass_policy is not None:
                completion_options.bypass_policy = resolve_on_off_switch(bypass_policy)
            if bypass_policy_reason is not None:
                completion_options.bypass_reason = bypass_policy_reason
            if delete_source_branch is not None:
                completion_options.delete_source_branch = resolve_on_off_switch(delete_source_branch)
            if squash is not None:
                completion_options.squash_merge = resolve_on_off_switch(squash)
            if merge_commit_message is not None:
                completion_options.merge_commit_message = merge_commit_message
            pr.completion_options = completion_options
        if auto_complete is not None:
            if resolve_on_off_switch(auto_complete):
                pr.auto_complete_set_by = IdentityRef(id=resolve_identity_as_id(ME, team_instance))
            else:
                pr.auto_complete_set_by = IdentityRef(id=EMPTY_UUID)
        pr = client.update_pull_request(git_pull_request_to_update=pr,
                                        project=existing_pr.repository.project.name,
                                        repository_id=existing_pr.repository.name,
                                        pull_request_id=pull_request_id)
    except Exception as ex:
        handle_command_exception(ex)
    return pr


def complete_pull_request(pull_request_id, team_instance=None, detect=None):
    """Complete a pull request.
    :param pull_request_id: The ID of the pull request to complete.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    return _update_pull_request_status(pull_request_id=pull_request_id, new_status='completed',
                                       team_instance=team_instance, detect=detect)


def abandon_pull_request(pull_request_id, team_instance=None, detect=None):
    """Abandon a pull request.
    :param pull_request_id: The ID of the pull request to abandon.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    return _update_pull_request_status(pull_request_id=pull_request_id, new_status='abandoned',
                                       team_instance=team_instance, detect=detect)


def reactivate_pull_request(pull_request_id, team_instance=None, detect=None):
    """Reactivate an abandoned pull request.
    :param pull_request_id: The ID of the pull request to reactivate.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`GitPullRequest <git.v4_0.models.GitPullRequest>`
    """
    return _update_pull_request_status(pull_request_id=pull_request_id, new_status='active',
                                       team_instance=team_instance, detect=detect)


def create_pull_request_reviewers(pull_request_id, reviewers, team_instance=None, detect=None):
    """Adds reviewers to a git pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param reviewers: Users or groups to include as reviewers on a pull request. Space separated.
    :type reviewers: list of str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        resolved_reviewers = _resolve_reviewers_as_refs(reviewers, team_instance)
        identities = client.create_pull_request_reviewers(reviewers=resolved_reviewers,
                                                          project=pr.repository.project.id,
                                                          repository_id=pr.repository.id,
                                                          pull_request_id=pull_request_id)
    except Exception as ex:
        handle_command_exception(ex)
    return identities


def delete_pull_request_reviewers(pull_request_id, reviewers, team_instance=None, detect=None):
    """Remove reviewers from a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param reviewers: Users or groups to remove as reviewers on a pull request. Space separated.
    :type reviewers: list of str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        resolved_reviewers = _resolve_reviewers_as_ids(reviewers, team_instance)
        for reviewer in resolved_reviewers:
            client.delete_pull_request_reviewer(project=pr.repository.project.id,
                                                repository_id=pr.repository.id,
                                                pull_request_id=pull_request_id,
                                                reviewer_id=reviewer)
        return client.get_pull_request_reviewers(project=pr.repository.project.id,
                                                 repository_id=pr.repository.id,
                                                 pull_request_id=pull_request_id)
    except Exception as ex:
        handle_command_exception(ex)


def list_pull_request_reviewers(pull_request_id, team_instance=None, detect=None):
    """List reviewers of a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        return client.get_pull_request_reviewers(project=pr.repository.project.id,
                                                 repository_id=pr.repository.id,
                                                 pull_request_id=pull_request_id)
    except Exception as ex:
        handle_command_exception(ex)


def add_pull_request_work_items(pull_request_id, work_items, team_instance=None, detect=None):
    """Add work items to a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param work_items: Work item IDs to link to a pull request. Space separated.
    :type work_items: list of int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`AssociatedWorkItem <git.v4_0.models.AssociatedWorkItem>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        existing_pr = client.get_pull_request_by_id(pull_request_id)
        if work_items is not None and len(work_items) > 0:
            work_items = list(set(work_items))  # make distinct
            wit_client = get_work_item_tracking_client(team_instance)
            pr_url = 'vstfs:///Git/PullRequestId/{project}%2F{repo}%2F{id}'.format(
                    project=existing_pr.repository.project.id, repo=existing_pr.repository.id, id=pull_request_id)
            for work_item_id in work_items:
                patch_document = []
                patch_operation = JsonPatchOperation()
                patch_operation.op = 0
                patch_operation.path = '/relations/-'
                patch_operation.value = WorkItemRelation()
                patch_operation.value.attributes = {'name': 'Pull Request'}
                patch_operation.value.rel = 'ArtifactLink'
                patch_operation.value.url = pr_url
                patch_document.append(patch_operation)
                try:
                    wit_client.update_work_item(document=patch_document, id=work_item_id)
                except VstsClientRequestError as ex:
                    logging.exception(ex)
                    message = ex.args[0]
                    if message != 'Relation already exists.':
                        raise CLIError(ex)
            refs = client.get_pull_request_work_items(project=existing_pr.repository.project.id,
                                                      repository_id=existing_pr.repository.id,
                                                      pull_request_id=pull_request_id)
        ids = []
        for ref in refs:
            ids.append(ref.id)
        return wit_client.get_work_items(ids=ids)
    except Exception as ex:
        handle_command_exception(ex)


def remove_pull_request_work_items(pull_request_id, work_items, team_instance=None, detect=None):
    """Remove work items from a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param work_items: Work item IDs to unlink from a pull request. Space separated.
    :type work_items: list of int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`AssociatedWorkItem <git.v4_0.models.AssociatedWorkItem>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        existing_pr = client.get_pull_request_by_id(pull_request_id)
        if work_items is not None and work_items:
            work_items = list(set(work_items))  # make distinct
            wit_client = get_work_item_tracking_client(team_instance)
            work_items_full = wit_client.get_work_items(ids=work_items, expand=1)
            if work_items_full:
                url = 'vstfs:///Git/PullRequestId/{project}%2F{repo}%2F{id}'.format(
                    project=existing_pr.repository.project.id, repo=existing_pr.repository.id, id=pull_request_id)
                for work_item in work_items_full:
                    if work_item.relations is not None:
                        index = 0
                        for relation in work_item.relations:
                            if relation.url == url:
                                patch_document = []

                                patch_test_operation = JsonPatchOperation()
                                patch_test_operation.op = 'test'
                                patch_test_operation.path = '/rev'
                                patch_test_operation.value = work_item.rev
                                patch_document.append(patch_test_operation)

                                patch_operation = JsonPatchOperation()
                                patch_operation.op = 1
                                patch_operation.path = '/relations/{index}'.format(index=index)
                                patch_document.append(patch_operation)

                                wit_client.update_work_item(document=patch_document, id=work_item.id)
                            else:
                                index += 1
                refs = client.get_pull_request_work_items(project=existing_pr.repository.project.id,
                                                          repository_id=existing_pr.repository.id,
                                                          pull_request_id=pull_request_id)
                if refs:
                    ids = []
                    for ref in refs:
                        ids.append(ref.id)
                    if ids:
                        return wit_client.get_work_items(ids=ids)
    except Exception as ex:
        handle_command_exception(ex)


def list_pull_request_work_items(pull_request_id, team_instance=None, detect=None):
    """List work items associated with pull requests.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`AssociatedWorkItem <git.v4_0.models.AssociatedWorkItem>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        refs = client.get_pull_request_work_items(project=pr.repository.project.id,
                                                  repository_id=pr.repository.id,
                                                  pull_request_id=pull_request_id)
        if refs:
            ids = []
            for ref in refs:
                ids.append(ref.id)
            wit_client = get_work_item_tracking_client(team_instance)
            return wit_client.get_work_items(ids=ids)
    except Exception as ex:
        handle_command_exception(ex)


def _update_pull_request_status(pull_request_id, new_status, team_instance=None, detect=None):
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        existing_pr = client.get_pull_request_by_id(pull_request_id)
        pr = GitPullRequest(status=new_status)
        if new_status == 'completed':
            pr.last_merge_source_commit = existing_pr.last_merge_source_commit
        pr = client.update_pull_request(git_pull_request_to_update=pr,
                                        project=existing_pr.repository.project.name,
                                        repository_id=existing_pr.repository.name,
                                        pull_request_id=pull_request_id)
    except Exception as ex:
        handle_command_exception(ex)
    return pr


def vote_pull_request(pull_request_id, vote, team_instance=None, detect=None):
    """Vote on a pull request.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param vote: The new vote value for the pull request.
    :type vote: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_git_client(team_instance)
        pr = client.get_pull_request_by_id(pull_request_id)
        resolved_reviewer = IdentityRefWithVote(id=resolve_identity_as_id(ME, team_instance))
        resolved_reviewer.vote = _convert_vote_to_int(vote)
        created_reviewer = client.create_pull_request_reviewer(project=pr.repository.project.id,
                                                               repository_id=pr.repository.id,
                                                               pull_request_id=pull_request_id,
                                                               reviewer_id=resolved_reviewer.id,
                                                               reviewer=resolved_reviewer)
    except Exception as ex:
        handle_command_exception(ex)
    return created_reviewer


def _convert_vote_to_int(vote):
    if vote.lower() == 'approve':
        return 10
    if vote.lower() == 'approve-with-suggestions':
        return 5
    if vote.lower() == 'reset':
        return 0
    if vote.lower() == 'wait-for-author':
        return -5
    if vote.lower() == 'reject':
        return -10
    raise CLIError('"{vote}" is an invalid value for a pull request vote.'.format(vote=vote))


def list_pr_policies(pull_request_id, team_instance=None, detect=None, top=None, skip=None):
    """List Pull request policies.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :param top: Maximum number of results to list.
    :type top: int
    :param skip: Number of results to skip.
    :type skip: int
    :rtype: list of :class:`PolicyEvaluationRecord <policy.v4_0.models.PolicyEvaluationRecord>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        git_client = get_git_client(team_instance)
        pr = git_client.get_pull_request_by_id(pull_request_id)
        policy_client = get_policy_client(team_instance)
        artifact_id = "vstfs:///CodeReview/CodeReviewId/{project_id}/{pull_request_id}".format(
                project_id=pr.repository.project.id, pull_request_id=pull_request_id)
        return policy_client.get_policy_evaluations(project=pr.repository.project.id,
                                                    artifact_id=artifact_id,
                                                    top=top,
                                                    skip=skip)
    except Exception as ex:
        handle_command_exception(ex)


def queue_pr_policy(pull_request_id, evaluation_id, team_instance=None, detect=None):
    """Queue a Pull request policy.
    :param pull_request_id: The ID of the pull request.
    :type pull_request_id: int
    :param evaluation_id: The evaluation ID of the policy to queue.
    :type evaluation_id: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`PolicyEvaluationRecord <policy.v4_0.models.PolicyEvaluationRecord>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        git_client = get_git_client(team_instance)
        pr = git_client.get_pull_request_by_id(pull_request_id)
        policy_client = get_policy_client(team_instance)
        return policy_client.requeue_policy_evaluation(project=pr.repository.project.id,
                                                       evaluation_id=evaluation_id)
    except Exception as ex:
        handle_command_exception(ex)


def _resolve_reviewers_as_refs(reviewers, team_instance):
    """Takes a list containing identity names, emails, and ids,
    and return a list of IdentityRefWithVote objects.
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :rtype: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """
    resolved_reviewers = None
    if reviewers is not None and reviewers:
        resolved_reviewers = []
        for reviewer in reviewers:
            resolved_reviewers.append(IdentityRefWithVote(id=resolve_identity_as_id(reviewer, team_instance)))
    return resolved_reviewers


def _resolve_reviewers_as_ids(reviewers, team_instance):
    """Takes a list containing identity names, emails, and ids,
    and returns a list of IdentityRefWithVote objects.
    """
    resolved_reviewers = None
    if reviewers is not None and reviewers:
        resolved_reviewers = []
        for reviewer in reviewers:
            resolved_reviewers.append(resolve_identity_as_id(reviewer, team_instance))
    return resolved_reviewers


def _open_pull_request(pull_request, team_instance):
    """Opens the pull request in the default browser.
    :param pull_request: The pull request to open.
    :type pull_request: str
    """
    url = team_instance.rstrip('/') + '/' + uri_quote(pull_request.repository.project.name)\
        + '/_git/' + uri_quote(pull_request.repository.name) + '/pullrequest/'\
        + str(pull_request.pull_request_id)
    webbrowser.open_new(url=url)


def _get_default_branch(team_instance, project, repository):
    client = get_git_client(team_instance)
    repo = client.get_repository(project=project, repository_id=repository)
    return repo.default_branch

