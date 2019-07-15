# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import os
from knack.log import get_logger
from knack.prompting import prompt_pass
from azext_devops.devops_sdk.v5_0.service_endpoint.models import ServiceEndpoint, EndpointAuthorization
from azext_devops.dev.common.services import get_service_endpoint_client, resolve_instance_and_project
from azext_devops.dev.common.const import CLI_ENV_VARIABLE_PREFIX, AZ_DEVOPS_GITHUB_PAT_ENVKEY
from azext_devops.dev.common.prompting import verify_is_a_tty_or_raise_error

from .const import (SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN,
                    SERVICE_ENDPOINT_TYPE_GITHUB,
                    SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL,
                    SERVICE_ENDPOINT_TYPE_AZURE_RM)

logger = get_logger(__name__)


def list_service_endpoints(organization=None, project=None, detect=None):
    """List service endpoints in a project.
    :rtype: list of :class:`VssJsonCollectionWrapper <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)
    return client.get_service_endpoints(project)


def show_service_endpoint(id, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Get the details of a service endpoint.
    :param id: ID of the service endpoint.
    :type id: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)
    return client.get_service_endpoint_details(project, id)


def delete_service_endpoint(id, deep=False, organization=None, project=None, detect=None):  # pylint: disable=redefined-builtin
    """Deletes service endpoint
    :param id: Id of the service endpoint to delete.
    :type id: str
    :param deep: Specific to AzureRM endpoint created in Automatic flow. When it is specified,
    this will also delete corresponding AAD application in Azure.
    :type deep: bool
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)
    return client.delete_service_endpoint(project, id, deep)

def create_azurerm_service_endpoint(name, azure_rm_tenant_id, azure_rm_service_principal_id,
                                    azure_rm_subscription_id, azure_rm_subscription_name,
                                    azure_rm_service_principal_certificate_path=None,
                                    organization=None, project=None, detect=None):
    """ Create an Azure RM type service endpoint.
    :param name: Name of service endpoint to create
    :type name: str
    :param azure_rm_tenant_id: tenant id for creating azure rm service endpoint
    :type azure_rm_tenant_id: str
    :param azure_rm_service_principal_id: service principal id for creating azure rm service endpoint
    :type azure_rm_service_principal_id: str
    :param azure_rm_subscription_id: subscription id for azure rm service endpoint
    :type azure_rm_subscription_id: str
    :param azure_rm_service_principal_certificate_path: Path to (.pem) which is certificate.
     Create using command "openssl pkcs12 -in file.pfx -out file.pem -nodes -password pass:<password_here>"
    :type azure_rm_service_principal_certificate_path: str
    :param azure_rm_subscription_name: name of azure subscription for azure rm service endpoint
    :type azure_rm_subscription_name: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)

    service_endpoint_authorization = EndpointAuthorization(
        parameters={'tenantid': azure_rm_tenant_id,
                    'serviceprincipalid': azure_rm_service_principal_id},
        scheme=SERVICE_ENDPOINT_AUTHORIZATION_SERVICE_PRINCIPAL)

    if azure_rm_service_principal_certificate_path is None:
        AZURE_RM_SP_KEY_END_VARIABLE_NAME = CLI_ENV_VARIABLE_PREFIX + 'AZURE_RM_SERVICE_PRINCIPAL_KEY'
        if AZURE_RM_SP_KEY_END_VARIABLE_NAME not in os.environ:
            error_message = 'Please specify azure service principal key in ' + AZURE_RM_SP_KEY_END_VARIABLE_NAME +\
                            ' environment variable in non-interactive mode or use ' +\
                            '--azure-rm-service-principal-certificate-path'
            verify_is_a_tty_or_raise_error(error_message)
            azure_rm_service_principal_key = prompt_pass('Azure RM service principal key:', confirm=True)
        else:
            azure_rm_service_principal_key = os.environ[AZURE_RM_SP_KEY_END_VARIABLE_NAME]

        service_endpoint_authorization.parameters['authenticationType'] = 'spnKey'
        service_endpoint_authorization.parameters['serviceprincipalkey'] = azure_rm_service_principal_key
    else:
        with open(azure_rm_service_principal_certificate_path, "r") as f:
            service_endpoint_authorization.parameters['authenticationType'] = 'spnCertificate'
            service_endpoint_authorization.parameters['servicePrincipalCertificate'] = f.read()

    service_endpoint_data = {
        'subscriptionId': azure_rm_subscription_id,
        'subscriptionName': azure_rm_subscription_name,
        'environment': 'AzureCloud',
        'creationMode': 'Manual'
    }
    service_endpoint_to_create = ServiceEndpoint(
        authorization=service_endpoint_authorization, data=service_endpoint_data,
        name=name, type=SERVICE_ENDPOINT_TYPE_AZURE_RM, url='https://management.azure.com/')
    return client.create_service_endpoint(service_endpoint_to_create, project)


def create_github_service_endpoint(name, github_url,
                                   organization=None, project=None, detect=None):
    """ Create a GitHub service endpoint.
    :param name: Name of service endpoint to create
    :type name: str
    :param github_url: Url for github for creating service endpoint
    :type github_url: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)
    if AZ_DEVOPS_GITHUB_PAT_ENVKEY not in os.environ:
        error_message = 'Please pass GitHub access token in ' + AZ_DEVOPS_GITHUB_PAT_ENVKEY +\
                        ' environment variable in non-interactive mode.'
        verify_is_a_tty_or_raise_error(error_message)
        github_access_token = prompt_pass('GitHub access token:', confirm=True)
    else:
        github_access_token = os.environ[AZ_DEVOPS_GITHUB_PAT_ENVKEY]

    service_endpoint_authorization = EndpointAuthorization(
        parameters={'accessToken': github_access_token},
        scheme=SERVICE_ENDPOINT_AUTHORIZATION_PERSONAL_ACCESS_TOKEN)
    service_endpoint_to_create = ServiceEndpoint(
        authorization=service_endpoint_authorization,
        name=name, type=SERVICE_ENDPOINT_TYPE_GITHUB, url=github_url)
    return client.create_service_endpoint(service_endpoint_to_create, project)



def create_service_endpoint(service_endpoint_configuration, organization=None,
                            project=None, detect=None):
    """ (PREVIEW) Create a service endpoint using configuration file.
    :param name: Name of service endpoint to create
    :type name: str
    :param service_endpoint_configuration: Configuration file with service endpoint request.
    :type authorization_scheme: str
    :rtype: :class:`ServiceEndpoint <service_endpoint.v4_1.models.ServiceEndpoint>`
    """
    organization, project = resolve_instance_and_project(detect=detect,
                                                         organization=organization,
                                                         project=project)
    client = get_service_endpoint_client(organization)
    with open(service_endpoint_configuration) as f:
        import json
        service_endpoint_to_create = json.load(f)
        return client.create_service_endpoint(service_endpoint_to_create, project)
