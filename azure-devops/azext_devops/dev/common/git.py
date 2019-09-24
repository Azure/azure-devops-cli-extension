# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import subprocess
import sys

from knack.log import get_logger
from knack.util import CLIError
from .uri import uri_parse

logger = get_logger(__name__)

_GIT_EXE = 'git'


def set_config(key, value, local=True):
    scope = _get_git_config_scope_arg(local)
    subprocess.check_output([_GIT_EXE, 'config', scope, key, value])


def unset_config(key, local=True):
    scope = _get_git_config_scope_arg(local)
    subprocess.check_output([_GIT_EXE, 'config', scope, '--unset', key])


def get_config(key, local=True):
    scope = _get_git_config_scope_arg(local)
    return subprocess.check_output([_GIT_EXE, 'config', scope, key])


def _get_git_config_scope_arg(local):
    if local:
        return '--local'
    return '--global'


def fetch_remote_and_checkout(refName, remote_name):
    subprocess.run([_GIT_EXE, 'fetch', remote_name, refName], check=False)
    subprocess.run([_GIT_EXE, 'checkout', get_branch_name_from_ref(refName)], check=False)
    subprocess.run([_GIT_EXE, 'pull', remote_name, get_branch_name_from_ref(refName)], check=False)


def get_current_branch_name():
    try:
        output = subprocess.check_output([_GIT_EXE, 'symbolic-ref', '--short', '-q', 'HEAD'])
    except BaseException as ex:  # pylint: disable=broad-except
        logger.info('GitDetect: Could not detect current branch based on current working directory.')
        logger.debug(ex, exc_info=True)
        return None
    if sys.stdout.encoding is not None:
        result = output.decode(sys.stdout.encoding)
    else:
        result = output.decode()
    return result.strip()


def get_remote_url(validation_function=None):
    remotes = get_git_remotes()
    if remotes is not None:
        if _ORIGIN_PUSH_KEY in remotes and (validation_function is None or
                                            validation_function(remotes[_ORIGIN_PUSH_KEY])):
            return remotes[_ORIGIN_PUSH_KEY]
        for k, value in remotes.items():
            if k != _ORIGIN_PUSH_KEY and k.endswith('(push)') and (validation_function is None or
                                                                   validation_function(value)):
                return value
    return None


def get_git_credentials(organization):
    parse_result = uri_parse(organization)
    protocol = parse_result.scheme
    host = parse_result.netloc
    standard_in = bytes('protocol={protocol}\nhost={host}'.format(protocol=protocol, host=host), 'utf-8')
    try:
        # pylint: disable=unexpected-keyword-arg
        output = subprocess.check_output([_GIT_EXE, 'credential-manager', 'get'], input=standard_in)
    except BaseException as ex:  # pylint: disable=broad-except
        logger.info('GitDetect: Could not detect git credentials for current working directory.')
        logger.debug(ex, exc_info=True)
        return None
    if sys.stdout.encoding is not None:
        lines = output.decode(sys.stdout.encoding).split('\n')
    else:
        lines = output.decode().split('\n')
    properties = {}
    for line in lines:
        equal_position = line.find('=')
        if equal_position >= 0:
            properties[line[0:equal_position]] = line[equal_position + 1:]
    return properties


def get_git_remotes():
    if _git_remotes:
        return _git_remotes
    try:
        # Example output:
        # git remote - v
        # full  https://mseng.visualstudio.com/DefaultCollection/VSOnline/_git/_full/VSO (fetch)
        # full  https://mseng.visualstudio.com/DefaultCollection/VSOnline/_git/_full/VSO (push)
        # origin  https://mseng.visualstudio.com/defaultcollection/VSOnline/_git/VSO (fetch)
        # origin  https://mseng.visualstudio.com/defaultcollection/VSOnline/_git/VSO (push)
        output = subprocess.check_output([_GIT_EXE, 'remote', '-v'], stderr=subprocess.STDOUT)
    except BaseException as ex:  # pylint: disable=broad-except
        logger.info('GitDetect: Could not detect current remotes based on current working directory.')
        logger.debug(ex, exc_info=True)
        return None
    if sys.stdout.encoding is not None:
        lines = output.decode(sys.stdout.encoding).split('\n')
    else:
        lines = output.decode().split('\n')
    for line in lines:
        components = line.strip().split()
        if len(components) == 3:
            _git_remotes[components[0] + components[2]] = components[1]
    return _git_remotes


def resolve_git_refs(ref):
    """Prepends 'refs/' prefix to ref str if not already there.
    :param str ref: The text to validate.
    :rtype: str
    """
    if ref is not None and not ref.startswith(REFS_PREFIX):
        ref = REFS_PREFIX + ref
    return ref


def get_ref_name_from_ref(ref):
    """Removes 'refs/' prefix from ref str if there.
    :param ref: The text to validate.
    :type ref: str
    :rtype: str
    """
    if ref is not None and ref.startswith(REFS_PREFIX):
        ref = ref[len(REFS_PREFIX):]
    return ref


def resolve_git_ref_heads(ref):
    """Prepends 'refs/heads/' prefix to ref str if not already there.
    :param ref: The text to validate.
    :type ref: str
    :rtype: str
    """
    if ref is not None and not ref.startswith(REF_HEADS_PREFIX) and not ref.startswith(REF_PULL_PREFIX):
        ref = REF_HEADS_PREFIX + ref
    return ref


def get_branch_name_from_ref(ref):
    """Removes 'refs/heads/' prefix from ref str if there.
    :param ref: The text to validate.
    :type ref: str
    :rtype: str
    """
    if ref is not None and ref.startswith(REF_HEADS_PREFIX):
        ref = ref[len(REF_HEADS_PREFIX):]
    return ref


def setup_git_alias(alias, command, local=False):
    try:
        set_config(key=_get_alias_key(alias),
                   value=_get_alias_value(command),
                   local=local)
    except OSError:
        raise CLIError('Setting the git alias failed. Ensure git is installed and in your path.')


def clear_git_alias(alias, local=False):
    unset_config(key=_get_alias_key(alias), local=local)


def is_git_alias_setup(alias, command, local=False):
    try:
        try:
            value = get_config(key=_get_alias_key(alias), local=local)
        except subprocess.CalledProcessError:
            return False
        return _get_alias_value(command) == value.decode(sys.stdout.encoding).strip()
    except OSError:
        raise CLIError('Checking the git config values failed. Ensure git is installed and in your path.')


def _get_alias_key(alias):
    return 'alias.' + alias


def _get_alias_value(command):
    mime = '.cmd' if sys.platform.lower().startswith('win') else ''
    return '!f() { exec az' + mime + ' ' + command + ' \"$@\"; }; f'


_git_remotes = {}
_ORIGIN_PUSH_KEY = 'origin(push)'
REFS_PREFIX = 'refs/'
REF_HEADS_PREFIX = 'refs/heads/'
REF_PULL_PREFIX = 'refs/pull/'
GIT_CREDENTIALS_USERNAME_KEY = 'username'
GIT_CREDENTIALS_PASSWORD_KEY = 'password'
