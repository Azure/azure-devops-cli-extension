# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import JsonPatchOperation, Wiql

from azext_devops.dev.common.services import (get_work_item_tracking_client,
                                              resolve_instance)

logger = get_logger(__name__)


def get_relation_types_show(organization=None, detect=None):
    """ List work item relations supported in the organization.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_work_item_tracking_client(organization)
    return client.get_relation_types()


def add_relation(id, relation_type, target_id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """ Add relation(s) to work item.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    patch_document = []
    client = get_work_item_tracking_client(organization)

    relation_types_from_service = client.get_relation_types()
    relation_type_system_name = get_system_relation_name(relation_types_from_service, relation_type)

    target_work_item_ids = target_id.split(',')
    work_item_query_clause = []
    for target_work_item_id in target_work_item_ids:
        work_item_query_clause.append('[System.Id] = {}'.format(target_work_item_id))

    wiql_query_format = 'SELECT [System.Id] FROM WorkItems WHERE ({})'
    wiql_query_to_get_target_work_items = wiql_query_format.format(' OR '.join(work_item_query_clause))

    wiql_object = Wiql()
    wiql_object.query = wiql_query_to_get_target_work_items
    target_work_items = client.query_by_wiql(wiql=wiql_object).work_items

    if len(target_work_items) != len(target_work_item_ids):
        raise CLIError('Id(s) supplied in --target-id is not valid')

    patch_document = []

    for target_work_item in target_work_items:
        op = _create_patch_operation('add', '/relations/-', relation_type_system_name, target_work_item.url)
        patch_document.append(op)

    client.update_work_item(document=patch_document, id=id)
    work_item = client.get_work_item(id, expand='All')
    work_item = fill_friendly_name_for_relations_in_work_item(relation_types_from_service, work_item)

    return work_item

def add_relation_url(id, relation_type, url, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """ Add relation URL directly to item without looking up target work item id.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    patch_document = []
    client = get_work_item_tracking_client(organization)

    relation_types_from_service = client.get_relation_types()
    relation_type_system_name = get_system_relation_name(relation_types_from_service, relation_type)

    remote_urls = url.split(',')
    patch_document = []

    for remote_url in remote_urls:
        op = _create_patch_operation('add', '/relations/-', relation_type_system_name, remote_url)
        patch_document.append(op)

    client.update_work_item(document=patch_document, id=id)
    work_item = client.get_work_item(id, expand='All')
    work_item = fill_friendly_name_for_relations_in_work_item(relation_types_from_service, work_item)

    return work_item

def remove_relation(id, relation_type, target_id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """ Remove relation(s) from work item.
    """
    organization = resolve_instance(detect=detect, organization=organization)
    patch_document = []
    client = get_work_item_tracking_client(organization)

    relation_types_from_service = client.get_relation_types()
    relation_type_system_name = get_system_relation_name(relation_types_from_service, relation_type)
    target_work_item_ids = target_id.split(',')

    main_work_item = client.get_work_item(id, expand='All')

    if main_work_item.relations:
        for target_work_item_id in target_work_item_ids:
            target_work_item = client.get_work_item(target_work_item_id, expand='All')
            target_work_item_url = target_work_item.url

            index = 0
            for relation in main_work_item.relations:
                if relation.rel == relation_type_system_name and relation.url == target_work_item_url:
                    po = _create_patch_operation('remove', '/relations/{}'.format(index))
                    patch_document.append(po)
                    break
                index = index + 1

    if len(patch_document) != len(target_work_item_ids):
        raise CLIError('Id(s) supplied in --target-id is not valid')

    client.update_work_item(document=patch_document, id=id)
    work_item = client.get_work_item(id, expand='All')
    work_item = fill_friendly_name_for_relations_in_work_item(relation_types_from_service, work_item)

    return work_item


def show_work_item(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """ Get work item, fill relations with friendly name
    """
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_work_item_tracking_client(organization)

    work_item = client.get_work_item(id, expand='All')
    relation_types_from_service = client.get_relation_types()
    work_item = fill_friendly_name_for_relations_in_work_item(relation_types_from_service, work_item)
    return work_item


def fill_friendly_name_for_relations_in_work_item(relation_types_from_service, wi):
    if not wi.relations:
        return wi

    for relation in wi.relations:
        for relation_type_from_service in relation_types_from_service:
            if relation_type_from_service.reference_name == relation.rel:
                relation.rel = relation_type_from_service.name
    return wi


def get_system_relation_name(relation_types_from_service, relation_type):
    for relation_type_from_service in relation_types_from_service:
        if relation_type_from_service.name.lower() == relation_type.lower():
            return relation_type_from_service.reference_name

    raise CLIError("--relation-type is not valid. Use \"az boards work-item relation list-type\" " +
                   "command to list possible relation types in your project")


def _create_patch_operation(op, path, rel=None, url=None):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    if rel is not None and url is not None:
        patch_operation.value = {
            'rel': rel,
            'url': url
        }

    return patch_operation
