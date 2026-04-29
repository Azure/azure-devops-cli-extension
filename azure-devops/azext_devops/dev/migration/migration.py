# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import re
import subprocess
import time
import sys
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from msrest import Configuration
from msrest.service_client import ServiceClient
from msrest.universal_http import ClientRequest
from knack.util import CLIError

from knack.log import get_logger

from azext_devops.version import VERSION
from azext_devops.dev.common.services import get_connection, resolve_instance
from azext_devops.dev.common.uuid import is_uuid

logger = get_logger(__name__)


API_VERSION = '7.2-preview'
MIGRATIONS_API_PATH = '/_apis/elm/migrations'
DEVICE_FLOW_CONFIG_API_PATH = '/_apis/migrations/deviceFlowConfig'
LEGACY_DEVICE_FLOW_CONFIG_API_PATH = '/_apis/elm/migrations/deviceFlowConfig'
GITHUB_TOKEN_ENV_VAR = 'ELM_GITHUB_TOKEN'
_SKIP_VALIDATION_POLICIES = {
    'none': 0,
    'activepullrequestcount': 1,
    'pullrequestdeltasize': 2,
    'agentpoolexists': 4,
    'maxfilesize': 8,
    'maxpullrequestsize': 16,
    'maxpushpacksize': 32,
    'maxreferencenamelength': 64,
    'maxreposize': 128,
    'targetrepositorydoesnotexist': 256,
    'all': 2147483647,
}
_SUCCESS_TERMINAL_STATES = {
    'succeeded',
    'completed'
}
_NON_ACTIVE_STATES = {
    'completed',
    'succeeded',
    'failed',
    'suspended'
}
_ACTIVE_STAGES = {
    'queued',
    'validation',
    'synchronization',
    'cutover'
}
_URL_PATTERN = re.compile(r'^https?://[^\s]+$', re.IGNORECASE)


def list_migrations(include_inactive=False, project=None, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    client = _get_service_client(organization)
    url = _build_migration_url(organization)
    if include_inactive:
        url += '&includeInactiveMigrations=true'
    project = _normalize_optional_text(project)
    if project:
        url += '&project={}'.format(quote_plus(project))
    result = _send_request(client, 'GET', url)
    items = result.get('value', result) if isinstance(result, dict) else result
    if not items:
        hint = '' if include_inactive else ' Use --include-inactive to include completed or abandoned migrations.'
        logger.warning('No migrations found.%s', hint)
    return result


def _normalize_optional_text(value):
    if value is None:
        return None
    normalized = str(value).strip()
    return normalized if normalized else None


def _parse_skip_validation(skip_validation):
    if skip_validation is None:
        return None

    if isinstance(skip_validation, int):
        if skip_validation < 0:
            raise CLIError('--skip-validation must be a non-negative integer or a comma-separated list '
                           'of policy names.')
        return skip_validation

    normalized = _normalize_optional_text(skip_validation)
    if normalized is None:
        raise CLIError('--skip-validation cannot be empty. Provide a non-negative integer or a '
                       'comma-separated list of policy names.')

    if normalized.isdigit():
        return int(normalized)

    policies = [policy.strip() for policy in normalized.split(',')]
    if any(not policy for policy in policies):
        raise CLIError('--skip-validation contains an empty policy name. Provide a comma-separated '
                       'list such as "AgentPoolExists,MaxRepoSize".')

    mask = 0
    invalid_policies = []
    for policy in policies:
        key = _normalize_state(policy)
        if key not in _SKIP_VALIDATION_POLICIES:
            invalid_policies.append(policy)
            continue
        value = _SKIP_VALIDATION_POLICIES[key]
        if value == _SKIP_VALIDATION_POLICIES['all']:
            return value
        mask |= value

    if invalid_policies:
        raise CLIError('--skip-validation contains unsupported policy name(s): {}. Supported values: {}. '
                       'You can also pass a non-negative integer bitmask.'
                       .format(', '.join(invalid_policies),
                               ', '.join([
                                   'None',
                                   'ActivePullRequestCount',
                                   'PullRequestDeltaSize',
                                   'AgentPoolExists',
                                   'MaxFileSize',
                                   'MaxPullRequestSize',
                                   'MaxPushPackSize',
                                   'MaxReferenceNameLength',
                                   'MaxRepoSize',
                                   'TargetRepositoryDoesNotExist',
                                   'All'
                               ])))

    return mask


def get_migration(repository_id=None, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    return _send_request(client, 'GET', url)


def create_migration(repository_id=None, target_repository=None, target_owner_user_id=None,
                     validate_only=False, cutover_date=None, agent_pool=None,
                     skip_validation=None, service_endpoint_id=None, github_token=None,
                     organization=None, detect=None):
    target_repository = _normalize_optional_text(target_repository)
    target_owner_user_id = _normalize_optional_text(target_owner_user_id)
    agent_pool = _normalize_optional_text(agent_pool)
    service_endpoint_id = _normalize_optional_text(service_endpoint_id)
    github_token = _normalize_optional_text(github_token)
    skip_validation = _parse_skip_validation(skip_validation)

    if not target_repository:
        raise CLIError('--target-repository must be specified.')
    _validate_target_repository(target_repository)
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    github_token = _resolve_github_user_token(client, organization, target_repository, github_token)

    payload = {
        'targetRepository': target_repository,
        'gitHubUserToken': github_token,
        'validateOnly': bool(validate_only),
    }
    if target_owner_user_id:
        payload['targetOwnerUserId'] = target_owner_user_id
    if agent_pool:
        payload['agentPoolName'] = agent_pool
    if cutover_date is not None:
        payload['scheduledCutoverDate'] = cutover_date
    if skip_validation is not None:
        payload['skipValidation'] = skip_validation
    if service_endpoint_id:
        payload['serviceEndpointId'] = service_endpoint_id

    url = _build_migration_url(organization, repository_id)
    try:
        return _send_request(client, 'POST', url, payload)
    except CLIError as ex:
        error_text = str(ex)
        if 'status 409' in error_text and 'TF400898' in error_text:
            raise CLIError('An active migration already exists for repository {}. '
                           'Delete (abandon) the existing migration before creating a new one.'
                           .format(repository_id))
        raise


def _resolve_github_user_token(client, organization, target_repository, github_token=None):
    token = _normalize_optional_text(github_token)
    if token:
        return token

    env_token = _normalize_optional_text(os.getenv(GITHUB_TOKEN_ENV_VAR))
    if env_token:
        return env_token

    flow_config = _get_device_flow_config(client, organization, target_repository)
    client_id = _normalize_optional_text(flow_config.get('clientId'))
    enterprise_url = _normalize_optional_text(flow_config.get('enterpriseUrl'))
    if not client_id or not enterprise_url:
        raise CLIError('Device flow configuration response is missing clientId or enterpriseUrl.')

    return _run_device_flow(client_id, enterprise_url)


def _get_device_flow_config(client, organization, target_repository):
    urls = [
        _build_device_flow_config_url(organization, target_repository, DEVICE_FLOW_CONFIG_API_PATH),
        _build_device_flow_config_url(organization, target_repository, LEGACY_DEVICE_FLOW_CONFIG_API_PATH),
    ]

    first_error = None
    for index, url in enumerate(urls):
        try:
            return _send_request(client, 'GET', url)
        except CLIError as ex:
            if index == 0 and 'status 404' in str(ex):
                first_error = ex
                continue
            if index == 1 and first_error and 'status 404' in str(ex):
                raise CLIError('GitHub device-flow configuration is unavailable. '
                               'Provide --github-token or set ELM_GITHUB_TOKEN to continue.')
            raise

    if first_error:
        raise first_error
    raise CLIError('Unable to retrieve device flow configuration.')


def _build_device_flow_config_url(base_url, target_repository, api_path=DEVICE_FLOW_CONFIG_API_PATH):
    url = base_url.rstrip('/') + api_path
    return '{}?targetRepository={}&api-version={}'.format(url, quote_plus(target_repository), API_VERSION)


def _run_device_flow(client_id, enterprise_url):
    enterprise_url = enterprise_url.rstrip('/')
    device_code_response = _post_form('{}{}'.format(enterprise_url, '/login/device/code'), {
        'client_id': client_id,
    })

    device_code = _normalize_optional_text(device_code_response.get('device_code'))
    user_code = _normalize_optional_text(device_code_response.get('user_code'))
    verification_uri = _normalize_optional_text(device_code_response.get('verification_uri'))
    interval = _parse_positive_int(device_code_response.get('interval', 5), 'interval')
    expires_in = _parse_positive_int(device_code_response.get('expires_in', 900), 'expires_in')

    if not device_code or not user_code or not verification_uri:
        raise CLIError('Invalid device-flow response: missing required fields.')

    print('Open: {}'.format(verification_uri))
    print('Code: {}'.format(user_code))
    if _copy_to_clipboard(user_code):
        print('Code copied to clipboard.')
    print('Waiting for authorization...')

    deadline = time.monotonic() + expires_in
    token_url = '{}{}'.format(enterprise_url, '/login/oauth/access_token')
    grant_type = 'urn:ietf:params:oauth:grant-type:device_code'

    while time.monotonic() < deadline:
        time.sleep(interval)
        poll_response = _post_form(token_url, {
            'client_id': client_id,
            'device_code': device_code,
            'grant_type': grant_type,
        })

        token = _normalize_optional_text(poll_response.get('access_token'))
        if token:
            return token

        error = _normalize_optional_text(poll_response.get('error'))
        if error == 'authorization_pending':
            continue
        if error == 'slow_down':
            interval += 5
            continue
        if error == 'access_denied':
            raise CLIError('Authorization denied in GitHub device flow.')
        if error == 'expired_token':
            raise CLIError('Device code expired. Re-run the command to authorize again.')

        description = _normalize_optional_text(poll_response.get('error_description'))
        if description:
            raise CLIError('GitHub device flow failed: {}'.format(description))
        raise CLIError('GitHub device flow failed: {}'.format(error or 'unknown error'))

    raise CLIError('Timed out waiting for GitHub authorization. Re-run the command and complete login sooner.')


def _copy_to_clipboard(text):
    if not text:
        return False

    commands = []
    if os.name == 'nt':
        commands.append(['clip'])
    elif sys.platform == 'darwin':
        commands.append(['pbcopy'])
    else:
        commands.extend([
            ['xclip', '-selection', 'clipboard'],
            ['xsel', '--clipboard', '--input'],
        ])

    for command in commands:
        try:
            subprocess.run(command, input=text.encode('utf-8'), check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except (OSError, subprocess.SubprocessError):
            continue

    return False


def _post_form(url, data):
    body = '&'.join(['{}={}'.format(quote_plus(str(key)), quote_plus(str(value))) for key, value in data.items()])
    request = Request(url=url, data=body.encode('utf-8'))
    request.add_header('Accept', 'application/json')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')

    try:
        with urlopen(request) as response:
            content = response.read()
            return json.loads(content.decode('utf-8'))
    except HTTPError as ex:
        if ex.code in (401, 403):
            raise CLIError('GitHub device flow is unavailable for this organization. '
                           'This can happen if the GitHub app is not installed or the service is unavailable. '
                           'Try again later, or provide --github-token (or set ELM_GITHUB_TOKEN).')
        detail = ''
        try:
            content = ex.read()
            if content:
                parsed = json.loads(content.decode('utf-8'))
                detail = parsed.get('error_description') or parsed.get('error') or str(parsed)
        except Exception:  # pylint: disable=broad-except
            detail = ''
        raise CLIError('GitHub device flow request failed with status {}. {}'.format(ex.code, detail))
    except URLError as ex:
        raise CLIError('GitHub device flow request failed: {}'.format(ex.reason))


def _parse_positive_int(value, field_name):
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        raise CLIError('Invalid device-flow response: {} must be a positive integer.'.format(field_name))

    if parsed <= 0:
        raise CLIError('Invalid device-flow response: {} must be a positive integer.'.format(field_name))
    return parsed


def _validate_target_repository(target_repository):
    if not _URL_PATTERN.match(target_repository):
        raise CLIError('--target-repository must be a valid URL in the format https://host/org/repo.')

    parsed = urlparse(target_repository)
    if parsed.scheme != 'https':
        raise CLIError('--target-repository must be a valid URL in the format https://host/org/repo.')

    if not parsed.netloc or parsed.params or parsed.query or parsed.fragment:
        raise CLIError('--target-repository must be a valid URL in the format https://host/org/repo.')

    path_parts = [part for part in parsed.path.split('/') if part]
    if len(path_parts) != 2:
        raise CLIError('--target-repository must be a valid URL in the format https://host/org/repo.')


def pause_migration(repository_id=None, organization=None, detect=None):
    result = _update_migration(repository_id, organization, detect, status_requested='suspended')
    if not result:
        return {'message': 'Migration paused successfully.'}
    return result


def resume_migration(repository_id=None, validate_only=False, migration=False, organization=None, detect=None):
    if validate_only and migration:
        raise CLIError('Please specify only one of --validate-only or --migration.')

    organization = _resolve_org_for_auth(organization, detect)
    migration_data = get_migration(repository_id=repository_id, organization=organization, detect=None)

    if migration and _is_validate_only_succeeded(migration_data):
        return _promote_to_full_migration(migration_data, repository_id, organization)

    if _is_migration_active(migration_data):
        state_text = _get_migration_state_text(migration_data)
        raise CLIError('Migration is currently active ({}). Pause it first using '
                       '"az devops migrations pause --repository-id <guid>" before resuming or changing mode.'
                       .format(state_text))

    if _is_migration_terminal(migration_data):
        status = _get_effective_status(migration_data)
        is_val_only = migration_data.get('validateOnly') is True
        if _is_success_terminal_status(status) and is_val_only:
            raise CLIError('Validation already completed. Promote it with '
                           '"az devops migrations resume --repository-id {} --migration", '
                           'or abandon and create a new migration.'.format(repository_id))
        if _is_success_terminal_status(status):
            raise CLIError('Migration already completed. Use '
                           '"az devops migrations abandon --repository-id {}" to reset, '
                           'then create a new migration.'.format(repository_id))

    validate_only_value = None
    if validate_only:
        validate_only_value = True
    elif migration:
        validate_only_value = False

    return _update_migration(repository_id, organization, None,
                             validate_only=validate_only_value, status_requested='active')


def schedule_cutover(repository_id=None, cutover_date=None, organization=None, detect=None):
    if not cutover_date:
        raise CLIError('--date must be specified.')
    return _update_migration(repository_id, organization, detect, scheduled_cutover_date=cutover_date,
                             include_cutover=True)


def cancel_cutover(repository_id=None, organization=None, detect=None):
    result = _update_migration(repository_id, organization, detect, scheduled_cutover_date=None,
                               include_cutover=True)
    if not result:
        return {'message': 'Cutover cancelled successfully.'}
    return result


def delete_migration(repository_id=None, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    _send_request(client, 'DELETE', url)
    return {'message': 'Migration abandoned successfully.'}


def _update_migration(repository_id, organization, detect, validate_only=None,
                      status_requested=None, scheduled_cutover_date=None, include_cutover=False):
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)

    payload = {}
    if validate_only is not None:
        payload['validateOnly'] = bool(validate_only)
    if status_requested is not None:
        payload['statusRequested'] = status_requested
    if include_cutover:
        payload['scheduledCutoverDate'] = scheduled_cutover_date
    return _send_request(client, 'PUT', url, payload)


def _resolve_repository_id(repository_id):
    if not repository_id:
        raise CLIError('--repository-id must be specified.')
    if not is_uuid(repository_id):
        raise CLIError('--repository-id must be a valid GUID.')
    return repository_id


def _normalize_state(value):
    if value is None:
        return ''
    normalized = str(value).strip().lower()
    return normalized.replace(' ', '').replace('-', '').replace('_', '')


def _is_success_terminal_status(status):
    return status in _SUCCESS_TERMINAL_STATES


def _get_effective_status(migration):
    if not isinstance(migration, dict):
        return ''
    # Prefer actual migration status over requested status when both are present.
    status = _normalize_state(migration.get('status'))
    if status:
        return status
    return _normalize_state(migration.get('statusRequested'))


def _get_migration_state_text(migration):
    status_requested = migration.get('statusRequested')
    status = migration.get('status')
    stage = migration.get('stage')

    parts = []
    if status_requested:
        parts.append('statusRequested: {}'.format(status_requested))
    if status:
        parts.append('status: {}'.format(status))
    if stage:
        parts.append('stage: {}'.format(stage))

    return ', '.join(parts) if parts else 'state unknown'


def _is_migration_active(migration):
    if not isinstance(migration, dict):
        return False

    status = _get_effective_status(migration)
    if status:
        return status not in _NON_ACTIVE_STATES

    stage = _normalize_state(migration.get('stage'))
    if stage:
        return stage in _ACTIVE_STAGES

    return False


def _is_migration_terminal(migration):
    if not isinstance(migration, dict):
        return False
    status = _get_effective_status(migration)
    return _is_success_terminal_status(status) or status == 'failed'


def _is_validate_only_succeeded(migration):
    if not isinstance(migration, dict):
        return False
    return (migration.get('validateOnly') is True and
            _is_success_terminal_status(_get_effective_status(migration)))


def _promote_to_full_migration(migration_data, repository_id, organization):
    del migration_data
    return _update_migration(repository_id, organization, detect=None,
                             validate_only=False, status_requested='active')


def _resolve_org_for_auth(organization, detect):
    return resolve_instance(detect=detect, organization=organization)


def _build_migration_url(base_url, repository_id=None):
    url = base_url.rstrip('/') + MIGRATIONS_API_PATH
    if repository_id:
        url += '/{}'.format(repository_id)
    return url + '?api-version=' + API_VERSION


def _get_service_client(organization):
    config = Configuration(base_url=None)
    config.add_user_agent('devOpsCli/{}'.format(VERSION))
    config.retry_policy.policy.status_forcelist = []
    connection = get_connection(organization)
    return ServiceClient(creds=connection._creds, config=config)  # pylint: disable=protected-access


def _send_request(client, method, url, content=None):
    request = ClientRequest(method=method, url=url)
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json;api-version=' + API_VERSION
    }
    response = client.send(request=request, headers=headers, content=content)
    if response.status_code < 200 or response.status_code >= 300:
        error_detail = ''
        try:
            body = response.json()
            precheck_detail = _extract_precheck_issue_detail(body)
            if precheck_detail:
                error_detail = precheck_detail
            else:
                error_detail = body.get('message') or body.get('Message') or str(body)
        except Exception:  # pylint: disable=broad-except
            error_detail = getattr(response, 'text', None) or getattr(response, 'content', None) or ''
        raise CLIError('Request failed with status {}. {}'.format(response.status_code, error_detail))

    content_type = response.headers.get('Content-Type') if response.headers else None
    if content_type and 'json' in content_type:
        return response.json()
    return {}


def _extract_precheck_issue_detail(body):
    if not isinstance(body, dict):
        return None

    issue_collections = []
    for key in ('preCheckIssues', 'PreCheckIssues', 'validationIssues', 'ValidationIssues', 'issues', 'Issues'):
        value = body.get(key)
        if isinstance(value, list):
            issue_collections.extend(value)

    messages = []
    for issue in issue_collections:
        if not isinstance(issue, dict):
            continue
        issue_type = (issue.get('preCheckIssueType') or issue.get('PreCheckIssueType') or
                      issue.get('issueType') or issue.get('IssueType'))
        issue_message = (issue.get('message') or issue.get('Message') or
                         issue.get('errorMessage') or issue.get('ErrorMessage'))

        issue_type = _normalize_optional_text(issue_type)
        issue_message = _normalize_optional_text(issue_message)

        if issue_type and issue_message:
            messages.append('[{}] {}'.format(issue_type, issue_message))
        elif issue_type:
            messages.append('[{}]'.format(issue_type))
        elif issue_message:
            messages.append(issue_message)

    if messages:
        return 'Pre-check issues: {}'.format('; '.join(messages))

    return None
