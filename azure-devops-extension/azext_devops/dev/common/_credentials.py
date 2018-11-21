# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
from knack.config import CLIConfig
from knack.util import CLIError, ensure_dir
from six.moves import configparser
from .uri import uri_parse

from knack.log import get_logger
logger = get_logger(__name__)

from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR
_PAT_FILE = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'personalAccessTokens')

def get_credential(devops_organization, fall_back_to_default=True):
    token = _get_credential(devops_organization)
    if token is None and devops_organization is not None and fall_back_to_default:
        token = _get_credential(devops_organization=None)
    return token


def _get_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Getting credential: %s', key)
    try:
        import keyring
        return keyring.get_password(key, _USERNAME)
    except RuntimeError as ex:
        #fetch credentials from file if keyring is missing
        if sys.platform.startswith(_LINUX_PLATFORM):
            ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
            logger.debug('Keyring package not found. Fetching credentials from the file: %s', _PAT_FILE)
            creds_list = _get_credentials_list()
            try:
                return creds_list.get(key, _USERNAME)
            except (configparser.NoOptionError, configparser.NoSectionError):
                return None
        else:
            raise CLIError(ex)

def set_credential(devops_organization, token):
    try:
        key = _get_service_name(devops_organization)
        import keyring      
        # check for and delete existing credential
        old_token = keyring.get_password(key, _USERNAME)
        if old_token is not None:
            keyring.delete_password(key, _USERNAME)
        logger.debug('Setting credential: %s', key)
        keyring.set_password(key, _USERNAME, token)
    except RuntimeError as ex:
        #store credentials in azuredevops config directory if keyring is missing
        if sys.platform.startswith(_LINUX_PLATFORM):
            logger.debug('Keyring package not found. Hence, storing credentials in the file: %s', _PAT_FILE)  
            creds_list = _get_credentials_list()
            if key not in creds_list.sections():
                creds_list.add_section(key)
                logger.debug('Added new entry to PAT file : %s ',key)
            creds_list.set(key, _USERNAME, token)
            _commit_change(creds_list)
        else:
            raise CLIError(ex)


def clear_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Clearing credential: %s', key)
    try:
        import keyring
        keyring.delete_password(key, _USERNAME)
    except keyring.errors.PasswordDeleteError as ex:
        raise CLIError('The credential was not found')
    except RuntimeError as ex :        
        if sys.platform.startswith(_LINUX_PLATFORM):
            logger.debug('Keyring package not found. Checking file for credentials: %s', _PAT_FILE)
            creds_list = _get_credentials_list()
            if key not in creds_list.sections():
                    raise CLIError('The credential was not found')
            creds_list.remove_section(key)
            _commit_change(creds_list)
        else:
            raise CLIError(ex)


def _get_service_name(devops_organization):
    if devops_organization is not None:
        return 'azdevops-cli:' + normalize_url_for_key(devops_organization)
    else:
        return 'azdevops-cli: default'

def normalize_url_for_key(url):
    components = uri_parse(url)
    return components.scheme.lower() + '://' + components.netloc.lower()

def _get_config_parser():
    if sys.version_info.major == 3:
        return configparser.ConfigParser(interpolation=None)
    return configparser.ConfigParser()

def _get_credentials_list():
    try:
        credential_list = _get_config_parser()
        credential_list.read(_PAT_FILE)
        return credential_list
    except Exception: 
        return _get_config_parser()

def _commit_change(credential_list):
    with open(_PAT_FILE, 'w+') as creds_file:
            credential_list.write(creds_file)

# a value is required for the python config file that gets generated on some operating systems.
_USERNAME = 'Personal Access Token'
_LINUX_PLATFORM = 'linux'
