# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from vsts.exceptions import VstsAuthenticationError

from .services import raise_authentication_error

logger = get_logger(__name__)

def handle_command_exception(exception):
    if isinstance(exception, CLIError):
        raise exception
    if isinstance(exception, VstsAuthenticationError):
        raise_authentication_error(exception)
    logger.exception(exception)
    raise CLIError(exception)
