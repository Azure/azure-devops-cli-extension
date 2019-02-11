# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import webbrowser

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError
from azext_devops.vstsCompressed.work_item_tracking.v4_0.models.models import JsonPatchOperation
from azext_devops.vstsCompressed.work_item_tracking.v4_0.models.models import Wiql
from azext_devops.dev.common.identities import (ME, get_current_identity,
                                                resolve_identity,
                                                get_account_from_identity)
from azext_devops.dev.common.services import (get_work_item_tracking_client,
                                              resolve_instance,
                                              resolve_instance_and_project)
from azext_devops.dev.common.uri import uri_quote

logger = get_logger(__name__)


def create_work_item(work_item_type, title, description=None, assigned_to=None, area=None,
                     iteration=None, reason=None, discussion=None, fields=None, open=False,  # pylint: disable=redefined-builtin
                     organization=None, project=None, detect=None):
    r"""Create a work item.
    :param work_item_type: Name of the work item type (e.g. Bug).
    :type work_item_type: str
    :param title: Title of the work item.
    :type title: str
    :param description: Description of the work item.
    :type description: str
    :param assigned_to: Name of the person the work item is assigned-to (e.g. fabrikam).
    :type assigned_to: str
    :param area: Area the work item is assigned to (e.g. Demos)
    :type area: str
    :param iteration: Iteration path of the work item (e.g. Demos\Iteration 1).
    :type iteration: str
    :param reason: Reason for the state of the work item.
    :type reason: str
    :param discussion: Comment to add to a discussion in a work item.
    :type discussion: str
    :param fields: Space separated "field=value" pairs for custom fields you would like to set.
    :type fields: [str]
    :param open: Open the work item in the default web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project, project_required=True)
        patch_document = []
        if title is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Title', title))
        else:
            raise ValueError('--title is a required argument.')
        if description is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Description', description))
        if assigned_to is not None:
            # 'assigned to' does not take an identity id.  Display name works.
            assigned_to = assigned_to.strip()
            if assigned_to == '':
                resolved_assigned_to = ''
            else:
                resolved_assigned_to = _resolve_identity_as_unique_user_id(assigned_to, organization)
            if resolved_assigned_to is not None:
                patch_document.append(_create_work_item_field_patch_operation('add', 'System.AssignedTo',
                                                                              resolved_assigned_to))
        if area is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.AreaPath', area))
        if iteration is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.IterationPath', iteration))
        if reason is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Reason', reason))
        if discussion is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.History', discussion))
        if fields is not None and fields:
            for field in fields:
                kvp = field.split('=', 1)
                if len(kvp) == 2:
                    patch_document.append(_create_work_item_field_patch_operation('add', kvp[0], kvp[1]))
                else:
                    raise ValueError('The --fields argument should consist of space separated "field=value" pairs.')
        client = get_work_item_tracking_client(organization)
        work_item = client.create_work_item(document=patch_document, project=project, type=work_item_type)
        if open:
            _open_work_item(work_item, organization)
        return work_item
    except VstsServiceError as ex:
        _handle_vsts_service_error(ex)


def update_work_item(id, title=None, description=None, assigned_to=None, state=None, area=None,  # pylint: disable=redefined-builtin
                     iteration=None, reason=None, discussion=None, fields=None, open=False,  # pylint: disable=redefined-builtin
                     organization=None, detect=None):
    r"""Update work items.
    :param id: The id of the work item to update.
    :type id: int
    :param title: Title of the work item.
    :type title: str
    :param description: Description of the work item.
    :type description: str
    :param assigned_to: Name of the person the work item is assigned-to (e.g. fabrikam).
    :type assigned_to: str
    :param state: State of the work item (e.g. active).
    :type state: str
    :param area: Area the work item is assigned to (e.g. Demos).
    :type area: str
    :param iteration: Iteration path of the work item (e.g. Demos\Iteration 1).
    :type iteration: str
    :param reason: Reason for the state of the work item.
    :type reason: str
    :param discussion: Comment to add to a discussion in a work item.
    :type discussion: str
    :param fields: Space separated "field=value" pairs for custom fields you would like to set.
    :type fields: [str]
    :param open: Open the work item in the default web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        organization = resolve_instance(detect=detect, organization=organization)
        patch_document = []
        if title is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Title', title))
        if description is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.Description', description))
        if assigned_to is not None:
            assigned_to = assigned_to.strip()
            # 'assigned to' does not take an identity id.  Display name works.
            if assigned_to == '':
                resolved_assigned_to = ''
            else:
                resolved_assigned_to = _resolve_identity_as_unique_user_id(assigned_to, organization)
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
        if discussion is not None:
            patch_document.append(_create_work_item_field_patch_operation('add', 'System.History', discussion))
        if fields is not None and fields:
            for field in fields:
                kvp = field.split('=', 1)
                if len(kvp) == 2:
                    patch_document.append(_create_work_item_field_patch_operation('add', kvp[0], kvp[1]))
                else:
                    raise ValueError('The --fields argument should consist of space separated "field=value" pairs.')
        client = get_work_item_tracking_client(organization)
        work_item = client.update_work_item(document=patch_document, id=id)
        if open:
            _open_work_item(work_item, organization)
        return work_item
    except VstsServiceError as ex:
        _handle_vsts_service_error(ex)


def delete_work_item(id, destroy=False, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Delete a work item.
    :param id: Unique id of the work item.
    :type id: int
    :param destroy: Permanently delete this work item.
    :type destroy: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItemDelete>`
    """
    try:
        organization = resolve_instance(detect=detect, organization=organization)
        client = get_work_item_tracking_client(organization)
        delete_response = client.delete_work_item(id, destroy)
        print('Deleted work item {}'.format(id))
        return delete_response
    except VstsServiceError as ex:
        _handle_vsts_service_error(ex)


def _handle_vsts_service_error(ex):
    logger.debug(ex, exc_info=True)
    if ex.type_key == 'RuleValidationException' and "FieldReferenceName" in ex.custom_properties:
        if ex.message is not None:
            message = ex.message
            if message and message[len(message) - 1] != '.':
                message += '.'
            name = ex.custom_properties["FieldReferenceName"]
            if name is not None:
                if name in _SYSTEM_FIELD_ARGS:
                    message += ' Use the --{} argument to supply this value.'.format(_SYSTEM_FIELD_ARGS[name])
                else:
                    message += ' To specify a value for this field, use the --field argument and set the name of the ' \
                               + 'name/value pair to {}.'.format(name)
        else:
            message = "RuleValidationException for FieldReferenceName: " + ex.custom_properties["FieldReferenceName"]
        raise CLIError(ValueError(message))
    else:
        raise CLIError(ex)


def show_work_item(id, open=False, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details for a work item.
    :param id: The ID of the work item
    :type id: int
    :param open: Open the work item in the default web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        organization = resolve_instance(detect=detect, organization=organization)
        try:
            client = get_work_item_tracking_client(organization)
            work_item = client.get_work_item(id)
        except VstsServiceError as ex:
            _handle_vsts_service_error(ex)

        if open:
            _open_work_item(work_item, organization)
        return work_item
    except VstsServiceError as ex:
        raise CLIError(ex)


# pylint: disable=too-many-statements
def query_work_items(wiql=None, id=None, path=None, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Query for a list of work items.
    :param wiql: The query in Work Item Query Language format.  Ignored if --id or --path is specified.
    :type wiql: str
    :param id: The UUID of an existing query.  Required unless --path or --wiql are specified.
    :type id: str
    :param path: The path of an existing query.  Ignored if --id is specified.
    :type path: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    try:
        if wiql is None and path is None and id is None:
            raise CLIError("Either the --wiql, --id, or --path argument must be specified.")
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project, project_required=False)
        client = get_work_item_tracking_client(organization)
        if id is None and path is not None:
            if project is None:
                raise CLIError("The --project argument must be specified for this query.")
            query = client.get_query(project=project, query=path)
            id = query.id
        if id is not None:
            query_result = client.query_by_id(id=id)
        else:
            wiql_object = Wiql()
            wiql_object.query = wiql
            query_result = client.query_by_wiql(wiql=wiql_object)
        if query_result.work_items:
            _last_query_result[_LAST_QUERY_RESULT_KEY] = query_result  # store query result for table view
            safety_buffer = 100  # a buffer in the max url length to protect going over the limit
            remaining_url_length = 2048 - safety_buffer
            remaining_url_length -= len(organization)
            # following subtracts relative url, the asof parameter and beginning of id and field parameters.
            # asof value length will vary, but this should be the longest possible
            remaining_url_length -=\
                len('/_apis/wit/workItems?ids=&fields=&asOf=2017-11-07T17%3A05%3A34.06699999999999999Z')
            fields = []
            fields_length_in_url = 0
            if query_result.columns:
                for field_ref in query_result.columns:
                    fields.append(field_ref.reference_name)
                    if fields_length_in_url > 0:
                        fields_length_in_url += 3  # add 3 for %2C delimiter
                    fields_length_in_url += len(uri_quote(field_ref.reference_name))
                    if fields_length_in_url > 800:
                        logger.info("Not retrieving all fields due to max url length.")
                        break
            remaining_url_length -= fields_length_in_url
            max_work_items = 1000
            work_items_batch_size = 200
            current_batch = []
            work_items = []
            work_item_url_length = 0
            for work_item_ref in query_result.work_items:
                if len(work_items) >= max_work_items:
                    logger.info("Only retrieving the first %s work items.", max_work_items)
                    break
                if work_item_url_length > 0:
                    work_item_url_length += 3  # add 3 for %2C delimiter
                work_item_url_length += len(str(work_item_ref.id))
                current_batch.append(work_item_ref.id)

                if remaining_url_length - work_item_url_length <= 0 or len(current_batch) == work_items_batch_size:
                    # url is near max length, go ahead and send first request for details.
                    # url can go over by an id length because we have a safety buffer
                    current_batched_items = client.get_work_items(ids=current_batch,
                                                                  as_of=query_result.as_of,
                                                                  fields=fields)
                    for work_item in current_batched_items:
                        work_items.append(work_item)
                    current_batch = []
                    work_item_url_length = 0

            if current_batch:
                current_batched_items = client.get_work_items(ids=current_batch,
                                                              as_of=query_result.as_of,
                                                              fields=fields)
                for work_item in current_batched_items:
                    work_items.append(work_item)
            # put items in the same order they appeared in the initial query results
            work_items = sorted(work_items, key=_get_sort_key_from_last_query_results)
            return work_items
        return None
    except VstsServiceError as ex:
        raise CLIError(ex)


def _get_sort_key_from_last_query_results(work_item):
    work_items = get_last_query_result().work_items
    i = 0
    num_items = len(work_items)
    while i < num_items:
        if work_items[i].id == work_item.id:
            return i
        i += 1
    # following lines should never be reached
    raise CLIError("Work Item {} was not found in the original query results.".format(work_item.id))


_last_query_result = {}
_LAST_QUERY_RESULT_KEY = 'value'


def get_last_query_result():
    return _last_query_result.get(_LAST_QUERY_RESULT_KEY, None)


def _open_work_item(work_item, organization):
    """Opens the work item in the default browser.
    :param work_item: The work item to open.
    :type work_item: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItem>`
    """
    project = work_item.fields['System.TeamProject']
    url = organization.rstrip('/') + '/' + uri_quote(project) + '/_workitems?id='\
        + uri_quote(str(work_item.id))
    logger.debug('Opening web page: %s', url)
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


def _resolve_identity_as_unique_user_id(identity_filter, organization):
    """Takes an identity name, email, alias, or id, and returns the unique_user_id.
    """
    if identity_filter.find(' ') > 0 or identity_filter.find('@') > 0:
        return identity_filter
    if identity_filter.lower() == ME:
        identity = get_current_identity(organization)
    else:
        # For alias
        identity = resolve_identity(identity_filter, organization)
    if identity is not None:
        return get_account_from_identity(identity)
    return None


_SYSTEM_FIELD_ARGS = {'System.Title': 'title',
                      'System.Description': 'description',
                      'System.AssignedTo': 'assigned-to',
                      'System.State': 'state',
                      'System.AreaPath': 'area-path',
                      'System.IterationPath': 'iteration-path',
                      'System.Reason': 'reason',
                      'System.History': 'history'}
