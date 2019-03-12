# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

from azext_devops.dev.common.services import (get_extension_client,
                                              resolve_instance)
from azext_devops.dev.common.arguments import resolve_true_false

logger = get_logger(__name__)


def list_extensions(include_built_in='true', include_disabled='true', organization=None, detect=None):
    """ List extensions installed in an organization
    """
    include_built_in = resolve_true_false(include_built_in)
    include_disabled = resolve_true_false(include_disabled)
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    extensions = extension_client.get_installed_extensions(include_disabled_extensions=include_disabled)

    if not include_built_in:
        filteredResult = []
        for extension in extensions:
            if 'builtIn' not in str(extension.flags):
                filteredResult.append(extension)

        extensions = filteredResult

    return extensions


def get_extension(publisher_id, extension_id, organization=None, detect=None):
    """ Get detail of single extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.get_installed_extension_by_name(publisher_name=publisher_id,
                                                            extension_name=extension_id)


def install_extension(publisher_id, extension_id, organization=None, detect=None):
    """ Install an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.install_extension_by_name(publisher_name=publisher_id,
                                                      extension_name=extension_id)


def uninstall_extension(publisher_id, extension_id, organization=None, detect=None):
    """ Uninstall an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.uninstall_extension_by_name(publisher_name=publisher_id,
                                                        extension_name=extension_id)


def enable_extension(publisher_id, extension_id, organization=None, detect=None):
    """ Enable an extension
    """
    return _update_extension_state(disable=False,
                                   enable=True,
                                   publisher_id=publisher_id,
                                   extension_id=extension_id,
                                   organization=organization,
                                   detect=detect)


def disable_extension(publisher_id, extension_id, organization=None, detect=None):
    """ Disable an extension
    """
    return _update_extension_state(disable=True,
                                   enable=False,
                                   publisher_id=publisher_id,
                                   extension_id=extension_id,
                                   organization=organization,
                                   detect=detect)


def _update_extension_state(disable, enable,
                            publisher_id, extension_id,
                            organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    current_extension = extension_client.get_installed_extension_by_name(
        publisher_name=publisher_id,
        extension_name=extension_id)

    state_from_service = str(current_extension.install_state.flags)
    logger.info('state received from service')
    logger.info(state_from_service)

    if disable:
        flags = [x.strip() for x in state_from_service.split(',')]
        if 'disabled' in flags:
            raise CLIError('Extension is already in disabled state')
        flags.append('disabled')
        updated_state = ', '.join(flags)

    if enable:
        flags = [x.strip() for x in state_from_service.split(',')]
        if 'disabled' not in flags:
            raise CLIError('Extension is already in enabled state')
        flags.remove('disabled')
        updated_state = ', '.join(flags)

    current_extension.install_state.flags = updated_state

    return extension_client.update_installed_extension(current_extension)
