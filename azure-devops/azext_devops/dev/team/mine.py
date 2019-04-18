# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.dev.common.services import (get_git_client,
                                              get_work_item_tracking_client,
                                              resolve_instance_project_and_repo)
from azext_devops.devops_sdk.v5_0.work_item_tracking.models import Wiql
from azext_devops.dev.common.identities import get_current_identity
from azext_devops.devops_sdk.v5_0.git.models import GitPullRequestSearchCriteria
from azext_devops.dev.common.uri import uri_quote

logger = get_logger(__name__)

def manage_mine(work_item=None, pull_request=None, organization=None, project=None, repository=None, detect=None):
    """Manage your items (Workitems/PRs).
    :param repository: Name or ID of the repository
    :param work_item: List work-item
    :param pull_request: List pull requests
    """
    if not pull_request and not work_item:
        raise CLIError("Either work-item or pull-request must be queried.")
    repo_required = pull_request is not None
    organization, project, repository = resolve_instance_project_and_repo(detect=detect,
                                                                          organization=organization,
                                                                          project=project,
                                                                          project_required=True,
                                                                          repo=repository,
                                                                          repo_required=repo_required)
    if work_item:
        if work_item.lower() == 'assigned':
            wiql = ASSIGNED_TO_QUERY
        else:
            wiql = CREATED_BY_QUERY
        return _get_wit(organization, wiql)
    elif pull_request:
        current_identity = get_current_identity(organization)
        if pull_request.lower() == 'assigned':
            _get_prs(organization=organization, project=project, repository=repository, assigned=current_identity)
        else:
            _get_prs(organization=organization, project=project, repository=repository, creator=current_identity)



def _get_prs(organization, project, repository, creator=None, assigned=None):
    search_criteria = GitPullRequestSearchCriteria(
        creator_id=creator,
        reviewer_id=assigned) # status=status)
    client = get_git_client(organization)
    if repository is None:
        pr_list = client.get_pull_requests_by_project(project=project, search_criteria=search_criteria)
    else:
        pr_list = client.get_pull_requests(project=project, repository_id=repository,
                                           search_criteria=search_criteria)

    return {'pull_requests' : pr_list}


# pylint: disable=line-too-long
ASSIGNED_TO_QUERY = 'select [System.Id], [System.WorkItemType], [System.Title], [System.State], [System.AreaPath], [System.IterationPath] from WorkItems where [System.Id] in (@Follows)'
CREATED_BY_QUERY = 'select [System.Id], [System.WorkItemType], [System.Title], [System.State], [System.AreaPath], [System.IterationPath] from WorkItems where [System.Id] in (@Follows)'

def _get_wit(organization, wiql):
    client = get_work_item_tracking_client(organization)
    wiql_object = Wiql()
    wiql_object.query = wiql
    query_result = client.query_by_wiql(wiql=wiql_object)
    if query_result.work_items:
        _last_query_result[_LAST_QUERY_RESULT_KEY] = query_result  # store query result for table view
        safety_buffer = 100  # a buffer in the max url length to protect going over the limit
        remaining_url_length = 2048 - safety_buffer
        remaining_url_length -= len(organization)
        # following subtracts relative url, the asof parameter and beginning of id and field parameters.
        # asof value length will vary, but this should be the longest possible
        remaining_url_length -=\
            len('/_apis/wit/workItems?ids=&fields=&asOf=2017-11-07T17%3A05%3A34.06699999999999999Z')
        fields = []
        fields_length_in_url = 0
        if query_result.columns:
            for field_ref in query_result.columns:
                fields.append(field_ref.reference_name)
                if fields_length_in_url > 0:
                    fields_length_in_url += 3  # add 3 for %2C delimiter
                fields_length_in_url += len(uri_quote(field_ref.reference_name))
                if fields_length_in_url > 800:
                    logger.info("Not retrieving all fields due to max url length.")
                    break
        remaining_url_length -= fields_length_in_url
        max_work_items = 1000
        work_items_batch_size = 200
        current_batch = []
        work_items = []
        work_item_url_length = 0
        for work_item_ref in query_result.work_items:
            if len(work_items) >= max_work_items:
                logger.info("Only retrieving the first %s work items.", max_work_items)
                break
            if work_item_url_length > 0:
                work_item_url_length += 3  # add 3 for %2C delimiter
            work_item_url_length += len(str(work_item_ref.id))
            current_batch.append(work_item_ref.id)

            if remaining_url_length - work_item_url_length <= 0 or len(current_batch) == work_items_batch_size:
                # url is near max length, go ahead and send first request for details.
                # url can go over by an id length because we have a safety buffer
                current_batched_items = client.get_work_items(ids=current_batch,
                                                              as_of=query_result.as_of,
                                                              fields=fields)
                for work_item in current_batched_items:
                    work_items.append(work_item)
                current_batch = []
                work_item_url_length = 0

        if current_batch:
            current_batched_items = client.get_work_items(ids=current_batch,
                                                          as_of=query_result.as_of,
                                                          fields=fields)
            for work_item in current_batched_items:
                work_items.append(work_item)
        # put items in the same order they appeared in the initial query results
        work_items = sorted(work_items, key=_get_sort_key_from_last_query_results)
        return { 'workitems' : work_items }

def _get_sort_key_from_last_query_results(work_item):
    work_items = get_last_query_result().work_items
    i = 0
    num_items = len(work_items)
    while i < num_items:
        if work_items[i].id == work_item.id:
            return i
        i += 1
    # following lines should never be reached
    raise CLIError("Work Item {} was not found in the original query results.".format(work_item.id))


_last_query_result = {}
_LAST_QUERY_RESULT_KEY = 'value'


def get_last_query_result():
    return _last_query_result.get(_LAST_QUERY_RESULT_KEY, None)
