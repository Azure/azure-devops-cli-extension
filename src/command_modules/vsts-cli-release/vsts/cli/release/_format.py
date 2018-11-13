# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import dateutil


from collections import OrderedDict


def transform_releases_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_release_row(item))
    return table_output


def transform_release_table_output(result):
    table_output = [_transform_release_row(result)]
    return table_output


def _transform_release_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Status'] = row['status']
    table_row['Definition Name'] = row['releaseDefinition']['name']
    table_row['Created on'] = row['createdOn']
    return table_row


def transform_release_definitions_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_release_definition_row(item))
    return table_output


def transform_release_definition_table_output(result):
    table_output = [_transform_release_definition_row(result)]
    return table_output


def _transform_release_definition_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Created On'] = row['createdOn']
    return table_row