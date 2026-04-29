# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re
from urllib.parse import quote_plus

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
                     skip_validation=None, service_endpoint_id=None, organization=None, detect=None):
    target_repository = _normalize_optional_text(target_repository)
    target_owner_user_id = _normalize_optional_text(target_owner_user_id)
    agent_pool = _normalize_optional_text(agent_pool)
    service_endpoint_id = _normalize_optional_text(service_endpoint_id)
    skip_validation = _parse_skip_validation(skip_validation)

    if not target_repository:
        raise CLIError('--target-repository must be specified.')
    if not _URL_PATTERN.match(target_repository):
        raise CLIError('--target-repository must be a valid URL starting with http:// or https://.')
    if not target_owner_user_id:
        raise CLIError('--target-owner-user-id must be specified.')

    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)

    payload = {
        'targetRepository': target_repository,
        'targetOwnerUserId': target_owner_user_id,
        'validateOnly': bool(validate_only),
    }
    if agent_pool:
        payload['agentPoolName'] = agent_pool
    if cutover_date is not None:
        payload['scheduledCutoverDate'] = cutover_date
    if skip_validation is not None:
        payload['skipValidation'] = skip_validation
    if service_endpoint_id:
        payload['serviceEndpointId'] = service_endpoint_id

    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    return _send_request(client, 'POST', url, payload)


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
            error_detail = body.get('message') or body.get('Message') or str(body)
        except Exception:  # pylint: disable=broad-except
            error_detail = getattr(response, 'text', None) or getattr(response, 'content', None) or ''
        raise CLIError('Request failed with status {}. {}'.format(response.status_code, error_detail))

    content_type = response.headers.get('Content-Type') if response.headers else None
    if content_type and 'json' in content_type:
        return response.json()
    return {}
