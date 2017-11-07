# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict

_work_item_title_truncation_length = 70


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
            if len(title) > _work_item_title_truncation_length:
                title = title[0:_work_item_title_truncation_length - 3] + '...'
            table_row['Title'] = title
        else:
            table_row['Title'] = ' '
        if 'System.AssignedTo' in row['fields']:
            table_row['Assigned To'] = row['fields']['System.AssignedTo']
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
    table_row = OrderedDict()
    max_columns = 5
    i = 0
    system_prefix = 'System.'
    length_system_prefix = len(system_prefix)
    for key in row:
        if key.startswith(system_prefix):
            column_header = key[length_system_prefix:]
        else:
            column_header = key
        table_row[column_header] = row[key]
        i += 1
        if i >= max_columns:
            # limit number of columns in table view
            break
    return table_row
