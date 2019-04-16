# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
from collections import OrderedDict
from azext_devops.dev.common.format import trim_for_display, date_time_to_only_date


def transform_extension_search_results_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_extension_search_result_row(item))
    return table_output


def _transform_extension_search_result_row(row):
    table_row = OrderedDict()
    table_row['Publisher Id'] = row['publisher']['publisherName']
    table_row['Extension Id'] = row['extensionName']
    table_row['Name'] = row['displayName']

    return table_row


def transform_extension_table_output(result):
    table_output = [_transform_extension_row(result)]
    return table_output


def transform_extensions_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_extension_key):
        table_output.append(_transform_extension_row(item))
    return table_output


def _transform_extension_row(row):
    table_row = OrderedDict()
    table_row['Publisher Id'] = trim_for_display(row['publisherId'], 10)
    table_row['Extension Id'] = trim_for_display(row['extensionId'], 20)
    table_row['Name'] = trim_for_display(row['extensionName'], 20)
    table_row['Version '] = trim_for_display(row['version'], 20)
    table_row['Last Updated '] = date_time_to_only_date(row['lastPublished'])
    table_row['States'] = trim_for_display(row['installState']['flags'], 20)
    table_row['Flags'] = trim_for_display(row['flags'], 20)

    return table_row


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


def transform_groups_table_output(result):
    table_output = []
    if result['continuationToken'] is not None:
        print('Showing only 500 groups. ' +
              'To list next set of groups use this token as --continuation-token argument and run the command again.' +
              ' TOKEN:', result['continuationToken'])
    for item in result['graphGroups']:
        table_output.append(_transform_group_row(item))
    return table_output


def transform_group_table_output(result):
    table_output = [_transform_group_row(result)]
    return table_output


def _transform_group_row(row):
    table_row = OrderedDict()
    table_row['Display Name'] = row['principalName']
    table_row['Descriptor'] = row['descriptor']
    return table_row


def transform_memberships_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_membership_row(result[item]))
    return table_output


def _transform_membership_row(row):
    table_row = OrderedDict()
    if row['subjectKind'] == 'user':
        table_row['Name'] = row['displayName']
    else:
        table_row['Name'] = row['principalName']
    table_row['Type'] = row['subjectKind']
    table_row['Email'] = row['mailAddress']
    table_row['Descriptor'] = row['descriptor']
    return table_row


def transform_namespaces_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_namespace_row(item))
    return table_output


def _transform_namespace_row(row):
    table_row = OrderedDict()
    table_row['Id'] = row['namespaceId']
    table_row['Name'] = row['name']
    return table_row


def transform_namespace_table_output(result):
    table_output = []
    for item in result[0]['actions']:
        table_output.append(_transform_namespace_details_row(item))
    return table_output


def _transform_namespace_details_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['name']
    table_row['Permission Description'] = row['displayName']
    table_row['Permission Bit'] = row['bit']
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


def transform_wikis_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_wiki_key):
        table_output.append(_transform_wiki_row(item))
    return table_output


def transform_wiki_table_output(result):
    table_output = [_transform_wiki_row(result)]
    return table_output


def _transform_wiki_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Type'] = row['type']
    return table_row


def transform_wiki_page_table_output(result):
    table_output = [_transform_wiki_page_row(result)]
    return table_output


def _transform_wiki_page_row(row):
    table_row = OrderedDict()
    table_row['ETag'] = row['eTag']
    table_row['Git Path'] = row['page']['gitItemPath']
    table_row['Is Parent'] = row['page']['isParentPage']
    table_row['order'] = row['page']['order']
    return table_row


def transform_team_members_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_member_key):
        table_output.append(_transform_team_member_row(item))
    return table_output


def _transform_team_member_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['identity']['id']
    table_row['Name'] = row['identity']['displayName']
    table_row['Email'] = row['identity']['uniqueName']

    return table_row


def transform_users_table_output(result):
    members = result['members']
    table_output = []
    for item in members:
        table_output.append(_transform_user_row(item))
    return table_output


def transform_user_table_output(result):
    table_output = [_transform_user_row(result)]
    return table_output


def _transform_user_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Display Name'] = row['user']['displayName']
    table_row['Email'] = row['user']['mailAddress']
    table_row['License Type'] = row['accessLevel']['accountLicenseType']
    table_row['Access Level'] = row['accessLevel']['licenseDisplayName']
    table_row['Status'] = row['accessLevel']['status']
    return table_row


def _get_extension_key(extension):
    return extension['extensionName'].lower()


def _get_service_endpoint_key(service_endpoint_row):
    return service_endpoint_row['name'].lower()


def _get_project_key(project_row):
    return project_row['name'].lower()


def _get_team_key(team_row):
    return team_row['name'].lower()


def _get_wiki_key(wiki_row):
    return wiki_row['name'].lower()


def _get_member_key(member_row):
    return member_row['identity']['uniqueName'].lower()
