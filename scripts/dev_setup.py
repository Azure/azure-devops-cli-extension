# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
from subprocess import check_call, CalledProcessError


print('Running dev setup...')

def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

# install to edge build of azure-cli
exec_command('pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge --no-cache-dir')

print('Finished dev setup.')
