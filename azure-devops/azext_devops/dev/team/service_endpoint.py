# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack.log import get_logger
from knack.util import CLIError
from vsts.exceptions import VstsServiceError
from vsts.service_endpoint.v4_1.models.service_endpoint import ServiceEndpoint
from vsts.service_endpoint.v4_1.models.endpoint_authorization import EndpointAuthorization
from azext_devops.dev.common.services import get_service_endpoint_client, resolve_instance_and_project

from .const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                    SERVICE_ENDPOINT_TYPE_GITHUB,
                    SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                    SERVICE_ENDPOINT_TYPE_AZURE_RM)

logger = get_logger(__name__)

def list_service_endpoints(devops_organization=None, project=None, detect=None):
    """List service endpoints in a project.
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: list of :class:`VssJsonCollectionWrapper <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        client = get_service_endpoint_client(devops_organization)
        return client.get_service_endpoints(project)

    except VstsServiceError as ex:
        raise CLIError(ex)

def show_service_endpoint(service_endpoint_id, devops_organization=None, project=None, detect=None):
    """Get the details of a service endpoint.
    :param service_endpoint_id: ID of the service endpoint.
    :type service_endpoint_id: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        client = get_service_endpoint_client(devops_organization)
        return client.get_service_endpoint_details(project, service_endpoint_id)

    except VstsServiceError as ex:
        raise CLIError(ex)

def create_service_endpoint(service_endpoint_type, authorization_scheme, name,
                            github_access_token=None, github_url=None,
                            azure_rm_tenant_id=None, azure_rm_service_principal_id=None,
                            azure_rm_service_prinicipal_key=None, azure_rm_subscription_id=None,
                            azure_rm_subscription_name=None, devops_organization=None,
                            project=None, detect=None):
    """Create a service endpoint
    :param service_endpoint_type: Type of service endpoint
    :type service_endpoint_type: str
    :param name: Name of service endpoint to create
    :type name: str
    :param authorization_scheme: Authorization to be used in service endpoint creation
     Github service endpoint supports PersonalAccessToken
     AzureRm service endpoint supports ServicePrincipal
    :type authorization_scheme: str
    :param github_access_token: PAT token of github for creating github service endpoint
    :type github_access_token: str
    :param github_url: Url for github for creating service endpoint
    :type github_url: str
    :param azure_rm_tenant_id: tenant id for creating azure rm service endpoint
    :type azure_rm_tenant_id: str
    :param azure_rm_service_principal_id: service principal id for creating azure rm service endpoint
    :type azure_rm_service_principal_id: str
    :param azure_rm_service_prinicipal_key: key/password for service principal used to create azure rm service endpoint
    :type azure_rm_service_prinicipal_key: str
    :param azure_rm_subscription_id: subscription id for azure rm service endpoint
    :type azure_rm_subscription_id: str
    :param azure_rm_subscription_name: name of azure subscription for azure rm service endpoint
    :type azure_rm_subscription_name: str
    :param devops_organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type devops_organization: str
    :param project: Name or ID of the project.
    :type project: str
    :param detect: Automatically detect organization. Default is "on".
    :type detect: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    try:
        devops_organization, project = resolve_instance_and_project(detect=detect,
                                                                    devops_organization=devops_organization,
                                                                    project=project)
        client = get_service_endpoint_client(devops_organization)

        if (service_endpoint_type == SERVICE_ENDPOINT_TYPE_GITHUB
                and authorization_scheme == SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN):
            service_endpoint_authorization = EndpointAuthorization(
                parameters={'accessToken':github_access_token},
                scheme=SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN)
            service_endpoint_to_create = ServiceEndpoint(
                authorization=service_endpoint_authorization,
                name=name, type=SERVICE_ENDPOINT_TYPE_GITHUB, url=github_url)
            return client.create_service_endpoint(service_endpoint_to_create, project)
        elif (service_endpoint_type == SERVICE_ENDPOINT_TYPE_AZURE_RM
              and authorization_scheme == SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL):
            service_endpoint_authorization = EndpointAuthorization(
                parameters={
                    'tenantid':azure_rm_tenant_id,
                    'serviceprincipalid':azure_rm_service_principal_id,
                    'authenticationType':'spnKey',
                    'serviceprincipalkey':azure_rm_service_prinicipal_key
                    },
                scheme=SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL)
            service_endpoint_data = {
                'subscriptionId':azure_rm_subscription_id,
                'subscriptionName':azure_rm_subscription_name,
                'environment':'AzureCloud',
                'creationMode':'Manual'
            }
            service_endpoint_to_create = ServiceEndpoint(
                authorization=service_endpoint_authorization, data=service_endpoint_data,
                name=name, type=SERVICE_ENDPOINT_TYPE_AZURE_RM, url='https://management.azure.com/')
            return client.create_service_endpoint(service_endpoint_to_create, project)
        else:
            raise CLIError('this combination of endpoint type is not supported with this authorization scheme')

    except VstsServiceError as ex:
        raise CLIError(ex)
