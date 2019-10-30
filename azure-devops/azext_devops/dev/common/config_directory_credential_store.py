# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
from knack.util import CLIError, ensure_dir
from knack.log import get_logger
from six.moves import configparser
from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR

logger = get_logger(__name__)


class ConfigDirectoryCredentialStore:
    @staticmethod
    def set_password(key, token):
        ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
        logger.debug('storing credentials in the file: : %s ', ConfigDirectoryCredentialStore._PAT_FILE)
        creds_list = ConfigDirectoryCredentialStore._get_credentials_list()
        if key not in creds_list.sections():
            creds_list.add_section(key)
            logger.debug('Added new entry to PAT file : %s ', key)
        creds_list.set(key, ConfigDirectoryCredentialStore._USERNAME, token)
        ConfigDirectoryCredentialStore._commit_change(creds_list)

    @staticmethod
    def get_password(key):
        ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
        logger.debug('getting credentials from the file: : %s ', ConfigDirectoryCredentialStore._PAT_FILE)
        creds_list = ConfigDirectoryCredentialStore._get_credentials_list()
        try:
            return creds_list.get(key, ConfigDirectoryCredentialStore._USERNAME)
        except (configparser.NoOptionError, configparser.NoSectionError):
            return None

    @staticmethod
    def clear_password(key):
        ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
        logger.debug('clearing credentials from the file: : %s ', ConfigDirectoryCredentialStore._PAT_FILE)
        creds_list = ConfigDirectoryCredentialStore._get_credentials_list()
        if key not in creds_list.sections():
            raise CLIError('The credential was not found')
        creds_list.remove_section(key)
        ConfigDirectoryCredentialStore._commit_change(creds_list)

    @staticmethod
    def get_pat_file():
        return ConfigDirectoryCredentialStore._PAT_FILE

    @staticmethod
    def _get_config_parser():
        if sys.version_info.major == 3:
            return configparser.ConfigParser(interpolation=None)
        return configparser.ConfigParser()

    @staticmethod
    def _get_credentials_list():
        try:
            credential_list = ConfigDirectoryCredentialStore._get_config_parser()
            credential_list.read(ConfigDirectoryCredentialStore._PAT_FILE)
            return credential_list
        except BaseException:  # pylint: disable=broad-except
            return ConfigDirectoryCredentialStore._get_config_parser()

    @staticmethod
    def _commit_change(credential_list):
        with open(ConfigDirectoryCredentialStore._PAT_FILE, 'w+') as creds_file:
            credential_list.write(creds_file)

    # a value is required for the python config file that gets generated on some operating systems.
    _USERNAME = 'Personal Access Token'
    _PAT_FILE = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'personalAccessTokens')
