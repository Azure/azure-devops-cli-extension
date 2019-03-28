from azext_devops.dev.common.services import resolve_instance_and_project, get_pipeline_client
from azext_devops.dev.common.git import resolve_git_ref_heads
from azext_devops.dev.common.identities import resolve_identity_as_id
from .pipeline import _open_pipeline_run


def pipeline_run_show(id, open=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details of a pipeline run.
    :param id: ID of the pipeline run.
    :type id: int
    :param open: Open the build results page in your web browser.
    :type open: bool
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param project: Name or ID of the team project.
    :type project: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: :class:`<Build> <build.v5_1.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_pipeline_client(organization)
    build = client.get_build(build_id=id, project=project)
    if open:
        _open_pipeline_run(build, organization)
    return build


def pipeline_run_list(pipeline_id=None, branch=None, organization=None, project=None, detect=None, top=None,
                      result=None, status=None, reason=None, tags=None, requested_for=None):
    """List the pipeline runs in a project.
    :param pipeline_id: ID of definition to list builds for.
    :type pipeline_id: int
    :param branch: Filter by builds for this branch.
    :type branch: str
    :param top: Maximum number of builds to list.
    :type top: int
    :param result: Limit to builds with this result.
    :type result: str
    :param status: Limit to builds with this status.
    :type status: str
    :param reason: Limit to builds with this reason.
    :type reason: str
    :param tags: Limit to builds with each of the specified tags. Space separated.
    :type tags: list of str
    :param requested_for: Limit to builds requested for this user or group.
    :type requested_for: str
    :rtype: :class:`<Build> <build.v5_1.models.Build>`
    """
    organization, project = resolve_instance_and_project(
        detect=detect, organization=organization, project=project)
    client = get_pipeline_client(organization)
    if pipeline_id is not None and pipeline_id:
        pipeline_id = list(set(pipeline_id))  # make distinct
    if tags is not None and tags:
        tags = list(set(tags))  # make distinct
    builds = client.get_builds(definitions=pipeline_id,
                               project=project,
                               branch_name=resolve_git_ref_heads(branch),
                               top=top,
                               result_filter=result,
                               status_filter=status,
                               reason_filter=reason,
                               tag_filters=tags,
                               requested_for=resolve_identity_as_id(requested_for, organization))
    return builds


def pipeline_run_add_tag(run_id, tags, organization=None, project=None, detect=None):
    """Add tag(s) for a pipeline run.
    :param run_id: ID of the pipeline run.
    :type run_id: int
    :param tags: Tag(s) to be added to the pipeline run. [Comma seperated values]
    :type tags: str
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_pipeline_client(organization)
    tags = list(map(str, tags.split(',')))
    if len(tags) == 1:
        tags = client.add_build_tag(project=project, build_id=run_id, tag=tags[0])
    else:
        tags = client.add_build_tags(tags=tags, project=project, build_id=run_id)
    return tags


def pipeline_run_delete_tag(run_id, tag, organization=None, project=None, detect=None):
    """Delete a pipeline run tag.
    :param run_id: ID of the pipeline run.
    :type run_id: int
    :param tag: Tag to be deleted from the pipeline run.
    :type tag: str
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_pipeline_client(organization)
    tags = client.delete_build_tag(project=project, build_id=run_id, tag=tag)
    return tags


def pipeline_run_get_tags(run_id, organization=None, project=None, detect=None):
    """Get tags for a pipeline run.
    :param run_id: ID of the  pipeline run.
    :type run_id: int
    :rtype: list of str
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_pipeline_client(organization)
    tags = client.get_build_tags(build_id=run_id, project=project)
    return tags
