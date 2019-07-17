# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from azext_devops.dev.common.services import (get_build_client,
                                              resolve_instance_and_project)
from azext_devops.dev.common.artifacttool import ArtifactToolInvoker
from azext_devops.dev.common.artifacttool_updater import ArtifactToolUpdater
from azext_devops.dev.common.external_tool import ProgressReportingExternalToolInvoker

logger = get_logger(__name__)


def run_artifact_download(run_id, artifact_name, path, organization=None, project=None, detect=None):
    """ Download a pipeline artifact.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    :param artifact_name: Name of the artifact to download.
    :type artifact_name: string
    :param path: Path to download the artifact into.
    :type path: string
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.download_pipeline_artifact(
        organization=organization, project=project, run_id=run_id, artifact_name=artifact_name, path=path)


def run_artifact_list(run_id, organization=None, project=None, detect=None):
    """ List artifacts associated with a run.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    artifacts = client.get_artifacts(project=project, build_id=run_id)
    return artifacts


def run_artifact_upload(run_id, artifact_name, path, organization=None, project=None, detect=None):
    """ Upload a pipeline artifact.
    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    :param artifact_name: Name of the artifact to upload.
    :type artifact_name: string
    :param path: Path to upload the artifact from.
    :type path: string
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)
    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.upload_pipeline_artifact(
        organization=organization, project=project, run_id=run_id, artifact_name=artifact_name, path=path)
