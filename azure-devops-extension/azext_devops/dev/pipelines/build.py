# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from webbrowser import open_new

from knack.log import get_logger
from knack.util import CLIError
from vsts.exceptions import VstsServiceError
from vsts.build.v4_0.models.build import Build
from vsts.build.v4_0.models.definition_reference import DefinitionReference
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.identities import resolve_identity_as_id
from azext_devops.dev.common.services import (get_build_client,
                                      resolve_instance_and_project)
from azext_devops.dev.common.uri import uri_quote
from .build_definition import get_definition_id_from_name

logger = get_logger(__name__)


def build_queue(definition_id=None, definition_name=None, branch=None, variables=None, open_browser=False,
                devops_organization=None, project=None, detect=None, source_branch=None):
    """Request (queue) a build.
    :param definition_id: ID of the definition to queue. Required if --name is not supplied.
    :type definition_id: int
    :param definition_name: Name of the definition to queue. Ignored if --id is supplied.
    :type definition_name: str
    :param branch: Branch to build. Required if there is not a default branch set up on the definition. Example: "dev".
    :type branch: str
    :param variables: Space separated "name=value" pairs for the variables you would like to set.
    :type variables: [str]
    :param open_browser: Open the build results page in your web browser.
    :type open_browser: bool
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :param source_branch: Obsolete. Use --branch instead.
    :type source_branch: str
    :rtype: :class:`<Build> <build.v4_0.models.Build>`
    """
    try:
        if branch is None:
            branch = source_branch
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                            devops_organization=devops_organization,
                                                            project=project)
        if definition_id is None and definition_name is None:
            raise ValueError('Either the --definition-id argument or the --definition-name argument ' +
                            'must be supplied for this command.')
        client = get_build_client(devops_organization)
        if definition_id is None:
            definition_id = get_definition_id_from_name(definition_name, client, project)
        definition_reference = DefinitionReference(id=definition_id)
        build = Build(definition=definition_reference)
        build.source_branch = resolve_git_ref_heads(branch)
        if variables is not None and variables:
            build.parameters = {}
            for variable in variables:
                separator_pos = variable.find('=')
                if separator_pos >= 0:
                    build.parameters[variable[:separator_pos]] = variable[separator_pos + 1:]
                else:
                    raise ValueError('The --variables argument should consist of space separated "name=value" pairs.')
        queued_build = client.queue_build(build=build, project=project)
        if open_browser:
            _open_build(queued_build, devops_organization)
        return queued_build
    except VstsServiceError as ex:
        raise CLIError(ex)


def build_show(build_id, open_browser=False, devops_organization=None, project=None, detect=None):
    """Get the details of a build.
    :param build_id: ID of the build.
    :type build_id: int
    :param open_browser: Open the build results page in your web browser.
    :type open_browser: bool
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: :class:`<Build> <build.v4_0.models.Build>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                devops_organization=devops_organization,
                                                                project=project)
        client = get_build_client(devops_organization)
        build = client.get_build(build_id=build_id, project=project)
        if open_browser:
            _open_build(build, devops_organization)
        return build
    except VstsServiceError as ex:
        raise CLIError(ex)


def build_list(definition_ids=None, branch=None, devops_organization=None, project=None, detect=None, top=None,
               result=None, status=None, reason=None, tags=None, requested_for=None):
    """List build results.
    :param definition_ids: IDs (space separated) of definitions to list builds for.
    :type definition_ids: list of int
    :param branch: Filter by builds for this branch.
    :type branch: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
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
    :rtype: :class:`<Build> <build.v4_0.models.Build>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                devops_organization=devops_organization,
                                                                project=project)
        client = get_build_client(devops_organization)
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
                                    requested_for=resolve_identity_as_id(requested_for, devops_organization))
        return builds
    except VstsServiceError as ex:
        raise CLIError(ex)


def _open_build(build, devops_organization):
    """Open the build results page in your web browser.
    :param :class:`<Build> <build.v4_0.models.Build>` build:
    :param str devops_organization:
    """
    # https://mseng.visualstudio.com/vsts-cli/_build/index?buildId=4053990
    project = build.project.name
    url = devops_organization.rstrip('/') + '/' + uri_quote(project) + '/_build/index?buildid='\
        + uri_quote(str(build.id))
    logger.debug('Opening web page: %s', url)
    open_new(url=url)
