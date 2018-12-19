# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pkg_resources
pkg_resources.declare_namespace(__name__)

import knack.help # pylint: disable=unused-import

from ._help import load_artifacts_help

def load_params(_):
    import knack.arguments # pylint: disable=redefined-outer-name


def load_commands():
    import knack.commands # pylint: disable=redefined-outer-name

load_artifacts_help()