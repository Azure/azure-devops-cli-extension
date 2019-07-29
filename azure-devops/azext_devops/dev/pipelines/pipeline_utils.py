# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import get_build_client
from azext_devops.devops_sdk.v5_0.build.models import DefinitionResourceReference


def set_authorize_resource(authorized, res_id, name, res_type, organization, project):
    """
    param authorized: Boolean value set to authorize or unauthorize resource
    param id: Id of the resource to authorize
    param name: Name of the resource to authorize
    param type: Type of the resource to authorize
    param organization: Organization URL
    param project: Project Id
    """
    client = get_build_client(organization=organization)
    resources = [DefinitionResourceReference(authorized=authorized, id=res_id, name=name, type=res_type)]
    client.authorize_project_resources(resources=resources, project=project)


def get_authorize_resource(res_id, res_type, organization, project):
    """
    param id: Id of the resource to authorize
    param name: Name of the resource to authorize
    param type: Type of the resource to authorize
    param organization: Organization URL
    param project: Project Id
    """
    client = get_build_client(organization=organization)
    resource = client.get_project_resources(project=project, id=res_id, type=res_type)
    if resource:
        return resource[0].authorized
    return None
