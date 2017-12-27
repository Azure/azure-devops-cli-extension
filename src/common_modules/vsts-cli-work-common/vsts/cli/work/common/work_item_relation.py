# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.work_item_tracking.v4_0.models.json_patch_operation import JsonPatchOperation
from vsts.work_item_tracking.v4_0.models.work_item_relation import WorkItemRelation
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_work_item_tracking_client,
                                      resolve_instance,
                                      resolve_instance_and_project)
from vsts.cli.common.uri import uri_quote


_RELATION_FIELD_ARGS = {
    'child': 'System.LinkTypes.Hierarchy-Forward',
    'duplicate': 'System.LinkTypes.Duplicate-Forward',
    'duplicateOf': 'System.LinkTypes.Duplicate-Reverse',
    'parent': 'System.LinkTypes.Hierarchy-Forward',
    'predecessor': 'System.LinkTypes.Dependency-Reverse',
    'referencedBy': 'Microsoft.VSTS.TestCase.SharedParameterReferencedBy-Forward',
    'references': 'Microsoft.VSTS.TestCase.SharedParameterReferencedBy-Reverse',
    'related': 'System.LinkTypes.Related',
    'successor': 'System.LinkTypes.Dependency-Forward'
}


def add_work_item_relations(work_item_id, relations, team_instance=None, detect=None):
    """Add relations to a work item.
    :param int work_item_id: The ID of the work item
    :param [str] relations: Space separated "relation=value" pairs for custom relations. Value is the ID of a work item; Key is one of [child, duplicate, duplicateOf, parent, predecessor, referencedBy, references, related, successor].
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        patch_document = []
        if relations is not None:
            _append_relations(patch_document, relations, 'add', team_instance)
        client = get_work_item_tracking_client(team_instance)
        return client.update_work_item(document=patch_document, id=work_item_id).relations
    except Exception as ex:
        handle_command_exception(ex)


def remove_work_item_relations(work_item_id, indexes, team_instance=None, detect=None):
    """Remove relations to a work item.
    :param int work_item_id: The ID of the work item
    :param str indexes: Colon separated values of the index or the relations to remove.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        patch_document = []
        if indexes is not None:
            for index in indexes.split(','):
                patch_document.append(create_patch_operation('remove', '/relations/' + index))
        client = get_work_item_tracking_client(team_instance)
        return client.update_work_item(document=patch_document, id=work_item_id).relations
    except Exception as ex:
        handle_command_exception(ex)


def show_work_item_relations(work_item_id, team_instance=None, detect=None):
    """Show relations of a work item.
    :param int work_item_id: The ID of the work item
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        client = get_work_item_tracking_client(team_instance)
        work_item = client.get_work_item(id=work_item_id, expand='relations')
        return work_item.relations
    except Exception as ex:
        handle_command_exception(ex)


def _append_relations(work_item, relations, op, team_instance):
    for relation in relations:
        kvp = relation.split('=')
        if len(kvp) == 2:
            for value in kvp[1].split(','):
                work_item.append(create_work_item_relation_patch_operation(kvp[0], value,
                    op, team_instance))
        else:
            raise ValueError('The --relations argument should consist of space separated "relation=value" pairs.')


def create_patch_operation(op, path, value=None):
    patch_operation = JsonPatchOperation()
    patch_operation.op = op
    patch_operation.path = path
    if value is not None:
        patch_operation.value = value
    return patch_operation


def create_work_item_relation_patch_operation(field, value, op, team_instance):
    relation = WorkItemRelation(
        rel=_RELATION_FIELD_ARGS[field],
        url=team_instance + '/apis/wit/workItems/' + value)
    return create_patch_operation(op=op, path='/relations/-', value=relation)