# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import requests
from knack.log import get_logger
from knack.util import CLIError
from knack.prompting import prompt
from azext_devops.dev.common.git import resolve_git_ref_heads, get_branch_name_from_ref

logger = get_logger(__name__)

_HTTP_NOT_FOUND_STATUS = 404
_HTTP_SUCCESS_STATUS = 200

class Files:  # pylint: disable=too-few-public-methods
    def __init__(self, path, content):
        self.path = path
        self.content = content


def get_github_pat_token():
    from azext_devops.dev.common.github_credential_manager import GithubCredentialManager
    github_manager = GithubCredentialManager()
    return github_manager.get_token()


def get_github_repos_api_url(repo_id):
    return 'https://api.github.com/repos/' + repo_id


def push_files_github(files, repo_name, branch, commit_to_branch, message="Set up CI with Azure Pipelines"):
    if commit_to_branch:
        commit_files_to_github_branch(files, repo_name, branch, message)
        return branch
    # Pull request flow
    # Create Branch
    new_branch = create_github_branch(repo=repo_name, source=branch)
    # Commit files to branch
    commit_files_to_github_branch(files, repo_name, new_branch, message)
    # Create PR from new branch
    pr = create_pr_github(branch, new_branch, repo_name, message)
    print('Created a Pull Request - {url}'.format(url=pr['url']))
    return new_branch


def create_pr_github(branch, new_branch, repo_name, message):
    token = get_github_pat_token()
    create_pr_url = 'https://api.github.com/repos/{repo_id}/pulls'.format(repo_id=repo_name)
    create_pr_request_body = {
        "title": message,
        "head": new_branch,
        "base": branch
        }
    create_response = requests.post(url=create_pr_url, auth=('', token),
                                    json=create_pr_request_body, headers=get_application_json_header())
    if not create_response.status_code == 201:
        raise CLIError('Pull request creation failed. Error: ({err})'.format(err=create_response.reason))
    import json
    return json.loads(create_response.text)


def create_github_branch(repo, source):
    token = get_github_pat_token()
    # Validate new branch name is valid
    branch_is_valid = False
    while not branch_is_valid:
        new_branch = prompt(msg='Enter new branch name to create: ')
        if not get_github_branch(repo, new_branch):
            branch_is_valid = True
        else:
            logger.warning('Not a valid branch name.')
    # Get source branch ref
    ref_item = get_github_branch(repo, source)
    if not ref_item:
        raise CLIError('Branch ({branch}) does not exist.'.format(branch=source))
    source_ref = ref_item['object']['sha']
    create_github_ref_url = 'https://api.github.com/repos/{repo_id}/git/refs'.format(repo_id=repo)
    create_github_ref_request_body = {
        "ref": resolve_git_ref_heads(new_branch),
        "sha": source_ref
        }
    create_response = requests.post(url=create_github_ref_url, auth=('', token),
                                    json=create_github_ref_request_body, headers=get_application_json_header())
    if not create_response.status_code == 201:
        raise CLIError('Branch creation failed. Error: ({err})'.format(err=create_response.reason))
    return get_branch_name_from_ref(new_branch)


def get_github_branch(repo, branch):
    token = get_github_pat_token()
    head_ref_name = resolve_git_ref_heads(branch).lower()
    get_branch_url = 'https://api.github.com/repos/{repo_id}/git/{refs_heads_branch}'.format(
        repo_id=repo, refs_heads_branch=head_ref_name)
    get_response = requests.get(get_branch_url, auth=('', token))
    if get_response.status_code == _HTTP_NOT_FOUND_STATUS:
        return None
    if get_response.status_code == _HTTP_SUCCESS_STATUS:
        import json
        refs = json.loads(get_response.text)
        if isinstance(refs, list):
            if refs[0]['ref'].startswith(head_ref_name + '/'):
                raise CLIError('Branch ({branch}) is a folder. Hence not a valid branch name'.format(branch=branch))
            # Parse and find correct branch
            for ref in refs:
                if ref['ref'] == head_ref_name:
                    return ref
            return None
        elif refs['ref'] == head_ref_name:
            return refs
        else:
            raise CLIError('Cannot get branch ({branch})'.format(branch=branch))


def commit_files_to_github_branch(files, repo_name, branch, message):
    if files:
        for file in files:
            commit_file_to_github_branch(file.path, file.content, repo_name, branch, message)
    else:
        raise CLIError("No files to checkin.")

def get_application_json_header():
    return {'Content-Type': 'application/json' + '; charset=utf-8',
            'Accept': 'application/json'}

def commit_file_to_github_branch(path_to_commit, content, repo_name, branch, message, skip_ci=True):
    import base64
    if not skip_ci:
        message = message + ' [skip ci]'
    headers = get_application_json_header()

    url_for_github_file_api = 'https://api.github.com/repos/{repo_name}/contents/{path_to_commit}'.format(
        repo_name=repo_name, path_to_commit=path_to_commit)
    if path_to_commit and content:
        path_to_commit = path_to_commit.strip('.')
        path_to_commit = path_to_commit.strip('/')
        encoded_content = base64.b64encode(content.encode('utf-8')).decode("utf-8")
        request_body = {
            "message": message,
            "branch": branch,
            "content": encoded_content
        }
        token = get_github_pat_token()
        logger.warning('Checking in file %s in the Github repository %s', path_to_commit, repo_name)
        # Todo: Validate response and return status from function
        response = requests.put(url_for_github_file_api, auth=('', token),
                                json=request_body, headers=headers)
        logger.debug(response)
