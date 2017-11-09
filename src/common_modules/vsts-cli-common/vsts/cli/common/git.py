# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import subprocess
import sys
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


try:
    from azure.cli.core.util import CLIError
except ImportError:
    from knack.util import CLIError


def set_config(key, value, local=True):
    if local:
        scope = '--local'
    else:
        scope = '--global'
    subprocess.check_output(['git', 'config', scope, key, value])


def unset_config(key, local=True):
    if local:
        scope = '--local'
    else:
        scope = '--global'
    subprocess.check_output(['git', 'config', scope, '--unset', key])


def get_config(key, local=True):
    if local:
        scope = '--local'
    else:
        scope = '--global'
    return subprocess.check_output(['git', 'config', scope, key])


def get_current_branch_name():
    try:
        output = subprocess.check_output(['git', 'symbolic-ref', '--short', '-q', 'HEAD'])
    except subprocess.CalledProcessError as ex:
        logging.info('GitDetect: Could not detect current branch based on current working directory.')
        logging.exception(ex)
        return None
    return output.decode(sys.stdout.encoding).strip()


def get_remote_url(validation_function=None):
    remotes = get_git_remotes()
    if remotes is not None:
        if _ORIGIN_PUSH_KEY in remotes and (validation_function is None
                                            or validation_function(remotes[_ORIGIN_PUSH_KEY])):
            return remotes[_ORIGIN_PUSH_KEY]
        for k, value in remotes.items():
            if k != _ORIGIN_PUSH_KEY and k.endswith('(push)') and (validation_function is None
                                                                   or validation_function(value)):
                return value
    return None


def get_git_credentials(team_instance):
    parse_result = urlparse(team_instance)
    protocol = parse_result.scheme
    host = parse_result.netloc
    standard_in = bytes('protocol={protocol}\nhost={host}'.format(protocol=protocol, host=host), 'utf-8')
    try:
        output = subprocess.check_output(['git', 'credential-manager', 'get'], input=standard_in)
    except subprocess.CalledProcessError as ex:
        logging.info('GitDetect: Could not detect git credentials for current working directory.')
        logging.exception(ex)
        return None
    lines = output.decode(sys.stdout.encoding).split(sep='\n')
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
        output = subprocess.check_output(['git', 'remote', '-v'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as ex:
        logging.info('GitDetect: Could not detect current remotes based on current working directory.')
        logging.exception(ex)
        return None
    lines = output.decode(sys.stdout.encoding).split(sep='\n')
    for line in lines:
        components = line.strip().split()
        if len(components) == 3:
            _git_remotes[components[0] + components[2]] = components[1]
    return _git_remotes


def resolve_git_ref_heads(ref):
    """Prepends 'refs/heads/' prefix to ref str if not already there.
    :param ref: The text to validate.
    :type ref: str
    :rtype: str
    """
    if ref is not None and not ref.startswith(REF_HEADS_PREFIX):
        ref = REF_HEADS_PREFIX + ref
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
    return '!f() { exec vsts.cmd ' + command + ' \"$@\"; }; f'


_git_remotes = {}
_ORIGIN_PUSH_KEY = 'origin(push)'
REF_HEADS_PREFIX = 'refs/heads/'
GIT_CREDENTIALS_USERNAME_KEY = 'username'
GIT_CREDENTIALS_PASSWORD_KEY = 'password'


class GitRemote:
    """ GitRemote.
    """
    def __init__(self, name, url, direction):
        self.name = name
        self.url = url
        self.direction = direction
