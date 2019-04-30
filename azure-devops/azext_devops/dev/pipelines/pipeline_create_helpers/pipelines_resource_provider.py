# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.dev.common.prompting import prompt_user_friendly_choice_list, prompt_not_empty
from azext_devops.dev.common.services import (
    get_service_endpoint_client, get_new_cix_client, get_default_subscription_info)
from azext_devops.dev.pipelines.pipeline_create_helpers.github_api_helper import get_github_pat_token
from azext_devops.devops_sdk.v5_1.service_endpoint.models import ServiceEndpoint, EndpointAuthorization

logger = get_logger(__name__)


def get_github_service_endpoint(organization, project):
    """
    This will try to create a GitHub service connection if there is no existing one in the project
    GitHub pat token will be asked for interactively or can be provided
    by setting the Environment variable AZ_DEVOPS_GITHUB_PAT_ENVKEY.
    Service endpoint connection name is asked as input from the user, if the environment is non interative
    name is set to default  AzureDevopsCliCreatePipelineFlow
    """
    se_client = get_service_endpoint_client(organization)
    existing_service_endpoints = _get_service_endpoints(organization, project, 'github')
    service_endpoints_choice_list = ['Create new GitHub service connection']
    github_service_endpoints = []
    choice = 0
    for endpoint in existing_service_endpoints:
        if endpoint.authorization.scheme == 'InstallationToken':
            service_endpoints_choice_list.append('{} {}'.format(endpoint.name, '(Recommended)'))
        else:
            service_endpoints_choice_list.append('{}'.format(endpoint.name))
        github_service_endpoints.append(endpoint)
    if github_service_endpoints:
        choice = prompt_user_friendly_choice_list(
            "Which service connection do you want to use to communicate with GitHub?",
            service_endpoints_choice_list)
    if choice == 0:
        logger.debug("Creating a new service endpoint.")
        github_pat = get_github_pat_token()
        se_name = prompt_not_empty('Enter a service endpoint name to create? ')
        print('')
        service_endpoint_authorization = EndpointAuthorization(parameters={'accessToken': github_pat},
                                                               scheme='PersonalAccessToken')
        service_endpoint_to_create = ServiceEndpoint(authorization=service_endpoint_authorization,
                                                     name=se_name, type='github',
                                                     url='https://github.com/')
        return se_client.create_service_endpoint(service_endpoint_to_create, project).id
    return existing_service_endpoints[choice - 1].id


def _get_service_endpoints(organization, project, endpoint_type=None):
    """
    Get the list of existing service connections filtered by type if mentioned
    """
    client = get_service_endpoint_client(organization)
    all_connections = client.get_service_endpoints(project)
    if endpoint_type is None:
        return all_connections
    filtered_connection = []
    for connection in all_connections:
        if connection.type.lower() == endpoint_type.lower():
            filtered_connection.append(connection)
    return filtered_connection


def get_azure_rm_service_connection_id(organization, project):
    azure_rm_connection = get_azure_rm_service_connection(organization, project)
    return azure_rm_connection['Id']


def get_azure_rm_service_connection(organization, project):
    logger.debug('Create a new Azure Resource Manager service connection')
    subscription_id, subscription_name, tenant_id, environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for creating Azure RM connection.", subscription_name)
    cix_client = get_new_cix_client(organization=organization)
    azure_rm_connection_create_obj = get_azure_rm_connection_create_object(
        subscription_id, subscription_name, environment_name, tenant_id)
    azure_rm_connection = cix_client.create_resources(creation_parameters=azure_rm_connection_create_obj,
                                                      project=project)
    azure_rm_connection_obj = azure_rm_connection.resources['azureRmConnection']
    poll_connection_ready(organization, project, azure_rm_connection_obj['Id'])
    return azure_rm_connection_obj


def get_kubernetes_environment_resource(organization, project, repo_name):
    logger.debug("Creating a new k8s environment resource.")
    import subprocess
    import json
    subscription_id, subscription_name, tenant_id, environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for fetching AKS clusters.", subscription_name)
    aks_list = subprocess.check_output('az aks list -o json', shell=True)
    aks_list = json.loads(aks_list)
    if aks_list:
        cluster_choice = 0
        cluster_choice_list = []
        for aks_clusters in aks_list:
            cluster_choice_list.append(aks_clusters['name'])
        cluster_choice = prompt_user_friendly_choice_list(
            "Which kubernetes cluster do you want to target for this pipeline?", cluster_choice_list)
        selected_cluster = aks_list[cluster_choice]
        create_namespace, namespace = get_kubernetes_namespace(organization, project, selected_cluster,
                                                               subscription_id, subscription_name, tenant_id,
                                                               environment_name)
        kubernetes_connection_obj = get_kubernetes_connection_create_object(
            subscription_id, subscription_name, selected_cluster['id'], selected_cluster['name'],
            selected_cluster['fqdn'], tenant_id, namespace, create_namespace, environment_name)
        cix_client = get_new_cix_client(organization=organization)
        kubernetes_connection = cix_client.create_resources(creation_parameters=kubernetes_connection_obj,
                                                            project=project)
        k8s_connection_obj = kubernetes_connection.resources['k8sConnection']
        poll_connection_ready(organization, project, k8s_connection_obj['Id'])
        kubernetes_env_obj = get_kubernetes_resource_create_object(
            k8s_connection_obj['Name'],
            selected_cluster['name'],
            repo_name,
            k8s_connection_obj['Id'],
            namespace)
        kubernetes_environment_resource = cix_client.create_resources(creation_parameters=kubernetes_env_obj,
                                                                      project=project)
        return kubernetes_environment_resource.resources['k8sResource']
    raise CLIError('There are no AKS clusters under your subscription. '
                   'Create the clusters or switch to another subscription, verify with '
                   'command \'az aks list\' and try again.')


def get_kubernetes_namespace(organization, project, cluster, subscription_id, subscription_name,
                             tenant_id, azure_env):
    choice_list = []
    existing_namespace_list = []
    choice_list.append("Create new")
    se_request_obj = get_se_kubernetes_namespace_request_obj(subscription_id, subscription_name, cluster['id'],
                                                             cluster['name'], cluster['fqdn'], azure_env, tenant_id)
    se_client = get_service_endpoint_client(organization=organization)
    se_result = se_client.execute_service_endpoint_request(service_endpoint_request=se_request_obj, project=project,
                                                           endpoint_id=cluster['name'])
    if se_result.result:
        import json
        for namespace in se_result.result:
            ns_json_obj = json.loads(namespace)
            existing_namespace_list.append(ns_json_obj['Value'])
            choice_list.append(ns_json_obj['Value'])
    choice = prompt_user_friendly_choice_list("Which kubernetes namespace do you want to target?",
                                              choice_list)
    if choice == 0:
        create_namespace = True
        namespace = prompt_not_empty("Enter a name for new namespace to create: ")
        print('')
    else:
        create_namespace = False
        namespace = existing_namespace_list[choice - 1]
    return create_namespace, namespace


def poll_connection_ready(organization, project, connection_id):
    import colorama
    import humanfriendly
    import time
    colorama.init()
    with humanfriendly.Spinner(label="Checking resource readiness") as spinner:
        se_client = get_service_endpoint_client(organization)
        while True:
            spinner.step()
            time.sleep(0.5)
            service_endpoint = se_client.get_service_endpoint_details(project, connection_id)
            if service_endpoint.is_ready:
                break


def get_se_kubernetes_namespace_request_obj(subscription_id, subscription_name, cluster_id, cluster_name, fqdn,
                                            azure_env, tenant_id):
    return {
        "dataSourceDetails": {
            "dataSourceName": "KubernetesNamespaces",
            "headers": [
            ],
            "resourceUrl": "",
            "parameters": {
                "clusterName": cluster_name
            }
        },
        "resultTransformationDetails": {
            "resultTemplate": "{ \"Value\" : \"{{metadata.name}}\", \"DisplayValue\" : \"{{metadata.name}}\" }"
        },
        "serviceEndpointDetails": {
            "authorization": {
                "parameters": {
                    "azureEnvironment": azure_env,
                    "azureTenantId": tenant_id
                },
                "scheme": "Kubernetes"
            },
            "data": {
                "authorizationType": "AzureSubscription",
                "azureSubscriptionId": subscription_id,
                "azureSubscriptionName": subscription_name,
                "clusterId": cluster_id
            },
            "type": "Kubernetes",
            "url": "https://" + fqdn
        }
    }


def get_container_registry_service_connection(organization, project):
    import subprocess
    import json
    subscription_id, subscription_name, tenant_id, _environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for fetching Azure Container Registries.",
                   subscription_name)
    acr_list = subprocess.check_output('az acr list -o json', shell=True)
    acr_list = json.loads(acr_list)
    if acr_list:
        registry_choice = 0
        registry_choice_list = []
        for acr_clusters in acr_list:
            registry_choice_list.append(acr_clusters['name'])
        registry_choice = prompt_user_friendly_choice_list(
            "Which Azure Container Registry do you want to use for this pipeline?", registry_choice_list)
        selected_registry = acr_list[registry_choice]
        cix_client = get_new_cix_client(organization=organization)
        acr_connection_obj = get_container_registry_connection_create_object(
            subscription_id,
            subscription_name,
            tenant_id,
            selected_registry['id'],
            selected_registry['name'],
            selected_registry['loginServer'])
        acr_container_resource = cix_client.create_resources(creation_parameters=acr_connection_obj, project=project)
        poll_connection_ready(organization, project,
                              acr_container_resource.resources['containerRegistryConnection']['Id'])
        return acr_container_resource.resources['containerRegistryConnection']
    raise CLIError('There is no Azure container registry associated with your subscription. '
                   'Create an ACR or switch to another subscription, '
                   'verify with command \'az acr list\' and try again.')


def get_webapp_from_list_selection():
    logger.debug("Fetching web app list to display")
    import subprocess
    import json
    _subscription_id, subscription_name, _tenant_id, _environment_name = get_default_subscription_info()
    logger.warning("Using your default Azure subscription %s for fetching Web App list.", subscription_name)
    webapp_list = subprocess.check_output('az webapp list -o json', shell=True)
    webapp_list = json.loads(webapp_list)
    if webapp_list:
        app_choice = 0
        app_choice_list = []
        for webapp in webapp_list:
            app_choice_list.append(webapp['name'])
        app_choice = prompt_user_friendly_choice_list(
            "Which Web App do you want to target?", app_choice_list)
        return webapp_list[app_choice]['name']
    raise CLIError('There are no Web apps in this subscription. Either create a Web App using this subscription '
                   'or change to another subscription. Verify with command \'az webapp list\'.')


def get_kubernetes_resource_create_object(resource_name, cluster_name, repo_name,
                                          kubernetes_service_connection_id, namespace):
    return {
        "k8sResource": {
            "resourcetocreate": {
                "name": resource_name,
                "namespace": namespace,
                "clusterName": cluster_name,
                "serviceEndpointId": kubernetes_service_connection_id
            },
            "type": "environmentResource:kubernetes"
        },
        "environment": {
            "resourcetocreate": {
                "name": repo_name,
                "description": "CI/CD setup from this repo: '{reponame}'".format(reponame=repo_name)
            },
            "type": "environment"
        }
    }


def get_kubernetes_connection_create_object(subscription_id, subscription_name, cluster_id, cluster_name, fqdn,
                                            tenant_id, namespace, create_namespace, azure_env):
    return {
        "k8sConnection": {
            "resourcetocreate": {
                "data": {
                    "authorizationType": "AzureSubscription",
                    "azureSubscriptionId": subscription_id,
                    "azureSubscriptionName": subscription_name,
                    "clusterId": cluster_id,
                    "namespace": namespace,
                    "operation.createNamespace": create_namespace
                },
                "name": cluster_name + "-" + namespace,
                "type": "kubernetes",
                "url": "https://" + fqdn,
                "authorization": {
                    "scheme": "Kubernetes",
                    "parameters": {
                        "azureEnvironment": azure_env,
                        "azureTenantId": tenant_id
                    }
                }
            },
            "type": "endpoint:kubernetes"
        }
    }


def get_container_registry_connection_create_object(subscription_id, subscription_name, tenant_id, registry_id,
                                                    registry_name, login_server):
    return {
        "containerRegistryConnection": {
            "resourcetocreate": {
                "data": {
                    "registrytype": "ACR",
                    "registryId": registry_id,
                    "subscriptionId": subscription_id,
                    "subscriptionName": subscription_name
                },
                "name": registry_name,
                "type": "dockerregistry",
                "url": "https://" + login_server,
                "authorization": {
                    "scheme": "serviceprincipal",
                    "parameters": {
                        "tenantId": tenant_id,
                        "servicePrincipalId": "<placeholder>",
                        "scope": registry_id,
                        "loginServer": login_server
                    }
                }
            },
            "type": "endpoint:containerRegistry"
        }
    }


def get_azure_rm_connection_create_object(subscription_id, subscription_name, azure_env, tenant_id):
    return {
        "azureRmConnection": {
            "resourcetocreate": {
                "data": {
                    "subscriptionId": subscription_id,
                    "subscriptionName": subscription_name,
                    "environment": azure_env,
                    "scopeLevel": "Subscription",
                    "creationMode": "Automatic",
                    "azureSpnRoleAssignmentId": "",
                    "azureSpnPermissions": "",
                    "spnObjectId": "",
                    "appObjectId": ""
                },
                "name": "{sub_name} ({sub_id})".format(sub_name=subscription_name, sub_id=subscription_id),
                "type": "azurerm",
                "url": "https://management.azure.com/",
                "authorization": {
                    "scheme": "ServicePrincipal",
                    "parameters": {
                        "tenantid": tenant_id,
                        "serviceprincipalid": "",
                        "authenticationType": "spnKey",
                        "serviceprincipalkey": ""
                    }
                }
            },
            "type": "endpoint:azureRm"
        }
    }
