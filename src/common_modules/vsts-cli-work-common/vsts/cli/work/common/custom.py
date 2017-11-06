# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import urllib
import webbrowser

from knack.util import CLIError
from vsts.exceptions import VstsServiceError
from vsts.work_item_tracking.v4_0.models.json_patch_operation import JsonPatchOperation
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.identities import resolve_identity_as_display_name
from vsts.cli.common.vsts import (get_base_url,
                                  get_work_item_tracking_client,
                                  resolve_instance,
                                  resolve_instance_and_project)


def create_work_item(work_item_type, title, description=None, assigned_to=None, state=None, area=None,
                     iteration=None, reason=None, history=None, fields=None, open_browser=False,
                     team_instance=None, project=None, detect=None):
    """Create a new work item.
    :param work_item_type: Name of the work item type (e.g. Bug).
    :type work_item_type: str
    :param title:
    :type title: str
    :param description:
    :type description: str
    :param assigned_to:
    :type assigned_to: str
    :param state:
    :type state: str
    :param area:
    :type area: str
    :param iteration:
    :type iteration: str
    :param reason:
    :type reason: str
    :param history:
    :type history: str
    :param fields: Space separated "field=value" pairs for custom fields you would like to set.
    :type fields: [str]
    :param open_browser: Open the work item in the default web browser.
    :type open_browser: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        team_instance, project = resolve_instance_and_project(detect=detect,
                                                              team_instance=team_instance,
                                                              project=project,
                                                              project_required=True)
        patch_document = []
        if title is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Title', title))
        else:
            raise ValueError('--title is a required argument.')
        if description is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Description', description))
        if assigned_to is not None:
            # 'assigned to' does not take an identity id.  Display name works.
            if assigned_to == '':
                resolved_assigned_to = ''
            else:
                resolved_assigned_to = resolve_identity_as_display_name(assigned_to, team_instance)
            if resolved_assigned_to is not None:
                patch_document.append(_create_work_item_field_patch_operation('add', 'System.AssignedTo',
                                                                              resolved_assigned_to))
        if state is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.State', state))
        if area is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.AreaPath', area))
        if iteration is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.IterationPath', iteration))
        if reason is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Reason', reason))
        if history is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.History', history))
        if fields is not None and fields:
            for field in fields:
                kvp = field.split('=')
                if len(kvp) == 2:
                    patch_document.append(_create_work_item_field_patch_operation('add', kvp[0], kvp[1]))
                else:
                    raise ValueError('The --fields argument should consist of space separated "field=value" pairs.')
        client = get_work_item_tracking_client(team_instance)
        work_item = client.create_work_item(document=patch_document, project=project, type=work_item_type)
        if open_browser:
            _open_work_item(work_item, team_instance)
        return work_item
    except VstsServiceError as ex:
        _handle_vsts_service_error(ex)
    except Exception as ex:
        handle_command_exception(ex)


def update_work_item(work_item_id, title=None, description=None, assigned_to=None, state=None, area=None,
                     iteration=None, reason=None, history=None, fields=None, open_browser=False,
                     team_instance=None, detect=None):
    """Create a new work item.
    :param work_item_id: The id of the work item to update.
    :type work_item_id: str
    :param title:
    :type title: str
    :param description:
    :type description: str
    :param assigned_to:
    :type assigned_to: str
    :param state:
    :type state: str
    :param area:
    :type area: str
    :param iteration:
    :type iteration: str
    :param reason:
    :type reason: str
    :param history:
    :type history: str
    :param fields: Space separated "field=value" pairs for custom fields you would like to set.
    :type fields: [str]
    :param open_browser: Open the work item in the default web browser.
    :type open_browser: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        patch_document = []
        if title is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Title', title))
        if description is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Description', description))
        if assigned_to is not None:
            # 'assigned to' does not take an identity id.  Display name works.
            if assigned_to == '':
                resolved_assigned_to = ''
            else:
                resolved_assigned_to = resolve_identity_as_display_name(assigned_to, team_instance)
            if resolved_assigned_to is not None:
                patch_document.append(_create_work_item_field_patch_operation('add', 'System.AssignedTo',
                                                                              resolved_assigned_to))
        if state is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.State', state))
        if area is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.AreaPath', area))
        if iteration is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.IterationPath', iteration))
        if reason is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Reason', reason))
        if history is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.History', history))
        if fields is not None and fields:
            for field in fields:
                kvp = field.split('=')
                if len(kvp) == 2:
                    patch_document.append(_create_work_item_field_patch_operation('add', kvp[0], kvp[1]))
                else:
                    raise ValueError('The --fields argument should consist of space separated "field=value" pairs.')
        client = get_work_item_tracking_client(team_instance)
        work_item = client.update_work_item(document=patch_document, id=work_item_id)
        if open_browser:
            _open_work_item(work_item, team_instance)
        return work_item
    except VstsServiceError as ex:
        _handle_vsts_service_error(ex)
    except Exception as ex:
        handle_command_exception(ex)


def _handle_vsts_service_error(ex):
    logging.exception(ex)
    if ex.type_key == 'RuleValidationException' and "FieldReferenceName" in ex.custom_properties:
        if ex.message is not None:
            message = ex.message
            if message and message[len(message) - 1] != '.':
                message += '.'
            name = ex.custom_properties["FieldReferenceName"]
            if name in _system_field_args:
                message += ' Use the --{} argument to supply this value.'.format(_system_field_args[name])
            else:
                message += ' To specify a value for this field, use the --field argument and set the name of the ' \
                           + 'name/value pair to {}.'.format(name)
        else:
            message = "RuleValidationException for FieldReferenceName: " + ex.custom_properties["FieldReferenceName"]
        raise CLIError(ValueError(message))
    else:
        raise CLIError(ex)


def show_work_item(work_item_id, open_browser=False, team_instance=None, detect=None):
    """Show details for a work item.
    :param work_item_id: The ID of the work item
    :type work_item_id: int
    :param open_browser: Open the work item in the default web browser.
    :type open_browser: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_work_item_tracking_client(team_instance)
        work_item = client.get_work_item(work_item_id)
        if open_browser:
            _open_work_item(work_item, team_instance)
        return work_item
    except Exception as ex:
        handle_command_exception(ex)


def _open_work_item(work_item, team_instance):
    """Opens the work item in the default browser.
    :param work_item: The work item to open.
    :type work_item: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    project = work_item.fields['System.TeamProject']
    url = urllib.parse.urljoin(get_base_url(team_instance), urllib.parse.quote(project) + '/_workitems?id='
                               + urllib.parse.quote(str(work_item.id)))
    webbrowser.open_new(url=url)


def _create_patch_operation(op, path, value):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = value
    return patch_operation


def _create_work_item_field_patch_operation(op, field, value):
    path = '/fields/{field}'.format(field=field)
    return _create_patch_operation(op=op, path=path, value=value)


_system_field_args = {'System.Title': 'title',
                      'System.Description': 'description',
                      'System.AssignedTo': 'assigned-to',
                      'System.State': 'state',
                      'System.AreaPath': 'area-path',
                      'System.IterationPath': 'iteration-path',
                      'System.Reason': 'reason',
                      'System.History': 'history'}
