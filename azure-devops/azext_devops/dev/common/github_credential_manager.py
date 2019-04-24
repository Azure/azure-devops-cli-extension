# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import random
import string
import base64
import requests
from knack.prompting import prompt, prompt_pass
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def singleton(myclass):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = myclass(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class GithubCredentialManager():
    """ GithubCredentialManager
    """
    def __init__(self):
        self.username = None
        self.password = None
        self.token = None

    def create_token(self, note=None):
        self.username = prompt(msg='Enter your GitHub username (leave blank for using already generated PAT): ')
        if not self.username:
            self.token = prompt_pass(msg='Enter your GitHub PAT: ')
            return self.token

        self.password = prompt_pass(msg='Enter your GitHub password: ')
        if not note:
            note = "AzureDevopsCLIExtensionToken_" + randomword(10)
        encoded_pass = base64.b64encode(self.username.encode('utf-8') + b':' + self.password.encode('utf-8'))
        basic_auth = 'basic ' + encoded_pass.decode("utf-8")
        request_body = {
            "scopes": [
                'admin:repo_hook',
                'repo',
                'user'
                ],
            "note": note
            }
        headers = {'Content-Type': 'application/json' + '; charset=utf-8',
                   'Accept': 'application/json',
                   'Authorization': basic_auth}
        response = self.post_authorization_request(headers=headers, body=request_body)

        if (response.status_code == 401 and response.headers.get('X-GitHub-OTP') and
                response.headers.get('X-GitHub-OTP').startswith('required')):
            two_factor_code = prompt(msg='Enter your two factor authentication code: ')
            headers = {'Content-Type': 'application/json' + '; charset=utf-8',
                       'Accept': 'application/json',
                       'Authorization': basic_auth,
                       'X-GitHub-OTP': two_factor_code}
            response = self.post_authorization_request(headers=headers, body=request_body)
        import json
        response_json = json.loads(response.content)
        if response.status_code == 200 or response.status_code == 201:
            logger.warning('Created new personal access token with scopes (admin:repo_hook, repo, user). Name: %s'
                           ' You can revoke this from your GitHub settings if the pipeline is no longer required.', note)
            self.token = response_json['token']
            return self.token
        else:
            raise CLIError('Could not create GitHub token. Check your credentials and try again.')

    def post_authorization_request(self, headers, body):
        return requests.post('https://api.github.com/authorizations',
                             json=body, headers=headers)

    def get_token(self, note=None):
        import os
        from azext_devops.dev.common.const import AZ_DEVOPS_GITHUB_PAT_ENVKEY
        github_pat = os.getenv(AZ_DEVOPS_GITHUB_PAT_ENVKEY, None)
        if github_pat:
            logger.warning('Using GitHub PAT token found in environment variable (%s).', AZ_DEVOPS_GITHUB_PAT_ENVKEY)
            return github_pat

        if not self.token:
            return self.create_token(note=note)
        return self.token
