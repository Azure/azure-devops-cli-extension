# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
import pip
from knack.util import CLIError, ensure_dir
from knack.log import get_logger
from six.moves import configparser
from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR

logger = get_logger(__name__)


class CredentialStore:
    def __init__(self):
        self._initialize_keyring()

    def set_password(self, key, token):
        try:
            import keyring
        except ImportError:
            if hasattr(pip, 'main'):
                pip.main(['install', 'keyring'])
            else:
                pip._internal.main(['install', 'keyring'])

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
                logger.debug('Keyring package not found. Hence, storing credentials in the file: %s', self._PAT_FILE)
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
            return keyring.get_password(key, self._USERNAME)
        except RuntimeError as ex:
            # fetch credentials from file if keyring is missing
            if sys.platform.startswith(self._LINUX_PLATFORM):
                ensure_dir(AZ_DEVOPS_GLOBAL_CONFIG_DIR)
                logger.debug('Keyring package not found. Fetching credentials from the file: %s', self._PAT_FILE)
                creds_list = self._get_credentials_list()
                try:
                    return creds_list.get(key, self._USERNAME)
                except (configparser.NoOptionError, configparser.NoSectionError):
                    return None
            else:
                raise CLIError(ex)

    def clear_password(self, key):
        import keyring
        try:
            keyring.delete_password(key, self._USERNAME)
        except keyring.errors.PasswordDeleteError:
            raise CLIError('The credential was not found')
        except RuntimeError as ex:
            if sys.platform.startswith(self._LINUX_PLATFORM):
                logger.debug('Keyring package not found. Checking file for credentials: %s', self._PAT_FILE)
                creds_list = self._get_credentials_list()
                if key not in creds_list.sections():
                    raise CLIError('The credential was not found')
                creds_list.remove_section(key)
                self._commit_change(creds_list)
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
        except BaseException:
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
