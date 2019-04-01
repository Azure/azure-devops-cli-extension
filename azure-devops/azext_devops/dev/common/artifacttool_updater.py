# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import io
import os
import platform
import shutil
import stat
import sys
import uuid
import zipfile

import humanfriendly
import requests

from knack.log import get_logger
from knack.util import CLIError
import distro

from azext_devops.dev.common.services import get_connection
from azext_devops.dev.common.config import AZ_DEVOPS_GLOBAL_CONFIG_DIR
from azext_devops.dev.common.const import (ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY,
                                           ARTIFACTTOOL_OVERRIDE_URL_ENVKEY,
                                           ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY)

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class ArtifactToolUpdater:

    def get_latest_artifacttool(self, organization):
        artifacttool_binary_override_path = os.environ.get(ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY)
        if artifacttool_binary_override_path is not None:
            artifacttool_binary_path = artifacttool_binary_override_path
            logger.debug("ArtifactTool path was overriden to '%s' due to environment variable %s",
                         artifacttool_binary_path, ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY)
        else:
            logger.debug("Checking for a new ArtifactTool")
            artifacttool_binary_path = self._get_artifacttool(organization)
        return artifacttool_binary_path

    def _get_artifacttool(self, organization):  # pylint: disable=no-self-use
        logger.debug("Checking for ArtifactTool updates")

        # Call the auto-update API to find the current version of ArtifactTool
        # If AZURE_DEVOPS_EXT_ARTIFACTTOOL_OVERRIDE_URL is set, instead always download from the URL
        artifacttool_override_url = os.environ.get(ARTIFACTTOOL_OVERRIDE_URL_ENVKEY)
        if artifacttool_override_url is not None:
            release_uri = artifacttool_override_url
            release_id = "custom_{}".format(uuid.uuid4())
            logger.debug("ArtifactTool download URL is being overridden to '%s' (ID '%s')", release_uri, release_id)
        else:
            override_version = os.environ.get(ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY)
            try:
                release = _get_current_release(organization, override_version)
            except Exception as ex:
                logger.debug(ex, exc_info=True)
                raise CLIError('Failed to update Universal Packages tooling.\n {}'.format(ex))
            release_uri, release_id = release

        # Determine the path for the release, and skip downloading if it already exists
        logger.debug("Checking if we already have ArtifactTool release '%s'", release_id)
        release_dir = _compute_release_dir(release_id)
        if os.path.exists(release_dir):
            logger.debug("Not updating ArtifactTool because the current release already exists at '%s'", release_dir)
            return release_dir

        # Doesn't already exist. Download and extract the release.
        logger.debug("Updating to ArtifactTool release %s since it doesn't exist at %s", release_id, release_dir)
        _update_artifacttool(release_uri, release_id)

        return release_dir


def _update_artifacttool(uri, release_id):
    root = _compute_artifacttool_root()

    # Remove all existing releases. In the future we may maintain some old versions,
    # but right now we always delete them.
    if os.path.isdir(root):
        for item in os.listdir(root):
            path = os.path.join(root, item)
            if os.path.isdir(path):
                logger.debug("Trying to remove old release %s", item)
                shutil.rmtree(path, ignore_errors=True)   # Failing cleanup is not fatal

    with humanfriendly.Spinner(label="Downloading Universal Packages tooling ({})"
                               .format(release_id), total=100, stream=sys.stderr) as spinner:
        spinner.step()
        logger.debug("Downloading ArtifactTool from %s", uri)

        # Make the request, determine the total size
        response = requests.get(uri, stream=True)
        content_length_header = response.headers['Content-Length'].strip()
        content_length = int(content_length_header)

        # Do the download, updating the progress bar
        content = io.BytesIO()
        bytes_so_far = 0
        for chunk in response.iter_content(chunk_size=1024 * 512):
            if chunk:
                content.write(chunk)
                bytes_so_far += len(chunk)
                spinner.step(100 * float(bytes_so_far) / float(content_length))

        # Extract the zip
        release_temp_dir = os.path.join(root, str(uuid.uuid4()))
        logger.debug("Extracting ArtifactTool to %s", release_temp_dir)
        f = zipfile.ZipFile(content)
        try:
            _mkdir_if_not_exist(release_temp_dir)
            f.extractall(path=release_temp_dir)

            # For Linux, ensure the executable bit is set on the binary "ArtifactTool" if it exists.
            # Python has a bug https://bugs.python.org/issue15795 where file permissions are not preserved.
            artifacttool_binary = os.path.join(release_temp_dir, "artifacttool")
            if os.path.exists(artifacttool_binary):
                artifacttool_stat = os.stat(artifacttool_binary)
                os.chmod(artifacttool_binary,
                         artifacttool_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

            # Move the release into the real releases location
            release_dir = _compute_release_dir(release_id)
            logger.debug("Moving downloaded ArtifactTool from %s to %s", release_temp_dir, release_dir)
            os.rename(release_temp_dir, release_dir)
            logger.info("Downloaded Universal Packages tooling successfully")
        except BaseException as ex:  # pylint: disable=broad-except
            logger.error("An error occurred while extracting the Universal Packages tooling: %s", ex)
            logger.debug("Removing temporary directory %s", release_temp_dir)
            shutil.rmtree(release_temp_dir, ignore_errors=True)


def _get_current_release(organization, override_version):
    connection = get_connection(organization)
    client = connection.get_client('azext_devops.dev.common.client_tool.client_tool_client.ClientToolClient')
    logger.debug("Looking up current version of ArtifactTool...")
    # Distro returns empty strings on Windows currently, so don't even send
    distro_name = distro.id() or None
    distro_version = distro.version() or None
    release = client.get_clienttool_release(
        "ArtifactTool",
        os_name=platform.system(),
        arch=platform.machine(),
        distro_name=distro_name,
        distro_version=distro_version,
        version=override_version)
    return (release.uri, _compute_id(release)) if release is not None else None


def _mkdir_if_not_exist(path):
    try:
        os.makedirs(path)
    except OSError:
        # Ignore errors that were likely because the directory already exists
        if not os.path.isdir(path):
            raise


def _compute_id(release):
    return "{}_{}_{}".format(release.name, release.rid, release.version)


def _compute_artifacttool_root():
    az_devops_cli_root = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'cli', 'tools')
    return os.path.join(az_devops_cli_root, "artifacttool")


def _compute_release_dir(release_id):
    return os.path.join(_compute_artifacttool_root(), release_id)
