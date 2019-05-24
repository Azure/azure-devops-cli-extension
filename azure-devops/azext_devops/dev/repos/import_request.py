# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
from knack.prompting import prompt_pass
from azext_devops.devops_sdk.v5_0.service_endpoint.models import ServiceEndpoint, EndpointAuthorization
from azext_devops.devops_sdk.v5_0.git.models import GitImportRequestParameters
from azext_devops.devops_sdk.v5_0.git.models import GitImportGitSource
from azext_devops.devops_sdk.v5_0.git.models import GitImportRequest

from azext_devops.dev.common.services import (get_git_client,
                                              resolve_instance_project_and_repo,
                                              get_service_endpoint_client)
from azext_devops.dev.common.const import CLI_ENV_VARIABLE_PREFIX
from azext_devops.dev.common.prompting import verify_is_a_tty_or_raise_error


def create_import_request(git_source_url, project=None, repository=None,
                          requires_authorization=False,
                          user_name=None,
                          git_service_endpoint_id=None,
                          organization=None, detect=None):
    """Create a git import request (currently only supports import from public git source)
    :param repository: Name or ID of the repository to create the import request in.
    :type repository: str
    :param git_source_url: Url of the source git repository
    :type git_source_url: str
    :param requires_authorization: Flag to tell if source git repository is private.
    :type requires_authorization: bool
    :param user_name: User name in case source git repository is private
    :type user_name: str
    :param git_service_endpoint_id: Service Endpoint for connection to external endpoint
    :type git_service_endpoint_id: str
    """
    organization, project, repository = resolve_instance_project_and_repo(
        detect=detect,
        organization=organization,
        project=project,
        repo=repository,
        repo_required=True)

    delete_se_after_import = False

    password = None
    import random
    import string
    import os
    if requires_authorization and git_service_endpoint_id is None:
        delete_se_after_import = True
        GIT_SOURCE_PASSWORD_OR_PAT = CLI_ENV_VARIABLE_PREFIX + 'GIT_SOURCE_PASSWORD_OR_PAT'
        if GIT_SOURCE_PASSWORD_OR_PAT in os.environ:
            password = os.environ[GIT_SOURCE_PASSWORD_OR_PAT]
        else:
            error_message = 'Please specify target git password / PAT in ' + GIT_SOURCE_PASSWORD_OR_PAT +\
                            ' environment variable in non-interactive mode.'
            verify_is_a_tty_or_raise_error(error_message)
            password = prompt_pass('Git Password / PAT:', confirm=True)

        service_endpoint_authorization = EndpointAuthorization(
            parameters={'password': password, 'username': user_name},
            scheme='UsernamePassword')
        service_endpoint_to_create = ServiceEndpoint(
            authorization=service_endpoint_authorization,
            name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            type='git',
            url=git_source_url)
        client = get_service_endpoint_client(organization)
        se_created = client.create_service_endpoint(service_endpoint_to_create, project)
        git_service_endpoint_id = se_created.id

    client = get_git_client(organization)
    gitImportGitSource = GitImportGitSource(overwrite=False, url=git_source_url)
    gitImportRequestParameter = GitImportRequestParameters(
        delete_service_endpoint_after_import_is_done=delete_se_after_import,
        git_source=gitImportGitSource,
        service_endpoint_id=git_service_endpoint_id,
        tfvc_source=None)
    gitImportRequest = GitImportRequest(parameters=gitImportRequestParameter)
    importRequest = client.create_import_request(import_request=gitImportRequest, project=project,
                                                 repository_id=repository)
    return _wait_for_import_request(client, project, repository, importRequest.import_request_id)


def _wait_for_import_request(client, project, repository, import_request_id, interval_seconds=5):
    import_request = client.get_import_request(project, repository, import_request_id)
    while not _has_import_request_completed(import_request):
        time.sleep(interval_seconds)
        import_request = client.get_import_request(project, repository, import_request_id)
    return import_request


def _has_import_request_completed(import_request):
    status = import_request.status.lower()
    return status in ('completed', 'failed', 'abandoned')
