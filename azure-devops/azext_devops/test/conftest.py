# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import sys
from azure.cli.core.extension import get_extension_path
# Make sure that the extension install directory is on sys.path so that dependencies can be found.

extensionPath = get_extension_path('azure-devops')
sys.path.append(extensionPath)
