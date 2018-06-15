# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import io
import logging
import os
import tempfile
import zipfile
import requests

logger = logging.getLogger('vsts.packaging')

class ArtifactToolUpdater:
    ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY = "VSTS_ARTIFACTTOOL_OVERRIDE_PATH"
    ARTIFACTTOOL_OVERRIDE_URL_ENVKEY = "VSTS_ARTIFACTTOOL_OVERRIDE_URL"
    DEFAULT_ARTIFACTTOOL_BINARY_URL = "https://upacktoolsdev.blob.core.windows.net/artifacttool/artifacttool-win10-x64-Release.zip"

    def get_latest_artifacttool(self, team_instance):
        artifacttool_binary_override_path = os.environ.get(self.ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY)
        if artifacttool_binary_override_path is not None:
            artifacttool_binary_path = artifacttool_binary_override_path
            logger.debug("ArtifactTool path was overriden to '%s' due to environment variable %s" % (artifacttool_binary_path, self.ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY))
        else:
            logger.debug("Checking for a new ArtifactTool")
            artifacttool_binary_path = self._update_artifacttool(team_instance)
            logger.debug("Using downloaded ArtifactTool from '%s'" % artifacttool_binary_path)
        return artifacttool_binary_path

    def _update_artifacttool(self, team_instance):
        logger.debug("Checking for ArtifactTool updates")
        artifacttool_binary_url = self.DEFAULT_ARTIFACTTOOL_BINARY_URL
        artifacttool_binary_override_url = os.environ.get(self.ARTIFACTTOOL_OVERRIDE_URL_ENVKEY)
        if artifacttool_binary_override_url is not None:
            artifacttool_binary_url = artifacttool_binary_override_url
            logger.debug("ArtifactTool download URL was overridden to '%s' due to environment variable %s" % (artifacttool_binary_override_url, self.ARTIFACTTOOL_OVERRIDE_URL_ENVKEY))
        else:
            logger.debug("Using default update URL '%s'" % artifacttool_binary_url)

        head_result = requests.head(artifacttool_binary_url)
        etag = head_result.headers.get('ETag').strip("\"").replace("0x", "").lower()
        logger.debug("Latest ArtifactTool is ETag '%s'" % etag)

        temp_dir = tempfile.gettempdir()
        tool_root = os.path.join(temp_dir, "ArtifactTool")
        tool_dir = os.path.join(tool_root, etag)
          
        # For now, just download if the directory for this etag doesn't exist
        binary_path = os.path.join(tool_dir, "artifacttool-win10-x64-Release", "ArtifactTool.exe")
        if os.path.exists(binary_path):
            logger.debug("Not downloading ArtifactTool as it already exists at %s" % tool_dir)
        else:
            logger.debug("Downloading ArtifactTool to %s" % tool_dir)
            content = requests.get(artifacttool_binary_url)
            f = zipfile.ZipFile(io.BytesIO(content.content))
            f.extractall(path=tool_dir)

        return binary_path
