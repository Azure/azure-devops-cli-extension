# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import requests
from knack.log import get_logger
from azext_devops.dev.common.services import _get_credentials

logger = get_logger(__name__)

def checkin_file_to_github(path_to_commit, content, service_endpoint_id, repo_name, branch,
                           organization, project, message="Set up CI with Azure Pipelines"):
    vss_credentials = _get_credentials(organization)
    headers = {'Content-Type': 'application/json' + '; charset=utf-8',
               'Accept': 'application/json'}
    headers['X-TFS-FedAuthRedirect'] = 'Suppress'
    headers['X-VSS-ForceMsaPassThrough'] = 'true'

    url_for_dataProvider = organization + '/_apis/Contribution/HierarchyQuery?api-version=5.0-preview.1'
    if path_to_commit and content:
        path_to_commit = path_to_commit.strip('.')
        path_to_commit = path_to_commit.strip('/')
        path_to_commit = './' + path_to_commit
        commit_to_github_request_body = {
            "contributionIds": [
                "ms.vss-build-web.commit-file-data-provider"
                ],
            "dataProviderContext": {
                "properties": {
                    "connectionId": service_endpoint_id,
                    "sourceProvider": "github",
                    "repository": repo_name,
                    "path": path_to_commit,
                    "content": content,
                    "targetBranch": branch,
                    "sourceBranch": None,
                    "message": message,
                    "description": "",
                    "sourcePage": {
                        "routeId": "ms.vss-build-web.ci-definition-designer-route",
                        "routeValues": {
                            "project": project
                        }
                    }
                }
            }
        }
        logger.warning('Checking in file %s in the Github repository %s', path_to_commit, repo_name)
        # Todo: Validate response and return status from function
        requests.post(url_for_dataProvider, auth=(vss_credentials.username, vss_credentials.password),
                      json=commit_to_github_request_body, headers=headers)
