# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


_WORK_ITEM_TITLE_TRUNCATION_LENGTH = 70
_PATH_TRUNCATION_LENGTH = 50


def transform_work_item_relation_type_table_output(result):
    table_output = []
    for item in result:
        table_row = OrderedDict()
        table_row['Name'] = item['name']
        table_row['ReferenceName'] = item['referenceName']
        table_row['Enabled'] = item['attributes']['enabled']
        table_row['Usage'] = item['attributes']['usage']
        table_output.append(table_row)

    return table_output


def transform_work_item_relations(result):
    if result['relations'] is None:
        return []

    relations = result['relations']
    table_output = []
    for item in relations:
        table_row = OrderedDict()
        table_row['Relation Type'] = item['rel']
        table_row['Url'] = item['url']
        table_output.append(table_row)

    return table_output


def transform_work_items_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_work_items_row(item))
    return table_output


def transform_work_item_table_output(result):
    table_output = [_transform_work_items_row(result)]
    return table_output


def _transform_work_items_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    if 'fields' in row:
        if 'System.WorkItemType' in row['fields']:
            table_row['Type'] = row['fields']['System.WorkItemType']
        else:
            table_row['Type'] = ' '
        if 'System.Title' in row['fields']:
            title = row['fields']['System.Title']
            if len(title) > _WORK_ITEM_TITLE_TRUNCATION_LENGTH:
                title = title[0:_WORK_ITEM_TITLE_TRUNCATION_LENGTH - 3] + '...'
            table_row['Title'] = title
        else:
            table_row['Title'] = ' '
        if 'System.AssignedTo' in row['fields']:
            table_row['Assigned To'] = row['fields']['System.AssignedTo']['uniqueName']
        else:
            table_row['Assigned To'] = ' '
        if 'System.State' in row['fields']:
            table_row['State'] = row['fields']['System.State']
        else:
            table_row['State'] = ' '

    else:
        table_row['Type'] = ' '
        table_row['Title'] = ' '
        table_row['Assigned To'] = ' '
        table_row['State'] = ' '
    return table_row


def transform_work_item_query_result_table_output(result):
    table_output = []
    for item in result:
        if 'fields' in item:
            table_output.append(transform_work_item_query_result_row_output(item['fields']))
    return table_output


def transform_work_item_query_result_row_output(row):
    from azext_devops.dev.boards.work_item import get_last_query_result
    table_row = OrderedDict()
    max_columns = 5
    i = 0
    for field_reference in get_last_query_result().columns:
        if field_reference.reference_name in row:
            if row[field_reference.reference_name] == 0:
                # knack hides column values that are equal to numeric 0.
                table_row[field_reference.name] = '0'
            else:
                if field_reference.reference_name == 'System.Title':
                    title = row[field_reference.reference_name]
                    if len(title) > _WORK_ITEM_TITLE_TRUNCATION_LENGTH:
                        title = title[0:_WORK_ITEM_TITLE_TRUNCATION_LENGTH - 3] + '...'
                    table_row[field_reference.name] = title
                else:
                    table_row[field_reference.name] = row[field_reference.reference_name]
        else:
            table_row[field_reference.name] = ' '
        i += 1
        if i >= max_columns:
            # limit number of columns in table view
            break
    return table_row


def transform_work_item_team_iterations_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_team_iteration_row(item))
    return table_output


def transform_work_item_team_iteration_table_output(result):
    table_output = [_transform_team_iteration_row(result)]
    return table_output


def _transform_team_iteration_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    if row['attributes']['startDate'] is None:
        table_row['Start Date'] = ''
    else:
        table_row['Start Date'] = row['attributes']['startDate']
    if row['attributes']['finishDate'] is None:
        table_row['Finish Date'] = ''
    else:
        table_row['Finish Date'] = row['attributes']['finishDate']
    table_row['Path'] = row['path']
    return table_row


def transform_work_item_project_classification_nodes_table_output(response):
    table_op = []
    table_op = transform_work_item_project_classification_nodes_table_output_recursive(response, table_op)
    return table_op


def transform_work_item_project_classification_nodes_table_output_recursive(result, table_output):
    table_output.append(_transform_project_classification_node_row(result))    
    if result['children']:
        for item in result['children']:
            table_output = transform_work_item_project_classification_nodes_table_output_recursive(item, table_output)
    return table_output


def _transform_project_classification_node_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Identifier'] = row['identifier']
    table_row['Name'] = row['name']
    if row['attributes']:
        table_row['Start Date'] = row['attributes']['startDate']
        table_row['Finish Date'] = row['attributes']['finishDate']
    path = row['path']
    if len(path) > _PATH_TRUNCATION_LENGTH:
        path = path[0:_PATH_TRUNCATION_LENGTH - 3] + '...'
    table_row['Path'] = path
    table_row['Has Children'] = row['hasChildren']
    return table_row
