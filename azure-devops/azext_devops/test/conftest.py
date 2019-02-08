# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import sys, os
from azure.cli.core.extension import get_extension_path
# Make sure that the application source directory (this directory's parent) is on sys.path.

extensionPath = get_extension_path('azure-devops')
sys.path.append(extensionPath)
