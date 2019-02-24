# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.build.v4_0.models.models import Build
from azext_devops.vstsCompressed.build.v4_0.models.models import DefinitionReference
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_build_client,
                                              resolve_instance_and_project)
from azext_devops.dev.common.uri import uri_quote

logger = get_logger(__name__)

def run_artifact_download(run_id=None, artifact_name=None, path=None, organization=None, project=None, detect=None):
    """Download a pipeline artifact.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    :param artifact_name: Name of the artifact to download.
    :type artifact_name: string
    :param path: Path to download the artifact into.
    :type path: string
    """

    try:
        organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
        client = get_build_client(organization)
        print(client)
    except VstsServiceError as ex:
        raise CLIError(ex)

def run_artifact_list(run_id=None, organization=None, project=None, detect=None):
    """List artifacts associate with run.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    """

    try:
        organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
        client = get_build_client(organization)
        artifacts = client.get_artifacts(run_id, project)
        return artifacts
    except VstsServiceError as ex:
        raise CLIError(ex)

def run_artifact_upload(run_id=None, artifact_name=None, path=None, organization=None, project=None, detect=None):
    """Upload a pipeline artifact.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    :param artifact_name: Name of the artifact to upload.
    :type artifact_name: string
    :param path: Path to upload the artifact from.
    :type path: string
    """

    try:
        organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
        client = get_build_client(organization)
        print(client)
    except VstsServiceError as ex:
        raise CLIError(ex)