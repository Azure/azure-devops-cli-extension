# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

from azure.cli.core.extension.operations import _run_pip

logger = get_logger(__name__)


def install_keyring():
    _install_package('keyring~=13.2.1')


def _install_package(package_name):
    logger.debug('installing %s', package_name)
    pip_args = ['install', package_name]
    _run_pip(pip_args)  # pylint: disable=protected-access
