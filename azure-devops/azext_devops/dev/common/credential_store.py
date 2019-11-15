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
from .pip_helper import install_keyring

logger = get_logger(__name__)


class CredentialStore:
    def __init__(self):
        self._initialize_keyring()


    def set_password(self, key, token):
        try:
            import keyring
        except ImportError:
            install_keyring()
            self._initialize_keyring()
            import keyring

        try:
            # check for and delete existing credential
            old_token = keyring.get_password(key, self._USERNAME)
            if old_token is not None:
                keyring.delete_password(key, self._USERNAME)
            logger.debug('Setting credential: %s', key)
            keyring.set_password(key, self._USERNAME, token)
        except Exception as ex:  # pylint: disable=broad-except
            # store credentials in azuredevops config directory if keyring is missing or malfunctioning
            if sys.platform.startswith(self._LINUX_PLATFORM):
                logger.warning('Failed to store PAT using keyring; falling back to file storage.')
                logger.warning('You can clear the stored credential by running az devops logout.')
                logger.warning('Refer https://aka.ms/azure-devops-cli-auth to know more on sign in with PAT.')
                logger.debug('Keyring failed. ERROR :%s', ex)
                logger.debug('Storing credentials in the file: %s', self._PAT_FILE)
                creds_list = self._get_credentials_list()
                if key not in creds_list.sections():
                    creds_list.add_section(key)
                    logger.debug('Added new entry to PAT file : %s ', key)
                creds_list.set(key, self._USERNAME, token)
                self._commit_change(creds_list)
            else:
                raise CLIError(ex)

    def get_password(self, key):
        try:
            import keyring
        except ImportError:
            return None
        try:
            token = keyring.get_password(key, self._USERNAME)
        except Exception as ex:  # pylint: disable=broad-except
            # fetch credentials from file if keyring is missing or malfunctioning
            if sys.platform.startswith(self._LINUX_PLATFORM):
                token = None
            else:
                raise CLIError(ex)
        # look for credential in file too for linux if token is None
        if token is None and sys.platform.startswith(self._LINUX_PLATFORM):
            token = self.get_PAT_from_file(key)
        return token

    def clear_password(self, key):
        try:
            import keyring
        except ImportError:
            install_keyring()
            self._initialize_keyring()
            import keyring
        if sys.platform.startswith(self._LINUX_PLATFORM):
            keyring_token = None
            file_token = None
            try:
                keyring_token = keyring.get_password(key, self._USERNAME)
                if keyring_token:
                    keyring.delete_password(key, self._USERNAME)
            except Exception as ex:  # pylint: disable=broad-except
                logger.debug("%s", ex)
                file_token = self.get_PAT_from_file(key)
                if file_token:
                    self.delete_PAT_from_file(key)
            if(keyring_token is None and file_token is None):
                raise CLIError(self._CRDENTIAL_NOT_FOUND_MSG)
        else:
            try:
                keyring.delete_password(key, self._USERNAME)
            except keyring.errors.PasswordDeleteError:
                raise CLIError(self._CRDENTIAL_NOT_FOUND_MSG)
            except RuntimeError as ex:  # pylint: disable=broad-except
                raise CLIError(ex)

    def get_PAT_from_file(self, key):
        ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
        logger.debug('Keyring not configured properly or package not found.'
                'Looking for credentials with key:%s in the file: %s', key, self._PAT_FILE)
        creds_list = self._get_credentials_list()
        try:
            return creds_list.get(key, self._USERNAME)
        except (configparser.NoOptionError, configparser.NoSectionError):
            return None

    def delete_PAT_from_file(self, key):
        logger.debug('Keyring not configured properly or package not found.'
                     'Looking for credentials with key:%s in the file: %s', key, self._PAT_FILE)
        creds_list = self._get_credentials_list()
        if key not in creds_list.sections():
            raise CLIError(self._CRDENTIAL_NOT_FOUND_MSG)
        creds_list.remove_section(key)
        self._commit_change(creds_list)

    @staticmethod
    def _get_config_parser():
        if sys.version_info.major == 3:
            return configparser.ConfigParser(interpolation=None)
        return configparser.ConfigParser()

    @staticmethod
    def _get_credentials_list():
        try:
            credential_list = CredentialStore._get_config_parser()
            credential_list.read(CredentialStore._PAT_FILE)
            return credential_list
        except BaseException:  # pylint: disable=broad-except
            return CredentialStore._get_config_parser()

    @staticmethod
    def _commit_change(credential_list):
        with open(CredentialStore._PAT_FILE, 'w+') as creds_file:
            credential_list.write(creds_file)

    @staticmethod
    def _initialize_keyring():
        try:
            import keyring
        except ImportError:
            return

        def _only_builtin(backend):
            return (
                backend.__module__.startswith('keyring.backends.') and
                'chain' not in backend.__module__
            )

        keyring.core.init_backend(_only_builtin)
        logger.debug('Keyring backend : %s', keyring.get_keyring())

    # a value is required for the python config file that gets generated on some operating systems.
    _USERNAME = 'Personal Access Token'
    _LINUX_PLATFORM = 'linux'
    _PAT_FILE = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'personalAccessTokens')
    _CRDENTIAL_NOT_FOUND_MSG = 'The credential was not found'
