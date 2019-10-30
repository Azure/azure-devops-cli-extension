# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
from knack.util import CLIError
from knack.log import get_logger
from six.moves import configparser
from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR
from .pip_helper import install_keyring
from .config_directory_credential_store import ConfigDirectoryCredentialStore

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
        except RuntimeError as ex:
            # store credentials in azuredevops config directory if keyring is missing
            if sys.platform.startswith(self._LINUX_PLATFORM):
                ConfigDirectoryCredentialStore.set_password(key, token)
            else:
                raise CLIError(ex)

    def get_password(self, key):
        try:
            import keyring
        except ImportError:
            return None

        try:
            return keyring.get_password(key, self._USERNAME)
        except Exception as ex:  # pylint: disable=broad-except
            # fetch credentials from file if keyring has issues
            cred = ConfigDirectoryCredentialStore.get_password(key)
            if cred is None:
                raise CLIError(ex)

    def clear_password(self, key):
        try:
            import keyring
        except ImportError:
            install_keyring()
            self._initialize_keyring()
            import keyring

        try:
            keyring.delete_password(key, self._USERNAME)
        except keyring.errors.PasswordDeleteError:
            raise CLIError('The credential was not found')
        except RuntimeError as ex:
            if sys.platform.startswith(self._LINUX_PLATFORM):
                ConfigDirectoryCredentialStore.clear_password(key)
            else:
                raise CLIError(ex)

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
