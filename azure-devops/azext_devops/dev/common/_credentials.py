# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from knack.log import get_logger
from knack.util import CLIError
from .uri import uri_parse
from .credential_store import CredentialStore
from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR

logger = get_logger(__name__)


def get_credential(devops_organization, fall_back_to_default=True):
    token = _get_credential(devops_organization)
    if token is None and devops_organization is not None and fall_back_to_default:
        token = _get_credential(devops_organization=None)
    return token


def _get_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Getting credential: %s', key)
    cred_store = CredentialStore()
    return cred_store.get_password(key)


def set_credential(devops_organization, token):
    key = _get_service_name(devops_organization)
    cred_store = CredentialStore()
    cred_store.set_password(key, token)

    if os.path.isfile(ORGANIZATION_LIST_FILE):
        # No need to add organization if it's already present.
        with open(ORGANIZATION_LIST_FILE, 'r') as org_list:
            for organization in org_list:
                if key == organization.rstrip():
                    return
    with open(ORGANIZATION_LIST_FILE, 'a+') as org_list:
        org_list.write(key + "\n")


def clear_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Clearing credential: %s', key)
    cred_store = CredentialStore()

    if key == _DEFAULT_CREDENTIAL_KEY:
        # remove all organizations and delete the file
        if os.path.isfile(ORGANIZATION_LIST_FILE):
            with open(ORGANIZATION_LIST_FILE) as org_list_file:
                for organization in org_list_file:
                    cred_store.clear_password(organization.rstrip())
            os.remove(ORGANIZATION_LIST_FILE)
        else:
            raise CLIError('No credentials were found.')
    else:
        # delete particular organization from the list
        if os.path.isfile(ORGANIZATION_LIST_FILE):
            with open(ORGANIZATION_LIST_FILE, "r") as input_file:
                orgs = input_file.readlines()
            with open(ORGANIZATION_LIST_FILE, "w") as output_file:
                for line in orgs:
                    if line.rstrip() != key:
                        output_file.write(line)
        cred_store.clear_password(key)


def _get_service_name(devops_organization):
    if devops_organization is not None:
        return 'azdevops-cli:' + normalize_url_for_key(devops_organization)
    return _DEFAULT_CREDENTIAL_KEY


def normalize_url_for_key(url):
    components = uri_parse(url)
    normalized_url = components.scheme.lower() + '://' + components.netloc.lower()
    organization_name = components.path.lower()
    if(organization_name and ('visualstudio.com' not in url.lower())):
        organization_name = organization_name.split('/')[1]
        normalized_url = normalized_url + '/' + organization_name
    return normalized_url


_DEFAULT_CREDENTIAL_KEY = 'azdevops-cli: default'
ORGANIZATION_LIST_FILE = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'organization_list')
