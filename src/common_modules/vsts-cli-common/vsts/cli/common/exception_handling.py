# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging


from knack.util import CLIError
from vsts.exceptions import VstsAuthenticationError
from .vsts import raise_authentication_error


def handle_command_exception(exception):
    logging.exception(exception)
    if isinstance(exception, CLIError):
        raise exception
    if isinstance(exception, VstsAuthenticationError):
        raise_authentication_error(exception)
    raise CLIError(exception)
