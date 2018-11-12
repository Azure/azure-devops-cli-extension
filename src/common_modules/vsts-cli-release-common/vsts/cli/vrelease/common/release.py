# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from vsts.release.v4_0.models.release import Release
from vsts.release.v4_0.models.release_start_metadata import ReleaseStartMetadata
from vsts.release.v4_0.models.artifact_metadata import ArtifactMetadata
from vsts.release.v4_0.models.build_version import BuildVersion

from vsts.cli.common.identities import resolve_identity_as_id
from vsts.cli.common.services import (get_release_client, resolve_instance_and_project)
from vsts.cli.common.uri import uri_quote
from .release_definition import get_definition_id_from_name

logger = get_logger(__name__)

def release_create(definition_id=None, definition_name=None, artifact_metadata_list=None, description=None, open_browser=False,
                team_instance=None, project=None, detect=None):
    """Request (create) a release.
    :param definition_id: ID of the definition to create. Required if --name is not supplied.
    :type definition_id: int
    :param definition_name: Name of the definition to create. Ignored if --id is supplied.
    :type definition_name: str
    :param open_browser: Open the release results page in your web browser.
    :type open_browser: bool
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param artifact_metadata_list: Space separated "alias=version_id" pairs.
    :type artifact_metadata_list: [str]
	:param description: Description of the release.
    :type description: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: :class:`<ReleaseStartMetadata> <release.v4_0.models.ReleaseStartMetadata>`
    """

    team_instance, project = resolve_instance_and_project(detect=detect,
                                                          team_instance=team_instance,
                                                          project=project)
    if definition_id is None and definition_name is None:
        raise ValueError('Either the --definition-id argument or the --definition-name argument ' +
                         'must be supplied for this command.')
    client = get_release_client(team_instance)
    
    if definition_id is None:
        definition_id = get_definition_id_from_name(definition_name, client, project)

    artifacts = []
    if artifact_metadata_list is not None and artifact_metadata_list:
        for artifact_metadata in artifact_metadata_list:
             separator_pos = artifact_metadata.find('=')
             if separator_pos >= 0:
                 instance_reference = BuildVersion(id=artifact_metadata[separator_pos + 1:])
                 artifact = ArtifactMetadata(alias=artifact_metadata[:separator_pos], instance_reference=instance_reference)
                 artifacts.append(artifact)
             else:
                 raise ValueError('The --artifact_meta_data_list argument should consist of space separated "alias=version_id" pairs.'+artifact_metadata)
    
    release = ReleaseStartMetadata(definition_id=definition_id, artifacts=artifacts, description=description)
    
    created_release = client.create_release(release_start_metadata=release, project=project)
    
    if open_browser:
        _open_release(created_release, team_instance)
    
    return created_release


def release_show(release_id, open_browser=False, team_instance=None, project=None, detect=None):
    """Get the details of a release.
    :param release_id: ID of the release.
    :type release_id: int
    :param open_browser: Open the release results page in your web browser.
    :type open_browser: bool
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: :class:`<Release> <release.v4_0.models.Release>`
    """
    team_instance, project = resolve_instance_and_project(detect=detect,
                                                          team_instance=team_instance,
                                                          project=project)
    client = get_release_client(team_instance)
    release = client.get_release(release_id=release_id, project=project)
    if open_browser:
        _open_release(release, team_instance)
    return release


def release_list(definition_id=None, source_branch=None, team_instance=None, project=None, detect=None, top=None,
                 status=None):
    """List release results.
    :param definition_id: ID of definition to list releases for.
    :type definition_id: int
    :param branch: Filter by releases for this branch.
    :type branch: str
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :param top: Maximum number of releases to list. Default is 50.
    :type top: int
    :param status: Limit to releases with this status.
    :type status: str
    :param source_branch: Filter releases for this branch.
    :type source_branch: str
    :rtype: :class:`<Release> <release.v4_0.models.Release>`
    """
    team_instance, project = resolve_instance_and_project(detect=detect,
                                                           team_instance=team_instance,
                                                           project=project)
    client = get_release_client(team_instance)

    releases = client.get_releases(definition_id=definition_id,
                                project=project,
                                source_branch_filter=source_branch,
                                top=top,
                                status_filter=status)
    return releases


def _open_release(release, team_instance):
    """Open the release results page in your web browser.
    :param :class:`<Release> <release.v4_0.models.Release>` release:
    :param str team_instance:
    """
    # https://mseng.visualstudio.com/vsts-cli/_release/index?releaseId=4053990
    project = release.project.name
    url = team_instance.rstrip('/') + '/' + uri_quote(project) + '/_release/index?releaseid='\
        + uri_quote(str(release.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)
