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
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_work_item_tracking_client(organization)
    return client.get_relation_types()

def add_relation(id, relation_type, target_ids, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    patch_document = []
    client = get_work_item_tracking_client(organization)

    relation_types_from_service = client.get_relation_types()
    relation_type_system_name = None

    for relation_type_from_service in relation_types_from_service:
        if relation_type_from_service.name.lower() == relation_type.lower():
            relation_type_system_name = relation_type_from_service.reference_name
            break

    if relation_type_system_name is None:
        raise CLIError("--relation-type is not valid")

    target_work_item_ids = target_ids.split(',')
    work_item_query_clause = []
    for target_work_item_id in target_work_item_ids:
        work_item_query_clause.append('[System.Id] = {}'.format(target_work_item_id))

    wiql_query_to_get_target_work_items = 'SELECT [System.Id] FROM WorkItems WHERE ({})'.format(' OR '.join(work_item_query_clause))

    wiql_object = Wiql()
    wiql_object.query = wiql_query_to_get_target_work_items
    target_work_items = client.query_by_wiql(wiql=wiql_object).work_items

    patch_document = []

    for target_work_item in target_work_items:
        op = _create_patch_operation('add', '/relations/-', relation_type_system_name, target_work_item.url)
        patch_document.append(op)

    client.update_work_item(document=patch_document, id=id)
    work_item = client.get_work_item(id, expand='All')

    return work_item


def _create_patch_operation(op, path, rel, url):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    patch_operation.value = {
        'rel': rel,
        'url': url
    }
    return patch_operation




    
