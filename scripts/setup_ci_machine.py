# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from .script_utils import exec_command, install_python_packages, COMMAND_UPGRADE_PIP

def setup_ci_machine():
    exec_command(COMMAND_UPGRADE_PIP)
    install_python_packages([
        'wheel',
        'pytest',
        'coverage',
        'pytest-cov',
        'pip install --pre azure-cli --extra-index-url https://azurecliprod.blob.core.windows.net/edge'
        'git+https://github.com/Azure/azure-cli@master#egg=azure-cli-testsdk&subdirectory=src/azure-cli-testsdk -q'
        ])
    exec_command('az -h')
    exec_command('az devops -h')

if __name__ == "__main__":
    setup_ci_machine()
