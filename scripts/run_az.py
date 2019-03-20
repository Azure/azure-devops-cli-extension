# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from azure.cli import __main__ as cli_main

# If import here is failing then it means you need to install azure cli core in machine
# pip install "git+https://github.com/Azure/azure-cli@dev#egg=azure-cli-core&subdirectory=src/azure-cli-core"

sys.exit(cli_main(sys.argv))
