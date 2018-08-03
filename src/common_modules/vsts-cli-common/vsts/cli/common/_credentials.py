# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import keyring

from knack.util import CLIError
from .uri import uri_parse

from knack.log import get_logger
logger = get_logger(__name__)

#
# IMPORTANT: This function is called by the install script (scripts/curl_install/install.py)
#            to verify that credentials can be accessed. Be careful when changing this method
#            so it does not impact install.
#
def get_credential(team_instance, fall_back_to_default=True):
    token = _get_credential(team_instance)
    if token is None and team_instance is not None and fall_back_to_default:
        token = _get_credential(team_instance=None)
    return token


def _get_credential(team_instance):
    key = _get_service_name(team_instance)
    logger.debug('Getting credential: %s', key)
    try:
        return keyring.get_password(key, _USERNAME)
    except RuntimeError as ex:
        logger.exception(ex)
        raise CLIError(ex)


def set_credential(team_instance, token):
    try:
        key = _get_service_name(team_instance)

        # check for and delete existing credential
        old_token = keyring.get_password(key, _USERNAME)
        if old_token is not None:
            keyring.delete_password(key, _USERNAME)

        logger.debug('Setting credential: %s', key)
        keyring.set_password(key, _USERNAME, token)
    except RuntimeError as ex:
        logger.exception(ex)
        raise CLIError(ex)


def clear_credential(team_instance):
    key = _get_service_name(team_instance)
    logger.debug('Clearing credential: %s', key)
    try:
        keyring.delete_password(key, _USERNAME)
    except keyring.errors.PasswordDeleteError as ex:
        logger.exception(ex)
        raise CLIError('The credential was not found')


def _get_service_name(team_instance):
    if team_instance is not None:
        return 'vsts-cli:' + normalize_url_for_key(team_instance)
    else:
        return 'vsts-cli: default'


def normalize_url_for_key(url):
    components = uri_parse(url)
    return components.scheme.lower() + '://' + components.netloc.lower()


# a value is required for the python config file that gets generated on some operating systems.
_USERNAME = 'Personal Access Token'
