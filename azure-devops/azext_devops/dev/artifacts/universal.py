# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import colorama
from knack.log import get_logger
from azext_devops.dev.common.services import resolve_instance
from azext_devops.dev.common.artifacttool import ArtifactToolInvoker
from azext_devops.dev.common.artifacttool_updater import ArtifactToolUpdater
from azext_devops.dev.common.external_tool import ProgressReportingExternalToolInvoker

logger = get_logger(__name__)

_UNIVERSAL_PREVIEW_MESSAGE = "Universal Packages is currently in preview."


def publish_package(feed, name, version, path, description=None, organization=None, detect=None):
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
    """
    colorama.init()   # Needed for humanfriendly spinner to display correctly
    logger.warning(_UNIVERSAL_PREVIEW_MESSAGE)
    organization = resolve_instance(detect=detect, organization=organization)
    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.publish_universal(organization, feed, name, version, description, path)


def download_package(feed, name, version, path, file_filter=None, organization=None, detect=None):
    """(PREVIEW) Download a package.
    :param feed: Name or ID of the feed.
    :type feed: str
    :param name: Name of the package, e.g. 'foo-package'.
    :type name: str
    :param version: Version of the package, e.g. 1.0.0.
    :type version: str
    :param path: Directory to place the package contents.
    :type path: str
    :param file_filter: Wildcard filter for file download.
    :type file_filter: str
    """
    colorama.init()  # Needed for humanfriendly spinner to display correctly
    logger.warning(_UNIVERSAL_PREVIEW_MESSAGE)
    organization = resolve_instance(detect=detect, organization=organization)
    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.download_universal(organization, feed, name, version, path, file_filter)
