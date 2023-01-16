# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from azext_devops.devops_sdk.v5_0.build.models import Build, DefinitionReference, AgentPoolQueue
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_build_client,
                                              resolve_instance_and_project)
from azext_devops.dev.common.uri import uri_quote
from .build_definition import get_definition_id_from_name

logger = get_logger(__name__)


def build_queue(definition_id=None, definition_name=None, branch=None, variables=None, open=False,  # pylint: disable=redefined-builtin
                organization=None, project=None, detect=None, commit_id=None, queue_id=None):
    """Request (queue) a build.
    :param definition_id: ID of the definition to queue. Required if --name is not supplied.
    :type definition_id: int
    :param definition_name: Name of the definition to queue. Ignored if --id is supplied.
    :type definition_name: str
    :param branch: Branch to build. Required if there is not a default branch set up on the definition. Example:
    refs/heads/master or master or refs/pull/1/merge or refs/tags/tag
    :type branch: str
    :param variables: Space separated "name=value" pairs for the variables you would like to set.
    :type variables: [str]
    :param open: Open the build results page in your web browser.
    :type open: bool
    :param commit_id: Commit ID of the branch to build.
    :type commit_id: str
    :param queue_id: Queue Id of the pool that will be used to queue the build.
    :type queue_id: str
    :rtype: :class:`<Build> <v5_0.build.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    if definition_id is None and definition_name is None:
        raise ValueError('Either the --definition-id argument or the --definition-name argument ' +
                         'must be supplied for this command.')
    client = get_build_client(organization)
    if definition_id is None:
        definition_id = get_definition_id_from_name(definition_name, client, project)
    definition_reference = DefinitionReference(id=definition_id)
    build = Build(definition=definition_reference)
    build.source_branch = resolve_git_ref_heads(branch)
    build.source_version = commit_id
    if queue_id is not None:
        build.queue = AgentPoolQueue()
        build.queue.id = queue_id
    if variables is not None and variables:
        build.parameters = {}
        for variable in variables:
            separator_pos = variable.find('=')
            if separator_pos >= 0:
                build.parameters[variable[:separator_pos]] = variable[separator_pos + 1:]
            else:
                raise ValueError('The --variables argument should consist of space separated "name=value" pairs.')
    queued_build = client.queue_build(build=build, project=project)
    if open:
        _open_build(queued_build, organization)
    return queued_build


def build_show(id, open=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Get the details of a build.
    :param id: ID of the build.
    :type id: int
    :param open: Open the build results page in your web browser.
    :type open: bool
    :rtype: :class:`<Build> <v5_0.build.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    build = client.get_build(build_id=id, project=project)
    if open:
        _open_build(build, organization)
    return build


def build_list(definition_ids=None, branch=None, organization=None, project=None, detect=None, top=None,
               result=None, status=None, reason=None, tags=None, requested_for=None):
    """List build results.
    :param definition_ids: IDs (space separated) of definitions to list builds for.
    :type definition_ids: list of int
    :param branch: Filter by builds for this branch.
    :type branch: str
    :param top: Maximum number of builds to list.
    :type top: int
    :param result: Limit to builds with this result.
    :type result: str
    :param status: Limit to builds with this status.
    :type status: str
    :param reason: Limit to builds with this reason.
    :type reason: str
    :param tags: Limit to builds with each of the specified tags. Space separated.
    :type tags: list of str
    :param requested_for: Limit to builds requested for this user or group.
    :type requested_for: str
    :rtype: :class:`<Build> <v5_0.build.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    if definition_ids is not None and definition_ids:
        definition_ids = list(set(definition_ids))  # make distinct
    if tags is not None and tags:
        tags = list(set(tags))  # make distinct
    builds = client.get_builds(definitions=definition_ids,
                               project=project,
                               branch_name=resolve_git_ref_heads(branch),
                               top=top,
                               result_filter=result,
                               status_filter=status,
                               reason_filter=reason,
                               tag_filters=tags,
                               requested_for=resolve_identity_as_id(requested_for, organization))
    return builds


def build_cancel(build_id, open=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Cancels if build is running.
    :param build_id: ID of the build.
    :type build_id: int
    :param open: Open the build results page in your web browser.
    :type open: bool
    :rtype: :class:`<Build> <v5_0.build.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_build_client(organization)
    build = Build(status="Cancelling")
    build = client.update_build(build=build, project=project, build_id=build_id)
    if open:
        _open_build(build, organization)
    return build


def add_build_tags(build_id, tags, organization=None, project=None, detect=None):
    """Add tag(s) for a build.
    :param build_id: ID of the build.
    :type build_id: int
    :param tags: Tag(s) to be added to the build. [Comma seperated values]
    :type tags: str
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_build_client(organization)
    tags = list(map(str, tags.split(',')))
    if len(tags) == 1:
        tags = client.add_build_tag(project=project, build_id=build_id, tag=tags[0])
    else:
        tags = client.add_build_tags(tags=tags, project=project, build_id=build_id)
    return tags


def delete_build_tag(build_id, tag, organization=None, project=None, detect=None):
    """Delete a build tag.
    :param build_id: ID of the build.
    :type build_id: int
    :param tag: Tag to be deleted from the build.
    :type tag: str
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_build_client(organization)
    tags = client.delete_build_tag(project=project, build_id=build_id, tag=tag)
    return tags


def get_build_tags(build_id, organization=None, project=None, detect=None):
    """Get tags for a build
    :param build_id: ID of the build.
    :type build_id: int
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_build_client(organization)
    tags = client.get_build_tags(build_id=build_id, project=project)
    return tags


def _open_build(build, organization):
    """Open the build results page in your web browser.
    :param :class:`<Build> <v5_0.build.models.Build>` build:
    :param str organization:
    """
    # https://dev.azure.com/OrgName/ProjectName/_build/index?buildId=1234
    project = build.project.name
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_build/index?buildid='\
        + uri_quote(str(build.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)
