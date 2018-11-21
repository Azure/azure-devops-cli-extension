# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from vsts.cli.common.services import (get_release_client,resolve_instance_and_project)
from vsts.cli.common.uri import uri_quote
from vsts.cli.common.uuid import is_uuid

logger = get_logger(__name__)

def release_definition_list(name=None, top=None, team_instance=None, project=None, artifact_type=None, artifact_source_id=None, detect=None):
    """List release definitions.
    :param name: Limit results to definitions with this name or starting with this name. Examples: "FabCI" or "Fab*"
    :type name: str
    :param top: Maximum number of definitions to list.
    :type top: int
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param artifact_type: Release definitions with given artifactType will be returned.
    :type artifact_type: str
    :param artifact_source_id: Limit results to definitions associated with this artifact_source_id.e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json at https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions.
    :type artifact_source_id: str
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: [ReleaseDefinitionReference]
    """
    team_instance, project = resolve_instance_and_project(detect=detect,
                                                          team_instance=team_instance,
                                                          project=project)
    client = get_release_client(team_instance)
    query_order = 'nameAscending'
    definition_references = client.get_release_definitions(project=project, search_text=name, artifact_source_id=artifact_source_id,
                                                           artifact_type=artifact_type, top=top, query_order=query_order)
    return definition_references


def release_definition_show(definition_id=None, name=None, open_browser=False, team_instance=None, project=None,
                          detect=None):
    """Get the details of a release definition.
    :param definition_id: ID of the definition.
    :type definition_id: int
    :param name: Name of the definition. Ignored if --id is supplied.
    :type name: str
    :param open_browser: Open the definition summary page in your web browser.
    :type open_browser: bool
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect values for instance and project. Default is "on".
    :type detect: str
    :rtype: ReleaseDefinitionReference
    """
    team_instance, project = resolve_instance_and_project(detect=detect,
                                                            team_instance=team_instance,
                                                            project=project)
    client = get_release_client(team_instance)
    if definition_id is None:
        if name is not None:
            definition_id = get_definition_id_from_name(name, client, project)
        else:
            raise ValueError("Either the --id argument or the --name argument must be supplied for this command.")
    release_definition = client.get_release_definition(definition_id=definition_id, project=project)
    if open_browser:
        _open_definition(release_definition)
    return release_definition


def _open_definition(definition):
    """Opens the release definition in the default browser.
    :param :class:`<ReleaseDefinitionReference> <release.v4_0.models.ReleaseDefinitionReference>` definition:
    """
    url = _get_release_definition_web_url(definition)
    if url is not None and url:
        logger.debug('Opening web page: %s', url)
        open_new(url=url)


def get_definition_id_from_name(name, client, project):
    definition_references = client.get_release_definitions(project=project, search_text=name, is_exact_name_match='true')
    if len(definition_references) == 1:
        return definition_references[0].id
    elif len(definition_references) > 1:
        if is_uuid(project):
            project = definition_references[0].project.name
        message = 'Multiple definitions were found matching name "{name}" in project "{project}".  Try '\
                  + 'supplying the definition ID.'
        raise ValueError(message.format(name=name, project=project))
    else:
        raise ValueError('There were no release definitions matching name "{name}" in project "{project}".'
                         .format(name=name, project=project))

 
def _get_release_definition_web_url(definition):
    links = definition._links
    if links is not None and links:
        properties = links.additional_properties
        if properties is not None and properties:
            web_url = properties.get('web')
            if web_url is not None and web_url:
                return web_url.get('href')