# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
import dateutil

_VALUE_TRUNCATION_LENGTH = 80


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


def transform_build_tags_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_build_tags_row(item))
    return table_output


def _transform_build_tags_row(row):
    table_row = OrderedDict()
    table_row['Tags'] = row
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


def _get_task_key(row):
    return row['name'].lower()


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
    table_row['Definition Name'] = row['releaseDefinition']['name']
    table_row['Created By'] = row['createdBy']['displayName']
    created_on = dateutil.parser.parse(row['createdOn']).astimezone(dateutil.tz.tzlocal())
    table_row['Created On'] = str(created_on.date()) + ' ' + str(created_on.time())
    table_row['Status'] = row['status']
    table_row['Description'] = row['description']
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
    table_row['CreatedBy'] = row['createdBy']['displayName']
    table_row['Created On'] = row['createdOn']
    return table_row


def transform_runs_artifact_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_runs_artifact_row(item))
    return table_output


def _transform_runs_artifact_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Type'] = row['resource']['type']
    return table_row


def transform_pipelines_table_output(result):
    table_output = []
    include_draft_column = False
    for item in result:
        if item['quality'] == 'draft':
            include_draft_column = True
            break
    for item in result:
        table_output.append(_transform_pipeline_row(item, include_draft_column))
    return table_output


def transform_pipeline_table_output(result):
    table_output = [_transform_pipeline_row(result, result['quality'] == 'draft')]
    return table_output


def _transform_pipeline_row(row, include_draft_column=False):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    path = row['path']
    table_row['Path'] = path[:50] + '..' if len(path) > 50 else path
    name = row['name']
    table_row['Name'] = name[:50] + '..' if len(name) > 50 else name
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


def transform_pipeline_runs_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_run_row(item))
    return table_output


def transform_pipeline_or_run_table_output(result):
    table_output = [_transform_pipeline_or_run_row(result)]
    return table_output


def _transform_pipeline_or_run_row(row):
    if row.get("buildNumber", None):  # Hack to detect the json object is definition or run
        return _transform_pipeline_run_row(row)
    return _transform_pipeline_row(row)


def transform_pipeline_run_table_output(result):
    table_output = [_transform_pipeline_run_row(result)]
    return table_output


def _transform_pipeline_run_row(row):
    from azext_devops.dev.common.git import REF_HEADS_PREFIX
    table_row = OrderedDict()
    table_row['Run ID'] = row['id']
    table_row['Number'] = row['buildNumber']
    table_row['Status'] = row['status']
    if row['result']:
        table_row['Result'] = row['result']
    else:
        table_row['Result'] = ' '
    table_row['Pipeline ID'] = row['definition']['id']
    table_row['Pipeline Name'] = row['definition']['name']

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


def transform_pipelines_pools_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_pool_row(item))
    return table_output


def transform_pipelines_pool_table_output(result):
    table_output = [_transform_pipeline_pool_row(result)]
    return table_output


def _transform_pipeline_pool_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Is Hosted'] = row['isHosted']
    table_row['Pool Type'] = row['poolType']
    return table_row


def transform_pipelines_agents_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_agent_row(item))
    return table_output


def transform_pipelines_agent_table_output(result):
    table_output = [_transform_pipeline_agent_row(result)]
    return table_output


def _transform_pipeline_agent_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Is Enabled'] = row['enabled']
    table_row['Status'] = row['status']
    table_row['Version'] = row['version']
    return table_row


def transform_pipelines_queues_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_queue_row(item))
    return table_output


def transform_pipelines_queue_table_output(result):
    table_output = [_transform_pipeline_queue_row(result)]
    return table_output


def _transform_pipeline_queue_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Pool IsHosted'] = row['pool']['isHosted']
    table_row['Pool Type'] = row['pool']['poolType']
    return table_row


def transform_pipelines_variable_groups_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_variable_group_row(item))
    return table_output


def transform_pipelines_variable_group_table_output(result):
    table_output = [_transform_pipeline_variable_group_row(result)]
    return table_output


def _transform_pipeline_variable_group_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['Type'] = row['type']
    table_row['Description'] = row['description']
    if row.get('authorized', None) is not None:
        table_row['Is Authorized'] = row['authorized']
    table_row['Number of Variables'] = len(row['variables'])
    return table_row


def transform_pipelines_variables_table_output(result):
    table_output = []
    for key, value in result.items():
        table_output.append(_transform_pipeline_variable_row(key, value))
    return table_output


def _transform_pipeline_variable_row(key, value):
    table_row = OrderedDict()
    table_row['Name'] = key
    table_row['Allow Override'] = 'True' if value['allowOverride'] else 'False'
    table_row['Is Secret'] = 'True' if value['isSecret'] else 'False'
    val = value['value'] if value['value'] is not None else ''
    if len(val) > _VALUE_TRUNCATION_LENGTH:
        val = val[0:_VALUE_TRUNCATION_LENGTH] + '...'
    table_row['Value'] = val
    return table_row


def transform_pipelines_var_group_variables_table_output(result):
    table_output = []
    for key, value in result.items():
        table_output.append(_transform_pipeline_var_group_variable_row(key, value))
    return table_output


def _transform_pipeline_var_group_variable_row(key, value):
    table_row = OrderedDict()
    table_row['Name'] = key
    table_row['Is Secret'] = 'True' if value['isSecret'] else 'False'
    val = value['value'] if value['value'] is not None else ''
    if len(val) > _VALUE_TRUNCATION_LENGTH:
        val = val[0:_VALUE_TRUNCATION_LENGTH] + '...'
    table_row['Value'] = val
    return table_row


def transform_pipelines_folders_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pipeline_folder_row(item))
    return table_output


def transform_pipelines_folder_table_output(result):
    table_output = [_transform_pipeline_folder_row(result)]
    return table_output


def _transform_pipeline_folder_row(row):
    table_row = OrderedDict()
    table_row['Path'] = row['path']
    val = row['description'] if row['description'] is not None else ''
    if len(val) > _VALUE_TRUNCATION_LENGTH:
        val = val[0:_VALUE_TRUNCATION_LENGTH] + '...'
    table_row['Description'] = val
    return table_row
