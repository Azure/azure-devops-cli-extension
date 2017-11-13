# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import dateutil


from collections import OrderedDict
from vsts.cli.common.git import REF_HEADS_PREFIX


def transform_builds_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_build_row(item))
    return table_output


def transform_build_table_output(result):
    table_output = [_transform_build_row(result)]
    return table_output


def _transform_build_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Number'] = row['buildNumber']
    table_row['Definition ID'] = row['definition']['id']
    table_row['Definition Name'] = row['definition']['name']
    source_branch = row['sourceBranch']
    if source_branch[0:len(REF_HEADS_PREFIX)] == REF_HEADS_PREFIX:
        source_branch = source_branch[len(REF_HEADS_PREFIX):]
    table_row['Source Branch'] = source_branch
    table_row['Status'] = row['status']
    queued_time = dateutil.parser.parse(row['queueTime']).astimezone(dateutil.tz.tzlocal())
    table_row['Queued Time'] = str(queued_time.date()) + ' ' + str(queued_time.time())
    table_row['Priority'] = row['priority']
    table_row['Reason'] = row['reason']
    return table_row


def transform_definitions_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_definition_row(item))
    return table_output


def transform_definition_table_output(result):
    table_output = [_transform_definition_row(result)]
    return table_output


def _transform_definition_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    if row['quality'] == 'draft':
        table_row['Draft'] = True
    else:
        table_row['Draft'] = ' '
    if row['queueStatus']:
        table_row['Status'] = row['queueStatus']
    else:
        table_row['Status'] = ' '
    if row['queue']:
        table_row['Default Queue'] = row['queue']['name']
    else:
        table_row['Default Queue'] = ' '
    table_row['Created'] = dateutil.parser.parse(row['createdDate']).astimezone(dateutil.tz.tzlocal()).date()
    if row['authoredBy']:
        table_row['Last Modified By'] = row['authoredBy']['displayName']
    else:
        table_row['Last Modified By'] = ' '
    return table_row
