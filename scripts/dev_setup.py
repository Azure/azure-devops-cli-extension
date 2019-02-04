# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from .script_utils import exec_command, AZURE_CONFIG_DIR, EXTENSION_DIR, COMMAND_UPGRADE_PIP

# install general requirements and azure-cli
exec_command(COMMAND_UPGRADE_PIP)

# install to edge build of azure-cli
exec_command(
    'pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge --no-cache-dir')

os.environ['AZURE_EXTENSION_DIR'] = os.path.join(AZURE_CONFIG_DIR, 'devcliextensions')

exec_command('pip install -e {}'.format(EXTENSION_DIR))
exec_command(
    'pip install --upgrade --target {0}/devcliextensions/azure-devops {1}'.format(AZURE_CONFIG_DIR, EXTENSION_DIR))

print('Finished dev setup.')
