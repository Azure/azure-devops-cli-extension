# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
import dateutil.parser
import dateutil.tz


_PR_TITLE_TRUNCATION_LENGTH = 50
_WORK_ITEM_TITLE_TRUNCATION_LENGTH = 70


def transform_pull_requests_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_pull_request_row(item))
    return table_output


def transform_pull_request_table_output(result):
    table_output = [_transform_pull_request_row(result)]
    return table_output


def _transform_pull_request_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['pullRequestId']
    table_row['Created'] = dateutil.parser.parse(row['creationDate']).astimezone(dateutil.tz.tzlocal()).date()
    table_row['Creator'] = row['createdBy']['uniqueName']
    title = row['title']
    if len(title) > _PR_TITLE_TRUNCATION_LENGTH:
        title = title[0:_PR_TITLE_TRUNCATION_LENGTH - 3] + '...'
    table_row['Title'] = title
    table_row['Status'] = row['status'].capitalize()
    table_row['Repository'] = row['repository']['name']
    return table_row


def transform_reviewers_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_reviewer_table_key):
        table_output.append(_transform_reviewer_row(item))
    return table_output


def transform_reviewer_table_output(result):
    table_output = [_transform_reviewer_row(result)]
    return table_output


def _get_reviewer_table_key(row):
    if row['isRequired']:
        key = '0'
    else:
        key = '1'
    key += row['displayName'].lower()
    return key


_UNIQUE_NAME_GROUP_PREFIX = 'vstfs:///'


def _transform_reviewer_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['displayName']
    if row['uniqueName'][0:len(_UNIQUE_NAME_GROUP_PREFIX)] != _UNIQUE_NAME_GROUP_PREFIX:
        table_row['Email'] = row['uniqueName']
    else:
        table_row['Email'] = ' '
    table_row['ID'] = row['id']
    table_row['Vote'] = _get_vote_from_vote_number(int(row['vote']))
    if row['isRequired']:
        table_row['Required'] = 'True'
    else:
        table_row['Required'] = 'False'
    return table_row


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
        if 'System.AssignedTo' in row['fields']:
            table_row['Assigned To'] = row['fields']['System.AssignedTo']
        else:
            table_row['Assigned To'] = ' '
        if 'System.State' in row['fields']:
            table_row['State'] = row['fields']['System.State']
        else:
            table_row['State'] = ' '
        if 'System.Title' in row['fields']:
            title = row['fields']['System.Title']
            if len(title) > _WORK_ITEM_TITLE_TRUNCATION_LENGTH:
                title = title[0:_WORK_ITEM_TITLE_TRUNCATION_LENGTH - 3] + '...'
            table_row['Title'] = title
        else:
            table_row['Title'] = ' '
    else:
        table_row['Assigned To'] = ' '
        table_row['State'] = ' '
        table_row['Title'] = ' '
    return table_row


def _get_vote_from_vote_number(number):
    if number == 10:
        return 'Approved'
    if number == 5:
        return 'Approved with suggestions'
    if number == -5:
        return 'Waiting for author'
    if number == -10:
        return 'Rejected'
    return ' '


def transform_policies_table_output(result):
    from azext_devops.dev.common.identities import (ensure_display_names_in_cache,
                                                    get_display_name_from_identity_id)
    from azext_devops.dev.common.services import get_first_vss_instance_uri
    table_output = []
    reviewer_ids = []
    for item in result:
        reviewer_id = get_required_reviewer_from_evaluation_row(item)
        if reviewer_id is not None:
            reviewer_ids.append(get_required_reviewer_from_evaluation_row(item))
    organization = get_first_vss_instance_uri()
    ensure_display_names_in_cache(organization, reviewer_ids)
    for item in result:
        reviewer_id = get_required_reviewer_from_evaluation_row(item)
        if reviewer_id is not None:
            display_name = get_display_name_from_identity_id(organization, reviewer_id)
        else:
            display_name = None
        if display_name is not None:
            table_output.append(_transform_policy_row(item, display_name))
        else:
            table_output.append(_transform_policy_row(item))
    return sorted(table_output, key=_get_policy_table_key)


def get_required_reviewer_from_evaluation_row(row):
    if 'requiredReviewerIds' in row['configuration']['settings'] and len(
            row['configuration']['settings']['requiredReviewerIds']) == 1:
        return row['configuration']['settings']['requiredReviewerIds'][0]
    return None


def transform_policy_table_output(result):
    table_output = [_transform_policy_row(result)]
    return table_output


def _get_policy_table_key(row):
    if row['Blocking'] == 'True':
        key = '0'
    else:
        key = '1'
    key += row['Policy'].lower()
    return key


def _transform_policy_row(row, identity_display_name=None):
    table_row = OrderedDict()
    table_row['Evaluation ID'] = row['evaluationId']
    table_row['Policy'] = _build_policy_name(row, identity_display_name)
    if row['configuration']['isBlocking']:
        table_row['Blocking'] = 'True'
    else:
        table_row['Blocking'] = 'False'
    table_row['Status'] = _convert_policy_status(row['status'])
    if row['context'] and 'isExpired' in row['context']:
        if row['context']['isExpired']:
            table_row['Expired'] = 'True'
        else:
            table_row['Expired'] = 'False'
    else:
        # Not Applicable
        table_row['Expired'] = ' '
    if row['context'] and 'buildId' in row['context'] and row['context']['buildId'] is not None:
        table_row['Build ID'] = row['context']['buildId']
    else:
        table_row['Build ID'] = ' '
    return table_row


def _build_policy_name(row, identity_display_name=None):
    policy = row['configuration']['type']['displayName']
    if 'displayName' in row['configuration']['settings']\
            and row['configuration']['settings']['displayName'] is not None:
        policy += ' (' + row['configuration']['settings']['displayName'] + ')'
    if 'minimumApproverCount' in row['configuration']['settings']\
            and row['configuration']['settings']['minimumApproverCount'] is not None:
        policy += ' (' + str(row['configuration']['settings']['minimumApproverCount']) + ')'
    if identity_display_name is not None and 'requiredReviewerIds' in row['configuration']['settings']:
        if len(row['configuration']['settings']['requiredReviewerIds']) > 1:
            policy += ' (' + str(len(row['configuration']['settings']['requiredReviewerIds'])) + ')'
        elif len(row['configuration']['settings']['requiredReviewerIds']) == 1:
            policy += ' (' + identity_display_name + ')'
    return policy


def _convert_policy_status(status):
    if status == 'queued':
        return ' '
    return status.capitalize()


def transform_refs_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_repo_key):
        table_output.append(_transform_ref_row(item))
    return table_output


def transform_ref_table_output(result):
    table_output = [_transform_ref_row(result)]
    return table_output


def _transform_ref_row(row):
    from azext_devops.dev.common.git import get_ref_name_from_ref
    table_row = OrderedDict()
    if 'objectId' in row:
        table_row['Object ID'] = row['objectId']
    if ('oldObjectId' in row) and ('newObjectId' in row):
        old_id = row['oldObjectId']
        new_id = row['newObjectId']
        if old_id == '0000000000000000000000000000000000000000':
            table_row['Object ID'] = new_id
        elif new_id == '0000000000000000000000000000000000000000':
            table_row['Object ID'] = old_id
        else:
            table_row['Old Object ID'] = old_id
            table_row['New Object ID'] = new_id
    table_row['Name'] = get_ref_name_from_ref(row['name'])
    return table_row


def transform_repos_table_output(result):
    table_output = []
    for item in sorted(result, key=_get_repo_key):
        table_output.append(_transform_repo_row(item))
    return table_output


def transform_repo_table_output(result):
    table_output = [_transform_repo_row(result)]
    return table_output


def transform_repo_import_table_output(result):
    table_output = OrderedDict()
    table_output['Name'] = result['repository']['name']
    table_output['Project'] = result['repository']['project']['name']
    table_output['Import Status'] = result['status']
    return table_output


def _transform_repo_row(row):
    from azext_devops.dev.common.git import get_branch_name_from_ref
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    if row['defaultBranch']:
        table_row['Default Branch'] = get_branch_name_from_ref(row['defaultBranch'])
    else:
        table_row['Default Branch'] = ' '
    table_row['Project'] = row['project']['name']
    return table_row


def _get_repo_key(repo_row):
    return repo_row['name']
