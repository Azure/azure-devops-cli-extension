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
    from .project import (PROCESS_TEMPLATE_CAPABILITY_NAME,
                          VERSION_CONTROL_CAPABILITY_NAME,
                          VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME)
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Visibility'] = row['visibility'].capitalize()

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


def transform_service_endpoints_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_service_endpoint_key):
        table_output.append(_transform_service_endpoint_row(item))
    return table_output


def _transform_service_endpoint_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Type'] = row['type']
    table_row['Is Ready'] = row['isReady']
    table_row['Created By'] = row['createdBy']['displayName']

    return table_row


def transform_teams_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_team_key):
        table_output.append(_transform_team_row(item))
    return table_output


def transform_team_table_output(result):
    table_output = [_transform_team_row(result)]
    return table_output


def _transform_team_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Description'] = row['description']

    return table_row


def transform_team_members_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_member_key):
        table_output.append(_transform_team_member_row(item))
    return table_output


def _transform_team_member_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['displayName']
    table_row['Email'] = row['uniqueName']

    return table_row


def _get_service_endpoint_key(service_endpoint_row):
    return service_endpoint_row['name'].lower()


def _get_project_key(project_row):
    return project_row['name'].lower()


def _get_team_key(team_row):
    return team_row['name'].lower()


def _get_member_key(member_row):
    return member_row['uniqueName'].lower()
