# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import sys

import colorama
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import get_core_client, resolve_instance

from .artifacttool import ArtifactToolInvoker
from .artifacttool_updater import ArtifactToolUpdater
from .external_tool import ProgressReportingExternalToolInvoker

logger = logging.getLogger('vsts.packaging')

_UNIVERSAL_PREVIEW_MESSAGE = colorama.Fore.YELLOW + 'Universal Packages is currently in preview.\n' + colorama.Fore.RESET

def publish_package(feed, name, version, path, description=None, team_instance=None, detect=None):
    """(PREVIEW) Publish a package to a feed.
    :param feed: Name or ID of the feed.
    :type feed: str
    :param name: Name of the package, e.g. 'foo-package'.
    :type name: str
    :param version: Version of the package, e.g. '1.0.0'.
    :type version: str
    :param description: Description of the package.
    :type description: str
    :param path: Directory containing the package contents.
    :type path: str
    :param team_instance: VSTS account URL. Example: 'https://myaccount.visualstudio.com'.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
    :type detect: str
    """
    try:
        colorama.init() # Needed for humanfriendly spinner to display correctly
        sys.stderr.write(_UNIVERSAL_PREVIEW_MESSAGE)
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
        return artifact_tool.publish_universal(team_instance, feed, name, version, description, path)
    except Exception as ex:
        handle_command_exception(ex)
      
def download_package(feed, name, version, path, team_instance=None, detect=None):
    """(PREVIEW) Download a package.
    :param feed: Name or ID of the feed.
    :type feed: str
    :param name: Name of the package, e.g. 'foo-package'.
    :type name: str
    :param version: Version of the package, e.g. 1.0.0.
    :type version: str
    :param path: Directory to place the package contents.
    :type path: str
    :param team_instance: VSTS account URL. Example: 'https://myaccount.visualstudio.com'.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
    :type detect: str
    """
    try:
        colorama.init() # Needed for humanfriendly spinner to display correctly
        sys.stderr.write(_UNIVERSAL_PREVIEW_MESSAGE)
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
        return artifact_tool.download_universal(team_instance, feed, name, version, path)
    except Exception as ex:
        handle_command_exception(ex)
