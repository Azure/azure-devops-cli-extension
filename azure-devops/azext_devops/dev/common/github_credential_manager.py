# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
import base64
from knack.log import get_logger
from knack.util import CLIError

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
        req_body = {
            "scopes": [
                'admin:repo_hook', 
                'repo', 
                'user'
                ],
            "note": note
            }
        headers = {'Content-Type': 'application/json' + '; charset=utf-8',
                   'Accept': 'application/json',
                   'Authorization': basic_auth,
                   'X-GitHub-OTP': two_factor_code}
        response = requests.post('https://api.github.com/authorizations',
                                 json=req_body, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            logger.warning('Created new personal access token with scopes (admin:repo_hook, repo, user). You can revoke this from your GitHub settings if the pipeline is no longer requird.')
            import json
            token = json.loads(response.content)['token']
            return token
        else:
            raise CLIError('Could not create GitHub token. Check your credentials and try again.')
