# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pip

from knack.log import get_logger

logger = get_logger(__name__)


def install_keyring():
    _install_package('keyring')

def _install_package(package_name):
    logger.debug('installing %s', package_name)
    if hasattr(pip, 'main'):
        pip.main(['install', package_name])  # pylint: disable=no-member
    else:
        pip._internal.main(['install', package_name])  # pylint: disable=protected-access
