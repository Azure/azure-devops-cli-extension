# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import dateutil


from collections import OrderedDict


def transform_builds_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_build_row(item))
    return table_output


def transform_build_table_output(result):
    table_output = [_transform_build_row(result)]
    return table_output


def _transform_build_row(row):
    from azext_devops.dev.common.git import REF_HEADS_PREFIX
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Number'] = row['buildNumber']
    table_row['Status'] = row['status']
    if row['result']:
        table_row['Result'] = row['result']
    else:
        table_row['Result'] = ' '
    table_row['Definition ID'] = row['definition']['id']
    table_row['Definition Name'] = row['definition']['name']

    if row['sourceBranch']:
        source_branch = row['sourceBranch']
        if source_branch[0:len(REF_HEADS_PREFIX)] == REF_HEADS_PREFIX:
            source_branch = source_branch[len(REF_HEADS_PREFIX):]
        table_row['Source Branch'] = source_branch
    else:
        table_row['Source Branch'] = ' '

    queued_time = dateutil.parser.parse(row['queueTime']).astimezone(dateutil.tz.tzlocal())
    table_row['Queued Time'] = str(queued_time.date()) + ' ' + str(queued_time.time())
    table_row['Reason'] = row['reason']
    return table_row


def transform_definitions_table_output(result):
    table_output = []
    include_draft_column = False
    for item in result:
        if item['quality'] == 'draft':
            include_draft_column = True
            break
    for item in result:
        table_output.append(_transform_definition_row(item, include_draft_column))
    return table_output


def transform_definition_table_output(result):
    table_output = [_transform_definition_row(result, result['quality'] == 'draft')]
    return table_output


def _transform_definition_row(row, include_draft_column=False):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    if include_draft_column:
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
    return table_row


def transform_tasks_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_task_key):
        table_output.append(_transform_task_row(item))
    return table_output


def transform_task_table_output(result):
    table_output = [_transform_task_row(result)]
    return table_output


def _transform_task_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Author'] = row['author']
    table_row['Version'] = '.'.join([str(row['version']['major']),
                                     str(row['version']['minor']),
                                     str(row['version']['patch'])])
    if row['version']['isTest']:
        table_row['Version'] += '*'
    return table_row


def _get_task_key(row):
    return row['name'].lower()
