# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_projects_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_project_key):
        table_output.append(_transform_project_row(item))
    return table_output


def transform_project_table_output(result):
    table_output = [_transform_project_row(result)]
    return table_output


def _transform_project_row(row):
    from azdos.cli.team.common.project import (PROCESS_TEMPLATE_CAPABILITY_NAME,
                                              VERSION_CONTROL_CAPABILITY_NAME,
                                              VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME)
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['State'] = row['state']

    if 'capabilities' in row:
        capabilities = row['capabilities']
        if PROCESS_TEMPLATE_CAPABILITY_NAME in capabilities:
            process_capabilities = capabilities[PROCESS_TEMPLATE_CAPABILITY_NAME]
            if 'templateName' in process_capabilities:
                table_row['Process'] = process_capabilities['templateName']
        if VERSION_CONTROL_CAPABILITY_NAME in capabilities:
            version_capabilities = capabilities[VERSION_CONTROL_CAPABILITY_NAME]
            if VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME in version_capabilities:
                table_row['Source Control'] = version_capabilities[VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME]

    return table_row


def _get_project_key(project_row):
    return project_row['name'].lower()
