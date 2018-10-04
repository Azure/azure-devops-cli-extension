# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time

from vsts.git.v4_0.models.git_import_request_parameters import GitImportRequestParameters
from vsts.git.v4_0.models.git_import_git_source import GitImportGitSource
from vsts.git.v4_0.models.git_import_request import GitImportRequest

from azext_dev.dev.common.services import get_git_client, resolve_instance_project_and_repo

def create_import_request(project = None, repository = None, git_source_url = None,
                          team_instance=None, detect=None):
    """Create a git import request (currently only supports import from public git source)
    :param project: Name or ID of the team project.
    :type project: str
    :param repository: Name or ID of the repository to create the import request in.
    :type repository: str
    :param git_source_url: Url of the source git repository
    :type git_source_url: str
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance, project, repository, source and target branches
                   if these values are not specified. Default is "on".
    :type detect: str
    """
    team_instance, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                            team_instance=team_instance,
                                                                            project=project,
                                                                            repo=repository)
    client = get_git_client(team_instance)
    gitImportGitSource = GitImportGitSource(overwrite = False,url = git_source_url)
    gitImportRequestParameter = GitImportRequestParameters(delete_service_endpoint_after_import_is_done = False,
                                                           git_source = gitImportGitSource,
                                                           service_endpoint_id = None,
                                                           tfvc_source = None)
    gitImportRequest = GitImportRequest(parameters = gitImportRequestParameter)
    importRequest = client.create_import_request(import_request = gitImportRequest, project = project, repository_id = repository)
    return wait_for_import_request(client, project, repository, importRequest.import_request_id)

def wait_for_import_request(client, project, repository, import_request_id, interval_seconds=5):
    import_request = client.get_import_request(project, repository, import_request_id)
    while not has_import_request_completed(import_request):
        time.sleep(interval_seconds)
        import_request = client.get_import_request(project, repository, import_request_id)
    return import_request

def has_import_request_completed(import_request):
    status = import_request.status.lower()
    return status == 'completed' or status == 'failed' or status == 'abandoned'