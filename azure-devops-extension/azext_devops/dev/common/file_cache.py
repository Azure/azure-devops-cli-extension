# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from .config import GLOBAL_CONFIG_DIR
from vsts._file_cache import get_cache, DEFAULT_MAX_AGE

from knack.util import ensure_dir

def _get_cache_dir():
    azdevops_config_dir = os.getenv('AZURE_DEVOPS_CACHE_DIR', None) or os.path.join(GLOBAL_CONFIG_DIR, 'cache')
    ensure_dir(azdevops_config_dir)
    return azdevops_config_dir


DEFAULT_CACHE_DIR = _get_cache_dir()


def get_cli_cache(name, max_age=DEFAULT_MAX_AGE, cache_dir=DEFAULT_CACHE_DIR):
    return get_cache(name, max_age, cache_dir)
