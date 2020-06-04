# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
from subprocess import check_output, STDOUT, CalledProcessError

from knack.log import get_logger
from knack.util import CLIError

from azure.cli.core.extension import get_extension_path

logger = get_logger(__name__)


def install_keyring():
    _install_package('keyring~=17.1.1')


def _run_pip(pip_exec_args):
    cmd = [sys.executable, '-m', 'pip'] + pip_exec_args + ['-vv', '--disable-pip-version-check', '--no-cache-dir']
    logger.debug('Running: %s', cmd)
    try:
        log_output = check_output(cmd, stderr=STDOUT, universal_newlines=True)
        logger.debug(log_output)
        returncode = 0
    except CalledProcessError as e:
        logger.debug(e.output)
        logger.debug(e)
        returncode = e.returncode
    return returncode


def _install_package(package_name):
    logger.debug('installing %s', package_name)
    extensionPath = get_extension_path('azure-devops')
    pip_args = ['install', package_name, '--target', extensionPath]
    pip_status_code = _run_pip(pip_args)  # pylint: disable=protected-access
    if pip_status_code > 0:
        raise CLIError('An error occurred. Pip failed with status code {} for package {}. '
                       'Use --debug for more information.'.format(pip_status_code, package_name))
