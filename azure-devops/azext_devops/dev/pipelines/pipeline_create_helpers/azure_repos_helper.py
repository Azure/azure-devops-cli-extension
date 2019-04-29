# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.prompting import prompt
from knack.util import CLIError
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.services import get_git_client


logger = get_logger(__name__)


def push_files_to_azure_repo(files, repo_name, branch, commit_to_branch, organization, project,
                             message="Set up CI with Azure Pipelines"):
    if commit_to_branch:
        _checkin_files_to_azure_repo(files, repo_name, branch, organization, project, message)
        return branch
    # pull request flow
    new_branch = get_new_azure_repo_branch(organization, project, repo_name, branch)
    _checkin_files_to_azure_repo(files, repo_name, new_branch, organization, project, message)
    pr = create_pull_request_azure_repo(
        organization=organization, project=project, repository=repo_name, source=new_branch, target=branch,
        message=message)
    print('Created a Pull Request - {url}'.format(url=pr.url))
    return new_branch


def get_new_azure_repo_branch(organization, project, repository, source):
    from azext_devops.dev.repos.ref import list_refs, create_ref
    # get source ref object id
    object_id = None
    branch = resolve_git_ref_heads(source)
    filter_str = branch[5:]  # remove 'refs' to use as filter
    refs_list = list_refs(filter=filter_str, repository=repository, organization=organization, project=project)
    for ref in refs_list:
        if ref.name == branch:
            object_id = ref.object_id
            break
    if not object_id:
        raise CLIError('Cannot fetch source branch details for branch {br}'.format(br=branch))
    # get valid branch name
    branch_is_valid = False
    while not branch_is_valid:
        new_branch = prompt(msg='Enter new branch name to create: ')
        try:
            create_ref('heads/' + new_branch, object_id, repository, organization, project)
            branch_is_valid = True
        except Exception:  # pylint: disable=broad-except
            logger.warning('Not a valid branch name.')
    return new_branch


def create_pull_request_azure_repo(organization, project, repository, source, target, message):
    from azext_devops.dev.repos.pull_request import create_pull_request
    pr = create_pull_request(project=project, repository=repository, source_branch=source, target_branch=target,
                             title=message, description=['Creating Azure Pipeline for the repository.'],
                             organization=organization)
    return pr


def _checkin_files_to_azure_repo(files, repo_name, branch, organization, project,
                                 message):
    if files:
        for file in files:
            _checkin_file_to_azure_repo(file.path, file.content, repo_name, branch, organization, project, message)
    else:
        raise CLIError("No files to checkin.")


def _checkin_file_to_azure_repo(path_to_commit, content, repo_name, branch,
                                organization, project, message):
    logger.warning('Checking in file %s in the Azure repo %s', path_to_commit, repo_name)
    message = message + ' [skip ci]'
    git_client = get_git_client(organization=organization)
    from azext_devops.devops_sdk.v5_0.git.models import GitPush, GitRefUpdate
    # Get base commit Id
    all_heads_refs = git_client.get_refs(repository_id=repo_name,
                                         project=project,
                                         filter='heads/')
    old_object_id = None
    for ref in all_heads_refs:
        if ref.name == resolve_git_ref_heads(branch):
            old_object_id = ref.object_id
    if not old_object_id:
        raise CLIError('Cannot checkin the file. Error in getting the commits info for {branch}'.format(branch=branch))

    push_object = GitPush()
    ref_update = GitRefUpdate()
    ref_update.name = resolve_git_ref_heads(branch)
    ref_update.old_object_id = old_object_id
    push_object.ref_updates = [ref_update]
    push_object.commits = _get_commits_object(path_to_commit, content, message)
    git_client.create_push(push=push_object, repository_id=repo_name, project=project)


def _get_commits_object(path_to_commit, content, message):
    return [
        {
            "comment": message,
            "changes": [
                {
                    "changeType": "add",
                    "item": {
                        "path": path_to_commit
                    },
                    "newContent": {
                        "content": content,
                        "contentType": "rawtext"
                    }
                }
            ]
        }
    ]
