from azext_dev.dev.common.services import (get_work_item_tracking_client,
                                      resolve_instance,
                                      resolve_instance_and_project)

def delete_work_item(work_item_id, destroy=False, team_instance=None, project=None, detect=None):
    """Delete a work item.
    :param work_item_id: Unique id of the work item.
    :type work_item_id: str
    :param destroy: Permanently delete this work item.
    :type destroy: bool
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItemDelete>`
    """

    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    client = get_work_item_tracking_client(team_instance)
    return client.delete_work_item(work_item_id,destroy)