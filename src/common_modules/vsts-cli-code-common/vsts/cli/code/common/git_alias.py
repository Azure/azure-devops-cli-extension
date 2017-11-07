# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.cli.common.git import setup_git_alias


def setup_git_aliases(local=False):
    """Configure aliases for Git (to enable commands like 'git pr list')
    :param local: Sets the alias in the local git config rather than the global config.
    :type local: bool
    """
    setup_git_alias('pr', 'code pr', local=local)
    setup_git_alias('repo', 'code repo', local=local)
