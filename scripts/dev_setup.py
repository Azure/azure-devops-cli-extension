# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys
import glob
import os
from glob import glob
from subprocess import check_call, CalledProcessError

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
os.chdir(root_dir)


def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


vsts_python_api_repo = os.environ['vsts-python-api-repo']

packages = []
if os.path.isdir(vsts_python_api_repo):
    packages.append(vsts_python_api_repo + "/vsts")
packages.append(root_dir + "/src/common_modules/vsts-cli-common")
packages.extend(os.path.dirname(p) for p in glob('src/common_modules/vsts-cli*/setup.py') if 'vsts-cli-common' not in p)
packages.extend(os.path.dirname(p) for p in glob('src/command_modules/vsts-cli*/setup.py'))
packages.append(root_dir + "/src/vsts-cli")

# Extract nspkg and sort nspkg by number of "-"
nspkg_packages = [p for p in packages if "nspkg" in p]
nspkg_packages.sort(key=lambda x: len([c for c in x if c == '-']))

content_packages = [p for p in packages if p not in nspkg_packages]

print('Running dev setup...')
print('Root directory \'{}\'\n'.format(root_dir))

# install general requirements
if os.path.isfile('./requirements.txt'):
    exec_command('pip install -r requirements.txt')

# install packages
for package_list in [nspkg_packages, content_packages]:
    for package_name in package_list:
        exec_command('pip install -e {}'.format(package_name))

# install packaging requirements
if os.path.isfile('./scripts/packaging_requirements.txt'):
    exec_command('pip install -r scripts/packaging_requirements.txt')
