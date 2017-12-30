# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.git.v4_0.models.git_annotated_tag import GitAnnotatedTag
from vsts.git.v4_0.models.git_version_descriptor import GitVersionDescriptor
from vsts.git.v4_0.models.git_object import GitObject
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_git_client,
                                      resolve_instance,
                                      resolve_instance_project_and_repo)


def create_tag(name, object_id, message=None, repository=None, team_instance=None, project=None, detect=None):
    """Create a tag.
    :param str name: Name of the annotated tag.
    :param str object_id: ID of the object the tag is pointing to.
    :param str message: Message of the annotated tag.
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)

        tagged_object = GitObject(object_id)
        tag = GitAnnotatedTag(name=name,
                              message=message,
                              tagged_object=tagged_object)
        return client.create_annotated_tag(tag, project, repository)
    except Exception as ex:
        handle_command_exception(ex)


def show_tag(object_id, repository=None, team_instance=None, project=None, detect=None):
    """Get the details of a tag.
    :param str object_id: ID of the tag.
    :param str repository: Name or ID of the repository.
    :param str team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project collection.
    :param str project: Name or ID of the project.
    :param str detect: When 'On' unsupplied arg values will be detected from the current working directory's repo.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        return client.get_annotated_tag(project=project,
                                        repository_id=repository,
                                        object_id=object_id)
    except Exception as ex:
        handle_command_exception(ex)