# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azdos._file_cache import get_cache, DEFAULT_MAX_AGE


def _get_cache_dir():
    azdos_config_dir = os.getenv('VSTS_CACHE_DIR', None) or os.path.expanduser(os.path.join('~', '.azdos', 'cli',
                                                                                           'cache'))
    if not os.path.exists(azdos_config_dir):
        os.makedirs(azdos_config_dir)
    return azdos_config_dir


DEFAULT_CACHE_DIR = _get_cache_dir()


def get_cli_cache(name, max_age=DEFAULT_MAX_AGE, cache_dir=DEFAULT_CACHE_DIR):
    return get_cache(name, max_age, cache_dir)
