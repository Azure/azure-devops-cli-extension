# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from .uri import uri_parse
from .credential_store import CredentialStore

logger = get_logger(__name__)


def get_credential(organization, fall_back_to_default=True):
    token = _get_credential(organization)
    if token is None and organization is not None and fall_back_to_default:
        token = _get_credential(organization=None)
    return token


def _get_credential(organization):
    key = _get_service_name(organization)
    logger.debug('Getting credential: %s', key)
    cred_store = CredentialStore()
    return cred_store.get_password(key)


def set_credential(organization, token):
    key = _get_service_name(organization)
    cred_store = CredentialStore()
    cred_store.set_password(key, token)


def clear_credential(organization):
    key = _get_service_name(organization)
    logger.debug('Clearing credential: %s', key)
    cred_store = CredentialStore()
    cred_store.clear_password(key)


def _get_service_name(organization):
    if organization is not None:
        return 'azdevops-cli:' + normalize_url_for_key(organization)
    return 'azdevops-cli: default'


def normalize_url_for_key(url):
    components = uri_parse(url)
    normalized_url = components.scheme.lower() + '://' + components.netloc.lower()
    organization_name = components.path.lower()
    if(organization_name and ('visualstudio.com' not in url.lower())):
        organization_name = organization_name.split('/')[1]
        normalized_url = normalized_url + '/' + organization_name
    return normalized_url
