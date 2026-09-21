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
import os
import time
from typing import Optional, Callable, Any

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


def run_artifact_upload(
    run_id: int,
    artifact_name: str,
    path: str,
    organization: Optional[str] = None,
    project: Optional[str] = None,
    detect: Optional[bool] = None,
    properties: Optional[str] = None,
    validate_path: bool = True,
    dry_run: bool = False,
    retry_count: int = 3,
    backoff_seconds: float = 0.1,
    log_progress: bool = True,
    on_progress: Optional[Callable[[str, int], None]] = None,
    on_complete: Optional[Callable[[Any], None]] = None,
    on_error: Optional[Callable[[Exception], None]] = None,
) -> Any:
    """
    Upload a pipeline artifact with robust options and hooks.

    :param run_id: ID of the run that the artifact is associated to.
    :type run_id: int
    :param artifact_name: Name of the artifact to upload.
    :type artifact_name: string
    :param path: Path to upload the artifact from.
    :type path: string
    :param properties: Optional custom properties for the artifact in 'key1=value1;key2=value2' format.
    :type properties: string
    :param validate_path: Whether to validate the path before upload.
    :type validate_path: bool
    :param dry_run: If True, do not actually upload.
    :type dry_run: bool
    :param retry_count: Number of times to retry on failure.
    :type retry_count: int
    :param log_progress: Whether to log progress.
    :type log_progress: bool
    :param on_progress: Optional callback for progress updates.
    :type on_progress: callable
    :param on_complete: Optional callback for completion.
    :type on_complete: callable
    :param on_error: Optional callback for errors.
    :type on_error: callable
    """
    organization, project = resolve_instance_and_project(detect=detect, organization=organization, project=project)

    if validate_path and not os.path.exists(path):
        error_msg = f"Artifact path does not exist: {path}"
        logger.error(error_msg)
        exc = FileNotFoundError(error_msg)
        if on_error:
            on_error(exc)
        raise exc

    if dry_run:
        logger.info("Dry run enabled. Skipping upload.")
        result = {"status": "dry_run", "artifact_name": artifact_name, "path": path}
        if on_complete:
            on_complete(result)
        return result

    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())

    for attempt in range(1, retry_count + 1):
        try:
            logger.info(f"Upload attempt {attempt} of {retry_count}")
            result = artifact_tool.upload_pipeline_artifact(
                organization=organization,
                project=project,
                run_id=run_id,
                artifact_name=artifact_name,
                path=path,
                properties=properties,
            )
            if log_progress and on_progress:
                on_progress(f"Upload completed for {artifact_name}", 100)
            if on_complete:
                on_complete(result)
            return result
        except Exception as ex:
            logger.error(f"Upload attempt {attempt} failed: {ex}")
            if on_error:
                on_error(ex)
            if attempt < retry_count:
                time.sleep(backoff_seconds * attempt)
            else:
                logger.error("All upload attempts failed.")
                raise ex
