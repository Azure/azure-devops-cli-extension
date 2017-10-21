# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import keyring
import logging
import os


from vsts._file_cache import get_cache


try:
    from azure.cli.core.util import CLIError
except ImportError:
    from knack.util import CLIError


def get_credential(team_instance):
    service_name = _get_service_name(team_instance)
    try:
        token = keyring.get_password(service_name, _username)
        _transfer_file_storage_to_keyring()
        if token is not None:
            return token
        else:
            return keyring.get_password(service_name, _username)
    except RuntimeError as e:
        logging.exception(e)
        if _credentials_cache[team_instance]:
            return _credentials_cache[team_instance]
        else:
            return None


def set_credential(team_instance, token):
    try:
        keyring.set_password(_get_service_name(team_instance), _username, token)
    except RuntimeError as e:
        logging.exception(e)
        team_instance = normalize_url_for_key(team_instance)
        _credentials_cache[team_instance] = token


def clear_credential(team_instance):
    service_name = _get_service_name(team_instance)
    try:
        keyring.delete_password(service_name, _username)
    except keyring.errors.PasswordDeleteError as e:
        logging.exception(e)
        team_instance = normalize_url_for_key(team_instance)
        if _credentials_cache[team_instance]:
            del _credentials_cache[team_instance]
        else:
            raise CLIError('The credential was not found')


def _get_service_name(team_instance):
    return 'vsts-cli:' + normalize_url_for_key(team_instance)


def normalize_url_for_key(url):
    if url.endswith('/'):
        url = url[:-1]
    url = url.lower()
    return url


def _transfer_file_storage_to_keyring():
    if os.path.exists(_credentials_cache.file_name):
        try:
            for entry in _credentials_cache:
                logging.info('Moving token to keyring for team instance: ' + entry)
                if keyring.get_password(_get_service_name(entry), _username) is None:
                    set_credential(entry, _credentials_cache[entry])
        finally:
            logging.info('Deleting old token file: ' + _credentials_cache.file_name)
            os.remove(_credentials_cache.file_name)

_credentials_cache = get_cache('tokens', 0)

# a value is required for the python config file that gets generated on some operating systems.
_username = 'Personal Access Token'
