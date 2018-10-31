#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
import os
from subprocess import check_call, CalledProcessError

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))

print('Running dev setup...')
print('Root directory \'{}\'\n'.format(root_dir))

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

exec_command('pip install -r requirements.txt')

# upgrade to latest az-dev-cli
exec_command('pip install --upgrade .')
#exec_command('pip install wheel')
