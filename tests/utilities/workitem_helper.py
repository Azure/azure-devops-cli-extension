from azext_devops.dev.common.services import (get_work_item_tracking_client,
                                      resolve_instance,
                                      resolve_instance_and_project)

def delete_work_item(work_item_id, destroy=False, devops_organization=None, project=None, detect=None):
    """Delete a work item.
    :param work_item_id: Unique id of the work item.
    :type work_item_id: int
    :param destroy: Permanently delete this work item.
    :type destroy: bool
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: :class:`<WorkItem> <work-item-tracking.v4_0.models.WorkItemDelete>`
    """

    devops_organization = resolve_instance(detect=detect, devops_organization=devops_organization)
    client = get_work_item_tracking_client(devops_organization)
    return client.delete_work_item(work_item_id,destroy)