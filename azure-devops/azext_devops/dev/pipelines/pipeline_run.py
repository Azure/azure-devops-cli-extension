from azext_devops.dev.common.services import resolve_instance_and_project, get_pipeline_client
from .pipeline import _open_pipeline_run
from vsts.exceptions import VstsServiceError
from knack.util import CLIError

def pipeline_run_tag(id=None, organization=None, project=None, detect=None):
    """Tag a pipeline run.
    """
    pass


def pipeline_run_show(id, open=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details of a pipeline run.
    :param id: ID of the build.
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
    try:
        organization, project = resolve_instance_and_project(
            detect=detect, organization=organization, project=project)
        client = get_pipeline_client(organization)
        build = client.get_build(build_id=id, project=project)
        if open:
            _open_pipeline_run(build, organization)
        return build
    except VstsServiceError as ex:
        raise CLIError(ex)


def pipeline_run_list(organization=None, project=None, detect=None):
    """List the pipeline runs in a project.
    """
    pass
