# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import io
import logging
import os
import platform
import shutil
import stat
import sys
import tempfile
import uuid
import zipfile

import humanfriendly
import requests
from knack.util import CLIError
from vsts.cli.common.services import get_vss_connection

logger = logging.getLogger('vsts.packaging')

class ArtifactToolUpdater:
    ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY = "VSTS_CLI_ARTIFACTTOOL_OVERRIDE_PATH"
    ARTIFACTTOOL_OVERRIDE_URL_ENVKEY = "VSTS_CLI_ARTIFACTTOOL_OVERRIDE_URL"
    ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY = "VSTS_CLI_ARTIFACTTOOL_OVERRIDE_VERSION"

    def get_latest_artifacttool(self, team_instance):
        artifacttool_binary_override_path = os.environ.get(self.ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY)
        if artifacttool_binary_override_path is not None:
            artifacttool_binary_path = artifacttool_binary_override_path
            logger.debug("ArtifactTool path was overriden to '{}' due to environment variable {}".format(artifacttool_binary_path, self.ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY))
        else:
            logger.debug("Checking for a new ArtifactTool")
            artifacttool_binary_path = self._get_artifacttool(team_instance)
        return artifacttool_binary_path

    def _get_artifacttool(self, team_instance):
        logger.debug("Checking for ArtifactTool updates")

        # Call the auto-update API to find the current version of ArtifactTool
        # If VSTS_ARTIFACTTOOL_OVERRIDE_URL is set, instead always download from the URL
        artifacttool_override_url = os.environ.get(self.ARTIFACTTOOL_OVERRIDE_URL_ENVKEY)
        if artifacttool_override_url is not None:
            release_uri = artifacttool_override_url
            release_id = "custom_{}".format(uuid.uuid4())
            logger.debug("ArtifactTool download URL is being overridden to '{}' (ID '{}')".format(release_uri, release_id))
        else:
            override_version = os.environ.get(self.ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY)
            try:
                release = self._get_current_release(team_instance, override_version)
            except Exception as ex:
                raise CLIError('Failed to update Universal Packages tooling.\n{}'.format(ex))
            release_uri, release_id = release

        # Determine the path for the release, and skip downloading if it already exists
        logger.debug("Checking if we already have ArtifactTool release '{}'".format(release_id))
        release_dir = self._compute_release_dir(release_id)
        if os.path.exists(release_dir):
            logger.debug("Not updating ArtifactTool because the current release already exists at '{}'".format(release_dir))
            return release_dir
              
        # Doesn't already exist. Download and extract the release.
        logger.debug("Updating to ArtifactTool release {} since it doesn't exist at {}".format(release_id, release_dir))
        self._update_artifacttool(release_uri, release_id)

        return release_dir

    def _get_current_release(self, team_instance, override_version):
        connection = get_vss_connection(team_instance)
        client = connection.get_client('vsts.cli.package.common.client_tool.client_tool_client.ClientToolClient')
        logger.debug("Looking up current version of ArtifactTool...")
        release = client.get_clienttool_release("ArtifactTool", os_name=platform.system(), arch=platform.machine(), version=override_version)
        return (release.uri, self._compute_id(release)) if release is not None else None

    def _update_artifacttool(self, uri, release_id):
        root = self._compute_artifacttool_root()
        
        # Remove all existing releases. In the future we may maintain some old versions, but right now we always delete them.
        if os.path.isdir(root):
            for item in os.listdir(root):
                path = os.path.join(root, item)
                if os.path.isdir(path):
                    logger.debug("Trying to remove old release {}".format(item))
                    shutil.rmtree(path, ignore_errors=True) # Failing cleanup is not fatal

        with humanfriendly.Spinner(label="Downloading Universal Packages tooling ({})".format(release_id), total=100, stream=sys.stderr) as spinner:
            spinner.step()
            logger.debug("Downloading ArtifactTool from {}".format(uri))

            # Make the request, determine the total size
            response = requests.get(uri, stream=True)
            content_length_header = response.headers['Content-Length'].strip()
            content_length = int(content_length_header)

            # Do the download, updating the progress bar
            content=io.BytesIO()
            bytes_so_far = 0
            for chunk in response.iter_content(chunk_size=1024*512):
                if chunk:
                    content.write(chunk)
                    bytes_so_far += len(chunk)
                    spinner.step(100 * float(bytes_so_far)/float(content_length))

            # Extract the zip
            release_temp_dir = os.path.join(root, str(uuid.uuid4()))
            logger.debug("Extracting ArtifactTool to {}".format(release_temp_dir))
            f = zipfile.ZipFile(content)
            try:
                self._mkdir_if_not_exist(release_temp_dir)
                f.extractall(path=release_temp_dir)

                # For Linux, ensure the executable bit is set on the binary "ArtifactTool" if it exists.
                # Python has a bug https://bugs.python.org/issue15795 where file permissions are not preserved.
                artifacttool_binary = os.path.join(release_temp_dir, "artifacttool")
                if os.path.exists(artifacttool_binary):
                    artifacttool_stat = os.stat(artifacttool_binary)
                    os.chmod(artifacttool_binary, artifacttool_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

                # Move the release into the real releases location
                release_dir = self._compute_release_dir(release_id)
                logger.debug("Moving downloaded ArtifactTool from {} to {}".format(release_temp_dir, release_dir))
                os.rename(release_temp_dir, release_dir)
                logger.info("Downloaded Universal Packages tooling successfully")
            except Exception as ex:
                logger.error("An error occurred while extracting the Universal Packages tooling: {}".format(ex))
                logger.debug("Removing temporary directory {}".format(release_temp_dir))
                shutil.rmtree(release_temp_dir, ignore_errors=True)

    def _mkdir_if_not_exist(self, path):
        try: 
            os.makedirs(path)
        except OSError:
            # Ignore errors that were likely because the directory already exists
            if not os.path.isdir(path):
                raise

    def _compute_id(self, release):
        return "{}_{}_{}".format(release.name, release.rid, release.version)

    def _compute_artifacttool_root(self):
        vsts_cli_root = os.path.expanduser(os.path.join('~', '.vsts', 'cli', 'tools'))
        return os.path.join(vsts_cli_root, "artifacttool")

    def _compute_release_dir(self, release_id):
        return os.path.join(self._compute_artifacttool_root(), release_id)