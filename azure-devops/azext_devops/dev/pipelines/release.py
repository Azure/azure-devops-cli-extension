# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from vsts.release.v4_0.models.release_start_metadata import ReleaseStartMetadata
from vsts.release.v4_0.models.artifact_metadata import ArtifactMetadata
from vsts.release.v4_0.models.build_version import BuildVersion
from knack.log import get_logger
from azext_devops.dev.common.services import (get_release_client, resolve_instance_and_project)
from .release_definition import get_definition_id_from_name

logger = get_logger(__name__)


def release_create(definition_id=None, definition_name=None, artifact_metadata_list=None, description=None,
                   open_browser=False, devops_organization=None, project=None, detect=None):
    """Request (create) a release.
    :param definition_id: ID of the definition to create. Required if --definition-name is not supplied.
    :type definition_id: int
    :param definition_name: Name of the definition to create. Ignored if --definition-id is supplied.
    :type definition_name: str
    :param open_browser: Open the release results page in your web browser.
    :type open_browser: bool
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param artifact_metadata_list: Space separated "alias=version_id" pairs.
    :type artifact_metadata_list: [str]
    :param description: Description of the release.
    :type description: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    :rtype: :class:`<ReleaseStartMetadata> <release.v4_0.models.ReleaseStartMetadata>`
    """

    devops_organization, project = resolve_instance_and_project(
        detect=detect, devops_organization=devops_organization, project=project)
    if definition_id is None and definition_name is None:
        raise ValueError('Either the --definition-id argument or the --definition-name argument ' +
                         'must be supplied for this command.')
    client = get_release_client(devops_organization)

    if definition_id is None:
        definition_id = get_definition_id_from_name(definition_name, client, project)

    artifacts = []
    if artifact_metadata_list is not None and artifact_metadata_list:
        for artifact_metadata in artifact_metadata_list:
            separator_pos = artifact_metadata.find('=')
            if separator_pos >= 0:
                instance_reference = BuildVersion(id=artifact_metadata[separator_pos + 1:])
                artifact = ArtifactMetadata(alias=artifact_metadata[:separator_pos],
                                            instance_reference=instance_reference)
                artifacts.append(artifact)
            else:
                raise ValueError('The --artifact_meta_data_list argument should consist'
                                 'of space separated "alias=version_id" pairs.' + artifact_metadata)

    release = ReleaseStartMetadata(definition_id=definition_id, artifacts=artifacts, description=description)

    created_release = client.create_release(release_start_metadata=release, project=project)

    if open_browser:
        _open_release(created_release)

    return created_release


def release_show(release_id, open_browser=False, devops_organization=None, project=None, detect=None):
    """Get the details of a release.
    :param release_id: ID of the release.
    :type release_id: int
    :param open_browser: Open the release results page in your web browser.
    :type open_browser: bool
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    :rtype: :class:`<Release> <release.v4_0.models.Release>`
    """
    devops_organization, project = resolve_instance_and_project(
        detect=detect, devops_organization=devops_organization, project=project)
    client = get_release_client(devops_organization)
    release = client.get_release(release_id=release_id, project=project)
    if open_browser:
        _open_release(release)
    return release


def release_list(definition_id=None, source_branch=None, devops_organization=None, project=None, detect=None, top=None,
                 status=None):
    """List release results.
    :param definition_id: ID of definition to list releases for.
    :type definition_id: int
    :param branch: Filter by releases for this branch.
    :type branch: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for organization and project. Default is "on".
    :type detect: str
    :param top: Maximum number of releases to list. Default is 50.
    :type top: int
    :param status: Limit to releases with this status.
    :type status: str
    :param source_branch: Filter releases for this branch.
    :type source_branch: str
    :rtype: :class:`<Release> <release.v4_0.models.Release>`
    """
    devops_organization, project = resolve_instance_and_project(
        detect=detect, devops_organization=devops_organization, project=project)
    client = get_release_client(devops_organization)

    releases = client.get_releases(definition_id=definition_id,
                                   project=project,
                                   source_branch_filter=source_branch,
                                   top=top,
                                   status_filter=status)
    return releases


def _open_release(release):
    """Open the release results page in your web browser.
    :param :class:`<Release> <release.v4_0.models.Release>` release:
    """
    url = _get_release_web_url(release)
    if url is not None and url:
        logger.debug('Opening web page: %s', url)
        open_new(url=url)


def _get_release_web_url(release):
    links = release._links  # pylint: disable=protected-access
    if links is not None and links:
        properties = links.additional_properties
        if properties is not None and properties:
            web_url = properties.get('web')
            if web_url is not None and web_url:
                return web_url.get('href')
    return None
