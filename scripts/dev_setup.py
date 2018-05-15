# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys
import os
from glob import glob
from subprocess import check_call, CalledProcessError

print('Running dev setup...')
root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
print('Root directory \'{}\'\n'.format(root_dir))
os.chdir(root_dir)


def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


exec_command('python -m pip install --upgrade pip')
exec_command('python -m pip install --upgrade wheel')

packages = []

# VSTS Python SDK package (from either local directory or latest)
if 'vsts-python-api-repo' in os.environ and os.path.isdir(os.environ['vsts-python-api-repo']):
    packages.append(os.environ['vsts-python-api-repo'] + "/vsts")
else:
    exec_command("pip install vsts --upgrade --no-cache-dir --extra-index-url https://vstscli.azurewebsites.net")

# VSTS CLI packages (from local directory)
packages.append("src/common_modules/vsts-cli-common")
packages.extend(os.path.dirname(p) for p in glob('src/common_modules/vsts-cli*/setup.py') if 'vsts-cli-common' not in p)
packages.extend(os.path.dirname(p) for p in glob('src/command_modules/vsts-cli*/setup.py'))
packages.append("src/vsts-cli")

# install general requirements
if os.path.isfile('./requirements.txt'):
    exec_command('pip install -r requirements.txt')

# install packages
exec_command('pip install -e {}'.format(' -e '.join(packages)))
