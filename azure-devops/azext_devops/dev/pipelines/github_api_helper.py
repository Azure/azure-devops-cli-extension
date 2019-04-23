# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import requests
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


class Files:
    def __init__(self, path, content):
        self.path = path
        self.content = content


def get_github_pat_token():
    from azext_devops.dev.common.github_credential_manager import GithubCredentialManager
    github_manager = GithubCredentialManager()
    return github_manager.get_token()


def checkin_files_to_github(files, repo_name, branch, message="Set up CI with Azure Pipelines"):
    if files:
        for file in files:
            checkin_file_to_github(file.path, file.content, repo_name, branch, message)
    else:
        raise CLIError("No files to checkin.")


def checkin_file_to_github(path_to_commit, content, repo_name, branch, message):
    import base64
    message = message + ' [skip ci]'
    headers = {'Content-Type': 'application/json' + '; charset=utf-8',
               'Accept': 'application/json'}

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
