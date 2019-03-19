# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import base64
import requests
from knack.prompting import prompt
from knack.log import get_logger
from knack.util import CLIError
from .prompting import verify_is_a_tty_or_raise_error

logger = get_logger(__name__)


class GithubCredentialManager():
    """ GithubCredentialManager
    """
    def __init__(self, username, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    def create_token(self, note="AzureDevopsCLIExtensionToken", two_factor_code=None):
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
        response = GithubCredentialManager.post_authorization_request(headers=headers, body=request_body)

        if (response.status_code == 401 and response.headers.get('X-GitHub-OTP') and
                response.headers.get('X-GitHub-OTP').startswith('required')):
            if not two_factor_code:
                verify_is_a_tty_or_raise_error(
                    error_msg='Your GitHub account is protected by two-factor authentication. '
                    'Cannot use non-interactive flow to create a PAT')
                two_factor_code = prompt(msg='Enter your two factor authentication code: ')
            headers = {'Content-Type': 'application/json' + '; charset=utf-8',
                       'Accept': 'application/json',
                       'Authorization': basic_auth,
                       'X-GitHub-OTP': two_factor_code}
            response = GithubCredentialManager.post_authorization_request(headers=headers, body=request_body)
        import json
        response_json = json.loads(response.content)
        if response.status_code == 200 or response.status_code == 201:
            logger.warning('Created new personal access token with scopes (admin:repo_hook, repo, user).'
                           ' You can revoke this from your GitHub settings if the pipeline is no longer requird.')
            return response_json['token']
        else:
            raise CLIError('Could not create GitHub token. Check your credentials and try again.')

    @staticmethod
    def post_authorization_request(headers, body):
        return requests.post('https://api.github.com/authorizations',
                             json=body, headers=headers)
