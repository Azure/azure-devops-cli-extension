# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import webbrowser

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.core.models import TeamProject
from azext_devops.dev.common.operations import wait_for_long_running_operation
from azext_devops.dev.common.services import (get_core_client,
                                              get_core_client_v51,
                                              resolve_instance)
from azext_devops.dev.common.uri import uri_quote

logger = get_logger(__name__)


def create_project(name, organization=None, process=None, source_control='git', description=None,
                   visibility='private', detect=None, open=False):  # pylint: disable=redefined-builtin
    """Create a team project.
    :param name: Name of the new project.
    :type name: str
    :param process: Process to use. Default if not specified.
    :type process: str
    :param source_control: Source control type of the initial code repository created.
    :type source_control: str
    :param description: Description for the new project.
    :type description: str
    :param visibility: Project visibility.
    :type visibility: str
    :test pr change
    :param open: Open the team project in the default web browser.
    :type open: bool
    :rtype: :class:`<TeamProject> <v5_0.core.models.TeamProject>`
    """
    organization = resolve_instance(detect=detect, organization=organization)

    team_project = TeamProject()
    team_project.name = name
    team_project.description = description

    # private is the only allowed value by vsts right now.
    team_project.visibility = visibility

    core_client = get_core_client(organization)

    # get process template id
    process_id = None
    process_list = core_client.get_processes()
    if process is not None:
        process_lower = process.lower()
        for prc in process_list:
            if prc.name.lower() == process_lower:
                process_id = prc.id
                break
        if process_id is None:
            raise CLIError('Could not find a process template with name: "{}"'.format(name))
    if process_id is None:
        for prc in process_list:
            if prc.is_default:
                process_id = prc.id
                break
        if process_id is None:
            raise CLIError('Could not find a default process template: "{}"'.format(name))

    # build capabilities
    version_control_capabilities = {VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME: source_control}
    process_capabilities = {PROCESS_TEMPLATE_CAPABILITY_TEMPLATE_TYPE_ID_ATTRIBUTE_NAME: process_id}
    team_project.capabilities = {VERSION_CONTROL_CAPABILITY_NAME: version_control_capabilities,
                                 PROCESS_TEMPLATE_CAPABILITY_NAME: process_capabilities}

    # queue project creation
    operation_reference = core_client.queue_create_project(project_to_create=team_project)
    operation = wait_for_long_running_operation(organization, operation_reference.id, 1)
    status = operation.status.lower()
    if status == 'failed':
        raise CLIError('Project creation failed.')
    if status == 'cancelled':
        raise CLIError('Project creation was cancelled.')

    team_project = core_client.get_project(project_id=name, include_capabilities=True)
    if open:
        _open_project(team_project)
    return team_project


def delete_project(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete team project.
    :param id: The id of the project to delete.
    :type id: str
    """
    organization = resolve_instance(detect=detect, organization=organization)
    core_client = get_core_client(organization)
    operation_reference = core_client.queue_delete_project(project_id=id)
    operation = wait_for_long_running_operation(organization, operation_reference.id, 1)
    status = operation.status.lower()
    if status == 'failed':
        raise CLIError('Project deletion failed.')
    if status == 'cancelled':
        raise CLIError('Project deletion was cancelled.')
    print('Deleted project {}'.format(id))
    return operation


def show_project(project, organization=None, detect=None, open=False):  # pylint: disable=redefined-builtin
    """Show team project.
    :param project: The id or name of the project to show.
    :type project: str
    :param open: Open the team project in the default web browser.
    :type open: bool
    :rtype: :class:`<TeamProject> <v5_0.core.models.TeamProject>`
    """
    organization = resolve_instance(detect=detect, organization=organization)
    core_client = get_core_client(organization)
    team_project = core_client.get_project(project_id=project, include_capabilities=True)
    if open:
        _open_project(team_project)
    return team_project


def list_projects(organization=None,
                  top=None,
                  skip=None,
                  state_filter='all',
                  continuation_token=None,
                  get_default_team_image_url=None,
                  detect=None):
    """List team projects
    :param top: Maximum number of results to list.
    :type top: int
    :param skip: Number of results to skip.
    :type skip: int
    :rtype: list of :class:`<TeamProject> <v5_0.core.models.TeamProject>`
    """
    logger.debug('Opening web page: %s', 'Test CLI Release')

    logger.debug('__________________________________________________________________________________________________')

    organization = resolve_instance(detect=detect, organization=organization)
    core_client = get_core_client_v51(organization)
    team_projects = core_client.get_projects(state_filter=state_filter,
                                             top=top,
                                             skip=skip,
                                             continuation_token=continuation_token,
                                             get_default_team_image_url=get_default_team_image_url)
    return team_projects


def _open_project(project):
    """Opens the project in the default browser.
    """
    api_segment = '/_apis/'
    pos = project.url.find(api_segment)
    if pos >= 0:
        url = project.url[:pos + 1] + uri_quote(project.name)
        logger.debug('Opening web page: %s', url)
        webbrowser.open_new(url=url)
    else:
        raise CLIError("Failed to open web browser, due to unrecognized url in response.")


# capability keys
VERSION_CONTROL_CAPABILITY_NAME = 'versioncontrol'
VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME = 'sourceControlType'
PROCESS_TEMPLATE_CAPABILITY_NAME = 'processTemplate'
PROCESS_TEMPLATE_CAPABILITY_TEMPLATE_TYPE_ID_ATTRIBUTE_NAME = 'templateTypeId'
