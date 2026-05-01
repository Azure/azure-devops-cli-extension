# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
from azext_devops.dev.common.format import trim_for_display, date_time_to_only_date


_TARGET_TRUNCATION_LENGTH = 60


def transform_message_output(result):
    if result is None:
        return []
    if isinstance(result, dict) and 'message' in result:
        row = OrderedDict()
        row['Message'] = result['message']
        return [row]
    return transform_migration_table_output(result)


def transform_migrations_table_output(result):
    migrations = _unwrap_migration_list(result)
    table_output = []
    for item in migrations:
        table_output.append(_transform_migration_row(item))
    return table_output


def transform_migration_table_output(result):
    if result is None:
        return []
    return [_transform_migration_row(result)]


def transform_cutover_review_table_output(result):
    if not isinstance(result, dict):
        return []

    failed_count = result.get('failedCount')
    blocked_count = result.get('blockedCount')
    pending_count = result.get('pendingCount')
    total_unprocessed = result.get('totalUnprocessedCount')
    failed_items = result.get('failedItems') if isinstance(result.get('failedItems'), list) else []

    if not failed_items:
        row = OrderedDict()
        row['FailedCount'] = failed_count
        row['BlockedCount'] = blocked_count
        row['PendingCount'] = pending_count
        row['TotalUnprocessedCount'] = total_unprocessed
        row['State'] = None
        row['Type'] = None
        row['PullRequestUrl'] = None
        return [row]

    rows = []
    for index, item in enumerate(failed_items):
        row = OrderedDict()
        row['FailedCount'] = failed_count if index == 0 else None
        row['BlockedCount'] = blocked_count if index == 0 else None
        row['PendingCount'] = pending_count if index == 0 else None
        row['TotalUnprocessedCount'] = total_unprocessed if index == 0 else None
        row['State'] = item.get('state') if isinstance(item, dict) else None
        row['Type'] = item.get('type') if isinstance(item, dict) else None
        row['PullRequestUrl'] = item.get('pullRequestUrl') if isinstance(item, dict) else None
        rows.append(row)

    return rows


def _unwrap_migration_list(result):
    if isinstance(result, dict) and 'value' in result:
        return result['value']
    if isinstance(result, list):
        return result
    return []


def _transform_migration_row(row):
    table_row = OrderedDict()
    table_row['RepositoryId'] = row.get('repositoryId')
    table_row['TargetRepository'] = trim_for_display(row.get('targetRepository'),
                                                     _TARGET_TRUNCATION_LENGTH)
    table_row['Status'] = row.get('status')
    table_row['Stage'] = row.get('stage')
    table_row['ValidateOnly'] = row.get('validateOnly')
    table_row['CutoverDate'] = date_time_to_only_date(row.get('scheduledCutoverDate'))
    table_row['CodeSyncDate'] = date_time_to_only_date(row.get('codeSyncDate'))
    table_row['PrSyncDate'] = date_time_to_only_date(row.get('pullRequestSyncDate'))
    return table_row
