# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest import Configuration
from msrest.service_client import ServiceClient
from msrest.universal_http import ClientRequest
from knack.util import CLIError

from azext_devops.version import VERSION
from azext_devops.dev.common.services import get_connection, resolve_instance
from azext_devops.dev.common.uuid import is_uuid


API_VERSION = '7.2-preview'
MIGRATIONS_API_PATH = '/_apis/elm/migrations'
_NON_ACTIVE_STATES = {
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
def list_migrations(include_inactive=False, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    client = _get_service_client(organization)
    url = _build_migration_url(organization)
    if include_inactive:
        url += '&includeInactiveMigrations=true'
    return _send_request(client, 'GET', url)


def _normalize_optional_text(value):
    if value is None:
        return None
    normalized = str(value).strip()
    return normalized if normalized else None


def get_migration(repository_id=None, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    return _send_request(client, 'GET', url)


def create_migration(repository_id=None, target_repository=None, target_owner_user_id=None,
                     validate_only=False, cutover_date=None, agent_pool=None,
                     skip_validation=None, organization=None, detect=None):
    agent_pool = _normalize_optional_text(agent_pool)
    skip_validation = _normalize_optional_text(skip_validation)
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

    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    return _send_request(client, 'POST', url, payload)


def pause_migration(repository_id=None, organization=None, detect=None):
    return _update_migration(repository_id, organization, detect, status_requested='suspended')


def resume_migration(repository_id=None, validate_only=False, migration=False, organization=None, detect=None):
    if validate_only and migration:
        raise CLIError('Please specify only one of --validate-only or --migration.')

    migration_data = get_migration(repository_id=repository_id, organization=organization, detect=detect)
    if _is_migration_active(migration_data):
        status = migration_data.get('statusRequested') or migration_data.get('status')
        stage = migration_data.get('stage')
        raise CLIError('Migration is active (statusRequested: {}, stage: {}). Pause it before resuming or changing mode.'
                       .format(status, stage))

    validate_only_value = None
    if validate_only:
        validate_only_value = True
    elif migration:
        validate_only_value = False

    return _update_migration(repository_id, organization, detect,
                             validate_only=validate_only_value, status_requested='active')


def schedule_cutover(repository_id=None, cutover_date=None, organization=None, detect=None):
    if not cutover_date:
        raise CLIError('--date must be specified.')
    return _update_migration(repository_id, organization, detect, scheduled_cutover_date=cutover_date,
                             include_cutover=True)


def cancel_cutover(repository_id=None, organization=None, detect=None):
    return _update_migration(repository_id, organization, detect, scheduled_cutover_date=None,
                             include_cutover=True)


def delete_migration(repository_id=None, organization=None, detect=None):
    organization = _resolve_org_for_auth(organization, detect)
    repository_id = _resolve_repository_id(repository_id)
    client = _get_service_client(organization)
    url = _build_migration_url(organization, repository_id)
    return _send_request(client, 'DELETE', url)


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


def _is_migration_active(migration):
    if not isinstance(migration, dict):
        return False

    status = _normalize_state(migration.get('statusRequested') or migration.get('status'))
    if status:
        return status not in _NON_ACTIVE_STATES

    stage = _normalize_state(migration.get('stage'))
    if stage:
        return stage in _ACTIVE_STAGES

    return False


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
        error_detail = getattr(response, 'text', None) or getattr(response, 'content', None) or ''
        raise CLIError('Request failed with status {}. {}'.format(response.status_code, error_detail))

    content_type = response.headers.get('Content-Type') if response.headers else None
    if content_type and 'json' in content_type:
        return response.json()
    return {}
