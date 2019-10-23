# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import colorama
from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.services import resolve_instance, resolve_instance_and_project
from azext_devops.dev.common.artifacttool import ArtifactToolInvoker
from azext_devops.dev.common.artifacttool_updater import ArtifactToolUpdater
from azext_devops.dev.common.external_tool import ProgressReportingExternalToolInvoker

logger = get_logger(__name__)


def publish_package(feed,
                    name,
                    version,
                    path,
                    description=None,
                    scope='organization',
                    organization=None,
                    project=None,
                    detect=None):
    """Publish a package to a feed.
    :param scope: Scope of the feed: 'project' if the feed was created in a project, and 'organization' otherwise.
    :type scope: str
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

    if scope == 'project':
        organization, project = resolve_instance_and_project(
            detect=detect,
            organization=organization,
            project=project)
    else:
        if project is not None:
            raise CLIError('--scope \'project\' is required when specifying a project in --project')

        organization = resolve_instance(
            detect=detect,
            organization=organization)

    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.publish_universal(organization, project, feed, name, version, description, path)


def download_package(feed,
                     name,
                     version,
                     path,
                     file_filter=None,
                     scope='organization',
                     organization=None,
                     project=None,
                     detect=None):
    """Download a package.
    :param scope: Scope of the feed: 'project' if the feed was created in a project, and 'organization' otherwise.
    :type scope: str
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

    if scope == 'project':
        organization, project = resolve_instance_and_project(
            detect=detect,
            organization=organization,
            project=project)
    else:
        if project is not None:
            raise CLIError('--scope \'project\' is required when specifying a project in --project')

        organization = resolve_instance(
            detect=detect,
            organization=organization)

    artifact_tool = ArtifactToolInvoker(ProgressReportingExternalToolInvoker(), ArtifactToolUpdater())
    return artifact_tool.download_universal(organization, project, feed, name, version, path, file_filter)
