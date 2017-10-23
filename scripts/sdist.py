# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys
import glob
import os
from subprocess import check_call, CalledProcessError

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
os.chdir(root_dir)


def exec_command(command, cwd):
    try:
        print('CWD: ' + cwd)
        print('Executing: ' + command)
        check_call(command.split(), cwd=cwd)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


setup_files = [setup_file for root, dirs, files in os.walk(root_dir)
               for setup_file in glob.glob(os.path.join(root, 'setup.py'))]

# sdist packages
for file in setup_files:
    exec_command('python setup.py sdist', os.path.dirname(file))
