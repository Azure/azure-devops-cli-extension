# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import datetime
import os
from collections import OrderedDict

from knack.log import get_logger
from knack.util import CLIError
from msrest.authentication import BasicAuthentication
from azure.cli.core._profile import Profile
from vsts.vss_connection import VssConnection
from azext_devops.version import VERSION
from .arguments import should_detect
from .const import (DEFAULTS_SECTION,
                    DEVOPS_ORGANIZATION_DEFAULT,
                    DEVOPS_TEAM_PROJECT_DEFAULT,
                    PAT_ENV_VARIABLE_NAME)
from ._credentials import get_credential
from .git import get_remote_url
from .vsts_git_url_info import VstsGitUrlInfo
from .uri import uri_parse_instance_from_git_uri

logger = get_logger(__name__)


def get_vss_connection(devops_organization):
    devops_organization = devops_organization.lower()
    if devops_organization not in _vss_connection:
        credentials = _get_credentials(devops_organization)
        try:
            from .telemetry import try_send_telemetry_data
            _vss_connection[devops_organization] = _get_vss_connection(devops_organization, credentials)
            try_send_telemetry_data(devops_organization)
        except Exception as ex:
            logger.debug(ex, exc_info=True)
            raise CLIError(ex)
    return _vss_connection[devops_organization]


def _get_credentials(devops_organization):
    pat_token_present = False
    if PAT_ENV_VARIABLE_NAME in os.environ or get_credential(devops_organization) is not None:
        logger.debug("PAT is present which can be used against this instance")
        pat_token_present = True

    try:
        token_from_az_login = get_token_from_az_logins(devops_organization, pat_token_present)
        if token_from_az_login:
            credentials = BasicAuthentication('', token_from_az_login)
            return credentials
    except BaseException as ex:
        logger.debug("az login is not present")
        logger.debug(ex, exc_info=True)

    if PAT_ENV_VARIABLE_NAME in os.environ:
        pat = os.environ[PAT_ENV_VARIABLE_NAME]
        logger.info("received PAT from environment variable")
    else:
        pat = get_credential(devops_organization)
    if pat is not None:
        logger.info("Creating connection with personal access token.")
        credentials = BasicAuthentication('', pat)
        # credentials can be incorrect but they are present then it means user has already done az devops login to set
        # so let the user get a 401
        return credentials

    raise get_authentication_error('Before you can run Azure DevOps commands, you need to run the login command'
                                   '(az login if using AAD/MSA identity else az devops login if using PAT token) to '
                                   'setup credentials.')


def validate_token_for_instance(devops_organization, credentials):
    logger.debug("instance recieved in validate_token_for_instance %s", devops_organization)
    devops_organization = uri_parse_instance_from_git_uri(devops_organization)
    logger.debug("instance processed in validate_token_for_instance %s", devops_organization)
    connection = _get_vss_connection(devops_organization, credentials)
    core_client = connection.get_client('vsts.core.v4_0.core_client.CoreClient')
    try:
        core_client.get_projects(state_filter='all', top=1, skip=0)
        return True
    except BaseException as ex2:
        logger.debug(ex2, exc_info=True)
        logger.debug("Failed to connect using provided credentials")
    return False


def get_token_from_az_logins(devops_organization, pat_token_present):
    profile = Profile()
    dummy_user = profile.get_current_account_user()     # noqa: F841
    subscriptions = profile.load_cached_subscriptions(False)
    tenantsDict = OrderedDict()

    # first loop to make sure the first identity we try with is coming from selected subscription
    for subscription in subscriptions:
        if subscription['isDefault'] == "true":
            tenantsDict[(subscription['tenantId'], subscription['user']['name'])] = ''

    for subscription in subscriptions:
        tenantsDict[(subscription['tenantId'], subscription['user']['name'])] = ''

    skipValidateToken = False
    if pat_token_present is False and len(tenantsDict) == 1:
        skipValidateToken = True

    try:
        for key, dummy_value in tenantsDict.items():
            try:
                logger.debug('trying to get token (temp) for tenant %s and user %s ', key[0], key[1])
                token = get_token_from_az_login(profile, key[1], key[0])
                credentials = BasicAuthentication('', token)

                if skipValidateToken is True:
                    return token
                if validate_token_for_instance(devops_organization, credentials):
                    return token
                logger.debug('invalid token obtained for tenant %s', key[0])
            except BaseException as ex2:
                logger.debug(ex2)
                logger.debug('failed while trying to get token for tenant %s', key[0])
    except BaseException as ex:
        logger.debug(ex)

    return ''


def get_token_from_az_login(profile, user, tenant):
    try:
        auth_token = profile.get_access_token_for_resource(user, tenant, '499b84ac-1321-427f-aa17-267ca6975798')
        return auth_token
    except BaseException as ex:
        logger.debug('not able to get token from az login')
        logger.debug(ex, exc_info=True)
        return ""


def _get_vss_connection(devops_organization, credentials):
    return VssConnection(get_base_url(devops_organization), creds=credentials,
                         user_agent='devOpsCli/{}'.format(VERSION))


def get_first_vss_instance_uri():
    for key in _vss_connection:
        return key


def get_release_client(team_instance=None):
    connection = get_vss_connection(team_instance)
    return connection.get_client('vsts.release.v4_0.release_client.ReleaseClient')


def get_build_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.build.v4_0.build_client.BuildClient')


def get_ci_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client(
        'vsts.customer_intelligence.v4_0.customer_intelligence_client.CustomerIntelligenceClient')


def get_core_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.core.v4_0.core_client.CoreClient')


def get_git_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.git.v4_0.git_client.GitClient')


def get_identity_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.identity.v4_0.identity_client.IdentityClient')


def get_service_endpoint_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient')


def get_location_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.location.v4_0.location_client.LocationClient')


def get_member_entitlement_management_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.member_entitlement_management.v4_1.member_entitlement_management_client.'
                                 'MemberEntitlementManagementClient')


def get_operations_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.operations.v4_0.operations_client.OperationsClient')


def get_policy_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.policy.v4_0.policy_client.PolicyClient')


def get_settings_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.settings.v4_0.settings_client.SettingsClient')


def get_task_agent_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.task_agent.v4_0.task_agent_client.TaskAgentClient')


def get_work_item_tracking_client(devops_organization=None):
    connection = get_vss_connection(devops_organization)
    return connection.get_client('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient')


def get_base_url(devops_organization):
    if devops_organization is not None:
        return devops_organization
    raise _team_devops_organization_arg_error()


def _team_devops_organization_arg_error():
    return CLIError('--organization must be specified. The value should be the URI of your Azure DevOps '
                    'organization, for example: https://dev.azure.com/MyOrganization/ or your TFS organization. '
                    'You can set a default value by running: az devops configure --defaults '
                    'organization=https://dev.azure.com/MyOrganization/. For auto detection to work '
                    '(--detect on), you must be in a local Git directory that has a "remote" referencing a '
                    'Azure DevOps or TFS repository.')


def _raise_team_project_arg_error():
    raise CLIError('--project must be specified. The value should be the ID or name of a team project. '
                   'You can set a default value by running: az devops configure --defaults project=<ProjectName>.')


def resolve_instance_project_and_repo(detect, devops_organization, project=None, project_required=True, repo=None):
    if devops_organization is None:
        if should_detect(detect):
            git_info = get_vsts_info_from_current_remote_url()
            devops_organization = git_info.uri
            if project is None:
                project = git_info.project
                if repo is None:
                    repo = git_info.repo
        if devops_organization is None:
            devops_organization = _resolve_instance_from_config(devops_organization)
        if project is None:
            project = _resolve_project_from_config(project, project_required)
    if project_required and project is None:
        _raise_team_project_arg_error()
    return devops_organization, project, repo


def resolve_instance_and_project(detect, devops_organization, project=None, project_required=True):
    devops_organization, project, _ = resolve_instance_project_and_repo(
        detect=detect, devops_organization=devops_organization, project=project, project_required=project_required)
    return devops_organization, project


def resolve_instance(detect, devops_organization):
    devops_organization, _ = resolve_instance_and_project(
        detect=detect, devops_organization=devops_organization, project_required=False)
    return devops_organization


def _resolve_instance_from_config(devops_organization):
    from .config import azdevops_config
    if devops_organization is None:
        if azdevops_config.has_option(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT):
            devops_organization = azdevops_config.get(DEFAULTS_SECTION, DEVOPS_ORGANIZATION_DEFAULT)
        if devops_organization is None or devops_organization == '':
            raise _team_devops_organization_arg_error()
    return devops_organization


def _resolve_project_from_config(project, project_required=True):
    from .config import azdevops_config
    if project is None:
        if azdevops_config.has_option(DEFAULTS_SECTION, DEVOPS_TEAM_PROJECT_DEFAULT):
            project = azdevops_config.get(DEFAULTS_SECTION, DEVOPS_TEAM_PROJECT_DEFAULT)
        if project_required and (project is None or project == ''):
            _raise_team_project_arg_error()
    return project


def get_vsts_info_from_current_remote_url():
    start = datetime.datetime.now()
    info = VstsGitUrlInfo(get_remote_url(VstsGitUrlInfo.is_vsts_url_candidate))
    end = datetime.datetime.now()
    duration = end - start
    logger.info("Detect: Url discovery took %s", str(duration))
    return info


def get_connection_data(devops_organization):
    devops_organization = devops_organization.lower()
    if devops_organization in _connection_data:
        return _connection_data[devops_organization]
    location_client = get_location_client(devops_organization)
    _connection_data[devops_organization] = location_client.get_connection_data()
    return _connection_data[devops_organization]


def get_authentication_error(message):
    return CLIError(str(message) + "  Please see https://aka.ms/azure-devops-cli-auth for more information.")


def clear_connection_cache():
    _vss_connection.clear()


_connection_data = {}
_vss_connection = OrderedDict()
