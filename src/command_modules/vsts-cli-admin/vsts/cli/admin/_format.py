# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_banner_table_output(result):
    table_output = []
    for k, v in result.items():
        table_output.append(_transform_banner_row(k, v))
    return table_output


def _transform_banner_row(key, value):
    table_row = OrderedDict()
    table_row['ID'] = key
    if 'message' in value:
        table_row['Message'] = value['message']
    else:
        table_row['Message'] = ' '
    if 'level' in value:
        level = value['level']
        if level is not None and level != '':
            level = level[0:1].upper() + level[1:]
        table_row['Level'] = level
    else:
        table_row['Level'] = 'Info'
    if 'expirationDate' in value:
        table_row['Expiration Date'] = value['expirationDate']
    else:
        table_row['Expiration Date'] = ' '
    return table_row
