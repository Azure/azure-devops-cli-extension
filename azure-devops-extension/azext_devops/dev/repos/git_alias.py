# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.git import is_git_alias_setup, setup_git_alias, clear_git_alias


def setup_git_aliases(local=False):
    """Configure aliases for Git (to enable commands like 'git pr list')
    :param local: Sets the alias in the local git config rather than the global config.
    :type local: bool
    """
    for key in git_aliases:
        setup_git_alias(key, git_aliases[key], local=local)


def clear_git_aliases(local=False):
    """
    :param local: Checks the alias in the local git config rather than the global config.
    :type local: bool
    """
    for key in git_aliases:
        if is_git_alias_setup(key, git_aliases[key], local=local):
            clear_git_alias(alias=key, local=local)


def are_git_aliases_setup(local=False):
    """
    :param local: Checks the alias in the local git config rather than the global config.
    :type local: bool
    """
    for key in git_aliases:
        if not is_git_alias_setup(key, git_aliases[key], local=local):
            return False
    return True


git_aliases = {'pr': 'repos pr',
               'repo': 'repos repo'}
