# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from azext_devops.vstsCompressed.exceptions import VstsServiceError

logger = get_logger(__name__)

def azure_devops_exception_handler(ex):
    if isinstance(ex, VstsServiceError):
        logger.debug('handling vsts service error')
        raise CLIError(ex)
    else:
        logger.debug('handling generic error')
