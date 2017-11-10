# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import os
import keyring

from knack.util import CLIError
from vsts._file_cache import get_cache
from .uri import uri_parse


def get_credential(team_instance):
    key = _get_service_name(team_instance)
    logging.debug('Getting credential: %s', key)
    try:
        token = keyring.get_password(key, _USERNAME)
        _transfer_file_storage_to_keyring()
        if token is not None:
            return token
        else:
            token = keyring.get_password(key, _USERNAME)
            if token is not None:
                return token
            else:
                logging.debug('Getting default credential')
                return keyring.get_password(_get_service_name(team_instance=None), _USERNAME)
    except RuntimeError as ex:
        logging.exception(ex)
        raise CLIError(ex)


def set_credential(team_instance, token):
    try:
        key = _get_service_name(team_instance)

        # check for and delete existing credential
        old_token = keyring.get_password(key, _USERNAME)
        if old_token is not None:
            keyring.delete_password(key, _USERNAME)

        logging.debug('Setting credential: %s', key)
        keyring.set_password(key, _USERNAME, token)
    except RuntimeError as ex:
        logging.exception(ex)
        raise CLIError(ex)


def clear_credential(team_instance):
    key = _get_service_name(team_instance)
    logging.debug('Clearing credential: %s', key)
    try:
        keyring.delete_password(key, _USERNAME)
    except keyring.errors.PasswordDeleteError as ex:
        logging.exception(ex)
        raise CLIError('The credential was not found')


def _get_service_name(team_instance):
    if team_instance is not None:
        return 'vsts-cli:' + normalize_url_for_key(team_instance)
    else:
        return 'vsts-cli: default'


def normalize_url_for_key(url):
    components = uri_parse(url)
    return components.scheme.lower() + '://' + components.netloc.lower()


def _transfer_file_storage_to_keyring():
    old_cache_dir = os.getenv('VSTS_CACHE_DIR', None) or os.path.expanduser(
            os.path.join('~', '.vsts', 'cache'))
    if os.path.exists(old_cache_dir):
        credentials_cache = get_cache('tokens', 0, old_cache_dir)
        if os.path.exists(credentials_cache.file_name):
            try:
                for entry in credentials_cache:
                    logging.info('Moving token to keyring for instance: %s', entry)
                    if keyring.get_password(_get_service_name(entry), _USERNAME) is None:
                        set_credential(entry, credentials_cache[entry])
            finally:
                logging.info('Deleting old token file: %s', credentials_cache.file_name)
                os.remove(credentials_cache.file_name)


# a value is required for the python config file that gets generated on some operating systems.
_USERNAME = 'Personal Access Token'
