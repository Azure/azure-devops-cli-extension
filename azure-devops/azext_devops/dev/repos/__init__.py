# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pkg_resources
from ._help import load_repos_help

pkg_resources.declare_namespace(__name__)

load_repos_help()
