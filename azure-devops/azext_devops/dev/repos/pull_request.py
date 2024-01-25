# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import webbrowser

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.devops_sdk.exceptions import AzureDevOpsClientRequestError
from azext_devops.devops_sdk.v5_0.git.models import (GitPullRequest, GitPullRequestCompletionOptions,
                                                     GitPullRequestSearchCriteria, IdentityRef, IdentityRefWithVote,
                                                     ResourceRef, GitRefFavorite, WebApiTagDefinition)
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import JsonPatchOperation, WorkItemRelation
from azext_devops.dev.common.arguments import should_detect
from azext_devops.dev.common.git import get_current_branch_name, resolve_git_ref_heads, fetch_remote_and_checkout
from azext_devops.dev.common.identities import ME, resolve_identity_as_id
from azext_devops.dev.common.uri import uri_quote
from azext_devops.dev.common.uuid import EMPTY_UUID
from azext_devops.dev.common.services import (get_git_client,
                                              get_policy_client,
                                              get_work_item_tracking_client,
                                              resolve_instance,
                                              resolve_instance_project_and_repo,
                                              get_vsts_info_from_current_remote_url)

logger = get_logger(__name__)


def show_pull_request(id, open=False, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Get the details of a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param open: Open the pull request in your web browser.
    :type open: bool
    :rtype: :class:`GitPullRequest <v5_0.git.models.GitPullRequest>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    pr = client.get_pull_request(project=pr.repository.project.id,
                                 repository_id=pr.repository.id,
                                 pull_request_id=id,
                                 include_commits=False,
                                 include_work_item_refs=True)
    if open:
        _open_pull_request(pr, organization)
    return pr


def list_pull_requests(repository=None, creator=None, include_links=False, reviewer=None,
                       source_branch=None, status=None, target_branch=None, project=None,
                       skip=None, top=None, organization=None, detect=None):
    """List pull requests.
    :param repository: Name or ID of the repository.
    :type repository: str
    :param creator: Limit results to pull requests created by this user.
    :type creator: str
    :param include_links: Include _links for each pull request.
    :type include_links: bool
    :param reviewer: Limit results to pull requests where this user is a reviewer.
    :type reviewer: str
    :param source_branch: Limit results to pull requests that originate from this source branch.
    :type source_branch: str
    :param status: Limit results to pull requests with this status.
    :type status: str
    :param target_branch: Limit results to pull requests that target this branch.
    :type target_branch: str
    :param skip: Number of pull requests to skip.
    :type skip: int
    :param top: Maximum number of pull requests to list.
    :type top: int
    :rtype: list of :class:`VssJsonCollectionWrapper <v5_0.git.models.VssJsonCollectionWrapper>`
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect,
        organization=organization,
        project=project,
        repo=repository)
    search_criteria = GitPullRequestSearchCriteria(
        creator_id=resolve_identity_as_id(creator, organization),
        include_links=include_links,
        reviewer_id=resolve_identity_as_id(reviewer, organization),
        source_ref_name=resolve_git_ref_heads(source_branch),
        status=status,
        target_ref_name=resolve_git_ref_heads(target_branch))
    client = get_git_client(organization)
    if repository is None:
        pr_list = client.get_pull_requests_by_project(project=project, search_criteria=search_criteria,
                                                      skip=skip, top=top)
    else:
        pr_list = client.get_pull_requests(project=project, repository_id=repository,
                                           search_criteria=search_criteria,
                                           skip=skip, top=top)
    return pr_list


# pylint: disable=too-many-statements, too-many-locals, redefined-builtin
def create_pull_request(project=None, repository=None, source_branch=None, target_branch=None,
                        title=None, description=None, auto_complete=False, squash=False,
                        delete_source_branch=False, bypass_policy=False, bypass_policy_reason=None,
                        merge_commit_message=None, optional_reviewers=None, required_reviewers=None ,work_items=None, draft=None,
                        open=False, organization=None, detect=None, transition_work_items=False,
                        labels=None):  # pylint: disable=redefined-builtin
    """Create a pull request.
    :param project: Name or ID of the team project.
    :type project: str
    :param repository: Name or ID of the repository to create the pull request in.
    :type repository: str
    :param source_branch: Name of the source branch. Example: "dev".
    :type source_branch: str
    :param target_branch: Name of the target branch. If not specified, defaults to the
                          default branch of the target repository.
    :type target_branch: str
    :param title: Title for the new pull request.
    :type title: str
    :param draft: Use this flag to create the pull request in draft/work in progress mode.
    :type draft: bool
    :param description: Description for the new pull request. Can include markdown.
                        Each value sent to this arg will be a new line.
                        For example: --description "First Line" "Second Line"
    :type description: list of str
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
    :param bypass_policy_reason: Reason for bypassing the required policies.
    :type bypass_policy_reason: str
    :param merge_commit_message: Message displayed when commits are merged.
    :type merge_commit_message: str
    :param optional_reviewers: Additional users or groups to include as optional reviewers on the new pull request.
                      Space separated.
    :type optional_reviewers: list of str
    :param required_reviewers: Additional users or groups to include as required reviewers on the new pull request.
                      Space separated.
    :type required_reviewers: list of str
    :param work_items: IDs of the work items to link to the new pull request. Space separated.
    :type work_items: list of str
    :param open: Open the pull request in your web browser.
    :type open: bool
    :param transition_work_items: Transition any work items linked to the pull request into the next logical state.
                   (e.g. Active -> Resolved)
    :type transition_work_items: bool
    :param labels: The labels associated with the pull request. Space separated.
    :type labels: list of str
    :rtype: :class:`GitPullRequest <v5_0.git.models.GitPullRequest>`
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect,
        organization=organization,
        project=project,
        repo=repository)
    source_branch, target_branch = _get_branches_for_pull_request(
        organization, project, repository, source_branch, target_branch, detect)
    client = get_git_client(organization)
    multi_line_description = None
    if description is not None:
        multi_line_description = '\n'.join(description)
    if labels is not None:
        labels = [WebApiTagDefinition(name=label) for label in labels.split(' ')]
    pr = GitPullRequest(description=multi_line_description,
                        source_ref_name=source_branch,
                        target_ref_name=target_branch,
                        labels=labels)
    if draft is not None:
        pr.is_draft = draft
    if title is not None:
        pr.title = title
    else:
        pr.title = 'Merge ' + source_branch + ' to ' + target_branch
    pr.source_ref_name = resolve_git_ref_heads(source_branch)
    pr.target_ref_name = resolve_git_ref_heads(target_branch)
    if pr.source_ref_name == pr.target_ref_name:
        raise CLIError('The source branch, "{}", can not be the same as the target branch.'.format
                       (pr.source_ref_name))

    if optional_reviewers is not None:
        optional_reviewers = list(set(x.lower() for x in optional_reviewers))
        optional_reviewers = _resolve_reviewers_as_refs(optional_reviewers, organization)
    else:
        optional_reviewers = []

    if required_reviewers is not None:
        required_reviewers = list(set(x.lower() for x in required_reviewers))
        required_reviewers = _resolve_reviewers_as_refs(required_reviewers, organization)
    else:
        required_reviewers = []

    for required_reviewer in required_reviewers:
        required_reviewer.is_required = True

        # remove duplicates by id, duplicated will only be required only
        for optional_reviewer in optional_reviewers[:]:
            if optional_reviewer.id == required_reviewer.id:
                optional_reviewers.remove(optional_reviewer)

    reviewers = [*optional_reviewers, *required_reviewers]

    if len(reviewers) > 0:
        pr.reviewers = reviewers
    
    if work_items is not None and work_items:
        resolved_work_items = []
        for work_item in work_items:
            resolved_work_items.append(ResourceRef(id=work_item))
        pr.work_item_refs = resolved_work_items
    pr = client.create_pull_request(git_pull_request_to_create=pr, project=project,
                                    repository_id=repository)
    # if title or description are not provided and there is a single commit, we will
    # use the its comment to populate the not-provided field(s).
    # the first line of the commit comment is used for title and all lines of the
    # comment are used for description.
    title_from_commit = None
    description_from_commit = None
    if (title is None) or (description is None):
        commits = client.get_pull_request_commits(repository_id=repository, pull_request_id=pr.pull_request_id,
                                                  project=project)
        if len(commits) == 1:
            commit_details = client.get_commit(commit_id=commits[0].commit_id, repository_id=repository,
                                               project=project, change_count=0)
            first_commit_comment = commit_details.comment

            if first_commit_comment:
                # when title is not specified, use the first line of first commit comment as PR title
                if title is None:
                    title_from_commit = first_commit_comment.split("\n")[0]
                # when description is not specified, use the entire commit comment as PR description
                if description is None:
                    description_from_commit = first_commit_comment
    set_completion_options = (bypass_policy or
                              bypass_policy_reason is not None or
                              squash or
                              merge_commit_message is not None or
                              delete_source_branch or
                              transition_work_items)
    if auto_complete or set_completion_options or title_from_commit is not None or description_from_commit is not None:
        pr_for_update = GitPullRequest()
        if auto_complete:
            # auto-complete will not get set on create, so a subsequent update is required.
            pr_for_update.auto_complete_set_by = IdentityRef(id=resolve_identity_as_id(ME, organization))
        if set_completion_options:
            completion_options = GitPullRequestCompletionOptions()
            completion_options.bypass_policy = bypass_policy
            completion_options.bypass_reason = bypass_policy_reason
            completion_options.delete_source_branch = delete_source_branch
            completion_options.squash_merge = squash
            completion_options.merge_commit_message = merge_commit_message
            completion_options.transition_work_items = transition_work_items
            pr_for_update.completion_options = completion_options
        if title_from_commit is not None:
            pr_for_update.title = title_from_commit
        if description_from_commit is not None:
            pr_for_update.description = description_from_commit
        pr = client.update_pull_request(git_pull_request_to_update=pr_for_update,
                                        project=pr.repository.project.id,
                                        repository_id=pr.repository.id,
                                        pull_request_id=pr.pull_request_id)
    if open:
        _open_pull_request(pr, organization)
    return pr


def _get_branches_for_pull_request(organization, project, repository, source_branch, target_branch, detect):
    if should_detect(detect):
        if source_branch is None:
            source_branch = get_current_branch_name()
            if source_branch is None:
                raise ValueError('The source branch could not be detected,'
                                 'please provide the --source-branch argument.')
    else:
        if source_branch is None:
            raise ValueError('--source-branch is a required argument.')
    if target_branch is None:
        if project is not None and repository is not None:
            target_branch = _get_default_branch(organization, project, repository)
        if target_branch is None:
            raise ValueError('The target branch could not be detected,'
                             'please provide the --target-branch argument.')
    return source_branch, target_branch


def update_pull_request(id, title=None, description=None, auto_complete=None,  # pylint: disable=redefined-builtin
                        squash=None, delete_source_branch=None, bypass_policy=None, draft=None,
                        bypass_policy_reason=None, merge_commit_message=None, organization=None, detect=None,
                        transition_work_items=None, status=None):
    """Update a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param title: New title for the pull request.
    :type title: str
    :param description: New description for the pull request.  Can include markdown.  Each value sent to this
                        arg will be a new line. For example: --description "First Line" "Second Line"
    :type description: list of str
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
    :param bypass_policy_reason: Reason for bypassing the required policies.
    :type bypass_policy_reason: str
    :param draft: Publish the PR or convert to draft mode.
    :type draft: bool
    :param merge_commit_message: Message displayed when commits are merged.
    :type merge_commit_message: str
    :param transition_work_items: Transition any work items linked to the pull request into the next logical state.
                   (e.g. Active -> Resolved)
    :type transition_work_items: bool
    :param status: Set the new state of pull request.
    :type status: str
    :rtype: :class:`GitPullRequest <v5_0.git.models.GitPullRequest>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    existing_pr = client.get_pull_request_by_id(id)
    if description is not None:
        multi_line_description = '\n'.join(description)
    else:
        multi_line_description = None
    pr = GitPullRequest(title=title, description=multi_line_description)
    if (bypass_policy is not None or   # pylint: disable=too-many-boolean-expressions
            bypass_policy_reason is not None or
            squash is not None or
            merge_commit_message is not None or
            delete_source_branch is not None or
            transition_work_items is not None):
        completion_options = existing_pr.completion_options
        if completion_options is None:
            completion_options = GitPullRequestCompletionOptions()
        if bypass_policy is not None:
            completion_options.bypass_policy = bypass_policy
        if bypass_policy_reason is not None:
            completion_options.bypass_reason = bypass_policy_reason
        if delete_source_branch is not None:
            completion_options.delete_source_branch = delete_source_branch
        if squash is not None:
            completion_options.squash_merge = squash
        if merge_commit_message is not None:
            completion_options.merge_commit_message = merge_commit_message
        if transition_work_items is not None:
            completion_options.transition_work_items = transition_work_items
        pr.completion_options = completion_options
    if auto_complete is not None:
        if auto_complete:
            pr.auto_complete_set_by = IdentityRef(id=resolve_identity_as_id(ME, organization))
        else:
            pr.auto_complete_set_by = IdentityRef(id=EMPTY_UUID)
    if draft is not None:
        pr.is_draft = draft
    if status is not None:
        pr.status = status
        if status == 'completed':
            pr.last_merge_source_commit = existing_pr.last_merge_source_commit
            if not pr.completion_options:
                pr.completion_options = existing_pr.completion_options
    pr = client.update_pull_request(git_pull_request_to_update=pr,
                                    project=existing_pr.repository.project.name,
                                    repository_id=existing_pr.repository.name,
                                    pull_request_id=id)
    return pr


def create_pull_request_reviewers(id, reviewers, organization=None, detect=None, required=None):  # pylint: disable=redefined-builtin
    """Add one or more reviewers to a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param reviewers: Users or groups to include as reviewers on a pull request. Space separated.
    :type reviewers: list of str
    :param required: Make the reviewers required.
    :type reviewers: bool
    :rtype: list of :class:`IdentityRefWithVote <v5_0.git.models.IdentityRefWithVote>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    resolved_reviewers = _resolve_reviewers_as_refs(reviewers, organization)
    
    if required:
        for reviewer in resolved_reviewers:
            reviewer.is_required = True
    
    identities = client.create_pull_request_reviewers(reviewers=resolved_reviewers,
                                                      project=pr.repository.project.id,
                                                      repository_id=pr.repository.id,
                                                      pull_request_id=id)
    return identities


def delete_pull_request_reviewers(id, reviewers, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Remove one or more reviewers from a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param reviewers: Users or groups to remove as reviewers on a pull request. Space separated.
    :type reviewers: list of str
    :rtype: list of :class:`IdentityRefWithVote <v5_0.git.models.IdentityRefWithVote>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    resolved_reviewers = _resolve_reviewers_as_ids(reviewers, organization)
    for reviewer in resolved_reviewers:
        client.delete_pull_request_reviewer(project=pr.repository.project.id,
                                            repository_id=pr.repository.id,
                                            pull_request_id=id,
                                            reviewer_id=reviewer)
    return client.get_pull_request_reviewers(project=pr.repository.project.id,
                                             repository_id=pr.repository.id,
                                             pull_request_id=id)


def list_pull_request_reviewers(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """List reviewers of a pull request.
    :param id: ID of the pull request.
    :type id: int
    :rtype: list of :class:`IdentityRefWithVote <v5_0.git.models.IdentityRefWithVote>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    return client.get_pull_request_reviewers(project=pr.repository.project.id,
                                             repository_id=pr.repository.id,
                                             pull_request_id=id)


def add_pull_request_work_items(id, work_items, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Link one or more work items to a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param work_items: IDs of the work items to link. Space separated.
    :type work_items: list of int
    :rtype: list of :class:`AssociatedWorkItem <v5_0.git.models.AssociatedWorkItem>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    existing_pr = client.get_pull_request_by_id(id)
    if work_items is not None and work_items:
        work_items = list(set(work_items))  # make distinct
        wit_client = get_work_item_tracking_client(organization)
        pr_url = 'vstfs:///Git/PullRequestId/{project}%2F{repo}%2F{id}'.format(
            project=existing_pr.repository.project.id, repo=existing_pr.repository.id, id=id)
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
            except AzureDevOpsClientRequestError as ex:
                logger.debug(ex, exc_info=True)
                message = ex.args[0]
                if message != 'Relation already exists.':
                    raise CLIError(ex)
        refs = client.get_pull_request_work_item_refs(project=existing_pr.repository.project.id,
                                                      repository_id=existing_pr.repository.id,
                                                      pull_request_id=id)
    ids = []
    for ref in refs:
        ids.append(ref.id)
    return wit_client.get_work_items(ids=ids)


def checkout(id, remote_name='origin'):  # pylint: disable=redefined-builtin
    """Checkout the PR source branch locally, if no local changes are present
    :param id: ID of the pull request.
    :type id: int
    :param remote_name: Name of git remote against which PR is raised
    :type remote_name: str
    """
    git_info = get_vsts_info_from_current_remote_url()
    organization = git_info.uri
    if not organization:
        raise CLIError('This command should be used from a valid Azure DevOps git repository only')

    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)

    # favorite the ref
    refFavoriteRequest = GitRefFavorite(name=pr.source_ref_name, repository_id=pr.repository.id, type=2)
    try:
        client.create_favorite(favorite=refFavoriteRequest, project=pr.repository.project.id)
    except Exception as ex:  # pylint: disable=broad-except
        if 'is already a favorite for user' not in str(ex):
            raise ex

    fetch_remote_and_checkout(pr.source_ref_name, remote_name)


def remove_pull_request_work_items(id, work_items, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Unlink one or more work items from a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param work_items: IDs of the work items to unlink. Space separated.
    :type work_items: list of int
    :rtype: list of :class:`AssociatedWorkItem <v5_0.git.models.AssociatedWorkItem>`
    """
    # pylint: disable=too-many-nested-blocks
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    existing_pr = client.get_pull_request_by_id(id)
    if work_items is not None and work_items:
        work_items = list(set(work_items))  # make distinct
        wit_client = get_work_item_tracking_client(organization)
        work_items_full = wit_client.get_work_items(ids=work_items, expand=1)
        if work_items_full:
            url = 'vstfs:///Git/PullRequestId/{project}%2F{repo}%2F{id}'.format(
                project=existing_pr.repository.project.id, repo=existing_pr.repository.id, id=id)
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
            refs = client.get_pull_request_work_item_refs(project=existing_pr.repository.project.id,
                                                          repository_id=existing_pr.repository.id,
                                                          pull_request_id=id)
            if refs:
                ids = []
                for ref in refs:
                    ids.append(ref.id)
                if ids:
                    return wit_client.get_work_items(ids=ids)
    return None


def list_pull_request_work_items(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """List linked work items for a pull request.
    :param id: ID of the pull request.
    :type id: int
    :rtype: list of :class:`AssociatedWorkItem <v5_0.git.models.AssociatedWorkItem>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    refs = client.get_pull_request_work_item_refs(project=pr.repository.project.id,
                                                  repository_id=pr.repository.id,
                                                  pull_request_id=id)
    if refs:
        ids = []
        for ref in refs:
            ids.append(ref.id)
        wit_client = get_work_item_tracking_client(organization)
        return wit_client.get_work_items(ids=ids)

    return refs


def vote_pull_request(id, vote, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Vote on a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param vote: New vote value for the pull request.
    :type vote: int
    :rtype: :class:`IdentityRefWithVote <v5_0.git.models.IdentityRefWithVote>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_git_client(organization)
    pr = client.get_pull_request_by_id(id)
    resolved_reviewer = IdentityRefWithVote(id=resolve_identity_as_id(ME, organization))
    resolved_reviewer.vote = _convert_vote_to_int(vote)
    created_reviewer = client.create_pull_request_reviewer(project=pr.repository.project.id,
                                                           repository_id=pr.repository.id,
                                                           pull_request_id=id,
                                                           reviewer_id=resolved_reviewer.id,
                                                           reviewer=resolved_reviewer)
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


def list_pr_policies(id, organization=None, detect=None, top=None, skip=None):  # pylint: disable=redefined-builtin
    """List policies of a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param top: Maximum number of policies to list.
    :type top: int
    :param skip: Number of policies to skip.
    :type skip: int
    :rtype: list of :class:`PolicyEvaluationRecord <policy.v4_0.models.PolicyEvaluationRecord>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    git_client = get_git_client(organization)
    pr = git_client.get_pull_request_by_id(id)
    policy_client = get_policy_client(organization)
    artifact_id = "vstfs:///CodeReview/CodeReviewId/{project_id}/{pull_request_id}".format(
        project_id=pr.repository.project.id, pull_request_id=id)
    return policy_client.get_policy_evaluations(project=pr.repository.project.id,
                                                artifact_id=artifact_id,
                                                top=top,
                                                skip=skip)


def queue_pr_policy(id, evaluation_id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Queue an evaluation of a policy for a pull request.
    :param id: ID of the pull request.
    :type id: int
    :param evaluation_id: ID of the policy evaluation to queue.
    :type evaluation_id: str
    :rtype: :class:`PolicyEvaluationRecord <policy.v4_0.models.PolicyEvaluationRecord>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    git_client = get_git_client(organization)
    pr = git_client.get_pull_request_by_id(id)
    policy_client = get_policy_client(organization)
    return policy_client.requeue_policy_evaluation(project=pr.repository.project.id,
                                                   evaluation_id=evaluation_id)


def _resolve_reviewers_as_refs(reviewers, organization):
    """Takes a list containing identity names, emails, and ids,
    and return a list of IdentityRefWithVote objects.
    :rtype: list of :class:`IdentityRefWithVote <v5_0.git.models.IdentityRefWithVote>`
    """
    resolved_reviewers = None
    if reviewers is not None and reviewers:
        resolved_reviewers = []
        for reviewer in reviewers:
            resolved_reviewers.append(IdentityRefWithVote(id=resolve_identity_as_id(reviewer, organization)))
    return resolved_reviewers


def _resolve_reviewers_as_ids(reviewers, organization):
    """Takes a list containing identity names, emails, and ids,
    and returns a list of IdentityRefWithVote objects.
    """
    resolved_reviewers = None
    if reviewers is not None and reviewers:
        resolved_reviewers = []
        for reviewer in reviewers:
            resolved_reviewers.append(resolve_identity_as_id(reviewer, organization))
    return resolved_reviewers


def _open_pull_request(pull_request, organization):
    """Opens the pull request in the default browser.
    :param pull_request: The pull request to open.
    :type pull_request: str
    """
    url = organization.rstrip('/') + '/' + uri_quote(pull_request.repository.project.name)\
        + '/_git/' + uri_quote(pull_request.repository.name) + '/pullrequest/'\
        + str(pull_request.pull_request_id)
    webbrowser.open_new(url=url)


def _get_default_branch(organization, project, repository):
    client = get_git_client(organization)
    repo = client.get_repository(project=project, repository_id=repository)
    return repo.default_branch
