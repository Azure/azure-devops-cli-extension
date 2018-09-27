# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pkg_resources
pkg_resources.declare_namespace(__name__)

from ._help import load_boards_help

import knack.help # pylint: disable=unused-import


def load_params(_):
    import knack.arguments # pylint: disable=redefined-outer-name


def load_commands():
    import knack.commands # pylint: disable=redefined-outer-name

load_boards_help()