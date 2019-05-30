# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
import os
from subprocess import check_call, CalledProcessError

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
extension_dir = os.path.join(root_dir,'azure-devops')
azure_dir = os.getenv('AZURE_CONFIG_DIR', None) or os.path.expanduser(os.path.join('~', '.azure'))

print('Running dev setup...')
print('Root directory \'{}\'\n'.format(root_dir))
print('Extension directory \'{}\'\n'.format(extension_dir))
print('Azure root directory \'{}\'\n'.format(azure_dir))

def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


# install general requirements and azure-cli
exec_command('python -m pip install --upgrade pip')

# install to edge build of azure-cli
exec_command('pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge --no-cache-dir')
requirementFile = os.path.join(root_dir + "requirements.txt")
exec_command('pip install -r ' + requirementFile)
os.environ['AZURE_EXTENSION_DIR'] = os.path.join(azure_dir,'devcliextensions')

exec_command('pip install -e {}'.format(extension_dir))
exec_command('pip install --upgrade --target {0}/devcliextensions/azure-devops {1}'.format(azure_dir, extension_dir))

print('Finished dev setup.')